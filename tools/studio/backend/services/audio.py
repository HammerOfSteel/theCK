"""Audio format conversion using ffmpeg."""

import subprocess
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def convert_audio(
    input_path: Path,
    output_path: Path,
    output_format: str = "ogg_vorbis",
) -> Path:
    """
    Convert audio between formats using ffmpeg.

    Supported output_format values:
      - ogg_vorbis  (Ren'Py standard)
      - ogg_opus    (smaller files)
      - wav         (lossless fallback)
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    codec_args = {
        "ogg_vorbis": ["-c:a", "libvorbis", "-q:a", "6"],
        "ogg_opus": ["-c:a", "libopus", "-b:a", "64k"],
        "wav": ["-c:a", "pcm_s16le", "-ar", "44100", "-ac", "1"],
    }

    if output_format not in codec_args:
        raise ValueError(f"Unsupported format: {output_format}. Use: {list(codec_args)}")

    cmd = [
        "ffmpeg", "-y",
        "-i", str(input_path),
        *codec_args[output_format],
        str(output_path),
    ]

    logger.info("Running: %s", " ".join(cmd))
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)

    if result.returncode != 0:
        raise RuntimeError(f"ffmpeg failed: {result.stderr}")

    logger.info("Converted: %s → %s", input_path.name, output_path.name)
    return output_path
