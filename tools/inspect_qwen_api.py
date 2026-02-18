#!/usr/bin/env python3
"""Inspect the Qwen3-TTS API to find available endpoints."""

import httpx
import json

QWEN_API = "http://localhost:42003"

print("🔍 Inspecting Qwen3-TTS API...")
print("=" * 60)

async def inspect_api():
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            # Try common documentation endpoints
            endpoints_to_try = [
                "/",
                "/docs",
                "/openapi.json",
                "/api",
                "/api/v1",
                "/api/v1/voices",
                "/api/v1/voice-clone",
                "/api/v1/custom-voice",
                "/health",
            ]
            
            print(f"✓ Attempting to connect to: {QWEN_API}\n")
            
            for endpoint in endpoints_to_try:
                try:
                    print(f"Trying: {endpoint}")
                    response = await client.get(f"{QWEN_API}{endpoint}")
                    if response.status_code == 200:
                        print(f"  ✓ {endpoint} - Status: {response.status_code}")
                        
                        # Try to parse as JSON
                        try:
                            data = response.json()
                            print(f"  JSON Response:")
                            print(f"  {json.dumps(data, indent=2)[:500]}")
                        except:
                            # Print first 300 chars of text
                            text = response.text[:300]
                            print(f"  Text Response (first 300 chars):")
                            print(f"  {text}")
                        print()
                    else:
                        print(f"  ✗ {endpoint} - Status: {response.status_code}")
                except Exception as e:
                    print(f"  ✗ {endpoint} - Error: {str(e)[:100]}")
                print()
            
            # Try to list known API endpoints
            print("\n📋 Known API endpoints from code:")
            print("  POST /api/v1/voice-design/generate - Generate speech with natural language voice description")
            print("  POST /api/v1/custom-voice/generate - Generate speech with preset speaker")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nMake sure Qwen3-TTS is running at http://localhost:42003/")

if __name__ == "__main__":
    import asyncio
    asyncio.run(inspect_api())
