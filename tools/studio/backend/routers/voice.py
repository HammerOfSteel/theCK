"""Voice generation & audio conversion API routes."""

import tempfile
import uuid
import csv
import io
from pathlib import Path

from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi.responses import FileResponse
from pydantic import BaseModel

from backend.config import settings
from backend.services import kokoro, audio, qwen_tts

router = APIRouter(prefix="/api/voice", tags=["voice"])


class GenerateRequest(BaseModel):
    text: str
    voice: str = "🇺🇸 🚺 Nicole 🎧"
    speed: float = 1.0
    output_path: str | None = None  # relative to /data/audio


class ConvertRequest(BaseModel):
    input_path: str   # relative to /data/audio
    output_format: str = "ogg_vorbis"  # ogg_vorbis | ogg_opus | wav


class GenerateResponse(BaseModel):
    path: str
    filename: str


class ConvertResponse(BaseModel):
    path: str
    filename: str


class QwenGenerateRequest(BaseModel):
    text: str
    character: str = "Narrator"
    mood: str = "normal"
    speed: float = 1.0
    output_path: str | None = None  # relative to /data/audio


class BatchVoiceResponse(BaseModel):
    generated: list[dict]
    total: int
    success: int
    failed: int


@router.get("/voices")
def get_voices():
    """List available TTS voices."""
    return {"voices": kokoro.list_voices()}


@router.post("/generate", response_model=GenerateResponse)
def generate_voice(req: GenerateRequest):
    """Generate speech from text using Kokoro TTS."""
    try:
        if req.output_path:
            out = settings.audio_dir / req.output_path
        else:
            # Auto-generate a temp name
            out = settings.output_dir / "voice" / f"{uuid.uuid4().hex[:8]}.wav"

        result_path = kokoro.generate_speech(
            text=req.text,
            voice=req.voice,
            speed=req.speed,
            output_path=out,
        )

        return GenerateResponse(path=str(result_path), filename=result_path.name)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Voice generation failed: {e}")


@router.post("/convert", response_model=ConvertResponse)
def convert_audio_file(req: ConvertRequest):
    """Convert an audio file to a different format."""
    try:
        input_path = settings.audio_dir / req.input_path

        if not input_path.exists():
            # Also check output dir
            input_path = settings.output_dir / "voice" / req.input_path
            if not input_path.exists():
                raise FileNotFoundError(f"Audio file not found: {req.input_path}")

        # Determine output extension
        ext_map = {"ogg_vorbis": ".ogg", "ogg_opus": ".ogg", "wav": ".wav"}
        ext = ext_map.get(req.output_format, ".ogg")
        out_path = input_path.with_suffix(ext)

        # Avoid overwriting source if same extension
        if out_path == input_path:
            out_path = input_path.with_stem(input_path.stem + f"_{req.output_format}")
            out_path = out_path.with_suffix(ext)

        result = audio.convert_audio(input_path, out_path, req.output_format)
        return ConvertResponse(path=str(result), filename=result.name)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Conversion failed: {e}")


# --- Qwen3-TTS Routes ---

@router.get("/qwen/characters")
async def get_qwen_characters():
    """List available characters for Qwen3-TTS."""
    service = qwen_tts.QwenTTSService(base_url=settings.qwen_url, api_key=settings.qwen_api_key)
    return {"characters": service.list_characters()}


@router.get("/qwen/characters/{character}/moods")
async def get_character_moods(character: str):
    """Get available moods for a specific character."""
    service = qwen_tts.QwenTTSService(base_url=settings.qwen_url, api_key=settings.qwen_api_key)
    moods = service.get_character_moods(character)
    if not moods:
        raise HTTPException(status_code=404, detail=f"Character '{character}' not found")
    return {"character": character, "moods": moods}


@router.post("/qwen/generate", response_model=GenerateResponse)
async def generate_qwen_voice(req: QwenGenerateRequest):
    """Generate speech using Qwen3-TTS with character and mood selection."""
    try:
        service = qwen_tts.QwenTTSService(base_url=settings.qwen_url, api_key=settings.qwen_api_key)
        
        if req.output_path:
            out = settings.audio_dir / req.output_path
        else:
            # Auto-generate path based on character/mood
            char_safe = req.character.lower().replace(" ", "_")
            mood_safe = req.mood.lower().replace(" ", "_")
            out = settings.audio_dir / "narrator" / f"{char_safe}_{mood_safe}_{uuid.uuid4().hex[:8]}.wav"
        
        result_path = await service.generate_speech(
            text=req.text,
            character=req.character,
            mood=req.mood,
            speed=req.speed,
            output_path=out,
        )
        
        return GenerateResponse(path=str(result_path), filename=result_path.name)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Qwen TTS generation failed: {e}")


@router.post("/qwen/batch", response_model=BatchVoiceResponse)
async def batch_generate_qwen_voices(file: UploadFile = File(...)):
    """Batch generate voices from CSV.
    
    CSV format (with header):
    text,character,mood,speed,output_path
    "Hello, welcome!",Amelia,happy,1.0,amelia_greeting.wav
    "I understand.",Lucas,normal,0.9,lucas_response.wav
    """
    try:
        service = qwen_tts.QwenTTSService(base_url=settings.qwen_url, api_key=settings.qwen_api_key)
        
        # Read CSV
        contents = await file.read()
        csv_text = contents.decode("utf-8")
        csv_reader = csv.DictReader(io.StringIO(csv_text))
        
        results = []
        success = 0
        failed = 0
        
        for row in csv_reader:
            try:
                text = row.get("text", "").strip()
                character = row.get("character", "Narrator").strip()
                mood = row.get("mood", "normal").strip()
                speed = float(row.get("speed", "1.0"))
                output_path_str = row.get("output_path", "").strip()
                
                if not text:
                    continue
                
                # Generate output path
                if output_path_str:
                    out = settings.audio_dir / "narrator" / output_path_str
                else:
                    char_safe = character.lower().replace(" ", "_")
                    mood_safe = mood.lower().replace(" ", "_")
                    out = settings.audio_dir / "narrator" / f"{char_safe}_{mood_safe}_{uuid.uuid4().hex[:8]}.wav"
                
                result_path = await service.generate_speech(
                    text=text,
                    character=character,
                    mood=mood,
                    speed=speed,
                    output_path=out,
                )
                
                results.append({
                    "text": text[:50] + "..." if len(text) > 50 else text,
                    "character": character,
                    "mood": mood,
                    "path": str(result_path),
                    "filename": result_path.name,
                    "status": "success"
                })
                success += 1
                
            except Exception as e:
                results.append({
                    "text": row.get("text", "")[:50],
                    "character": row.get("character", ""),
                    "mood": row.get("mood", ""),
                    "error": str(e),
                    "status": "failed"
                })
                failed += 1
        
        return BatchVoiceResponse(
            generated=results,
            total=len(results),
            success=success,
            failed=failed
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Batch processing failed: {e}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Conversion failed: {e}")


@router.get("/preview/{filename}")
def preview_audio(filename: str):
    """Stream an audio file for playback in the browser."""
    # Search in output dir first, then audio dir
    for base in [settings.output_dir / "voice", settings.audio_dir]:
        for path in base.rglob(filename):
            if path.is_file():
                return FileResponse(path, media_type="audio/ogg")

    raise HTTPException(status_code=404, detail="Audio file not found")
