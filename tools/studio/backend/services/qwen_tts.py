"""Qwen3-TTS integration for character voice synthesis."""

import httpx
from pathlib import Path
import base64
import logging
import subprocess
import tempfile
import json

logger = logging.getLogger(__name__)


# Voice mappings based on character design docs (characters.md + dialogue_style_guide.md)
# Each character has a detailed natural language description and mood-specific instructions
CHARACTER_VOICES = {
    "Amelia": {
        "description": "young British female voice aged 18 with middle register and suburban London accent, speaking at medium pace with dry self-deprecating humor, pausing thoughtfully between thoughts",
        "moods": {
            "neutral": "speaking calmly and thoughtfully",
            "anxious": "speaking with voice pitching higher and tension showing",
            "vulnerable": "speaking softly with emotion",
            "passionate": "speaking with energy and conviction",
            "angry": "speaking with controlled intensity",
            "sad": "speaking with quiet sadness",
            "happy": "speaking warmly with gentle happiness",
            "thinking": "speaking slowly with longer pauses, working something out",
        }
    },
    "Ella": {
        "description": "young British female voice aged 18 with South London casual accent, loud and warm with rapid-fire delivery, barely pausing for breath, full of chaotic energy",
        "moods": {
            "normal": "speaking cheerfully and rapidly",
            "supportive": "speaking warmly and reassuringly",
            "worried": "speaking with rapid concern and care",
            "hurt": "speaking quietly with rare sadness",
        }
    },
    "Prof. Hawthorne": {
        "description": "mature British male voice aged 58, educated and formal but not stiff, speaking deliberately and never rushing, with bone-dry humor, voice drops when moved emotionally",
        "moods": {
            "lecturing": "speaking formally with authority",
            "socratic": "speaking questioningly with dry humor",
            "vulnerable": "speaking with voice dropping, showing rare warmth and depth",
        }
    },
    "Dr. Simmons": {
        "description": "warm professional British female voice aged 38 with Birmingham accent and Caribbean lilt, conversational and flowing naturally",
        "moods": {
            "supportive": "speaking warmly and compassionately",
            "teaching": "speaking conversationally with flowing wisdom",
            "vulnerable": "speaking with gentle honesty",
        }
    },
    "Maya": {
        "description": "young British female voice aged 20 with Bristol accent, enthusiastic and expansive, speaking faster when excited, with warm slightly grandiose humor",
        "moods": {
            "enthusiastic": "speaking rapidly with excitement getting faster",
            "spiritual": "becoming still and precise, fewer words with more silence",
            "vulnerable": "speaking with cracked certainty, sounding very young",
        }
    },
    "Lucas": {
        "description": "young British male voice aged 19 with quiet measured Leeds accent softened by education, with Nigerian English influences, slow and deliberate with long thoughtful pauses, deadpan humor",
        "moods": {
            "normal": "speaking very slowly and deliberately with long pauses",
            "deadpan": "speaking flatly with dry humor arriving three seconds late",
            "vulnerable": "speaking even more quietly than usual with carefully chosen words",
        }
    },
    "Zara": {
        "description": "young Nigerian-British female voice aged 20 blending South London and Lagos accents, direct and punchy, building momentum when passionate, sharp humor, eloquent not loud when angry",
        "moods": {
            "normal": "speaking directly and confidently without wasting words",
            "angry": "speaking with eloquent surgical precision, not loud",
            "vulnerable": "speaking briefly, hating to show it, wrapped in deflection",
        }
    },
    "Raj": {
        "description": "young British male voice aged 21 with warm Manchester accent, easy flowing and conversational, affable and self-deprecating, making the room feel lighter",
        "moods": {
            "normal": "speaking warmly and inclusively with food metaphors",
            "serious": "speaking with dramatic rare gravity, making everyone stop",
        }
    },
    "Sarah": {
        "description": "young British female voice aged 18 with soft rural Devon accent, halting speech that starts and stops and tries again, with dark sudden humor, becoming monosyllabic when depressed",
        "moods": {
            "good_day": "speaking gently with wonder, sentences opening like flowers",
            "dark_humor": "speaking with sudden dark wit that startles",
            "opening_up": "speaking haltingly but honestly with breaks and pauses",
            "depressed": "speaking flatly and quietly, monosyllabic, the light in the voice gone",
        }
    },
    "Elena": {
        "description": "mature British female voice aged 45 with proper Cornish accent softened, unhurried with weight behind every sentence, wry earthy humor, speaking through story not lecture, with occasional Cornish words",
        "moods": {
            "normal": "speaking unhurriedly with full silences that are not empty",
            "teaching": "telling a folk tale and waiting for you to find the lesson",
            "wry": "speaking with earthy humor about the absurdity of modern life versus ancient things",
        }
    },
    "Tasha": {
        "description": "young British female voice aged 20 with Surrey polished RP accent softened, controlled and precise with every word chosen for maximum effect, cutting humor, purring when cruel",
        "moods": {
            "cruel": "purring smoothly, making cruelty sound like concern or compliment",
            "defensive": "speaking with controlled annoyance, plausibly deniable",
            "vulnerable": "speaking with broken control, the accent slipping, sounding young",
        }
    },
    "Sophia": {
        "description": "young British female voice aged 19 with Oxford educated accent, rapid and precise like presenting a paper, accidentally funny when being earnest, efficient delivery",
        "moods": {
            "academic": "speaking very rapidly and precisely like presenting research",
            "vulnerable": "speaking slower and more uncertainly, asking questions without answers",
        }
    },
    "Liz": {
        "description": "young British female voice aged 18 with cheerful Cardiff Welsh accent, bubbly and chatty, filling silences with warmth, accent strongest when excited or upset",
        "moods": {
            "normal": "speaking bubbly and warmly, filling every silence",
            "homesick": "speaking small and quiet, the opposite of usual self",
        }
    },
    "Michael": {
        "description": "young British male voice aged 22 with Hackney London accent, confident and articulate, commanding and oratorial when passionate about activism",
        "moods": {
            "activist": "speaking with oratorial passion, turning conversation into rally",
            "casual": "speaking conversationally and approachable",
        }
    },
    "Mr. James": {
        "description": "middle-aged British male voice aged 46 with quiet Jamaican-English accent, measured and considered, expressing love through calm steady presence, saying less than he thinks, slow deliberate speech",
        "moods": {
            "normal": "speaking very slowly and considerately with long pauses",
        }
    },
    "Mrs. James": {
        "description": "middle-aged British female voice aged 44 with warm expressive Jamaican-English accent, flowing and emotional, talking through feelings naturally, occasionally overwhelming",
        "moods": {
            "normal": "speaking warmly and emotionally with flowing feeling",
        }
    },
    "Lily": {
        "description": "teenage British female voice aged 16 with energetic London accent, talking fast and texting faster, affectionate underneath the performance of being cool",
        "moods": {
            "normal": "speaking rapidly with scattered youthful energy",
        }
    },
    "Narrator": {
        "description": "soft British Welsh female voice with gentle ASMR quality, calm and measured, not too fast, warm and soothing, guiding the story with intimate warmth",
        "moods": {
            "normal": "speaking slowly and clearly with soft warm delivery, like gentle storytelling",
        }
    }
}


class QwenTTSService:
    """Qwen3-TTS API client."""
    
    def __init__(self, base_url: str = "http://host.docker.internal:42003", api_key: str = "your-api-key-1"):
        self.base_url = base_url
        self.api_key = api_key
        
    async def generate_speech(
        self,
        text: str,
        character: str = "Narrator",
        mood: str = "normal",
        speed: float = 1.0,
        output_path: Path | None = None,
    ) -> Path:
        """Generate speech using Qwen3-TTS Voice Design.
        
        Args:
            text: Text to synthesize
            character: Character name from CHARACTER_VOICES
            mood: Mood/emotion for the character
            speed: Speech speed (0.5 to 2.0)
            output_path: Where to save the audio file
            
        Returns:
            Path to the generated audio file
        """
        # Get character config
        char_config = CHARACTER_VOICES.get(character, CHARACTER_VOICES["Narrator"])
        
        # Build natural language voice description combining character and mood
        voice_description = char_config["description"]
        mood_instruction = char_config["moods"].get(mood, char_config["moods"].get("normal", "speaking naturally"))
        
        # Combine: "A warm, professional female voice with British accent, speaking calmly and thoughtfully"
        full_instruct = f"A {voice_description.lower()}, {mood_instruction.lower()}"
        
        # Prepare request for Voice Design endpoint
        payload = {
            "text": text,
            "language": "English",
            "instruct": full_instruct,
            "speed": speed,
            "response_format": "base64"
        }
        
        headers = {
            "Content-Type": "application/json",
            "X-API-Key": self.api_key
        }
        
        logger.info(f"Generating speech for {character} ({mood}): {text[:50]}...")
        logger.debug(f"Voice instruction: {full_instruct}")
        
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(
                    f"{self.base_url}/api/v1/voice-design/generate",
                    json=payload,
                    headers=headers
                )
                response.raise_for_status()
                
                result = response.json()
                audio_b64 = result["audio"]
                sample_rate = result.get("sample_rate", 24000)
                
                # Decode base64 audio
                audio_data = base64.b64decode(audio_b64)
                
                # Save to file
                if output_path is None:
                    output_path = Path(f"/tmp/qwen_tts_{character}_{mood}.wav")
                
                output_path.parent.mkdir(parents=True, exist_ok=True)
                output_path.write_bytes(audio_data)
                
                logger.info(f"Generated audio: {output_path} ({sample_rate}Hz)")
                return output_path
                
        except httpx.HTTPError as e:
            logger.error(f"Qwen TTS API error: {e}")
            raise Exception(f"Failed to generate speech: {e}")
    
    def convert_to_ogg(self, wav_path: Path) -> Path:
        """Convert WAV file to OGG Vorbis format.
        
        Args:
            wav_path: Path to WAV file
            
        Returns:
            Path to converted OGG file
        """
        ogg_path = wav_path.with_suffix('.ogg')
        
        try:
            # Use ffmpeg to convert to OGG Vorbis
            subprocess.run(
                [
                    'ffmpeg', '-i', str(wav_path),
                    '-c:a', 'libvorbis',
                    '-qscale:a', '6',  # Quality 6 (good quality, reasonable size)
                    '-y',  # Overwrite output file
                    str(ogg_path)
                ],
                check=True,
                capture_output=True,
                text=True
            )
            
            logger.info(f"Converted to OGG: {ogg_path}")
            
            # Remove the WAV file
            wav_path.unlink()
            
            return ogg_path
            
        except subprocess.CalledProcessError as e:
            logger.error(f"FFmpeg conversion failed: {e.stderr}")
            raise Exception(f"Failed to convert to OGG: {e}")
        except FileNotFoundError:
            logger.error("ffmpeg not found. Please install ffmpeg.")
            raise Exception("ffmpeg is required for OGG conversion")
    
    async def generate_speech_ogg(
        self,
        text: str,
        character: str = "Narrator",
        mood: str = "normal",
        speed: float = 1.0,
        output_path: Path | None = None,
    ) -> Path:
        """Generate speech and convert to OGG format.
        
        Args:
            text: Text to synthesize
            character: Character name from CHARACTER_VOICES
            mood: Mood/emotion for the character
            speed: Speech speed (0.5 to 2.0)
            output_path: Where to save the OGG file
            
        Returns:
            Path to the generated OGG file
        """
        # Generate WAV first
        wav_path = await self.generate_speech(
            text=text,
            character=character,
            mood=mood,
            speed=speed,
            output_path=output_path.with_suffix('.wav') if output_path else None
        )
        
        # Convert to OGG
        ogg_path = self.convert_to_ogg(wav_path)
        
        # If specific output path was requested, rename to it
        if output_path and ogg_path != output_path:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            ogg_path.rename(output_path)
            return output_path
        
        return ogg_path
    
    def list_characters(self) -> list[dict]:
        """List all available characters with their moods."""
        return [
            {
                "name": char_name,
                "description": char_config["description"],
                "moods": list(char_config["moods"].keys())
            }
            for char_name, char_config in CHARACTER_VOICES.items()
        ]
    
    def get_character_moods(self, character: str) -> list[str]:
        """Get available moods for a character."""
        char_config = CHARACTER_VOICES.get(character, {})
        return list(char_config.get("moods", {}).keys())
    
    async def generate_speech_clone(
        self,
        text: str,
        character: str = "Narrator",
        speed: float = 1.0,
        output_path: Path | None = None,
    ) -> Path:
        """Generate speech using voice cloning from saved prompts.
        
        This uses pre-created voice clone prompts for consistent character voices.
        
        Args:
            text: Text to synthesize
            character: Character name (must have a saved prompt)
            speed: Speech speed (0.5 to 2.0)
            output_path: Where to save the audio file
            
        Returns:
            Path to the generated audio file
        """
        # Load prompt mapping
        prompts_file = Path("/data/audio/voice_references/voice_prompts.json")
        if not prompts_file.exists():
            raise Exception("Voice prompts file not found. Run create_voice_prompts.py first.")
        
        prompts_data = json.loads(prompts_file.read_text())
        prompt_mapping = prompts_data.get("prompt_mapping", {})
        
        # Get prompt ID for character
        prompt_id = prompt_mapping.get(character)
        if not prompt_id:
            logger.warning(f"No voice prompt for '{character}', falling back to Narrator")
            prompt_id = prompt_mapping.get("Narrator")
            if not prompt_id:
                raise Exception("No voice prompts available")
        
        # Prepare request for generate-with-prompt endpoint
        payload = {
            "prompt_id": prompt_id,
            "text": text,
            "language": "Auto",
            "speed": speed,
            "response_format": "base64"
        }
        
        headers = {
            "Content-Type": "application/json",
            "X-API-Key": self.api_key
        }
        
        logger.info(f"Generating cloned speech for {character} (prompt: {prompt_id[:8]}...): {text[:50]}...")
        
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(
                    f"{self.base_url}/api/v1/base/generate-with-prompt",
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
    
    async def generate_speech_clone_ogg(
        self,
        text: str,
        character: str = "Narrator",
        speed: float = 1.0,
        output_path: Path | None = None,
    ) -> Path:
        """Generate speech using voice cloning and convert to OGG format.
        
        Args:
            text: Text to synthesize
            character: Character name (must have a saved prompt)
            speed: Speech speed (0.5 to 2.0)
            output_path: Where to save the OGG file
            
        Returns:
            Path to the generated OGG file
        """
        # Generate WAV first
        wav_path = await self.generate_speech_clone(
            text=text,
            character=character,
            speed=speed,
            output_path=output_path.with_suffix('.wav') if output_path else None
        )
        
        # Convert to OGG
        ogg_path = self.convert_to_ogg(wav_path)
        
        # If specific output path was requested, rename to it
        if output_path and ogg_path != output_path:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            ogg_path.rename(output_path)
            return output_path
        
        return ogg_path
