# Phase 07 — Voice & Narration (TTS Pipeline)

> *Goal: Extend the voiced-narration pipeline proven on Chapter 1 to the whole game, and decide the
> scope of character voice acting.*
> **Status: Chapter 1 narrator audio already generated** (60 lines, Kokoro TTS "Nicole" voice) —
> see `audio/narrator/chapter_1/`. Per-character voice reference clips exist in
> `game/audio/voice_references/` (18 `*_reference.wav` + `voice_prompts.json`).

---

## 7.1 Pipeline Consolidation (do first)
- [ ] **Document the pipeline** — Script/tooling that turns a `chapter_N.rpy` into `chapter_N_with_voice.rpy`
      + per-line WAVs. Record exact commands in repo memory so it is reproducible.
- [ ] **Decide integration strategy** — Non-destructive: generate `chapter_N_with_voice.rpy` and toggle
      voiced vs. silent via a build flag or `config`, rather than overwriting `chapter_N.rpy`.
      (Currently Chapter 1 uses a manual `mv` swap — replace with a clean toggle.)
- [ ] **Naming + folder convention** — Lock `audio/narrator/chapter_N/line_NNN_L<line>.wav` scheme
- [ ] **Format decision** — Ship as `.ogg` (convert from WAV) to shrink build size (~65 MB/chapter as WAV)
- [ ] **Voice channel** — Route through Ren'Py `voice` channel; verify auto-forward / interrupt-on-skip behaviour

## 7.2 Narrator Rollout (Chapters 2–12)
- [ ] **Chapter 1** — ✅ Generated (60 lines). Re-run through finalised pipeline once toggle exists.
- [ ] **Chapter 2** — Generate narrator lines
- [ ] **Chapter 3** — Generate narrator lines
- [ ] **Chapter 4** — Generate narrator lines
- [ ] **Chapter 5** — Generate narrator lines
- [ ] **Chapter 6** — Generate narrator lines
- [ ] **Chapter 7** — Generate narrator lines
- [ ] **Chapter 8** — Generate narrator lines
- [ ] **Chapter 9** — Generate narrator lines
- [ ] **Chapter 10** — Generate narrator lines
- [ ] **Chapter 11** — Generate narrator lines
- [ ] **Chapter 12** — Generate narrator lines (all 7 endings)

## 7.3 Character Voice (scope decision)
- [ ] **Decision gate** — Narrator-only, OR full character voice acting? (Reference clips already exist for
      18 characters, implying full-cast intent.) Estimate cost/time before committing.
- [ ] **Consistency test** — Generate a sample scene with 3–4 characters; check voices are distinct and
      match `design/dialogue_style_guide.md` personalities
- [ ] **Per-character rollout** — If greenlit, generate by character across chapters (track as sub-list)
- [ ] **Pronunciation lexicon** — Kernewek / Cornish place names, "Mên-an-Tol", "pellar", character names

## 7.4 Voice QA
- [ ] **Sync pass** — Voice line matches on-screen text (no drift after dialogue edits from Phase 08)
- [ ] **Re-gen policy** — Any dialogue changed in Phase 08 flags its voice line as stale for re-generation
- [ ] **Volume/normalise** — Voice normalised and ducks ambient music
- [ ] **Accessibility overlap** — Ensure voiced narration coexists with Ren'Py self-voicing (don't double-speak)
- [ ] **Licence check** — Confirm TTS model + reference-voice usage terms allow distribution

---

**Dependency note:** Run **after** Phase 08 dialogue polish for each chapter where possible, so voice
lines are generated against final text and don't need re-recording. Chapter 1 is already voiced — flag its
lines for re-gen if its text changes.

**Exit criteria:** Chosen voice scope is fully generated as `.ogg`, in sync with final text, toggleable,
normalised, and licence-cleared.
