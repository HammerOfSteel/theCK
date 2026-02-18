/**
 * Amelia Studio — Voice generation module
 * Supports Kokoro TTS and Qwen3-TTS with character voices
 */

let currentProvider = 'qwen';
let qwenCharacters = [];
let qwenCurrentMoods = [];

document.addEventListener('DOMContentLoaded', () => {
  initVoice();
});

async function initVoice() {
  // Provider tabs
  document.querySelectorAll('.provider-tab[data-provider]').forEach(tab => {
    if (tab.closest('#tab-voice')) {
      tab.addEventListener('click', () => {
        currentProvider = tab.dataset.provider;
        document.querySelectorAll('#tab-voice .provider-tab').forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        
        if (currentProvider === 'qwen') {
          document.getElementById('qwenOptions').style.display = '';
          document.getElementById('kokoroOptions').style.display = 'none';
        } else {
          document.getElementById('qwenOptions').style.display = 'none';
          document.getElementById('kokoroOptions').style.display = '';
        }
      });
    }
  });

  // Load Qwen3-TTS characters
  try {
    const data = await api('/api/voice/qwen/characters');
    qwenCharacters = data.characters;
    const charSelect = document.getElementById('qwenCharacter');
    qwenCharacters.forEach(c => {
      const opt = document.createElement('option');
      opt.value = c.name;
      opt.textContent = c.name;
      opt.dataset.description = c.description;
      opt.dataset.moods = JSON.stringify(c.moods);
      charSelect.appendChild(opt);
    });
    
    // Load moods for first character
    if (qwenCharacters.length > 0) {
      updateQwenMoods();
    }
    
    charSelect.addEventListener('change', updateQwenMoods);
  } catch (e) {
    console.warn('Could not load Qwen characters:', e);
  }

  // Load Kokoro voices
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
    console.warn('Could not load Kokoro voices:', e);
  }

  // Speed slider
  const speedSlider = document.getElementById('voiceSpeed');
  const speedValue = document.getElementById('voiceSpeedValue');
  speedSlider.addEventListener('input', () => {
    speedValue.textContent = speedSlider.value;
  });

  // Generate button
  document.getElementById('btnGenVoice').addEventListener('click', generateVoice);

  // Convert button
  document.getElementById('btnConvert').addEventListener('click', convertVoice);
}

function updateQwenMoods() {
  const charSelect = document.getElementById('qwenCharacter');
  const moodSelect = document.getElementById('qwenMood');
  const selectedOpt = charSelect.selectedOptions[0];
  
  if (!selectedOpt) return;
  
  const moods = JSON.parse(selectedOpt.dataset.moods || '[]');
  moodSelect.innerHTML = '';
  moods.forEach(mood => {
    const opt = document.createElement('option');
    opt.value = mood;
    opt.textContent = mood;
    moodSelect.appendChild(opt);
  });
}

async function generateVoice() {
  const text = document.getElementById('voiceText').value.trim();
  if (!text) { toast('Enter some text to generate', 'error'); return; }

  const outputPath = document.getElementById('voiceOutput').value.trim() || null;
  showLoading('Generating voice...');
  const resultEl = document.getElementById('voiceResult');

  try {
    let data;
    
    if (currentProvider === 'qwen') {
      // Qwen3-TTS
      const character = document.getElementById('qwenCharacter').value;
      const mood = document.getElementById('qwenMood').value;
      
      data = await api('/api/voice/qwen/generate', {
        method: 'POST',
        body: JSON.stringify({ text, character, mood, output_path: outputPath }),
      });
    } else {
      // Kokoro TTS
      const voice = document.getElementById('voiceSelect').value;
      const speed = parseFloat(document.getElementById('voiceSpeed').value);
      
      data = await api('/api/voice/generate', {
        method: 'POST',
        body: JSON.stringify({ text, voice, speed, output_path: outputPath }),
      });
    }

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
