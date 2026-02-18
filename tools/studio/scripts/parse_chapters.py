#!/usr/bin/env python3
"""Parse all chapter .rpy files and generate dialogue structure."""

import sys
import json
from pathlib import Path

# Add backend to path
backend_path = Path(__file__).parent.parent / "backend"
sys.path.insert(0, str(backend_path))

from utils.rpy_parser import RenpyParser, clean_text_for_tts


def main():
    """Parse all chapter files and generate dialogue.json."""
    
    # Paths
    game_dir = Path("/Users/terrygoleman/Documents/dev/theCK/Amelia_V2/game")
    output_file = Path(__file__).parent.parent / "backend" / "data" / "dialogue.json"
    
    # Create parser
    parser = RenpyParser()
    
    # Get all chapter files
    chapter_files = parser.get_chapter_files(game_dir)
    
    print(f"Found {len(chapter_files)} chapter files:")
    for chapter_name in chapter_files:
        print(f"  - {chapter_name}")
    
    # Parse all chapters
    all_dialogue = {}
    total_lines = 0
    
    for chapter_name, chapter_path in chapter_files.items():
        print(f"\nParsing {chapter_name}...")
        
        dialogue_lines = parser.parse_file(chapter_path)
        
        # Convert to dict structure
        chapter_dialogue = []
        for line in dialogue_lines:
            chapter_dialogue.append({
                "character": line.character,
                "text": line.text,
                "text_clean": clean_text_for_tts(line.text),
                "voice_file": line.voice_file,
                "line_number": line.line_number
            })
        
        all_dialogue[chapter_name] = {
            "file": str(chapter_path.name),
            "line_count": len(chapter_dialogue),
            "dialogue": chapter_dialogue
        }
        
        total_lines += len(chapter_dialogue)
        print(f"  Found {len(chapter_dialogue)} dialogue lines")
        
        # Show character distribution
        char_counts = {}
        for line in chapter_dialogue:
            char = line["character"]
            char_counts[char] = char_counts.get(char, 0) + 1
        
        print(f"  Characters: {', '.join([f'{char}({count})' for char, count in sorted(char_counts.items())])}")
    
    # Create output directory
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Save to JSON
    output_data = {
        "total_chapters": len(all_dialogue),
        "total_lines": total_lines,
        "chapters": all_dialogue
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Dialogue structure saved to: {output_file}")
    print(f"   Total chapters: {len(all_dialogue)}")
    print(f"   Total dialogue lines: {total_lines}")
    
    # Also create a summary CSV for quick reference
    summary_file = output_file.parent / "dialogue_summary.csv"
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write("chapter,character,line_number,text_preview,voice_file\n")
        for chapter_name, chapter_data in all_dialogue.items():
            for line in chapter_data["dialogue"]:
                text_preview = line["text_clean"][:60].replace('"', '""')
                f.write(f'"{chapter_name}","{line["character"]}",{line["line_number"]},"{text_preview}","{line["voice_file"] or ""}"\n')
    
    print(f"   Summary CSV: {summary_file}")


if __name__ == "__main__":
    main()
