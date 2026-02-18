"""fal.ai image generation client — text-to-image and image-to-image."""

import os
import base64
import logging
import httpx
from pathlib import Path

import fal_client

from backend.config import settings

logger = logging.getLogger(__name__)

# Available models and their fal.ai endpoint IDs
MODELS = {
    "flux-dev": {
        "id": "fal-ai/flux/dev",
        "label": "Flux Dev ($0.025/img)",
        "supports_ip_adapter": True,
    },
    "flux-pro": {
        "id": "fal-ai/flux-pro/v1.1",
        "label": "Flux Pro 1.1 ($0.05/img)",
        "supports_ip_adapter": False,
    },
    "flux-schnell": {
        "id": "fal-ai/flux/schnell",
        "label": "Flux Schnell ($0.003/img)",
        "supports_ip_adapter": False,
    },
}

# Dimension presets for VN assets
DIMENSION_PRESETS = {
    "sprite": {"width": 600, "height": 900, "label": "Character Sprite (600×900)"},
    "background": {"width": 1920, "height": 1080, "label": "Background (1920×1080)"},
    "cg": {"width": 1920, "height": 1080, "label": "CG / Event Art (1920×1080)"},
    "square": {"width": 1024, "height": 1024, "label": "Square (1024×1024)"},
    "custom": {"width": 0, "height": 0, "label": "Custom"},
}


def _ensure_key():
    """Set fal.ai key in environment if configured."""
    if settings.fal_key:
        os.environ["FAL_KEY"] = settings.fal_key


def list_models() -> list[dict]:
    """Return available model options."""
    return [{"key": k, **v} for k, v in MODELS.items()]


def list_presets() -> list[dict]:
    """Return dimension preset options."""
    return [{"key": k, **v} for k, v in DIMENSION_PRESETS.items()]


async def generate_image(
    prompt: str,
    model: str = "flux-dev",
    width: int = 1024,
    height: int = 1024,
    num_images: int = 1,
    guidance_scale: float = 3.5,
    num_inference_steps: int = 28,
    reference_image_url: str | None = None,
    output_path: Path | None = None,
) -> list[dict]:
    """
    Generate image(s) from a text prompt via fal.ai.

    Returns list of dicts: [{"url": "...", "local_path": "..." | None}]
    """
    _ensure_key()

    if model not in MODELS:
        raise ValueError(f"Unknown model: {model}. Use: {list(MODELS)}")

    model_id = MODELS[model]["id"]

    arguments = {
        "prompt": prompt,
        "image_size": {"width": width, "height": height},
        "num_images": num_images,
        "guidance_scale": guidance_scale,
        "num_inference_steps": num_inference_steps,
        "enable_safety_checker": False,
    }

    # IP-Adapter for character consistency (Flux Dev only)
    if reference_image_url and MODELS[model].get("supports_ip_adapter"):
        arguments["ip_adapter"] = {
            "ip_adapter_image_url": reference_image_url,
            "ip_adapter_scale": 0.7,
        }

    logger.info("Generating via %s: %dx%d, %d image(s)", model_id, width, height, num_images)

    result = await fal_client.run_async(model_id, arguments=arguments)

    images = result.get("images", [])
    results = []

    for i, img_data in enumerate(images):
        img_url = img_data.get("url", "")
        local_path = None

        if output_path and img_url:
            # Download and save
            if num_images > 1:
                stem = output_path.stem
                ext = output_path.suffix
                save_path = output_path.parent / f"{stem}_{i}{ext}"
            else:
                save_path = output_path

            save_path.parent.mkdir(parents=True, exist_ok=True)

            async with httpx.AsyncClient() as client:
                resp = await client.get(img_url, timeout=60)
                resp.raise_for_status()
                save_path.write_bytes(resp.content)
                local_path = str(save_path)
                logger.info("Saved image to %s", save_path)

        results.append({
            "url": img_url,
            "local_path": local_path,
            "width": img_data.get("width", width),
            "height": img_data.get("height", height),
        })

    return results


async def edit_image(
    image_url: str,
    prompt: str,
    model: str = "flux-dev",
    strength: float = 0.75,
    output_path: Path | None = None,
) -> list[dict]:
    """
    Edit an existing image with a text prompt (image-to-image).
    """
    _ensure_key()

    model_id = "fal-ai/flux/dev/image-to-image"

    arguments = {
        "image_url": image_url,
        "prompt": prompt,
        "strength": strength,
        "num_inference_steps": 28,
        "guidance_scale": 3.5,
        "enable_safety_checker": False,
    }

    logger.info("Editing image via %s, strength=%.2f", model_id, strength)

    result = await fal_client.run_async(model_id, arguments=arguments)

    images = result.get("images", [])
    results = []

    for img_data in images:
        img_url = img_data.get("url", "")
        local_path = None

        if output_path and img_url:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            async with httpx.AsyncClient() as client:
                resp = await client.get(img_url, timeout=60)
                resp.raise_for_status()
                output_path.write_bytes(resp.content)
                local_path = str(output_path)

        results.append({
            "url": img_url,
            "local_path": local_path,
        })

    return results
