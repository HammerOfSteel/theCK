# The CK: Amelia V2 — Master TODO

> This is the living task tracker for the V2 rewrite. Items are ordered by dependency — later phases require earlier phases to be complete.

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

### 2.2 Writing Passes (Future)
- [ ] **Dialogue polish** — Read all dialogue aloud. Cut anything that feels like a lecture.
- [ ] **Thematic consistency** — Verify alchemical/Jungian threads are woven subtly, not stated.
- [ ] **Pacing review** — Each chapter: rising/falling tension, no two scenes at same pitch.
- [ ] **Character voice audit** — Every character identifiable by dialogue alone.
- [ ] **Content sensitivity review** — Sarah's arc, racism, bullying, depression — accurate and careful.

---

## PHASE 2.5: SONG INTEGRATION ✅ COMPLETE

> *Committed as `9a0a0d3` (206 insertions). Dancing Salamanders / Geddon Bird songs placed as slideshow moments.*

- [x] **songs.md** — Design document: 20 primary placements, 16 reserve songs, thematic arc
- [x] **slideshows.rpy** — 26 slideshow labels (20 unique songs + 7 daffodils ending variants)
- [x] **Chapter calls** — 26 `call slideshow_` statements placed across all 12 chapters
- [x] **Verification** — All calls match labels, 0 compile errors

---

## PHASE 3: ART & ASSETS ← CURRENT PHASE

### 3.1 Image Prompt Packs
> *Strategy: Create detailed, consistent image generation prompts organised by category. Erik tests with various AI image generators. Focus on the visual novel art direction — quality and consistency over quantity.*

**Prompt files in `Amelia_V2/prompts/`:**

#### Characters (`prompts/characters/`)
Each character gets a dedicated prompt file with a master reference prompt (the "character sheet") and per-expression variants. Consistent style prefix, pose, and lighting anchors ensure the same character looks like the same person across every generation.

- [ ] **amelia.md** — 12 expressions × 3 outfit groups (casual/academic/special). Visual arc across chapters.
- [ ] **ella.md** — 8 expressions × 2 outfits. Primarily phone screen + London chapters.
- [ ] **sarah.md** — 8 expressions × 2 outfits. Visual deterioration arc. Wren tattoo consistency.
- [ ] **lucas.md** — 8 expressions × 2 outfits.
- [ ] **zara.md** — 8 expressions × 1 outfit.
- [ ] **raj.md** — 8 expressions × 1 outfit (+ apron variant).
- [ ] **liz.md** — 8 expressions × 1 outfit.
- [ ] **mentors.md** — Hawthorne, Simmons, Maya, Elena. 6 expressions each.
- [ ] **supporting.md** — Tasha, Sophia, Michael, David, Grace, Lily, Mr. Osei. 4 expressions each.

#### Backgrounds (`prompts/backgrounds/`)
63 unique scene tags across all chapters. Grouped by location cluster with time-of-day and weather variants.

- [ ] **london.md** — 11 backgrounds (James house, bookshop, Thames, park, café, train, Lily's room)
- [ ] **plymouth_campus.md** — 18 backgrounds (campus quad, lectures, library, psych building, Barbican)
- [ ] **plymouth_living.md** — 14 backgrounds (halls, flat kitchen, corridors, individual rooms)
- [ ] **plymouth_hoe.md** — 4 backgrounds (dawn, day, grey, the Bench). Weather and season variants.
- [ ] **cornwall.md** — 9 backgrounds (Mên-an-Tol, Merry Maidens, Madron Well, Fogou, coast, moor, Tintagel, Eden)
- [ ] **special_locations.md** — Elena's cottage (ext+int), mentor offices, Maya's ceremony room

#### CG Event Art (`prompts/cg/`)
- [ ] **cg_scenes.md** — 12 core CGs + 7 ending variants (Thames, move-in, the bench, mentor meet, Maidens, Sarah's room, Fogou entrance, crisis corridor, results, London return, Fogou interior, endings)
- [ ] **slideshow_scenes.md** — Mood backgrounds for the 20 song slideshow moments

#### UI (`prompts/ui/`)
- [ ] **ui_elements.md** — Main menu background, textbox design, journal mockup, phone screen frame

### 3.2 Technical Implementation
> *Ren'Py engine work. Core structure exists; screens/GUI/layered images still needed.*

- [x] **Project structure** — Amelia_V2/game/ with definitions.rpy and 12 chapters
- [x] **Character definitions** — 18 characters defined in definitions.rpy
- [x] **Variable architecture** — 6-stat karma, relationship vars, flags, conditions in definitions.rpy
- [ ] **Layered image declarations** — Add `layeredimage` blocks once sprites are generated
- [ ] **Screen customisation** — Journal screen, custom choice screen, content warning screen, phone screen
- [ ] **GUI styling** — Textbox, fonts, colours per alchemical phase
- [ ] **Save system** — Proper save/load with stat tracking intact

### 3.3 Audio
- [x] **Song integration** — 20 Dancing Salamanders songs placed as slideshow moments
- [x] **9 song .wav files** available (need .ogg conversion)
- [ ] **Ambient music** — Per-chapter mood music for non-slideshow scenes
- [ ] **Sound effects** — Rain, wind, seagulls, kitchen, phone, footsteps
- [ ] **Ambient loops** — Library hum, café chatter, moor wind, ocean waves, fire crackle
- [ ] **Song .ogg conversion** — Convert existing .wav files; source remaining 11 songs

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
| `9a0a0d3` | 2.5 | Songs — 3 new placements, updated songs.md + slideshows.rpy |

### Asset Counts
| Category | Count | Status |
|----------|-------|--------|
| Design documents | 14 | ✅ Complete |
| Ren'Py scripts | 14 | ✅ Complete |
| Slideshow labels | 26 | ✅ Coded |
| Background scenes needed | 63 | Prompts pending |
| Character sprite sets needed | ~18 | Prompts pending |
| CG event illustrations | 19+ | Prompts pending |
| Song audio files (.wav) | 9 of 20 | Partial |

### File Structure
```
Amelia_V2/
├── design/           # 14 design documents (Phase 1)
├── game/             # 14 .rpy scripts (Phase 2 + 2.5)
├── prompts/          # Image generation prompts (Phase 3) ← NEXT
│   ├── characters/   # Per-character sprite prompts
│   ├── backgrounds/  # Per-location background prompts
│   ├── cg/           # CG event art + slideshow prompts
│   └── ui/           # UI element prompts
└── audio/            # Song files (9 .wav available)
```

---

*Last updated: February 2026*
