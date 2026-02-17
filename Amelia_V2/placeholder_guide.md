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

## 2. Folder Structure — Complete File Listing

> Every filename below is **exact**. Use `.png` or `.webp` — Ren'Py accepts either. All sizes are width × height.
> The code in `layered_images.rpy` and `placeholders.rpy` references these paths directly.

### 2.1 Backgrounds — `game/images/bg/` (58 files, each 1920×1080)

All backgrounds go directly in the `bg/` folder. The filename **must** match the scene tag used in scripts.

#### London (Nigredo — Ch1, Ch10, Ch12)
```
bg_james_kitchen_evening.png      # James family kitchen, warm evening light
bg_james_house_morning.png        # James house exterior, morning
bg_amelia_bedroom_night.png       # Amelia's London bedroom, night
bg_amelia_bedroom_dark.png        # Same bedroom, lights off / very dark
bg_amelia_home.png                # Amelia's London home, general
bg_family_home.png                # James family home, general
bg_park_bench_sunset.png          # Local park bench, golden hour
bg_bookshop.png                   # Independent bookshop exterior
bg_bookshop_interior.png          # Bookshop interior, warm shelves
bg_thames_night.png               # Thames embankment, night
bg_thames.png                     # Thames embankment, daytime
bg_london_cafe.png                # London café interior
bg_london_park.png                # London park, daytime
bg_london_train.png               # Train interior / platform
bg_lily_room.png                  # Lily's bedroom
bg_motorway_daytime.png           # Motorway driving view, daytime
```

#### Plymouth Campus (Albedo — Ch2–9)
```
bg_plymouth_first_sight.png       # First view of Plymouth from road/bridge
bg_campus_tour.png                # University campus during orientation tour
bg_campus_daytime.png             # Campus grounds, general daytime
bg_campus_quad.png                # Campus quadrangle / central green
bg_lecture_theatre.png            # Large lecture theatre interior
bg_psych_building.png             # Psychology building exterior
bg_psych_building_corridor.png    # Psychology building corridor
bg_psych_building_lecture.png     # Psychology lecture hall interior
bg_seminar_room.png               # Small seminar/tutorial room
bg_library.png                    # University library, daytime
bg_library_night.png              # Library at night, desk lamps
bg_library_study_area.png         # Library study area / reading nooks
bg_su_night.png                   # Student Union at night, lively
bg_barbican_bookshop.png          # Barbican Bookshop in Plymouth
bg_hawthorne_office.png           # Prof. Hawthorne's office (books, tweed)
bg_simmons_office.png             # Dr. Simmons's office (warm, plants)
bg_counsellor_office.png          # University counsellor's office
bg_hospital_corridor.png          # NHS hospital corridor
```

#### Plymouth Living (Albedo — Ch2–9)
```
bg_halls_kitchen_evening.png      # Student halls shared kitchen, evening
bg_halls_kitchen_night.png        # Same kitchen, late night
bg_kitchen_halls.png              # Kitchen in halls, general (alt angle)
bg_flat_kitchen.png               # Second-year flat kitchen
bg_flat_party.png                 # Flat during a party
bg_halls_corridor.png             # Halls of residence corridor
bg_amelia_room_plymouth_night.png # Amelia's Plymouth room, night
bg_amelia_room_plymouth_day.png   # Amelia's Plymouth room, daytime
bg_amelia_room_plymouth_rain.png  # Amelia's Plymouth room, rain on window
bg_lucas_room.png                 # Lucas's room
bg_maya_room_candlelit.png        # Maya's room, candles lit
bg_maya_room_ceremony.png         # Maya's room set up for ceremony
```

#### Plymouth Hoe
```
bg_plymouth_hoe_grey.png          # Plymouth Hoe, overcast grey sky
bg_plymouth_hoe_dawn.png          # Plymouth Hoe at dawn, warm light
bg_plymouth_hoe_day.png           # Plymouth Hoe, clear daytime
```

#### Cornwall (Earthy green)
```
bg_cornwall_coast.png             # Cornish coastline, dramatic
bg_cornwall_night.png             # Cornwall landscape at night
bg_bodmin_moor.png                # Bodmin Moor, misty
bg_men_an_tol.png                 # Mên-an-Tol stone formation
bg_merry_maidens.png              # Merry Maidens stone circle
bg_madron_well.png                # Madron Holy Well
bg_fogou_entrance.png             # Fogou entrance, dark stone
bg_tintagel.png                   # Tintagel castle/coast
bg_eden_project.png               # Eden Project biomes
```

---

### 2.2 Character Sprites — `game/images/characters/` (120 files total)

Each character has a subfolder. Files are full-body PNG sprites with **transparent background**, roughly **700×1400 px**. One file per expression. Characters with outfit variants get subfolders per outfit.

#### `characters/amelia/` — 12 expressions × 6 outfits = up to 72 files
Start with the `casual_autumn` set — it's the most used.
```
casual_autumn/
    neutral.png
    happy.png
    sad.png
    angry.png
    surprised.png
    thinking.png
    worried.png
    laughing.png
    anxious.png
    determined.png
    tearful.png
    peaceful.png
going_out/
    neutral.png   happy.png   sad.png   ... (same 12 expressions)
home_tired/
    neutral.png   happy.png   sad.png   ...
academic/
    neutral.png   happy.png   sad.png   ...
crisis/
    neutral.png   happy.png   sad.png   ...
summer/
    neutral.png   happy.png   sad.png   ...
```

#### `characters/sarah/` — 9 expressions × 4 outfits = up to 36 files
```
early_a/
    neutral.png           # Cream jumper, Ch2–5
    happy.png
    sad.png
    surprised.png
    thinking.png
    worried.png
    withdrawn.png         # Key expression — distant, hollow
    present.png           # Brief moments of connection
    flat.png              # Emotionally blank
early_b/
    neutral.png   happy.png   ... (same 9)
late_c/
    neutral.png   happy.png   ... (same 9, visually deteriorated)
recovery_d/
    neutral.png   happy.png   ... (same 9, new colours, healthier)
```

#### `characters/ella/` — 8 expressions × 3 variants = up to 24 files
```
casual_london/
    neutral.png
    happy.png
    sad.png
    fierce.png
    worried.png
    laughing.png
    exasperated.png
    hurt.png
going_out/
    neutral.png   happy.png   ... (same 8)
headwrap/
    neutral.png   happy.png   ... (same 8, headwrap instead of afro out)
```

#### `characters/lucas/` — 8 expressions × 2 outfits = 16 files
```
casual/
    neutral.png   happy.png   sad.png   worried.png
    surprised.png   thinking.png   laughing.png   vulnerable.png
academic/
    neutral.png   happy.png   ... (same 8)
```

#### `characters/zara/` — 8 expressions (single outfit)
```
neutral.png   happy.png   annoyed.png   surprised.png
thinking.png   determined.png   laughing.png   warm.png
```

#### `characters/raj/` — 8 expressions (single outfit)
```
neutral.png   happy.png   worried.png   laughing.png
serious.png   cooking.png   gentle.png   upset.png
```

#### `characters/liz/` — 6 expressions (single outfit)
```
neutral.png   happy.png   worried.png
surprised.png   laughing.png   concerned.png
```

#### `characters/hawthorne/` — 6 expressions (single outfit)
```
wry_amusement.png   sharp_focus.png   rare_warmth.png
devastating_honesty.png   disappointed.png   teaching.png
```

#### `characters/simmons/` — 6 expressions (single outfit)
```
patient_listening.png   gentle_challenge.png   quiet_delight.png
rare_tears.png   serious.png   encouraging.png
```

#### `characters/maya/` — 6 expressions (single outfit)
```
warm_welcome.png   intense_focus.png   mysterious.png
grounded.png   teaching.png   concerned.png
```

#### `characters/elena/` — 6 expressions × 2 variants = 12 files
```
indoors/
    appraising.png   amused.png   stern.png
    vulnerable.png   teaching.png   gentle.png
outdoors/
    appraising.png   amused.png   stern.png
    vulnerable.png   teaching.png   gentle.png
```

#### `characters/tasha/` — 4 expressions (single outfit)
```
pleasant.png   cruel.png   exposed.png   angry.png
```

#### `characters/sophia/` — 4 expressions (single outfit)
```
composed.png   calculating.png   genuine.png   conflicted.png
```

#### `characters/michael/` — 4 expressions (single outfit)
```
grinning.png   serious.png   confused.png   protective.png
```

#### `characters/david/` — 4 expressions (single outfit)
```
steady.png   proud.png   worried.png   laughing.png
```

#### `characters/grace/` — 4 expressions (single outfit)
```
warm.png   stern.png   tearful.png   proud.png
```

#### `characters/lily/` — 4 expressions (single outfit)
```
unimpressed.png   grinning.png   soft.png   laughing.png
```

#### `characters/mr_osei/` — 3 expressions (single outfit)
```
wise_warmth.png   thoughtful.png   gentle.png
```

---

### 2.3 CG Event Art — `game/images/cg/` (19+ files, each 1920×1080)

```
cg_thames_night.png               # CG1  — Amelia alone at Thames embankment
cg_movein_kitchen.png             # CG2  — First meeting in halls kitchen
cg_the_bench.png                  # CG3  — Amelia & Sarah on Plymouth Hoe bench
cg_mentor_hawthorne.png           # CG4A — First meeting with Hawthorne
cg_mentor_simmons.png             # CG4B — First meeting with Simmons
cg_mentor_maya.png                # CG4C — First meeting with Maya
cg_mentor_elena.png               # CG4D — First meeting with Elena
cg_merry_maidens.png              # CG5  — Group at Merry Maidens circle
cg_sarahs_room.png                # CG6  — Amelia at Sarah's door
cg_fogou_entrance.png             # CG7  — Standing at Fogou entrance
cg_crisis_corridor.png            # CG8  — Hospital corridor moment
cg_results.png                    # CG9  — Results day
cg_london_return.png              # CG10 — Returning to London, changed
cg_fogou_interior.png             # CG11 — Inside the Fogou (mystical)
cg_ending_grief.png               # CG12A — Grief ending
cg_ending_alchemist.png           # CG12B — Alchemist ending
cg_ending_scholar.png             # CG12C — Scholar ending
cg_ending_companion.png           # CG12D — Companion ending
cg_ending_healer.png              # CG12E — Healer ending
cg_ending_whole.png               # CG12F — Whole/integrated ending
cg_ending_bittersweet.png         # CG12G — Bittersweet ending
```

---

### 2.4 UI Elements — `game/images/ui/` (8+ files)

```
main_menu_bg.png                  # 1920×1080 — Main menu background
textbox.png                       # 1920×250  — Dialogue textbox (with alpha)
namebox.png                       # 300×60    — Character name box (with alpha)
journal_bg.png                    # 800×600   — Journal screen background
phone_frame.png                   # 400×700   — Phone overlay frame (with alpha)
choice_nigredo.png                # 800×80    — Choice button, Nigredo palette
choice_albedo.png                 # 800×80    — Choice button, Albedo palette
choice_citrinitas.png             # 800×80    — Choice button, Citrinitas palette
choice_rubedo.png                 # 800×80    — Choice button, Rubedo palette
content_warning_bg.png            # 1920×1080 — Content warning screen bg (optional)
```

---

### 2.5 Naming Rules

- **Backgrounds**: Filename = scene tag exactly. `scene bg_thames_night` → `bg_thames_night.png`
- **Characters**: Referenced by `layered_images.rpy` via path. Organised in subfolders by character and outfit.
- **CGs**: Use `cg_` prefix. Referenced explicitly in scripts when added.
- **UI**: Referenced by `gui.rpy` and `screens.rpy` via path.
- **Format**: PNG preferred (lossless + alpha). WEBP also works. JPG for backgrounds only (no alpha).
- **No spaces in filenames** — use underscores only.

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
