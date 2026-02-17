# The CK: Amelia V2 — Master TODO

> Living task tracker for the V2 rewrite. Phases are ordered by dependency.
> **Art generation is deliberately the final step** — everything else should work with placeholders first.

---

## PHASE 1: FOUNDATION (Design & Planning) ✅ COMPLETE

> *Committed as `9caac90`. All 14 design documents in `Amelia_V2/design/`.*

### 1.1 Core Documents
- [x] **overview.md** — Vision, themes, structural changes, file layout
- [x] **characters.md** — Full character bible with arcs, voices, relationships
- [x] **world_and_locations.md** — All locations with sensory detail and symbolic meaning
- [x] **game_mechanics.md** — Karma/Fate system, stats, thresholds, endings, dice mechanics
- [x] **narrative_structure.md** — Chapter-by-chapter breakdown with acts, scenes, choices

### 1.2 Design Documents
- [x] **choice_map.md** — Full branching tree with every choice, point value, conditional branch
- [x] **relationship_matrix.md** — Per-chapter relationship tracking for every character pair
- [x] **dialogue_style_guide.md** — Voice samples for every character in multiple emotional states
- [x] **alchemical_thread_map.md** — Scene-to-alchemical-stage mapping, embedded symbolism
- [x] **cornish_folklore_reference.md** — Cornish legends, pellar traditions, Kernewek, sites
- [x] **sarahs_arc.md** — Scene-by-scene arc, outcome spectrum, tone guidelines, content warnings
- [x] **art_direction.md** — Visual style guide, colour palettes, character designs, prompt discipline
- [x] **point_balance_spreadsheet.md** — Full point simulation across 6 playstyles

---

## PHASE 2: WRITING (Ren'Py Scripts) ✅ COMPLETE

> *Committed as `ce173ef` (10,655 insertions). All 14 .rpy files in `Amelia_V2/game/`.*

### 2.1 Script Files
- [x] **definitions.rpy** — Characters, variables (6-stat karma, relationships, flags), init logic
- [x] **Chapter 1** — London farewell. Amelia, Ella, family, bookshop, Thames
- [x] **Chapter 2** — Journey to Plymouth. Arrival, Liz, kitchen introductions, Freshers'
- [x] **Chapter 3** — First semester struggles. Tasha, Zara, Jung group, Maya, bench with Sarah
- [x] **Chapter 4** — Four mentor paths (Hawthorne/Simmons/Maya/Elena). Cornwall trips
- [x] **Chapter 5** — Settling in. Michael, Sophia, Raj, group Cornwall trip, karma dice
- [x] **Chapter 6** — Tasha escalation, Sarah withdrawal, Christmas, midwinter occult
- [x] **Chapter 7** — Gathering storm. Mentor deepens, Sarah darkens, research dilemma
- [x] **Chapter 8** — THE crisis. Academic collapse, Sarah's fate, four outcome variants
- [x] **Chapter 9** — Recovery. Academic rebound, friendship, Cornwall restoration
- [x] **Chapter 10** — London return. Ella reunion, parents, bookshop revisit
- [x] **Chapter 11** — Final term. Exams, Sophia, Tasha resolution, Cornwall, the Fogou
- [x] **Chapter 12** — Seven endings. Shared opening, unique conclusions, credits

---

## PHASE 2.5: SONG INTEGRATION ✅ COMPLETE

> *Committed as `9a0a0d3` (206 insertions). Dancing Salamanders / Geddon Bird songs placed as slideshow moments.*

- [x] **songs.md** — Design document: 20 primary placements, 16 reserve songs, thematic arc
- [x] **slideshows.rpy** — 26 slideshow labels (20 unique songs + 7 daffodils ending variants)
- [x] **Chapter calls** — 26 `call slideshow_` statements placed across all 12 chapters
- [x] **Verification** — All calls match labels, 0 compile errors

---

## PHASE 3: IMAGE PROMPT PACKS ✅ COMPLETE

> *Committed as `c4758a3` (2,208 insertions). 17 prompt files in `Amelia_V2/prompts/`.*

### Characters (`prompts/characters/`) — 9 files
- [x] **amelia.md** — 12 expressions × 6 outfit variants. Visual arc across chapters.
- [x] **ella.md** — 8 expressions × 2 outfits. Phone screen + London chapters.
- [x] **sarah.md** — 9 expressions × visual deterioration arc. Wren tattoo. Ch6 turning point.
- [x] **lucas.md** — 8 expressions × 2 outfits.
- [x] **zara.md** — 8 expressions.
- [x] **raj.md** — 8 expressions + cooking special.
- [x] **liz.md** — 6 expressions.
- [x] **mentors.md** — Hawthorne, Simmons, Maya, Elena. 6 expressions each.
- [x] **supporting.md** — Tasha, Sophia, Michael, David, Grace, Lily, Mr. Osei.

### Backgrounds (`prompts/backgrounds/`) — 5 files
- [x] **london.md** — 12 backgrounds (James house, bookshop, Thames, park, café, train)
- [x] **plymouth_campus.md** — 18 backgrounds (campus, lectures, library, psych building, offices)
- [x] **plymouth_living.md** — 14 backgrounds (halls, flat, corridors, individual rooms)
- [x] **plymouth_hoe.md** — 4 backgrounds + THE BENCH as special motif
- [x] **cornwall.md** — 9+ backgrounds (Mên-an-Tol, Merry Maidens, Fogou, coast, Elena's cottage)

### CG & UI (`prompts/cg/` + `prompts/ui/`) — 3 files
- [x] **cg_scenes.md** — 12 core CGs + 7 ending variants
- [x] **slideshow_scenes.md** — Mood backgrounds for 20 song slideshow moments
- [x] **ui_elements.md** — Main menu, textbox, journal, phone screen, choice menu, content warnings

---

## PHASE 3.5: PLACEHOLDER ART & TECHNICAL WORK ← CURRENT PHASE

> *Goal: Make the game fully runnable with placeholder assets. Complete all Ren'Py engine work so that when we focus on art, we only swap images — no code changes needed.*

### 3.5.1 Placeholder System
- [x] **placeholders.rpy** — Ren'Py displayable declarations for all 58 backgrounds (coloured solids with text labels, alchemical palette coded). Game runs without any image files.
- [x] **placeholder_guide.md** — Sourcing guide with recommended sites, search terms, naming conventions, and folder structure for when real images replace placeholders.
- [x] **images/ directory** — Organised folder tree ready to receive final art.

### 3.5.2 Technical Implementation
- [x] Project structure — Amelia_V2/game/ with definitions.rpy and 12 chapters
- [x] Character definitions — 18 characters defined in definitions.rpy
- [x] Variable architecture — 6-stat karma, relationship vars, flags, conditions
- [ ] **Screen customisation** — Journal screen, custom choice screen, content warning screen, phone screen
- [ ] **GUI styling** — Textbox, fonts, colours per alchemical phase
- [ ] **Save system** — Proper save/load with stat tracking intact
- [ ] **Layered image stubs** — `layeredimage` blocks that reference placeholder sprites, ready for real art swap

### 3.5.3 Audio
- [x] Song integration — 20 Dancing Salamanders songs placed as slideshow moments
- [x] 9 song .wav files available (need .ogg conversion)
- [ ] **Ambient music** — Per-chapter mood music for non-slideshow scenes
- [ ] **Sound effects** — Rain, wind, seagulls, kitchen, phone, footsteps
- [ ] **Ambient loops** — Library hum, café chatter, moor wind, ocean waves, fire crackle
- [ ] **Song .ogg conversion** — Convert existing .wav files; source remaining 11 songs

### 3.5.4 Writing Passes
- [ ] **Dialogue polish** — Read all dialogue aloud. Cut anything that feels like a lecture.
- [ ] **Thematic consistency** — Verify alchemical/Jungian threads are woven subtly, not stated.
- [ ] **Pacing review** — Each chapter: rising/falling tension, no two scenes at same pitch.
- [ ] **Character voice audit** — Every character identifiable by dialogue alone.
- [ ] **Content sensitivity review** — Sarah's arc, racism, bullying, depression — accurate and careful.

---

## PHASE 3.9: ART GENERATION (Final step before Polish)

> *Dedicated art phase. Take your time. Use the prompt packs in `prompts/` and test across generators. Replace placeholder images one category at a time.*

### 3.9.1 Character Sprites
- [ ] **Amelia** — Master sheet → 12 expressions × outfit variants
- [ ] **Sarah** — Master sheet → 9 expressions × visual deterioration arc
- [ ] **Ella** — 8 expressions × 2 outfits
- [ ] **Lucas** — 8 expressions × 2 outfits
- [ ] **Zara, Raj, Liz** — 8/8/6 expressions each
- [ ] **Mentors (4)** — Hawthorne, Simmons, Maya, Elena. 6 expressions each.
- [ ] **Supporting (7)** — Tasha, Sophia, Michael, David, Grace, Lily, Mr. Osei
- [ ] **Layered image update** — Swap placeholder `layeredimage` refs to final art

### 3.9.2 Backgrounds
- [ ] **London** — 12 backgrounds
- [ ] **Plymouth Campus** — 18 backgrounds
- [ ] **Plymouth Living** — 14 backgrounds
- [ ] **Plymouth Hoe** — 4 backgrounds + the Bench
- [ ] **Cornwall** — 9+ backgrounds

### 3.9.3 CG Event Art
- [ ] **12 core CGs** — Thames, move-in, bench, mentors, Maidens, Sarah, Fogou, crisis, results, return, endings
- [ ] **7 ending variants** — Grief, Alchemist, Scholar, Companion, Healer, Whole, Bittersweet
- [ ] **Slideshow atmospherics** — Mood images for 20 song moments

### 3.9.4 UI Art
- [ ] **Main menu background**
- [ ] **Textbox design**
- [ ] **Journal / phone mockups**
- [ ] **Choice menu styling**

---

## PHASE 4: POLISH & RELEASE

- [ ] **Playtesting** — 5+ distinct playthroughs (Scholar, Companion, Healer, Alchemist, Tragic)
- [ ] **Point balance testing** — Stat simulations, safety nets for edge cases.
- [ ] **Proofreading** — Full text pass for spelling, grammar, consistency.
- [ ] **Art consistency** — Character appearances match across scenes. Season-appropriate clothing.
- [ ] **Accessibility** — Text size, dyslexia font, content warnings toggle, self-voicing.
- [ ] **Build & package** — Windows, Mac, Linux builds. Cross-platform testing.

---

## QUICK REFERENCE

### Git History
| Commit | Phase | Description |
|--------|-------|-------------|
| `9caac90` | 1 | Foundation — 13 design documents |
| `ce173ef` | 2 | Writing — definitions.rpy + 12 chapter scripts (10,655 lines) |
| `9a0a0d3` | 2.5 | Songs — 20 placements, updated songs.md + slideshows.rpy |
| `c4758a3` | 3 | Image prompt packs (17 files, 2,208 lines) + updated todo.md |

### Asset Counts
| Category | Count | Status |
|----------|-------|--------|
| Design documents | 14 | ✅ Complete |
| Ren'Py scripts | 14 | ✅ Complete |
| Slideshow labels | 26 | ✅ Coded |
| Image prompt files | 17 | ✅ Complete |
| Background scenes needed | 58 | 🟡 Placeholders active |
| Character sprite sets needed | ~16 | 🟡 Placeholders pending |
| CG event illustrations | 19+ | ⬜ Phase 3.9 |
| Song audio files (.wav) | 9 of 20 | 🟡 Partial |

### File Structure
```
Amelia_V2/
├── design/              # 14 design documents (Phase 1)
├── game/                # Ren'Py game files
│   ├── definitions.rpy  # Characters, variables, functions
│   ├── chapter_*.rpy    # 12 chapter scripts (Phase 2)
│   ├── slideshows.rpy   # 26 song slideshow labels (Phase 2.5)
│   ├── placeholders.rpy # Placeholder image declarations (Phase 3.5)
│   └── images/          # Final art goes here (Phase 3.9)
│       ├── bg/          # 58 backgrounds (1920×1080)
│       ├── characters/  # Per-character sprite folders
│       ├── cg/          # CG event illustrations
│       └── ui/          # UI elements
├── prompts/             # Image generation prompts (Phase 3)
│   ├── characters/      # 9 character prompt files
│   ├── backgrounds/     # 5 location cluster files
│   ├── cg/              # 2 CG + slideshow files
│   └── ui/              # 1 UI element file
├── audio/               # Song files (9 .wav available)
├── placeholder_guide.md # Sourcing guide for placeholder/final art
└── todo.md              # This file
```

---

*Last updated: February 2026*
