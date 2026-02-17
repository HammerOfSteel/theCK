# UI Elements — Image Prompts

> Visual components for the game's interface: main menu, textbox design reference, journal mockup, and phone screen frame. These must match the game's painterly style while being clean enough to function as UI.

---

## MAIN MENU BACKGROUND

The main menu is the first thing a player sees. It sets the tone.

```
Painterly illustration, soft oil painting style, 1920x1080 landscape. Plymouth Hoe at dusk — a slow, golden-hour view. The weathered wooden bench (Sarah's bench) visible in the middle distance. Smeaton's Tower behind it, the sea beyond, Drake's Island a dark shape on the water. The sky is purple-gold, the last light of the day. The left side of the image should be slightly darker/simpler — this is where the menu text will overlay:
  - New Story
  - Continue
  - Chapters
  - Journal
  - Settings
  - Content Warnings
The text will be gold (#FFD700), left-aligned. The image must accommodate this — no important detail on the left 30%. The mood is: a story is about to begin. Come sit on this bench and look at the sea. Contemporary British literary illustration. No anime, no photorealistic.
```

### Alternative Main Menu Concept
```
Painterly illustration, soft oil painting style, 1920x1080. Close-up of an open journal/notebook on a desk, surrounded by objects: a pen, a mug of tea, dried flowers, a postcard of Cornwall's coast. The journal pages are blank or have faint handwriting. Warm golden light from a desk lamp. The objects tell the story before the story begins. Menu text overlays the left page. The mood is: someone's life is waiting to be read. No anime, no photorealistic.
```

---

## TEXTBOX DESIGN REFERENCE

Not a full image prompt — a design specification for the textbox panel.

```
TEXTBOX DESIGN SPEC:
- Semi-transparent dark panel (#1A1A2E at 80% opacity)
- Soft rounded edges (10px radius)
- Height: approximately 200px, spanning full width with 40px margin each side
- Position: bottom-aligned
- Character name: Gold (#FFD700), 18pt, clean serif font (Georgia), positioned above the dark panel
- Dialogue text: Off-white (#F5F5F0) with subtle 1px drop shadow, 16pt, same serif font
- No hard outline — the panel should feel like it's SITTING on the image, not stamped
- The panel's transparency should let the scene show through slightly

PROMPT FOR REFERENCE IMAGE:
Painterly illustration showing a visual novel textbox mockup at the bottom of a scene. A semi-transparent dark panel with soft rounded corners spans the bottom of the frame. Above it, a character name "Amelia" in gold. Inside the panel, dialogue text in soft white: "The sea looks different when you know you'll have to leave it." The panel is elegant, minimal, not intrusive. A scene of Plymouth Hoe at dusk is visible above and through the panel.
```

---

## JOURNAL SCREEN DESIGN

Amelia's journal — accessible from the menu. The player's reward for paying attention.

```
JOURNAL DESIGN SPEC:
- Full-screen overlay (16:9)
- Background: a physical notebook — lined paper, slightly cream/off-white
- Handwriting font for Amelia's entries (something personal, slightly uneven, NOT Comic Sans)
- Three tabs along the top: NOTES | PEOPLE | CURIOSITIES
- Border: leather-journal texture, worn, personal

PROMPT FOR REFERENCE:
Painterly illustration, soft oil painting style. A close-up of an open personal journal/notebook. Cream-coloured lined pages. Handwritten notes in neat but personal handwriting — thoughts, observations, a small sketch in the margin (a wren, perhaps). Tabs visible at the top marked in different colours. The journal sits on a wooden desk with a pen beside it. Warm light. This is Amelia's private space — her way of processing the world. The mood is intimate and careful. No anime, no photorealistic.
```

### Journal — Curiosities Tab (Elena Path)
When OK ≥ 5, this tab fills with alchemical sketches and notes.

```
Same journal base but the page content is different — Amelia's drawings of alchemical symbols (ouroboros, the squared circle, the holed stone), a quoted line from Paracelsus, Kernewek words with definitions, a rough map of ley lines. The sketches are learning-in-progress, not expert — she's discovering this. Some words circled, question marks in the margin.
```

---

## PHONE SCREEN

The most innovative UI element. Texting scenes appear on a simulated phone.

```
PHONE SCREEN DESIGN SPEC:
- Centred overlay: ~400×700px with rounded corners
- Dark background (dark mode UI)
- iMessage-style bubbles: blue (#3478F6) for Amelia, grey (#E5E5EA) for others
- Contact name at top (varies by relationship level)
- Typing indicator: three animated dots
- Timestamp below messages (in-game time)
- Small profile photo circle for the contact

PROMPT FOR REFERENCE:
A mockup of a smartphone screen in dark mode, realistic but stylised to match a painterly game aesthetic. The screen shows a text conversation between "Ella 🤍" and the player. Blue bubbles on the right (Amelia's messages), grey on the left (Ella's). The messages are casual, warm, British — "are you dead or just ignoring me" / "both" / "lol ring me later yeah". A typing indicator (three dots) shows at the bottom. The phone's edges are slightly rounded, the screen has a subtle glow. The overall feel should match the game's literary-illustration style, not look like a real screenshot.
```

---

## CHOICE MENU DESIGN

```
CHOICE MENU DESIGN SPEC:
- Choices displayed as rectangular buttons, centred on screen
- Background: matches current alchemical phase colour (variable)
  - Nigredo: dark brown-amber
  - Albedo: cool grey-blue
  - Citrinitas: warm saffron-gold
  - Rubedo: deep wine-rose
- Text: off-white (#F5F5F0), clean serif font
- Hover state: gold (#FFD700) outline glow
- Selected: brief gold pulse animation
- NO stat indicators visible — choices should not telegraph consequences
- Gated choices (stat-locked): greyed out with a faint lock icon, no text explaining why

PROMPT FOR REFERENCE:
A visual novel choice screen mockup showing three choice buttons stacked vertically over a blurred Plymouth Hoe background. The buttons have soft, rounded backgrounds in a cool grey-blue (Albedo palette). Choice text in clean white serif: "Sit with her" / "Give her space" / "Ask if she wants tea". The second option has a subtle gold hover-glow. One option (a fourth) is greyed out with a tiny lock icon. The design is clean, literary, not gamey. No anime, no photorealistic.
```

---

## CONTENT WARNING SCREEN

```
PROMPT FOR REFERENCE:
A simple, clean screen design with a warm dark background (#1A1A2E). Centred text in gold and white: "Content Note" at the top in gold, followed by a brief, matter-of-fact description in white. Below the text, two simple buttons: "Continue" and "Skip this scene." At the bottom, smaller text: "UK support lines: Samaritans 116 123 | Mind 0300 123 3393." The design is respectful, not dramatic — informational, caring, non-intrusive. Warm but sombre.
```

---

## GENERATION PRIORITY

1. **Main menu background** — First impression. Get this right.
2. **Phone screen mockup** — Novel UI element, tests the style
3. **Textbox reference** — Core gameplay element
4. **Choice menu** — Tests phase-colour system
5. **Journal** — Nice-to-have for later
