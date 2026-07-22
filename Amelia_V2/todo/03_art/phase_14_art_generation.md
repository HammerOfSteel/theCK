# Phase 14 — Art Generation (Sprites, Backgrounds, CG, UI)

> **Deliberately one of the last stages before release.** Everything else must work on placeholders first.
> Text should be locked (Phase 08) so art matches final scenes, and the procgen track (`02_procedural_generation/`)
> should have had its chance to produce categories it can. This phase produces or finalises everything the
> procgen engine did **not** deliver, plus final human QA on everything visual.
>
> Use the prompt packs in `prompts/`, the discipline in `design/art_direction.md`, and the sourcing guide in
> `placeholder_guide.md`. Replace placeholder images one category at a time.

---

## 14.1 Source routing (decide per category)
- [ ] **Procgen vs manual split** — For each category, mark whether it's supplied by the procgen engine
      (Phase 13) or produced here manually / via AI prompting. Avoid double-work.

## 14.2 Character Sprites
- [ ] **Amelia** — Master sheet → 12 expressions × outfit variants (visual arc: hair messier over the year)
- [ ] **Sarah** — Master sheet → 9 expressions × visual deterioration arc (Ch6 turning point, wren tattoo)
- [ ] **Ella** — 8 expressions × 2 outfits
- [ ] **Lucas** — 8 expressions × 2 outfits
- [ ] **Zara, Raj, Liz** — 8 / 8 / 6 expressions each (+ Raj cooking special)
- [ ] **Mentors (4)** — Hawthorne, Simmons, Maya, Elena — 6 expressions each
- [ ] **Supporting (7)** — Tasha, Sophia, Michael, David, Grace, Lily, Mr. Osei
- [ ] **Layered image finalise** — Swap placeholder `layeredimage` refs to final art in `layered_images.rpy`

## 14.3 Backgrounds (58)
- [ ] **London** — 12 backgrounds
- [ ] **Plymouth Campus** — 18 backgrounds
- [ ] **Plymouth Living** — 14 backgrounds
- [ ] **Plymouth Hoe** — 4 backgrounds + THE BENCH motif
- [ ] **Cornwall** — 9+ backgrounds (Mên-an-Tol, Merry Maidens, Fogou, coast, Elena's cottage)

## 14.4 CG Event Art
- [ ] **12 core CGs** — Thames, move-in, bench, mentors, Maidens, Sarah, Fogou, crisis, results, return, endings
- [ ] **7 ending variants** — Grief, Alchemist, Scholar, Companion, Healer, Whole, Bittersweet
- [ ] **Slideshow atmospherics** — Mood images for 20 song moments

## 14.5 UI Art
- [ ] **Main menu background** (still or video)
- [ ] **Textbox design**
- [ ] **Journal / phone mockups**
- [ ] **Choice menu styling**
- [ ] **Icon + presplash + web presplash**

## 14.6 Visual Consistency Pass
- [ ] **Style unity** — Every asset feels from one hand (`art_direction.md §1`); reject stylistic outliers
- [ ] **Phase-colour continuity** — Alchemical palette shift reads correctly across chapters
- [ ] **Continuity** — Character appearance matches across scenes; season-appropriate clothing
- [ ] **Resolution/anchor QA** — Sprites align on backgrounds; CG fills correctly at 1920×1080
- [ ] **Placeholder sweep** — No placeholder solid remains anywhere in a full playthrough
- [ ] **Attribution/licence ledger** — Record generator/model/source + licence for every shipped asset

---

**Exit criteria:** Every visual placeholder is replaced with final art, style is unified, phase colour reads,
no missing-image errors on a full playthrough, and licences are recorded.
