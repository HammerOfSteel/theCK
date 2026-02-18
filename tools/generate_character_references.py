#!/usr/bin/env python3
"""
Generate reference voices for each character using Qwen3-TTS Voice Design API.
These reference voices will be saved and can be used for voice cloning to ensure
consistency across all dialogue generation.
"""

import asyncio
import httpx
import json
import base64
from pathlib import Path

# Configuration
QWEN_API = "http://localhost:42003"
QWEN_API_KEY = "your-api-key-1"
OUTPUT_DIR = Path(__file__).parent.parent / "Amelia_V2" / "game" / "audio" / "voice_references"

# Sample text for each character - representative of their speech pattern
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

# Import character voice descriptionsexport from qwen_tts.py
CHARACTER_VOICES = {
    "Amelia": {
        "description": "young British female voice aged 18 with middle register and suburban London accent, speaking at medium pace with dry self-deprecating humor, pausing thoughtfully between thoughts",
        "mood": "thinking"
    },
    "Ella": {
        "description": "young British female voice aged 18 with South London casual accent, loud and warm with rapid-fire delivery, barely pausing for breath, full of chaotic energy",
        "mood": "normal"
    },
    "Prof. Hawthorne": {
        "description": "mature British male voice aged 58, educated and formal but not stiff, speaking deliberately and never rushing, with bone-dry humor, voice drops when moved emotionally",
        "mood": "lecturing"
    },
    "Dr. Simmons": {
        "description": "warm professional British female voice aged 38 with Birmingham accent and Caribbean lilt, conversational and flowing naturally",
        "mood": "supportive"
    },
    "Maya": {
        "description": "young British female voice aged 20 with Bristol accent, enthusiastic and expansive, speaking faster when excited, with warm slightly grandiose humor",
        "mood": "enthusiastic"
    },
    "Lucas": {
        "description": "young British male voice aged 19 with quiet measured Leeds accent softened by education, with Nigerian English influences, slow and deliberate with long thoughtful pauses, deadpan humor",
        "mood": "normal"
    },
    "Zara": {
        "description": "young Nigerian-British female voice aged 20 blending South London and Lagos accents, direct and punchy, building momentum when passionate, sharp humor, eloquent not loud when angry",
        "mood": "normal"
    },
    "Raj": {
        "description": "young British male voice aged 21 with warm Manchester accent, easy flowing and conversational, affable and self-deprecating, making the room feel lighter",
        "mood": "normal"
    },
    "Sarah": {
        "description": "young British female voice aged 18 with soft rural Devon accent, halting speech that starts and stops and tries again, with dark sudden humor, becoming monosyllabic when depressed",
        "mood": "opening_up"
    },
    "Elena": {
        "description": "mature British female voice aged 45 with proper Cornish accent softened, unhurried with weight behind every sentence, wry earthy humor, speaking through story not lecture, with occasional Cornish words",
        "mood": "normal"
    },
    "Tasha": {
        "description": "young British female voice aged 20 with Surrey Home Counties accent, polished and precise, capable of sweetness that masks cruelty, defensive when vulnerable",
        "mood": "normal"
    },
    "Michael": {
        "description": "young British male voice aged 22 with London Hackney accent, passionate and articulate, speaking with conviction and urgency, charismatic energy",
        "mood": "normal"
    },
    "Sophia": {
        "description": "young British female voice aged 19 with Oxford educated accent, precise and quick, competitive energy, softening when vulnerable",
        "mood": "normal"
    },
    "Liz": {
        "description": "young British female voice aged 18 with Welsh Cardiff accent, cheerful and bubbly, speaking with wonder about marine life, warm and genuine",
        "mood": "normal"
    },
    "Mr. James": {
        "description": "mature British male voice aged 46 with Jamaican London accent, quiet and steady, practical and measured, warmth expressed through actions not words",
        "mood": "normal"
    },
    "Mrs. James": {
        "description": "mature British female voice aged 44 with Jamaican London accent, warm and talkative, openly emotional, speaking with love and concern",
        "mood": "normal"
    },
    "Lily": {
        "description": "teenage British female voice aged 16, questioning and uncertain, speaking with adolescent energy and insecurity, bright but nervous",
        "mood": "normal"
    },
    "Narrator": {
        "description": "soft British Welsh female voice with gentle ASMR quality, calm and measured, not too fast, warm and soothing",
        "mood": "normal"
    }
}


async def generate_reference_voice(character: str, text: str, voice_config: dict, output_path: Path):
    """Generate a reference voice sample for a character."""
    
    # Build full voice instruction
    full_instruct = f"A {voice_config['description']}, speaking naturally"
    
    payload = {
        "text": text,
        "language": "English",
        "instruct": full_instruct,
        "speed": 1.0,
        "response_format": "base64"
    }
    
    headers = {
        "Content-Type": "application/json",
        "X-API-Key": QWEN_API_KEY
    }
    
    print(f"  Generating reference for {character}...")
    print(f"  Text: {text[:60]}...")
    print(f"  Instruction: {full_instruct[:80]}...")
    
    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                f"{QWEN_API}/api/v1/voice-design/generate",
                json=payload,
                headers=headers
            )
            response.raise_for_status()
            
            result = response.json()
            audio_b64 = result["audio"]
            
            # Decode and save
            audio_data = base64.b64decode(audio_b64)
            output_path.write_bytes(audio_data)
            
            print(f"  ✓ Saved: {output_path.name} ({len(audio_data) / 1024:.1f} KB)")
            
            return {
                "character": character,
                "reference_file": output_path.name,
                "sample_text": text,
                "voice_description": voice_config['description'],
                "file_size_kb": len(audio_data) / 1024
            }
            
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return {
            "character": character,
            "error": str(e)
        }


async def main():
    """Generate reference voices for all characters."""
    print("=" * 60)
    print("🎙️  Generating Character Reference Voices")
    print("=" * 60)
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Total characters: {len(CHARACTER_VOICES)}")
    print()
    
    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    results = []
    
    for character, voice_config in CHARACTER_VOICES.items():
        sample_text = SAMPLE_TEXTS.get(character, "This is a sample voice for testing.")
        output_path = OUTPUT_DIR / f"{character.lower().replace(' ', '_')}_reference.wav"
        
        result = await generate_reference_voice(character, sample_text, voice_config, output_path)
        results.append(result)
        print()
    
    # Save metadata
    metadata_path = OUTPUT_DIR / "voice_references.json"
    metadata = {
        "generated_at": "2026-02-18",
        "qwen_api": QWEN_API,
        "voice_design_api": f"{QWEN_API}/api/v1/voice-design/generate",
        "references": results
    }
    
    metadata_path.write_text(json.dumps(metadata, indent=2))
    
    print("=" * 60)
    print("✨ Reference Voice Generation Complete!")
    print("=" * 60)
    print(f"Generated: {len([r for r in results if 'error' not in r])}/{len(results)} voices")
    print(f"Metadata: {metadata_path}")
    print()
    print("📝 Next steps:")
    print("1. Listen to the generated reference voices to verify quality")
    print("2. Manually add these voices to Qwen3-TTS voice library via the UI")
    print("3. Note the voice IDs/names assigned by Qwen3-TTS")
    print("4. Update the batch generation to use voice cloning with these references")


if __name__ == "__main__":
    asyncio.run(main())
