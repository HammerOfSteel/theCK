"""
Standalone SDXL Image-to-Image Server

Run this separately (not in Docker) to provide local img2img generation.

Usage:
    python sdxl_img2img_server.py

The server will run on http://127.0.0.1:7861
"""

import base64
import io
import logging
from pathlib import Path

import torch
from diffusers import StableDiffusionXLImg2ImgPipeline
from PIL import Image
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(title="SDXL Img2Img Server")

# Global pipeline instance
pipe = None


class Img2ImgRequest(BaseModel):
    prompt: str
    image: str  # base64 encoded
    strength: float = 0.6
    guidance_scale: float = 7.5
    num_inference_steps: int = 30


class Img2ImgResponse(BaseModel):
    image: str  # base64 encoded


def load_pipeline():
    """Load SDXL img2img pipeline."""
    global pipe
    
    if pipe is not None:
        return pipe
    
    logger.info("Loading SDXL img2img pipeline...")
    
    # Use CPU to avoid Mac MPS issues
    device = "cpu"
    logger.info(f"Using device: {device}")
    
    pipe = StableDiffusionXLImg2ImgPipeline.from_pretrained(
        "stabilityai/stable-diffusion-xl-base-1.0",
        torch_dtype=torch.float32,  # Use FP32 on CPU
        use_safetensors=True,
    )
    
    pipe = pipe.to(device)
    pipe.enable_attention_slicing()
    
    logger.info("Pipeline loaded successfully")
    return pipe


@app.on_event("startup")
async def startup():
    """Load pipeline on startup."""
    try:
        load_pipeline()
    except Exception as e:
        logger.error(f"Failed to load pipeline: {e}")
        raise


@app.get("/health")
async def health_check():
    """Health check endpoint with hardware info."""
    import platform
    import psutil

    hw = {
        "platform": platform.system(),
        "machine": platform.machine(),
        "processor": platform.processor() or "unknown",
        "cpu_count": psutil.cpu_count(logical=True),
        "ram_total_gb": round(psutil.virtual_memory().total / (1024**3), 1),
        "ram_available_gb": round(psutil.virtual_memory().available / (1024**3), 1),
    }

    # CUDA / GPU detection
    hw["cuda_available"] = torch.cuda.is_available()
    if torch.cuda.is_available():
        hw["gpu_name"] = torch.cuda.get_device_name(0)
        hw["gpu_vram_gb"] = round(torch.cuda.get_device_properties(0).total_mem / (1024**3), 1)
        hw["gpu_count"] = torch.cuda.device_count()
    else:
        hw["gpu_name"] = None
        hw["gpu_vram_gb"] = 0
        hw["gpu_count"] = 0

    # Check for Apple MPS
    hw["mps_available"] = hasattr(torch.backends, "mps") and torch.backends.mps.is_available()

    # Current device used by the pipeline
    hw["active_device"] = str(pipe.device) if pipe else "not loaded"

    # GPU recommendation
    if hw["cuda_available"]:
        hw["gpu_tier"] = "good"
        hw["recommendation"] = f"CUDA GPU detected ({hw['gpu_name']}). Local SDXL runs well."
    elif hw["mps_available"]:
        hw["gpu_tier"] = "fair"
        hw["recommendation"] = "Apple MPS detected. Local SDXL works but may be slow."
    elif hw["ram_total_gb"] >= 12:
        hw["gpu_tier"] = "cpu_only"
        hw["recommendation"] = "No GPU acceleration. SDXL runs on CPU (very slow). Consider fal.ai for images."
    else:
        hw["gpu_tier"] = "limited"
        hw["recommendation"] = "No GPU and limited RAM. Use fal.ai (cloud) for image generation."

    return {"status": "healthy", "model": "sdxl-img2img", "hardware": hw}


@app.post("/img2img", response_model=Img2ImgResponse)
async def generate_img2img(req: Img2ImgRequest):
    """Generate image using img2img."""
    try:
        global pipe
        
        if pipe is None:
            pipe = load_pipeline()
        
        # Decode input image
        img_data = base64.b64decode(req.image)
        init_image = Image.open(io.BytesIO(img_data)).convert("RGB")
        
        logger.info(f"Generating img2img: {req.prompt[:50]}...")
        logger.info(f"Image size: {init_image.size}, Strength: {req.strength}, Steps: {req.num_inference_steps}")
        
        # Generate
        with torch.no_grad():
            result = pipe(
                prompt=req.prompt,
                image=init_image,
                strength=req.strength,
                guidance_scale=req.guidance_scale,
                num_inference_steps=req.num_inference_steps,
            )
        
        # Encode output
        output_image = result.images[0]
        buffer = io.BytesIO()
        output_image.save(buffer, format="PNG")
        output_b64 = base64.b64encode(buffer.getvalue()).decode()
        
        logger.info("Generation complete")
        
        return Img2ImgResponse(image=output_b64)
        
    except Exception as e:
        logger.error(f"Generation failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    logger.info("Starting SDXL Img2Img Server on http://0.0.0.0:7861")
    logger.info("This may take a few minutes to load the model...")
    uvicorn.run(app, host="0.0.0.0", port=7861)
