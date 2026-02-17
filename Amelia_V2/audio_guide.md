# Audio Requirements Guide

> Complete list of every audio file the game needs, with exact filenames, folder locations, and descriptions. All files go in `game/audio/`. Format: `.ogg` (Vorbis) — Ren'Py's preferred format.

---

## Folder Structure

```
game/audio/
├── songs/              # 20 Dancing Salamanders / Geddon Bird songs (slideshow moments)
├── ambient/            # Per-scene mood music loops (play continuously under dialogue)
└── sfx/                # Short sound effects (one-shot)
```

---

## 1. Songs — `audio/songs/` (20 files)

These are already placed in the scripts via `slideshows.rpy`. You have 9 as .wav — convert to .ogg and source the remaining 11.

| # | Filename | Song Title | Chapter | Have .wav? |
|---|----------|-----------|---------|------------|
| 1 | `paper_planes.ogg` | Paper Planes | Ch1 | Check |
| 2 | `lighthouse_in_the_fog.ogg` | Lighthouse in the Fog | Ch2 | Check |
| 3 | `two_birds.ogg` | Two Birds | Ch3 | Check |
| 4 | `hawthorne.ogg` | Hawthorne | Ch4 | Check |
| 5 | `circles_in_the_sand.ogg` | Circles in the Sand | Ch4 | Check |
| 6 | `kindeling_kin.ogg` | Kindeling Kin | Ch5 | Check |
| 7 | `the_mist_laden_path.ogg` | The Mist-Laden Path | Ch5 | Check |
| 8 | `mirror_of_the_mind.ogg` | Mirror of the Mind | Ch6 | Check |
| 9 | `oh_sarah.ogg` | Oh Sarah | Ch6 | Check |
| 10 | `bare_with_me.ogg` | Bare With Me | Ch7 | Check |
| 11 | `living_on_the_moon.ogg` | Living on the Moon | Ch7 | Check |
| 12 | `forgetmeknot.ogg` | Forgetmeknot | Ch8 | Check |
| 13 | `jolly_rum_ba_low.ogg` | Jolly Rum Ba Low | Ch8 | Check |
| 14 | `the_long_way_home.ogg` | The Long Way Home | Ch9 | Check |
| 15 | `amelia.ogg` | Amelia | Ch9 | Check |
| 16 | `here_now_and_blues.ogg` | Here Now and Blues | Ch10 | Check |
| 17 | `between_the_veil.ogg` | Between the Veil | Ch11 | Check |
| 18 | `the_work.ogg` | The Work | Ch11 | Check |
| 19 | `the_quiet_of_morning.ogg` | The Quiet of Morning | Ch11 | Check |
| 20 | `daffodils_in_the_snow.ogg` | Daffodils in the Snow | Ch12 (all 7 endings) | Check |

### Converting .wav → .ogg

Use FFmpeg (free, command line):
```
ffmpeg -i input.wav -c:a libvorbis -q:a 6 output.ogg
```
Quality 6 is good for music. Batch convert all at once:
```powershell
Get-ChildItem *.wav | ForEach-Object { ffmpeg -i $_.FullName -c:a libvorbis -q:a 6 ($_.BaseName + ".ogg") }
```

---

## 2. Ambient Music — `audio/ambient/` (51 files)

These are background mood tracks that play under dialogue. They should be **loopable** (seamless start/end) and **2–5 minutes long**. Soft, atmospheric — not distracting from dialogue.

All filenames below are already referenced (commented out) in the chapter scripts. When you create/source these tracks, uncomment the corresponding `play music` line in each chapter.

### Chapter 1 — London / Nigredo (warm, melancholic, departure)
| Filename | Scene | Mood Description |
|----------|-------|-----------------|
| `ch1_park.ogg` | Park bench with Ella | Warm afternoon, gentle guitar or piano, bittersweet |
| `ch1_home.ogg` | Packing, family scenes | Domestic warmth, soft strings, hint of sadness |
| `ch1_bookshop.ogg` | Bookshop visit | Cosy, dusty, acoustic, slightly mysterious |
| `ch1_thames.ogg` | Thames night farewell | Night river ambience, lonely piano, poignant |

### Chapter 2 — Arrival / Albedo (new, uncertain, hopeful)
| Filename | Scene | Mood Description |
|----------|-------|-----------------|
| `ch2_morning.ogg` | Departure morning | Early morning, quiet anticipation, acoustic |
| `ch2_drive.ogg` | Motorway journey | Movement, gentle electronic pulse, road feel |
| `ch2_kitchen.ogg` | Halls kitchen introductions | Lively, warm, social buzz, light percussion |
| `ch2_su_night.ogg` | Student Union night | Bar atmosphere, upbeat but not overpowering |
| `ch2_lecture.ogg` | First lectures | Academic, contemplative, soft ambient |
| `ch2_party.ogg` | Freshers' party | Party energy, bass, social chaos |

### Chapter 3 — First Semester / Albedo (isolation building)
| Filename | Scene | Mood Description |
|----------|-------|-----------------|
| `ch3_rain.ogg` | Rainy campus, Tasha encounter | Rain, tension, uncomfortable strings |
| `ch3_tension.ogg` | Group dynamics, Tasha escalation | Unsettled, minor key, building pressure |
| `ch3_hoe.ogg` | Plymouth Hoe, meeting Sarah | Coastal wind, open, tentatively hopeful |

### Chapter 4 — Mentors / Albedo (learning, exploration)
| Filename | Scene | Mood Description |
|----------|-------|-----------------|
| `ch4_hawthorne.ogg` | Hawthorne's office | Old study, ticking clock, scholarly warmth |
| `ch4_simmons.ogg` | Simmons's office | Calm, therapeutic, gentle piano |
| `ch4_maya.ogg` | Maya's room | Earthy, incense, low percussion, spiritual |
| `ch4_elena.ogg` | Elena introduction | Mysterious, slightly unsettling, Slavic folk hints |
| `ch4_cornwall_hawk.ogg` | Cornwall with Hawthorne | Coastal intellectual, literary strings |
| `ch4_cornwall_sim.ogg` | Cornwall with Simmons | Coastal reflective, gentle brass |
| `ch4_cornwall_maya.ogg` | Cornwall with Maya | Earth and stone, ritual drums |
| `ch4_cornwall_elena.ogg` | Cornwall with Elena | Ancient and mystical, drone, pipes |

### Chapter 5 — Settling In / Albedo (rhythm, friendship)
| Filename | Scene | Mood Description |
|----------|-------|-----------------|
| `ch5_rhythm.ogg` | Daily campus life | Upbeat, rhythmic, settled feeling |
| `ch5_protest.ogg` | Michael/protest scene | Energy, conviction, march drums |
| `ch5_kitchen_evening.ogg` | Kitchen community evening | Warm communal, cooking sounds, laughter undertone |
| `ch5_cornwall.ogg` | Group Cornwall trip | Adventure, open landscape, ensemble |
| `ch5_close.ogg` | Chapter close, deepening bonds | Gentle, reflective, satisfied |

### Chapter 6 — Descent / Citrinitas cusp (tension, concern, winter)
| Filename | Scene | Mood Description |
|----------|-------|-----------------|
| `ch6_tension.ogg` | Tasha escalation | Tight, anxious strings, building dread |
| `ch6_sarah.ogg` | Sarah withdrawal scenes | Hollow, sparse, echoing piano, distance |
| `ch6_3am.ogg` | Late night worry | 3am silence, clock ticking, isolated |
| `ch6_exams.ogg` | Exam stress | Pressure, metronome-like pulse, concentration |
| `ch6_christmas.ogg` | Christmas at home | Forced cheerfulness, domestic but strained |
| `ch6_midwinter.ogg` | Midwinter occult scene | Dark ritual, low drone, candle flicker, archaic |

### Chapter 7 — The Gathering Storm / Citrinitas (darkness deepening)
| Filename | Scene | Mood Description |
|----------|-------|-----------------|
| `ch7_mentor.ogg` | Mentor deepening (all 4 paths) | Intense learning, gravitas, threshold |
| `ch7_sarah.ogg` | Sarah's deterioration | Heartbreak, descending notes, cold |
| `ch7_shadow.ogg` | Shadow integration themes | Jungian darkness, cello, depth |
| `ch7_ethics.ogg` | Research dilemma scenes | Moral weight, conflicted, ambiguous |
| `ch7_occult.ogg` | Occult knowledge scenes | Esoteric, layered harmonics, ancient |
| `ch7_storm.ogg` | Chapter climax, approaching crisis | Rolling tension, storm building, dramatic |

### Chapter 8 — The Ordeal / Citrinitas (crisis, action)
| Filename | Scene | Mood Description |
|----------|-------|-----------------|
| `ch8_crisis.ogg` | Academic collapse | Overwhelming, cascading, dissonant |
| `ch8_sarah_crisis.ogg` | Sarah's crisis point | Emergency, heartbeat, urgency, fear |
| `ch8_ashes.ogg` | Aftermath | Devastation, silence, sparse single notes |

### Chapter 9 — Recovery / Rubedo begins (spring, rebuilding)
| Filename | Scene | Mood Description |
|----------|-------|-----------------|
| `ch9_spring.ogg` | Spring term, recovery | Fresh growth, birdsong, gentle warmth returning |

### Chapter 10 — The Road Back / Rubedo (homecoming)
| Filename | Scene | Mood Description |
|----------|-------|-----------------|
| `ch10_homecoming.ogg` | London return, changed perspective | Nostalgic but mature, piano + strings |

### Chapter 11 — Resurrection / Rubedo (culmination)
| Filename | Scene | Mood Description |
|----------|-------|-----------------|
| `ch11_resurrection.ogg` | Final term, integration | Gathering strength, full ensemble, ascending |

### Chapter 12 — Endings / Rubedo (resolution)
| Filename | Scene | Mood Description |
|----------|-------|-----------------|
| `ch12_last_morning.ogg` | Shared opening, last Plymouth morning | Dawn, quiet fullness, bittersweetness |
| `ending_grief.ogg` | Grief ending | Mourning, solo instrument, weight |
| `ending_alchemist.ogg` | Alchemist ending | Mystical completion, layered, gold |
| `ending_scholar.ogg` | Scholar ending | Intellectual warmth, purposeful |
| `ending_companion.ogg` | Companion ending | Community, warmth, ensemble |
| `ending_healer.ogg` | Healer ending | Compassion, gentle strings, care |
| `ending_whole.ogg` | Whole/integrated ending | Full harmony, all themes resolved |
| `ending_bittersweet.ogg` | Bittersweet ending | Mixed, beautiful but incomplete |

---

## 3. Sound Effects — `audio/sfx/` (15 files)

Short one-shot sounds. Most are only used once or twice. Keep them under 5 seconds.

| Filename | Description | Where Used |
|----------|-------------|-----------|
| `sfx_phone_ring.ogg` | Mobile phone ringing | Ch1 (Ella calls) |
| `sfx_phone_buzz.ogg` | Phone vibration / text notification | Throughout (text scenes) |
| `sfx_knock.ogg` | Door knock | Ch2 (halls), Ch8 (Sarah's door) |
| `sfx_door_open.ogg` | Door opening | Various |
| `sfx_rain_start.ogg` | Rain beginning on window | Ch3, Ch6 (rainy scenes) |
| `sfx_seagulls.ogg` | Plymouth seagulls, coastal | Hoe scenes, campus outdoor |
| `sfx_wind_moor.ogg` | Wind on moorland | Cornwall, Bodmin |
| `sfx_ocean_waves.ogg` | Ocean waves, rhythmic | Hoe, Cornwall coast |
| `sfx_fire_crackle.ogg` | Fireplace / candle crackle | Elena's cottage, Maya's room |
| `sfx_kettle.ogg` | Kettle boiling | Kitchen scenes |
| `sfx_book_open.ogg` | Book pages turning/opening | Bookshop, library |
| `sfx_footsteps_corridor.ogg` | Footsteps in corridor | Hospital, halls, campus |
| `sfx_crowd_murmur.ogg` | Background crowd / lecture hall | SU, lectures, parties |
| `sfx_train_departing.ogg` | Train pulling away from station | Ch1 (leaving London) |
| `sfx_stone_echo.ogg` | Echo in stone chamber | Fogou scenes |

---

## 4. Generating Ambient Music

Since you can easily generate these, here are tips for each alchemical phase:

### Nigredo (Ch1–3) — Warm Darkness
- **Key**: Minor keys, A minor, D minor
- **Instruments**: Acoustic guitar, piano, cello, soft brushed drums
- **Tempo**: 60–80 BPM
- **Mood words for generators**: melancholic, warm, intimate, autumn evening, farewell, London rain

### Albedo (Ch4–7) — Cool Light / Intellectual
- **Key**: C major/A minor shifts, modal (Dorian/Mixolydian for Celtic scenes)
- **Instruments**: Piano, strings, flute, light percussion, acoustic bass
- **Tempo**: 70–90 BPM
- **Mood words**: coastal grey, academic, discovery, sea mist, Cornwall stone circles

### Citrinitas (Ch8–9) — Crisis Gold
- **Key**: Diminished, shifted tonalities, resolving to major at end of Ch9
- **Instruments**: Cello, dissonant piano, processed sounds, silence as instrument
- **Tempo**: Variable — 50 BPM for aftermath, 120+ for crisis
- **Mood words**: emergency, hospital, shattering, then slowly... spring, recovery, new growth

### Rubedo (Ch10–12) — Integration Red
- **Key**: D major, G major, full harmonic resolution
- **Instruments**: Full ensemble — everything from earlier phases combined
- **Tempo**: 80–100 BPM
- **Mood words**: homecoming, maturity, gratitude, bittersweet, completion, dawn

### General Guidelines
- **Length**: 2–4 minutes, loopable (fade end matches fade start)
- **Volume**: These play UNDER dialogue. Keep them quiet and atmospheric. The songs in slideshows are the featured music.
- **Format**: Export as .ogg (Vorbis), 44.1kHz, ~128kbps is fine for ambient

---

## 5. Quick Reference — What's Already Coded

The chapter scripts already have commented-out `play music` lines ready to uncomment. Example from chapter_1.rpy:
```renpy
## Currently commented out:
# play music "audio/ambient/ch1_park.ogg" fadein 2.0
```

When you place the .ogg file at the right path, just remove the `#` to activate it. The fadeins/fadeouts and `stop music` calls are already written throughout all chapters.

The two `play sound` lines are also ready:
```renpy
# play sound "audio/sfx/sfx_phone_ring.ogg"    # chapter_1.rpy L104
# play sound "audio/sfx/sfx_knock.ogg"          # chapter_2.rpy L325
```

Additional `play sound` calls for the other SFX in section 3 can be added when you spot good moments during the writing passes.

---

*All paths are relative to `game/`. Ren'Py looks for audio files starting from the `game/` directory.*
