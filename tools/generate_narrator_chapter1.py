#!/usr/bin/env python3
"""Generate narrator lines for Chapter 1 using Kokoro-TTS Nicole voice."""

import json
import subprocess
import tempfile
import sys
import os
from pathlib import Path

# Add Kokoro to path
kokoro_path = Path("/Users/terrygoleman/pinokio/api/Kokoro-TTS.git")
sys.path.insert(0, str(kokoro_path))

# Set environment for Kokoro
cache_base = str(kokoro_path / 'cache')
os.environ["HF_HOME"] = str(Path(cache_base) / 'HF_HOME')
os.environ["TORCH_HOME"] = str(Path(cache_base) / 'TORCH_HOME')
os.environ["TRANSFORMERS_CACHE"] = os.environ["HF_HOME"]
os.environ["HF_DATASETS_CACHE"] = os.environ["HF_HOME"]
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_HUB_OFFLINE"] = "1"

import torch
from kokoro import KModel, KPipeline
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="torch.nn.modules.rnn")
warnings.filterwarnings("ignore", category=FutureWarning, module="torch.nn.utils.weight_norm")

# Initialize Kokoro model (load once)
print("Loading Kokoro model...")
torch.nn.utils.parametrize = torch.nn.utils.parametrizations.weight_norm
CUDA_AVAILABLE = torch.cuda.is_available()

if CUDA_AVAILABLE:
    model = KModel(repo_id="hexgrad/Kokoro-82M").to('cuda').eval()
    print("Model loaded to GPU")
else:
    model = KModel(repo_id="hexgrad/Kokoro-82M").to('cpu').eval()
    print("Model loaded to CPU")

# Load American English pipeline for Nicole voice
pipeline = KPipeline(repo_id="hexgrad/Kokoro-82M", lang_code='a', model=False)


def forward(ps, ref_s, speed):
    """Forward pass through model."""
    # Same logic as app.py forward function
    if CUDA_AVAILABLE:
        return model(ps, ref_s.to('cuda'), speed)
    else:
        return model(ps, ref_s, speed)


def generate_with_kokoro(text: str, voice: str = "af_nicole", speed: float = 1.0) -> Path:
    """Generate speech using Kokoro-TTS directly."""
    # Use 500 char chunks like app.py
    CHAR_LIMIT = 500
    chunks = [text[i:i + CHAR_LIMIT] for i in range(0, len(text), CHAR_LIMIT)]
    
    # Load voice pack (Nicole is af_nicole)
    pack = pipeline.load_voice(voice)
    
    audio_output = []
    
    for chunk in chunks:
        for _, ps, _ in pipeline(chunk, voice, speed):
            ref_s = pack[len(ps)-1]
            audio = forward(ps, ref_s, speed)
            audio_output.append(torch.tensor(audio.cpu().numpy() if CUDA_AVAILABLE else audio.numpy()))
    
    # Combine chunks
    audio_combined = torch.cat(audio_output, dim=-1)
    
    # Save to temp WAV file (24kHz like Kokoro)
    import scipy.io.wavfile as wavfile
    temp_wav = Path(tempfile.mktemp(suffix=".wav"))
    wavfile.write(str(temp_wav), 24000, audio_combined.numpy())
    
    return temp_wav


def convert_to_ogg(wav_path: Path, ogg_path: Path):
    """Convert WAV to OGG using ffmpeg."""
    ogg_path.parent.mkdir(parents=True, exist_ok=True)
    
    cmd = [
        "ffmpeg", "-y", "-i", str(wav_path),
        "-c:a", "vorbis", "-q:a", "4",
        str(ogg_path)
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        raise Exception(f"FFmpeg failed: {result.stderr[:200]}")
    
    # Clean up WAV
    wav_path.unlink()


def main():
    """Generate all narrator lines for chapter_1."""
    
    # Paths
    dialogue_json = Path(__file__).parent / "studio" / "backend" / "data" / "dialogue.json"
    audio_base = Path("/Users/terrygoleman/Documents/dev/theCK/Amelia_V2/game/audio")
    
    # Load dialogue data
    print("Loading dialogue data...")
    with open(dialogue_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    chapter_data = data["chapters"]["chapter_1"]
    dialogue_lines = chapter_data["dialogue"]
    
    # Filter for narrator lines only
    narrator_lines = [
        (idx, line) for idx, line in enumerate(dialogue_lines)
        if line["character"] == "Narrator"
    ]
    
    print(f"\n{'='*70}")
    print(f"Chapter 1 Narrator Voice Generation")
    print(f"{'='*70}")
    print(f"Total narrator lines: {len(narrator_lines)}")
    print(f"Voice: 🇺🇸 🚺 Nicole 🎧 (Kokoro-TTS)")
    print(f"Format: WAV (24kHz)")
    print(f"{'='*70}\n")
    
    generated = 0
    failed = 0
    
    for idx, (line_num, line) in enumerate(narrator_lines, 1):
        text = line["text_clean"]
        
        # Generate filename - use .wav instead of .ogg
        voice_file = line.get("voice_file")
        if voice_file:
            # Use existing path but change extension
            output_path = audio_base / voice_file.replace("audio/", "").replace(".ogg", ".wav")
        else:
            # Generate new path with .wav extension
            line_idx = str(line_num + 1).zfill(3)
            output_path = audio_base / f"narrator/chapter_1/line_{line_idx}.wav"
        
        # Create directory
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Show progress
        print(f"[{idx}/{len(narrator_lines)}] {output_path.name}")
        print(f"  Text: {text[:60]}{'...' if len(text) > 60 else ''}")
        
        try:
            # Generate WAV with Kokoro
            temp_wav = generate_with_kokoro(text)
            wav_size = temp_wav.stat().st_size / 1024
            print(f"  ✓ Generated WAV ({wav_size:.1f} KB)")
            
            # Move to final location (no conversion needed)
            import shutil
            shutil.move(str(temp_wav), str(output_path))
            print(f"  ✓ Saved: {output_path.relative_to(audio_base)}")
            
            generated += 1
            
        except Exception as e:
            print(f"  ✗ Error: {e}")
            failed += 1
        
        print()
    
    # Summary
    print(f"{'='*70}")
    print(f"Generation Complete!")
    print(f"{'='*70}")
    print(f"✓ Generated: {generated}/{len(narrator_lines)}")
    if failed > 0:
        print(f"✗ Failed: {failed}")
    print(f"{'='*70}\n")
    print("Note: Files saved as WAV. Ren'Py supports WAV natively.")
    print("If you need OGG, convert them later with:")
    print("  for f in audio/narrator/chapter_1/*.wav; do")
    print("    ffmpeg -i \"$f\" -c:a vorbis -q:a 4 \"${f%.wav}.ogg\"; done")


if __name__ == "__main__":
    main()
