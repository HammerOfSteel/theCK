# Phase 12 — Automated Asset Workflows (Full Generation)

> *Goal: Use Amelia Studio to actually generate the game's assets — every character in every outfit × pose ×
> emotion, every background — automatically and reproducibly, from `content/amelia/` definitions.*
> Depends on Phase 11 (Studio app) and Phase 10 (backend).

---

## 12.1 Author Amelia content packs (`content/amelia/`)
- [ ] **Character defs** — one per cast member (Amelia, Sarah, Ella, Lucas, Zara, Raj, Liz, 4 mentors,
      7 supporting) from `prompts/characters/*` + `art_direction.md §4`: identity reference image, outfit
      sets, required pose list, required emotion list, palette bindings, arc variants (Amelia hair, Sarah
      deterioration)
- [ ] **Background defs** — per location cluster (London, Campus, Living, Hoe, Cornwall) from
      `prompts/backgrounds/*` + `world_and_locations.md`, with phase-palette bindings
- [ ] **Voice bindings** — map characters/narrator to Kokoro references (`game/audio/voice_references/`)

## 12.2 Character generation (the big one)
- [ ] Lock each character's base via Character Creator/Cloner (consistent identity approved)
- [ ] Generate outfit sets per character
- [ ] Generate the pose set per outfit
- [ ] Generate the emotion set per outfit/pose (the expressions the game needs)
- [ ] Background removal + upscale on all; consistent framing/anchor
- [ ] Review/approve the full matrix; regenerate rejects; everything reproducible via manifest

## 12.3 Background generation
- [ ] Generate all 58 backgrounds from defs at target resolution (`art_direction §2`)
- [ ] Apply correct alchemical phase colour per location/chapter
- [ ] Review/approve; regenerate rejects

## 12.4 Voice (orchestrated, optional here)
- [ ] Batch-drive Kokoro narrator lines per chapter via the Studio (feeds Phase 07)
- [ ] Normalise + approve; keep in sync with final text (defer to post-text-lock chapters)

## 12.5 Consistency & coverage gates
- [ ] Identity QA — each character is the same person across the whole matrix
- [ ] Style QA — all assets share the target painterly look; phase colour reads
- [ ] Coverage — output matches exactly what the game references (no missing pose/emotion/background)
- [ ] Naming — outputs already match the game's expected asset names (set in export config)

---

**Exit criteria:** From `content/amelia/`, the Studio has generated + we've approved the full character
matrix and background set (and optionally narrator voice), in target style, with reproducible manifests and
game-ready names. Ready for delivery in Phase 13.
