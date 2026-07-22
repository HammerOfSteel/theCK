# Track: Procedural Generation (Modular Engine)

> A research-and-build track for **procedural character and environment generation** — 2D and/or 3D —
> usable in this visual novel *and* designed to graduate into a future standalone game engine.
> This is a **parallel R&D track**, not a blocker for shipping Amelia V2. If the modular system matures in
> time, it feeds Phase 14 (Art); if not, Amelia ships on hand-made/AI-prompted art and the engine continues
> as its own project.

---

## Why this track exists

The goal is a **reusable generation subsystem**, not a one-off asset script bolted onto Amelia. Every past
attempt to build procedural systems tangled with a specific game got regretted and thrown away. This time
the core must be **game-agnostic** from day one.

## The hard rule: engine / content split

All work in this track obeys a strict two-layer split. Nothing crosses the line.

```
engine/                     # ZERO game-specific imports. Compiles/runs standalone.
  procgen/
    core/                   # shared: RNG, seeds, param schema, layer compositor, export
    character/              # character generation module (parametric + asset assembly)
    environment/            # environment / background generation module
    export/                 # writers: PNG/atlas/layeredimage, glTF, etc.

content/
  amelia/                   # THIS GAME's data only: catalogs, palettes, presets, prompt refs
    characters/             # e.g. amelia.json, sarah.json — parameters, not code
    environments/           # location definitions, biome/palette configs
    palettes/               # alchemical phase palettes (from design/art_direction.md)
```

**Engine layer (`engine/procgen/`)**
- No import of Ren'Py, no import of Amelia game state, no Amelia schema, no Amelia UI.
- Deterministic: same seed + same params → same output.
- Consumes *data* (config objects/JSON) and produces *assets* (images, layers, meshes, manifests).
- Must build and run from a bare test harness with no game present.

**Content layer (`content/amelia/`)**
- Pure data the engine consumes: presets, catalogs, palettes, prompt references.
- No generation logic. If it contains an algorithm, it's in the wrong layer.

**Integration layer (game side, tracked in `phase_13`)**
- The only place that knows about *both* Ren'Py and the engine.
- Thin adapter: reads `content/amelia/*`, calls `engine/procgen`, writes into `game/images/…`,
  updates `layered_images.rpy` references.

## Deferred decisions (do NOT do yet)
- **No npm/pip package, no monorepo, no separate repo** yet. Do the in-repo `engine/` vs `content/`
  split first. Real package extraction is deferred until either a **third** project needs the code or a
  dedicated engine project formally starts. (Premature packaging is wasted tooling investment.)
- **2D vs 3D** is an open research question — resolved in `phase_09_research.md`, not assumed here.

## Phases in this track
| Phase | File | Purpose |
|-------|------|---------|
| 09 | `phase_09_research.md` | Survey techniques, repos, libraries/frameworks; pick approach |
| 10 | `phase_10_engine_core.md` | Build the game-agnostic core (RNG, params, compositor, export) |
| 11 | `phase_11_character_module.md` | Character generation module + Amelia content pack |
| 12 | `phase_12_environment_module.md` | Environment/background module + Amelia content pack |
| 13 | `phase_13_renpy_integration.md` | Thin adapter into Ren'Py; feed Phase 14 art |

## Track exit criteria
- `engine/procgen/` builds and runs from a standalone harness with **no game code present**.
- Amelia consumes it only through the `content/amelia/` data + the `phase_13` adapter.
- At least one real Amelia asset category (e.g. a background set or a character layer set) is produced
  end-to-end by the engine and swapped into the game with no engine change — only content data.
