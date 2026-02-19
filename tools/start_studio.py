#!/usr/bin/env python3
"""
Amelia Studio Launcher — Cross-platform (Windows / Linux / macOS)
"""

import os
import sys
import json
import time
import shutil
import signal
import platform
import subprocess
import urllib.request
from pathlib import Path

# --- Constants ---
SCRIPT_DIR = Path(__file__).resolve().parent
STUDIO_DIR = SCRIPT_DIR / "studio"
PID_FILE = SCRIPT_DIR / ".studio_pids.json"
IS_WINDOWS = platform.system() == "Windows"
IS_MAC = platform.system() == "Darwin"

# ──────────────────────────────────────────────
# PID & Process Management
# ──────────────────────────────────────────────

def save_pids(sdxl_pid=None):
    pids = load_pids()
    if sdxl_pid:
        pids["sdxl_pid"] = sdxl_pid
    with open(PID_FILE, "w") as f:
        json.dump(pids, f)

def load_pids():
    if PID_FILE.exists():
        try:
            return json.loads(PID_FILE.read_text())
        except:
            return {}
    return {}

def clear_pids():
    if PID_FILE.exists():
        PID_FILE.unlink()

def is_process_alive(pid):
    if not pid: return False
    if IS_WINDOWS:
        try:
            output = subprocess.check_output(['tasklist', '/FI', f'PID eq {pid}'], stderr=subprocess.STDOUT).decode()
            return str(pid) in output
        except: return False
    else:
        try:
            os.kill(pid, 0)
            return True
        except OSError:
            return False

def is_docker_container_running():
    cmd = get_docker_compose_cmd()
    if not cmd: return False
    try:
        result = subprocess.run(cmd + ["ps", "--format", "json"], cwd=STUDIO_DIR, capture_output=True, text=True)
        return "running" in result.stdout.lower()
    except:
        return False

# ──────────────────────────────────────────────
# System Helpers & Docker Control
# ──────────────────────────────────────────────

def which(cmd: str) -> str | None:
    return shutil.which(cmd)

def get_docker_compose_cmd() -> list[str]:
    try:
        subprocess.run(["docker", "compose", "version"], capture_output=True, check=True)
        return ["docker", "compose"]
    except:
        if which("docker-compose"):
            return ["docker-compose"]
    return []

def is_docker_running() -> bool:
    try:
        result = subprocess.run(["docker", "info"], capture_output=True, timeout=5)
        return result.returncode == 0
    except:
        return False

def start_docker_desktop() -> bool:
    """Attempt to launch Docker Desktop based on OS."""
    if is_docker_running(): return True

    if IS_WINDOWS:
        dd_path = Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "Docker" / "Docker" / "Docker Desktop.exe"
        if dd_path.exists():
            subprocess.Popen([str(dd_path)], creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
    elif IS_MAC:
        if Path("/Applications/Docker.app").exists():
            subprocess.Popen(["open", "-a", "Docker"])
    else:
        # Linux
        subprocess.run(["sudo", "systemctl", "start", "docker"], capture_output=True)

    print("Waiting for Docker to start", end="", flush=True)
    for _ in range(30):
        if is_docker_running():
            print(" Ready!")
            return True
        print(".", end="", flush=True)
        time.sleep(2)
    print("\nERROR: Docker timed out.")
    return False

def get_venv_python() -> str:
    venv_dir = SCRIPT_DIR / "venv"
    if IS_WINDOWS:
        return str(venv_dir / "Scripts" / "python.exe")
    return str(venv_dir / "bin" / "python")

def health_check(url: str, timeout: float = 2.0) -> bool:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            return 200 <= response.status < 300
    except:
        return False

# ──────────────────────────────────────────────
# Requirements & Setup
# ──────────────────────────────────────────────

def check_prerequisites():
    if not which("docker"):
        print("ERROR: Docker not found. Please install Docker.")
        return False
    
    if not is_docker_running():
        print("Docker is not running. Attempting to start...")
        if not start_docker_desktop():
            return False
            
    if not get_docker_compose_cmd():
        print("ERROR: docker-compose not found.")
        return False
    return True

def ensure_env_file():
    env_path = STUDIO_DIR / ".env"
    example_path = STUDIO_DIR / ".env.example"
    if not env_path.exists() and example_path.exists():
        print("  Creating .env from example...")
        shutil.copy(example_path, env_path)
        print("  ⚠️  Action Required: Edit studio/.env to add your FAL_KEY.")

def ensure_venv():
    venv_dir = SCRIPT_DIR / "venv"
    py = get_venv_python()
    if not venv_dir.exists():
        print("  Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", str(venv_dir)], check=True)
    
    # Check if psutil is already there to avoid unnecessary pip calls
    try:
        subprocess.run([py, "-c", "import psutil"], check=True, capture_output=True)
    except subprocess.CalledProcessError:
        print("  Installing core dependencies in venv...")
        subprocess.run([py, "-m", "pip", "install", "-q", "psutil", "torch", "torchvision", "diffusers", "transformers", "accelerate", "fastapi", "uvicorn"], check=True)

def detect_and_save_hardware():
    venv_py = get_venv_python()
    # Pass the output directory as an argument to avoid path issues inside the string
    output_path = str(STUDIO_DIR / "output")
    
    detect_code = r'''
import os, platform, json, subprocess, sys
output_dir = sys.argv[1]
try: import psutil
except: psutil = None
try: import torch
except: torch = None

hw = {"platform": platform.system(), "cpu_count": os.cpu_count() or 0, "gpu_tier": "limited", "cuda": False, "mps": False}

if psutil:
    mem = psutil.virtual_memory()
    hw["ram_total_gb"] = round(mem.total / (1024**3), 1)
if torch:
    hw["cuda"] = torch.cuda.is_available()
    if hw["cuda"]:
        hw["gpu_name"] = torch.cuda.get_device_name(0)
        hw["gpu_tier"] = "good"
    elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        hw["gpu_tier"] = "fair"
        hw["mps"] = True

os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "hardware.json"), "w") as f:
    json.dump(hw, f, indent=2)
print(f"  Hardware tier: {hw['gpu_tier']}")
'''
    subprocess.run([venv_py, "-c", detect_code, output_path], check=True)

# ──────────────────────────────────────────────
# Main Logic
# ──────────────────────────────────────────────

def start_sdxl_server():
    server_script = SCRIPT_DIR / "sdxl_img2img_server.py"
    if not server_script.exists(): return None
    
    venv_py = get_venv_python()
    log_file = SCRIPT_DIR / "sdxl_server.log"
    print(f"  Launching SDXL server...")
    
    with open(log_file, "w") as log:
        proc = subprocess.Popen(
            [venv_py, str(server_script)],
            cwd=str(SCRIPT_DIR),
            stdout=log,
            stderr=subprocess.STDOUT,
            creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if IS_WINDOWS else 0,
        )
    return proc

def stop_all():
    print("Stopping all Amelia Studio services...")
    dc_cmd = get_docker_compose_cmd()
    if dc_cmd:
        subprocess.run(dc_cmd + ["down"], cwd=STUDIO_DIR)
    
    # Kill SDXL
    pids = load_pids()
    pid = pids.get("sdxl_pid")
    if pid and is_process_alive(pid):
        if IS_WINDOWS: subprocess.run(["taskkill", "/F", "/PID", str(pid)], capture_output=True)
        else: os.kill(pid, signal.SIGTERM)
    
    # Cleanup orphans
    if IS_WINDOWS:
        subprocess.run(["powershell", "-Command", "Get-Process python* -ErrorAction SilentlyContinue | Where-Object { $_.CommandLine -like '*sdxl_img2img*' } | Stop-Process -Force"], capture_output=True)
    else:
        subprocess.run(["pkill", "-f", "sdxl_img2img_server.py"], capture_output=True)
        
    clear_pids()
    print("Done.")

def show_status():
    pids = load_pids()
    sdxl_up = health_check("http://127.0.0.1:7861/health")
    ui_up = is_docker_container_running()
    print(f"SDXL Server: {'RUNNING' if sdxl_up else 'STOPPED'}")
    print(f"Studio UI:   {'RUNNING' if ui_up else 'STOPPED'}")

def main():
    args = sys.argv[1:]
    if "stop" in args or "--stop" in args:
        stop_all(); return
    if "status" in args or "--status" in args:
        show_status(); return

    mode = "foreground" if ("--fg" in args or "--foreground" in args) else "background"

    print("=========================================")
    print(f"Amelia Studio Launcher [{mode}]")
    print("=========================================")

    if not check_prerequisites(): return
    
    ensure_env_file()
    ensure_venv()
    detect_and_save_hardware()

    # Start SDXL if not alive
    if not health_check("http://127.0.0.1:7861/health"):
        proc = start_sdxl_server()
        if proc: save_pids(proc.pid)

    dc_cmd = get_docker_compose_cmd()
    if mode == "foreground":
        try:
            subprocess.run(dc_cmd + ["up", "--build"], cwd=STUDIO_DIR)
        except KeyboardInterrupt:
            pass
        stop_all()
    else:
        subprocess.run(dc_cmd + ["up", "--build", "-d"], cwd=STUDIO_DIR)
        print("\nStudio running at http://localhost:8500")

if __name__ == "__main__":
    main()