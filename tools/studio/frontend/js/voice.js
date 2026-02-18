/**
 * Amelia Studio — Voice generation module
 */

document.addEventListener('DOMContentLoaded', () => {
  initVoice();
});

async function initVoice() {
  // Load voice options
  try {
    const data = await api('/api/voice/voices');
    const select = document.getElementById('voiceSelect');
    data.voices.forEach(v => {
      const opt = document.createElement('option');
      opt.value = v;
      opt.textContent = v;
      select.appendChild(opt);
    });
  } catch (e) {
    console.warn('Could not load voices:', e);
  }

  // Generate button
  document.getElementById('btnGenVoice').addEventListener('click', generateVoice);

  // Convert button
  document.getElementById('btnConvert').addEventListener('click', convertVoice);
}

async function generateVoice() {
  const text = document.getElementById('voiceText').value.trim();
  if (!text) { toast('Enter some text to generate', 'error'); return; }

  const voice = document.getElementById('voiceSelect').value;
  const speed = parseFloat(document.getElementById('voiceSpeed').value);
  const outputPath = document.getElementById('voiceOutput').value.trim() || null;

  showLoading('Generating voice...');
  const resultEl = document.getElementById('voiceResult');

  try {
    const data = await api('/api/voice/generate', {
      method: 'POST',
      body: JSON.stringify({ text, voice, speed, output_path: outputPath }),
    });

    // Set audio player source
    const player = document.getElementById('voicePlayer');
    player.src = `/api/voice/preview/${data.filename}`;
    player.hidden = false;

    resultEl.className = 'result-info success';
    resultEl.textContent = `Generated: ${data.filename}`;

    // Enable convert button
    document.getElementById('btnConvert').disabled = false;
    document.getElementById('btnConvert').dataset.path = data.path;
    document.getElementById('btnConvert').dataset.filename = data.filename;

    toast('Voice generated successfully', 'success');
  } catch (e) {
    resultEl.className = 'result-info error';
    resultEl.textContent = `Error: ${e.message}`;
    toast(e.message, 'error');
  } finally {
    hideLoading();
  }
}

async function convertVoice() {
  const btn = document.getElementById('btnConvert');
  const inputPath = btn.dataset.path;
  if (!inputPath) { toast('Generate a voice first', 'error'); return; }

  showLoading('Converting to OGG Vorbis...');
  const resultEl = document.getElementById('voiceResult');

  try {
    const data = await api('/api/voice/convert', {
      method: 'POST',
      body: JSON.stringify({
        input_path: btn.dataset.filename,
        output_format: 'ogg_vorbis',
      }),
    });

    resultEl.className = 'result-info success';
    resultEl.textContent = `Converted: ${data.filename}`;
    toast('Audio converted to OGG Vorbis', 'success');
  } catch (e) {
    resultEl.className = 'result-info error';
    resultEl.textContent = `Error: ${e.message}`;
    toast(e.message, 'error');
  } finally {
    hideLoading();
  }
}
