# Track: Amelia Studio (AI Asset Pipeline)

> A build track for **Amelia Studio** — a local, automated visual-novel asset studio that generates
> every character (in every outfit, pose, and emotion) and every background, then delivers them into the
> Ren'Py game. Built on **ComfyUI + VNCCS** for image generation and **Kokoro TTS** for voice, wrapped in
> our own **Studio UI + automation layer**.
>
> **This replaces the former "procedural generation" R&D track.** We are no longer building a parametric
> procedural generator from scratch — we are orchestrating proven AI-generation tools (VNCCS pipeline)
> behind a nice studio UI and fully automated, reproducible workflows.

---

## What we're building

1. **A local generation backend** — ComfyUI running headless with the [VNCCS](https://github.com/AHEKOT/ComfyUI_VNCCS)
   suite (Character Creator, Pose Studio, Clothes, Emotions, background removal, upscale) + Kokoro TTS,
   driven programmatically via the ComfyUI queue API.
2. **Amelia Studio** — our own UI/framework on top of that API: a character/background/scene manager where
   we define assets once and generate/review/approve them; "generate every pose × emotion × outfit" at the
   press of a button.
3. **Fully automated, proven workflows** — deterministic, batchable pipelines that turn Amelia's content
   definitions into finished, background-removed, correctly-named sprites and backgrounds ready for Ren'Py.

## Reference tool: VNCCS (what it gives us)
- **Consistent characters** across all images (the hard VN problem — solved by VNCCS's 4-step flow).
- **Character Cloner** — clone a character from *any* reference image (our prompt-pack designs, a sketch,
  a screenshot). Great for locking Amelia's cast to their `prompts/characters/*` designs.
- **Pose Studio** — arbitrary poses from presets or an imported reference pose.
- **Clothes** — multiple named outfit sets per character.
- **Emotions** — large emotion library + custom emotions; base calm face → emotional variants.
- **Background removal** (chroma-key + SAM3) and **upscaling** built in.
- Output lands in `ComfyUI/output/VNCCS/Characters/`. MIT-licensed. Roadmap: animations, 3D environments,
  CG, voice, music.

---

## ✅ Existing base (already in the repo): `tools/studio/`

We already built an early **"Amelia Studio"** in a prior session — it's committed under
[`tools/`](../../../tools/) (repo root), not lost. **Do not start from scratch — extend this.**

What it already has:
- **FastAPI backend** (`tools/studio/backend/`) with routers for `voice`, `images`, `batch`, `auth`
  and services for **Kokoro TTS**, **Qwen3-TTS** (+ voice cloning), **fal.ai**, **local SDXL**, audio.
- **Web frontend** (`tools/studio/frontend/`) — voice/images/batch/settings/status tabs, login.
- **Batch CSV** processing, **character anchors** (`backend/data/character_anchors.json`), a Ren'Py
  parser (`backend/utils/rpy_parser.py`), auto-save into the game's audio dirs, Docker/compose.
- Launchers `tools/start_studio.sh` / `start_studio.py`; standalone `sdxl_img2img_server.py`; plus the
  voice/sprite/bg-removal scripts at `tools/*.py` / `tools/*.sh`.
- Docs: `tools/README.md`, `tools/STUDIO_GUIDE.md`, `tools/VOICE_CLONING_*.md`, `ENHANCEMENT_SUMMARY.md`.

**Gap vs this track:** the base generates images via **fal.ai / local SDXL**, *not* VNCCS, and has no
consistent-character pipeline. The new work is: swap/augment image gen to **ComfyUI + VNCCS**, add the
pose×emotion×outfit automation, and formalise the Studio/content split. Phase 10 should **inventory and
run** this base first; Phases 11–12 **extend** it rather than rebuild.

> Note: `tools/studio/.env` (real API keys), `output/` (runtime DB/uploads/voice), caches and logs are
> gitignored — keep secrets only in your local `.env` (copy from `.env.example`).

## ⚠️ Key constraint: style match
VNCCS ships **anime** base models (Illustrious / Anima). Amelia's art direction is **painterly /
semi-realistic — explicitly NOT anime** (`design/art_direction.md §1`). Matching our style with a
realistic/painterly checkpoint + LoRA (and confirming VNCCS's consistency tricks still hold with it) is a
**primary research risk**, resolved in Phase 09 before we commit.

## The engine/content split still applies
Amelia Studio is a **reusable VN tool**, not an Amelia-only script. Keep the split:

```
studio/                     # the reusable app/framework — game-agnostic
  api/                      # ComfyUI queue-API client, VNCCS workflow drivers, Kokoro driver
  workflows/                # parameterised ComfyUI/VNCCS workflow templates (no Amelia specifics)
  ui/                       # Studio UI (asset manager, batch runner, review/approve)
  export/                   # writers: sprite sets, atlases, layeredimage bundles, manifests

content/
  amelia/                   # THIS GAME's data only
    characters/             # character defs: identity ref, outfits, pose list, emotion list
    backgrounds/            # location/scene defs
    voice/                  # Kokoro voice bindings (reuse voice_references/)
```

- **studio/** knows how to run VN asset pipelines in general. No Amelia names, no game state, no Ren'Py.
- **content/amelia/** is pure data the Studio consumes.
- The Ren'Py delivery adapter (Phase 13) is the only piece that knows both Studio outputs and `game/`.
- **Deferred:** no separate package/repo for `studio/` until a 2nd game needs it — in-repo split first.

## Phases in this track
| Phase | File | Purpose |
|-------|------|---------|
| 09 | `phase_09_research.md` | VNCCS/ComfyUI/Kokoro best practices, style-match, API automation, UI stack — decide |
| 10 | `phase_10_backend_setup.md` | Install VNCCS + models + Kokoro; headless ComfyUI API; prove workflows manually |
| 11 | `phase_11_studio_ui.md` | Amelia Studio UI + automation framework (asset manager + batch runner) |
| 12 | `phase_12_automated_workflows.md` | Automated pipelines: characters (pose×emotion×outfit), backgrounds, voice |
| 13 | `phase_13_renpy_integration.md` | Deliver Studio outputs into the game (layeredimage, naming, per-category swap) |

## Track exit criteria
- Amelia Studio can, from `content/amelia/` definitions, generate a full character's outfit × pose ×
  emotion matrix and a background set **automatically**, with review/approve, and deliver them into
  `game/images/` with no manual renaming.
- The Studio app has no Amelia-specific code — swapping in a different `content/<game>/` pack would drive it
  for another visual novel.
