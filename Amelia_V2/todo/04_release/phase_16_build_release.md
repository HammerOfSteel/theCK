# Phase 16 — Build, Package & Release

> *Goal: Ship. Produce distributable builds and everything a storefront needs.*
> Runs after Phase 15 sign-off.

---

## 16.1 Build configuration
- [ ] **`options.rpy` final** — Name, version, build name, `build.classify`/`archive` rules, icon
- [ ] **Exclude dev files** — Keep `.rpy` source, backups, `text_files/`, prompt packs, and `todo/` out of
      distributed builds (build classify rules)
- [ ] **Compile check** — Fresh `.rpyc` compile; `lint` clean; no debug flags left on
- [ ] **Build-size review** — Convert remaining WAV → OGG; verify audio/art compression; check final size

## 16.2 Platform builds
- [ ] **Windows** build + launch test
- [ ] **macOS** build + launch test (codesign/notarize if distributing outside a store)
- [ ] **Linux** build + launch test
- [ ] **(Optional) Web** build test if targeting browser
- [ ] **Cross-platform save parity** — Saves behave consistently across platforms

## 16.3 Store / distribution prep
- [ ] **Store page copy** — Description, tags, content warnings, screenshots, trailer
- [ ] **Capsule/marketing art** — Key art, thumbnails (can reuse Phase 14 CGs)
- [ ] **Credits screen final** — Writing, art, music/songs, voices, tools, third-party licences
- [ ] **Legal** — All asset licences/attributions cleared (art, audio, fonts, TTS voices, Studio-generated outputs)
- [ ] **Privacy/EULA** — If any, included and linked

## 16.4 Release
- [ ] **Release candidate tag** — Version-tag the repo; freeze content
- [ ] **Final RC playthrough** — One clean end-to-end run on the packaged build (not the editor)
- [ ] **Publish** — Upload to chosen platform(s) (itch.io / Steam / direct)
- [ ] **Backup** — Archive final source + assets + build artifacts

---

**Exit criteria:** Signed, lint-clean, correctly-sized builds for all target platforms launch from the
packaged artifact (not the editor), all licences cleared, and the release is published + archived.
