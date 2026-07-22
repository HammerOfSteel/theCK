# Phase 11 — Amelia Studio UI & Framework

> *Goal: Build the Studio app — a nice-looking, reusable UI + automation framework on top of the Phase 10
> backend. Define assets once, generate/review/approve, organise the library. Game-agnostic (`studio/`).*
> Depends on Phase 10 (working headless API client).

---

> **Build on the existing base** at `tools/studio/` (FastAPI backend + web frontend + Kokoro/Qwen/fal/
> SDXL services + batch + rpy_parser). Extend and refactor it toward the `studio/` structure below — do
> not rebuild from scratch.

## 11.1 Framework core (`studio/`)
- [ ] Formalise `studio/api/` — ComfyUI queue-API client + VNCCS workflow drivers + Kokoro driver (from Phase 10)
- [ ] `studio/workflows/` — parameterised workflow templates (character, pose, clothes, emotion, background,
      voice), with a clean "fill these params" interface. No Amelia specifics.
- [ ] Job system — queue, run, track status, retry, cancel; persist job history + manifests
- [ ] `studio/export/` — writers for sprite sets, atlases, layeredimage bundles, and manifests
- [ ] Content loader — read/validate `content/<game>/` defs against the Phase 09 schema

## 11.2 Studio UI
- [ ] **Character manager** — list/create characters; edit identity ref, outfits, pose list, emotion list, palette
- [ ] **Background manager** — list/create locations/scenes; edit prompts, palette phase, variants
- [ ] **Batch runner** — "generate all / generate selected" for a character's outfit × pose × emotion matrix;
      per-background generation; live progress + queue view
- [ ] **Review & approve** — grid of generated variants; approve / regenerate / tweak-and-rerun per cell
- [ ] **Library** — browse approved assets; search/filter; see manifests (seed/params) for reproducibility
- [ ] **Voice tab** (optional) — drive Kokoro lines, preview, approve (wraps Phase 07 pipeline)
- [ ] Looks good — polished, consistent, comfortable to use for long sessions (this is a real app)

## 11.3 Wiring to content
- [ ] Studio reads/writes `content/amelia/` on disk (defs are the source of truth, editable in-app + in files)
- [ ] Approvals + manifests stored alongside content so runs are reproducible and reviewable
- [ ] No Amelia-specific logic in `studio/` — Amelia lives entirely in `content/amelia/`

## 11.4 Quality
- [ ] Framework tests — API client, workflow param injection, export writers, content-schema validation
- [ ] Portability check — point the Studio at a tiny **fixture** `content/` pack; app still works (proves
      game-agnosticism)
- [ ] Docs — `studio/README.md`: run the app, add a workflow, add a game via a content pack

---

**Exit criteria:** A working, good-looking Studio app that loads Amelia content, drives the Phase 10 backend,
runs batch jobs with progress, and supports review/approve — with zero Amelia-specific code in `studio/`.
