"""Studio configuration — loaded from .env and environment variables."""

from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    # fal.ai
    fal_key: str = ""

    # Kokoro TTS (local via Docker host)
    kokoro_host: str = "host.docker.internal"
    kokoro_port: int = 7860

    # Qwen3-TTS (local via Docker host)
    qwen_host: str = "host.docker.internal"
    qwen_port: int = 42003
    qwen_api_key: str = "your-api-key-1"

    # Data paths (mounted volumes)
    images_dir: Path = Path("/data/images")
    audio_dir: Path = Path("/data/audio")
    prompts_dir: Path = Path("/data/prompts")
    game_dir: Path = Path("/data/game")
    output_dir: Path = Path("/data/output")

    @property
    def kokoro_url(self) -> str:
        return f"http://{self.kokoro_host}:{self.kokoro_port}/"

    @property
    def qwen_url(self) -> str:
        return f"http://{self.qwen_host}:{self.qwen_port}"

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
