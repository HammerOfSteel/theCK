/**
 * Amelia Studio — Image generation module
 * Supports fal.ai (cloud) and local SDXL with character anchors
 */

let currentImageProvider = 'local';
let anchorCharacters = [];
let currentAnchors = {};

document.addEventListener('DOMContentLoaded', () => {
  initImages();
});

const PRESET_DIMS = {
  sprite:     { width: 600,  height: 900  },
  background: { width: 1920, height: 1080 },
  cg:         { width: 1920, height: 1080 },
  square:     { width: 1024, height: 1024 },
};

let uploadedRefUrl = null;

async function initImages() {
  // Provider tabs
  document.querySelectorAll('.provider-tab[data-provider]').forEach(tab => {
    if (tab.closest('#tab-images')) {
      tab.addEventListener('click', () => {
        currentImageProvider = tab.dataset.provider;
        document.querySelectorAll('#tab-images .provider-tab').forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        
        if (currentImageProvider === 'local') {
          document.getElementById('localOptions').style.display = '';
        } else {
          document.getElementById('localOptions').style.display = 'none';
        }
      });
    }
  });

  // Load character anchors for local SDXL
  try {
    const data = await api('/api/images/anchors');
    anchorCharacters = data.anchors;
    const charSelect = document.getElementById('anchorCharacter');
    anchorCharacters.forEach(c => {
      const opt = document.createElement('option');
      opt.value = c.character;
      opt.textContent = c.character;
      opt.dataset.character = JSON.stringify(c);
      charSelect.appendChild(opt);
    });
    
    if (anchorCharacters.length > 0) {
      updateAnchorOptions();
    }
    
    charSelect.addEventListener('change', updateAnchorOptions);
  } catch (e) {
    console.warn('Could not load anchors:', e);
  }

  // Local strength slider
  const strengthSlider = document.getElementById('localStrength');
  const strengthValue = document.getElementById('localStrengthValue');
  if (strengthSlider) {
    strengthSlider.addEventListener('input', () => {
      strengthValue.textContent = strengthSlider.value;
    });
  }

  // Load fal.ai models
  try {
    const data = await api('/api/images/models');
    const select = document.getElementById('imgModel');
    if (select) {
      data.models.forEach(m => {
        const opt = document.createElement('option');
        opt.value = m.key;
        opt.textContent = m.label;
        select.appendChild(opt);
      });
    }
  } catch (e) {
    console.warn('Could not load models:', e);
  }

  // Preset change
  const presetSelect = document.getElementById('imgPreset');
  if (presetSelect) {
    presetSelect.addEventListener('change', (e) => {
      const custom = document.getElementById('customDims');
      if (e.target.value === 'custom') {
        custom.style.display = 'flex';
      } else {
        custom.style.display = 'none';
      }
    });
  }

  // Sliders
  const guidanceSlider = document.getElementById('imgGuidance');
  const guidanceValue = document.getElementById('imgGuidanceValue');
  const stepsSlider = document.getElementById('imgSteps');
  const stepsValue = document.getElementById('imgStepsValue');
  
  if (guidanceSlider) {
    guidanceSlider.addEventListener('input', () => {
      guidanceValue.textContent = guidanceSlider.value;
    });
  }
  
  if (stepsSlider) {
    stepsSlider.addEventListener('input', () => {
      stepsValue.textContent = stepsSlider.value;
    });
  }

  // Reference image upload (for fal.ai)
  const refArea = document.getElementById('refUploadArea');
  const refInput = document.getElementById('refFileInput');
  const refPreview = document.getElementById('refPreview');
  const refClear = document.getElementById('refClear');
  const refLabel = document.getElementById('refUploadLabel');

  if (refArea) {
    refArea.addEventListener('click', (e) => {
      if (e.target !== refClear) refInput.click();
    });

    refArea.addEventListener('dragover', (e) => {
      e.preventDefault();
      refArea.classList.add('dragover');
    });

    refArea.addEventListener('dragleave', () => {
      refArea.classList.remove('dragover');
    });

    refArea.addEventListener('drop', (e) => {
      e.preventDefault();
      refArea.classList.remove('dragover');
      if (e.dataTransfer.files.length) {
        refInput.files = e.dataTransfer.files;
        uploadReference(e.dataTransfer.files[0]);
      }
    });
  }

  if (refInput) {
    refInput.addEventListener('change', () => {
      if (refInput.files.length) uploadReference(refInput.files[0]);
    });
  }

  if (refClear) {
    refClear.addEventListener('click', (e) => {
      e.stopPropagation();
      uploadedRefUrl = null;
      refPreview.hidden = true;
      refClear.hidden = true;
      refLabel.hidden = false;
      document.getElementById('refImageUrl').value = '';
    });
  }

  // Generate button
  document.getElementById('btnGenImage').addEventListener('click', generateImage);

  // Edit button
  const editBtn = document.getElementById('btnEditImage');
  if (editBtn) editBtn.addEventListener('click', editImage);
}

function updateAnchorOptions() {
  const charSelect = document.getElementById('anchorCharacter');
  const expressionSelect = document.getElementById('anchorExpression');
  const outfitSelect = document.getElementById('anchorOutfit');
  
  const selectedOpt = charSelect.selectedOptions[0];
  if (!selectedOpt) return;
  
  const character = JSON.parse(selectedOpt.dataset.character);
  currentAnchors = character;
  
  // Update expressions
  expressionSelect.innerHTML = '';
  character.expressions.forEach(expr => {
    const opt = document.createElement('option');
    opt.value = expr.name;
    opt.textContent = expr.name;
    opt.dataset.description = expr.description;
    expressionSelect.appendChild(opt);
  });
  
  // Update outfits
  outfitSelect.innerHTML = '';
  character.outfits.forEach(outfit => {
    const opt = document.createElement('option');
    opt.value = outfit.name;
    opt.textContent = outfit.name;
    opt.dataset.description = outfit.description;
    outfitSelect.appendChild(opt);
  });
}

async function uploadReference(file) {
  const refPreview = document.getElementById('refPreview');
  const refClear = document.getElementById('refClear');
  const refLabel = document.getElementById('refUploadLabel');

  // Show local preview immediately
  const reader = new FileReader();
  reader.onload = (e) => {
    refPreview.src = e.target.result;
    refPreview.hidden = false;
    refClear.hidden = false;
    refLabel.hidden = true;
  };
  reader.readAsDataURL(file);

  // Upload to fal.ai CDN
  try {
    const formData = new FormData();
    formData.append('file', file);
    const res = await fetch('/api/images/upload-reference', { method: 'POST', body: formData });
    if (!res.ok) throw new Error('Upload failed');
    const data = await res.json();
    uploadedRefUrl = data.url;
    document.getElementById('refImageUrl').value = data.url;
    toast(`Reference uploaded: ${data.filename}`, 'success');
  } catch (e) {
    toast(`Upload failed: ${e.message}`, 'error');
  }
}

async function generateImage() {
  const prompt = document.getElementById('imgPrompt').value.trim();
  if (!prompt) { toast('Enter a prompt', 'error'); return; }

  const outputPath = document.getElementById('imgOutput').value.trim() || null;
  showLoading('Generating image...');
  const resultEl = document.getElementById('imageResult');
  const gallery = document.getElementById('imageGallery');

  try {
    let data;
    
    if (currentImageProvider === 'local') {
      // Local SDXL with character anchors
      const character = document.getElementById('anchorCharacter').value;
      const expression = document.getElementById('anchorExpression').value;
      const outfit = document.getElementById('anchorOutfit').value;
      const strength = parseFloat(document.getElementById('localStrength').value);
      
      data = await api('/api/images/local/img2img', {
        method: 'POST',
        body: JSON.stringify({
          prompt,
          character,
          expression,
          outfit,
          strength,
          output_path: outputPath,
        }),
      });
    } else {
      // fal.ai cloud generation
      const model = document.getElementById('imgModel').value;
      const preset = document.getElementById('imgPreset').value;
      const numImages = parseInt(document.getElementById('imgCount').value);
      const guidance = parseFloat(document.getElementById('imgGuidance').value);
      const steps = parseInt(document.getElementById('imgSteps').value);

      let width, height;
      if (preset === 'custom') {
        width = parseInt(document.getElementById('imgWidth').value);
        height = parseInt(document.getElementById('imgHeight').value);
      } else {
        ({ width, height } = PRESET_DIMS[preset]);
      }

      const refUrl = document.getElementById('refImageUrl').value.trim() || uploadedRefUrl || null;

      data = await api('/api/images/generate', {
        method: 'POST',
        body: JSON.stringify({
          prompt,
          model,
          width,
          height,
          num_images: numImages,
          guidance_scale: guidance,
          num_inference_steps: steps,
          reference_image_url: refUrl,
          output_path: outputPath,
        }),
      });
    }

    // Show results in gallery
    gallery.innerHTML = '';
    data.images.forEach(img => {
      const imgEl = document.createElement('img');
      imgEl.src = img.url;
      imgEl.title = img.local_path || 'Generated image';
      imgEl.addEventListener('click', () => {
        const editSource = document.getElementById('editSource');
        if (editSource) editSource.value = img.url;
        window.open(img.url, '_blank');
      });
      gallery.appendChild(imgEl);
    });

    resultEl.className = 'result-info success';
    const savedMsg = data.images[0]?.local_path ? ` → Saved to ${data.images[0].local_path}` : '';
    resultEl.textContent = `Generated ${data.images.length} image(s)${savedMsg}`;
    toast('Image generated!', 'success');
  } catch (e) {
    resultEl.className = 'result-info error';
    resultEl.textContent = `Error: ${e.message}`;
    toast(e.message, 'error');
  } finally {
    hideLoading();
  }
}
      body: JSON.stringify({
        prompt,
        model,
        width,
        height,
        num_images: numImages,
        guidance_scale: guidance,
        num_inference_steps: steps,
        reference_image_url: refUrl,
        output_path: outputPath,
      }),
    });

    // Show results in gallery
    gallery.innerHTML = '';
    data.images.forEach(img => {
      const imgEl = document.createElement('img');
      imgEl.src = img.url;
      imgEl.title = img.local_path || 'Generated image';
      imgEl.addEventListener('click', () => {
        // Set as edit source
        document.getElementById('editSource').value = img.url;
        // Also open in new tab for full view
        window.open(img.url, '_blank');
      });
      gallery.appendChild(imgEl);
    });

    resultEl.className = 'result-info success';
    const savedMsg = data.images[0]?.local_path ? ` → Saved to ${data.images[0].local_path}` : '';
    resultEl.textContent = `Generated ${data.images.length} image(s)${savedMsg}`;
    toast('Image generated!', 'success');
  } catch (e) {
    resultEl.className = 'result-info error';
    resultEl.textContent = `Error: ${e.message}`;
    toast(e.message, 'error');
  } finally {
    hideLoading();
  }
}

async function editImage() {
  const imageUrl = document.getElementById('editSource').value.trim();
  const prompt = document.getElementById('editPrompt').value.trim();
  if (!imageUrl) { toast('Provide a source image URL', 'error'); return; }
  if (!prompt) { toast('Enter an edit prompt', 'error'); return; }

  const strength = parseFloat(document.getElementById('editStrength').value);
  const model = document.getElementById('imgModel').value;
  const outputPath = document.getElementById('editOutput').value.trim() || null;

  showLoading('Editing image...');
  const resultEl = document.getElementById('imageResult');
  const gallery = document.getElementById('imageGallery');

  try {
    const data = await api('/api/images/edit', {
      method: 'POST',
      body: JSON.stringify({
        image_url: imageUrl,
        prompt,
        model,
        strength,
        output_path: outputPath,
      }),
    });

    // Add to gallery (don't clear — show before/after)
    data.images.forEach(img => {
      const imgEl = document.createElement('img');
      imgEl.src = img.url;
      imgEl.title = 'Edited';
      imgEl.style.border = '2px solid var(--accent)';
      imgEl.addEventListener('click', () => window.open(img.url, '_blank'));
      gallery.appendChild(imgEl);
    });

    resultEl.className = 'result-info success';
    resultEl.textContent = `Edited image saved`;
    toast('Image edited!', 'success');
  } catch (e) {
    resultEl.className = 'result-info error';
    resultEl.textContent = `Error: ${e.message}`;
    toast(e.message, 'error');
  } finally {
    hideLoading();
  }
}
