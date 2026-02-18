/**
 * Amelia Studio — Batch processing module (CSV import)
 */

document.addEventListener('DOMContentLoaded', () => {
  initBatch();
  initChapterGeneration();
});

let batchRows = [];
let currentJobId = null;
let pollInterval = null;

function initBatch() {
  const csvArea = document.getElementById('csvUploadArea');
  const csvInput = document.getElementById('csvFileInput');

  csvArea.addEventListener('click', () => csvInput.click());

  csvArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    csvArea.classList.add('dragover');
  });

  csvArea.addEventListener('dragleave', () => csvArea.classList.remove('dragover'));

  csvArea.addEventListener('drop', (e) => {
    e.preventDefault();
    csvArea.classList.remove('dragover');
    if (e.dataTransfer.files.length) handleCsvFile(e.dataTransfer.files[0]);
  });

  csvInput.addEventListener('change', () => {
    if (csvInput.files.length) handleCsvFile(csvInput.files[0]);
  });

  document.getElementById('btnDownloadTemplate').addEventListener('click', downloadTemplate);
  document.getElementById('btnRunBatch').addEventListener('click', runBatch);
  document.getElementById('btnClearBatch').addEventListener('click', clearBatch);
}

async function handleCsvFile(file) {
  const formData = new FormData();
  formData.append('file', file);

  try {
    const res = await fetch('/api/batch/parse-csv', { method: 'POST', body: formData });
    if (!res.ok) throw new Error('Failed to parse CSV');
    const data = await res.json();

    batchRows = data.rows;
    renderBatchTable();
    document.getElementById('csvUploadLabel').textContent = `Loaded: ${file.name}`;
    toast(`Parsed ${data.count} rows from CSV`, 'success');
  } catch (e) {
    toast(`CSV parse error: ${e.message}`, 'error');
  }
}

function renderBatchTable() {
  const preview = document.getElementById('batchPreview');
  const tbody = document.getElementById('batchTableBody');
  const count = document.getElementById('batchCount');

  preview.hidden = false;
  count.textContent = batchRows.length;
  tbody.innerHTML = '';

  batchRows.forEach((row, i) => {
    const tr = document.createElement('tr');

    const typeIcons = { voice: '🎙️', image: '🖼️', image_edit: '✏️' };
    const modelOrVoice = row.type === 'voice' ? (row.voice || '—').substring(0, 20) : (row.model || '—');
    const size = row.type !== 'voice' ? `${row.width}×${row.height}` : '—';

    tr.innerHTML = `
      <td>${i + 1}</td>
      <td>${typeIcons[row.type] || '?'} ${row.type || 'unknown'}</td>
      <td title="${escapeAttr(row.prompt)}">${truncate(row.prompt, 60)}</td>
      <td title="${escapeAttr(row.output_path)}">${truncate(row.output_path, 40)}</td>
      <td>${modelOrVoice}</td>
      <td>${size}</td>
      <td><span class="badge badge-pending" id="rowStatus_${i}">pending</span></td>
    `;

    tbody.appendChild(tr);
  });
}

function downloadTemplate() {
  window.location.href = '/api/batch/csv-template';
}

async function runBatch() {
  if (!batchRows.length) { toast('Load a CSV first', 'error'); return; }

  const progressSection = document.getElementById('batchProgress');
  progressSection.hidden = false;

  // Mark all as running
  batchRows.forEach((_, i) => {
    const badge = document.getElementById(`rowStatus_${i}`);
    if (badge) { badge.className = 'badge badge-pending'; badge.textContent = 'queued'; }
  });

  try {
    const data = await api('/api/batch/run', {
      method: 'POST',
      body: JSON.stringify({ rows: batchRows }),
    });

    currentJobId = data.job_id;
    toast(`Batch started: ${data.total} jobs`, 'info');

    // Start polling
    if (pollInterval) clearInterval(pollInterval);
    pollInterval = setInterval(pollBatchStatus, 2000);
  } catch (e) {
    toast(`Batch failed: ${e.message}`, 'error');
  }
}

async function pollBatchStatus() {
  if (!currentJobId) return;

  try {
    const data = await api(`/api/batch/status/${currentJobId}`);

    // Update progress bar
    const pct = data.total > 0 ? (data.completed + data.failed) / data.total * 100 : 0;
    document.getElementById('progressFill').style.width = `${pct}%`;
    document.getElementById('progressText').textContent =
      `${data.completed + data.failed} / ${data.total} (${data.failed} failed)`;

    // Update row statuses
    data.results.forEach(r => {
      const badge = document.getElementById(`rowStatus_${r.index}`);
      if (badge) {
        if (r.status === 'ok') {
          badge.className = 'badge badge-ok';
          badge.textContent = 'done';
        } else if (r.status === 'error') {
          badge.className = 'badge badge-error';
          badge.textContent = 'error';
          badge.title = r.error || '';
        }
      }
    });

    // Mark currently processing row
    const processing = data.completed + data.failed;
    if (processing < data.total) {
      const badge = document.getElementById(`rowStatus_${processing}`);
      if (badge && badge.textContent === 'queued') {
        badge.className = 'badge badge-running';
        badge.textContent = 'running';
      }
    }

    // Done?
    if (data.status !== 'running') {
      clearInterval(pollInterval);
      pollInterval = null;
      currentJobId = null;
      const msg = data.failed > 0
        ? `Batch complete with ${data.failed} error(s)`
        : `Batch complete: ${data.completed} items processed`;
      toast(msg, data.failed > 0 ? 'error' : 'success');
    }
  } catch (e) {
    console.warn('Poll failed:', e);
  }
}

function clearBatch() {
  batchRows = [];
  document.getElementById('batchPreview').hidden = true;
  document.getElementById('batchProgress').hidden = true;
  document.getElementById('csvUploadLabel').textContent = 'Click or drag CSV file here';
  document.getElementById('csvFileInput').value = '';
  if (pollInterval) { clearInterval(pollInterval); pollInterval = null; }
  currentJobId = null;
}

// -- Helpers --

function truncate(str, max) {
  if (!str) return '';
  return str.length > max ? str.slice(0, max) + '…' : str;
}

function escapeAttr(str) {
  if (!str) return '';
  return str.replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}


// ============================================================================
// CHAPTER GENERATION
// ============================================================================

let chapters = [];
let currentChapterJobId = null;
let chapterPollInterval = null;

function initChapterGeneration() {
  // Load chapters
  loadChapters();

  // Event listeners
  document.getElementById('chapterSelect').addEventListener('change', onChapterSelect);
  document.getElementById('btnGenerateChapter').addEventListener('click', generateChapter);
  document.getElementById('btnRefreshChapters').addEventListener('click', loadChapters);
}

async function loadChapters() {
  const select = document.getElementById('chapterSelect');
  select.innerHTML = '<option value="">Loading chapters...</option>';
  select.disabled = true;

  try {
    const data = await api('/api/batch/chapters');
    chapters = data.chapters;

    select.innerHTML = '<option value="">Select a chapter...</option>';
    chapters.forEach(ch => {
      const option = document.createElement('option');
      option.value = ch.name;
      option.textContent = `${ch.display_name} (${ch.line_count} lines)`;
      option.dataset.lineCount = ch.line_count;
      option.dataset.fileName = ch.file;
      select.appendChild(option);
    });

    select.disabled = false;
    toast(`Loaded ${chapters.length} chapters`, 'success');
  } catch (e) {
    select.innerHTML = '<option value="">Error loading chapters</option>';
    toast(`Failed to load chapters: ${e.message}`, 'error');
  }
}

function onChapterSelect() {
  const select = document.getElementById('chapterSelect');
  const selectedOption = select.options[select.selectedIndex];
  const chapterInfo = document.getElementById('chapterInfo');
  const btn = document.getElementById('btnGenerateChapter');

  if (!select.value) {
    chapterInfo.hidden = true;
    btn.disabled = true;
    return;
  }

  // Show chapter info
  document.getElementById('chapterLineCount').textContent = selectedOption.dataset.lineCount;
  document.getElementById('chapterFileName').textContent = selectedOption.dataset.fileName;
  chapterInfo.hidden = false;
  btn.disabled = false;
}

async function generateChapter() {
  const chapterSelect = document.getElementById('chapterSelect');
  const providerSelect = document.getElementById('chapterProvider');
  const backupCheckbox = document.getElementById('chapterBackup');

  const chapter = chapterSelect.value;
  if (!chapter) {
    toast('Please select a chapter', 'error');
    return;
  }

  const provider = providerSelect.value;
  const backup = backupCheckbox.checked;

  // Show progress
  const progressSection = document.getElementById('chapterProgress');
  progressSection.hidden = false;
  document.getElementById('chapterProgressFill').style.width = '0%';
  document.getElementById('chapterProgressText').textContent = '0 / 0';
  document.getElementById('chapterProgressStats').textContent = '';

  // Disable button
  document.getElementById('btnGenerateChapter').disabled = true;
  toast(`Starting chapter generation: ${chapter}`, 'info');

  try {
    const data = await api('/api/batch/generate-chapter', {
      method: 'POST',
      body: JSON.stringify({ chapter, provider, backup_existing: backup }),
    });

    currentChapterJobId = data.job_id;
    toast(`Chapter generation started: ${data.total} lines`, 'success');

    // Start polling
    if (chapterPollInterval) clearInterval(chapterPollInterval);
    chapterPollInterval = setInterval(pollChapterStatus, 1000);
  } catch (e) {
    toast(`Failed to start generation: ${e.message}`, 'error');
    document.getElementById('btnGenerateChapter').disabled = false;
    progressSection.hidden = true;
  }
}

async function pollChapterStatus() {
  if (!currentChapterJobId) return;

  try {
    const data = await api(`/api/batch/status/${currentChapterJobId}`);

    // Update progress bar
    const pct = data.total > 0 ? (data.completed + data.failed + data.skipped) / data.total * 100 : 0;
    document.getElementById('chapterProgressFill').style.width = `${pct}%`;

    // Update progress text
    const completed = data.completed + data.failed + data.skipped;
    document.getElementById('chapterProgressText').textContent = `${completed} / ${data.total}`;

    // Update stats
    const stats = [];
    if (data.completed > 0) stats.push(`✅ ${data.completed} generated`);
    if (data.failed > 0) stats.push(`❌ ${data.failed} failed`);
    if (data.skipped > 0) stats.push(`⏭️ ${data.skipped} skipped`);
    if (data.backed_up > 0) stats.push(`💾 ${data.backed_up} backed up`);
    document.getElementById('chapterProgressStats').textContent = stats.join(' • ');

    // Done?
    if (data.status !== 'running') {
      clearInterval(chapterPollInterval);
      chapterPollInterval = null;
      currentChapterJobId = null;
      document.getElementById('btnGenerateChapter').disabled = false;

      const msg = data.failed > 0
        ? `Chapter complete with ${data.failed} error(s)`
        : `Chapter complete: ${data.completed} lines generated`;
      toast(msg, data.failed > 0 ? 'warning' : 'success');

      // Log errors if any
      if (data.failed > 0) {
        const errors = data.results.filter(r => r.status === 'error');
        console.error('Chapter generation errors:', errors);
      }
    }
  } catch (e) {
    console.warn('Chapter poll failed:', e);
  }
}
