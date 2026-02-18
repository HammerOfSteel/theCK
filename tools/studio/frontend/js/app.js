/**
 * Amelia Studio — Core app module
 * Tab navigation, utilities, toast notifications, prompt browser.
 */

// ---- Utilities ----

async function api(path, options = {}) {
  const res = await fetch(path, {
    headers: { 'Content-Type': 'application/json', ...options.headers },
    ...options,
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: res.statusText }));
    throw new Error(err.detail || 'Request failed');
  }
  return res.json();
}

function toast(message, type = 'info') {
  const container = document.getElementById('toastContainer');
  const el = document.createElement('div');
  el.className = `toast ${type}`;
  el.textContent = message;
  container.appendChild(el);
  setTimeout(() => el.remove(), 5000);
}

function showLoading(text = 'Processing...') {
  const overlay = document.getElementById('loadingOverlay');
  document.getElementById('loadingText').textContent = text;
  overlay.classList.add('visible');
}

function hideLoading() {
  document.getElementById('loadingOverlay').classList.remove('visible');
}

// ---- Tab Navigation ----

document.querySelectorAll('.sidebar-nav li').forEach(li => {
  li.addEventListener('click', () => {
    // Deactivate all
    document.querySelectorAll('.sidebar-nav li').forEach(x => x.classList.remove('active'));
    document.querySelectorAll('.tab-panel').forEach(x => x.classList.remove('active'));
    // Activate clicked
    li.classList.add('active');
    const tabId = `tab-${li.dataset.tab}`;
    document.getElementById(tabId).classList.add('active');
  });
});

// ---- Range inputs: sync value display ----

document.querySelectorAll('input[type="range"]').forEach(range => {
  const valueEl = document.getElementById(range.id + 'Value');
  if (valueEl) {
    range.addEventListener('input', () => { valueEl.textContent = range.value; });
  }
});

// ---- Health Check ----

async function checkHealth() {
  try {
    const data = await api('/api/health');
    const kokoro = document.getElementById('statusKokoro');
    const fal = document.getElementById('statusFal');
    const ffmpeg = document.getElementById('statusFfmpeg');

    kokoro.className = `status-dot ${data.services.kokoro_tts === 'connected' ? 'ok' : 'err'}`;
    kokoro.title = `Kokoro TTS: ${data.services.kokoro_tts}`;

    fal.className = `status-dot ${data.services.fal_ai === 'configured' ? 'ok' : 'err'}`;
    fal.title = `fal.ai: ${data.services.fal_ai}`;

    ffmpeg.className = `status-dot ${data.services.ffmpeg === 'available' ? 'ok' : 'err'}`;
    ffmpeg.title = `ffmpeg: ${data.services.ffmpeg}`;
  } catch (e) {
    console.warn('Health check failed:', e);
  }
}

// ---- Prompt Browser ----

async function loadPrompts() {
  const list = document.getElementById('promptsList');
  try {
    const data = await api('/api/prompts');
    const byCategory = {};

    data.packs.forEach(pack => {
      if (!byCategory[pack.category]) byCategory[pack.category] = [];
      byCategory[pack.category].push(pack);
    });

    list.innerHTML = '';
    for (const [cat, packs] of Object.entries(byCategory)) {
      const catEl = document.createElement('div');
      catEl.className = 'prompt-category';
      catEl.textContent = cat;
      list.appendChild(catEl);

      packs.forEach(pack => {
        const item = document.createElement('div');
        item.className = 'prompt-item';
        item.textContent = pack.name;
        item.addEventListener('click', () => loadPromptContent(pack.path, item));
        list.appendChild(item);
      });
    }
  } catch (e) {
    list.innerHTML = '<p style="padding:12px;color:var(--text-hint)">Could not load prompt packs</p>';
  }
}

async function loadPromptContent(path, itemEl) {
  // Highlight active
  document.querySelectorAll('.prompt-item').forEach(x => x.classList.remove('active'));
  itemEl.classList.add('active');

  const viewer = document.getElementById('promptViewer');
  try {
    const data = await api(`/api/prompts/${path}`);
    viewer.innerHTML = renderMarkdown(data.content);
    addCopyButtons();
  } catch (e) {
    viewer.innerHTML = `<p class="placeholder-text">Error loading prompt pack</p>`;
  }
}

/**
 * Minimal markdown renderer — handles the subset used in prompt packs.
 * Supports: h1-h3, code blocks, inline code, blockquotes, bold, italic,
 * unordered/ordered lists, tables, hr, paragraphs.
 */
function renderMarkdown(md) {
  let html = '';
  const lines = md.split('\n');
  let i = 0;
  let inList = false;
  let listType = '';

  while (i < lines.length) {
    const line = lines[i];

    // Code block
    if (line.startsWith('```')) {
      let code = '';
      i++;
      while (i < lines.length && !lines[i].startsWith('```')) {
        code += escapeHtml(lines[i]) + '\n';
        i++;
      }
      i++; // skip closing ```
      html += `<pre><code>${code.trimEnd()}</code><button class="copy-btn" onclick="copyPrompt(this)">Copy</button></pre>`;
      continue;
    }

    // Table
    if (line.includes('|') && line.trim().startsWith('|')) {
      let tableHtml = '<table>';
      let isHeader = true;
      while (i < lines.length && lines[i].includes('|') && lines[i].trim().startsWith('|')) {
        const row = lines[i].trim();
        // Skip separator row
        if (/^\|[\s\-:|]+\|$/.test(row)) { i++; isHeader = false; continue; }
        const cells = row.split('|').filter((_, idx, arr) => idx > 0 && idx < arr.length - 1);
        const tag = isHeader ? 'th' : 'td';
        tableHtml += '<tr>' + cells.map(c => `<${tag}>${inlineMarkdown(c.trim())}</${tag}>`).join('') + '</tr>';
        if (isHeader) isHeader = false;
        i++;
      }
      tableHtml += '</table>';
      html += tableHtml;
      continue;
    }

    // Headings
    if (line.startsWith('### ')) { html += `<h3>${inlineMarkdown(line.slice(4))}</h3>`; i++; continue; }
    if (line.startsWith('## ')) { html += `<h2>${inlineMarkdown(line.slice(3))}</h2>`; i++; continue; }
    if (line.startsWith('# ')) { html += `<h1>${inlineMarkdown(line.slice(2))}</h1>`; i++; continue; }

    // Blockquote
    if (line.startsWith('> ')) { html += `<blockquote>${inlineMarkdown(line.slice(2))}</blockquote>`; i++; continue; }

    // Horizontal rule
    if (/^---+$/.test(line.trim())) { html += '<hr>'; i++; continue; }

    // Unordered list
    if (/^\s*[-*] /.test(line)) {
      if (!inList || listType !== 'ul') {
        if (inList) html += `</${listType}>`;
        html += '<ul>';
        inList = true;
        listType = 'ul';
      }
      html += `<li>${inlineMarkdown(line.replace(/^\s*[-*] /, ''))}</li>`;
      i++;
      continue;
    }

    // Ordered list
    if (/^\s*\d+\. /.test(line)) {
      if (!inList || listType !== 'ol') {
        if (inList) html += `</${listType}>`;
        html += '<ol>';
        inList = true;
        listType = 'ol';
      }
      html += `<li>${inlineMarkdown(line.replace(/^\s*\d+\. /, ''))}</li>`;
      i++;
      continue;
    }

    // Close list if not a list item
    if (inList) {
      html += `</${listType}>`;
      inList = false;
    }

    // Empty line
    if (line.trim() === '') { i++; continue; }

    // Paragraph
    html += `<p>${inlineMarkdown(line)}</p>`;
    i++;
  }

  if (inList) html += `</${listType}>`;
  return html;
}

function inlineMarkdown(text) {
  text = escapeHtml(text);
  text = text.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
  text = text.replace(/\*(.+?)\*/g, '<em>$1</em>');
  text = text.replace(/`(.+?)`/g, '<code>$1</code>');
  return text;
}

function escapeHtml(text) {
  return text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function copyPrompt(btn) {
  const code = btn.previousElementSibling.textContent;
  navigator.clipboard.writeText(code).then(() => {
    btn.textContent = 'Copied!';
    setTimeout(() => { btn.textContent = 'Copy'; }, 1500);
  });
}

// Make copyPrompt globally accessible
window.copyPrompt = copyPrompt;

// ---- Init ----

document.addEventListener('DOMContentLoaded', () => {
  checkHealth();
  loadPrompts();
  // Refresh health every 30s
  setInterval(checkHealth, 30000);
});
