#!/usr/bin/env python3
"""
Convert OGG Opus files to OGG Vorbis format for Ren'Py compatibility.
"""

import os
import subprocess
from pathlib import Path

# Paths
input_dir = Path("Amelia_V2/audio/narrator/chapter_1")
output_dir = input_dir  # Same directory, will overwrite

def convert_to_vorbis(input_file, output_file):
    """Convert OGG Opus to OGG Vorbis using ffmpeg."""
    cmd = [
        "ffmpeg",
        "-i", str(input_file),
        "-c:a", "libvorbis",  # Use Vorbis codec
        "-q:a", "4",  # Quality level 4 (good for voice)
        "-y",  # Overwrite
        str(output_file)
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error converting {input_file.name}:")
        print(result.stderr)
        return False
    return True

def main():
    # Get all OGG files
    ogg_files = sorted(input_dir.glob("line_*.ogg"))
    
    if not ogg_files:
        print(f"No OGG files found in {input_dir}")
        return
    
    print(f"Converting {len(ogg_files)} OGG Opus files to OGG Vorbis...")
    
    # Create temp directory for new files
    temp_dir = input_dir / "temp_vorbis"
    temp_dir.mkdir(exist_ok=True)
    
    converted = 0
    for ogg_file in ogg_files:
        temp_output = temp_dir / ogg_file.name
        
        print(f"Converting {ogg_file.name}...", end=" ")
        if convert_to_vorbis(ogg_file, temp_output):
            print("✓")
            converted += 1
        else:
            print("✗")
    
    # Move converted files back
    print("\nReplacing original files...")
    for temp_file in temp_dir.glob("*.ogg"):
        original_file = input_dir / temp_file.name
        temp_file.replace(original_file)
    
    # Remove temp directory
    temp_dir.rmdir()
    
    print(f"\n✓ Converted {converted}/{len(ogg_files)} files to OGG Vorbis")
    
    # Show size comparison
    total_size = sum(f.stat().st_size for f in input_dir.glob("line_*.ogg"))
    print(f"Total size: {total_size / 1024 / 1024:.1f} MB")

if __name__ == "__main__":
    main()
