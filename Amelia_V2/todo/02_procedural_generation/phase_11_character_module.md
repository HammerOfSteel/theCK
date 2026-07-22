# Phase 11 — Procedural Character Module (`engine/procgen/character`)

> *Goal: A reusable character-generation module in the engine layer, plus an Amelia **content pack** that
> drives it. The module knows how to build characters in general; it knows nothing about Amelia specifically.*
> Depends on Phase 10 core.

---

## 11.1 Engine module (game-agnostic)
- [ ] **Character generator API** — Implement the Phase 09 signature, e.g.
      `generate_character(params, seed) -> LayerBundle` (base body, hair, outfit, expression, accessories)
- [ ] **Modular part system** — Parts are addressed by *category + id* from content data; the engine has no
      hard-coded character names or wardrobes
- [ ] **Expression system** — Generate an expression set from one base (eyes/brows/mouth swaps or
      model-driven), so N expressions come from one character definition
- [ ] **Outfit / variant system** — Multiple outfits per character via content-defined layer sets
- [ ] **Palette hook** — Character output can be tinted by a named palette (phase-driven shading)
- [ ] **Consistency mechanism** — Whatever the Phase 09 approach chose (locked seed / LoRA / IP-Adapter /
      fixed part atlas), enforce identity stability across a character's expression + outfit matrix
- [ ] **Deterministic** — Same character def + seed ⇒ identical sprite set every run

## 11.2 Amelia content pack (`content/amelia/characters/`)
- [ ] **Schema-conformant character defs** — One JSON per character (Amelia, Sarah, Ella, …) describing
      parts, expressions, outfits, palette bindings — **data only, no logic**
- [ ] **Source-of-truth mapping** — Populate from `prompts/characters/*` and `design/art_direction.md §4`
      (builds, hair, wardrobe, expression lists, visual arcs)
- [ ] **Arc-aware variants** — Encode visual-arc changes (Amelia's hair getting messier; Sarah's
      deterioration) as chapter/phase-tagged variants in content data
- [ ] **Reference clips cross-link** — If character voices are used, note the mapping to
      `game/audio/voice_references/` for pipeline coherence (data reference only)

## 11.3 Validation
- [ ] **Generate the full cast** — Produce every character's expression × outfit matrix from content
- [ ] **Identity QA** — Each character reads as the *same person* across all expressions/outfits
- [ ] **Style-consistency QA** — All characters share one visual language (`art_direction.md §1`)
- [ ] **Coverage check** — Output matches the required sprite list the game expects (no missing expressions)
- [ ] **Portability test** — Swap in a tiny *fixture* content pack (not Amelia) and confirm the module still
      produces sensible characters — proves the module isn't secretly Amelia-coupled

---

**Exit criteria:** The full Amelia cast can be generated from `content/amelia/characters/` with stable
identity and consistent style, and the same module produces a different cast from a fixture content pack
with **no engine changes**.
