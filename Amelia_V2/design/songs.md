# Songs & Musical Slideshows — The CK: Amelia

> Design document for song integration. Each slideshow is a cinematic interlude:
> no dialogue, background images cycling with dissolve transitions while a full song plays.
> The player watches and listens. Images may repeat — this is intentional.

---

## Audio File Convention

All song files should be placed in `game/audio/songs/` as `.ogg` files.
Filename convention: `snake_case_song_title.ogg`

Example: `audio/songs/paper_planes.ogg`

---

## Song Selection Summary

### Primary Songs (20 placements across 12 chapters)

| #  | Song                     | Album / Label     | Chapter | Moment                        |
|----|--------------------------|-------------------|---------|-------------------------------|
| 1  | Paper Planes             | Geddon Bird       | 1       | After Thames at Night         |
| 2  | Lighthouse in the Fog    | Geddon Bird       | 2       | The Drive to Plymouth         |
| 3  | Two Birds                | Geddon Bird       | 3       | After the Panic Attack        |
| 4  | Hawthorne                | Geddon Bird       | 4       | Cornwall Trip                 |
| 5  | Circles in the Sand      | Geddon Bird       | 5       | Group Cornwall Trip           |
| 6  | Kindeling Kin            | Geddon Bird       | 6       | Christmas at Home             |
| 7  | The Mist-Laden Path      | Three Drops       | 6       | Midwinter Solstice (cond.)    |
| 8  | Mirror of the Mind       | Geddon Bird       | 7       | The Gathering Storm           |
| 9  | Oh Sarah                 | Gills and Guts    | 8       | Before the Crisis (Porthcurno)|
| 10 | Bare With Me             | Geddon Bird       | 8       | In the Ashes (all paths)      |
| 11 | Forgetmeknot             | Dancing Salamanders | 8     | After tragic path (cond.)     |
| 12 | Living on the Moon       | Geddon Bird       | 8       | The Bottom                    |
| 13 | jolly-rum-ba-low!        | Geddon Bird       | 9       | Cornwall Healing Trip         |
| 14 | The Long Way Home        | Geddon Bird       | 10      | Train Home for Easter         |
| 15 | Here, Now, and Blues     | Geddon Bird       | 10      | Solo London Contemplation     |
| 16 | Between the Veil         | Geddon Bird       | 11      | Fogou / Mystical Climax       |
| 17 | The_Work                 | Geddon Bird       | 11      | Red Dawn (Rubedo)             |
| 18 | The Quiet of Morning     | Geddon Bird       | 12      | Last Goodbye                  |
| 19 | Daffodils in the Snow    | Tides in Memory's Arbor V2 | 12 | Before Ending Title Card |
| 20 | Amelia                   | Dancing Salamanders | 12    | Credits Theme                 |

> **Key additions from broader collection research:**
> - **Oh Sarah** (Gills and Guts album, set at Porthcurno Beach) — literally about reaching out to a friend named Sarah in crisis. "Oh Sarah, when you feel alone / Know you've got a place, a heart, a home." Must-have for Ch8.
> - **Forgetmeknot** (Dancing Salamanders) — explicitly about a friend dying during first year of university. "In the twilight of our first-year dreams / Desperation's whisper stole you away." Plays only on the tragic path (sarah_alive == False).
> - **Amelia** (Dancing Salamanders) — the protagonist's theme song. Mentions the Plym, the moors, the Hero's Journey arc. "Amelia, oh Amelia / In the heart of the storm, you'll find your way." Perfect credits theme.

### Reserve Songs (optional character-specific placements)

| Song                  | Album       | Potential Use                              |
|-----------------------|-------------|--------------------------------------------|
| Echoes in the Garden  | Geddon Bird | Maya mentor path variant (Ch4 or Ch7)      |
| Familiar Strangers    | Geddon Bird | Tasha resolution scene (Ch11)              |
| Mindful Meddling      | Geddon Bird | Academic rhythm montage (Ch5)              |
| The Weight of Words   | Geddon Bird | Lucas vulnerability scene (Ch6 or Ch7)     |
| Good Grief            | Dancing Salamanders | Processing grief (Ch9 alt)           |
| Her Name Unspoken     | A Spiral Path | Silence around the dead (Ch9 alt)        |
| The Train Back Home   | Gills and Guts | Train journey (Ch10 or Ch12 alt)        |
| Am I Me               | Gills and Guts | Identity crisis at Golitha Falls (Ch5/6) |
| See the Sea           | Gills and Guts | Mental health, Fistral Beach (Ch7 alt)   |
| Dartmoor              | Gills and Guts | Bodmin Moor identity/freedom (Ch4/5)     |
| The Bells of Lyonesse | Dancing Salamanders | Cornish folklore, Raj+Amelia (Ch4)   |
| Underneath the Hollow Hill | Three Drops | Celtic Otherworld, Fogou (Ch11 alt)  |
| Emergent              | Dancing Salamanders | Coming of age (Ch1 alt or credits)   |
| Sophia                | Dancing Salamanders | Seeker of light (Ch4 mentor alt)     |
| Butterfly Kisses on the Wind | Elara | Spirit of departed (Ch9 alt)           |
| The Anchor of Memories | Risca      | Standing in dead person's room (Ch9 alt) |

---

## Detailed Placement Guide

### Chapter 1 — The Ordinary World

**Song: "Paper Planes"**
- **Insertion point:** After Scene 1.6 (Thames at Night), before Scene 1.7 (Night Before Leaving)
- **Narrative context:** Amelia has walked the South Bank one last time. Nostalgia, finality, the city she's leaving. The song is about Amelia and Ella burning old letters — letting go of the past.
- **Slideshow images:** Thames at night, park bench at sunset, Mr. Osei's bookshop, Amelia's London bedroom, London bedroom (dark)
- **Mood:** Bittersweet, autumnal, farewell
- **Duration target:** ~3:00

### Chapter 2 — Call to Adventure

**Song: "Lighthouse in the Fog"**
- **Insertion point:** During Scene 2.2 (The Drive, M25→M5), replacing the narrated road-trip passage
- **Narrative context:** The motorway journey from London to Plymouth. England unspooling — Stonehenge in the distance, landscape shifting from suburban to wild, the sea appearing. The song captures Plymouth's fog, the Barbican, the Hoe, Drake Island — the city Amelia is heading towards.
- **Slideshow images:** Motorway daytime, Plymouth first sight, campus daytime, halls corridor, Plymouth Hoe (grey)
- **Mood:** Anticipatory, searching, bluesy
- **Duration target:** ~3:30

### Chapter 3 — Refusal of the Call

**Song: "Two Birds"**
- **Insertion point:** After Scene 3.7 (Panic Attack in the Library), before Scene 3.8 (Sarah on the Hoe)
- **Narrative context:** Amelia has just had her first breakdown. She's in her rainy Plymouth room, missing Ella, questioning everything. "Two Birds" is about Amelia and Ella — two paths diverging, distance and closeness, the ache of separation.
- **Slideshow images:** Plymouth room (rain), library at night, Plymouth Hoe (grey), halls kitchen at night, Plymouth room (rain)
- **Mood:** Melancholic, aching, grey
- **Duration target:** ~3:00

### Chapter 4 — Meeting the Mentor

**Song: "Hawthorne"**
- **Insertion point:** During Scene 4.2 (Cornwall Trip), after the mentor's teaching crystallises
- **Narrative context:** Amelia has just experienced her first encounter with the Cornish landscape — Bodmin Moor, Eden Project, Tintagel, or Madron Well depending on path. "Hawthorne" captures walking among ruins, thorns and growth, the scars that become wisdom. Works universally across all four mentor paths.
- **Slideshow images:** Bodmin Moor, Tintagel, Madron Well, Men-an-Tol, Merry Maidens, Eden Project
- **Mood:** Ancient, wise, weathered beauty
- **Duration target:** ~3:30

### Chapter 5 — Crossing the Threshold

**Song: "Circles in the Sand"**
- **Insertion point:** During Scene 5.6 (Group Cornwall Trip)
- **Narrative context:** The friend group exploring the Cornish coast together. Beach, rocks, laughter, wind. "Circles in the Sand" is about intergenerational patterns, identity on the shore — Raj's cultural threads woven through landscape.
- **Slideshow images:** Cornwall coast, campus quad, library study area, Cornwall coast, halls corridor
- **Mood:** Warm, expansive, identity-seeking
- **Duration target:** ~3:00

### Chapter 6 — Tests, Allies, Enemies

**Song: "Kindeling Kin"** (primary)
- **Insertion point:** During Scene 6.5 (Christmas at Home)
- **Narrative context:** Amelia returns to London for Christmas. The family home, Grace cooking, fairy lights, the familiar-made-strange. "Kindeling Kin" is about childhood memory, a mother's hidden burden, the garden, a lullaby — Grace's quiet strength.
- **Slideshow images:** Family home, London café, halls corridor, family home, London café
- **Mood:** Nostalgic, tender, domestic warmth
- **Duration target:** ~3:00

**Song: "The Mist-Laden Path"** (conditional — requires OK ≥ 5)
- **Insertion point:** During Scene 6.7 (Midwinter Solstice), if the occult thread is active
- **Narrative context:** Candles in the Cornish woods on the longest night. A ritual viewed or joined. Dawn breaking. "The Mist-Laden Path" is bilingual Welsh/English, Celtic mythology — the Seeker's first step on the path to Ceridwen's wisdom.
- **Slideshow images:** Cornwall at night, Cornwall coast, Madron Well, Cornwall at night, Cornwall coast
- **Mood:** Haunting, mystical, liminal
- **Duration target:** ~3:30

### Chapter 7 — The Approach

**Song: "Mirror of the Mind"**
- **Insertion point:** During Scene 7.7 (The Gathering Storm)
- **Narrative context:** Late February. Amelia stands on the Hoe as storm clouds build — literal and metaphorical. She's been confronting her shadow (snapping at Liz, the ethics dilemma). "Mirror of the Mind" is Maya-guided shadow work, Jungian mirrors, the deep reflection before crisis.
- **Slideshow images:** Plymouth Hoe (day), library study area, psych building corridor, Plymouth Hoe (day), lecture theatre
- **Mood:** Brooding, introspective, tension building
- **Duration target:** ~3:00

### Chapter 8 — The Ordeal

**Song: "Oh Sarah"** (opening — before the crisis)
- **Insertion point:** At the start of Scene 8.3 (The Sarah Score section), after Tasha's attack plays out but before the crisis moment
- **Narrative context:** Set at Porthcurno Beach. A friend sitting beside someone in crisis, unable to fix anything but refusing to leave. "Oh Sarah, when you feel alone / Know you've got a place, a heart, a home." The most literal, character-named song in the entire collection. This is the emotional prelude to the crisis.
- **Slideshow images:** Porthcurno Beach at dawn, two figures on the sand, waves crashing against cliffs, a hand reaching across a table, empty chair at a group table, night sky over the sea, morning light on breakwater, two cups of tea (one untouched)
- **Mood:** Raw, loving, helpless, anchored
- **Duration target:** ~3:30

**Song: "Bare With Me"** (all paths — In the Ashes)
- **Insertion point:** After Act 2 ends / the `scene black` transition, before the Aftermath scenes
- **Narrative context:** The emotional centre of the entire game. Sarah's crisis has just occurred. Everything is raw. "Bare With Me" is about grief, isolation, friends trying to help while being pushed away. The direct emotional truth of this moment.
- **Slideshow images:** Black, halls corridor, counsellor office, hospital corridor, Plymouth Hoe (dawn), black
- **Mood:** Devastating, raw, grief
- **Duration target:** ~3:30

**Song: "Forgetmeknot"** (conditional — tragic path only)
- **Insertion point:** After the tragic path is confirmed (sarah_alive == False), during or after the grief scenes
- **Narrative context:** "In the twilight of our first-year dreams / Two hearts entwined like whispered streams / Desperation's whisper stole you away." Explicitly about a friend dying during first year of university. The forget-me-not flower as promise. Plays ONLY if Sarah has died.
- **Slideshow images:** Forget-me-not flowers, empty dorm room, notebook with pressed flowers, friends holding each other in the corridor, Plymouth Hoe at dusk, a candle in a window, starlit campus, a single flower on a windowsill
- **Mood:** Devastating, memorial, promise to remember
- **Duration target:** ~3:00
- **Condition:** `sarah_alive == False`

**Song: "Living on the Moon"** (all paths — The Bottom)
- **Insertion point:** At Scene 8.7 (The Bottom), Amelia alone in her room
- **Narrative context:** Night, rain, the fire has burned. Amelia in bed, the year at its darkest point. "Living on the Moon" is about isolation as escape, someone reaching out, healing not running — Zara's quiet offer of connection.
- **Slideshow images:** Plymouth room (night), Plymouth Hoe (grey), library night, Plymouth room (night), halls corridor
- **Mood:** Isolated, fragile, the smallest ember
- **Duration target:** ~3:00

### Chapter 9 — The Reward

**Song: "jolly-rum-ba-low!"**
- **Insertion point:** During Scene 9.6 (Cornwall Healing Trip)
- **Narrative context:** March/April. The light is returning. Amelia revisits the Cornish landscape with her friends or mentor — the same rocks, but she's different. "jolly-rum-ba-low!" is Hal-an-Tow, Cornish May Day, the Green Man, spring celebration — life returning with force and joy.
- **Slideshow images:** Cornwall coast, Plymouth Hoe (day), Eden Project, Tintagel, Cornwall coast, campus quad
- **Mood:** Energetic, celebratory, spring, alive
- **Duration target:** ~3:00

### Chapter 10 — The Road Back

**Song: "The Long Way Home"** (primary)
- **Insertion point:** During Scene 10.1 (Train Home for Easter)
- **Narrative context:** The reverse journey — Plymouth to London by train. Fields, churches, the density of London approaching. "The Long Way Home" is about walking London at night, Dad's call, the question of what home means now.
- **Slideshow images:** London train, Plymouth Hoe (day), Cornwall coast, London train, family home
- **Mood:** Reflective, between-worlds, homeward
- **Duration target:** ~3:30

**Song: "Here, Now, and Blues"** (secondary)
- **Insertion point:** During Scene 10.5/10.4 (Solo London Contemplation)
- **Narrative context:** Amelia walks familiar London streets that feel different. Cherry blossom, April light. "Here, Now, and Blues" is about mindfulness, being present in the struggle, parenthood — David's unspoken love.
- **Slideshow images:** London park, Thames, bookshop, London park, family home
- **Mood:** Present, grounded, tender
- **Duration target:** ~3:00

### Chapter 11 — Resurrection

**Song: "Between the Veil"** (primary — mystical climax)
- **Insertion point:** During Scene 11.5 (Final Cornwall Trip / Fogou climax)
- **Narrative context:** The game's climactic mystical moment. For Elena-path players, this is the Fogou — crawling into an Iron Age underground chamber. For all paths, this is the transformative Cornwall encounter. "Between the Veil" features a fox spirit guide, dreamlike grief-and-release, a village memorial. Perfect for the liminal, between-worlds quality of this scene.
- **Slideshow images:** Fogou entrance, Cornwall coast, Madron Well, Men-an-Tol, Merry Maidens, Cornwall coast
- **Mood:** Otherworldly, sacred, transformative
- **Duration target:** ~3:30

**Song: "The_Work"** (secondary — Red Dawn / Rubedo)
- **Insertion point:** During Scene 11.8 (Red Dawn on the Hoe)
- **Narrative context:** THE visual and thematic climax of the entire game. Sunrise over Plymouth Sound. The sky turns red and gold — Rubedo, the alchemical gold. Drake's memorial silhouetted. "The_Work" is about Cornish cliffs, an unnamed guide, the alchemical journey, "learning to fall." The culmination of everything.
- **Slideshow images:** Plymouth Hoe (dawn), Cornwall coast, Plymouth Hoe (day), campus quad, Plymouth Hoe (dawn)
- **Mood:** Transcendent, golden, earned
- **Duration target:** ~3:30

### Chapter 12 — Return with the Elixir

**Song: "The Quiet of Morning"** (primary — farewell)
- **Insertion point:** During Scene 12.2 (Last Goodbye)
- **Narrative context:** The flat emptying. Boxes, bare walls, corridor hugs, the kitchen one last time. "The Quiet of Morning" is about Ella and a boat trip at dawn on Plymouth Sound — quiet, friendship, the sacredness of early morning. The gentlest farewell.
- **Slideshow images:** Plymouth room (day), flat kitchen, halls corridor, campus quad, Plymouth Hoe (day), Plymouth room (day)
- **Mood:** Gentle, quiet, grateful
- **Duration target:** ~3:00

**Song: "Daffodils in the Snow"** (closing — before ending title card)
- **Insertion point:** After the ending-specific narrative, before the `centered` title card
- **Narrative context:** The game's final musical statement. Whatever ending the player reached, this song is the emotional close. "Daffodils in the Snow" is about hope emerging from grief, spring from nigredo — daffodils pushing through snow. All four alchemical stages referenced. A broader, non-character-specific piece that unifies every ending.
- **Slideshow images:** Ending-specific (varies by ending — see implementation)
- **Mood:** Hopeful, earned, universal
- **Duration target:** ~3:30

**Song: "Amelia"** (credits theme)
- **Insertion point:** During the credits scroll after all endings
- **Narrative context:** The protagonist's anthem. "Born by the sea, where ideas set free / Off the moor, into the Plym she sails." Traces the entire Hero's Journey in one song — childhood, the call, the storm, scars as testament, the emerald sun. The player has just finished the story; this song is the final emotional statement.
- **Slideshow images:** Credit-roll images cycling through all 12 chapters — the park bench, the drive, campus, Cornwall, mentors, the ordeal, the Hoe at dawn, the train home
- **Mood:** Triumphant, emotional, complete
- **Duration target:** ~3:00

---

## Implementation Notes

### Ren'Py Slideshow Pattern

Each slideshow is implemented as a named label in `game/slideshows.rpy`.
Chapters call the slideshow with `call slideshow_chX_song_name`.

```renpy
label slideshow_ch1_paper_planes:
    # SLIDESHOW: "Paper Planes" — Amelia's last London night
    stop music fadeout 1.0
    play music "audio/songs/paper_planes.ogg" noloop
    scene bg_thames_night with dissolve
    pause 12.0
    scene bg_park_bench_sunset with dissolve
    pause 12.0
    # ... images cycle for ~3 minutes
    stop music fadeout 2.0
    return
```

### Timing

- Images change every 12 seconds with dissolve transitions
- Each slideshow has ~15 transitions (~3 minutes total)
- Songs play `noloop` — they end naturally
- If images finish before the song, the last image holds
- If the song finishes before images, the remaining images cycle in silence
- Both cases are acceptable per design intent

### Audio Files Required

Place the following `.ogg` files in `game/audio/songs/`:

```
paper_planes.ogg
lighthouse_in_the_fog.ogg
two_birds.ogg
hawthorne.ogg
circles_in_the_sand.ogg
kindeling_kin.ogg
the_mist_laden_path.ogg
mirror_of_the_mind.ogg
oh_sarah.ogg
bare_with_me.ogg
forgetmeknot.ogg
living_on_the_moon.ogg
jolly_rum_ba_low.ogg
the_long_way_home.ogg
here_now_and_blues.ogg
between_the_veil.ogg
the_work.ogg
the_quiet_of_morning.ogg
daffodils_in_the_snow.ogg
amelia.ogg
```

### Image Requirements

Slideshows reuse existing chapter backgrounds (47 unique backgrounds across the game).
No new images are required — the slideshows cycle through backgrounds already referenced in their respective chapters.

---

## Song-to-Character Mapping

| Song | Primary Character | Secondary |
|------|-------------------|-----------|
| Paper Planes | Amelia, Ella | — |
| Lighthouse in the Fog | Amelia (solo) | Plymouth itself |
| Two Birds | Amelia, Ella | — |
| Hawthorne | Hawthorne | All mentors |
| Circles in the Sand | Raj | Friend group |
| Kindeling Kin | Grace | Family |
| The Mist-Laden Path | Elena / Occult thread | Cornwall |
| Mirror of the Mind | Maya | Amelia's shadow |
| Oh Sarah | Amelia, Sarah | Friend group |
| Bare With Me | Amelia | Ella, Lucas, Maya |
| Forgetmeknot | Amelia, Sarah | — |
| Living on the Moon | Zara, Sarah | Amelia |
| jolly-rum-ba-low! | Cornwall (ensemble) | Spring itself |
| The Long Way Home | David | Family, London |
| Here, Now, and Blues | David | Parenthood |
| Between the Veil | Fox spirit / Spiritual | Amelia |
| The_Work | Elena / Guide figure | Alchemy |
| The Quiet of Morning | Ella | Friendship |
| Daffodils in the Snow | Universal | Hope / All endings |
| Amelia | Amelia (solo) | The full journey |

---

## Thematic Arc Through Songs

The 17 songs trace the alchemical journey:

1. **Nigredo (Ch1-3):** Loss, departure, darkness — Paper Planes, Lighthouse in the Fog, Two Birds
2. **Albedo (Ch4-6):** Discovery, reflection, mentorship — Hawthorne, Circles in the Sand, Kindeling Kin
3. **Citrinitas (Ch7-9):** Shadow work, crisis, first light — Mirror of the Mind, Oh Sarah, Bare With Me, Forgetmeknot, Living on the Moon, jolly-rum-ba-low!
4. **Rubedo (Ch10-12):** Integration, transformation, gold — The Long Way Home, Here Now and Blues, Between the Veil, The_Work, The Quiet of Morning, Daffodils in the Snow, Amelia
