# Voice Cloning Guide for Qwen3-TTS

## Overview

This guide explains how to use voice cloning with Qwen3-TTS for consistent character voices in The CK visual novel.

## Problem: Voice Inconsistency

When using Voice Design API directly, each generation creates a slightly different voice based on the natural language description. This causes characters to sound different across multiple dialogue lines.

## Solution: Two-Step Voice Cloning

### Step 1: Generate Reference Voices (DONE ✓)

We've created reference voice samples for all 18 characters using the Voice Design API. These are located in:

```
Amelia_V2/game/audio/voice_references/
```

Files generated:
- `amelia_reference.wav`
- `ella_reference.wav`
- `prof._hawthorne_reference.wav`
- `dr._simmons_reference.wav`
- `maya_reference.wav`
- `lucas_reference.wav`
- `zara_reference.wav`
- `raj_reference.wav`
- `sarah_reference.wav`
- `elena_reference.wav`
- `tasha_reference.wav`
- `michael_reference.wav`
- `sophia_reference.wav`
- `liz_reference.wav`
- `mr._james_reference.wav`
- `mrs._james_reference.wav`
- `lily_reference.wav`
- `narrator_reference.wav`

### Step 2: Add Voices to Qwen3-TTS Library

**Manual Process (via Qwen3-TTS UI):**

1. Open Qwen3-TTS UI (the one you mentioned has a "Voice Clone" tab)
2. Navigate to the **Voice Clone** tab
3. For each character:
   - Click "Upload Reference Audio" or similar
   - Select the character's `_reference.wav` file
   - Give it a name (e.g., "Amelia", "Ella", "Prof. Hawthorne")
   - Save to the voice library
4. **Important**: Note the exact voice ID or name that Qwen3-TTS assigns to each character

**Expected Voice Library Names:**
After uploading, you should have voices like:
```
Amelia
Ella
Prof. Hawthorne
Dr. Simmons
Maya
Lucas
Zara
Raj
Sarah
Elena
Tasha
Michael
Sophia
Liz
Mr. James
Mrs. James
Lily
Narrator
```

### Step 3: Using Voice Cloning API

Once voices are in the library, we can use them via the Voice Clone or Custom Voice API endpoint.

**Typical API endpoints:**
- Voice Design (current):  `/api/v1/voice-design/generate`
- Custom Voice (preset speakers): `/api/v1/custom-voice/generate`  
- Voice Clone (your saved voices): `/api/v1/voice-clone/generate` or `/api/v1/custom-voice/generate`

**Request format for voice cloning:**
```json
{
  "text": "Hello, this is Amelia speaking.",
  "voice_id": "Amelia",  // or "speaker": "Amelia"
  "language": "English",
  "speed": 1.0,
  "response_format": "base64"
}
```

### Step 4: Update Batch Generation

Once you've uploaded the voices to the Qwen3-TTS library and noted their IDs, we'll update the batch generation code to use voice cloning instead of voice design.

## API Endpoint Detection

We need to determine the exact endpoint and parameter names. Options:

1. **Check Qwen3-TTS Documentation**
   - Look for API docs on how to use saved/cloned voices

2. **Inspect the Voice Clone tab**
   - Open browser dev tools (F12)
   - Go to Voice Clone tab
   - Generate a test voice
   - Check the Network tab to see the API call

3. **Try common patterns:**
   - `/api/v1/voice-clone/generate` with `voice_id`
   - `/api/v1/custom-voice/generate` with `speaker`
   - `/api/v1/generate` with `voice_name`

## Next Steps for You

1. **Test the reference voices:**
   ```bash
   open /Users/terrygoleman/Documents/dev/theCK/Amelia_V2/game/audio/voice_references/
   ```
   Listen to a few to verify quality.

2. **Upload to Qwen3-TTS:**
   - Open the Qwen3-TTS UI
   - Go to Voice Clone tab
   - Upload all 18 reference files
   - Note the voice IDs assigned

3. **Find the voice clone API endpoint:**
   - Use browser dev tools to inspect a voice clone generation
   - OR check Qwen3-TTS documentation
   - Note the endpoint path and parameter names

4. **Report back:**
   Tell me:
   - The API endpoint URL (e.g., `/api/v1/voice-clone/generate`)
   - The parameter name for the voice (e.g., `voice_id`, `speaker`, `voice_name`)
   - Example request/response from the UI

Then I'll update the batch generation code to use voice cloning for consistent voices.

## Benefits

Once implemented:
- ✅ Consistent character voices across all dialogue
- ✅ Amelia always sounds like Amelia
- ✅ No variation between different generations
- ✅ Faster generation (voice cloning is usually faster than voice design)
- ✅ Better quality (cloning from a reference is more stable)

## Troubleshooting

**If voices still sound different:**
- Check that you're using the voice clone endpoint, not voice design
- Verify the voice ID matches exactly
- Ensure the reference audio quality is good
- Try regenerating the reference with different sample text if needed

**If upload fails:**
- Check file format (WAV should work)
- Try converting to a different sample rate (16kHz or 22kHz)
- Check file size limits in Qwen3-TTS
