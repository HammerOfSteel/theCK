# Phase 17 — Post-Release & Studio Continuation

> *Goal: Support the shipped game and continue Amelia Studio as its own long-term VN tool.*
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

## 17.3 Amelia Studio graduation (the long game)
- [ ] **Post-mortem** — What worked / didn't in the Studio/content split during Amelia
- [ ] **Harden the Studio** — Broaden fixtures, docs, and tests beyond Amelia's needs; stabilise workflows
- [ ] **Package-extraction gate** — When a **second** game needs it (or a dedicated tool project starts),
      extract `studio/` into its own package/repo. **Not before** — premature packaging is wasted
      tooling investment. (See `02_amelia_studio/README.md`.)
- [ ] **Content-pack template** — Ship a starter `content/<game>/` template so a new visual novel can adopt
      the Studio by writing data, not code

---

**Exit criteria:** Game is stable in the wild; Amelia Studio is documented and portable enough that a
future VN could adopt it via a content pack alone.
