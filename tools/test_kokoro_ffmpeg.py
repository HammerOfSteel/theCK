#!/usr/bin/env python3
import sys
from pathlib import Path
sys.path.insert(0, '/Users/terrygoleman/pinokio/api/Kokoro-TTS.git')
import os
cache_base = '/Users/terrygoleman/pinokio/api/Kokoro-TTS.git/cache'
os.environ['HF_HOME'] = cache_base + '/HF_HOME'
os.environ['TORCH_HOME'] = cache_base + '/TORCH_HOME'
os.environ['TRANSFORMERS_CACHE'] = os.environ['HF_HOME']
os.environ['TRANSFORMERS_OFFLINE'] = '1'
os.environ['HF_HUB_OFFLINE'] = '1'
import torch
torch.nn.utils.parametrize = torch.nn.utils.parametrizations.weight_norm
from kokoro import KModel, KPipeline
import scipy.io.wavfile as wavfile
import tempfile
import subprocess

print("Loading model...")
model = KModel(repo_id='hexgrad/Kokoro-82M').to('cpu').eval()
pipeline = KPipeline(repo_id='hexgrad/Kokoro-82M', lang_code='a', model=False)
pack = pipeline.load_voice('af_nicole')

text = 'Hello, this is a test.'
audio_output = []
for _, ps, _ in pipeline(text, 'af_nicole', 1.0):
    ref_s = pack[len(ps)-1]
    audio = model(ps, ref_s, 1.0)
    audio_output.append(torch.tensor(audio.numpy()))

audio_combined = torch.cat(audio_output, dim=-1)
temp_wav = tempfile.mktemp(suffix='.wav')
wavfile.write(temp_wav, 24000, audio_combined.numpy())
print(f'WAV created: {temp_wav}')
print(f'WAV size: {Path(temp_wav).stat().st_size} bytes')
print(f'WAV exists: {Path(temp_wav).exists()}')

# Test ffmpeg
temp_ogg = '/tmp/test.ogg'
cmd = ['ffmpeg', '-y', '-i', temp_wav, '-c:a', 'libvorbis', '-q:a', '4', temp_ogg]
print(f'\nRunning: {" ".join(cmd)}')
result = subprocess.run(cmd, capture_output=True, text=True)
print(f'FFmpeg returncode: {result.returncode}')
if result.returncode != 0:
    print(f'STDERR:\n{result.stderr}')
else:
    print(f'OGG created: {temp_ogg}')
    print(f'OGG size: {Path(temp_ogg).stat().st_size} bytes')
