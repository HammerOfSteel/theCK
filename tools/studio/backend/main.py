"""
Amelia Studio — Creative tools API for The CK visual novel.

Combines voice generation (Kokoro TTS), image generation (fal.ai),
audio conversion (ffmpeg), and batch processing in a single web UI.
"""

import logging
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse

from backend.config import settings
from backend.routers import voice, images, batch

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
)

app = FastAPI(
    title="Amelia Studio",
    description="Creative tools for The CK visual novel",
    version="1.0.0",
)

# Include API routers
app.include_router(voice.router)
app.include_router(images.router)
app.include_router(batch.router)


# --- Prompt pack browser ---

@app.get("/api/prompts")
def list_prompt_packs():
    """List all available prompt pack files."""
    packs = []
    if settings.prompts_dir.exists():
        for md_file in sorted(settings.prompts_dir.rglob("*.md")):
            rel = md_file.relative_to(settings.prompts_dir)
            packs.append({
                "path": str(rel).replace("\\", "/"),
                "category": rel.parts[0] if len(rel.parts) > 1 else "root",
                "name": md_file.stem,
            })
    return {"packs": packs}


@app.get("/api/prompts/{path:path}")
def read_prompt_pack(path: str):
    """Read the contents of a prompt pack markdown file."""
    file_path = settings.prompts_dir / path
    if not file_path.exists() or not file_path.suffix == ".md":
        return JSONResponse(status_code=404, content={"detail": "Prompt pack not found"})
    return {"path": path, "content": file_path.read_text(encoding="utf-8")}


# --- Asset browser ---

@app.get("/api/assets")
def list_assets(category: str = ""):
    """List existing generated assets (images / audio)."""
    results = []

    search_dirs = []
    if not category or category == "images":
        search_dirs.append(("images", settings.images_dir))
    if not category or category == "audio":
        search_dirs.append(("audio", settings.audio_dir))

    for cat, base_dir in search_dirs:
        if not base_dir.exists():
            continue
        for f in sorted(base_dir.rglob("*")):
            if f.is_file() and f.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".ogg", ".wav", ".mp3"}:
                results.append({
                    "category": cat,
                    "path": str(f.relative_to(base_dir)).replace("\\", "/"),
                    "name": f.name,
                    "size_kb": round(f.stat().st_size / 1024, 1),
                })

    return {"assets": results, "count": len(results)}


@app.get("/api/assets/image/{path:path}")
def serve_image(path: str):
    """Serve an image file for preview."""
    file_path = settings.images_dir / path
    if file_path.exists() and file_path.is_file():
        suffix = file_path.suffix.lower()
        media = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg", "webp": "image/webp"}
        return FileResponse(file_path, media_type=media.get(suffix.lstrip("."), "application/octet-stream"))
    return JSONResponse(status_code=404, content={"detail": "Image not found"})


# --- Health check ---

@app.get("/api/health")
def health():
    """Health check with service status."""
    kokoro_ok = False
    try:
        from backend.services.kokoro import get_client
        get_client()
        kokoro_ok = True
    except Exception:
        pass

    return {
        "status": "ok",
        "services": {
            "kokoro_tts": "connected" if kokoro_ok else "unavailable",
            "fal_ai": "configured" if settings.fal_key else "not configured",
            "ffmpeg": "available",  # Always available in Docker image
        },
        "paths": {
            "images": str(settings.images_dir),
            "audio": str(settings.audio_dir),
            "prompts": str(settings.prompts_dir),
        },
    }


# --- Ensure output dirs exist ---

@app.on_event("startup")
def startup():
    settings.output_dir.mkdir(parents=True, exist_ok=True)
    (settings.output_dir / "voice").mkdir(exist_ok=True)
    (settings.output_dir / "uploads").mkdir(exist_ok=True)


# --- Serve frontend ---

frontend_dir = Path(__file__).parent.parent / "frontend"
app.mount("/", StaticFiles(directory=str(frontend_dir), html=True), name="frontend")
