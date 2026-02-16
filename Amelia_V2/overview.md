# The CK: Amelia — V2 Overview

## Vision Statement

*The CK: Amelia* is a choice-driven visual novel that follows an eighteen-year-old psychology student through her first year at the University of Plymouth. It is a coming-of-age story told through the lens of the Hero's Journey, layered with philosophical depth — drawing from Jungian psychology, Hermetic alchemy, Cornish folklore, and Zen contemplation — without ever becoming didactic. The game should feel like a deeply personal modern story first, with its esoteric threads woven *underneath* the surface for players who look for them.

The V2 rewrite aims to:

1. **Deepen characters** — give every major NPC a personal arc, contradictions, desires, and growth that intersect meaningfully with Amelia's journey.
2. **Expand world-building** — make Plymouth, Cornwall, and London feel alive with sensory detail, local culture, weather, food, slang, and hidden layers of Cornish mysticism embedded in the landscape itself.
3. **Refine the narrative** — tighten pacing, modernise dialogue to sound like real 18–22 year olds, improve thematic coherence across the Hero's Journey structure.
4. **Flesh out game mechanics** — evolve the 6-stat point system into a subtle Fate/Karma engine that feels organic rather than gamey, with consequences that ripple across chapters.
5. **Design before implementing** — fully map out the choice architecture, character relationship web, and scene-by-scene flow before touching any Ren'Py code or art prompts.

---

## Core Themes

### Surface Layer (What the player feels)
- **Leaving home and becoming yourself** — the loneliness, excitement, and terror of starting university
- **Friendship as survival** — how the people you meet in your first year can save or break you
- **Mental health is real** — depression, anxiety, grief, and the courage it takes to reach out
- **Knowledge can transform you** — the texts you read and the ideas you encounter genuinely change who you become

### Middle Layer (What the attentive player notices)
- **The Shadow** (Jung) — every character represents an aspect of Amelia's psyche; Tasha is her shadow, Lucas her animus, Maya her guide to the collective unconscious
- **Solve et Coagula** — the alchemical process of dissolution and recombination mirrors Amelia's breakdown and reconstruction across the year
- **The Cornish Otherworld** — Cornwall's standing stones, holy wells, tin mines, and moors are not just scenery; they are thresholds between the mundane and the numinous
- **Fate and Free Will** — the karma/point system is the game's metaphor for how small choices compound into destiny

### Hidden Layer (The occult path)
- **The Great Work** — for players who pursue the OK (Occult Knowledge) path, the entire story maps to the stages of the alchemical *Magnum Opus*: Nigredo (chapter 8 ordeal), Albedo (chapter 11 resurrection), Citrinitas (approaching enlightenment), Rubedo (the Philosopher's Stone ending)
- **Cornish grimoire tradition** — real historical elements: the Cornish *pellar* (cunning folk), the Mên-an-Tol healing stone, the Pisky legends, Drolls (Cornish folk tales)
- **Hidden mentor Elena** — not just a mature student but a *pellar*, a custodian of a living folk tradition, accessible only to those who have been paying deep attention

---

## Structural Changes from V1

| Aspect | V1 | V2 |
|--------|----|----|
| **Timeline** | 3 years compressed | 1 full academic year (October → June), detailed week-by-week | 
| **Chapters** | 12 Hero's Journey stages | 12 retained, but each now has 3–5 acts with clearer pacing |
| **Characters** | Flat — each represents one theme | Multi-dimensional with their own arcs and contradictions |
| **Dialogue** | Formal, exposition-heavy | Naturalistic, age-appropriate, British university register |
| **Cornwall** | Scenic backdrop | Living character — weather, folklore, landscape as metaphor |
| **Alchemy** | Surface references | Deep structural motif — Nigredo/Albedo/Citrinitas/Rubedo mapped to story arc |
| **Point system** | Simple +1 tallying | Karma engine with thresholds, hidden combos, relationship gates |
| **Mentor system** | 4 mentors based on points | Retained and expanded — each mentor unlocks a *worldview* that colours all subsequent scenes |
| **Endings** | 6 endings at the end | Endings are earned across the whole game — seeds planted in ch1 bloom in ch12 |
| **Sarah arc** | Binary alive/dead | Spectrum of outcomes — saved early, saved late, hospitalised, lost — each with narrative weight |
| **Occult path** | Separate track | Woven into the main narrative as a legitimate parallel reading of events |
| **Art style** | Mixed DALL-E 2/3 | Unified semi-realistic style, consistent character designs (to be defined) |

---

## Tone & Feel

- **Atmospheric** — rain on Plymouth cobblestones, wind on Bodmin Moor, the smell of old books in second-hand shops
- **Grounded** — real student problems: money, homesickness, bad food, awkward silences, group projects
- **Warm but unflinching** — this is a story that deals honestly with depression, racism, bullying, and loss; it doesn't shy away but it is never exploitative
- **Quietly mystical** — Cornwall itself hums with an older energy; the player should feel it before they can name it
- **Dialogue-driven** — characters feel like people you'd actually know at university; they joke, they ramble, they say the wrong thing, they text at 2am

---

## File Structure (Amelia_V2/)

```
Amelia_V2/
├── overview.md              ← You are here
├── todo.md                  ← Master task tracker
├── design/
│   ├── characters.md        ← Full character profiles, arcs, relationships
│   ├── world_and_locations.md ← All locations with sensory detail & narrative purpose
│   ├── game_mechanics.md    ← Karma/Fate system, stats, thresholds, endings
│   ├── narrative_structure.md ← Chapter-by-chapter breakdown with acts & choices
│   ├── choice_map.md        ← Full branching tree with point values (later)
│   └── art_direction.md     ← Visual style guide, character designs, mood boards (later)
├── story/
│   ├── 01_ordinary_world.md
│   ├── ...
│   └── 12_return_with_the_elixir.md
├── game/                    ← Ren'Py scripts (later phase)
└── assets/                  ← Art prompts, music notes (later phase)
```

---

## Development Phases

**Phase 1: Foundation** (current)
- Character bibles
- World-building & location design
- Game mechanics & karma system design
- Narrative structure & scene-by-scene outline

**Phase 2: Writing**
- Full prose for all 12 chapters
- Dialogue polishing passes
- Choice architecture & point balancing

**Phase 3: Implementation**
- Ren'Py scripting
- Art prompt generation
- Music & sound design notes
- UI/UX refinement

**Phase 4: Polish**
- Playtesting & balancing
- Proofreading
- Art consistency pass
- Build & release
