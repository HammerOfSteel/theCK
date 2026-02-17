#!/usr/bin/env python3
"""Inspect the Kokoro TTS API to find available endpoints."""

from gradio_client import Client

KOKORO_API = "http://127.0.0.1:7860/"

print("🔍 Inspecting Kokoro TTS API...")
print("=" * 60)

try:
    client = Client(KOKORO_API)
    print(f"✓ Connected to: {KOKORO_API}")
    print("\n📋 Available API endpoints:\n")
    
    # The client object should have endpoint information
    print(client.view_api())
    
except Exception as e:
    print(f"❌ Error connecting to API: {e}")
    print("\nMake sure Kokoro TTS is running at http://127.0.0.1:7860/")
