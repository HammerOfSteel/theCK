"""Image generation & editing API routes (fal.ai)."""

import base64
import uuid
from pathlib import Path

from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from pydantic import BaseModel

from backend.config import settings
from backend.services import fal_ai

router = APIRouter(prefix="/api/images", tags=["images"])


class GenerateRequest(BaseModel):
    prompt: str
    model: str = "flux-dev"
    width: int = 1024
    height: int = 1024
    num_images: int = 1
    guidance_scale: float = 3.5
    num_inference_steps: int = 28
    reference_image_url: str | None = None
    output_path: str | None = None  # relative to /data/images


class EditRequest(BaseModel):
    image_url: str
    prompt: str
    model: str = "flux-dev"
    strength: float = 0.75
    output_path: str | None = None


class ImageResult(BaseModel):
    url: str
    local_path: str | None = None
    width: int = 0
    height: int = 0


class GenerateResponse(BaseModel):
    images: list[ImageResult]


@router.get("/models")
def get_models():
    """List available image generation models."""
    return {"models": fal_ai.list_models()}


@router.get("/presets")
def get_presets():
    """List dimension presets for VN assets."""
    return {"presets": fal_ai.list_presets()}


@router.post("/generate", response_model=GenerateResponse)
async def generate_image(req: GenerateRequest):
    """Generate image(s) from a text prompt."""
    if not settings.fal_key:
        raise HTTPException(status_code=400, detail="FAL_KEY not configured. Set it in .env")

    try:
        out_path = None
        if req.output_path:
            out_path = settings.images_dir / req.output_path

        results = await fal_ai.generate_image(
            prompt=req.prompt,
            model=req.model,
            width=req.width,
            height=req.height,
            num_images=req.num_images,
            guidance_scale=req.guidance_scale,
            num_inference_steps=req.num_inference_steps,
            reference_image_url=req.reference_image_url,
            output_path=out_path,
        )

        return GenerateResponse(images=[ImageResult(**r) for r in results])

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image generation failed: {e}")


@router.post("/edit", response_model=GenerateResponse)
async def edit_image(req: EditRequest):
    """Edit an existing image with a text prompt (image-to-image)."""
    if not settings.fal_key:
        raise HTTPException(status_code=400, detail="FAL_KEY not configured. Set it in .env")

    try:
        out_path = None
        if req.output_path:
            out_path = settings.images_dir / req.output_path

        results = await fal_ai.edit_image(
            image_url=req.image_url,
            prompt=req.prompt,
            model=req.model,
            strength=req.strength,
            output_path=out_path,
        )

        return GenerateResponse(images=[ImageResult(**r) for r in results])

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image editing failed: {e}")


@router.post("/upload-reference")
async def upload_reference(file: UploadFile = File(...)):
    """
    Upload a local reference image — returns a fal.ai-compatible URL.

    This uploads the file to fal.ai's CDN so it can be used as
    an IP-Adapter reference or image-to-image source.
    """
    if not settings.fal_key:
        raise HTTPException(status_code=400, detail="FAL_KEY not configured")

    try:
        import os
        os.environ["FAL_KEY"] = settings.fal_key

        content = await file.read()

        # Save locally first
        local_path = settings.output_dir / "uploads" / file.filename
        local_path.parent.mkdir(parents=True, exist_ok=True)
        local_path.write_bytes(content)

        # Upload to fal.ai CDN
        url = await fal_ai.fal_client.upload_file_async(local_path)

        return {"url": url, "filename": file.filename}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {e}")
