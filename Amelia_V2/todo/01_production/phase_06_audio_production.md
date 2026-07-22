# Phase 06 — Audio Production (Music & SFX)

> *Goal: Every non-voice audio cue the game references exists as a `.ogg` in `game/audio/`.*
> Requirements are fully specified in `audio_guide.md` (exact filenames + mood descriptions).
> **Voice/narration is tracked separately** in `phase_07_voice_narration.md`.

---

## 6.1 Songs — `audio/songs/` (20 files)
- [ ] **Inventory pass** — Confirm which of the 20 songs currently exist as `.wav` (guide says 9)
- [ ] **Convert existing** — `.wav → .ogg` via FFmpeg (`-c:a libvorbis -q:a 6`); batch script in audio_guide.md
- [ ] **Source remaining ~11** — Produce/commission missing songs per `design/songs.md` placements
- [ ] **Loudness normalise** — Target ~-16 LUFS integrated for consistent playback vs. dialogue
- [ ] **In-engine check** — Each song triggers on its `call slideshow_` and stops cleanly

## 6.2 Ambient Music — `audio/ambient/` (51 files)
- [ ] **Generate/collect 51 loopable mood tracks** — 2–5 min, seamless loop, per audio_guide.md
- [ ] **Phase grouping** — Tag by alchemical phase (Nigredo/Albedo/Citrinitas/Rubedo) for tonal consistency
- [ ] **Loop-point QA** — No audible seam at wrap; fade/crossfade config in gui.rpy channels
- [ ] **Scene wiring** — Confirm each chapter scene references a real ambient filename (no missing-file console spam)

## 6.3 Sound Effects — `audio/sfx/` (15 files)
- [ ] **Generate/collect 15 SFX** — Exact filenames in audio_guide.md (phone buzz, door, sea, page turn, etc.)
- [ ] **One-shot QA** — Correct trigger points, no clipping, appropriate volume vs. music bed
- [ ] **Dice / karma cue** — Distinct SFX for the karma-dice mechanic moments

## 6.4 Mix & Delivery
- [ ] **Channel balance** — Set default volumes for music/ambient/sfx/voice channels in preferences
- [ ] **Mute/duck rules** — Ambient ducks under songs and (later) under voiced narration
- [ ] **License/attribution ledger** — Record source + licence for every third-party or model-generated track

---

**Exit criteria:** Zero "file not found" audio warnings on a full playthrough; song, ambient, and SFX
channels are balanced; attribution ledger complete.
