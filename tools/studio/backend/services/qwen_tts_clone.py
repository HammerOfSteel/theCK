"""Qwen3-TTS Voice Cloning Service - Updated for consistent character voices."""

import httpx
from pathlib import Path
import base64
import logging

logger = logging.getLogger(__name__)

# Voice library mapping - maps character names to their Qwen3-TTS voice library IDs
# TODO: Update these with actual voice IDs after uploading references to Qwen3-TTS
VOICE_LIBRARY = {
    "Amelia": "Amelia",
    "Ella": "Ella",
    "Prof. Hawthorne": "Prof. Hawthorne",
    "Dr. Simmons": "Dr. Simmons",
    "Maya": "Maya",
    "Lucas": "Lucas",
    "Zara": "Zara",
    "Raj": "Raj",
    "Sarah": "Sarah",
    "Elena": "Elena",
    "Tasha": "Tasha",
    "Michael": "Michael",
    "Sophia": "Sophia",
    "Liz": "Liz",
    "Mr. James": "Mr. James",
    "Mrs. James": "Mrs. James",
    "Lily": "Lily",
    "Narrator": "Narrator",
}


class QwenTTSCloneService:
    """Qwen3-TTS client with voice cloning support."""
    
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key
    
    async def generate_speech_clone(
        self,
        text: str,
        character: str = "Narrator",
        speed: float = 1.0,
        output_path: Path | None = None,
    ) -> Path:
        """Generate speech using voice cloning from saved library.
        
        Args:
            text: Text to speak
            character: Character name (must be in VOICE_LIBRARY)
            speed: Speech speed multiplier
            output_path: Where to save the audio file
            
        Returns:
            Path to the generated audio file
        """
        # Get voice ID from library
        voice_id = VOICE_LIBRARY.get(character)
        if not voice_id:
            logger.warning(f"Character '{character}' not in voice library, falling back to Narrator")
            voice_id = VOICE_LIBRARY["Narrator"]
        
        # TODO: Update this payload based on actual Qwen3-TTS voice clone API
        # Common patterns:
        # Option 1: Custom Voice API with speaker parameter
        payload = {
            "text": text,
            "speaker": voice_id,  # or "voice_id": voice_id, or "voice_name": voice_id
            "language": "English",
            "speed": speed,
            "response_format": "base64"
        }
        
        headers = {
            "Content-Type": "application/json",
            "X-API-Key": self.api_key
        }
        
        logger.info(f"Generating speech for {character} using cloned voice {voice_id}: {text[:50]}...")
        
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                # TODO: Update endpoint - try these in order:
                # 1. /api/v1/voice-clone/generate
                # 2. /api/v1/custom-voice/generate
                # 3. /api/v1/generate
                endpoint = f"{self.base_url}/api/v1/custom-voice/generate"
                
                response = await client.post(
                    endpoint,
                    json=payload,
                    headers=headers
                )
                response.raise_for_status()
                
                result = response.json()
                audio_b64 = result["audio"]
                
                # Decode base64 audio
                audio_data = base64.b64decode(audio_b64)
                
                # Save to file
                if output_path is None:
                    output_path = Path(f"/tmp/qwen_clone_{character}.wav")
                
                output_path.parent.mkdir(parents=True, exist_ok=True)
                output_path.write_bytes(audio_data)
                
                logger.info(f"Generated cloned audio: {output_path}")
                return output_path
                
        except httpx.HTTPError as e:
            logger.error(f"Qwen TTS Clone API error: {e}")
            raise Exception(f"Failed to generate cloned speech: {e}")
    
    def list_characters(self) -> list[dict]:
        """List available characters in the voice library."""
        return [
            {"name": char, "voice_id": voice_id}
            for char, voice_id in VOICE_LIBRARY.items()
        ]


# Convenience wrapper to match existing API
async def generate_speech_ogg_clone(
    text: str,
    character: str = "Narrator",
    speed: float = 1.0,
    output_path: Path | None = None,
    base_url: str = "http://host.docker.internal:42003",
    api_key: str = "your-api-key-1",
) -> Path:
    """Generate speech using voice cloning and convert to OGG.
    
    This is a drop-in replacement for the existing generate_speech_ogg function.
    """
    import subprocess
    
    service = QwenTTSCloneService(base_url=base_url, api_key=api_key)
    
    # Generate WAV
    if output_path:
        wav_path = output_path.with_suffix('.wav')
    else:
        wav_path = None
    
    wav_path = await service.generate_speech_clone(
        text=text,
        character=character,
        speed=speed,
        output_path=wav_path
    )
    
    # Convert to OGG
    ogg_path = wav_path.with_suffix('.ogg')
    
    try:
        subprocess.run(
            [
                'ffmpeg', '-i', str(wav_path),
                '-c:a', 'libvorbis',
                '-qscale:a', '6',
                '-y',
                str(ogg_path)
            ],
            check=True,
            capture_output=True,
            text=True
        )
        
        logger.info(f"Converted to OGG: {ogg_path}")
        wav_path.unlink()  # Remove WAV
        return ogg_path
        
    except subprocess.CalledProcessError as e:
        logger.error(f"FFmpeg conversion failed: {e.stderr}")
        raise Exception(f"Failed to convert to OGG: {e}")
