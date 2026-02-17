# Placeholder & Art Sourcing Guide

> This guide covers where to find placeholder images for development testing, and where to source or generate final art. The game runs without any image files thanks to `placeholders.rpy` — this guide is for when you want to start swapping in real visuals.

---

## 1. Quick Start

The game currently uses `game/placeholders.rpy` which defines all 58 backgrounds as coloured rectangles with text labels. **To replace any placeholder:**

1. Create the image file at 1920×1080 (backgrounds) or appropriate size (sprites)
2. Name it exactly as the tag — e.g. `bg_thames_night.png`
3. Place it in `game/images/bg/`
4. Delete the corresponding `image` line in `placeholders.rpy` (or delete the whole file when all are replaced)

Ren'Py will automatically pick up images from `game/images/` by filename.

---

## 2. Folder Structure

```
game/images/
├── bg/                     # 58 backgrounds (1920×1080 PNG or WEBP)
│   ├── london/             # Optional grouping — see naming note below
│   ├── plymouth/
│   ├── cornwall/
│   └── hoe/
├── characters/             # Character sprites
│   ├── amelia/             # e.g. amelia_neutral.png, amelia_happy.png
│   ├── sarah/
│   ├── ella/
│   ├── lucas/
│   ├── zara/
│   ├── raj/
│   ├── liz/
│   ├── maya/
│   ├── tasha/
│   ├── sophia/
│   ├── hawthorne/
│   ├── simmons/
│   ├── elena/
│   ├── david/
│   ├── grace/
│   ├── lily/
│   ├── michael/
│   └── mr_osei/
├── cg/                     # CG event illustrations (1920×1080)
│   ├── cg_thames_night.png
│   ├── cg_movein_kitchen.png
│   ├── cg_the_bench.png
│   └── ... (12 core + 7 endings)
└── ui/                     # UI elements
    ├── main_menu_bg.png
    ├── textbox.png
    ├── journal_bg.png
    └── phone_frame.png
```

### Important: Naming Convention

**Backgrounds** use flat names with underscores. Since our scripts say `scene bg_thames_night`, the file must be named `bg_thames_night.png` (or .webp/.jpg). You can put them in subdirectories but then you need explicit `image` declarations in a .rpy file mapping the path → tag name.

**Simplest approach:** Put all bg files directly in `game/images/bg/` with their full tag name.

**Characters** will use `layeredimage` declarations (to be written in Phase 3.5.2), so they can live in any subfolder — the code will reference them by path.

---

## 3. Background Placeholder Sources

### Recommended: Free Stock Photo Sites

For temporary development placeholders — atmospheric photos that roughly match each location. These are just for testing layout and mood; they'll be replaced by art-directed final images.

| Site | Strengths | Notes |
|------|-----------|-------|
| **[Unsplash](https://unsplash.com)** | High-quality, free, no attribution required | Best for moody landscapes and interiors |
| **[Pexels](https://pexels.com)** | Large library, free | Good for UK-specific locations |
| **[Pixabay](https://pixabay.com)** | Massive library, no attribution | Quality varies more |
| **[Flickr Creative Commons](https://flickr.com/creativecommons)** | Real Plymouth/Cornwall photos | Check individual licences |

### Search Terms by Location

| Background Cluster | Search Terms |
|-------------------|-------------|
| **London home** | `british terraced house interior`, `london kitchen evening light`, `teenager bedroom uk` |
| **Bookshop** | `independent bookshop interior warm`, `antiquarian bookshop shelves` |
| **Thames** | `thames night embankment`, `london river evening`, `thames sunset` |
| **Plymouth campus** | `uk university campus`, `modern university buildings`, `lecture theatre uk` |
| **Plymouth Hoe** | `plymouth hoe`, `plymouth sound`, `devon coastline grey` |
| **Student halls** | `uk student kitchen`, `university halls corridor`, `student bedroom uk` |
| **Library** | `university library interior`, `modern library study area`, `library night` |
| **Cornwall coast** | `cornwall coastline`, `cornish cliffs`, `cornwall dramatic sea` |
| **Bodmin Moor** | `bodmin moor`, `dartmoor misty`, `devon moorland` |
| **Mên-an-Tol** | `men an tol cornwall`, `cornish standing stones`, `neolithic stone ring` |
| **Merry Maidens** | `merry maidens cornwall`, `stone circle cornwall` |
| **Fogou** | `fogou cornwall`, `ancient underground passage`, `carn euny fogou` |
| **Tintagel** | `tintagel castle`, `tintagel coast cornwall` |
| **Hospital** | `nhs hospital corridor`, `uk hospital hallway` |

### Tip: Getting the Right Mood

For Nigredo chapters (1-3), look for images with warm shadows, golden hour, or overcast skies. For Albedo (4-7), seek out grey-blue coastal light, institutional interiors. For Cornwall scenes, moss and stone textures. The alchemical palette isn't just about colour grading — the *quality of light* matters most.

---

## 4. Character Sprite Sources

For visual novel character sprites, you need semi-transparent PNGs with multiple expressions. This is the trickiest category for placeholders since VN sprites have a specific format.

### Free VN Sprite Packs (for placeholder testing)

| Source | What's There | Link |
|--------|-------------|------|
| **itch.io "visual novel sprites"** | Hundreds of free/paid sprite packs in VN format | [itch.io/game-assets/tag-visual-novel](https://itch.io/game-assets/tag-visual-novel) |
| **itch.io "character sprites"** | More general, filter by free | [itch.io/game-assets/tag-character](https://itch.io/game-assets/tag-character) |
| **Sutemo's sprites** | High-quality free VN sprites, multiple expressions | Search itch.io for "Sutemo" |
| **noterminusgames** | Free diverse character sprites | Search itch.io for "noterminusgames" |
| **Lemma Soft Forums** | The main Ren'Py community — sprite sharing section | [lemmasoft.renai.us](https://lemmasoft.renai.us/forums/) |
| **OpenGameArt.org** | Free game art, some VN-format sprites | [opengameart.org](https://opengameart.org) |

### What to Look for in Placeholder Sprites

- **Format:** PNG with transparent background, roughly 700-1000px wide × 1200-1600px tall
- **Expressions:** At minimum neutral, happy, sad, surprised. More is better.
- **Style consistency:** All characters should look like they belong in the same game. Pick ONE sprite pack or artist — don't mix styles.
- **Diversity:** Amelia is mixed-race British-Jamaican. Sarah is British-white. Ella is Black British-Nigerian. Cast is diverse — ensure placeholder sprites reflect this, even approximately.

### For Final Art: Generation Options

When you're ready to create the real sprites using the prompt packs in `prompts/characters/`:

| Tool | Strength | Good For |
|------|----------|----------|
| **Midjourney** | Best at painterly/illustrated styles | Backgrounds, CGs, character reference sheets |
| **DALL-E 3** | Good consistency with detailed prompts | Character expressions, specific poses |
| **Stable Diffusion (ComfyUI)** | Full control, LoRA training possible | Consistent character faces across many expressions |
| **NovelAI** | Built for anime/VN art specifically | If you pivot to anime style |
| **Leonardo.ai** | Good free tier, character consistency tools | Testing and iteration |

### Key Technique: Character Consistency

The hardest part of AI-generated VN art is keeping characters looking like the *same person* across expressions. Strategies:

1. **Reference sheet first** — Generate a character sheet (front view, ¾ view, expressions) and use it as an image-to-image seed for all subsequent generations.
2. **LoRA training** (Stable Diffusion) — Train a small model on 10-20 images of your character. Best consistency but most technical effort.
3. **Seed locking** — In Midjourney/SD, find a good generation and use the same seed + similar prompts for variants.
4. **Inpainting** — Generate the neutral pose, then inpaint only the face/mouth for expression variants. Keeps body/clothes identical.

The prompt packs in `prompts/characters/` are structured with "anchor" details specifically for this — every expression prompt includes the same physical description so generators don't drift.

---

## 5. CG Event Art

CGs are full 1920×1080 illustrations showing specific story moments. These are the most important art pieces — they're what players remember.

### Placeholder Approach
For CGs during development, use the same stock photo approach as backgrounds, or just leave them as the background + character sprites and add CGs later.

### For Final Art
CGs are best done last, after character designs are locked. Each CG prompt in `prompts/cg/cg_scenes.md` includes composition notes and character positioning.

**Priority order** (generate these first for maximum impact):
1. `cg_the_bench` — The iconic recurring image
2. `cg_fogou_interior` — Climactic mystical moment (4 tiers)
3. `cg_thames_night` — Opening emotional beat
4. Ending CGs — Player's final impression

---

## 6. UI Elements

| Element | Size | Format | Notes |
|---------|------|--------|-------|
| Main menu BG | 1920×1080 | PNG/WEBP | Painted style, the Bench at dawn |
| Textbox | 1920×250 | PNG with alpha | Semi-transparent, painterly edges |
| Namebox | 300×60 | PNG with alpha | Matches textbox style |
| Journal BG | 800×600 | PNG | Leather/paper texture |
| Phone frame | 400×700 | PNG with alpha | Modern smartphone frame |
| Choice buttons | 800×80 | PNG with alpha | 4 variants (one per alchemical phase) |

### UI Placeholder Sources
- **Ren'Py default GUI** — Already works out of the box. Good enough for all development.
- **itch.io "renpy gui"** — Some free GUI packs that drop in
- **Game-icons.net** — Free SVG icons for UI elements

---

## 7. Audio Placeholder Note

Not covered in this art guide, but for reference:
- **freesound.org** — Ambient sounds (rain, seagulls, wind, fire)
- **incompetech.com** — Royalty-free background music
- **freemusicarchive.org** — CC-licensed music for mood tracks

The 20 Dancing Salamanders/Geddon Bird songs are the primary audio — ambient sound effects are secondary.

---

## 8. Replacement Checklist

When swapping in final art, work through these in order:

1. **[ ] Main characters** (Amelia, Sarah, Ella, Lucas) — Most screen time
2. **[ ] High-frequency backgrounds** (halls kitchen, campus, Amelia's room, the Hoe)
3. **[ ] Mentors** — For the mentor chapter playthroughs
4. **[ ] Cornwall backgrounds** — The mystical heart of the story
5. **[ ] Supporting characters** — Less screen time, can come later
6. **[ ] CG scenes** — Once character designs are locked
7. **[ ] UI elements** — Polish phase
8. **[ ] London backgrounds** — Only used in Ch1, Ch10, Ch12

After replacing each category, playtest those chapters to verify sizing, positioning, and mood.

---

*See `prompts/` directory for the detailed generation prompts for each image.*
