# Phase 17 — Post-Release & Engine Continuation

> *Goal: Support the shipped game and continue the procgen engine as its own long-term effort.*
> Optional / ongoing. Nothing here blocks release.

---

## 17.1 Post-launch support
- [ ] **Bug triage** — Collect player reports; hotfix soft-locks / crashes / typos
- [ ] **Save-compat patches** — Any post-release content respects the save-compatibility policy (Phase 05)
- [ ] **Balance tweaks** — Adjust from real playtest data if endings skew

## 17.2 Content follow-ups (optional)
- [ ] **Additional localisations** — Complete Korean/Swedish; add others
- [ ] **Full voice cast** — If shipped narrator-only, revisit full character voicing (Phase 07 decision)
- [ ] **Extras** — Director's-commentary mode, art gallery expansions, bonus scenes

## 17.3 Procgen engine graduation (the long game)
- [ ] **Post-mortem** — What worked / didn't in the `engine/procgen` modular split during Amelia
- [ ] **Harden the engine** — Broaden fixtures, docs, and tests beyond Amelia's needs
- [ ] **Package-extraction gate** — When a **third** project needs it (or a dedicated engine project starts),
      extract `engine/procgen` into its own package/repo. **Not before** — premature packaging is wasted
      tooling investment. (See `02_procedural_generation/README.md`.)
- [ ] **Content-pack template** — Ship a starter `content/<game>/` template so a new game can adopt the engine
      by writing data, not code

---

**Exit criteria:** Game is stable in the wild; the procgen engine is documented and portable enough that a
future project could adopt it via a content pack alone.
