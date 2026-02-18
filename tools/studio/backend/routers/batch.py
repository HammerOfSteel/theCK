"""Batch processing API — CSV import for bulk voice + image generation."""

import csv
import io
import asyncio
import logging
import uuid
import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import Literal

from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from backend.config import settings
from backend.services import kokoro, fal_ai, audio
from backend.services.qwen_tts import QwenTTSService
from backend.utils.rpy_parser import clean_text_for_tts

router = APIRouter(prefix="/api/batch", tags=["batch"])
logger = logging.getLogger(__name__)

# In-memory job tracking
_jobs: dict[str, dict] = {}


class BatchRow(BaseModel):
    type: Literal["voice", "image", "image_edit"]
    prompt: str
    output_path: str
    voice: str = "🇺🇸 🚺 Nicole 🎧"
    speed: float = 1.0
    model: str = "flux-dev"
    width: int = 1024
    height: int = 1024
    reference_image_url: str = ""
    strength: float = 0.75
    convert_to: str = ""  # e.g. ogg_vorbis


class BatchRequest(BaseModel):
    rows: list[BatchRow]


class BatchStatus(BaseModel):
    job_id: str
    total: int
    completed: int
    failed: int
    skipped: int = 0
    backed_up: int = 0
    status: str  # running | completed | failed | completed_with_errors
    results: list[dict]


@router.post("/parse-csv")
async def parse_csv(file: UploadFile = File(...)):
    """
    Parse a CSV file and return structured rows for preview before processing.

    Expected CSV columns:
      type, prompt, output_path, [voice, speed, model, width, height, reference_image_url, strength, convert_to]
    """
    content = await file.read()
    text = content.decode("utf-8-sig")  # Handle BOM

    reader = csv.DictReader(io.StringIO(text))
    rows = []

    for i, row in enumerate(reader):
        try:
            rows.append({
                "index": i,
                "type": row.get("type", "").strip(),
                "prompt": row.get("prompt", "").strip(),
                "output_path": row.get("output_path", "").strip(),
                "voice": row.get("voice", "🇺🇸 🚺 Nicole 🎧").strip(),
                "speed": float(row.get("speed", 1.0) or 1.0),
                "model": row.get("model", "flux-dev").strip(),
                "width": int(row.get("width", 1024) or 1024),
                "height": int(row.get("height", 1024) or 1024),
                "reference_image_url": row.get("reference_image_url", "").strip(),
                "strength": float(row.get("strength", 0.75) or 0.75),
                "convert_to": row.get("convert_to", "").strip(),
            })
        except (ValueError, KeyError) as e:
            rows.append({"index": i, "error": f"Parse error: {e}", **row})

    return {"rows": rows, "count": len(rows)}


@router.post("/run", response_model=BatchStatus)
async def run_batch(req: BatchRequest):
    """
    Execute a batch of voice/image generation tasks.

    Returns immediately with a job_id. Poll /api/batch/status/{job_id} for progress.
    """
    job_id = uuid.uuid4().hex[:12]
    _jobs[job_id] = {
        "total": len(req.rows),
        "completed": 0,
        "failed": 0,
        "status": "running",
        "results": [],
    }

    # Process in background
    asyncio.create_task(_process_batch(job_id, req.rows))

    return BatchStatus(job_id=job_id, **_jobs[job_id])


@router.get("/status/{job_id}", response_model=BatchStatus)
def get_batch_status(job_id: str):
    """Check the status of a running batch job."""
    if job_id not in _jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    return BatchStatus(job_id=job_id, **_jobs[job_id])


@router.get("/jobs")
def list_jobs():
    """List all batch jobs."""
    return {
        jid: {"total": j["total"], "completed": j["completed"], "failed": j["failed"], "status": j["status"]}
        for jid, j in _jobs.items()
    }


@router.get("/csv-template")
def get_csv_template():
    """Download a CSV template with example rows."""
    template = """type,prompt,output_path,voice,speed,model,width,height,reference_image_url,strength,convert_to
voice,"Late September. The kind of afternoon where the light turns everything to amber.",audio/narrator/chapter_1/line_001.wav,🇺🇸 🚺 Nicole 🎧,1.0,,,,,,ogg_vorbis
image,"Visual novel character illustration, young woman 18, mixed Chinese-British heritage, black shoulder-length hair, denim jacket. Neutral expression, waist-up, 3/4 view. Clean cel-shaded style.",characters/amelia/neutral.png,,,,flux-dev,600,900,,
image_edit,,characters/amelia/neutral_edit.png,,,flux-dev,,,https://example.com/source.png,0.75,
"""
    return StreamingResponse(
        io.StringIO(template),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=batch_template.csv"},
    )


async def _process_batch(job_id: str, rows: list[BatchRow]):
    """Process batch rows sequentially, updating job status."""
    job = _jobs[job_id]

    for i, row in enumerate(rows):
        result = {"index": i, "type": row.type, "output_path": row.output_path}
        try:
            if row.type == "voice":
                out = settings.audio_dir / row.output_path
                path = kokoro.generate_speech(
                    text=row.prompt,
                    voice=row.voice,
                    speed=row.speed,
                    output_path=out,
                )
                result["status"] = "ok"
                result["path"] = str(path)

                # Auto-convert if requested
                if row.convert_to:
                    ext_map = {"ogg_vorbis": ".ogg", "ogg_opus": ".ogg", "wav": ".wav"}
                    ext = ext_map.get(row.convert_to, ".ogg")
                    conv_path = path.with_suffix(ext)
                    audio.convert_audio(path, conv_path, row.convert_to)
                    result["converted_path"] = str(conv_path)

            elif row.type == "image":
                out = settings.images_dir / row.output_path
                images = await fal_ai.generate_image(
                    prompt=row.prompt,
                    model=row.model,
                    width=row.width,
                    height=row.height,
                    reference_image_url=row.reference_image_url or None,
                    output_path=out,
                )
                result["status"] = "ok"
                result["images"] = images

            elif row.type == "image_edit":
                out = settings.images_dir / row.output_path
                images = await fal_ai.edit_image(
                    image_url=row.reference_image_url,
                    prompt=row.prompt,
                    strength=row.strength,
                    output_path=out,
                )
                result["status"] = "ok"
                result["images"] = images

            else:
                result["status"] = "error"
                result["error"] = f"Unknown type: {row.type}"
                job["failed"] += 1

            if result.get("status") == "ok":
                job["completed"] += 1

        except Exception as e:
            logger.exception("Batch row %d failed", i)
            result["status"] = "error"
            result["error"] = str(e)
            job["failed"] += 1

        job["results"].append(result)

    job["status"] = "completed" if job["failed"] == 0 else "completed_with_errors"


# ============================================================================
# CHAPTER BATCH GENERATION
# ============================================================================

DIALOGUE_JSON_PATH = Path(__file__).parent.parent / "data" / "dialogue.json"


class ChapterGenerateRequest(BaseModel):
    chapter: str
    provider: Literal["qwen", "kokoro"] = "qwen"
    backup_existing: bool = True


@router.get("/chapters")
def list_chapters():
    """List all available chapters from the pre-parsed dialogue.json."""
    if not DIALOGUE_JSON_PATH.exists():
        raise HTTPException(
            status_code=404,
            detail="dialogue.json not found. Run scripts/parse_chapters.py first."
        )
    
    with open(DIALOGUE_JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    chapters = []
    for chapter_name, chapter_data in data["chapters"].items():
        chapters.append({
            "name": chapter_name,
            "display_name": chapter_name.replace("_", " ").title(),
            "file": chapter_data["file"],
            "line_count": chapter_data["line_count"],
        })
    
    return {
        "total_chapters": data["total_chapters"],
        "total_lines": data["total_lines"],
        "chapters": sorted(chapters, key=lambda x: x["name"])
    }


@router.post("/generate-chapter", response_model=BatchStatus)
async def generate_chapter(req: ChapterGenerateRequest):
    """
    Generate all dialogue audio for a chapter using Qwen3-TTS.
    
    - Reads dialogue from pre-parsed dialogue.json
    - Backs up existing audio files to dated bkp folder
    - Generates OGG audio for each line
    - Saves to correct paths based on character and chapter
    """
    if not DIALOGUE_JSON_PATH.exists():
        raise HTTPException(
            status_code=404,
            detail="dialogue.json not found. Run scripts/parse_chapters.py first."
        )
    
    # Load dialogue data
    with open(DIALOGUE_JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if req.chapter not in data["chapters"]:
        raise HTTPException(
            status_code=404,
            detail=f"Chapter '{req.chapter}' not found"
        )
    
    chapter_data = data["chapters"][req.chapter]
    dialogue_lines = chapter_data["dialogue"]
    
    # Create job
    job_id = uuid.uuid4().hex[:12]
    _jobs[job_id] = {
        "total": len(dialogue_lines),
        "completed": 0,
        "failed": 0,
        "skipped": 0,
        "backed_up": 0,
        "status": "running",
        "results": [],
        "chapter": req.chapter
    }
    
    # Process in background
    asyncio.create_task(_process_chapter_batch(job_id, req, dialogue_lines))
    
    return BatchStatus(job_id=job_id, **{k: v for k, v in _jobs[job_id].items() if k != "chapter"})


async def _process_chapter_batch(job_id: str, req: ChapterGenerateRequest, dialogue_lines: list[dict]):
    """Process all dialogue lines for a chapter."""
    job = _jobs[job_id]
    
    # Initialize Qwen TTS service
    qwen_tts = QwenTTSService(
        base_url=settings.qwen_url,
        api_key=settings.qwen_api_key
    )
    
    # Backup timestamp
    backup_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    for i, line in enumerate(dialogue_lines):
        result = {
            "index": i,
            "character": line["character"],
            "text_preview": line["text_clean"][:50]
        }
        
        try:
            # Determine output path - generate one if not specified
            if line.get("voice_file"):
                voice_file_path = Path(line["voice_file"])
            else:
                # Generate filename for lines without voice directives
                # Format: character_name/chapter_N/line_XXX.ogg
                char_name = line["character"].lower().replace(" ", "_").replace(".", "")
                line_num = str(i + 1).zfill(3)
                voice_file_path = Path(f"{char_name}/{req.chapter}/line_{line_num}.ogg")
            
            # Strip leading "audio/" if present (since settings.audio_dir already points to audio/)
            if voice_file_path.parts and voice_file_path.parts[0] == "audio":
                voice_file_path = Path(*voice_file_path.parts[1:])
            
            output_path = settings.audio_dir / voice_file_path
            
            # Backup existing file if it exists
            if output_path.exists() and req.backup_existing:
                backup_dir = output_path.parent / "bkp" / backup_timestamp
                backup_dir.mkdir(parents=True, exist_ok=True)
                backup_path = backup_dir / output_path.name
                shutil.copy2(output_path, backup_path)
                result["backed_up"] = str(backup_path.relative_to(settings.audio_dir))
                job["backed_up"] += 1
            
            # Generate audio with appropriate provider
            if req.provider == "qwen":
                # Use Qwen3-TTS with voice cloning for consistent character voices
                service = QwenTTSService(
                    base_url=settings.qwen_url,
                    api_key=settings.qwen_api_key
                )
                audio_path = await service.generate_speech_clone_ogg(
                    text=line["text_clean"],
                    character=line["character"],
                    speed=1.0,
                    output_path=output_path
                )
            else:
                # Use Kokoro (fallback)
                temp_wav = kokoro.generate_speech(
                    text=line["text_clean"],
                    voice="🇺🇸 🚺 Nicole 🎧",
                    speed=1.0
                )
                # Convert to OGG
                output_path.parent.mkdir(parents=True, exist_ok=True)
                audio.convert_audio(temp_wav, output_path, "ogg_vorbis")
                audio_path = output_path
            
            result["status"] = "ok"
            result["path"] = str(audio_path.relative_to(settings.audio_dir))
            result["file_size"] = audio_path.stat().st_size
            job["completed"] += 1
            
        except Exception as e:
            logger.exception(f"Failed to generate line {i} for {line['character']}")
            result["status"] = "error"
            result["error"] = str(e)
            job["failed"] += 1
        
        job["results"].append(result)
        
        # Small delay to avoid overwhelming the TTS service
        await asyncio.sleep(0.1)
    
    # Update final status
    if job["failed"] == 0:
        job["status"] = "completed"
    elif job["completed"] > 0:
        job["status"] = "completed_with_errors"
    else:
        job["status"] = "failed"
    
    logger.info(
        f"Chapter {req.chapter} generation complete: "
        f"{job['completed']} ok, {job['failed']} failed, {job['skipped']} skipped, "
        f"{job['backed_up']} backed up"
    )
