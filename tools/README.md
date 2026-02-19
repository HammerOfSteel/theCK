# The CK — Development Tools

Tools and utilities for creating content for The CK visual novel (Amelia V2).

## 🎨 Amelia Studio (Main Tool)

Enhanced creative studio for voice and image generation with character-aware features.

**Location:** `tools/studio/`

**Quick Start:**
```bash
cd tools
./start_studio.sh
```

**Features:**
- ✅ **Qwen3-TTS Voice Generation** — Character-based TTS with mood variations
- ✅ **Local SDXL Image Generation** — Anchor-based character sprite creation
- ✅ **fal.ai Integration** — External API for additional models
- ✅ **Batch CSV Processing** — Bulk voice & image generation
- ✅ **Auto File Organization** — Saves to correct game directories
- ✅ **Robust Hardware Info** — Hardware details (CPU, RAM, GPU, etc.) are always shown in the Studio UI, read directly from `/output/hardware.json` at startup—independent of SDXL or backend status.

**Documentation:** [STUDIO_GUIDE.md](./STUDIO_GUIDE.md)  
**Enhancement Summary:** [ENHANCEMENT_SUMMARY.md](./ENHANCEMENT_SUMMARY.md)

---

## 🖼️ Local SDXL Server

Standalone image-to-image generation server for character sprites.

**Location:** `tools/sdxl_img2img_server.py`

**Quick Start:**
```bash
cd tools
./start_sdxl_server.sh
```

**Details:**
- Runs on `http://127.0.0.1:7861`
- Uses CPU mode (Mac-compatible, no MPS issues)
- Generates character variations from anchor images
- First run downloads ~7GB of models

---

## 🔧 Utility Scripts

### Audio Conversion
- `convert_to_ogg.py` — Convert audio to OGG Vorbis
- `convert_to_vorbis.py` — Convert to OGG Vorbis (alternative)
- `convert_to_wav.py` — Convert to WAV format

### Voice Generation (Legacy)
- `generate_narrator_voice_ch1.py` — Chapter 1 narrator voice generation
- `integrate_voice_ch1.py` — Integrate voices into Ren'Py script
- `test_kokoro_api.py` — Test Kokoro TTS API

### Kokoro TTS Utilities  
- `inspect_kokoro_api.py` — Inspect Kokoro API endpoints

### Translation
- `translate_common_sv.py` — Translate common strings to Swedish

### Map Generation
- `generate_world_map.py` — Generate world/location maps

---

## 📁 Project Structure

```
tools/
├── studio/                    ← Main Studio (Docker-based)
│   ├── backend/               ← FastAPI backend
│   │   ├── routers/           ← API endpoints
│   │   │   ├── voice.py       ← Kokoro + Qwen3-TTS
│   │   │   ├── images.py      ← fal.ai + Local SDXL
│   │   │   └── batch.py       ← Batch processing
│   │   ├── services/          ← Business logic
│   │   │   ├── kokoro.py
│   │   │   ├── qwen_tts.py    ← Character voices
│   │   │   ├── local_sdxl.py  ← SDXL client
│   │   │   ├── fal_ai.py
│   │   │   └── audio.py
│   │   └── data/
│   │       └── character_anchors.json  ← Character definitions
│   ├── frontend/              ← UI (Gradio/custom)
│   └── examples/              ← CSV templates
│       ├── voice_batch_example.csv
│       └── image_batch_example.csv
│
├── sdxl_img2img_server.py     ← Standalone SDXL server
├── start_studio.sh            ← Studio launcher
├── start_sdxl_server.sh       ← SDXL launcher
│
├── STUDIO_GUIDE.md            ← Complete usage guide
├── ENHANCEMENT_SUMMARY.md     ← What's new
└── README.md                  ← This file
```

---

## 🚀 Workflows

### Voice Generation Workflow

1. **Single Character Line:**
   - Open Studio → Voice → Qwen3-TTS
   - Select character & mood
   - Enter dialogue
   - Generate

2. **Batch Scene:**
   - Create CSV: `text,character,mood,speed,output_path`
   - Upload via Batch Mode
   - Files auto-save to `Amelia_V2/game/audio/narrator/`

### Image Generation Workflow

1. **Single Character Sprite:**
   - Open Studio → Images → Local SDXL
   - Select character, expression, outfit
   - Enter prompt modification
   - Generate

2. **Batch Sprite Set:**
   - Create CSV: `prompt,character,expression,outfit,strength,output_path`
   - Upload via Batch Mode
   - Files auto-save to `Amelia_V2/game/images/characters/{character}/`

---

## 📖 Character Reference

**Available Characters:**
- Amelia James (12 moods)
- Ella Chen (4 moods)
- Lucas Adeyemi (3 moods)
- Zara Okafor (3 moods)
- Raj Sharma (2 moods)
- Sarah Whitmore (4 moods)
- Maya Patel (3 moods)
- Prof. Arthur Hawthorne (3 moods)
- Dr. Nadia Simmons (3 moods)
- Elena Trevorran (3 moods)
- Tasha Reynolds (3 moods)
- Sophia Langford (2 moods)
- Liz Torres (2 moods)
- Michael Okonkwo (2 moods)
- Mr. James, Mrs. James, Lily James, Narrator

**Character Data:**
- Voices: `tools/studio/backend/services/qwen_tts.py`
- Visuals: `tools/studio/backend/data/character_anchors.json`
- Design: `Amelia_V2/design/characters.md`
- Dialogue: `Amelia_V2/design/dialogue_style_guide.md`

---

## 🔌 API Endpoints

### Voice
- `GET /api/voice/qwen/characters` — List all characters
- `POST /api/voice/qwen/generate` — Single generation
- `POST /api/voice/qwen/batch` — CSV batch

### Images
- `GET /api/images/anchors` — List character anchors
- `GET /api/images/anchors/{character}/preview` — Preview anchor
- `POST /api/images/local/img2img` — Single generation
- `POST /api/images/local/batch` — CSV batch

Full API reference: [STUDIO_GUIDE.md](./STUDIO_GUIDE.md#api-reference)

---

## ⚙️ Configuration

**Studio Config:** `tools/studio/.env`
```bash
FAL_KEY=your_fal_ai_key_here
```

**Qwen3-TTS:**
- URL: `http://127.0.0.1:42003`
- API Key: `your-api-key-1`

**Local SDXL:**
- URL: `http://127.0.0.1:7861`
- Auto-configured (started via script)

---

## 🐛 Troubleshooting

**Studio won't start:**
- Ensure Docker Desktop is running
- Check: `docker-compose logs`

**SDXL gives errors:**
- First run downloads models (~7GB)
- Leave terminal open while using
- Check: `curl http://127.0.0.1:7861/health`

**Qwen3-TTS not responding:**
- Ensure service is running on port 42003
- Check API key is `your-api-key-1`

**Black images (should be fixed):**
- The SDXL server now uses CPU mode
- No more Mac MPS issues

Full troubleshooting: [STUDIO_GUIDE.md](./STUDIO_GUIDE.md#troubleshooting)

---

## 📝 Examples

**Voice CSV:**
```csv
text,character,mood,speed,output_path
"I understand.",Lucas,normal,0.9,lucas_response.wav
"You're surviving.",Ella,supportive,1.0,ella_supportive.wav
```

**Image CSV:**
```csv
prompt,character,expression,outfit,strength,output_path
"Thoughtful in autumn light",Amelia,thinking,casual_a,0.6,amelia_thinking.png
"Genuine smile at sunset",Amelia,happy,casual_a,0.6,amelia_happy.png
```

See `tools/studio/examples/` for full templates.

---

## 🎯 Quick Commands

**Start Everything:**
```bash
# Terminal 1 - SDXL
cd tools && ./start_sdxl_server.sh

# Terminal 2 - Studio
cd tools && ./start_studio.sh
```

**Test Studio:**
```bash
curl http://localhost:8000/api/voice/qwen/characters
curl http://localhost:8000/api/images/anchors
```

**Test SDXL:**
```bash
curl http://127.0.0.1:7861/health
```

---

## 📚 Further Reading

- [STUDIO_GUIDE.md](./STUDIO_GUIDE.md) — Complete usage documentation
- [ENHANCEMENT_SUMMARY.md](./ENHANCEMENT_SUMMARY.md) — What's new in this version
- `Amelia_V2/design/` — Character & dialogue style guides
- `Amelia_V2/prompts/` — Image generation prompts

---

**Ready to create!** Start with the Studio and explore the character voices and anchor images.
