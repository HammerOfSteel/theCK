# The CK: Amelia V2 — Art Direction

> Visual identity and design language for the V2 rewrite. All art is AI-generated (DALL·E 3 or equivalent). This document specifies style, colour, composition, and mood so that every image feels like it belongs to the same world.

---

## 1. VISUAL PHILOSOPHY

**Amelia is not anime. Amelia is not photorealistic. Amelia is painterly.**

The visual style sits between a watercolour illustration and a soft oil painting — the kind of thing you'd find in a contemporary British literary novel dust jacket. Think: Sally Mann's light, Andrew Wyeth's mood, and the muted warmth of a Ghibli background composition.

### Core Principles
1. **Atmosphere over detail.** A blurred coastline with the right light says more than a pixel-perfect photograph.
2. **Colour tells the story.** The alchemical palette (see §3) shifts across the game. A player who pays attention will notice the world changing colour around them.
3. **Faces are felt, not photographed.** Characters appear in CG scenes and sprites with expressive but slightly impressionistic features — clear enough to read emotion, soft enough to allow the player's imagination to fill in detail.
4. **Cornwall is a character.** The landscape art is the most detailed element of the game. The sea, the moor, the stone, the light — these must be beautiful and specific.
5. **Consistency over perfection.** Every image must feel like it came from the same artist's hand, even though it came from an AI. Prompt discipline is everything.

---

## 2. RESOLUTION & ASPECT RATIO

| Element | Resolution | Aspect |
|---------|-----------|--------|
| Background scenes | 1920 × 1080 | 16:9 |
| Character sprites | ~600 × 900 (variable) | Portrait |
| CG (full-screen event art) | 1920 × 1080 | 16:9 |
| UI elements (textbox, etc.) | Various | Match 1920 × 1080 canvas |
| Phone screen mockups | ~400 × 700 (inset panel) | ~9:16 |
| Journal entries | ~800 × 600 (overlay) | 4:3 |
| Main menu background | 1920 × 1080 (or video) | 16:9 |

---

## 3. THE ALCHEMICAL COLOUR PALETTE

The game's colour temperature shifts across four macro-phases, mirroring the Magnum Opus. This is the core visual storytelling device — the player doesn't need to know it's alchemy; they'll *feel* the world changing.

### Phase 1: NIGREDO (Chapters 1–3)
**Dominant:** Warm darks — burnt umber, charcoal, deep amber
**Accent:** Gold (from London streetlights, the bookshop, Ella's warmth)
**Sky:** Bruised. Sunsets. Heavy cloud.
**Light source:** Artificial — tungsten lamps, phone screens, kitchen bulbs.

| Hex | Name | Usage |
|-----|------|-------|
| `#2C1810` | Burnt Umber | Background shadow tone |
| `#4A3728` | Charcoal Brown | Interior walls, furniture |
| `#8B6914` | Dark Gold | Accent — bookshop glow, lamplight |
| `#FFD700` | True Gold | UI accent (carried from V1), Ella's texts |
| `#1A1A2E` | Midnight Blue | Night skies, Thames scene |
| `#6B4423` | Russet | Autumn leaves, moving boxes |
| `#D4A574` | Warm Sand | Skin tones, parchment |

### Phase 2: ALBEDO (Chapters 4–7)
**Dominant:** Cool whites and silvers — sea grey, chalk white, pale blue
**Accent:** Silver-blue (moon on water, Cornish granite, winter light)
**Sky:** Opening. Grey cloud breaking to pale blue. Dawn scenes.
**Light source:** Natural — cold daylight, sea reflection, candlelight in Maya's scenes.

| Hex | Name | Usage |
|-----|------|-------|
| `#C8D6E5` | Sea Grey | Plymouth skies, university buildings |
| `#F0EDE5` | Chalk White | Paper, whiteboard, snow |
| `#7BA7BC` | Cornish Blue | The sea, Hoe background |
| `#A8B5C5` | Silver | Stone circles, granite, fog |
| `#2C3E50` | Deep Slate | Shadows, Sarah's room |
| `#E8DCC8` | Parchment | Books, letters, journal |
| `#9B8EC4` | Lavender | Maya's scenes, ceremony |

### Phase 3: CITRINITAS (Chapters 8–9)
**Dominant:** Yellows — saffron, amber, pale lemon
**Accent:** Red (crisis), then shifting to sunrise gold (reward)
**Sky:** Storm breaking. Lightning. Then — dawn.
**Light source:** Dramatic — hospital fluorescent (Ch8), sunrise breaking through rain (Ch9).

| Hex | Name | Usage |
|-----|------|-------|
| `#DAA520` | Goldenrod | The turn — crisis becoming clarity |
| `#F4D03F` | Saffron | Warm light returning, exam scenes |
| `#8B0000` | Dark Red | Ch8 crisis (subtle — not garish) |
| `#FFFFF0` | Ivory | Hospital walls, blank page |
| `#FFF8DC` | Cornsilk | Recovery light, gentle morning |
| `#B8860B` | Dark Goldenrod | Mentor reveals, deep knowledge |
| `#FFE4B5` | Moccasin | Character warmth returning |

### Phase 4: RUBEDO (Chapters 10–12)
**Dominant:** Rich reds — wine, rose, terre verte, sunset
**Accent:** Full spectrum (integration — all previous colours return)
**Sky:** Clear. Wide. The weather has turned. Summer.
**Light source:** Golden hour. Sunset. Fire.

| Hex | Name | Usage |
|-----|------|-------|
| `#722F37` | Wine | Depth, maturity, Amelia's growth |
| `#C0392B` | Cinnabar Red | The alchemical red — Rubedo complete |
| `#E8A87C` | Peach | Skin in warm light, family scenes |
| `#2E8B57` | Sea Green | Cornwall in summer, life returning |
| `#FFD700` | True Gold | Returns from Nigredo — the circle closes |
| `#800020` | Burgundy | Elena's scenes, the Fogou |
| `#F5CBA7` | Apricot | Ella reunion, warmth of ending |

### Colour Rules
- **Never** use pure black (`#000000`) or pure white (`#FFFFFF`) in scene art. Always tint.
- **Sarah's scenes** trend 20% cooler and more desaturated than surrounding chapter norms. Her room in Ch6 should feel like the temperature dropped.
- **Elena's scenes** always have a warmth offset — even in the Albedo phase, her cottage has amber candlelight.
- **Phone screens** glow with the UI gold (`#FFD700`) regardless of phase, anchoring the player in the familiar.
- **The Grief ending** is the only ending that stays in Nigredo — the colour never fully warms.

---

## 4. CHARACTER VISUAL DESIGN

### 4.1 Amelia Chen
- **Age:** 18
- **Build:** Average height, slim. Mixed heritage (Chinese-British).
- **Hair:** Black, shoulder-length, usually tied back loosely. Gets messier as the year goes on (intentional visual arc).
- **Eyes:** Dark brown, expressive.
- **Wardrobe:** Practical. Jeans, boots, jumpers. A denim jacket that becomes iconic. Carries a canvas tote bag.
- **Colour key:** Deep blue denim / warm brown leather of bag.
- **Expression range:** Curious → anxious → resolved → warm → broken → rebuilt.
- **Visual arc:** Ch1: neat, tidy, careful. Ch4-5: more relaxed, slightly rumpled. Ch8: exhausted, raw. Ch12: settled, grown, still herself.

### 4.2 Ella Blackwood
- **Age:** 18
- **Build:** Taller than Amelia. Athletic. Black British, Afro-Caribbean heritage.
- **Hair:** Natural curls, big and beautiful. Sometimes in a headwrap.
- **Eyes:** Bright. Always looks like she's about to laugh or fight.
- **Wardrobe:** Colourful. Vintage finds. Dungarees, doc Martens, band tees. She is the most visually warm character.
- **Colour key:** Sunflower yellow / burnt orange.
- **Expression range:** Joy → fierce protectiveness → worry → hurt → determined.
- **Note:** Ella appears primarily in phone screens and London chapters. Her visual warmth should contrast sharply with Plymouth's cooler palette.

### 4.3 Professor Hawthorne
- **Age:** Late 50s
- **Build:** Tall, thin, slightly stooped. White British.
- **Hair:** Grey, thinning, swept back.
- **Wardrobe:** Worn tweed jacket, reading glasses pushed up on forehead, open-collar shirt. Academic shabby-genteel.
- **Colour key:** Muted olive / warm grey.
- **Expression range:** Wry amusement → sharp focus → rare warmth → devastating honesty.

### 4.4 Dr. Simmons
- **Age:** Early 40s
- **Build:** Medium height, rounded, warm. Ethnicity: open (British South Asian suggested for visual interest).
- **Hair:** Dark, usually in a neat braid or low bun.
- **Wardrobe:** Professional but approachable. Soft cardigans, nice scarves, sensible shoes.
- **Colour key:** Warm burgundy / cream.
- **Expression range:** Patient listening → gentle challenge → quiet delight → rare tears.

### 4.5 Maya Penrose
- **Age:** Mid 30s
- **Build:** Small, wiry, energetic. White British (Cornish).
- **Hair:** Long, dark red, often loose. Occasionally braided with ribbons or thread.
- **Wardrobe:** Bohemian-practical. Long skirts, boots, layers. Lots of rings. A necklace with a stone.
- **Colour key:** Deep green / earthen red.
- **Expression range:** Warm welcome → intense focus → mysterious → grounded.
- **Note:** Maya must NOT look like a hippie caricature. She's a working professional who happens to study folklore. Think: a university lecturer who also knows where the ley lines run.

### 4.6 Elena Voskresenskaya
- **Age:** 70s
- **Build:** Small, sharp, wiry. Slavic features (Russian émigré heritage, settled in Cornwall decades ago).
- **Hair:** White, cropped short. No-nonsense.
- **Wardrobe:** Practical Cornish country — waxed jacket, wellies, wool. Inside her cottage: a thick shawl, always cold.
- **Colour key:** Storm grey / amber candle glow.
- **Expression range:** Appraising → amused → stern → the rare unguarded moment of gentleness.
- **Her cottage:** The most important set in the game for the Elena path. Must feel: warm, crowded (books, herbs, stones, tools), lived-in for decades, not staged. Like walking into a different century.

### 4.7 Sarah Whitmore
- **Age:** 18
- **Build:** Small, thin (gets thinner). White British.
- **Hair:** Mouse brown, straight, often tucked behind ears. Becomes lank and unwashed in the depression spiral.
- **Eyes:** Grey-green. Alert in good moments. Vacant when she's bad.
- **Wardrobe:** Oversized jumpers. Jeans. Converse. Layers that hide her body.
- **Colour key:** Grey / pale blue — the coolest palette of any character.
- **Expression range:** Quiet observation → gentle humour → withdrawal → flatness → absence.
- **Visual arc:** Ch2: present, soft, slightly shy. Ch5: paler, thinner, less eye contact. Ch6: unwashed hair, dark circles. Ch8: depending on outcome.
- **CRITICAL: The wren tattoo** on her inner left wrist. Small, hand-drawn style. It must appear in sprites consistently. It is a recurring visual motif.

### 4.8 Lucas Holloway
- **Age:** 18
- **Build:** Tall, lanky. White British, West Country accent visualised through relaxed posture.
- **Hair:** Sandy, floppy, needs cutting.
- **Wardrobe:** Academic casual. Button-down over t-shirt. Glasses he occasionally forgets.
- **Colour key:** Navy / warm brown.

### 4.9 Zara Chen (no relation)
- **Age:** 19
- **Build:** Medium height, confident posture. Chinese-Malaysian heritage.
- **Hair:** Black, usually in a high ponytail. Streak of colour (changes each term — starts blue).
- **Wardrobe:** Streetwear meets vintage. Shows confidence. Earrings always.
- **Colour key:** Electric blue / black.

### 4.10 Raj Patel
- **Age:** 18
- **Build:** Stocky, solid. British-Indian.
- **Hair:** Black, short, neat.
- **Wardrobe:** Comfortable. Joggers, hoodies, trainers. Always smells like his own cooking.
- **Colour key:** Warm terracotta / cream.
- **Note:** The flatmate visual key. He is in the kitchen or near it in every flat scene.

### 4.11 Minor Characters (Sprite Notes)
- **Tasha:** Put-together. Blonde, styled. Expensive casual. Colour: cold pink / white.
- **Sophia:** Academic chic. Brunette, structured outfits. Colour: slate / emerald green.
- **Liz:** Bright, messy bun, surf-adjacent. Colour: turquoise / sandy yellow.
- **Michael:** Sporty, rugby build. Colour: red / navy.
- **David (Amelia's dad):** Working-class solid. Paint-stained hands. Colour: warm grey.
- **Grace (Amelia's mum):** Neat, warm. Chinese heritage visible. Colour: soft rose.
- **Lily (Amelia's sister):** Younger, sharper, more fashion-conscious. Colour: bright red.

---

## 5. KEY LOCATION ART

### 5.1 Plymouth Locations

**The Flat (Halls/Shared House)**
- Standard UK student accommodation. Magnolia walls, blue carpet, cheap furniture.
- The kitchen is the heart: too small, always busy, notice board on the wall.
- Shot types: kitchen (most common), corridor, individual rooms.
- Lighting: warm-tungsten overhead, window light from small windows.
- **Sarah's room:** Same layout as others but progressively darker across chapters. Ch2: tidy, fairy lights, art on walls. Ch6: curtains closed, dishes accumulated, fairy lights off.

**University of Plymouth Campus**
- Brutalist 1960s architecture softened by coastal light.
- The library: fluorescent, busy, functional. A place of work not beauty.
- Lecture halls: tiered seating, projector glow.
- The Roland Levinsky building: the one interesting piece of architecture — angular, glass, can be dramatic.

**Plymouth Hoe**
- The iconic Hoe promenade, Smeaton's Tower (red and white lighthouse), the sea beyond.
- Drake's Island visible in the Sound.
- **THE BENCH:** A specific weathered wooden bench facing the sea. This is Sarah's bench. It appears in Ch3 and Ch12. It should look the same both times. The world around it should look different.
- Weather and time of day vary: the Hoe must work at grey-afternoon (Ch3), rainy-night (Ch6), and summer-evening (Ch12).

**The Barbican**
- Cobbled streets, Tudor buildings, harbour.
- The bookshop (Ch1 extension, if applied to Plymouth): cramped, warm, floor-to-ceiling books. An ouroboros carved into the door frame (hidden detail).
- Pubs: traditional, low ceilings, warm light.

### 5.2 Cornwall Locations

**Mên-an-Tol**
- Three standing stones on open moorland. The holed stone (the Men) is central.
- Must feel ancient and matter-of-fact. These stones have been here longer than English.
- Light: pale, open, exposed. Wind visible in the grass.
- For the Elena path: moonlight variant (blue-silver, dramatic).

**Merry Maidens Stone Circle**
- 19 stones in a neat circle in a farmer's field.
- Accessible and unguarded. A stile in the hedge, a dirt path.
- Must feel: smaller than expected, more powerful than expected.

**Madron Holy Well**
- Deep in a wood, down a muddy path. The ruined baptistry. The well itself.
- Clootie rags tied to branches — strips of cloth, faded and rotting. Eerie and beautiful.
- Light: dappled, filtered through leaves. Green-gold.

**Carn Euny Fogou**
- A stone-lined passage underground. The entrance: a dark mouth in a hillside.
- Inside: torchlight (or candlelight) on ancient stone. Close, cold, echo.
- **This is the most important single image in the Elena path.** The fogou must feel like entering the earth — not a dungeon, not a cave, but the body of the land itself.
- Four potential renderings based on the Karma Dice tier (see alchemical_thread_map.md): unsettling, clarifying, numinous, transcendent.

**Elena's Cottage**
- A stone cottage on the clifftop near Zennor (or similar).
- Exterior: granite walls, slate roof, wind-bent trees, a garden of herbs and wildflowers.
- Interior: one central room with a fireplace. Shelves of books and jars. A worn wooden table. Dried plants hanging from beams. A chair with a cat on it.
- Must feel: *real*, not magical. The magic is in what Elena knows, not in how the room is decorated. No crystals, no pentagrams. This is a pellar's house — it looks like a grandmother's cottage because it is one.

### 5.3 London Locations (Chapters 1 & 10)

**Hackney**
- Amelia's home. A terraced house, ex-council, lovingly maintained.
- The kitchen: small, warm, rice cooker on the counter, Chinese calendar on the wall.
- David's building site visible from the window.
- Ella's house is nearby but we only see it via phone screen.

**The Thames at Night**
- Ch1 reflection scene. The South Bank, city lights on water.
- Atmosphere: beautiful but melancholy. This is goodbye. The water is black and gold.

**London in Ch10 (Return)**
- The same places but Amelia sees them differently.
- The house is smaller. The streets are louder. It's still home, but she's changed.
- Visual shift: Rubedo palette — warmer, redder than Ch1's Nigredo.

---

## 6. UI DESIGN

### 6.1 Textbox
- **V1 legacy:** Gold accent `#FFD700`, textbox with white outline, DejaVuSans font.
- **V2 approach:** Keep the gold accent as continuity. Redesign the textbox:
  - Semi-transparent dark panel with soft rounded edges
  - Font: switch to a clean serif for dialogue (Georgia or similar), sans-serif for UI
  - Character name displayed in gold above the textbox
  - Dialogue text in off-white `#F5F5F0` with subtle drop shadow instead of outline
  - The textbox should feel like it's sitting on the image, not stamped over it

### 6.2 Choice Menu
- Choices displayed as clean buttons with:
  - Soft background that matches the current alchemical phase colour
  - Hover state: gold outline glow
  - Selected: brief gold pulse
- **No stat indicators visible.** Choices should not telegraph their consequences.
- If a choice is gated (e.g., Elena path requires OK ≥ 5), show it as greyed with a faint lock icon (no text explaining why — let the player wonder).

### 6.3 Phone Screen
- **This is the most innovative UI element.** Texting scenes appear on a simulated phone screen.
- Phone appears as a centred overlay (400 × 700) with:
  - Rounded corners, dark mode UI
  - iMessage-style bubbles (blue for Amelia, grey for others)
  - Typing indicators (three dots) for tension
  - Timestamps that correspond to in-game time
  - Contact names per relationship level (e.g., Ella starts as "Ella 🤍", Raj as "Raj 🍳" because he set it himself)
- Text input choices appear as pre-typed messages the player selects from
- Phone can also show: social media posts (for Tasha drama), photos sent between characters, missed call notifications

### 6.4 Journal Screen
- Accessible via menu button. Amelia's in-game journal.
- Looks like a physical notebook — lined paper background, handwriting font for Amelia's entries
- Tabs: **Notes** (story recap, automatic), **People** (character notes unlocked by interaction), **Curiosities** (alchemical/occult details unlocked on Elena path)
- The "Curiosities" tab starts empty. On OK ≥ 5, it begins to fill with Amelia's drawings of symbols, quotes from Paracelsus, Kernewek words she's learned.
- **The journal is the player's reward for paying attention.** It is never required to progress; it is always worth reading.

### 6.5 Main Menu
- **V1:** Video background (`Amelia_Intro_BG_NO_SOUND.webm`), gold text.
- **V2 concept:** A slow-panning image of the Plymouth Hoe at dusk.
  - The bench (Sarah's bench) visible in the middle distance.
  - The sea beyond. Drake's Island.
  - Music: instrumental, acoustic guitar and strings. Cornish-influenced. Gentle.
  - Menu items in gold, left-aligned, clean:
    - **New Story**
    - **Continue**
    - **Chapters** (replay)
    - **Journal**
    - **Settings**
    - **Content Warnings**

### 6.6 Settings Additions
- **Sensitive Content Mode:** Toggle that adds per-scene content warnings before difficult scenes.
- **Helpline Information:** Always accessible. UK helplines displayed.
- **Text Speed:** Standard Ren'Py control but also:
  - **"Linger" mode:** Pauses text auto-advance at emotionally significant lines (the player must click to continue). On by default.

---

## 7. CG (EVENT ART) SPECIFICATIONS

### Key CG Scenes (Minimum Set)

| # | Chapter | Scene | Composition | Mood |
|---|---------|-------|-------------|------|
| 1 | Ch1 | Thames at night | Amelia standing at the South Bank railing, city lights reflecting on black water. Back to camera. | Melancholy, departure |
| 2 | Ch2 | Move-in day | The flat kitchen, group gathered. Raj at the stove. Amelia in the doorway. Sarah in the corner with her tea. | Warmth, possibility |
| 3 | Ch3 | The bench | Amelia and Sarah on the bench at the Hoe. Wide shot — two small figures, the enormous sea. | Quiet, honest, cold |
| 4 | Ch4 | Mentor meet | Three variants: Hawthorne's office (books, desk lamp), Simmons' therapy room (soft light), Maya's seminar (candles, objects) | Knowledge, first trust |
| 5 | Ch5 | The Merry Maidens | Stone circle at dusk. Amelia standing among the stones. Wind in her hair. | Awe, threshold |
| 6 | Ch6 | Sarah's room | Doorway perspective — Amelia looking into the dim room. Light from the corridor behind her. Sarah on the bed. | Heartbreak, care |
| 7 | Ch7 | Fogou entrance | Carn Euny passage mouth. Elena ahead with a lantern. Amelia about to enter. | Fear, trust, descent |
| 8 | Ch8 | The crisis | NOT the event itself. Amelia in a hospital corridor. Fluorescent light. Her hands. A paper cup of water. | Devastation, sterility |
| 9 | Ch9 | Result day | Amelia looking at a screen/paper. Expression depends on stat outcome. | Relief/anxiety |
| 10 | Ch10 | Return to London | The terraced house. Amelia at the front door. She's taller somehow. | Homecoming, change |
| 11 | Ch11 | Fogou interior (Elena path) | Inside the passage. Stone walls. Candle/torch light. Ancient carvings barely visible. | Transcendence |
| 12 | Ch12 | Ending variant | One per ending (7 total). These are the most important images in the game. |

### CG Composition Rules
1. **Amelia should be in most CGs** — the player is seeing through/alongside her
2. **Leave textbox-safe space** along the bottom 15% of every CG
3. **Faces in CGs should be more detailed** than sprites — these are the emotional peaks
4. **Lighting must match the alchemical phase** — check colour palette before generating
5. **No background character in a CG unless they matter** — empty space is powerful

---

## 8. AI IMAGE GENERATION — PROMPT DISCIPLINE

### Standard Prompt Structure
```
[Style] + [Subject] + [Setting] + [Lighting] + [Mood] + [Colour palette] + [Composition] + [Negative prompts]
```

### Style Prefix (Use for ALL images)
```
Painterly illustration, soft oil painting style, muted palette with [PHASE COLOUR],
contemporary British literary illustration, slightly impressionistic,
atmospheric lighting, no anime, no photorealistic, no cartoons
```

### Example Prompts

**The Bench (Ch3 CG):**
```
Painterly illustration, soft oil painting style, muted Albedo palette with sea grey 
and pale blue. Two young women sitting on a weathered wooden bench on Plymouth Hoe, 
facing the English Channel. Wide shot, the figures are small against the vast grey sea 
and overcast sky. Smeaton's Tower lighthouse visible in the distance. October afternoon, 
cold light, wind in their hair. The mood is honest and quiet and a little sad. 
Contemporary British literary illustration style. No anime, no photorealistic.
```

**Elena's Cottage Interior:**
```
Painterly illustration, soft oil painting style, warm amber and storm grey palette.
Interior of a small Cornish stone cottage. Ancient stone walls, low ceiling with 
dried herbs hanging from wooden beams. A lit fireplace casting warm orange light. 
Bookshelves overflowing with old volumes, jars of herbs and tinctures, a worn wooden 
table with a pestle and mortar. A grey cat curled in an armchair. One candle on the 
table. The feeling of decades of quiet knowledge. No crystals, no pentagrams — 
this is practical, lived-in, real. Contemporary British literary illustration style.
```

### Negative Prompt Library
Always include in relevant combinations:
```
No anime style, no manga, no photorealistic, no 3D render, no cartoon,
no neon colours, no high saturation, no fantasy clichés, no magic effects,
no glowing runes, no sparkles, no lens flare, no dramatic poses,
no exaggerated proportions, no sexualised content
```

### Consistency Tips
- Save working prompts and reuse with variations
- Reference specific real locations (Smeaton's Tower, Mên-an-Tol) for AI grounding
- Include "British" or "English" or "Cornish" to prevent the AI defaulting to American visual culture
- Always specify time of day and weather — AI defaults to sunny if you don't
- For character sprites: generate in consistent batches (all expressions for one character in one session)

---

## 9. SPRITE SPECIFICATIONS

### Expression Set (Per Character)
Each major character needs these expression states (minimum):

| State | Description |
|-------|-------------|
| `neutral` | Default resting face |
| `happy` | Genuine smile |
| `sad` | Downcast, eyes lowered |
| `angry` | Tight jaw, hard eyes |
| `surprised` | Wide eyes, open mouth |
| `thinking` | Looking aside, slight frown |
| `worried` | Brow furrowed, lips tight |
| `laughing` | Full laugh, head tilted |

**Additional for key characters:**
- **Amelia:** `anxious`, `determined`, `tearful`, `peaceful`
- **Sarah:** `withdrawn` (eyes half-closed, looking down), `present` (alert, engaged — rare after Ch5), `flat` (no expression — the scariest one)
- **Elena:** `appraising`, `teaching`, `vulnerable` (used once, maybe twice, in the whole game)
- **Ella:** `fierce`, `protective`, `exasperated-but-loving`

### Sprite Layering
Ren'Py supports composite sprites. Recommended approach:
- **Base:** Body + clothes (1-2 outfit variants per character per chapter group)
- **Face:** Expression overlay (interchangeable)
- **Accessory:** Optional (Amelia's tote bag, Zara's earrings, Raj's apron)
- This allows maximum variety from minimum asset count

### Outfit Changes
Characters don't wear the same thing every day. Minimum outfit variants:

| Character | Casual | Academic | Going Out | Ch10 London | Special |
|-----------|--------|----------|-----------|-------------|---------|
| Amelia | 3 | 1 | 1 | 1 (home clothes) | 1 (Ch12 ending) |
| Ella | 2 | — | 1 | 1 | — |
| Sarah | 2 (one gets worn repeatedly from Ch5) | 1 | — | — | — |
| Lucas | 2 | 1 | — | — | — |
| Others | 1-2 | 1 | — | — | — |

---

## 10. AUDIO DIRECTION (Brief)

*A full audio document may be produced later. Key points for visual-audio sync:*

### Music Palette
- **Instrument core:** Acoustic guitar, strings, piano. Simple. British folk-adjacent.
- **Cornwall scenes:** Add concertina or fiddle. Never cheesy. Think: Sam Lee, Kathryn Tickell, This Is The Kit.
- **Crisis (Ch8):** Near-silence. A held drone. The sound of fluorescent lights.
- **Endings:** Each has its own musical identity:
  - Scholar: Piano, resolving chord
  - Companion: Full ensemble, warm
  - Healer: Strings, gentle
  - Alchemist: Strange, harmonic, a fifth that shouldn't resolve but does
  - Whole: All instruments together, simple melody
  - Grief: Solo guitar, incomplete phrase
  - Bittersweet: The main theme in a minor key, then fading

### Ambient Sound
- **Plymouth:** Seagulls, traffic, rain, pub chatter, university corridor echo
- **Cornwall:** Wind (always wind), sea on rocks, sheep, birdsong, crackling fire (Elena's cottage)
- **London:** Different traffic, different sirens, different birds. The player should *hear* that they've left.

### The Silence
Some scenes should have NO music. Specifically:
- Sarah's room visit (Ch6)
- Parts of the Fogou descent
- The moment Amelia receives news in Ch8 (Tier 4)
- The bench, both times (Ch3 and Ch12)

---

## 11. VISUAL MOTIFS & RECURRING SYMBOLS

These images should recur throughout the game, connecting scenes across chapters:

| Symbol | First Appearance | Recurrences | Meaning |
|--------|-----------------|-------------|---------|
| **The wren** | Sarah's tattoo, Ch2 | Sarah's drawings, a wren on the Hoe, a wren on Elena's windowsill | The smallest bird. Vulnerable but alive. In Celtic lore: king of birds. |
| **The bench** | Ch3 | Ch12 (all endings). Empty or occupied. | The place where truth is spoken and not spoken. |
| **The holed stone** | Mên-an-Tol, Ch5 | Amelia's journal sketches, a pendant, the fogou entrance shape | Passage. Transformation. Seeing through to the other side. |
| **Black water** | Thames, Ch1 | The sea at night, Sarah's room (metaphor), the fogou water | The *nigredo*. Dissolution. What you must enter to be changed. |
| **Gold light** | Bookshop, Ch1 | Ella's warmth, the Citrinitas dawn, the final ending | The gold that was there from the beginning, unrecognised. |
| **Dried herbs** | Elena's cottage | Maya's seminar, the hospital (lavender sachet from Raj), Amelia's room by Ch12 | Care. Tradition. What grows and is kept and given. |
| **Empty chair** | Lecture hall, Ch5 (Sarah absent) | The flat kitchen, the graduation ceremony | Absence as presence. Who is missing. |

---

*Last updated: February 2026*
