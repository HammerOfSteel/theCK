/**
 * Amelia Studio — Image generation module (fal.ai)
 */

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
  // Load models
  try {
    const data = await api('/api/images/models');
    const select = document.getElementById('imgModel');
    data.models.forEach(m => {
      const opt = document.createElement('option');
      opt.value = m.key;
      opt.textContent = m.label;
      select.appendChild(opt);
    });
  } catch (e) {
    console.warn('Could not load models:', e);
  }

  // Preset change
  document.getElementById('imgPreset').addEventListener('change', (e) => {
    const custom = document.getElementById('customDims');
    if (e.target.value === 'custom') {
      custom.style.display = 'flex';
    } else {
      custom.style.display = 'none';
    }
  });

  // Reference image upload
  const refArea = document.getElementById('refUploadArea');
  const refInput = document.getElementById('refFileInput');
  const refPreview = document.getElementById('refPreview');
  const refClear = document.getElementById('refClear');
  const refLabel = document.getElementById('refUploadLabel');

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

  refInput.addEventListener('change', () => {
    if (refInput.files.length) uploadReference(refInput.files[0]);
  });

  refClear.addEventListener('click', (e) => {
    e.stopPropagation();
    uploadedRefUrl = null;
    refPreview.hidden = true;
    refClear.hidden = true;
    refLabel.hidden = false;
    document.getElementById('refImageUrl').value = '';
  });

  // Generate button
  document.getElementById('btnGenImage').addEventListener('click', generateImage);

  // Edit button
  document.getElementById('btnEditImage').addEventListener('click', editImage);
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

  const model = document.getElementById('imgModel').value;
  const preset = document.getElementById('imgPreset').value;
  const numImages = parseInt(document.getElementById('imgCount').value);
  const guidance = parseFloat(document.getElementById('imgGuidance').value);
  const steps = parseInt(document.getElementById('imgSteps').value);
  const outputPath = document.getElementById('imgOutput').value.trim() || null;

  let width, height;
  if (preset === 'custom') {
    width = parseInt(document.getElementById('imgWidth').value);
    height = parseInt(document.getElementById('imgHeight').value);
  } else {
    ({ width, height } = PRESET_DIMS[preset]);
  }

  // Reference image: from upload or URL input
  const refUrl = document.getElementById('refImageUrl').value.trim() || uploadedRefUrl || null;

  showLoading('Generating image...');
  const resultEl = document.getElementById('imageResult');
  const gallery = document.getElementById('imageGallery');

  try {
    const data = await api('/api/images/generate', {
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
