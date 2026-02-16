# The CK: Amelia V2 — Master TODO

> This is the living task tracker for the V2 rewrite. Items are ordered by dependency — later phases require earlier phases to be complete.

---

## PHASE 1: FOUNDATION (Design & Planning) ✅ CURRENT PHASE

### 1.1 Core Documents
- [x] **overview.md** — Vision, themes, structural changes, file layout
- [x] **characters.md** — Full character bible with arcs, voices, relationships
- [x] **world_and_locations.md** — All locations with sensory detail and symbolic meaning
- [x] **game_mechanics.md** — Karma/Fate system, stats, thresholds, endings, dice mechanics
- [x] **narrative_structure.md** — Chapter-by-chapter breakdown with acts, scenes, choices

### 1.2 Remaining Design Work
- [x] **choice_map.md** — Full branching tree in diagram form (Mermaid or similar). Every choice, every point value, every conditional branch mapped visually.
- [ ] **Character relationship matrix** — Detailed tracking of how every character pair's relationship changes per chapter.  
- [ ] **Dialogue style guide** — Voice samples for every character in different emotional states (calm, angry, vulnerable, drunk, texting). Rules for British university dialogue (slang, register, texting conventions).
- [ ] **Alchemical thread map** — The hidden layer fully charted: which scenes map to which alchemical stage, what symbolism is embedded where.
- [ ] **Cornish folklore reference** — Research document with real Cornish legends, *pellar* traditions, Kernewek phrases, sites, and how they integrate into the narrative.
- [ ] **Sarah's arc detailed outline** — The most sensitive thread needs its own dedicated document: scene-by-scene arc, the spectrum of outcomes, tone guidelines, content warning implementation.
- [ ] **art_direction.md** — Visual style guide for V2: character designs, colour palette, UI mood, scene composition rules. Unified art style specification for AI generation or commissioning.
- [ ] **Point balance spreadsheet** — Every choice in every chapter with its point awards, totalled and balanced. Simulate 5+ different playstyles to verify endings are reachable.

---

## PHASE 2: WRITING (Story & Dialogue)

### 2.1 Chapter Prose (Full Rewrites)
Write the complete narrative text for each chapter — all dialogue, narration, internal monologue, scene descriptions, and choice text.

- [ ] **Chapter 1: The Ordinary World** — London farewell. Establish Amelia, Ella, family, the bookshop, the river.
- [ ] **Chapter 2: The Call to Adventure** — Journey to Plymouth. Arrival, Liz, the kitchen introductions, Freshers', first lecture.
- [ ] **Chapter 3: Refusal of the Call** — First semester struggles. Tasha, Zara confrontation, Jung group, Maya ceremony, panic attack, the bench with Sarah.
- [ ] **Chapter 4: Meeting the Mentor** — Four variant paths written. Hawthorne, Simmons, Maya, Elena. Cornwall trips. Tests.
- [ ] **Chapter 5: Crossing the Threshold** — Settling in. Michael, Sophia, Raj's family, group Cornwall trip, karma dice event.
- [ ] **Chapter 6: Tests, Allies, Enemies** — Tasha escalation, Sarah withdrawal, Lucas vulnerability, Christmas exams, holiday break, midwinter occult.
- [ ] **Chapter 7: The Approach** — Gathering storm. Mentor deepens, Sarah darkens, Amelia's shadow, Sophia pivot, research dilemma.
- [ ] **Chapter 8: The Ordeal** — THE crisis chapter. Academic collapse, Sarah's fate, the aftermath. Four outcome variants.
- [ ] **Chapter 9: The Reward** — Recovery. Academic rebound, friendship consolidation, Cornwall restoration, mentor acknowledgment.
- [ ] **Chapter 10: The Road Back** — London return. Ella reunion, parents, Lily, solo contemplation, bookshop revisit.
- [ ] **Chapter 11: The Resurrection** — Final term. Exams, Sophia alliance, Tasha resolution, celebration, Cornwall final trip, the Fogou.
- [ ] **Chapter 12: Return with the Elixir** — Seven endings. Shared opening, unique conclusions.

### 2.2 Writing Passes
- [ ] **Dialogue polish** — Read all dialogue aloud. Does it sound like real people? Cut anything that feels like a lecture.
- [ ] **Thematic consistency** — Verify alchemical/Jungian threads are woven subtly, not stated.
- [ ] **Pacing review** — Each chapter should have rising/falling tension. No two consecutive scenes at the same emotional pitch.
- [ ] **Character voice audit** — Every character should be identifiable by dialogue alone (cover the name; can you tell who's speaking?).
- [ ] **Content sensitivity review** — Sarah's arc, racism scenes, bullying scenes, depression depictions — reviewed for accuracy and care.

---

## PHASE 3: IMPLEMENTATION (Ren'Py & Assets)

### 3.1 Technical Setup
- [ ] **Project structure** — New Ren'Py project in Amelia_V2/game/. Clean setup based on learnings from V1.
- [ ] **Character definitions** — Proper Ren'Py character objects with layered images, not one-image-per-scene.
- [ ] **Variable architecture** — All stats, relationships, flags, and conditions defined cleanly. The Fate Wheel engine.
- [ ] **Screen customisation** — Journal screen (Amelia's diary as stat-display), custom choice screens, content warning screen.
- [ ] **Save system** — Proper save/load with stat tracking intact.

### 3.2 Script Implementation
- [ ] Chapters 1–3 (before mentor fork)
- [ ] Chapter 4 (four mentor variants)
- [ ] Chapters 5–7 (with mentor colouring)
- [ ] Chapter 8 (Sarah branching — most complex)
- [ ] Chapters 9–11 (Sarah-alive and Sarah-dead variants)
- [ ] Chapter 12 (seven endings)
- [ ] **Karma Dice engine** — RNG system with stat modifiers, triggered at key moments
- [ ] **Ending calculation** — The algorithm that determines which ending plays

### 3.3 Art Assets
- [ ] **Character sprite sheets** — Consistent character art across all scenes. Expressions: neutral, happy, sad, angry, surprised, thoughtful.
- [ ] **Background art** — All locations. Unified style. Day/night/weather variants for key locations.
- [ ] **CG scenes** — Key dramatic moments rendered as full illustrations (Sarah's rescue, the Fogou, graduation, etc.)
- [ ] **UI art** — Journal design, main menu, choice buttons, transition effects.

### 3.4 Audio  
- [ ] **Music selection** — Per-chapter mood music. Licensed or original. Cornwall-evocative ambient for moor/coast scenes.
- [ ] **Sound effects** — Rain, wind, seagulls, kitchen sounds, phone buzzes, footsteps on cobblestones.
- [ ] **Ambient loops** — Location-specific: library hum, café chatter, moor wind, ocean waves.

---

## PHASE 4: POLISH & RELEASE

- [ ] **Playtesting** — At minimum 5 distinct playthroughs: Scholar path, Companion path, Healer path, Alchemist path, Tragic path. Verify all endings reachable. Check for dead branches.
- [ ] **Point balance testing** — Run stat simulations. Can a player accidentally lock themselves out of all good endings? If so, add safety nets.
- [ ] **Proofreading** — Full text pass for spelling, grammar, consistency.
- [ ] **Art consistency** — All character appearances match across scenes. Clothing appropriate to season/weather.
- [ ] **Accessibility** — Text size options, dyslexia-friendly font option, content warnings toggle, self-voicing support.
- [ ] **Build & package** — Windows, Mac, Linux builds. Test on all platforms.

---

## WHAT WE KEEP FROM V1

These elements are carried forward and improved:

| Element | V1 Status | V2 Plan |
|---|---|---|
| Hero's Journey 12-chapter structure | ✅ Strong foundation | Keep, deepen pacing within each chapter |
| 6-stat point system (AA/SI/MH/SD/MC/OK) | ✅ Good categories | Keep categories, redesign presentation as karma |
| Main character cast | ✅ Good archetypes | Keep and add depth, contradictions, personal arcs |
| Cornwall & Plymouth settings | ✅ Excellent choice | Keep and massively expand with sensory detail |
| Mentor system (4 paths) | ✅ Clever design | Keep, flesh out each path's unique content |
| Sarah's fate as key branching point | ✅ Powerful concept | Keep, expand from binary to spectrum |
| 6 endings | ✅ Good variety | Keep, add 7th (Bittersweet), deepen all |
| Occult/alchemy hidden path | ✅ Unique and compelling | Keep, integrate more deeply into main narrative |
| V1 images (chapters 1-3, 12) | Partial | Evaluate for reuse or reference; new art direction needed |
| V1 dialogue (chapters 1-3, 12) | Written | Rewrite from scratch, but mine for good moments to keep |

---

## WHAT CHANGES FROM V1

| Aspect | V1 | V2 |
|---|---|---|
| Timeline | 3 years vague | 1 year detailed (Oct–Jun) |
| Points display | notify() popup | Hidden; expressed through Amelia's journal |
| Image system | One full image per scene | Character sprites + backgrounds (layered) |
| Transitions | show/hide/black cycle | Proper dissolves, fades, weather effects |
| Sarah outcome | Binary (alive/dead) | 4-tier spectrum |
| Negative points | Rare | Meaningful — avoidance and cowardice penalised |
| Relationship tracking | Not tracked | Per-character relationship values |
| Dice/randomness | None | Karma Dice at pivotal moments |
| 7th ending | Didn't exist | The Bittersweet — for mixed-stat players |
| Cornwall depth | List of places | Each site with folklore, sensory detail, symbolic meaning |
| Character voices | Generic dialogue | Distinct, age-appropriate, British, identifiable |

---

## NEXT STEPS (Immediate)

The foundation documents are complete. The recommended next action is:

1. **Choice Map** — Map every choice in every chapter with its exact point values and conditional branches. This is the game's "skeleton" and must be bulletproof before writing begins.
2. **Sarah's Arc Document** — Because it's the most narratively complex and sensitive thread.
3. **Begin Chapter 1 prose** — Start writing. The best way to test the design is to write against it and see what works.

---

*Last updated: February 2026*
