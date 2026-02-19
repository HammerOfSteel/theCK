/**
 * Amelia Studio — Status bar module
 * Live service status monitoring and log viewer.
 */

const STATUS_COLORS = {
  running: 'ok',
  loading: 'warn',
  stopped: 'err',
  error:   'err',
};

const STATUS_LABELS = {
  running: 'Running',
  loading: 'Loading',
  stopped: 'Stopped',
  error:   'Error',
};

let statusBarOpen = false;
let logRefreshInterval = null;

// ---- Status Bar Toggle ----

function initStatusBar() {
  const toggle = document.getElementById('statusBarToggle');
  const body = document.getElementById('statusBarBody');
  const bar = document.getElementById('statusBar');

  toggle.addEventListener('click', () => {
    statusBarOpen = !statusBarOpen;
    bar.classList.toggle('open', statusBarOpen);

    if (statusBarOpen) {
      refreshLogs();
      startLogPolling();
    } else {
      stopLogPolling();
    }
  });

  document.getElementById('btnRefreshLogs').addEventListener('click', refreshLogs);

  // Initial status fetch
  refreshStatus();
  // Poll status every 15s
  setInterval(refreshStatus, 15000);
}

// ---- Service Status ----

async function refreshStatus() {
  try {
    const data = await api('/api/status');
    renderStatusDots(data.services);
    renderStatusCards(data.services);
    updateStatusSummary(data.services);
  } catch (e) {
    console.warn('Status fetch failed:', e);
  }
}

function renderStatusDots(services) {
  const container = document.getElementById('statusBarDots');
  container.innerHTML = '';
  services.forEach(svc => {
    const dot = document.createElement('span');
    dot.className = `sbar-dot ${STATUS_COLORS[svc.status] || 'err'}`;
    dot.title = `${svc.name}: ${svc.detail}`;
    container.appendChild(dot);
  });
}

function renderStatusCards(services) {
  const container = document.getElementById('statusCards');
  container.innerHTML = '';
  services.forEach(svc => {
    const card = document.createElement('div');
    card.className = `status-card ${STATUS_COLORS[svc.status] || 'err'}`;
    card.innerHTML = `
      <div class="status-card-indicator"></div>
      <div class="status-card-info">
        <span class="status-card-name">${svc.name}</span>
        <span class="status-card-detail">${svc.detail}</span>
      </div>
      <span class="status-card-badge">${STATUS_LABELS[svc.status] || svc.status}</span>
    `;
    container.appendChild(card);
  });
}

function updateStatusSummary(services) {
  const running = services.filter(s => s.status === 'running').length;
  const total = services.length;
  const el = document.getElementById('statusBarSummary');
  el.textContent = `${running}/${total} services`;
}

// ---- Log Viewer ----

async function refreshLogs() {
  const output = document.getElementById('logOutput');
  try {
    const data = await api('/api/status/logs?lines=120&service=sdxl');
    if (data.log) {
      output.textContent = data.log;
      if (document.getElementById('logAutoScroll').checked) {
        output.scrollTop = output.scrollHeight;
      }
    }
  } catch (e) {
    output.textContent = '(Could not fetch logs)';
  }
}

function startLogPolling() {
  if (logRefreshInterval) return;
  logRefreshInterval = setInterval(refreshLogs, 5000);
}

function stopLogPolling() {
  if (logRefreshInterval) {
    clearInterval(logRefreshInterval);
    logRefreshInterval = null;
  }
}

// ---- Init ----

document.addEventListener('DOMContentLoaded', initStatusBar);
