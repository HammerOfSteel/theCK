# Phase 13 — Ren'Py Integration & Asset Delivery

> *Goal: Deliver approved Amelia Studio outputs into the Ren'Py game — correct filenames, `layeredimage`
> wiring, one category at a time — so swapping placeholders for final art needs no script changes.*
> Depends on Phase 12 (approved assets). This is the bridge to Phase 14 (Art).

---

## 13.1 Delivery adapter
- [ ] Build the delivery step (in `studio/export/` + a thin game-side adapter): approved Studio assets →
      files placed in `game/images/…` with the game's expected names
- [ ] Map to existing references — filenames match `placeholders.rpy`, `layered_images.rpy`, `prompts/`
      naming so no `.rpy` edits are needed to swap art
- [ ] **`layeredimage` wiring** — generate/update `layered_images.rpy` blocks from the per-character
      pose/expression/outfit layer sets the Studio produced
- [ ] Idempotent — re-delivering reproduces identical files; unrelated files untouched

## 13.2 Swap-in strategy
- [ ] One category at a time (e.g. Cornwall backgrounds → verify in-engine → next)
- [ ] Placeholder parity — anything not yet generated keeps its placeholder; no missing-file errors ever
- [ ] Sprite anchors/framing correct at runtime; expressions switch cleanly

## 13.3 Validation
- [ ] End-to-end: at least one full character and one full background cluster delivered and running in-game
- [ ] In-engine visual QA across a real playthrough (resolution, anchors, expressions, phase colour)
- [ ] Build-size check (atlas/compression sane)
- [ ] Reproducibility — a fresh checkout can regenerate + redeliver an asset from content + manifest

## 13.4 Hand-off to Phase 14
- [ ] Categories the Studio produces well are marked "done" in `03_art/phase_14_art_generation.md`
- [ ] Any category the Studio can't nail falls back to manual/AI art in Phase 14 — documented

---

**Exit criteria:** Approved Studio assets are delivered into the game by filename with `layeredimage` wired,
one category at a time, no script edits and no missing-file errors; Phase 14 consumes Studio output as the
source for every category it covers.
