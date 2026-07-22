# Phase 05 — Engine & Technical ← CURRENT PHASE

> *Goal: Make the game fully runnable with placeholder assets. Complete all Ren'Py engine work
> so that when we focus on art, we only swap images — no code changes needed.*
> Prior work committed as `6898968` (placeholder system + sourcing guide + images dir).

---

## 5.1 Placeholder System ✅
- [x] **placeholders.rpy** — Displayable declarations for all 58 backgrounds (coloured solids
      with text labels, alchemical palette coded). Game runs without any image files.
- [x] **placeholder_guide.md** — Sourcing guide: recommended sites, search terms, naming
      conventions, folder structure for when real images replace placeholders.
- [x] **images/ directory** — Organised folder tree ready to receive final art.

## 5.2 Technical Implementation ✅
- [x] Project structure — `game/` with definitions.rpy and 12 chapters
- [x] Character definitions — 18 characters defined in definitions.rpy
- [x] Variable architecture — 6-stat karma, relationship vars, flags, conditions
- [x] **Screen customisation** — Journal, custom choice, content-warning, phone, quick menu,
      save/load, preferences, history, help, about, confirm, main menu, navigation
- [x] **GUI styling** — gui.rpy: textbox, fonts, alchemical phase colours
      (Nigredo/Albedo/Citrinitas/Rubedo), transitions, channel config
- [x] **Save system** — Standard save/load with slot grid, auto/quick save, stat tracking via `default` vars
- [x] **Layered image stubs** — layered_images.rpy: `layeredimage` blocks for all 18 characters
- [x] **Chapter tracking** — `current_chapter` var set at start of each chapter, drives GUI phase colours

## 5.3 Engine Hardening (NEW — do before art)
- [ ] **Full playthrough smoke test** — Reach all 7 endings with placeholders, log any crash/soft-lock
- [ ] **Variable audit** — Confirm every `default`/`define` is declared before first use; no undefined-var warnings
- [ ] **Rollback safety** — Verify rollback works across chapter boundaries and `call slideshow_` returns
- [ ] **Save compatibility policy** — Decide on `config.save_directory` + version tag so pre-release saves
      don't corrupt post-content-add saves. Document in repo memory.
- [ ] **Label/jump map** — Generate a script that lists every `label`, `jump`, `call`; flag orphans/dead ends
- [ ] **Lint clean** — `renpy.sh <project> lint` returns 0 warnings (or all warnings triaged/justified)
- [ ] **Persistent data** — Gallery/music-room unlock flags stored in `persistent.` namespace correctly
- [ ] **Config pass** — `options.rpy`: name, version, build name, icon, `config.has_autosave`, skip settings

## 5.4 Systems Screens (verify complete)
- [ ] **Gallery** — `gallery_screens.rpy` unlocks CG/backgrounds as seen; wire to persistent flags
- [ ] **Music room** — `music_player.rpy` plays unlocked songs; verify all 20 register
- [ ] **Codex / journal** — Confirm journal reflects live stats + relationship state per chapter

---

**Exit criteria:** Game is completable start-to-finish on placeholders, lints clean, saves are
forward-compatible, and no code change is required to later swap in art or audio — only asset files.
