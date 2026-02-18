"""Image generation & editing API routes (fal.ai + local SDXL)."""

import base64
import uuid
import csv
import io
import json
from pathlib import Path

from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from pydantic import BaseModel

from backend.config import settings
from backend.services import fal_ai, local_sdxl

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


class LocalImg2ImgRequest(BaseModel):
    prompt: str
    anchor_character: str
    expression: str = "neutral"
    outfit: str = "casual"
    strength: float = 0.6
    guidance_scale: float = 7.5
    num_inference_steps: int = 30
    output_path: str | None = None  # relative to /data/images


class AnchorImageInfo(BaseModel):
    character: str
    description: str
    anchor_image: str
    has_anchor: bool
    expressions: list[dict]
    outfits: list[dict]


class BatchImageResponse(BaseModel):
    generated: list[dict]
    total: int
    success: int
    failed: int


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


# --- Anchor Images & Local SDXL Routes ---

def load_character_anchors() -> dict:
    """Load character anchor definitions."""
    anchor_file = Path(__file__).parent.parent / "data" / "character_anchors.json"
    if anchor_file.exists():
        return json.loads(anchor_file.read_text())
    return {"characters": {}}


@router.get("/anchors")
async def list_anchor_images():
    """List all available character anchor images."""
    data = load_character_anchors()
    
    results = []
    for char_name, char_data in data["characters"].items():
        anchor_filename = char_data.get("anchor_image")
        anchor_path = settings.images_dir / "characters" / "anchors" / anchor_filename
        
        results.append(AnchorImageInfo(
            character=char_name,
            description=char_data.get("description", ""),
            anchor_image=anchor_filename,
            has_anchor=anchor_path.exists() if anchor_filename else False,
            expressions=char_data.get("expressions", []),
            outfits=char_data.get("outfits", [])
        ))
    
    return {"anchors": results}


@router.get("/anchors/{character}")
async def get_anchor_details(character: str):
    """Get details for a specific character's anchor."""
    data = load_character_anchors()
    
    char_data = data["characters"].get(character)
    if not char_data:
        raise HTTPException(status_code=404, detail=f"Character '{character}' not found")
    
    anchor_filename = char_data.get("anchor_image")
    anchor_path = settings.images_dir / "characters" / "anchors" / anchor_filename
    
    return AnchorImageInfo(
        character=character,
        description=char_data.get("description", ""),
        anchor_image=anchor_filename,
        has_anchor=anchor_path.exists() if anchor_filename else False,
        expressions=char_data.get("expressions", []),
        outfits=char_data.get("outfits", [])
    )


@router.get("/anchors/{character}/preview")
async def preview_anchor(character: str):
    """Get the anchor image for preview."""
    data = load_character_anchors()
    
    char_data = data["characters"].get(character)
    if not char_data:
        raise HTTPException(status_code=404, detail=f"Character '{character}' not found")
    
    anchor_filename = char_data.get("anchor_image")
    if not anchor_filename:
        raise HTTPException(status_code=404, detail="No anchor image defined")
    
    anchor_path = settings.images_dir / "characters" / "anchors" / anchor_filename
    if not anchor_path.exists():
        raise HTTPException(status_code=404, detail="Anchor image file not found")
    
    from fastapi.responses import FileResponse
    return FileResponse(anchor_path, media_type="image/png")


@router.get("/local/status")
async def check_local_sdxl_status():
    """Check if local SDXL server is running."""
    service = local_sdxl.LocalSDXLService()
    is_running = await service.check_status()
    return {"running": is_running, "url": service.base_url}


@router.post("/local/img2img", response_model=GenerateResponse)
async def generate_local_img2img(req: LocalImg2ImgRequest):
    """Generate image using local SDXL img2img with character anchor."""
    try:
        # Load character data
        data = load_character_anchors()
        char_data = data["characters"].get(req.anchor_character)
        if not char_data:
            raise HTTPException(status_code=404, detail=f"Character '{req.anchor_character}' not found")
        
        # Get anchor image path
        anchor_filename = char_data.get("anchor_image")
        if not anchor_filename:
            raise HTTPException(status_code=404, detail="No anchor image defined for character")
        
        anchor_path = settings.images_dir / "characters" / "anchors" / anchor_filename
        if not anchor_path.exists():
            raise HTTPException(status_code=404, detail="Anchor image file not found")
        
        # Determine output path
        if req.output_path:
            out_path = settings.images_dir / req.output_path
        else:
            char_safe = req.anchor_character.lower().replace(" ", "_")
            expr_safe = req.expression.lower().replace(" ", "_")
            outfit_safe = req.outfit.lower().replace(" ", "_")
            filename = f"{char_safe}_{expr_safe}_{outfit_safe}_{uuid.uuid4().hex[:8]}.png"
            out_path = settings.images_dir / "characters" / char_safe / filename
        
        # Generate using local SDXL
        service = local_sdxl.LocalSDXLService()
        result_path = await service.generate_img2img(
            prompt=req.prompt,
            anchor_image_path=anchor_path,
            strength=req.strength,
            guidance_scale=req.guidance_scale,
            num_inference_steps=req.num_inference_steps,
            output_path=out_path,
        )
        
        return GenerateResponse(images=[ImageResult(
            url="",
            local_path=str(result_path),
            width=0,
            height=0
        )])
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Local img2img generation failed: {e}")


@router.post("/local/batch", response_model=BatchImageResponse)
async def batch_generate_local_images(file: UploadFile = File(...)):
    """Batch generate images from CSV using local SDXL.
    
    CSV format (with header):
    prompt,character,expression,outfit,strength,output_path
    "Amelia looking thoughtful",Amelia,thinking,casual_a,0.6,amelia_thinking.png
    "Lucas with headphones",Lucas,neutral,casual,0.5,lucas_neutral.png
    """
    try:
        service = local_sdxl.LocalSDXLService()
        data = load_character_anchors()
        
        # Read CSV
        contents = await file.read()
        csv_text = contents.decode("utf-8")
        csv_reader = csv.DictReader(io.StringIO(csv_text))
        
        results = []
        success = 0
        failed = 0
        
        for row in csv_reader:
            try:
                prompt = row.get("prompt", "").strip()
                character = row.get("character", "").strip()
                expression = row.get("expression", "neutral").strip()
                outfit = row.get("outfit", "casual").strip()
                strength = float(row.get("strength", "0.6"))
                output_path_str = row.get("output_path", "").strip()
                
                if not prompt or not character:
                    continue
                
                # Get character anchor
                char_data = data["characters"].get(character)
                if not char_data:
                    raise ValueError(f"Character '{character}' not found")
                
                anchor_filename = char_data.get("anchor_image")
                if not anchor_filename:
                    raise ValueError(f"No anchor image for '{character}'")
                
                anchor_path = settings.images_dir / "characters" / "anchors" / anchor_filename
                if not anchor_path.exists():
                    raise ValueError(f"Anchor image not found: {anchor_filename}")
                
                # Determine output path
                if output_path_str:
                    out_path = settings.images_dir / "characters" / character.lower().replace(" ", "_") / output_path_str
                else:
                    char_safe = character.lower().replace(" ", "_")
                    expr_safe = expression.lower().replace(" ", "_")
                    outfit_safe = outfit.lower().replace(" ", "_")
                    filename = f"{char_safe}_{expr_safe}_{outfit_safe}_{uuid.uuid4().hex[:8]}.png"
                    out_path = settings.images_dir / "characters" / char_safe / filename
                
                # Generate
                result_path = await service.generate_img2img(
                    prompt=prompt,
                    anchor_image_path=anchor_path,
                    strength=strength,
                    output_path=out_path,
                )
                
                results.append({
                    "prompt": prompt[:50] + "..." if len(prompt) > 50 else prompt,
                    "character": character,
                    "expression": expression,
                    "outfit": outfit,
                    "path": str(result_path),
                    "filename": result_path.name,
                    "status": "success"
                })
                success += 1
                
            except Exception as e:
                results.append({
                    "prompt": row.get("prompt", "")[:50],
                    "character": row.get("character", ""),
                    "error": str(e),
                    "status": "failed"
                })
                failed += 1
        
        return BatchImageResponse(
            generated=results,
            total=len(results),
            success=success,
            failed=failed
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Batch processing failed: {e}")

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
