# Phase 12 — Procedural Environment Module (`engine/procgen/environment`)

> *Goal: A reusable environment/background-generation module in the engine layer, plus an Amelia **content
> pack** of location definitions. The module knows how to build environments in general; it knows nothing
> about Plymouth or Cornwall specifically.*
> Depends on Phase 10 core. Runs in parallel with Phase 11.

---

## 12.1 Engine module (game-agnostic)
- [ ] **Environment generator API** — e.g. `generate_environment(params, seed) -> Image`, producing a
      composed background at the game's target resolution (`art_direction.md §2`)
- [ ] **Layered scene composition** — Sky / far / mid / near / foreground layers assembled from content-defined
      elements; supports parallax-ready output if needed later
- [ ] **Palette / phase driving** — Recolour a whole scene to a named phase palette (the core "the world
      changes colour" device from `art_direction.md §3`)
- [ ] **Procedural detail** — Noise-driven sky/weather/lighting, time-of-day tinting, fog/atmosphere passes
- [ ] **Tiling / interior option** — If Phase 09 chose it: tile/WFC-based interior layout for rooms
- [ ] **Deterministic** — Same environment def + seed ⇒ identical background

## 12.2 Amelia content pack (`content/amelia/environments/` + `palettes/`)
- [ ] **Location defs** — One JSON per location cluster (London, Plymouth Campus, Plymouth Living,
      Plymouth Hoe, Cornwall) — **data only** — derived from `prompts/backgrounds/*` and
      `design/world_and_locations.md`
- [ ] **Alchemical palettes** — Encode the 4 phase palettes (Nigredo/Albedo/Citrinitas/Rubedo) from
      `art_direction.md §3` as reusable palette data
- [ ] **Signature-location care** — Ensure high-detail hero locations (Cornwall stones, THE BENCH, the Fogou)
      are expressible with enough control to look intentional, not generic
- [ ] **Phase bindings** — Map each location's appearance to its chapter/phase so colour shifts correctly

## 12.3 Validation
- [ ] **Generate all 58 backgrounds** — Full location set from content data
- [ ] **Phase-shift QA** — A single location rendered in different phases reads as the same place, different mood
- [ ] **Style-consistency QA** — Backgrounds share one painterly language and match character art
- [ ] **Coverage check** — Output matches the background list the game references (no missing scenes)
- [ ] **Portability test** — Swap in a fixture environment content pack; module still works — proves no
      Amelia coupling in the engine layer

---

**Exit criteria:** All Amelia backgrounds can be generated from `content/amelia/environments/` with correct
phase-driven colour and consistent style, and the same module produces a different world from a fixture
content pack with **no engine changes**.
