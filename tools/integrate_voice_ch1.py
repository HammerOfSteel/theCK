#!/usr/bin/env python3
"""
Generate Ren'Py voice integration code for chapter 1 narrator lines.
This creates a mapping file that can be used to add voice lines to the chapter.
"""

import re
from pathlib import Path

# Get the script's directory and construct absolute paths
SCRIPT_DIR = Path(__file__).parent
CHAPTER_FILE = SCRIPT_DIR.parent / "Amelia_V2" / "game" / "chapter_1.rpy"
AUDIO_DIR = SCRIPT_DIR.parent / "Amelia_V2" / "audio" / "narrator" / "chapter_1"
OUTPUT_FILE = SCRIPT_DIR.parent / "Amelia_V2" / "game" / "chapter_1_with_voice.rpy"

def extract_narrator_lines_with_context(rpy_file):
    """Extract narrator lines with their surrounding context."""
    narrator_lines = []
    
    with open(rpy_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    pattern = r'^\s{4}"(.+)"$'
    
    for line_num, line in enumerate(lines, 1):
        # Skip commented lines
        if line.strip().startswith('#'):
            continue
            
        # Match narrator lines
        match = re.match(pattern, line)
        if match:
            narrator_text = match.group(1)
            # Skip empty lines or lines with special formatting
            if narrator_text.strip() and not narrator_text.startswith('{'):
                narrator_lines.append({
                    'line_num': line_num,
                    'text': narrator_text,
                    'original_line': line,
                    'index_in_file': line_num - 1  # 0-based index for list
                })
    
    return narrator_lines, lines

def generate_voiced_chapter(audio_format='ogg'):
    """Generate a new version of the chapter with voice lines."""
    print("🎙️ Generating voiced chapter script...")
    print("=" * 60)
    
    narrator_lines, original_lines = extract_narrator_lines_with_context(CHAPTER_FILE)
    print(f"✓ Found {len(narrator_lines)} narrator lines")
    print(f"✓ Using audio format: {audio_format.upper()}")
    
    # Create output lines
    output_lines = original_lines.copy()
    
    # Track how many lines we've inserted (affects indices)
    offset = 0
    
    for idx, line_data in enumerate(narrator_lines, 1):
        # Find the audio file
        audio_filename = f"line_{idx:03d}_L{line_data['line_num']}.{audio_format}"
        audio_path = f"audio/narrator/chapter_1/{audio_filename}"
        
        # Check if audio file exists
        if not (AUDIO_DIR / audio_filename).exists():
            print(f"⚠️  Warning: Audio file not found: {audio_filename}")
            continue
        
        # Create the voice line to insert BEFORE the narrator line
        voice_line = f'    voice "{audio_path}"\n'
        
        # Insert position (account for previous insertions)
        insert_pos = line_data['index_in_file'] + offset
        
        # Insert the voice line
        output_lines.insert(insert_pos, voice_line)
        offset += 1
    
    # Write the new file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)
    
    print(f"✓ Generated voiced chapter: {OUTPUT_FILE}")
    print(f"✓ Added {len(narrator_lines)} voice statements")
    print("\n" + "=" * 60)
    print("📝 Next steps:")
    print("1. Review the generated file: chapter_1_with_voice.rpy")
    print("2. Test it in your Ren'Py game")
    print("3. If it works well, you can replace chapter_1.rpy")
    print("\nTo preview in Ren'Py:")
    print("  - Backup your original chapter_1.rpy")
    print("  - Rename chapter_1_with_voice.rpy to chapter_1.rpy")
    print("  - Launch the game and test")

def generate_voice_mapping():
    """Generate a simple mapping file showing line numbers and audio files."""
    narrator_lines, _ = extract_narrator_lines_with_context(CHAPTER_FILE)
    
    mapping_file = AUDIO_DIR / "voice_mapping.txt"
    
    with open(mapping_file, 'w', encoding='utf-8') as f:
        f.write("CHAPTER 1 NARRATOR VOICE MAPPING\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Total narrator lines: {len(narrator_lines)}\n")
        f.write(f"Voice: Nicole (🇺🇸 🚺 Nicole 🎧)\n")
        f.write("\n" + "-" * 80 + "\n\n")
        
        for idx, line_data in enumerate(narrator_lines, 1):
            audio_filename = f"line_{idx:03d}_L{line_data['line_num']}.wav"
            text_preview = line_data['text'][:70] + '...' if len(line_data['text']) > 70 else line_data['text']
            
            f.write(f"[{idx:03d}] Line {line_data['line_num']:4d}: {audio_filename}\n")
            f.write(f"      Text: {text_preview}\n\n")
    
    print(f"✓ Created voice mapping: {mapping_file}")

if __name__ == "__main__":
    print("🎭 Chapter 1 Voice Integration Generator")
    print("=" * 60)
    
    generate_voiced_chapter(audio_format='ogg')
    generate_voice_mapping()
    
    print("\n✨ Done!")
