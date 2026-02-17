#!/usr/bin/env python3
"""Test the Kokoro TTS API with a single line."""

from gradio_client import Client

KOKORO_API = "http://127.0.0.1:7860/"

print("🧪 Testing Kokoro TTS API...")
print("=" * 60)

try:
    client = Client(KOKORO_API)
    print("✓ Connected to API")
    
    # Test with a short narrator line
    test_text = "Late September. The kind of afternoon where the light turns everything to amber."
    test_voice = "🇺🇸 🚺 Nicole 🎧"
    
    print(f"\n📝 Test text: {test_text}")
    print(f"🎙️ Voice: {test_voice}")
    print("\nGenerating audio...")
    
    result = client.predict(
        text=test_text,
        voice=test_voice,
        speed=1.0,
        output_format="WAV",
        api_name="/generate_first"
    )
    
    print(f"\n✅ Success!")
    print(f"Audio file: {result[0]}")
    print(f"Phonemes: {result[1][:100]}..." if len(str(result[1])) > 100 else f"Phonemes: {result[1]}")
    
    # Play the audio (optional)
    import os
    if os.path.exists(result[0]):
        file_size = os.path.getsize(result[0])
        print(f"File size: {file_size:,} bytes")
        
        # On macOS, you can play the audio with afplay
        print(f"\n▶️ To listen: afplay '{result[0]}'")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()
