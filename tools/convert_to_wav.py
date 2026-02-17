#!/usr/bin/env python3
"""
Convert OGG files to WAV format for guaranteed Ren'Py compatibility.
"""

import os
import subprocess
from pathlib import Path

# Paths
input_dir = Path("Amelia_V2/audio/narrator/chapter_1")

def convert_to_wav(input_file):
    """Convert OGG to WAV using ffmpeg."""
    output_file = input_file.with_suffix('.wav')
    
    cmd = [
        "ffmpeg",
        "-i", str(input_file),
        "-c:a", "pcm_s16le",  # 16-bit PCM
        "-ar", "44100",  # 44.1kHz sample rate
        "-ac", "1",  # Mono
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
    
    print(f"Converting {len(ogg_files)} OGG files to WAV...")
    
    converted = 0
    for ogg_file in ogg_files:
        print(f"Converting {ogg_file.name}...", end=" ")
        if convert_to_wav(ogg_file):
            print("✓")
            converted += 1
        else:
            print("✗")
    
    print(f"\n✓ Converted {converted}/{len(ogg_files)} files to WAV")
    
    # Show size comparison
    wav_size = sum(f.stat().st_size for f in input_dir.glob("line_*.wav"))
    ogg_size = sum(f.stat().st_size for f in input_dir.glob("line_*.ogg"))
    print(f"WAV total: {wav_size / 1024 / 1024:.1f} MB")
    print(f"OGG total: {ogg_size / 1024 / 1024:.1f} MB")
    print(f"Size increase: {(wav_size - ogg_size) / 1024 / 1024:.1f} MB")

if __name__ == "__main__":
    main()
