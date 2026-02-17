#!/usr/bin/env python3
"""
Convert WAV narrator voice files to OGG format to save space.
"""

import subprocess
from pathlib import Path
import os

# Get the script's directory and construct absolute path
SCRIPT_DIR = Path(__file__).parent
AUDIO_DIR = SCRIPT_DIR.parent / "Amelia_V2" / "audio" / "narrator" / "chapter_1"

def check_ffmpeg():
    """Check if ffmpeg is available."""
    try:
        result = subprocess.run(['ffmpeg', '-version'], 
                              capture_output=True, 
                              text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def convert_wav_to_ogg(wav_file, bitrate='64k'):
    """
    Convert a WAV file to OGG Opus using ffmpeg.
    Bitrate: 64k is good for voice, 96k for music. Lower = smaller file.
    """
    ogg_file = wav_file.with_suffix('.ogg')
    
    cmd = [
        'ffmpeg',
        '-i', str(wav_file),
        '-c:a', 'libopus',  # Use Opus codec (better than Vorbis for voice)
        '-b:a', bitrate,
        '-y',  # Overwrite without asking
        str(ogg_file)
    ]
    
    try:
        result = subprocess.run(cmd, 
                              capture_output=True, 
                              text=True,
                              check=True)
        return ogg_file
    except subprocess.CalledProcessError as e:
        print(f"Error converting {wav_file.name}: {e.stderr}")
        return None

def main():
    print("🎵 Converting WAV files to OGG format")
    print("=" * 60)
    
    # Check for ffmpeg
    if not check_ffmpeg():
        print("❌ ffmpeg not found!")
        print("\nTo install ffmpeg on macOS:")
        print("  brew install ffmpeg")
        return
    
    print("✓ ffmpeg is available\n")
    
    # Find all WAV files
    wav_files = sorted(AUDIO_DIR.glob("*.wav"))
    
    if not wav_files:
        print(f"❌ No WAV files found in {AUDIO_DIR}")
        return
    
    print(f"Found {len(wav_files)} WAV files to convert\n")
    
    # Track sizes
    total_wav_size = 0
    total_ogg_size = 0
    converted_count = 0
    
    for idx, wav_file in enumerate(wav_files, 1):
        wav_size = wav_file.stat().st_size
        total_wav_size += wav_size
        
        print(f"[{idx}/{len(wav_files)}] Converting: {wav_file.name}")
        print(f"  WAV size: {wav_size / 1024:.1f} KB")
        
        ogg_file = convert_wav_to_ogg(wav_file, bitrate='64k')
        
        if ogg_file and ogg_file.exists():
            ogg_size = ogg_file.stat().st_size
            total_ogg_size += ogg_size
            reduction = ((wav_size - ogg_size) / wav_size) * 100
            
            print(f"  OGG size: {ogg_size / 1024:.1f} KB ({reduction:.1f}% smaller)")
            print(f"  ✓ Created: {ogg_file.name}\n")
            converted_count += 1
        else:
            print(f"  ✗ Failed to convert\n")
    
    # Summary
    print("=" * 60)
    print(f"✨ Conversion complete!")
    print(f"\nConverted: {converted_count}/{len(wav_files)} files")
    print(f"Original WAV size: {total_wav_size / (1024*1024):.2f} MB")
    print(f"New OGG size: {total_ogg_size / (1024*1024):.2f} MB")
    
    if total_wav_size > 0:
        savings = ((total_wav_size - total_ogg_size) / total_wav_size) * 100
        print(f"Space saved: {(total_wav_size - total_ogg_size) / (1024*1024):.2f} MB ({savings:.1f}%)")
    
    print("\n" + "=" * 60)
    print("📝 Next steps:")
    print("1. Test the OGG files to ensure quality is acceptable")
    print("2. If satisfied, you can delete the WAV files:")
    print(f"   rm {AUDIO_DIR}/*.wav")
    print("3. Regenerate the voiced chapter script with OGG files:")
    print("   python tools/integrate_voice_ch1.py --format ogg")

if __name__ == "__main__":
    main()
