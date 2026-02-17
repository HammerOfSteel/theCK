# The CK: Amelia

> A choice-driven visual novel about a young psychology student's transformative first year at the University of Plymouth — where Jungian shadows, Cornish folklore, and the quiet alchemy of growing up collide.

**Play now:** [amelia.dancingsalamanders.com](https://amelia.dancingsalamanders.com)

## Synopsis

Amelia James, 18, leaves suburban London for Plymouth to study psychology. What follows is one academic year (October to June) of friendship, heartbreak, intellectual awakening, and difficult choices — guided by the player. Beneath the coming-of-age surface runs a deeper current: the Hero's Journey mapped to the stages of the alchemical *Magnum Opus*, Cornish folklore threaded through the landscape, and a hidden path of genuine esoteric discovery for those who look for it.

The game tracks six dimensions of Amelia's growth — Academic Achievement, Social Interaction, Mental Health, Self-Discovery, Moral Choices, and Occult Knowledge — through a hidden karma system. Small choices compound into fate. Seven distinct endings await.

## Project Status

| Component | Status |
|---|---|
| **V1 (Amelia/)** | Legacy prototype. Chapters 1–3 & 12 playable. |
| **V2 (Amelia_V2/)** | **Active development.** Full scripts written, placeholder art in place, deployed to web. |
| **CI/CD** | GitHub Actions → Oracle Cloud. Manual-trigger deploy via `workflow_dispatch`. |

### What's Done

| Phase | Description | Status |
|---|---|---|
| **1 — Foundation** | 15 design documents: characters, world, mechanics, narrative, choice map, alchemy, folklore, art direction, point balancing | ✅ Complete |
| **2 — Writing** | 14 Ren'Py scripts (12 chapters + definitions + screens). ~10,600 lines. | ✅ Complete |
| **2.5 — Songs** | 20 Dancing Salamanders / Geddon Bird songs placed as slideshow moments | ✅ Complete |
| **3 — Image Prompts** | 17 prompt packs (9 character + 5 background + 3 CG/UI) for art generation | ✅ Complete |
| **3.5 — Placeholders & Tech** | Placeholder art system, layered images, GUI, screens, journal, phone, save system, audio guide | ✅ Complete |
| **3.5 — Audio** | Ambient tracks, SFX, song conversion | 🔧 In progress |
| **3.5 — Writing polish** | Dialogue, pacing, voice audit, sensitivity review | 📝 Not started |
| **3.9 — Art generation** | Character sprites, backgrounds, CGs, UI art | 📝 Not started |
| **4 — Polish & release** | Playtesting, balance, proofreading, accessibility, builds | 📝 Not started |

### Deployment

The game is deployed as a Ren'Py web build at **[amelia.dancingsalamanders.com](https://amelia.dancingsalamanders.com)**.

- **Hosting:** Oracle Cloud (Docker + FastAPI/uvicorn + nginx reverse proxy + Let's Encrypt SSL)
- **CI/CD:** [`.github/workflows/deploy-amelia.yml`](.github/workflows/deploy-amelia.yml) — manual trigger only
- **Build:** Downloads Ren'Py SDK + Web Extension, runs `web_build`, deploys via rsync
- **Presplash:** Randomly picks from `Amelia_V2/game/images/web_presplash/` each deploy

## Repository Layout

```
theCK/
├── .github/workflows/       # CI/CD
│   └── deploy-amelia.yml    #   Manual deploy workflow
├── Amelia/                  # V1 (legacy prototype)
│   ├── game/                #   Ren'Py scripts + assets
│   └── story/               #   Markdown story drafts
├── Amelia_V2/               # V2 (active development)
│   ├── design/              #   15 design documents
│   │   ├── characters.md
│   │   ├── world_and_locations.md
│   │   ├── game_mechanics.md
│   │   ├── narrative_structure.md
│   │   ├── choice_map.md
│   │   ├── relationship_matrix.md
│   │   ├── dialogue_style_guide.md
│   │   ├── alchemical_thread_map.md
│   │   ├── cornish_folklore_reference.md
│   │   ├── sarahs_arc.md
│   │   ├── art_direction.md
│   │   ├── point_balance_spreadsheet.md
│   │   └── songs.md
│   ├── game/                #   Ren'Py project
│   │   ├── chapter_1–12.rpy #   12 chapter scripts
│   │   ├── definitions.rpy  #   Characters, variables, init
│   │   ├── screens.rpy      #   Custom screens (journal, phone, etc.)
│   │   ├── gui.rpy          #   GUI styling, alchemical phase colours
│   │   ├── layered_images.rpy
│   │   ├── slideshows.rpy   #   Song moment slideshows
│   │   ├── audio/           #   songs/, ambient/, sfx/
│   │   └── images/          #   Sprites, backgrounds, CGs
│   ├── prompts/             #   Art generation prompt packs
│   │   ├── characters/      #   9 character prompt files
│   │   ├── backgrounds/     #   5 location prompt files
│   │   ├── cg/              #   CG scene + slideshow prompts
│   │   └── ui/              #   UI element prompts
│   ├── overview.md
│   ├── todo.md              #   Master task tracker
│   └── audio_guide.md       #   51 ambient + 15 SFX specs
├── normal_style_scripts/    # Alternate script format (reference)
└── tools/                   # Utility scripts (voice gen, conversion, etc.)
```

## Core Themes

- **Leaving home and becoming yourself** — the terror and exhilaration of the first year
- **Friendship as survival** — the people you meet can save or break you
- **Mental health is real** — depression, anxiety, and the courage to reach out (handled with care)
- **The Shadow** — every character mirrors an aspect of Amelia's psyche (Jung)
- **Solve et Coagula** — the alchemical process of dissolution and rebirth, mapped to the story arc
- **The Cornish Otherworld** — standing stones, holy wells, and the *pellar* tradition woven into Cornwall's landscape
- **Fate and free will** — small choices compound into destiny through the hidden karma engine

## Characters

### Main Cast
| Character | Role | Archetype |
|---|---|---|
| **Amelia James** | Protagonist, 18, psychology student | The Seeker — *prima materia* becoming gold |
| **Ella Chen** | Childhood best friend (London) | The Golden Thread — connection to the ordinary world |
| **Prof. Hawthorne** | Academic mentor | Salt — rigour, structure, the body of knowledge |
| **Dr. Simmons** | Wellbeing mentor | Mercury — fluidity, connection, emotional intelligence |
| **Maya Patel** | Spiritual friend/mentor | Sulphur — the volatile, the spiritual fire |
| **Elena Trevorran** | Hidden mentor — Cornish *pellar* | The Soror Mystica — the secret guide |
| **Lucas Adeyemi** | Intellectual companion | The Animus — the thinking-partner |
| **Zara Okafor** | Fighter, faces racism head-on | The Red Lion — transformation through confrontation |
| **Raj Sharma** | The heart of the group | The Self in community — warmth and belonging |
| **Sarah Whitmore** | Quiet, depressed, at risk | The Mirror — *can you save someone who doesn't want to be saved?* |
| **Tasha Reynolds** | Bully → potential redemption | The Shadow — what Amelia fears and represses |

### Supporting Cast
Sophia Langford (academic rival), Michael Okonkwo (activist), Liz Torres (roommate), Lily James (cousin), David & Grace James (parents)

## Structure

12 chapters following the Hero's Journey, each mapped to an alchemical stage:

| # | Chapter | Month | Alchemical Stage |
|---|---|---|---|
| 1 | The Ordinary World | September | Pre-Nigredo |
| 2 | The Call to Adventure | October | Early Nigredo |
| 3 | Refusal of the Call | Oct–Nov | Nigredo deepening |
| 4 | Meeting the Mentor | November | Late Nigredo / Albedo |
| 5 | Crossing the Threshold | Nov–Dec | Albedo |
| 6 | Tests, Allies, Enemies | Dec–Jan | Albedo continued |
| 7 | The Approach | Jan–Feb | Citrinitas beginning |
| 8 | **The Ordeal** | February | **Citrinitas — the furnace** |
| 9 | The Reward | March | Late Citrinitas |
| 10 | The Road Back | April | Early Rubedo |
| 11 | The Resurrection | May | Rubedo |
| 12 | Return with the Elixir | June | Post-Rubedo |

## Game Mechanics

- **6 stats** tracked silently: AA, SI, MH, SD, MC, OK
- **Hidden karma system** — the player sees consequences, not numbers
- **Amelia's journal** as the narrative stat screen
- **Relationship values** (0–10) per character
- **Dynamic mentor assignment** at end of Chapter 3
- **Sarah's fate** determined by cumulative choices across the whole game (4-tier spectrum, not binary)
- **Karma Dice** (d20 + modifiers) at pivotal moments for genuine uncertainty
- **7 endings:** The Scholar, The Companion, The Healer, The Alchemist, The Whole, The Grief, The Bittersweet

## Tech

- **Engine:** [Ren'Py](https://www.renpy.org/) 8.3.7
- **Resolution:** 1920×1080
- **Build name:** TheCK
- **Web deploy:** Ren'Py WebAssembly build via GitHub Actions → Oracle Cloud
- **Live at:** [amelia.dancingsalamanders.com](https://amelia.dancingsalamanders.com)

---

*By GizmoBot Studios — Luna Ironfoot (story/design), Zara Greenleaf (art/history), Mira Silverbranch (sound)*

---

# V1 Reference (Original Design)

> The sections below document the original V1 design. Kept for reference — the V2 design documents in `Amelia_V2/` supersede these.

<details>
<summary>Click to expand V1 design notes</summary>

## V1 Main Characters
- Amelia - The protagonist. A hopeful psychology student, eager to learn but unaware of the social and personal challenges she'll encounter.

- Ella - Amelia's childhood best friend. A steadfast supporter, she's the link to Amelia's past and provides a comforting voice.

- Prof. Hawthorne - The head of the psychology department. Stern yet fair, he becomes Amelia's mentor, guiding her through the intricacies of psychology.

- Lucas - Amelia's roommate. A bit introverted, he introduces Amelia to the world of Jungian psychology.

- Zara - A fellow student. Born in another country and having faced racism, she becomes Amelia's confidante in understanding racism and cultural differences.

- Maya - A student with a deep interest in ancient wisdom and Zen philosophy. She helps Amelia explore spiritual and philosophical dimensions.

- Raj - A student specializing in family systems. He helps Amelia understand the complexities of familial relationships.

- Sarah - Another student who Amelia meets by chance. Sarah is struggling with severe depression, and her presence in Amelia's life introduces themes of mental health and suicide. Her fate depends on the player's choices, with her potential suicide adding a layer of gravity to the narrative.

## V1 Background Characters
- Mr. & Mrs. James - Amelia's parents, who are both proud and worried about their daughter's journey.

- Lily - Amelia's younger cousin, a few years her junior. She looks up to Amelia and often seeks her advice, providing a familial connection and perspective on Amelia's growth.

- Tasha - Another student at the university, she is initially a bully towards Amelia but undergoes significant character development.

- Dr. Simmons - Teaches positive psychology. Enthusiastic and always encouraging students to look at the brighter side of life.

- Elena - A mature student who returned to university later in life. She becomes a motherly figure to Amelia, offering wisdom and life advice.

- Michael - A student activist passionate about social justice. He introduces Amelia to the broader social issues affecting students and society.

- Sophia - Amelia's academic rival. Competitive and driven, she pushes Amelia to excel but also challenges her in unexpected ways.

## V1 Places
### London
- Amelia's London Home - A cozy home in the suburbs, representing her comfort zone.
- Ella's House - The place where Amelia and Ella often hung out during their school days.
- Local Park - A peaceful green space where Amelia spent time reflecting and relaxing.
- High Street - A bustling area with shops, cafes, and the occasional street performer, representing the vibrant life of the city.
- Local Library - A quiet spot where Amelia used to study and escape from the hustle and bustle.
- Art Gallery - A place Amelia visited to find inspiration and serenity amidst her busy life.
- Museum of Natural History - A location filled with exhibits on human history and nature, sparking Amelia's interest in anthropology and psychology.
- Thames Riverside - A scenic area by the river where Amelia goes for walks and contemplation.
- Bookstore - A quaint bookstore where Amelia often buys her psychology and philosophy books.
- Tea House - A traditional tea house where Amelia and Ella enjoy afternoon tea, representing their cherished moments together.

### Plymouth
- Plymouth University - The main setting, full of academic buildings, dorms, and student hangouts.
- Prof. Hawthorne’s Office - A room filled with books, where Amelia gets guidance.
- City Library - A peaceful place where Amelia spends time studying.
- Student Union - A hub for student activities and social events.
- Local Café - A cozy spot where Amelia and her friends hang out and discuss life.
- Hoe Park - A large waterfront park offering stunning views of Plymouth Sound, a favorite spot for relaxation and reflection.
- Barbican - The historic heart of Plymouth with cobbled streets, shops, and restaurants. Amelia explores its rich history and cultural heritage.
- Royal William Yard - A scenic waterfront area with restaurants, art galleries, and events.
- Marine Biological Association - An institution for marine biology research where Amelia learns about psychology's relation to environmental science.
- Dartmoor National Park - Nearby, providing opportunities for outdoor adventures and deep reflection.

## Cornwall
- Cornwall Coastline - A serene place Amelia visits for introspection and exploration.
- St. Ives - A picturesque town known for its art scene and beautiful beaches.
- Tintagel - Famous for its castle and Arthurian legends, offering a mystical backdrop for Amelia's exploration.
- Penzance - A charming town with a rich history and beautiful seaside views.
- Falmouth - Known for its maritime heritage and vibrant cultural scene.
- Bodmin Moor - A wild, rugged landscape perfect for reflection and escape from the academic pressures.
- Eden Project - A vast collection of biomes housing a variety of plants, offering a unique and educational retreat.
- St. Michael's Mount - A tidal island with a medieval church and castle, providing a mystical and historical exploration site.
- Lost Gardens of Heligan - A restored botanical garden that offers a peaceful and introspective setting.
- Polperro - A quaint fishing village with narrow lanes and charming cottages, perfect for quiet contemplation.

## Other Locations
- Local Villages - Quaint, small villages dotting the landscape, each with its own charm and stories.
- Historical Sites - Various sites of historical importance scattered around Cornwall, providing a sense of depth and history.
- Nature Reserves - Protected areas showcasing the natural beauty of Cornwall, ideal for walks and contemplation.

# Story Format
Following the Hero’s Journey, the story would have:

- Ordinary World - Amelia in London, awaiting her university journey.

- Call to Adventure - Amelia's acceptance letter and her decision to leave for Plymouth.

- Refusal - Amelia's initial reluctance due to the fear of the unknown.

- Meeting with the Mentor - Introduction to Prof. Hawthorne.

- Crossing the Threshold - Amelia moves to Plymouth.

- Tests, Allies, Enemies - Facing bullying, meeting Zara, Lucas, Maya, and Raj, understanding racism, depression, and family dynamics. Chance encounter with Sarah.

- Approach - Amelia delves deeper into her psychology studies and chooses her specialization. Developing deeper connections with the main characters, especially Sarah, whose struggle with mental health becomes apparent.

- Ordeal - Facing severe depression and confronting her bully. The potential suicide of Sarah (based on player choices) adds an emotional and challenging layer.

- Reward - Amelia's personal growth and academic achievements. Coming to terms with Sarah's fate and learning from it.

- The Road Back - Returning to London during breaks, reflecting on her growth and the impact of her experiences.

- Resurrection - Amelia's final year, overcoming her last challenges and synthesizing her academic and personal growth.

- Return with the Elixir - Graduation and taking back her learnings to the real world, with a renewed sense of purpose and understanding of life’s complexities.

# Choice Dynamics and Choice Tree Overview
## Points System
The choices made by the player will affect Amelia's story through a point system that influences different aspects of her life. The points are categorized into the following general categories:

- Academic Achievement (AA) - Points accumulated based on Amelia's academic performance and her dedication to studies.
- Social Interaction (SI) - Points based on Amelia's relationships with friends, mentors, and other characters.
- Mental Health (MH) - Points reflecting Amelia's mental well-being, affected by her ability to cope with stress, depression, and personal challenges.
- Self-Discovery (SD) - Points representing Amelia's exploration of psychology, ancient wisdom, Zen, and personal growth.
- Moral Choices (MC) - Points determined by Amelia's ethical and moral decisions throughout the story.
- Occult Knowledge (OK) - Points gathered by Amelia exploring deeper occult, alchemical, and ancient wisdom themes.
Choice Dynamics

## Academic Achievement (AA)
- Studying - Choosing to spend time studying increases AA points.
- Attending Lectures - Regular attendance and participation in lectures boost AA points.
- Assignments and Exams - Performance in assignments and exams directly impacts AA points.
- Engaging with Professors - Building relationships with professors like Prof. Hawthorne enhances AA points.

## Social Interaction (SI)
- Friendship with Ella - Maintaining and nurturing the friendship with Ella adds SI points.
- Forming Bonds with Lucas, Zara, Maya, and Raj - Positive interactions and support among friends increase SI points.
- Navigating Bullying and Conflict - Successfully managing conflicts, such as with Tasha, affects SI points.
- Helping Sarah - Supporting Sarah in her struggles significantly impacts SI points.

## Mental Health (MH)
- Seeking Help - Choosing to seek counseling or support boosts MH points.
- Practicing Self-care - Engaging in activities that promote well-being, like meditation, increases MH points.
- Handling Stress - Successfully managing academic and personal stress affects MH points.
- Dealing with Sarah’s Situation - Decisions regarding Sarah's mental health and potential suicide impact MH points.

## Self-Discovery (SD)
- Exploring Psychology - Delving into different psychology specializations increases SD points.
- Learning Ancient Wisdom and Zen - Engaging with Maya and exploring philosophical teachings boosts SD points.
- Introspective Activities - Spending time in nature, like the Cornwall Coastline, and reflecting on personal growth adds SD points.
- Attending Workshops and Seminars - Participating in extracurricular activities related to psychology and philosophy enhances SD points.

## Moral Choices (MC)
- Ethical Dilemmas - Making decisions that reflect strong moral values adds MC points.
- Standing Up Against Injustice - Actions taken to combat bullying, racism, and social issues impact MC points.
- Helping Others - Acts of kindness and support, especially towards characters like Sarah, increase MC points.
- Personal Integrity - Maintaining honesty and integrity in various situations affects MC points.

## Occult Knowledge (OK)
- Secret Books and Manuscripts - Finding and studying ancient texts on alchemy, mysticism, and the occult increase OK points.
- Mystical Experiences - Engaging in unique events or rituals with Maya boosts OK points.
- Hidden Locations - Discovering and exploring hidden or mystical locations in Cornwall adds OK points.
- Special Characters - Interacting with characters knowledgeable in the occult and ancient wisdom enhances OK points.

# Choice Tree Overview
## Early Choices
Accepting the Offer - Decision to attend Plymouth University.
- High AA, SI, and SD points if Amelia eagerly accepts.
- Low MH and MC points if Amelia is reluctant and unsure.

First Days at University - Choices about settling in, attending orientation, and meeting new people.
- High SI and SD points if Amelia actively participates.
- Low MH points if Amelia isolates herself.

Mid-Game Choices
Balancing Studies and Social Life - Managing time between academics and friendships.
- High AA points if Amelia prioritizes studies.
- High SI and MH points if Amelia balances well.

Dealing with Bullying and Conflict - Choices regarding Tasha and other conflicts.
- High MC points if Amelia confronts bullying assertively.
- High SI points if Amelia seeks help and resolves conflicts peacefully.

Supporting Sarah - Decisions about helping Sarah through her mental health struggles.
- High MH and MC points if Amelia actively supports Sarah.
- Low MH points if Amelia neglects Sarah's issues.

Exploring the Occult Path - Discovering hidden books, engaging in rituals, and meeting special characters.
- High OK points if Amelia pursues these activities.
- Low AA and SI points if Amelia neglects her studies and social interactions for the occult path.

Late-Game Choices
Specialization Decision - Choosing a psychology specialization.
- High AA and SD points if Amelia makes a well-informed choice.
- Low MH points if she is indecisive and stressed.

Coping with Academic Pressure - Managing stress during exams and final projects.
High AA and MH points if Amelia employs healthy coping mechanisms.
- Low MH points if she succumbs to stress.
- Sarah’s Fate - The outcome of Sarah’s struggles.
- High MC and SI points if Sarah is saved due to Amelia’s intervention.
- Low MH and SI points if Sarah’s fate is tragic.

Final Occult Ritual - Engaging in a final, significant occult ritual.
High OK points if Amelia participates fully.
- Low MH and SI points if this path causes her to isolate herself further.

# Endings Based on Points
- Academic Success Ending - High AA and SD points. Amelia graduates with top honors and a deep understanding of her field.
- Social Butterfly Ending - High SI points. Amelia forms lasting friendships and is well-loved by her peers.
- Mental Health Advocate Ending - High MH and MC points. Amelia becomes a strong advocate for mental health awareness and support.
- Tragic Ending - Low MH and SI points. Amelia’s journey is marked by loss and unresolved issues.
- Balanced Growth Ending - High points across all categories. Amelia achieves a well-rounded success, balancing academics, friendships, personal growth, and moral integrity.
- Enlightenment Ending - High OK points. Amelia discovers deep occult and ancient wisdom, leading to a transformative experience of enlightenment.

This choice tree and points system create a dynamic and engaging story, where every decision shapes Amelia's journey and ultimate outcome, with the added depth of a secret path exploring occult wisdom and enlightenment.


# Story Progression Overview
The core events of the Hero's Journey will always occur, ensuring a consistent narrative backbone. Conditional paths and scenes will occur based on point balances, allowing for rich and varied experiences. The player will be able to gain points for each category (Academic Achievement, Social Interaction, Mental Health, Self-Discovery, Moral Choices, Occult Knowledge) throughout various paths, ensuring interwoven storylines.

# Explanation of Dynamic Choice Tree
- Always-Occurring Core Events: Key plot points and decisions that every player will encounter, forming the backbone of the narrative.
- Conditional Choices and Scenes: These depend on the player's accumulated points in different categories, influencing the narrative and allowing for diverse experiences.
- Interwoven Paths: Multiple paths intersect, providing opportunities to gain points in various categories and reflecting the complexity of life and fate.

# Choice Categories and Points
- Academic Achievement (AA): Choices related to studying, attending lectures, and engaging with professors.
- Social Interaction (SI): Choices related to forming and maintaining relationships.
- Mental Health (MH): Choices related to self-care, seeking help, and managing stress.
- Self-Discovery (SD): Choices related to exploring psychology, ancient wisdom, and personal growth.
- Moral Choices (MC): Choices reflecting ethical and moral decisions.
- Occult Knowledge (OK): Choices related to exploring occult, alchemical, and ancient wisdom themes.

# Choice Tree Representation
The following Mermaid JS chart represents the dynamic choice tree, showing how choices and paths interweave based on the points accumulated. Core events are highlighted to indicate always-occurring moments in the narrative.

```
graph TD
    A[Ordinary World] -->|Call to Adventure| B[Acceptance of University Offer]
    B -->|Refusal of the Call| C[Initial Reluctance]
    B -->|Meeting with the Mentor| D[Prof. Hawthorne]
    D -->|Crossing the Threshold| E[First Days at University]

    E -->|Active Participation| F1[Forming Bonds]
    E -->|Isolation| F2[Struggling Alone]

    F1 -->|Meet Lucas| G1[Introduction to Jungian Psychology]
    F1 -->|Meet Zara| G2[Understanding Racism]
    F1 -->|Meet Maya| G3[Ancient Wisdom and Zen]
    F1 -->|Meet Raj| G4[Family Systems]

    F2 -->|Low MH| H1[Seek Counseling]
    F2 -->|High MH| H2[Self-Reflection]

    G1 -->|High SI| I1[Developing Deep Friendship]
    G1 -->|High SD| I2[Exploring Jungian Concepts]
    
    G2 -->|High MC| I3[Stand Against Racism]
    G2 -->|High SI| I4[Supporting Zara]

    G3 -->|High OK| I5[Occult Exploration]
    G3 -->|High SD| I6[Spiritual Growth]

    G4 -->|High SI| I7[Understanding Family Dynamics]
    G4 -->|High SD| I8[Choosing Specialization]

    H1 -->|High MH| J1[Improved Well-being]
    H1 -->|Low MH| J2[Continued Struggles]

    J1 -->|Approach| K[Deepening Studies and Relationships]
    J2 -->|Approach| K

    K -->|Tests, Allies, Enemies| L1[Dealing with Bullying]
    K -->|Tests, Allies, Enemies| L2[Supporting Sarah]

    L1 -->|High MC| M1[Confront Tasha]
    L1 -->|High SI| M2[Seek Help Against Bullying]

    L2 -->|High MH| M3[Support Sarah's Mental Health]
    L2 -->|Low MH| M4[Neglect Sarah's Struggles]

    M1 -->|High MC| N1[Resolving Conflict]
    M2 -->|High SI| N2[Building Stronger Bonds]

    M3 -->|High MH| N3[Sarah's Recovery]
    M4 -->|Low MH| N4[Sarah's Tragic Fate]

    N1 -->|High SI| O1[Stronger Social Network]
    N2 -->|High MH| O2[Improved Mental Health]

    N3 -->|High SI| O3[Sarah's Continued Friendship]
    N4 -->|Low SI| O4[Dealing with Grief]

    O1 -->|Ordeal| P[Facing Final Academic and Personal Challenges]
    O2 -->|Ordeal| P

    O3 -->|Ordeal| P
    O4 -->|Ordeal| P

    P -->|Reward| Q[Personal Growth and Achievements]
    Q -->|The Road Back| R[Returning Home for Breaks]
    R -->|Resurrection| S[Final Year Challenges]
    S -->|Return with the Elixir| T[Graduation and Future]

    %% Occult Knowledge Path
    G3 -->|High OK| I5[Occult Exploration]
    I5 -->|Secret Books and Manuscripts| U1[Hidden Wisdom]
    U1 -->|Mystical Experiences| U2[Occult Rituals]
    U2 -->|High OK| U3[Enlightenment Path]

    U3 -->|Final Ritual| V[Achieving Enlightenment]
    V -->|High OK| W[Enlightenment Ending]
    
    %% Ending Paths
    T -->|High AA and SD| X1[Academic Success Ending]
    T -->|High SI| X2[Social Butterfly Ending]
    T -->|High MH and MC| X3[Mental Health Advocate Ending]
    T -->|Low MH and SI| X4[Tragic Ending]
    T -->|Balanced Points| X5[Balanced Growth Ending]
    W -->|High OK| X6[Enlightenment Ending]
```

# Key Story Progression Points
- Ordinary World: Sets the stage with Amelia's life in London.
- Call to Adventure: Amelia receives her acceptance letter to Plymouth University.
- Refusal of the Call: Amelia's initial reluctance and fears.
- Meeting with the Mentor: Introduction to Prof. Hawthorne.
- Crossing the Threshold: Moving to Plymouth and starting university.
- Tests, Allies, Enemies: Forming bonds, facing bullying, and supporting friends.
- Approach: Delving deeper into studies and relationships.
- Ordeal: Facing major academic and personal challenges, Sarahs suicide if player does not have very high scores in all categories.
- Reward: Achieving personal growth and academic success.
- The Road Back: Returning home for breaks and reflecting on growth.
- Resurrection: Final year challenges and synthesizing growth.
- Return with the Elixir: Graduation and looking forward to the future.

Additional Key Points
- Occult Knowledge Path: Secret books, mystical experiences, and occult rituals leading to potential enlightenment.
- Interwoven Paths: Opportunities to gain points in various categories through different paths, ensuring a rich and interconnected narrative.
</details>