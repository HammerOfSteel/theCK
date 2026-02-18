#!/bin/bash
# Start SDXL Img2Img Server
# This runs the local SDXL server for character image generation

cd "$(dirname "$0")"

echo "Starting SDXL Img2Img Server..."
echo "This will download models on first run (~7GB)"
echo ""

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate venv
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -q torch torchvision
pip install -q diffusers transformers accelerate
pip install -q pillow fastapi uvicorn pydantic httpx

echo ""
echo "Starting server on http://127.0.0.1:7861"
echo "Leave this terminal open while using the studio"
echo ""

python sdxl_img2img_server.py
