# Phase 15 — QA, Balancing & Accessibility

> *Goal: Prove the finished game works, is fair, is kind, and is playable by everyone — before building.*
> Runs after content is final (text, audio, art). Some checks repeat earlier per-phase QA at full-game scope.

---

## 15.1 Playtesting
- [ ] **5+ distinct playthroughs** — Scholar, Companion, Healer, Alchemist, Tragic (+ Occult path)
- [ ] **All 7 endings reachable** — Confirm each ending triggers from an intended, achievable path
- [ ] **Branch coverage** — Hit major conditional branches and relationship gates at least once
- [ ] **Soft-lock / dead-end hunt** — No unreachable content, no choice that strands the player
- [ ] **Save/load stress** — Save mid-scene, mid-choice, mid-slideshow; reload; rollback; no state corruption
- [ ] **Skip / auto / history** — Skip unseen vs seen, auto-forward, back-history all behave

## 15.2 Balance
- [ ] **Point-balance validation** — Full-game stat simulation vs `design/point_balance_spreadsheet.md`
- [ ] **Edge-case safety nets** — Extreme playstyles (min/max a stat) still reach a coherent ending
- [ ] **Karma-dice fairness** — Random mechanic feels fair; no run-ruining swings

## 15.3 Accessibility
- [ ] **Text scaling** — Adjustable text size; readable at defaults
- [ ] **Dyslexia font toggle** — Available and applied everywhere
- [ ] **Self-voicing** — Ren'Py self-voice works; doesn't conflict with voiced narration (Phase 07)
- [ ] **Content-warning toggle** — Global on/off + per-scene gating verified
- [ ] **Colour/contrast** — UI legible for low-vision / colour-blind players despite phase palette shifts
- [ ] **Input** — Keyboard + mouse + (if targeted) controller/touch all navigable

## 15.4 Localisation readiness (existing `tl/korean/`, `tl/swedish/`)
- [ ] **String extraction current** — `renpy.sh <project> translate` regenerated after final text
- [ ] **Existing translations reconciled** — Korean/Swedish stubs updated or explicitly deferred
- [ ] **Font coverage** — Fonts cover target-language glyphs (incl. Kernewek diacritics)

## 15.5 Full-text & audio final pass
- [ ] **Proofread** — Final spelling/grammar/consistency sweep on locked text
- [ ] **Audio sync** — Voiced lines match final text; no stale voice from pre-Phase-08 edits
- [ ] **Missing-asset zero** — Console clean of missing image/audio warnings across a full run

---

**Exit criteria:** All endings verified, balance validated, accessibility features working, console clean,
translations reconciled or explicitly deferred.
