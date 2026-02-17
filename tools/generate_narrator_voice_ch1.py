#!/usr/bin/env python3
"""
Extract narrator lines from chapter_1.rpy and generate voice using Kokoro TTS.
Uses the Nicole voice for all narrator lines.
"""

import re
import os
import shutil
from pathlib import Path
from gradio_client import Client

# Configuration
CHAPTER_FILE = Path("../Amelia_V2/game/chapter_1.rpy")
OUTPUT_DIR = Path("../Amelia_V2/audio/narrator/chapter_1")
TEMP_TEXT_DIR = OUTPUT_DIR / "text_files"
KOKORO_API = "http://127.0.0.1:7860/"
VOICE_NAME = "🇺🇸 🚺 Nicole 🎧"  # Kokoro voice name for Nicole

def extract_narrator_lines(rpy_file):
    """Extract narrator lines (lines starting with ") from Ren'Py script."""
    narrator_lines = []
    
    with open(rpy_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern for narrator lines: lines that start with " (after whitespace)
    # Excludes character dialogue (which has character name before the quote)
    pattern = r'^\s{4}"(.+)"$'
    
    for line_num, line in enumerate(content.split('\n'), 1):
        # Skip commented lines
        if line.strip().startswith('#'):
            continue
            
        # Match narrator lines (proper indentation, starts with quote)
        match = re.match(pattern, line)
        if match:
            narrator_text = match.group(1)
            # Skip empty lines or lines that are just transitions
            if narrator_text.strip() and not narrator_text.startswith('{'):
                narrator_lines.append({
                    'line_num': line_num,
                    'text': narrator_text,
                    'raw_line': line
                })
    
    return narrator_lines

def create_text_files(narrator_lines, output_dir):
    """Create individual text files for each narrator line."""
    output_dir.mkdir(parents=True, exist_ok=True)
    
    text_files = []
    for idx, line_data in enumerate(narrator_lines, 1):
        filename = f"line_{idx:03d}_L{line_data['line_num']}.txt"
        filepath = output_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(line_data['text'])
        
        text_files.append({
            'filepath': filepath,
            'line_num': line_data['line_num'],
            'text': line_data['text'],
            'output_audio': f"line_{idx:03d}_L{line_data['line_num']}.wav"
        })
    
    return text_files

def generate_voice_kokoro(text_files, voice="🇺🇸 🚺 Nicole 🎧", speed=1.0, output_format="WAV"):
    """Generate voice audio using Kokoro TTS API."""
    client = Client(KOKORO_API)
    
    print(f"\n🎙️ Generating voice with {voice} voice...")
    print(f"Total lines to process: {len(text_files)}")
    
    for idx, file_data in enumerate(text_files, 1):
        print(f"\n[{idx}/{len(text_files)}] Processing: {file_data['filepath'].name}")
        print(f"  Text: {file_data['text'][:60]}{'...' if len(file_data['text']) > 60 else ''}")
        
        try:
            # Use the /generate_first endpoint
            result = client.predict(
                text=file_data['text'],
                voice=voice,
                speed=speed,
                output_format=output_format,
                api_name="/generate_first"
            )
            
            # Result is a tuple: (audio_filepath, phoneme_sequence, other_value)
            audio_filepath = result[0]
            
            # Copy the generated audio to our output directory
            output_path = OUTPUT_DIR / file_data['output_audio']
            shutil.copy(audio_filepath, output_path)
            
            print(f"  ✓ Generated: {file_data['output_audio']}")
            
        except Exception as e:
            print(f"  ✗ Error: {e}")
            continue
    
    print("\n✨ Voice generation complete!")

def main():
    print("🎭 Narrator Voice Generation for Chapter 1")
    print("=" * 60)
    
    # Check if chapter file exists
    if not CHAPTER_FILE.exists():
        print(f"❌ Error: Chapter file not found: {CHAPTER_FILE}")
        return
    
    print(f"\n📖 Reading chapter file: {CHAPTER_FILE}")
    
    # Extract narrator lines
    narrator_lines = extract_narrator_lines(CHAPTER_FILE)
    print(f"✓ Found {len(narrator_lines)} narrator lines")
    
    # Create output directories
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    TEMP_TEXT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Create text files
    print(f"\n📝 Creating text files in: {TEMP_TEXT_DIR}")
    text_files = create_text_files(narrator_lines, TEMP_TEXT_DIR)
    print(f"✓ Created {len(text_files)} text files")
    
    # List first few lines as preview
    print("\n📋 Preview of narrator lines:")
    for i, line in enumerate(narrator_lines[:5], 1):
        preview = line['text'][:70] + '...' if len(line['text']) > 70 else line['text']
        print(f"  {i}. (Line {line['line_num']}): {preview}")
    if len(narrator_lines) > 5:
        print(f"  ... and {len(narrator_lines) - 5} more lines")
    
    # Ask if user wants to proceed with generation
    print("\n" + "=" * 60)
    print("⚠️  Before generating voice:")
    print("   1. Make sure Kokoro TTS is running at http://127.0.0.1:7860/")
    print("   2. Check the API endpoint name (might not be '/generate')")
    print("   3. You can inspect the Gradio interface to find correct endpoint")
    print("=" * 60)
    
    response = input("\nProceed with voice generation? (y/n): ")
    
    if response.lower() == 'y':
        generate_voice_kokoro(text_files, voice=VOICE_NAME)
    else:
        print("\n✓ Text files created. You can manually generate voice later.")
        print(f"  Text files location: {TEMP_TEXT_DIR}")

if __name__ == "__main__":
    main()
