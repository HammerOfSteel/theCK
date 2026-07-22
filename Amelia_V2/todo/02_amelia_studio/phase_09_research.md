# Phase 09 — Amelia Studio: Research & Pipeline Design

> *Goal: Learn the tools deeply and lock the pipeline design **before** building. Output is written
> decisions, a proven style match, and a small manual proof-of-concept — not the full app.*
> Read `../README.md` first (what we're building + the engine/content split).

---

## 9.1 Understand VNCCS end-to-end
- [ ] Read VNCCS README + Changelog; watch/skim the 3.0 workflow steps
- [ ] Map the 4-step flow to our needs: Character Creator → Pose Studio → Clothes → Emotions
- [ ] Study **Character Cloner** — can we lock each cast member to their `prompts/characters/*` design by
      cloning from a reference image? (Likely our main character-onboarding path.)
- [ ] Inventory VNCCS outputs + folder layout (`ComfyUI/output/VNCCS/Characters/`) and metadata files
- [ ] Note VNCCS roadmap items (animations, 3D env, CG, voice, music) — decide what we wait for vs build

## 9.2 Style match (PRIMARY RISK — resolve first)
- [ ] Confirm Amelia's target style from `design/art_direction.md §1` (painterly, semi-realistic, NOT anime)
- [ ] Test VNCCS with a **realistic/painterly checkpoint + LoRA** instead of the default anime models
- [ ] Verify character **consistency** still holds with a non-anime model (VNCCS is tuned for Illustrious/Anima)
- [ ] Verify the **alchemical phase palette** (art_direction §3) can be applied (prompt, LoRA, or post-recolour)
- [ ] Decision: exact base model + LoRA(s) + settings that hit our look. Record in `style_decision.md`.
      Fallback: accept a lightly stylised look, or restyle art direction — decide explicitly.

## 9.3 ComfyUI automation & API
- [ ] Learn the ComfyUI **queue API** (`/prompt`, `/history`, `/view`, websocket progress)
- [ ] Confirm VNCCS workflows can be exported as API-format JSON and driven headlessly (no manual clicking)
- [ ] Identify which VNCCS node parameters we must template (character, pose set, outfit, emotion list, seed)
- [ ] Determinism/repro: seed handling, model pinning, so a re-run reproduces a sprite
- [ ] Batch strategy: queue depth, VRAM limits, one-character-at-a-time vs full matrix

## 9.4 Backgrounds & audio pipelines
- [ ] Decide background generation approach (VNCCS is character-first; backgrounds may need a separate
      ComfyUI txt2img/scene workflow) — design a background workflow template
- [ ] Kokoro TTS: confirm local/API run mode we've used before; how the Studio will call it; reuse the
      existing `game/audio/voice_references/` clips + Phase 07 pipeline (don't duplicate — orchestrate)

## 9.5 Studio UI stack decision
- [ ] Choose the Studio app stack (e.g. local web app: FastAPI/Python + a JS frontend, or an Electron/
      Tauri desktop app) — weigh reuse, our familiarity, and talking to ComfyUI's API + local filesystem
- [ ] Sketch the Studio information architecture: Characters, Backgrounds, Scenes, Jobs/Queue, Review/Approve,
      Library — and how it maps to `content/amelia/` on disk
- [ ] Define the **content schema** (JSON): a character def (identity ref, outfits, poses, emotions, palette),
      a background def, a voice binding

## 9.6 Proof of concept (manual, throwaway)
- [ ] Manually run VNCCS to produce **one** Amelia sprite (base) in our chosen style
- [ ] Manually produce that sprite in **2 poses × 2 emotions × 1 outfit**, background-removed
- [ ] Drive **one** VNCCS workflow via the ComfyUI API from a script (no UI) — prove headless automation
- [ ] Generate **one** Kokoro voice line via script — prove audio automation path

## 9.7 Decide & document
- [ ] Write `pipeline_design.md` — the full plan: models, workflows, API flow, UI stack, content schema,
      folder conventions, determinism, batch strategy
- [ ] Scope gate vs Amelia release: is this achievable in time, or does Phase 14 (manual art) stay the
      fallback while the Studio matures? Decide explicitly.

---

**Exit criteria:** `style_decision.md` + `pipeline_design.md` written; a manually-produced Amelia sprite in
our target style; headless ComfyUI-API automation proven on one workflow; Kokoro automation proven. No Studio
app code yet — that's Phase 11.
