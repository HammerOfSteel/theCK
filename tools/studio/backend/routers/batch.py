"""Batch processing API — CSV import for bulk voice + image generation."""

import csv
import io
import asyncio
import logging
import uuid
from pathlib import Path
from typing import Literal

from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from backend.config import settings
from backend.services import kokoro, fal_ai, audio

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
    status: str  # running | completed | failed
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
