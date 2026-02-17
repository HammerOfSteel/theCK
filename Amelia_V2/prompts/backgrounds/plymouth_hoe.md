# Plymouth Hoe & The Bench — Background Prompts

> The Hoe is Plymouth's most iconic location and the game's recurring outdoor anchor. Smeaton's Tower, the sea, Drake's Island — and THE BENCH. Four variants needed for different chapters and weather conditions. The bench appears in Ch3 and Ch12 — same bench, same view, different Amelia.

---

## bg_plymouth_hoe_grey
**Used:** Ch3 (the bench scene with Sarah — one of the game's defining moments)
**Phase:** Albedo — cold, vast, honest

```
Painterly illustration, soft oil painting style, 1920x1080 landscape. Plymouth Hoe on a grey October afternoon. The wide promenade, Smeaton's Tower (the red and white lighthouse) in the middle distance. The English Channel beyond — vast, grey-green, cold. Drake's Island visible in Plymouth Sound. An overcast sky, heavy cloud, the light flat and honest. Wind visible in the grass and the distant flags. A weathered wooden bench facing the sea — THE BENCH — in the mid-ground (characters will be composited). The mood is enormous and quiet. Two people could sit here and say honest things because the sea makes everything else small. Colour palette: Albedo — sea grey #C8D6E5, chalk white, cornish blue #7BA7BC, deep slate #2C3E50 for shadows. Contemporary British literary illustration. No anime, no photorealistic.
```

---

## bg_plymouth_hoe_dawn
**Used:** Ch4 (early morning walk), Ch8 (after the crisis), Ch11 (pre-Fogou)
**Phase:** Varies — Albedo (Ch4), Citrinitas (Ch8), Rubedo (Ch11)

```
Painterly illustration, soft oil painting style, 1920x1080 landscape. Plymouth Hoe at dawn. The eastern sky above the city is breaking pink and gold. The sea is dark blue turning lighter at the horizon. Smeaton's Tower silhouetted against the dawn. Drake's Island a dark shape on the water. Almost no one here — the empty promenade, the bench, the vast quiet of early morning. Seagulls on the railing. The feeling of the world starting again.

VERSION NOTES:
- Ch4 (Albedo): Cool dawn — silver, pale pink, the light hasn't warmed yet
- Ch8 (Citrinitas): Golden dawn — the first warm light after the crisis. Hope returning. Saffron and gold breaking through grey.
- Ch11 (Rubedo): Summer dawn — warm, wide, the sky is full of colour. The world has turned.

No anime, no photorealistic.
```

---

## bg_plymouth_hoe_day
**Used:** Ch6, 7, 8, 9, 11, 12, slideshows (the most-used Hoe variant)
**Phase:** Varies — generate Albedo (winter) and Rubedo (summer) versions

```
WINTER VERSION (Ch6-8):
Painterly illustration, soft oil painting style, 1920x1080 landscape. Plymouth Hoe on a winter day — cold but clear. Smeaton's Tower sharp against pale blue sky. The sea grey-blue, white-capped. A few walkers on the promenade in coats. The bench visible. The beauty of a cold place on a cold day — bracing, not inviting. Colour palette: Albedo — silver, grey-blue sea, pale sky, granite. No anime, no photorealistic.

SUMMER VERSION (Ch9-12):
Painterly illustration, soft oil painting style, 1920x1080 landscape. Plymouth Hoe in late spring/early summer — warm, bright, alive. Smeaton's Tower in sunshine. The sea is actual blue now. People on the grass, an ice cream van (distant). The wind is warm. The same view as the grey version but transformed by season. The bench is still there. Colour palette: Rubedo — sea green, warm stone, gold-hour light, sky blue. No anime, no photorealistic.
```

---

## THE BENCH — Special Treatment

The bench is a **visual motif** (see art_direction.md §11). It must look the same in every appearance — weathered wood, facing the sea, slightly worn. The world around it changes; it doesn't.

Consider generating the bench as a focal element in each Hoe variant: same bench, same position, different light, different season. When both versions are side by side, the player should feel the passage of time and the passage of growth.

```
DETAIL PROMPT — The Bench:
A weathered wooden bench on Plymouth Hoe, facing the English Channel. Simple municipal design, painted slats faded by salt air and weather. It has been here a while. It is neither beautiful nor ugly — it is a place where people sit and look at the sea and think about their lives. In every version: the same bench, the same angle, the same view of Smeaton's Tower and Drake's Island beyond. What changes is the sky, the sea, the light, and who is sitting there.
```

---

## GENERATION ORDER

1. **bg_plymouth_hoe_grey** — THE defining outdoor image. Get this right first.
2. **bg_plymouth_hoe_day** (summer) — The contrast. Same place, different world.
3. **bg_plymouth_hoe_dawn** (Citrinitas) — The hope-returning version after Ch8.
4. **bg_plymouth_hoe_day** (winter) — The everyday version.
