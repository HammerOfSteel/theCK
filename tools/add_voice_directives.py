#!/usr/bin/env python3
"""Add voice directives to .rpy files for lines that don't have them."""

import re
import json
from pathlib import Path

def add_voice_directives_to_chapter(chapter_name: str):
    """Add voice directives to a chapter .rpy file based on dialogue.json."""
    
    # Paths
    game_dir = Path("/Users/terrygoleman/Documents/dev/theCK/Amelia_V2/game")
    dialogue_json = Path(__file__).parent / "studio" / "backend" / "data" / "dialogue.json"
    rpy_file = game_dir / f"{chapter_name}.rpy"
    
    # Load dialogue data
    with open(dialogue_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if chapter_name not in data["chapters"]:
        print(f"Chapter {chapter_name} not found in dialogue.json")
        return
    
    dialogue_lines = data["chapters"][chapter_name]["dialogue"]
    
    # Build a map of line_number -> voice_path for lines without voice files
    voice_map = {}
    for idx, entry in enumerate(dialogue_lines):
        if entry["voice_file"] is None and entry["line_number"] > 0:
            # Generate voice path
            char_name = entry["character"].lower().replace(" ", "_").replace(".", "")
            line_num = str(idx + 1).zfill(3)
            voice_path = f"audio/{char_name}/{chapter_name}/line_{line_num}.ogg"
            voice_map[entry["line_number"]] = voice_path
    
    # Read the .rpy file
    with open(rpy_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    added_count = 0
    
    for line_num, line in enumerate(lines, 1):
        stripped = line.strip()
        
        # Check if this line number needs a voice directive
        if line_num in voice_map:
            # Check if this is actually a dialogue line
            is_dialogue = (
                stripped.startswith('thought "') or
                stripped.startswith('centered "') or
                (stripped.startswith('"') and not any(kw in stripped.lower() for kw in ['menu:', 'scene', 'with', 'play', 'stop'])) or
                re.match(r'^\w+ "', stripped)  # Character dialogue: a "text", ella "text", etc
            )
            
            if is_dialogue:
                # Get indentation
                indent = len(line) - len(line.lstrip())
                indent_str = ' ' * indent
                
                # Add voice directive before this line
                new_lines.append(f'{indent_str}voice "{voice_map[line_num]}"\n')
                added_count += 1
        
        # Add the original line
        new_lines.append(line)
    
    # Backup original file
    backup_path = rpy_file.with_suffix('.rpy.backup')
    if not backup_path.exists():
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print(f"✓ Created backup: {backup_path}")
    
    # Write modified file
    with open(rpy_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f"✓ Added {added_count} voice directives to {rpy_file}")
    print(f"✓ Total dialogue entries: {len(dialogue_lines)}")
    print(f"✓ Lines without existing voice: {len(voice_map)}")


if __name__ == "__main__":
    import sys
    
    chapter = sys.argv[1] if len(sys.argv) > 1 else "chapter_1"
    add_voice_directives_to_chapter(chapter)
