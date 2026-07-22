# Phase 10 — Local Generation Backend (ComfyUI + VNCCS + Kokoro)

> *Goal: A reliable, reproducible local backend that the Studio will drive over an API. Everything works
> headlessly and produces our-style assets. No Studio UI yet — this is the engine room.*
> Depends on Phase 09 decisions (model + workflow choices).

---

## 10.0 Inventory & run the existing base first
- [ ] Read `tools/README.md` + `tools/STUDIO_GUIDE.md`; run `tools/start_studio.sh` and try it
- [ ] Confirm the existing Kokoro/Qwen voice + fal.ai/local-SDXL image paths still work
- [ ] Note what to reuse (backend/services, rpy_parser, character_anchors, batch) vs replace (add VNCCS)

## 10.1 Install & pin
- [ ] Install ComfyUI (prefer the VNCCS Easy-Install path or a clean manual install)
- [ ] Install **VNCCS** custom nodes + **VNCCS-Utils** (Pose Studio lives there) via Comfy Manager
- [ ] Install missing custom nodes; resolve dependencies (`requirements.txt`)
- [ ] Download the chosen models via VNCCS **Control Center** (Q5/Q8) + our style checkpoint + LoRA(s)
- [ ] **Pin versions** — record ComfyUI commit, VNCCS version, model hashes in `backend_versions.md`
- [ ] Install/configure **Kokoro TTS** local runtime (reuse our prior setup)

## 10.2 Prove the workflows manually (our style)
- [ ] Step 1 Character Creator / **Cloner** — create one Amelia base from her reference, in target style
- [ ] Pose Studio — generate a small pose set; import-a-pose from reference works
- [ ] Step 2 Clothes — one outfit set
- [ ] Step 3 Emotions — a few emotions on the base + outfit
- [ ] Background removal (chroma-key + SAM3) + upscale — clean cutouts
- [ ] Confirm consistency holds across the matrix in our (non-anime) style

## 10.3 Headless API operation
- [ ] Run ComfyUI in API/headless mode; confirm reachable on localhost
- [ ] Export each needed VNCCS workflow as **API-format JSON**
- [ ] Write a minimal Python client that queues a workflow via `/prompt`, polls `/history`, pulls images
      via `/view` (this becomes the seed of `studio/api/`)
- [ ] Parameter injection — swap character/pose/outfit/emotion/seed into the workflow JSON programmatically
- [ ] Progress + error handling over the websocket; robust ret/timeout on long jobs

## 10.4 Backgrounds & audio backends
- [ ] Stand up a **background/scene** ComfyUI workflow (txt2img + upscale) matching art direction
- [ ] Kokoro driver script — text in → normalised `.ogg` out, callable headlessly
- [ ] Confirm both are drivable by the same API client pattern

## 10.5 Determinism & housekeeping
- [ ] Seed + model pinning ⇒ re-running a job reproduces the asset
- [ ] Output foldering convention under VNCCS output; a manifest per generated asset (params + seed)
- [ ] Document exact run commands + API endpoints in repo memory (reproducible)

---

**Exit criteria:** ComfyUI+VNCCS+Kokoro run locally and headlessly; every workflow we need is exported as
API JSON and driven from a script; a character matrix + a background + a voice line are all produced in our
target style from the command line, reproducibly, with pinned versions.
