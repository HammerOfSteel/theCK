"""Voice generation & audio conversion API routes."""

import tempfile
import uuid
from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

from backend.config import settings
from backend.services import kokoro, audio

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


@router.get("/preview/{filename}")
def preview_audio(filename: str):
    """Stream an audio file for playback in the browser."""
    # Search in output dir first, then audio dir
    for base in [settings.output_dir / "voice", settings.audio_dir]:
        for path in base.rglob(filename):
            if path.is_file():
                return FileResponse(path, media_type="audio/ogg")

    raise HTTPException(status_code=404, detail="Audio file not found")
