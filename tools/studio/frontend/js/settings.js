/**
 * Amelia Studio — Settings tab logic.
 * Loads / saves configuration via /api/config and shows hardware info.
 */

(function () {
  'use strict';

  // ── Config keys to UI element mapping ──
  const FIELDS = {
    image_provider:  'cfgImageProvider',
    fal_key:         'cfgFalKey',
    voice_provider:  'cfgVoiceProvider',
    music_provider:  'cfgMusicProvider',
    sdxl_host:       'cfgSdxlHost',
    qwen_host:       'cfgQwenHost',
    kokoro_host:     'cfgKokoroHost',
  };

  // ── Load settings from server ──
  async function loadSettings() {
    try {
      const res = await fetch('/api/config');
      if (!res.ok) return;
      const data = await res.json();
      const cfg = data.config || {};
      for (const [key, elId] of Object.entries(FIELDS)) {
        const el = document.getElementById(elId);
        if (el && cfg[key] !== undefined) {
          el.value = cfg[key];
        }
      }
    } catch (e) {
      console.warn('Failed to load settings', e);
    }
  }

  // ── Save settings ──
  async function saveSettings() {
    const msg = document.getElementById('settingsSaveMsg');
    const config = {};
    for (const [key, elId] of Object.entries(FIELDS)) {
      const el = document.getElementById(elId);
      if (el) config[key] = el.value.trim();
    }
    try {
      const res = await fetch('/api/config', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(config),
      });
      const data = await res.json();
      if (data.ok) {
        msg.textContent = 'Settings saved!';
        msg.style.color = 'var(--success)';
      } else {
        msg.textContent = data.error || 'Save failed';
        msg.style.color = 'var(--danger)';
      }
    } catch (e) {
      msg.textContent = 'Network error';
      msg.style.color = 'var(--danger)';
    }
    setTimeout(() => { msg.textContent = ''; }, 3000);
  }

  // ── Load hardware info ──
  async function loadHardware() {
    const card = document.getElementById('hardwareCard');
    if (!card) return;
    try {
      const res = await fetch('/output/hardware.json');
      if (!res.ok) throw new Error('Not found');
      const hw = await res.json();
      if (!hw) {
        card.innerHTML = '<div class="hw-row"><span class="hw-label">Status</span><span class="hw-value">Hardware info unavailable</span></div>';
        return;
      }

      const tier = hw.gpu_tier || 'unknown';
      const tierColors = { good: 'var(--success)', fair: 'var(--info)', cpu_only: 'var(--accent)', limited: 'var(--danger)' };
      const tierColor = tierColors[tier] || 'var(--text-dim)';

      let html = '';
      html += hwRow('GPU', hw.gpu_name || 'None detected', tierColor);
      html += hwRow('CUDA', hw.cuda ? 'Available' : 'Not available', hw.cuda ? 'var(--success)' : 'var(--text-dim)');
      if (hw.mps) html += hwRow('Apple MPS', 'Available', 'var(--success)');
      html += hwRow('RAM', (hw.ram_total_gb !== undefined && hw.ram_total_gb !== null) ? hw.ram_total_gb + ' GB' : 'Unknown');
      html += hwRow('GPU Tier', tier.replace('_', ' ').toUpperCase(), tierColor);
      if (hw.recommendation) {
        html += '<div class="hw-recommendation">' + hw.recommendation + '</div>';
      }
      card.innerHTML = html;
    } catch (e) {
      card.innerHTML = '<div class="hw-row"><span class="hw-value">Unable to fetch hardware info</span></div>';
    }
  }

  function hwRow(label, value, color) {
    const style = color ? ' style="color:' + color + '"' : '';
    return '<div class="hw-row"><span class="hw-label">' + label + '</span><span class="hw-value"' + style + '>' + value + '</span></div>';
  }

  // ── User info + logout ──
  async function loadUser() {
    try {
      const res = await fetch('/api/auth/me');
      const data = await res.json();
      if (data.authenticated) {
        const el = document.getElementById('settingsUser');
        if (el) el.innerHTML = 'Signed in as <strong>' + data.user.username + '</strong> (' + data.user.role + ')';
      }
    } catch (e) { /* ignore */ }
  }

  function logout() {
    fetch('/api/auth/logout', { method: 'POST' }).then(() => {
      window.location.href = '/login.html';
    });
  }

  // ── Init ──
  document.addEventListener('DOMContentLoaded', () => {
    loadSettings();
    loadHardware();
    loadUser();

    const btnSave = document.getElementById('btnSaveSettings');
    if (btnSave) btnSave.addEventListener('click', saveSettings);

    const btnLogout = document.getElementById('btnLogout');
    if (btnLogout) btnLogout.addEventListener('click', logout);
  });
})();
