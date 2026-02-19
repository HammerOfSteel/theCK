#!/bin/bash
# Start Amelia Studio with all services (Studio UI + SDXL Server)
# NOTE: For cross-platform support (Windows/Linux/macOS), prefer using:
#   python start_studio.py
# This bash script is kept for backwards compatibility on Linux/macOS.

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SDXL_PID=""

# Cleanup function
cleanup() {
    echo ""
    echo "Shutting down services..."
    
    # Stop Docker Compose
    cd "$SCRIPT_DIR/studio"
    docker-compose down
    
    # Stop SDXL server
    if [ ! -z "$SDXL_PID" ]; then
        echo "Stopping SDXL server (PID: $SDXL_PID)..."
        kill $SDXL_PID 2>/dev/null
    fi
    
    # Kill any remaining SDXL processes
    pkill -f "sdxl_img2img_server.py" 2>/dev/null
    
    echo "All services stopped."
    exit 0
}

# Trap Ctrl+C and other exit signals
trap cleanup SIGINT SIGTERM EXIT

echo "========================================="
echo "Amelia Studio Launcher"
echo "========================================="
echo ""
echo "This will start:"
echo "  - SDXL Server (Python, local)"
echo "  - Studio Web UI (Docker)"
echo ""
echo "Note: Qwen3-TTS should already be running on port 42003"
echo ""

# Check dependencies
if ! command -v docker &> /dev/null; then
    echo "ERROR: Docker is not installed"
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "ERROR: docker-compose is not installed"
    exit 1
fi

if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    exit 1
fi

# Create .env if it doesn't exist
cd "$SCRIPT_DIR/studio"
if [ ! -f ".env" ]; then
    echo "Creating .env file from example..."
    cp .env.example .env
    echo ""
    echo "⚠️  Please edit studio/.env to add your FAL_KEY"
    echo "   (Press Ctrl+C to exit and edit, or Enter to continue)"
    read
fi

# Start SDXL Server
echo "========================================="
echo "Starting SDXL Server..."
echo "========================================="
cd "$SCRIPT_DIR"

# Check if venv exists, create if not
if [ ! -d "venv" ]; then
    echo "Creating virtual environment for SDXL server..."
    python3 -m venv venv
    source venv/bin/activate
    pip install -q torch torchvision
    pip install -q diffusers transformers accelerate
    pip install -q pillow fastapi uvicorn pydantic httpx
else
    source venv/bin/activate
fi

# Start SDXL server in background
echo "Launching SDXL server on http://127.0.0.1:7861"
echo "(First run will download ~7GB of models)"
python sdxl_img2img_server.py > sdxl_server.log 2>&1 &
SDXL_PID=$!

# Wait for SDXL to start
echo "Waiting for SDXL server to initialize..."
for i in {1..30}; do
    if curl -s http://127.0.0.1:7861/health > /dev/null 2>&1; then
        echo "✅ SDXL server is ready!"
        break
    fi
    sleep 2
    echo -n "."
done
echo ""

# Start Studio Docker Compose
echo ""
echo "========================================="
echo "Starting Studio Web UI..."
echo "========================================="
cd "$SCRIPT_DIR/studio"
docker-compose up --build

# This line is reached when docker-compose stops
echo ""
echo "Studio stopped."
