"""Local SDXL image-to-image generation service.

Runs SDXL img2img locally via HTTP API. The SDXL server should be started
separately via Python (not Docker) to avoid compatibility issues on Mac.
"""

import httpx
import base64
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class LocalSDXLService:
    """Client for local SDXL img2img server."""
    
    def __init__(self, base_url: str = "http://127.0.0.1:7861"):
        self.base_url = base_url
        
    async def check_status(self) -> bool:
        """Check if the local SDXL server is running."""
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                response = await client.get(f"{self.base_url}/health")
                return response.status_code == 200
        except Exception:
            return False
    
    async def generate_img2img(
        self,
        prompt: str,
        anchor_image_path: Path,
        strength: float = 0.6,
        guidance_scale: float = 7.5,
        num_inference_steps: int = 30,
        output_path: Path | None = None,
    ) -> Path:
        """Generate image using SDXL image-to-image.
        
        Args:
            prompt: Text prompt describing the desired modifications
            anchor_image_path: Path to the anchor/reference image
            strength: How much to transform the anchor (0.0 = no change, 1.0 = completely new)
            guidance_scale: How closely to follow the prompt
            num_inference_steps: Number of denoising steps
            output_path: Where to save the generated image
            
        Returns:
            Path to the generated image
        """
        # Read anchor image and encode to base64
        img_bytes = anchor_image_path.read_bytes()
        img_b64 = base64.b64encode(img_bytes).decode()
        
        # Prepare request (server will handle image processing)
        payload = {
            "prompt": prompt,
            "image": img_b64,
            "strength": strength,
            "guidance_scale": guidance_scale,
            "num_inference_steps": num_inference_steps,
        }
        
        logger.info(f"Generating img2img with prompt: {prompt[:50]}...")
        logger.info(f"Anchor image: {anchor_image_path}")
        logger.info(f"Strength: {strength}, Steps: {num_inference_steps}")
        
        try:
            async with httpx.AsyncClient(timeout=120.0) as client:
                response = await client.post(
                    f"{self.base_url}/img2img",
                    json=payload
                )
                response.raise_for_status()
                
                result = response.json()
                output_b64 = result["image"]
                
                # Decode and save
                output_data = base64.b64decode(output_b64)
                
                if output_path is None:
                    output_path = Path(f"/tmp/sdxl_output.png")
                
                output_path.parent.mkdir(parents=True, exist_ok=True)
                output_path.write_bytes(output_data)
                
                logger.info(f"Generated image saved to: {output_path}")
                return output_path
                
        except httpx.HTTPError as e:
            logger.error(f"Local SDXL API error: {e}")
            raise Exception(f"Failed to generate image: {e}")
