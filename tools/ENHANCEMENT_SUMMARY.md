# Amelia Studio — Enhancement Summary

## What Was Done

Successfully removed the problematic multi-image SDXL UI and enhanced the existing studio setup in the theCK repo with:

### 1. **Qwen3-TTS Integration** ✅
- Created `qwen_tts.py` service with 17 character voice definitions
- Each character has authentic mood variations based on dialogue style guide
- API endpoint: `http://127.0.0.1:42003` (your existing local setup)
- API key: `your-api-key-1`

**New Voice Router Endpoints:**
- `GET /api/voice/qwen/characters` - List all characters & moods
- `GET /api/voice/qwen/characters/{character}/moods` - Get moods for a character
- `POST /api/voice/qwen/generate` - Single generation with character/mood selection
- `POST /api/voice/qwen/batch` - CSV batch processing

**Character Voices:**
- Amelia (12 moods: neutral, anxious, vulnerable, passionate, angry, sad, happy, thinking, worried, laughing, determined, tearful, peaceful)
- Ella (4 moods: normal, supportive, worried, hurt)
- Lucas (3 moods: normal, deadpan, vulnerable)
- Zara (3 moods: normal, angry, vulnerable)
- Sarah (4 moods: good_day, dark_humor, opening_up, depressed)
- Prof. Hawthorne (3 moods: lecturing, socratic, vulnerable)
- Dr. Simmons (3 moods: supportive, teaching, vulnerable)
- Maya (3 moods: enthusiastic, spiritual, vulnerable)
- Plus: Raj, Elena, Tasha, Sophia, Liz, Michael, Mr/Mrs James, Lily, Narrator

### 2. **Local SDXL Image-to-Image** ✅
- Created standalone `sdxl_img2img_server.py` (runs outside Docker)
- Runs on CPU to avoid Mac MPS compatibility issues
- Port: `http://127.0.0.1:7861`
- Single anchor image reference (not multi-image)
- Expression and outfit variations per character

**New Image Router Endpoints:**
- `GET /api/images/anchors` - List all character anchors
- `GET /api/images/anchors/{character}` - Get character details
- `GET /api/images/anchors/{character}/preview` - Preview anchor image
- `GET /api/images/local/status` - Check if SDXL server is running
- `POST /api/images/local/img2img` - Single generation with character/expression/outfit
- `POST /api/images/local/batch` - CSV batch processing

### 3. **Character Anchor Data** ✅
- Created `character_anchors.json` with 14 characters
- Each character has:
  - Anchor image filename
  - Multiple expressions (neutral, happy, sad, angry, etc.)
  - Multiple outfits (casual, academic, crisis, summer, etc.)
- Based on actual character design from `Amelia_V2/design/`

### 4. **Batch Processing** ✅
- CSV import for both voice and images
- Character and mood variations in CSV rows
- Auto-generated filenames or custom output paths
- Success/failure tracking per item

### 5. **File Organization** ✅
All outputs save to correct game directories:
- Voice: `Amelia_V2/game/audio/narrator/`
- Images: `Amelia_V2/game/images/characters/{character}/`
- Anchors: `Amelia_V2/game/images/characters/anchors/`

### 6. **Startup Scripts** ✅
- `start_sdxl_server.sh` - Launches local SDXL server
- `start_studio.sh` - Launches main studio UI (Docker)
- Auto-creates venv and installs dependencies

### 7. **Documentation** ✅
- `STUDIO_GUIDE.md` - Complete usage guide with examples
- CSV template examples in `studio/examples/`
- API reference for all endpoints
- Troubleshooting section

---

## File Structure

```
theCK/
├── tools/
│   ├── STUDIO_GUIDE.md              ← Complete documentation
│   ├── start_studio.sh              ← Studio launcher
│   ├── start_sdxl_server.sh         ← SDXL server launcher
│   ├── sdxl_img2img_server.py       ← Standalone SDXL API server
│   └── studio/
│       ├── backend/
│       │   ├── routers/
│       │   │   ├── voice.py         ← Updated with Qwen3-TTS
│       │   │   └── images.py        ← Updated with local SDXL
│       │   ├── services/
│       │   │   ├── qwen_tts.py      ← NEW: Qwen3-TTS client
│       │   │   ├── local_sdxl.py    ← NEW: SDXL client
│       │   │   └── __init__.py      ← Updated exports
│       │   └── data/
│       │       └── character_anchors.json  ← NEW: Character definitions
│       └── examples/
│           ├── voice_batch_example.csv    ← NEW: Voice CSV template
│           └── image_batch_example.csv    ← NEW: Image CSV template
│
└── Amelia_V2/
    ├── design/
    │   ├── characters.md            ← Source of character data
    │   └── dialogue_style_guide.md  ← Source of voice moods
    └── game/
        ├── audio/
        │   └── narrator/            ← Voice output directory
        └── images/
            └── characters/
                ├── anchors/         ← Anchor images go here
                ├── amelia/          ← Generated Amelia variations
                ├── lucas/           ← Generated Lucas variations
                └── ...
```

---

## Next Steps

### 1. Set Up Anchor Images
Place master reference images (character sheets) in:
```
Amelia_V2/game/images/characters/anchors/
├── amelia_anchor.png
├── ella_anchor.png
├── lucas_anchor.png
└── ...
```

Generate these using your preferred AI tool with the prompts from:
- `Amelia_V2/prompts/characters/amelia.md`
- `Amelia_V2/prompts/characters/ella.md`
- etc.

### 2. Start Services

**Terminal 1 - Qwen3-TTS:**
```bash
# (Should already be running on port 42003)
# If not, start it according to your setup
```

**Terminal 2 - SDXL Server:**
```bash
cd /Users/terrygoleman/Documents/dev/theCK/tools
./start_sdxl_server.sh
```

**Terminal 3 - Studio UI:**
```bash
cd /Users/terrygoleman/Documents/dev/theCK/tools
./start_studio.sh
```

### 3. Test Workflows

**Test Voice Generation:**
1. Open http://localhost:8000
2. Go to Voice tab → Qwen3-TTS
3. Select: Character=Amelia, Mood=anxious
4. Enter text, click Generate
5. Check `Amelia_V2/game/audio/narrator/` for output

**Test Image Generation:**
1. Check SDXL status: http://localhost:8000/api/images/local/status
2. Go to Images tab → Local SDXL
3. Select: Character=Amelia, Expression=thinking, Outfit=casual_a
4. Enter prompt, click Generate
5. Check `Amelia_V2/game/images/characters/amelia/` for output

**Test Batch Processing:**
1. Use example CSVs from `tools/studio/examples/`
2. Upload via Batch Mode
3. Review results

---

## What Was Removed

- ❌ `/Users/terrygoleman/Documents/dev/multi-image-ui/` - Deleted entirely
  - The multi-image SDXL approach had Mac MPS compatibility issues
  - Black image output bug was unsolvable with multi-image blending
  - Replaced with cleaner single-anchor approach

---

## Technical Improvements

### Voice System
- **Before**: Only Kokoro TTS with generic voices
- **After**: Qwen3-TTS with character-specific voices and mood variations
- **Benefit**: Authentic character voices matching dialogue style guide

### Image System
- **Before**: Only fal.ai external API for generation
- **After**: Local SDXL img2img with anchor-based consistency
- **Benefit**: Better character consistency, works offline, no API costs for sprites

### Workflow
- **Before**: Manual one-by-one generation
- **After**: CSV batch processing for both voice and images
- **Benefit**: Generate entire scenes or batches of sprites efficiently

### File Organization
- **Before**: Manual file placement
- **After**: Auto-saves to correct game directories
- **Benefit**: Ready for Ren'Py integration without moving files

---

## Troubleshooting

If SDXL gives black images:
- ✅ Fixed by using CPU mode in `sdxl_img2img_server.py`
- The server uses `torch.float32` and `device="cpu"` to avoid Mac MPS issues

If Qwen3-TTS fails:
- Check it's running: `curl http://127.0.0.1:42003/health`
- Verify API key is `your-api-key-1`

If Docker issues:
- Ensure Docker Desktop is running
- Rebuild: `cd tools/studio && docker-compose down && docker-compose up --build`

---

## Summary

✅ **Removed**: Problematic multi-image UI  
✅ **Added**: Qwen3-TTS character voice system  
✅ **Added**: Local SDXL anchor-based image generation  
✅ **Added**: Batch CSV processing for voice & images  
✅ **Added**: Character data mapping from design files  
✅ **Added**: Auto file organization to game directories  
✅ **Added**: Complete documentation & examples  

**Ready to use!** Start with the example CSVs and build your workflows.
