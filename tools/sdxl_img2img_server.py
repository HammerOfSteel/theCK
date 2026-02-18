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
    """Health check endpoint."""
    return {"status": "healthy", "model": "sdxl-img2img"}


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
    logger.info("Starting SDXL Img2Img Server on http://127.0.0.1:7861")
    logger.info("This may take a few minutes to load the model...")
    uvicorn.run(app, host="127.0.0.1", port=7861)
