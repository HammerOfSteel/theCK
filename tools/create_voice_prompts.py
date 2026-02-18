#!/usr/bin/env python3
"""
Create voice clone prompts for all characters in Qwen3-TTS.
This is a one-time setup that saves each character's reference voice
as a reusable prompt for consistent voice generation.
"""

import asyncio
import httpx
import json
import base64
from pathlib import Path

# Configuration
QWEN_API = "http://localhost:42003"
QWEN_API_KEY = "your-api-key-1"
REFERENCES_DIR = Path(__file__).parent.parent / "Amelia_V2" / "game" / "audio" / "voice_references"
PROMPTS_FILE = REFERENCES_DIR / "voice_prompts.json"

# Sample texts for each character (from voice_references.json metadata)
SAMPLE_TEXTS = {
    "Amelia": "I keep reading about individuation but I can't even individuate myself from my mum's cooking. She sent me a Tupperware of jerk chicken through the post.",
    "Ella": "Okay, first of all, breathe. Second of all, I'm googling how to fight a bully through a laptop screen. Third of all, did you eat today?",
    "Prof. Hawthorne": "Miss James, I didn't ask what you feel about Milgram's experiment. I asked what it demonstrates. Your feelings are valid. They are also not the assignment.",
    "Dr. Simmons": "Look, I could cite you twelve studies on resilience and positive reframing. But right now? Right now I think you need a cup of tea and to cry for a bit.",
    "Maya": "Okay, hear me out — what if Jung was essentially describing the same process the alchemists were, just without the mercury and the furnaces?",
    "Lucas": "You know what I think about at 3am? Not the exam. The exam is just the exam. I think about whether my dad ever thought about me at 3am.",
    "Zara": "You read about systemic racism in a textbook? That's cute. I'll tell you about systemic racism at 2am at a bus stop in Lewisham.",
    "Raj": "Okay, listen, my nan makes the best dal in Manchester. In the north of England. I'm not saying my cooking is as good. I'm saying it's a loving tribute.",
    "Sarah": "You know that thing where the sea looks really calm and you think, that doesn't look cold at all? And then you put your foot in and it's so cold it burns?",
    "Elena": "You want to understand the mind? Then stop reading about it in a library and come stand in the rain on a moor at midnight.",
    "Tasha": "Oh, love, is that a charity shop jacket? No, genuinely, I think that's sweet. Very sustainable.",
    "Michael": "You're studying why people suffer. I'm asking who benefits from that suffering. Those are different questions, and only one of them changes anything.",
    "Sophia": "I don't understand why you'd choose to go to a film when you could be reading the Kahneman. It's Kahneman. Films will always be there.",
    "Liz": "I was up till 3am watching this documentary about octopuses and they're just so clever and it made me cry a bit because they die after they have babies.",
    "Mr. James": "I checked your car's oil and tire pressure. The spare tire's a bit low so I topped it up. Drive safe.",
    "Mrs. James": "I sent you some jerk chicken through the post. Should arrive Tuesday. There's rice in there too.",
    "Lily": "So like, hypothetically, if someone was questioning whether they might like girls as well as boys, how would you— never mind. Forget I said anything.",
    "Narrator": "Late September. The kind of afternoon where the light turns everything to amber, and the sea looks like hammered silver, and you can almost convince yourself that leaving home was the right thing to do."
}


async def create_voice_prompt(character: str, ref_audio_path: Path, ref_text: str):
    """Create a voice clone prompt from reference audio."""
    
    # Read reference audio and encode to base64
    audio_data = ref_audio_path.read_bytes()
    audio_b64 = base64.b64encode(audio_data).decode('utf-8')
    
    payload = {
        "ref_audio_base64": audio_b64,
        "ref_text": ref_text,
        "name": character,
        "x_vector_only_mode": False
    }
    
    headers = {
        "Content-Type": "application/json",
        "X-API-Key": QWEN_API_KEY
    }
    
    print(f"  Creating prompt for {character}...")
    print(f"  Reference: {ref_audio_path.name}")
    print(f"  Text length: {len(ref_text)} chars")
    
    try:
        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(
                f"{QWEN_API}/api/v1/base/create-prompt",
                json=payload,
                headers=headers
            )
            response.raise_for_status()
            
            result = response.json()
            prompt_id = result["prompt_id"]
            message = result.get("message", "")
            
            print(f"  ✓ Created prompt: {prompt_id}")
            print(f"  {message}")
            
            return {
                "character": character,
                "prompt_id": prompt_id,
                "reference_file": ref_audio_path.name,
                "reference_text": ref_text,
                "status": "success"
            }
            
    except httpx.HTTPStatusError as e:
        error_msg = e.response.text
        print(f"  ✗ HTTP Error: {e.response.status_code}")
        print(f"  {error_msg}")
        return {
            "character": character,
            "error": f"HTTP {e.response.status_code}: {error_msg}",
            "status": "failed"
        }
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return {
            "character": character,
            "error": str(e),
            "status": "failed"
        }


async def list_existing_prompts():
    """List all saved voice prompts."""
    headers = {"X-API-Key": QWEN_API_KEY}
    
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(
                f"{QWEN_API}/api/v1/base/prompts",
                headers=headers
            )
            response.raise_for_status()
            return response.json()
    except Exception as e:
        print(f"Could not list existing prompts: {e}")
        return {}


async def main():
    """Create voice clone prompts for all characters."""
    print("=" * 60)
    print("🎙️  Creating Voice Clone Prompts")
    print("=" * 60)
    print(f"References directory: {REFERENCES_DIR}")
    print()
    
    # Check if references exist
    if not REFERENCES_DIR.exists():
        print("❌ References directory not found!")
        print(f"Expected: {REFERENCES_DIR}")
        print()
        print("Run generate_character_references.py first to create reference voices.")
        return
    
    # List existing prompts
    print("Checking for existing prompts...")
    existing = await list_existing_prompts()
    if existing:
        print(f"Found {len(existing.get('prompts', []))} existing prompts")
        print()
    
    # Create prompts for each character
    results = []
    created = 0
    failed = 0
    
    for character, ref_text in SAMPLE_TEXTS.items():
        # Find reference audio file (handle dots and spaces)
        char_safe = character.lower().replace(' ', '_').replace('.', '.')  # Keep dots as-is for now
        ref_filename = f"{char_safe}_reference.wav"
        ref_path = REFERENCES_DIR / ref_filename
        
        if not ref_path.exists():
            print(f"⚠️  Skipping {character}: reference file not found ({ref_filename})")
            results.append({
                "character": character,
                "error": f"Reference file not found: {ref_filename}",
                "status": "skipped"
            })
            failed += 1
            print()
            continue
        
        result = await create_voice_prompt(character, ref_path, ref_text)
        results.append(result)
        
        if result.get("status") == "success":
            created += 1
        else:
            failed += 1
        
        print()
    
    # Save prompt IDs to file
    prompt_mapping = {
        r["character"]: r["prompt_id"]
        for r in results
        if r.get("status") == "success"
    }
    
    metadata = {
        "created_at": "2026-02-18",
        "qwen_api": QWEN_API,
        "create_prompt_endpoint": f"{QWEN_API}/api/v1/base/create-prompt",
        "generate_endpoint": f"{QWEN_API}/api/v1/base/generate-with-prompt",
        "prompt_mapping": prompt_mapping,
        "all_results": results
    }
    
    PROMPTS_FILE.write_text(json.dumps(metadata, indent=2))
    
    print("=" * 60)
    print("✨ Voice Clone Prompts Created!")
    print("=" * 60)
    print(f"Success: {created}/{len(SAMPLE_TEXTS)} prompts created")
    print(f"Failed: {failed}/{len(SAMPLE_TEXTS)}")
    print(f"Prompt mapping saved: {PROMPTS_FILE}")
    print()
    
    if created > 0:
        print("📝 Next step:")
        print("Run the batch generation with voice cloning enabled.")
        print("Each character will now use their consistent cloned voice!")
    else:
        print("⚠️  No prompts were created successfully.")
        print("Check the error messages above and ensure Qwen3-TTS is running.")


if __name__ == "__main__":
    asyncio.run(main())
