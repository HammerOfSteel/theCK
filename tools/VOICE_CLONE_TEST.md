# Voice Clone Testing Guide

## Quick Test: Inspect Qwen3-TTS Voice Clone API

### Step 1: Open Qwen3-TTS UI in Browser

1. Open your browser and go to the Qwen3-TTS interface (you mentioned it has a Voice Clone tab)
2. Open Developer Tools (F12 or right-click → Inspect)
3. Go to the **Network** tab in Developer Tools

### Step 2: Test Voice Clone Generation

1. Upload one of the reference voices (e.g., `amelia_reference.wav`) to the Voice Clone library
2. Give it a name (e.g., "Amelia")
3. Go to the Voice Clone tab
4. Enter test text: "Hello, this is a test of voice cloning."
5. Select the "Amelia" voice you just uploaded
6. Click Generate
7. **Watch the Network tab** - you'll see the API call

### Step 3: Capture API Details

In the Network tab, find the generation request (usually has "generate" in the name):

**Click on it and check:**

1. **Request URL** - e.g., `http://localhost:42003/api/v1/voice-clone/generate`
2. **Request Method** - POST
3. **Request Headers** - note any special headers
4. **Request Payload** - note the JSON structure, e.g.:
   ```json
   {
     "text": "Hello, this is a test",
     "voice_id": "Amelia",
     "language": "English",
     "speed": 1.0
   }
   ```
5. **Response** - check what the API returns

### Step 4: Report Back

Tell me:
- The exact endpoint path (the part after `localhost:42003`)
- The parameter name for the voice (e.g., `voice_id`, `speaker`, `voice_name`, etc.)
- The full request JSON
- Whether voice ID is a string (e.g., "Amelia") or something else

## Quick Test Script

Alternatively, I can create a test script to try different API endpoints. Once you upload one reference voice to the library, run this:

```bash
cd /Users/terrygoleman/Documents/dev/theCK
python3 tools/test_voice_clone_api.py "Amelia" "Hello, this is a test."
```

This will try common patterns and tell us which one works.

## Example API Patterns

Based on common TTS systems, the API likely uses one of these patterns:

### Pattern 1: Custom Voice API
```
POST http://localhost:42003/api/v1/custom-voice/generate
{
  "text": "Hello",
  "speaker": "Amelia",
  "language": "English",
  "speed": 1.0,
  "response_format": "base64"
}
```

### Pattern 2: Voice Clone API
```
POST http://localhost:42003/api/v1/voice-clone/generate  
{
  "text": "Hello",
  "voice_id": "Amelia",
  "language": "English",
  "speed": 1.0,
  "response_format": "base64"
}
```

### Pattern 3: Unified Generate API
```
POST http://localhost:42003/api/v1/generate
{
  "text": "Hello",
  "voice_name": "Amelia",
  "mode": "clone",
  "language": "English",
  "speed": 1.0,
  "response_format": "base64"
}
```

## Once We Know the API

Once you report back the exact API format, I'll:

1. Update `qwen_tts_clone.py` with the correct endpoint and parameters
2. Update the batch generation to use voice cloning
3. Test it on a few lines to verify consistency
4. Then you can regenerate all chapters with consistent voices
