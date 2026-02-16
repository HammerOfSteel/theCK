# The CK: Amelia V2 — Game Mechanics & Karma System

> The goal is a system that feels like *fate* rather than a score counter. The player should never think "I need 3 more AA points." They should think "I've been neglecting my studies" or "I wonder what would happen if I went to that stone circle with Elena." The numbers run silently underneath; the player experiences consequences, not mathematics.

---

## CORE PHILOSOPHY

### Karma, Not Points
In V1, choices directly awarded +1 to a stat category. In V2, we reframe this:

- **Choices create patterns.** A single choice rarely matters; it's the *accumulation* of choices that shapes destiny.
- **The system observes, then responds.** Instead of instant feedback ("SI +1!"), consequences emerge *later* — a character remembers what you did, a door opens that wouldn't have otherwise, a conversation takes a different tone.
- **Every gain has a cost.** Time spent studying is time not spent with friends. Time spent on the occult path is time not spent grounding yourself in the real world. The system enforces this through *opportunity cost*, not penalties.
- **Hidden thresholds trigger narrative shifts.** The player doesn't see the numbers — they see a friend say "You've been distant lately" (low SI), or a professor say "Your recent work has been exceptional" (high AA).

### The Fate Wheel (Internal Name)
Internally, we still track six stats. But the *presentation* to the player is different:

| Internal Stat | What the Player Experiences | Metaphor |
|---|---|---|
| **AA** (Academic Achievement) | Academic events, professor reactions, exam outcomes | The **Scholar's Path** |
| **SI** (Social Interaction) | Friendship quality, invitations, support availability | The **Web of Bonds** |
| **MH** (Mental Health) | Amelia's inner monologue, energy, coping ability | The **Inner Flame** |
| **SD** (Self-Discovery) | Philosophical insights, moments of clarity, personal growth | The **Mirror** |
| **MC** (Moral Choices) | How others trust Amelia, moral dilemmas' outcomes | The **Scales** |
| **OK** (Occult Knowledge) | Access to hidden content, Elena's path, mystical experiences | The **Veil** |

---

## STAT RANGES AND THRESHOLDS

### Per-Chapter Point Budget
Each chapter offers approximately **8–12 choice points** distributed across all categories. Not all categories are available in every chapter — the narrative naturally emphasises different aspects at different times.

### Running Totals (across 12 chapters)
- **Maximum possible per stat:** ~25–30 (if you single-mindedly pursue one path)
- **Realistic balanced play:** ~12–18 per stat
- **Minimum if actively neglected:** ~3–5 per stat

### Threshold Tiers

| Tier | Range | Narrative Effect |
|---|---|---|
| **Neglected** | 0–5 | Negative consequences manifest; characters comment; doors close |
| **Low** | 6–10 | Neutral — no special events, basic path |
| **Moderate** | 11–15 | Positive — some bonus scenes, warmer responses |
| **High** | 16–20 | Strong — significant narrative rewards, character arcs deepen |
| **Exceptional** | 21+ | Unlocks hidden content, special endings, unique scenes |

### Negative Points (New in V2)
Some choices can *reduce* a stat. This is rare and significant:
- Ignoring Sarah when she's clearly struggling: **MH -2, SI -1**
- Cheating on an assignment: **MC -3, AA -1** (even if you get the grade)
- Participating in Tasha's mockery of Zara: **MC -2, SI -2**
- Spending all your time on occult reading and missing a friend's crisis: **SI -2, MH -1**

These negative-point choices are *never* the obviously "bad" option. They are tempting, convenient, or the path of least resistance. The system punishes avoidance and moral cowardice, not honest mistakes.

---

## MENTOR ASSIGNMENT (Chapter 4)

The mentor system is the first major consequence of accumulated choices. At the end of Chapter 3, the Fate Wheel determines which mentor is assigned:

### Calculation
```
Scholar Score  = AA + MC
Healer Score   = MH + SI
Seeker Score   = SD + OK
```

The highest score determines the mentor. In case of ties, a secondary tiebreaker applies:

| Primary | Tiebreaker | Mentor |
|---|---|---|
| Scholar highest | MC > AA → Hawthorne; AA > MC → Hawthorne | **Prof. Hawthorne** |
| Healer highest | MH > SI → Simmons; SI > MH → Simmons | **Dr. Simmons** |
| Seeker highest | SD > OK → Maya; OK > SD → Maya | **Maya** |
| OK ≥ 8 alone | (regardless of other scores) | **Elena** (hidden) |

### Elena Override
Elena is accessible if:
- OK ≥ 8 by end of Chapter 3 (very difficult — requires pursuing every occult option)
- AND Amelia made the specific choice in Chapter 1 to buy the old book from the Bromley bookshop
- AND Amelia participated in Maya's ritual in Chapter 3

If Elena is assigned, the player gets a brief "something is different" moment — not a celebration, but a quiet recognition that a hidden door has opened.

### Mentor Colouring
Once assigned, the mentor **changes the flavour of all subsequent chapters**:
- **Hawthorne** scenes emphasise rigour, evidence, intellectual honesty, the history of ideas
- **Simmons** scenes emphasise wellbeing, positive reframing, emotional intelligence, care ethics
- **Maya** scenes emphasise meditation, philosophy, contemplation, the examined life
- **Elena** scenes emphasise folklore, the landscape, the old ways, direct experience over theory

This is implemented as **variant dialogue and alternate scenes** within each chapter, not as separate chapter scripts. The core narrative events remain the same; the *lens* changes.

---

## RELATIONSHIP TRACKING (New in V2)

Beyond the six stats, each major character has a **relationship value** (0–10) that tracks how strong Amelia's bond with them is.

### Characters Tracked
| Character | Starts At | Builds Through | Consequences of Low |
|---|---|---|---|
| **Ella** | 6 (old friend) | Phone calls, visiting London, sharing honestly | Ella stops calling back; painful silence |
| **Lucas** | 0 | Study sessions, late-night talks, shared vulnerability | Remains polite acquaintance; misses key scenes |
| **Zara** | 0 | Standing up for her, honest conversations about race | Respects Amelia less; critical at key moments |
| **Raj** | 1 (immediate warmth) | Spending time, asking about his life, eating his food | Quietly hurt; withdraws support when Amelia needs it |
| **Sarah** | 0 | Persistent kindness, not giving up when she pushes away | Less chance of saving her in Chapter 8 |
| **Maya** | 0 | Spiritual exploration, genuine curiosity, Cornwall trips | Occult path remains surface-level |
| **Tasha** | -2 (hostile) | Patience, confronting with empathy not anger | Remains antagonist; no redemption arc |
| **Sophia** | -1 (rivalry) | Reaching out, acknowledging her loneliness | Never becomes ally; hollow victory |

### How Relationships Build
- **Direct interaction choices** — choosing to spend time with a character raises their value
- **Remembering details** — if Amelia references something a character told her earlier, bonus
- **Moral alignment** — characters respond to choices that match their values
- **Consistency** — one grand gesture matters less than steady, reliable presence

### Relationship ↔ Stat Interaction
Relationships and stats are *linked but not identical*:
- High SI doesn't mean all relationships are high — you might have high SI from having two very deep friendships while neglecting others
- High relationship with Sarah + high MH = best chance of saving her
- High relationship with Maya + high OK = Elena path unlocks
- High relationship with Tasha (yes, positive) + high MC = her redemption arc

---

## THE SARAH EQUATION (Chapter 8)

Sarah's fate is the most important branching point in the game. It is NOT a single choice — it is the culmination of everything the player has done.

### The Calculation
```
Sarah Score = (relationship_sarah × 3) + MH + SI + MC + (relationship_ella × 0.5)
```

Why Ella? Because maintaining your old friendships while building new ones demonstrates the kind of sustained empathy that saves lives.

### Outcomes

| Sarah Score | Outcome | Narrative Effect |
|---|---|---|
| **45+** | **Full save** — Amelia recognises the signs early, intervenes with professional help; Sarah is hospitalised and begins recovery | Chapters 9–12: Sarah is present, fragile but healing; deep friendship |
| **30–44** | **Late save** — Amelia almost misses it; Sarah attempts but survives; the friendship is strained but intact | Chapters 9–12: Sarah is absent for a time, returns changed; complex |
| **15–29** | **Partial save** — Sarah survives physically but withdraws completely; Amelia carries guilt | Chapters 9–12: Sarah is gone from Plymouth; referenced in letters |
| **0–14** | **Tragic outcome** — Sarah dies. This is permanent. The game changes. | Chapters 9–12: Grief, memorial, the weight of "what if"; different ending pool |

### CRITICAL: No "trick" saves
There is no secret dialogue option that bypasses the calculation. You cannot "guess the right answer" in Chapter 8 and save Sarah with low stats. This is a *karma* system — it measures who you have been, not what you say in the moment.

However, there IS one exception: if Amelia has Elena as mentor AND OK ≥ 18, Elena gives Amelia a Cornish charm of protection to give to Sarah. This adds +10 to the Sarah Score — but only because Elena's path has its own demands. You don't "cheat" the system; you've been walking a harder path.

---

## ENDING DETERMINATION

### The Calculation (Chapter 12)
At the start of Chapter 12, the system evaluates:

```python
# Primary ending check (in priority order)
if sarah_died and MH <= 10 and SI <= 10:
    ending = "tragic"
elif OK >= 22 and SD >= 18 and completed_elena_path:
    ending = "enlightenment"
elif AA >= 20 and SD >= 18:
    ending = "academic_success"
elif SI >= 20 and relationship_avg >= 6:
    ending = "social_butterfly"  
elif MH >= 20 and MC >= 18:
    ending = "mental_health_advocate"
elif all_stats >= 14 and no_stat_below_10:
    ending = "balanced_growth"
else:
    ending = "bittersweet"  # NEW: a 7th ending for mixed results
```

### The Seven Endings

| # | Ending | Requirements | Theme |
|---|---|---|---|
| 1 | **The Scholar** | AA ≥ 20, SD ≥ 18 | Academic excellence, research career, deep intellectual fulfilment |
| 2 | **The Companion** | SI ≥ 20, avg relationships ≥ 6 | Rich social world, lasting friendships, chosen family |
| 3 | **The Healer** | MH ≥ 20, MC ≥ 18 | Mental health advocacy, helping others, turning pain into purpose |
| 4 | **The Alchemist** | OK ≥ 22, SD ≥ 18, Elena path | The Magnum Opus completed; Amelia creates the Philosopher's Stone (metaphorically or literally, depending on interpretation); transcendence |
| 5 | **The Whole** | All stats ≥ 14, none below 10 | Balanced growth, the well-rounded life, the Golden Mean |
| 6 | **The Grief** | Sarah died, MH ≤ 10, SI ≤ 10 | Loss and unresolved pain — but NOT without hope; this is a beginning, not an end |
| 7 | **The Bittersweet** | No other ending qualifies | A realistic, mixed outcome — some things were won, some were lost; life continues |

### NEW: The Bittersweet Ending
V1 had a gap where a player who didn't hit any specific threshold would get... nothing. V2 addresses this with a 7th ending that is *not* a failure state. It's the most realistic ending — some friendships deepened while others faded, academic work was uneven, personal growth happened but wasn't dramatic. It ends with Amelia on a train back to London, looking at the Cornish coastline through the window, uncertain but alive.

---

## CHOICE PRESENTATION

### Visual Language
- **Standard choices (2–3 options):** Presented as dialogue options or internal thoughts
- **Timed choices (rare):** Used in crisis moments — if Amelia doesn't choose within 15 seconds, a default (usually avoidance) is selected
- **Hidden choices:** Some scenes have a "do nothing / stay silent" option that isn't explicitly presented but exists (e.g., tapping on a certain object, waiting on a screen longer than expected)
- **Consequence echoes:** Periodically, the game shows a brief poetic line reflecting Amelia's current karmic state — e.g., *"The thread holds steady"* (relationships healthy) or *"Something in the dark shifts"* (OK rising)

### What the Player Never Sees
- Numerical stat values
- The specific points awarded for each choice
- The Sarah calculation
- The ending calculation
- The Elena unlock criteria

### What the Player *Does* See
- **Amelia's journal** (accessible from the menu) — her own reflections on how she's feeling, written in her voice. Updates after key scenes. This is the "stat screen" — expressed narratively, not numerically. Example entries:
  - *"Spent the whole afternoon in the library. My head is full of Freud. Also I haven't spoken to a human being since breakfast. Is this what being a scholar feels like? Because it tastes like stale coffee and regret."* (high AA, low SI recently)
  - *"Maya took me to the holy well today. I felt... something. I can't explain it. The water was cold and the trees were very still and I felt something."* (OK rising)
  - *"Sarah didn't come to the study group again. I texted her. No reply. I should go knock on her door. But what do I even say?"* (Sarah relationship + MH tension)

---

## DND-STYLE FATE MECHANICS (The "Karma Dice")

### Concept
At certain pivotal moments, the game introduces a **hidden dice roll** modified by the player's accumulated karma. This creates genuine uncertainty — even a well-played game has moments where fate intervenes.

### How It Works
```
Outcome = d20 + relevant_stat_modifier + relationship_modifier
```

### When It Triggers
- **Chapter 5:** A random event (good or bad) befalls a friend — outcome modified by SI
- **Chapter 6:** An accusation against Amelia or Zara — outcome modified by MC
- **Chapter 8:** Sarah's intervention timing — the *exact* moment Amelia acts, modified by MH (even if the overall calculation says "save", the details vary)
- **Chapter 11:** The resurrection test — what Amelia faces in her final challenge, modified by SD

### Example: Chapter 8 Crisis Timing
```
If sarah_score >= 45:
    roll = d20 + (MH // 3)
    if roll >= 15: Sarah found early, minimal harm
    if roll >= 10: Sarah found in time, hospitalised
    if roll < 10:  Sarah found late, touch-and-go recovery
```

This means even in the "best" outcome tier, there are variations — giving the game genuine replay value and the sense that fate is real.

### Player-Facing
The player never sees the dice. They see:
- **A brief visual effect** — a flicker, a gust of wind, a candle flame guttering — at the moment fate intervenes
- **Amelia's internal thought:** *"Something turned. I can't explain it. But something turned."*
- The resulting scene variation

---

## STAT GAIN DISTRIBUTION BY CHAPTER

This ensures the game is balanced and every chapter offers meaningful choices:

| Chapter | AA | SI | MH | SD | MC | OK | Total |
|---------|----|----|----|----|----|----|-------|
| 1 - Ordinary World | 1 | 2 | 1 | 2 | 1 | 1 | 8 |
| 2 - Call to Adventure | 2 | 2 | 1 | 1 | 1 | 1 | 8 |
| 3 - Refusal | 2 | 2 | 2 | 1 | 2 | 1 | 10 |
| 4 - Meeting Mentor | 2 | 1 | 1 | 3 | 1 | 2 | 10 |
| 5 - Crossing Threshold | 2 | 2 | 2 | 1 | 1 | 2 | 10 |
| 6 - Tests/Allies/Enemies | 1 | 3 | 2 | 1 | 3 | 2 | 12 |
| 7 - Approach | 2 | 1 | 2 | 2 | 1 | 2 | 10 |
| 8 - Ordeal | 1 | 2 | 3 | 1 | 3 | 2 | 12 |
| 9 - Reward | 2 | 2 | 2 | 2 | 1 | 1 | 10 |
| 10 - Road Back | 1 | 3 | 2 | 2 | 1 | 1 | 10 |
| 11 - Resurrection | 2 | 1 | 2 | 3 | 2 | 2 | 12 |
| 12 - Return | 1 | 1 | 1 | 1 | 1 | 1 | 6 |
| **TOTAL AVAILABLE** | **19** | **22** | **21** | **20** | **18** | **18** | **118** |

Note: A player can only earn ~60–70% of total available points in a single playthrough due to mutually exclusive choices. This ensures no single run feels "complete" — encouraging replay.

---

## HIDDEN ACHIEVEMENTS & EASTER EGGS

For replay value and the joy of discovery:

| Achievement | Trigger | Description |
|---|---|---|
| **The Bibliophile** | Find all 5 hidden books | Located in Bromley bookshop, Barbican shop, Hawthorne's shelf, Elena's flat, a fogou |
| **The Cartographer** | Visit all Cornwall locations | Explore every accessible Cornish site in one playthrough |
| **The Peacemaker** | Redeem Tasha | High MC + high Tasha relationship → her redemption scene |
| **The Keeper** | Maintain Ella relationship at 8+ | Never let the oldest friendship fade |
| **Kernow bys vyken** | Learn 10 Cornish phrases | Pay attention to Elena's teachings |
| **Against All Odds** | Save Sarah with exactly the threshold score | The dice roll just barely makes it — maximum narrative tension |
| **The Complete Work** | See all 7 endings | Requires multiple playthroughs |
| **Prima Materia** | Start New Game+ after Enlightenment ending | Something is different the second time through... |
