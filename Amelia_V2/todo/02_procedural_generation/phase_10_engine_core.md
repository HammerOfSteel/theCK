# Phase 10 — Procedural Engine: Core (`engine/procgen/core`)

> *Goal: Build the game-agnostic foundation that every generation module stands on. Zero game imports.
> Must build and run from a standalone test harness with no Amelia code present.*
> Depends on `phase_09` decisions (API surface + content schema).

---

## 10.1 Bootstrap the engine boundary
- [ ] **Create `engine/procgen/` tree** — `core/`, `character/`, `environment/`, `export/` (per `../README.md`)
- [ ] **Standalone guarantee** — Add a `engine/procgen/__main__` or `tools/harness` that runs a demo
      generation with **no game present**. This is the contract; keep it green forever.
- [ ] **No-crossing lint** — Add a check (test/CI/script) that fails if `engine/` imports anything from
      `content/` or the game. Direction of dependency is one-way: game → engine, never engine → game.
- [ ] **Dependency budget** — Keep engine deps minimal and documented; note offline-capability of each.

## 10.2 Determinism & parameters
- [ ] **Seeded RNG service** — Central RNG seeded per-generation; same seed + params ⇒ identical output
- [ ] **Parameter schema** — Typed, validated param objects (from the Phase 09 content schema). Reject
      malformed content data at the boundary with clear errors.
- [ ] **Config loader** — Load `content/<game>/…` JSON into validated param objects. The loader is generic;
      it must not know the word "Amelia" — the path/game id is passed in.

## 10.3 Composition & export primitives
- [ ] **Layer model** — Generic layered-image representation (ordered layers, anchors, blend/opacity)
- [ ] **Compositor** — Flatten layers → image; support masks and programmatic palette/recolour
- [ ] **Palette engine** — Map a named palette (e.g. an alchemical phase) onto grayscale/mask layers
- [ ] **Exporters (`export/`)** — Pluggable writers: flat PNG, sprite atlas + manifest, and a
      Ren'Py-`layeredimage`-friendly layer bundle. (Adapter that writes into the game lives in Phase 13,
      not here — `export/` only produces files/manifests, it doesn't know about `game/`.)

## 10.4 Quality gates for the core
- [ ] **Unit tests** — RNG determinism, schema validation, compositor correctness, palette mapping
- [ ] **Golden-image tests** — Fixed seed + fixed params ⇒ byte/near-byte-stable reference output
- [ ] **Harness demo** — `harness` generates a sample character + sample environment from *fixture* content
      (not Amelia content) to prove game-agnosticism
- [ ] **Docs** — `engine/procgen/README.md`: API surface, how to add a module, how to run the harness

---

**Exit criteria:** Core builds and passes tests from a bare harness with no game code; determinism proven by
golden-image tests; the one-way dependency rule is enforced by an automated check.
