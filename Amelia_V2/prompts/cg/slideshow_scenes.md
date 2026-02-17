# Slideshow Scene Backgrounds — Image Prompts

> Backgrounds used specifically in the 20 song slideshow moments. These cycle as a song plays, each shown for ~12 seconds with dissolve transitions. They need to be atmospheric and mood-setting — no characters, no text. Pure visual atmosphere.

---

## GENERATION APPROACH

Each slideshow in slideshows.rpy cycles through 8-14 background scenes. Many reuse backgrounds from the main game (bg_cornwall_coast, bg_plymouth_hoe_grey, etc.) — those are already covered in the background prompt files. This file covers **slideshow-specific backgrounds** that don't appear outside slideshows, or mood variants needed specifically for the musical atmosphere.

The slideshows are organised by chapter. See songs.md for full placement details.

---

## GENERAL SLIDESHOW STYLE

These are more impressionistic than gameplay backgrounds — leaning further into the "soft oil painting" end of the style spectrum. Think: album artwork, music video stills, atmospheric mood pieces.

```
Painterly illustration, soft oil painting style, 1920x1080 landscape. Atmospheric, impressionistic. No people visible. A mood piece — this image accompanies music and should feel like a feeling, not a location. [SPECIFIC DESCRIPTION]. Contemporary British literary illustration. No anime, no photorealistic.
```

---

## SLIDESHOW-SPECIFIC BACKGROUNDS NEEDED

### Rainy Window Close-up
```
Painterly illustration, soft oil painting style, 1920x1080. Close-up of rain on a window — rivulets of water catching the light, the world outside blurred and soft. Indoor warmth on one side, grey weather on the other. The glass is the boundary between comfort and exposure. Colour palette: varying — can be warm (amber behind) or cool (grey behind). No anime, no photorealistic.
```

### Empty Student Room — Morning Light
```
Painterly illustration, soft oil painting style, 1920x1080. An empty student bedroom in early morning light — the bed unmade, a coffee cup, sunlight falling across the desk through thin curtains. Someone has just left or is about to wake. The light is the subject. Peaceful, liminal. No anime, no photorealistic.
```

### Coastal Path — Mist
```
Painterly illustration, soft oil painting style, 1920x1080. A coastal path disappearing into sea mist, Cornwall. The path is visible for twenty metres, then the world fades to grey-white. Rough grass on either side. The sound of surf below, invisible. A metaphor for uncertainty. No anime, no photorealistic.
```

### Porthcurno Beach
**Used in: slideshow_ch8_oh_sarah (the "Oh Sarah" song moment)**
```
Painterly illustration, soft oil painting style, 1920x1080. Porthcurno Beach, Cornwall, England. Turquoise water in a sheltered cove between granite cliffs. White sand. The Minack Theatre carved into the cliff above. A specific, real, achingly beautiful place. Afternoon sun. The kind of beach that makes you feel the weight of things. No anime, no photorealistic.
```

### Empty Bench — Various Weather
```
Painterly illustration, soft oil painting style, 1920x1080. The bench on Plymouth Hoe — empty. WEATHER VARIANTS:
- Rain: The bench wet, the sea grey and angry, wind visible
- Snow: Frost on the slats, the sea steel-grey, everything quiet
- Dawn: First light catching the wood, the sea gold-grey
- Summer: The bench sun-warm, the sea blue, everything open
Generate 2-3 variants for reuse across slideshows. The bench is always the same. The weather is the emotion. No anime, no photorealistic.
```

### Kitchen — Night — One Light
```
Painterly illustration, soft oil painting style, 1920x1080. The flat kitchen at 3am — only the light over the stove on, casting a warm pool in the dark room. A single mug on the counter. The window shows city darkness. The intimacy of being the only one awake. No anime, no photorealistic.
```

### Cornwall Wildflowers
```
Painterly illustration, soft oil painting style, 1920x1080. Close-up of Cornish wildflowers — sea thrift, campion, gorse — on a clifftop. The flowers are in focus, the sea and sky soft behind them. Life persisting on the edge of the land. Warm, grounded, beautiful in a specific rather than generic way. No anime, no photorealistic.
```

### Hands Close-up Variants
For intimate slideshow moments:
```
Painterly illustration, soft oil painting style, 1920x1080.
- Two hands wrapped around a warm mug — comfort
- A hand on an open book page — knowledge
- Two hands (friendship) — one darker, one lighter — reaching or clasped
- A hand touching standing stone — connection to the ancient
Each should feel intimate, detailed, atmospheric. The hands tell the story. No anime, no photorealistic.
```

### Daffodils — Field
**Used in: All 7 daffodils ending slideshows**
```
Painterly illustration, soft oil painting style, 1920x1080. A field of daffodils in Cornwall or Devon — masses of yellow-gold flowers under spring sky. The iconic English spring image. Wordsworth's host of golden daffodils. The gold that was there from the beginning. This image should feel like the world exhaling. Generate VARIANTS:
- Wide field (full gold, blue sky, the promise fulfilled)
- Close-up (individual flowers, detail, water drops maybe)
- At dusk (gold flowers catching golden-hour light)
No anime, no photorealistic.
```

### Motorway at Night
```
Painterly illustration, soft oil painting style, 1920x1080. A motorway at night — red tail-lights stretching ahead in a long curve, white headlights coming the other way. The amber of sodium lamps. The feeling of distance and transition — between places, between lives. Impressionistic, the lights are the subject. No anime, no photorealistic.
```

### Pub Interior — Warm
```
Painterly illustration, soft oil painting style, 1920x1080. Interior of a traditional British pub — low ceilings, dark wood, warm light, bar with taps. No people (or distant silhouettes). The warmth of a specific kind of English social space — the pub as hearth. Colour palette: amber, dark wood, brass. No anime, no photorealistic.
```

### Tide Going Out
```
Painterly illustration, soft oil painting style, 1920x1080. The English Channel — the tide retreating from a rocky shore. Wet rock, reflected sky, tide pools, seaweed. The light is changing — either dawn or dusk. The feeling of something receding and something being revealed. No anime, no photorealistic.
```

---

## REUSE MAP

Most slideshow scenes reuse backgrounds from the main game. Here's what each slideshow draws from:

| Slideshow | Main bg assets reused | Slideshow-specific needed |
|-----------|----------------------|--------------------------|
| ch1_paper_planes | park_bench_sunset, thames_night, bookshop, bedroom | Rainy window |
| ch2_lighthouse | plymouth_first_sight, campus, halls, hoe_grey | Coastal path mist |
| ch3_two_birds | hoe_grey, library_night, amelia_room_rain | Empty bench rain variant |
| ch4_hawthorne | bodmin_moor, madron_well, merry_maidens | Hands on book |
| ch5_circles | cornwall_coast, men_an_tol, campus_quad | Wildflowers |
| ch6_kindeling | family_home, halls_corridor, cornwall_night | Kitchen one-light |
| ch7_mirror | library_study, hoe_day, amelia_room_night | Rainy window variant |
| ch8_oh_sarah | cornwall_coast, hoe_grey | Porthcurno Beach |
| ch8_forgetmeknot | halls_corridor, hoe_grey, amelia_room | Empty student room dawn |
| ch9_jolly_rum | cornwall_coast, eden, flat_kitchen | Pub interior |
| ch10_long_way_home | london_train, thames, bookshop | Motorway at night |
| ch10_here_now | hoe_day, campus_quad, amelia_room_day | Tide going out |
| ch11_between_veil | fogou_entrance, madron_well, cornwall_night | Hands on stone |
| ch11_the_work | library, campus_quad, amelia_room_day | Empty bench dawn |
| ch12_quiet_morning | park_bench, hoe_dawn | Empty room morning |
| ch12_amelia_credits | Multiple locations — journey montage | All variants |
| ch12_daffodils (×7) | Ending-specific bg | Daffodils field (all variants) |

---

## GENERATION PRIORITY

1. **Daffodils field** (wide) — Used in all 7 ending slideshows
2. **Empty bench variants** — Recurring motif across multiple slideshows
3. **Porthcurno Beach** — Specific, beautiful, needed for the "Oh Sarah" moment
4. **Rainy window** — Reused in multiple slideshows
5. **Coastal path mist** — Strong atmospheric piece
6–12. Remaining as needed
