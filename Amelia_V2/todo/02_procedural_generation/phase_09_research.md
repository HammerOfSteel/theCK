# Phase 09 — Procedural Generation: Research & Approach Selection

> *Goal: Understand the field, evaluate real tools/repos/frameworks, and choose a modular approach
> **before** writing engine code. Output is a written recommendation, not production code.*
> Read `../README.md` first for the engine/content split rule this track obeys.

---

## 9.1 Frame the problem
- [ ] **Define outputs precisely** — What must be generated for a VN?
      character sprites (base + expressions + outfits), backgrounds/environments, CG composites, tiling
      textures, palettes. List required resolutions/aspect from `design/art_direction.md`.
- [ ] **Define "procedural" for our case** — parametric assembly, rule-based composition, generative-model
      (diffusion) pipelines, or a hybrid. Note which give *deterministic, seed-reproducible* results.
- [ ] **2D vs 3D decision criteria** — VN needs 2D-presentable output. Options:
      pure 2D layered composition; 3D scene → rendered to 2D (VRoid/Blender/Godot render passes);
      diffusion + ControlNet for style. Score each on control, consistency, reuse, cost, offline-capability.
- [ ] **Reuse test** — For every candidate, ask: "Could this power a *different* game with only new content
      data?" Reject anything that can't.

## 9.2 Survey techniques (write notes per topic)
- [ ] **Parametric / layered 2D** — Modular sprite assembly (base + parts + palette swap), PSD/`layeredimage`
      pipelines, atlas packing. (Closest fit to Ren'Py's existing `layeredimage` system.)
- [ ] **Palette & material systems** — Programmatic recolour (map an alchemical phase palette onto grayscale
      masks), gradient maps, HSV shifting for phase-driven world colour.
- [ ] **Procedural environments (2D)** — Layer-based parallax scene composition, procedural skies/weather,
      noise-driven texture/detail, tile/wang-tile systems for interiors.
- [ ] **Procedural 3D → 2D render** — MakeHuman / VRoid Studio characters, Blender headless render pipelines,
      Godot scene-to-sprite export; evaluate for consistency vs. maintenance cost.
- [ ] **Generative model pipelines** — SDXL / diffusion + LoRA (style lock) + ControlNet/IP-Adapter (pose,
      composition, identity). Evaluate for *character identity consistency across expressions* (the hard
      problem for VN sprites) and for offline/local runnability.
- [ ] **Determinism & seeding** — How each approach reproduces the same output from a seed (critical for the
      engine's determinism guarantee).

## 9.3 Evaluate concrete repos / libraries / frameworks
> For each: license, language, maintenance status, offline capability, and — most importantly — how cleanly
> it can sit behind a game-agnostic engine boundary. Record findings in a comparison table.
- [ ] **Layered/2D asset tooling** — e.g. libraries for PSD → layered export, texture-atlas packers,
      image compositing libs (Pillow/`skia`/`Pixi`-style), Ren'Py `layeredimage` capabilities as a baseline
- [ ] **Character-creator engines** — VRoid Studio, MakeHuman, UMA-style modular systems, open-source
      "character creator" repos — for the 3D→2D option
- [ ] **Diffusion tooling** — ComfyUI (node graph = reusable pipeline), Automatic1111 API, `diffusers`;
      ControlNet / IP-Adapter / LoRA ecosystems for identity + pose control
- [ ] **Procedural/noise libs** — noise generators (Perlin/Simplex/OpenSimplex), WFC (Wave Function Collapse)
      implementations for tiling/interior layout
- [ ] **Existing procedural game frameworks** — study how engines expose generation as data-driven modules
      (for architecture ideas, not necessarily adoption)
- [ ] **Comparison matrix** — Score all candidates: control, consistency, licence, offline, cost,
      modularity/reuse, integration effort. Save as `research_findings.md` in this folder.

## 9.4 Prototype spikes (throwaway, in a scratch dir — not `engine/`)
- [ ] **Spike A — Layered 2D recolour** — Take one grayscale character/background, apply the 4 alchemical
      phase palettes programmatically. Proves palette-driven world colour with minimal assets.
- [ ] **Spike B — Identity consistency** — If pursuing diffusion: generate one character across 3 expressions
      with a locked LoRA/IP-Adapter; judge whether identity holds. This is the make-or-break test.
- [ ] **Spike C — Environment composition** — Compose one location from parallax layers + procedural sky.
- [ ] **Determinism check** — Re-run each spike with a fixed seed; confirm identical output.

## 9.5 Decide & document
- [ ] **Write `approach_decision.md`** — Chosen approach (2D/3D/hybrid), chosen tools, and the rationale
- [ ] **Define the engine API surface** — The minimal function signatures the core must expose
      (e.g. `generate_character(params, seed) -> layers`, `generate_environment(params, seed) -> image`)
- [ ] **Define the content schema** — JSON shape for a character/environment definition (what `content/amelia`
      files will contain)
- [ ] **Scope gate** — Confirm the chosen path is achievable without blocking Amelia's release. If it's too
      heavy, mark it "engine-track continues post-Amelia" and let Phase 14 use manual art.

---

**Exit criteria:** `research_findings.md`, `approach_decision.md`, a locked engine API surface, and a content
schema — all written down. No production engine code yet; that's Phase 10.
