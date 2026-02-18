"""Kokoro TTS client — calls the local Gradio-based Kokoro server."""

import shutil
import logging
from pathlib import Path

from gradio_client import Client

from backend.config import settings

logger = logging.getLogger(__name__)

# Default voices available in Kokoro
VOICES = [
    "🇺🇸 🚺 Nicole 🎧",
    "🇺🇸 🚺 Heart ❤️",
    "🇺🇸 🚺 Bella 🔔",
    "🇺🇸 🚺 Sarah 👩",
    "🇺🇸 🚹 Michael 🧔",
    "🇺🇸 🚹 Adam 👨",
    "🇬🇧 🚺 Emma 🌸",
    "🇬🇧 🚹 George 👑",
]


def get_client() -> Client:
    """Connect to the Kokoro TTS Gradio server."""
    return Client(settings.kokoro_url)


def list_voices() -> list[str]:
    """Return available voice options."""
    return VOICES


def generate_speech(
    text: str,
    voice: str = "🇺🇸 🚺 Nicole 🎧",
    speed: float = 1.0,
    output_path: Path | None = None,
) -> Path:
    """
    Generate speech from text via Kokoro TTS.

    Returns the path to the generated WAV file.
    """
    client = get_client()

    result = client.predict(
        text=text,
        voice=voice,
        speed=speed,
        output_format="WAV",
        api_name="/generate_first",
    )

    # result is (audio_filepath, phonemes, ...)
    source_path = Path(result[0])

    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, output_path)
        logger.info("Voice saved to %s", output_path)
        return output_path

    return source_path
