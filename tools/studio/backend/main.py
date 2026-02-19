"""
Amelia Studio — Creative tools API for The CK visual novel.

Combines voice generation (Kokoro TTS), image generation (fal.ai),
audio conversion (ffmpeg), and batch processing in a single web UI.
"""

import logging
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse, RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware

from backend.config import settings
from backend import database as db
from backend.routers import voice, images, batch, auth

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
app.include_router(auth.router)
app.include_router(voice.router)
app.include_router(images.router)
app.include_router(batch.router)


# --- Auth middleware ---

# Paths that don't require authentication
PUBLIC_PATHS = {"/login.html", "/api/auth/login", "/api/auth/register", "/api/auth/me", "/api/health", "/api/status"}
PUBLIC_PREFIXES = ("/css/", "/js/", "/api/auth/", "/output/")


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        path = request.url.path

        # Allow public paths
        if path in PUBLIC_PATHS or any(path.startswith(p) for p in PUBLIC_PREFIXES):
            return await call_next(request)

        # Check session cookie
        token = request.cookies.get("session")
        user = db.validate_session(token)
        if user:
            request.state.user = user
            return await call_next(request)

        # Not authenticated — redirect browser requests to login page
        accept = request.headers.get("accept", "")
        if "text/html" in accept:
            return RedirectResponse("/login.html", status_code=302)

        # API requests get a 401
        return JSONResponse(status_code=401, content={"detail": "Not authenticated"})


app.add_middleware(AuthMiddleware)


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


# --- Detailed status for status panel ---

import httpx
import collections


@app.get("/api/status")
async def status_overview():
    """Detailed status of all services, for the status bar UI."""
    services = []

    # 1. Studio API (self — always ok if we're responding)
    services.append({
        "name": "Studio API",
        "key": "studio",
        "status": "running",
        "detail": "port 8500",
    })

    # 2. SDXL Server
    sdxl_status = "stopped"
    sdxl_detail = f"{settings.sdxl_host}:{settings.sdxl_port}"
    hardware = None
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            r = await client.get(f"{settings.sdxl_url}/health")
            if r.status_code == 200:
                data = r.json()
                sdxl_status = "running"
                sdxl_detail = "healthy"
                hardware = data.get("hardware")
            else:
                sdxl_status = "error"
                sdxl_detail = f"HTTP {r.status_code}"
    except httpx.ConnectError:
        sdxl_status = "stopped"
        sdxl_detail = "not reachable"
    except httpx.TimeoutException:
        sdxl_status = "loading"
        sdxl_detail = "timed out (may be loading models)"
    except Exception as e:
        sdxl_status = "error"
        sdxl_detail = str(e)[:80]


    # Always read hardware.json if present (even if SDXL is down)
    hw_file = settings.output_dir / "hardware.json"
    if hw_file.exists():
        try:
            import json as _json
            hardware = _json.loads(hw_file.read_text())
            hardware["_source"] = "launcher"
        except Exception:
            pass

    services.append({
        "name": "SDXL Server",
        "key": "sdxl",
        "status": sdxl_status,
        "detail": sdxl_detail,
    })

    # 3. Qwen3-TTS
    qwen_status = "stopped"
    qwen_detail = f"{settings.qwen_host}:{settings.qwen_port}"
    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            r = await client.get(f"{settings.qwen_url}/v1/models")
            if r.status_code == 200:
                qwen_status = "running"
                qwen_detail = "connected"
            else:
                qwen_status = "error"
                qwen_detail = f"HTTP {r.status_code}"
    except httpx.ConnectError:
        qwen_status = "stopped"
        qwen_detail = "not reachable"
    except Exception:
        qwen_status = "error"

    services.append({
        "name": "Qwen3-TTS",
        "key": "qwen",
        "status": qwen_status,
        "detail": qwen_detail,
    })

    # 4. Kokoro TTS
    kokoro_status = "stopped"
    kokoro_detail = f"{settings.kokoro_host}:{settings.kokoro_port}"
    try:
        from backend.services.kokoro import get_client
        get_client()
        kokoro_status = "running"
        kokoro_detail = "connected"
    except Exception:
        kokoro_detail = "not reachable"

    services.append({
        "name": "Kokoro TTS",
        "key": "kokoro",
        "status": kokoro_status,
        "detail": kokoro_detail,
    })

    # 5. fal.ai
    services.append({
        "name": "fal.ai",
        "key": "fal",
        "status": "running" if settings.fal_key else "stopped",
        "detail": "API key configured" if settings.fal_key else "no API key",
    })

    # 6. ffmpeg
    services.append({
        "name": "ffmpeg",
        "key": "ffmpeg",
        "status": "running",
        "detail": "available",
    })

    return {"services": services, "hardware": hardware}


@app.get("/api/status/logs")
def status_logs(lines: int = 80, service: str = "sdxl"):
    """Return the last N lines of a service log."""
    if service == "sdxl":
        log_path = settings.sdxl_log
    else:
        return {"log": f"Unknown service: {service}", "lines": 0}

    if not log_path.exists():
        return {"log": "(log file not found)", "lines": 0}

    try:
        text = log_path.read_text(encoding="utf-8", errors="replace")
        all_lines = text.splitlines()
        tail = all_lines[-lines:]
        return {"log": "\n".join(tail), "lines": len(tail), "total_lines": len(all_lines)}
    except Exception as e:
        return {"log": f"Error reading log: {e}", "lines": 0}


# --- Config API ---

@app.get("/api/config")
def get_config(request: Request):
    """Get all saved configuration."""
    return {"ok": True, "config": db.get_all_config()}


@app.put("/api/config")
async def put_config(request: Request):
    """Save configuration key-value pairs."""
    body = await request.json()
    user = getattr(request.state, "user", None)
    user_id = user["id"] if user else None
    for key, value in body.items():
        db.set_config(key, str(value), user_id)
    return {"ok": True}


# --- Ensure output dirs exist ---

@app.on_event("startup")
def startup():
    settings.output_dir.mkdir(parents=True, exist_ok=True)
    (settings.output_dir / "voice").mkdir(exist_ok=True)
    (settings.output_dir / "uploads").mkdir(exist_ok=True)
    # Initialise database
    db.init_db()


# --- Serve frontend ---



# Ensure output dir exists before mounting as static
import os
os.makedirs(str(settings.output_dir), exist_ok=True)
app.mount("/output", StaticFiles(directory=str(settings.output_dir)), name="output")

# Mount frontend last so it does not shadow /output
frontend_dir = Path(__file__).parent.parent / "frontend"
app.mount("/", StaticFiles(directory=str(frontend_dir), html=True), name="frontend")
