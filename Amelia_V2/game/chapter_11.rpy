###############################################################################
##
##  CHAPTER 11: THE RESURRECTION
##
##  Hero's Journey: The hero faces a final test that synthesises all growth.
##  Alchemical Stage: Rubedo — the reddening; the completed Work.
##  Month: May. Location: Plymouth + Cornwall (final trip).
##  Palette: RED. Long golden light. The luminous quality of late spring.
##  Music: Full orchestration returning. Strings. Warmth. Grandeur.
##
##  Scenes: 8–10 (varies by path + Fogou) | Choices: 6 (+Fogou)
##  Max earnable: ~10–12 pts (path-dependent)
##
###############################################################################

label chapter_11:

    $ current_chapter = 11
    stop music fadeout 1.0
    scene black
    with fade

    centered "{size=+20}Chapter Eleven{/size}\n\n{size=+6}The Resurrection{/size}"
    pause 3.0

    ## =====================================================================
    ## SCENE 11.1 — MAY
    ## The days are long. Everything is bright and ending.
    ## =====================================================================

    scene bg_plymouth_hoe_day
    with dissolve

    # play music "audio/ch11_resurrection.ogg" fadein 3.0 volume 0.4

    "May."

    "The days are impossibly long — light until nine, ten, the sky holding its blue like a breath held too long. The campus is thick with blossom and the specific energy of people who know this is ending."

    "Revision timetables on every wall. Library seats fought over. The coffee shop queue at 8am. The particular intensity of students who've been told their future depends on the next three weeks."

    "Amelia walks to the library. She has a seat now — not by the window (someone else's territory) but in the corner, by the history section, where the light is good in the afternoon and nobody bothers her."

    "She's ready. Or as ready as anyone can be."

    ## =====================================================================
    ## SCENE 11.2 — FINAL EXAMS
    ## =====================================================================

    scene bg_library
    with dissolve

    "The first exam: Developmental Psychology. Two hours. Four questions from eight."

    "She opens the paper."

    "'Critically evaluate the role of early attachment relationships in the development of emotional regulation throughout the lifespan.'"

    thought "Bowlby. Ainsworth. The strange situation. Disorganised attachment as a predictor of—"

    "But it's not just theory anymore. It's Sarah's face in the hospital. It's Raj's hand on her shoulder. It's Ella's voice on the phone at 3am. It's her own door, open or closed."

    thought "I know this. Not because I read it. Because I lived it."

    ## =====================================================================
    ## CHOICE 11.1 — FINAL EXAMS
    ## =====================================================================

    if stat_mh < 10:
        menu:
            "The exam paper. Two hours. The pressure is a physical thing."

            "Prepared and disciplined — trust what you know.":
                $ ch11_exams = "prepared"
                $ add_stat("stat_aa", 1)
                $ add_stat("stat_sd", 1)

                "She writes."

                "The words come — not fluently, not without effort, but with a depth that surprises even her. She cites the research. She cites the experience. She makes connections between attachment theory and social identity that aren't in any textbook."

                "She finishes with four minutes to spare. She puts down her pen."

                thought "I did that. Not perfectly. But truly."

            "Anxious but persevering — get through it.":
                $ ch11_exams = "anxious"
                $ add_stat("stat_aa", 1)

                "Her hand shakes for the first ten minutes."

                "The words come — slowly, like pulling teeth. But they come."

                "She writes a solid answer. Not brilliant. Not inspired. But competent. True. Enough."

                thought "I'm going to pass. That's enough. Right now, that's enough."

            "Struggling — the pressure is too much.":
                $ ch11_exams = "struggling"
                $ add_stat("stat_mh", -1)

                "She stares at the paper."

                "Twenty minutes pass. She writes a sentence. Crosses it out. Writes another."

                "The exam hall is enormous and full of scribbling and she can't think. The words are in her head but they won't come out in the right order."

                "She submits something. It's not her best. It might not be enough."

                thought "I should have asked for mitigating circumstances. I should have done a lot of things."
    else:
        menu:
            "The exam paper. Two hours. She knows this."

            "Prepared and disciplined — trust what you know.":
                $ ch11_exams = "prepared"
                $ add_stat("stat_aa", 1)
                $ add_stat("stat_sd", 1)

                "She writes."

                "The answer flows — theory woven with insight, research connected to lived understanding. She finds herself making an argument she's never rehearsed: that attachment isn't just a childhood process but a lifelong practice of courage."

                "She finishes with four minutes to spare."

                thought "I know who I am when I write. That took a year to learn."

            "Anxious but persevering — get through it.":
                $ ch11_exams = "anxious"
                $ add_stat("stat_aa", 1)

                "The nerves come. Of course they do."

                "But she breathes. She starts. The words come — slowly at first, then with increasing certainty."

                "By the end, she's written something solid. Not perfect. Good."

                thought "I did it. It's done."

    ## =====================================================================
    ## SCENE 11.3 — SOPHIA RESOLUTION
    ## =====================================================================

    scene bg_library
    with dissolve

    "Between exams."

    if rel_sophia >= 3:
        "Sophia finds her in the library."

        sophia "I need a study partner for Research Methods. You're the only person in the cohort who actually understands factor analysis."

        a "That's not true. You understand it better than I do."

        sophia "I understand it theoretically. You understand it intuitively. There's a difference."

        "She sits down. She brought two coffees."

        sophia "I got you an Americano. You always get Americano."

        thought "She knows my coffee order. When did Sophia Chen start knowing my coffee order?"

        ## =====================================================================
        ## CHOICE 11.2A — SOPHIA (High relationship)
        ## =====================================================================

        menu:
            "Sophia is offering something. Study partnership. Maybe more."

            "Study together — become genuine friends.":
                $ ch11_sophia = "friends"
                $ add_stat("stat_si", 1)
                $ add_stat("stat_aa", 1)
                $ add_rel("rel_sophia", 1)

                "They study."

                "Three days. Every morning. Sophia is brilliant — precise, methodical, relentless. But she's also funny, in a dry way Amelia never noticed: deadpan observations about their lecturers, a running commentary on the absurdity of statistical terminology."

                sophia "The Bonferroni correction is named after an Italian mathematician who was probably having a breakdown when he invented it."

                a "That's not true."

                sophia "It should be."

                "On the third day, they pack up. Sophia pauses."

                sophia "I was awful to you. At the start. I was competitive and dismissive and I made you feel small."

                a "Sophia—"

                sophia "Let me say this. I was threatened by you. Because you're good at the thing I thought I was best at, and I didn't know how to share that space."

                "A pause."

                sophia "I'm sorry."

                a "Thank you. Genuinely."

                "They walk out of the library together. The sun is warm."

                sophia "Same time tomorrow?"

                a "Same time tomorrow."

    else:
        "Sophia is in the library. Same section. Different table."

        "They haven't spoken properly since — Amelia can't remember. The silence between them is thick with old rivalry."

        "Sophia glances up. They make eye contact."

        "Amelia nods. Sophia nods."

        ## =====================================================================
        ## CHOICE 11.2B — SOPHIA (Low relationship)
        ## =====================================================================

        menu:
            "The rivalry had a final flare during revision. Sophia got the last library copy of a key textbook."

            "Rise above it — she doesn't need Sophia's approval.":
                $ ch11_sophia = "rise_above"
                $ add_stat("stat_sd", 1)

                thought "I used to need to beat her. I used to check my marks against hers. I used to do that thing where you casually mention your grade in conversation."

                thought "I don't need that anymore. She's brilliant. I'm different. Those aren't in competition."

                "She goes back to her notes."

    ## =====================================================================
    ## SCENE 11.4 — TASHA RESOLUTION
    ## =====================================================================

    scene bg_campus_quad
    with dissolve

    "Tasha."

    "She's been peripheral all term. After the Instagram thing, after the formal complaint, after the silence — she exists at the edges of corridors, in the gaps between conversations."

    if rel_tasha >= 3 and stat_mc >= 15:

        "Until today."

        "Amelia is leaving the library. Tasha is sitting on the bench outside. Alone."

        "She's not on her phone. She's not doing anything. She's just — sitting."

        "Amelia almost walks past."

        "Almost."

        a "Tasha."

        "Tasha looks up. Her face does the thing — the mask, the armour, the practiced indifference."

        "But it doesn't hold. Something underneath cracks."

        ## =====================================================================
        ## CHOICE 11.3A — TASHA (Compassion ending)
        ## =====================================================================

        menu:
            "Tasha is unmasked. This is the moment."

            "Sit down. Give her the space to break.":
                $ ch11_tasha = "compassion"
                $ add_stat("stat_mc", 1)
                $ add_stat("stat_si", 1)
                $ add_rel("rel_tasha", 2)

                "She sits."

                "She doesn't say anything. She just sits."

                "A minute passes. Two."

                tasha "My mum's in hospital."

                "The words come out flat. Like stones."

                tasha "She's been in hospital for three months. I didn't tell anyone because — I don't know. Because if I said it out loud it would be real."

                a "I'm sorry."

                tasha "She's got MS. They diagnosed her in January. She was fine in September and now she can't — she can't walk properly. She drops things."

                "Tasha's voice breaks."

                tasha "And I've been here being — being {i}this{/i}. This awful person. Because if I was angry at everyone else, I didn't have to be afraid."

                "Her hands are shaking."

                tasha "I know that's not an excuse. I know what I did to Zara. I know what I've been like all year."

                a "It's not an excuse. But it's a reason."

                tasha "I sent Zara a letter. A real one. I don't know if she'll read it."

                a "She might."

                tasha "I wouldn't. If I were her."

                "They sit on the bench. The campus moves around them. Students heading to exams, to the library, to the pub."

                tasha "Why are you being nice to me? After everything?"

                a "Because someone was nice to me when I didn't deserve it."

                "Tasha cries. Quietly, privately, on a bench outside the library in May sunshine."

                "Amelia doesn't touch her. She just stays."

    elif stat_mc >= 12 and rel_tasha < 3:

        "Until today."

        "Amelia walks past her on the quad. Tasha is with someone Amelia doesn't recognise — a student from another course, probably."

        "Their eyes meet."

        ## =====================================================================
        ## CHOICE 11.3B — TASHA (Anger ending)
        ## =====================================================================

        menu:
            "Tasha. After everything."

            "Let her go. You've won, but it's hollow.":
                $ ch11_tasha = "anger"
                $ add_stat("stat_mc", 1)

                "Amelia keeps walking."

                thought "I reported her. I confronted her. I stood up. And she's still here, and Zara's still hurt, and the system processed it all and nothing really changed."

                thought "Except me. I changed."

                "She doesn't look back."

    else:
        "She's a figure on the edges. Unresolved."

        $ ch11_tasha = "unresolved"

        thought "Tasha. I never dealt with Tasha. Not really."

        thought "She's still there. The cruelty is still there. And I don't know what to do with that."

        "Some stories don't end. Some shadows aren't faced. This is one of them."

    ## =====================================================================
    ## SCENE 11.5 — THE GROUP DINNER
    ## =====================================================================

    scene bg_flat_kitchen
    with dissolve

    "The last night."

    "Not the {i}last{/i} last night — exams aren't quite over. But the last night that feels like a beginning rather than an ending."

    "Raj cooks. Of course he does. A feast — his grandmother's biryani, the real recipe, the one that takes four hours and fills the flat with the smell of cardamom and saffron and something Amelia has no word for except {i}love{/i}."

    "They cook together. Liz chops onions and cries. Lucas is on rice duty. Amelia is in charge of raita, which she ruins twice before getting it right."

    if sarah_alive:
        if sarah_outcome == "full_save":
            "Sarah sends a voice note from her parents' house in Devon: her laugh, a dog barking, and 'Save me some, you monsters.'"
        elif sarah_outcome == "late_save":
            "A text from Sarah: {i}'eat some for me. i miss you all. x'{/i}"
        elif sarah_outcome == "partial_save":
            "Sarah's name hovers in the room like a frequency. Nobody says it. Everybody's thinking it."
    else:
        "They set five places. One stays empty."

        "Nobody says anything. Raj puts a small bowl of rice at the empty place. It's not a ceremony. It's just Raj."

    "The biryani is extraordinary."

    raj "My grandmother would kill me if she knew I was making this for English people."

    liz "I'm Welsh!"

    raj "That's worse!"

    lucas "I thought the secret was the yoghurt."

    raj "The secret is patience. And cumin. And love."

    a "Did you just say love?"

    raj "I said cumin."

    ## =====================================================================
    ## CHOICE 11.4 — GROUP DINNER
    ## =====================================================================

    menu:
        "The table is full. The food is good. The year is ending."

        "Be fully present — toast the year, tears and laughter.":
            $ ch11_dinner = "present"
            $ add_stat("stat_si", 1)
            $ add_rel("rel_raj", 1)
            $ add_rel("rel_liz", 1)
            $ add_rel("rel_lucas", 1)

            "She stands up."

            a "I want to say something."

            liz "Oh God, is this a speech?"

            a "It's a speech."

            raj "Is there going to be crying?"

            a "Probably."

            lucas "Just do it."

            "She looks at them. This ridiculous, beautiful collection of humans."

            a "Seven months ago I walked into this kitchen and I didn't know any of you. And now I can't imagine — I literally can't imagine — what this year would have been without you."

            "Her voice cracks slightly."

            a "Raj, you've fed me more times than my actual mother. Lucas, you've said more to me in silence than most people say in words. Liz, you are the loudest, kindest, most Welsh person I've ever met."

            liz "I'm going to cry."

            a "Me too."

            if sarah_alive:
                a "And Sarah. Who isn't here but is."
            else:
                a "And Sarah."

                "The room goes quiet."

                a "Who was here. Who is always here."

            "She raises her glass."

            a "To the kitchen. To the biryani. To us."

            "They clink. They drink. Raj is crying into the saffron rice. Nobody tells him."

        "Be there but reflective — watch the group with love.":
            $ ch11_dinner = "reflective"
            $ add_stat("stat_sd", 1)

            "She doesn't make a speech."

            "She eats. She laughs at Raj's jokes. She listens to Liz's plans for the summer. She catches Lucas's eye across the table and they share the specific look of introverts who are full of love and don't know what to do with it."

            thought "I want to remember this. The light. The smell. The sound of Raj arguing with Liz about rice. Lucas's quiet laugh. The warmth."

            thought "This is the gold. Right here. This table."

        "Skip it — can't face the goodbyes.":
            $ ch11_dinner = "skip"
            $ add_rel("rel_raj", -1)
            $ add_rel("rel_liz", -1)
            $ add_rel("rel_lucas", -1)

            "She texts Raj: {i}\"not feeling great. save me a plate? x\"{/i}"

            "She stays in her room. The sounds of dinner come through the wall — laughter, the clink of glasses, music."

            "She lies on her bed and listens to her friends being happy and tells herself this is fine."

            "Raj leaves a plate of biryani outside her door. It's still warm."

    ## =====================================================================
    ## SCENE 11.6 — CORNWALL: THE FINAL TRIP
    ## Path-dependent culmination.
    ## =====================================================================

    scene black
    with fade

    "The last weekend of term."

    "Cornwall calls."

    ## ----- HAWTHORNE PATH -----

    if mentor_path == "hawthorne":

        scene bg_cornwall_coast
        with dissolve

        "Hawthorne drives. Classic FM. No apology."

        "But they're not going to the moors this time. They cross Devon into Exeter."

        scene bg_library
        with dissolve

        "The university library at Exeter. A special collection. Hawthorne has arranged a private viewing."

        hawthorne "These are the Webber Collection manuscripts. Sixteenth-century documents relating to tin mining, land charters, and — if you look carefully — marginalia that suggest some very interesting things about the intellectual life of Tudor Cornwall."

        "The librarian brings the manuscripts in padded boxes. White gloves required."

        "Amelia puts on the gloves. She opens the first document."

        "And her breath catches."

        "The handwriting is five hundred years old. The ink is brown. The page smells of time."

        "In the margin, someone has drawn a small diagram: three circles interlocked, with a symbol in each. Salt. Mercury. Sulphur."

        hawthorne "A mining document with alchemical marginalia. Nobody knows why. Perhaps the clerk was interested. Perhaps there's more to the history of Cornish mining than meets the eye."

        ## =====================================================================
        ## CHOICE 11.5 — HAWTHORNE PATH
        ## =====================================================================

        menu:
            "Five hundred years of history in her hands."

            "Engage deeply — bridge past and present. This is what scholarship is for.":
                $ ch11_cornwall = "deep"
                $ add_stat("stat_aa", 1)
                $ add_stat("stat_sd", 1)
                $ add_rel("rel_hawthorne", 1)

                a "This is extraordinary. The marginalia — it suggests a parallel intellectual tradition running alongside the official records."

                hawthorne "Go on."

                a "The mining records are economic. Practical. But someone — the same hand, look at the ink — was thinking about transformation. Physical transformation in the mines. Spiritual transformation in the margins."

                hawthorne "And what does that remind you of?"

                a "Everything."

                "He smiles. Actually smiles."

                hawthorne "Miss James, I believe you've just described the thesis you're going to write next year."

            "Appreciate it, but feel ready to move beyond academics.":
                $ ch11_cornwall = "beyond"
                $ add_stat("stat_sd", 1)

                a "It's beautiful. But..."

                hawthorne "But?"

                a "I used to think history was about knowing things. Now I think it's about understanding why knowing things matters."

                hawthorne "That's growth."

                a "It doesn't feel like growth. It feels like confusion."

                hawthorne "Same thing, often."

    ## ----- SIMMONS PATH -----

    elif mentor_path == "simmons":

        scene bg_eden_project
        with dissolve

        "The Eden Project. A retreat day. Not for students — for wellness practitioners, volunteers, people who work in mental health."

        simmons "I run this once a year. You're my first student invite."

        "The group is twelve people. A counsellor from Truro. A GP from Penzance. A community worker from Newquay. A minister from Bodmin."

        "They sit in a circle in the Mediterranean Biome. The air is warm and thick with rosemary and lavender."

        ## =====================================================================
        ## CHOICE 11.5 — SIMMONS PATH
        ## =====================================================================

        menu:
            "The retreat is for healers. Amelia is invited to participate."

            "Lead a session — share what you've learned, help others.":
                $ ch11_cornwall = "lead"
                $ add_stat("stat_mh", 1)
                $ add_stat("stat_mc", 1)
                $ add_rel("rel_simmons", 1)

                "Simmons nods. 'Tell them about your year. Just the parts that are relevant.'"

                "Amelia stands. Twelve faces. Professionals. People who do this for a living."

                "She talks about the flat. About Sarah. About the 3am and the hospital and the corridor."

                "She talks about what she learned: that being there is not the same as fixing, and that not-fixing can be the most important thing you do."

                "A counsellor from Truro is crying."

                "The GP from Penzance says: 'That's the hardest lesson in medicine. Thank you for saying it.'"

                simmons "That's my girl."

            "Participate — receive as well as give.":
                $ ch11_cornwall = "receive"
                $ add_stat("stat_mh", 1)

                "She listens."

                "The stories are heavy and beautiful. A GP talks about her first patient death. A counsellor talks about secondary trauma. The minister talks about holding grief for a community."

                "Amelia sits in the circle and absorbs it all and realises: she's on this path. Healing people. Being with people in their worst moments. It's not what she planned. It's who she is."

    ## ----- MAYA PATH -----

    elif mentor_path == "maya":

        scene bg_cornwall_coast
        with dissolve

        "Maya drives. The van rattles. The crystals on the dashboard catch the light."

        "They arrive at dawn."

        "A stone circle. Not the Merry Maidens — smaller, less famous, tucked into a hillside that catches the first light."

        maya "The Hurlers. Three circles, not one. Nobody knows why three."

        "The stones are grey against the green. The sky is turning gold."

        maya "You know what to do."

        a "Do I?"

        maya "Sit. Be still. Let the dawn come."

        ## =====================================================================
        ## CHOICE 11.5 — MAYA PATH
        ## =====================================================================

        menu:
            "Dawn. The stone circle. Stillness."

            "Achieve genuine stillness — something shifts.":
                $ ch11_cornwall = "stillness"
                $ add_stat("stat_sd", 1)
                $ add_stat("stat_ok", 1)
                $ add_rel("rel_maya", 1)

                "She sits."

                "The ground is cold. The stone behind her is cold. The air smells of gorse and moss."

                "She closes her eyes."

                "The thoughts come — exams, Sarah, Ella, the future. She lets them pass. They come again. She lets them pass."

                "And then—"

                "Silence."

                "Not the absence of sound — the birds are singing, the wind is moving, something rustles in the grass. But an inner silence. A stillness at the centre of the turning world."

                "She stays in it. A minute. Five minutes. An eternity."

                "When she opens her eyes, the sun is up. The stones are gold."

                maya "You felt it."

                a "I felt something."

                maya "That's all there is. Something."

            "Try hard — the mind wanders, but the dawn is beautiful.":
                $ ch11_cornwall = "try"
                $ add_stat("stat_sd", 1)

                "She sits."

                "The thoughts won't stop. Exams. Deadlines. Did she reply to Ella's text?"

                "She tries. The stillness comes in fragments — three seconds here, five there."

                "But the dawn is extraordinary."

                "The sky goes from grey to gold to blazing. The stones catch the light and for a moment they look alive."

                maya "The stillness doesn't have to be perfect to be real."

                a "It was very imperfect."

                maya "So is everything worth doing."

    ## ----- ELENA PATH: THE FOGOU -----

    elif mentor_path == "elena":

        scene bg_cornwall_coast
        with dissolve

        "Elena drives. No music. Just the road and the sound of the engine."

        elena "Dydh da. Are you ready?"

        a "For what?"

        elena "An gwella. The sight. The underground place."

        "Amelia's stomach tightens."

        a "You said you'd take me. In February."

        elena "I said I'd take you when you were ready. You're ready."

        "They drive through the May countryside — hedgerows loud with birdsong, fields of bluebells, the sky enormous and blue."

        "Carn Euny."

        "An ancient settlement. Iron Age — two thousand years old. Stone walls, ruined houses, a village that existed before Rome came to Britain."

        "And beneath it: the Fogou."

        scene bg_fogou_entrance
        with dissolve

        "The entrance. A low, dark passage into the earth."

        elena "This is a fogou. An underground chamber. Nobody knows what they were for — storage, ritual, refuge. Perhaps all three."

        "She lights a candle. Hands it to Amelia."

        elena "You go in alone."

        a "Alone?"

        elena "The Work is done alone. The athanor is sealed. The fire is inside."

        "She touches Amelia's cheek."

        elena "I'll be here when you come out. Meur ras. Thank you. For trusting the fire."

        "Amelia takes the candle."

        "The entrance is narrow. She has to crouch. Then crawl. The stone is cold under her hands."

        "The darkness swallows her."

        # --- SONG SLIDESHOW: "Between the Veil" — Fogou, mystical threshold ---
        call slideshow_ch11_between_the_veil

        ## =====================================================================
        ## THE FOGOU SCENE — KARMA DICE
        ## =====================================================================

        python:
            fogou_roll = renpy.random.randint(1, 20) + int(stat_ok / 2) + int(stat_sd / 3)

        if fogou_roll >= 25:

            ## TRANSCENDENT ENCOUNTER — the game's most profound scene.

            "The passage opens into the chamber."

            "She stands. The ceiling is just above her head. The candle flickers."

            "And then the candle goes out."

            "Darkness. Complete. The kind of dark that has weight."

            "She should be afraid."

            "She isn't."

            "Something is in the chamber with her."

            "Not a sound. Not a shape. A {i}presence{/i}. Like standing in a room where someone has just been — the warmth they left behind, the air they displaced."

            "She can't see anything. She can feel everything."

            "The year unfolds."

            "Not as memory — as something more like a map, seen from above. London (black). The train (grey). Plymouth (white). Cornwall (gold). The ordeal (fire). And now — this place. This darkness that is also light."

            "The presence speaks, if 'speaks' is the right word. It's not a voice. It's the shape of a thought that isn't hers."

            thought "You came through the fire."

            thought "Yes."

            thought "You are not the same."

            thought "No."

            thought "Are you ready to go back?"

            thought "I was always going back. But now I know what I'm bringing with me."

            "The candle relights."

            "She didn't touch it."

            "The chamber is empty. Stone walls. Low ceiling. Nothing else."

            "But the air is different. Warmer. Thick with something that smells like copper and earth and — is that rose? In a cave?"

            "She crawls out."

            "The sunlight hits her like a benediction."

            "Elena is sitting by the entrance. She looks at Amelia. Her face changes."

            elena "You saw it."

            a "I don't know what I saw."

            elena "You don't have to know. You will. Later. When you're ready."

            "Amelia looks at the sky. It is extraordinary — the blue is deeper, the light sharper, as though someone has adjusted the settings on reality."

            elena "Welcome home."

        elif fogou_roll >= 18:

            ## ALCHEMICAL VISIONS — her year mapped to the Magnum Opus.

            "The chamber."

            "She stands in the dark. The candle is small. The walls are close."

            "She breathes."

            "And the walls change."

            "Not physically — she's a psychology student, she knows what exhaustion and darkness and suggestion do to the mind. But the stone seems to shimmer. Colours move across the surface like oil on water."

            "Black. The Thames at night. Her suitcase. The bookshop with its bell."

            "White. Plymouth in the rain. Snow on the Hoe. Simmons' plants."

            "Yellow. The hospital lights. The fire. The waiting room."

            "Red. Now. This. The stone. The dark. The candle."

            "She sees the pattern. The pattern that was always there."

            thought "Nigredo. Albedo. Citrinitas. Rubedo."

            thought "I didn't learn these words. I didn't need to. I lived them."

            "The colours fade. The stone is stone again. The candle is a candle."

            "She crawls out."

            "Elena is waiting."

            elena "What did you see?"

            a "My year. In colours."

            elena "The stages."

            a "You could have just told me."

            elena "Would you have believed me?"

            a "...No."

            elena "That's why the Fogou exists."

        elif fogou_roll >= 12:

            ## PROFOUND SILENCE — presence without content.

            "The chamber."

            "She stands. The candle burns. The stone is stone."

            "Nothing happens."

            "She waits."

            "Silence. Full, heavy, warm silence."

            "She sits on the ground. The stone is cold but not uncomfortably so. The darkness beyond the candle is total."

            "And she stays."

            "How long? She doesn't know. Long enough for the candle to burn down an inch. Long enough for the silence to stop feeling like absence and start feeling like — fullness."

            "She's not meditating. She's not thinking. She's just... here. In the oldest room she's ever been in. Underground. Alone."

            thought "This is what it feels like to not be anything. Not a student. Not a daughter. Not a friend. Not a person who failed or succeeded or made the right choice or the wrong one."

            thought "Just — here."

            "She crawls out."

            "The light is blinding."

            elena "What happened?"

            a "Nothing."

            elena "Describe the nothing."

            a "It was... full."

            elena "Good. That's good."

        else:

            ## FEAR AND CONFUSION — but Elena is outside.

            "The chamber."

            "She stands. The candle flickers. The walls are close."

            "The darkness presses."

            "Something — fear? Memory? The specific cold of underground places — hits her and she can't breathe."

            "She tries to stay. She tries."

            "But the walls are too close and the dark is too deep and the candle is too small and she's crawling out — fast, faster, scraping her knees on the stone."

            "Daylight. Air. Sky."

            "Elena is there."

            elena "Fear is information."

            a "I couldn't — I tried—"

            elena "I know."

            "She sits beside Amelia on the grass."

            elena "The Fogou doesn't always open. For some people it takes years. For some, it never opens. That doesn't mean the Work has failed."

            a "It feels like failure."

            elena "The gold was always there. An alchemist who isn't ready isn't a failed alchemist. She's an alchemist who needs more time."

        ## ALL FOGOU OUTCOMES — STAT AWARDS (same for all)
        $ add_stat("stat_ok", 2)
        $ add_stat("stat_sd", 1)
        $ add_rel("rel_elena", 1)

    ## =====================================================================
    ## SCENE 11.7 — THE RESURRECTION TEST
    ## The internal reckoning. All paths converge.
    ## =====================================================================

    scene bg_amelia_room_plymouth_night
    with dissolve

    "Night. Her room. The last week of term."

    "Everything is slowing down. The exams are done — or nearly. The flat is starting to empty around the edges: posters coming down, boxes appearing, the gradual stripping-back that means the end."

    "Amelia lies in bed."

    "The question comes. The one she's been avoiding all year."

    thought "Who am I?"

    "Not who she was. Not who she wants to be. Who she {i}is{/i}. Now. Here. After everything."

    thought "I'm a person who walked into a room when it mattered."
    thought "I'm a person who missed chances and took others."
    thought "I'm a person who failed and kept going."
    thought "I'm a person who—"

    "The sentence doesn't finish."

    thought "The question isn't who am I. The question is: can I face what I've become without flinching?"

    ## =====================================================================
    ## CHOICE 11.6 — THE RESURRECTION TEST
    ## =====================================================================

    menu:
        "The test. The real one. Not exams — this."

        "Face it fully. Whatever her greatest fear is — look at it.":
            $ ch11_test = "face"
            $ add_stat("stat_sd", 1)
            $ add_stat("stat_mh", 1)

            thought "I'm afraid of not being enough."

            "There it is. The thing under everything. Under the studying and the overthinking and the performing competence."

            thought "I'm afraid that if I stop trying, if I stop proving myself, if I'm just... me... that's not enough."

            "She lets it sit."

            thought "And I need to face the possibility that it's true. That I'm not enough. That I'll never be enough. That 'enough' is a goalpost I keep moving."

            "The fear is enormous."

            "And she sits with it."

            "It doesn't eat her."

            thought "I'm not enough. And I'm here. And those two things coexist. And the universe hasn't collapsed."

            "She breathes."

            thought "Maybe enough isn't the point. Maybe the point is just... continuing."

        "Face it with support — bring a friend, mentally. Don't do this alone.":
            $ ch11_test = "supported"
            $ add_stat("stat_si", 1)
            $ add_stat("stat_mh", 1)

            thought "I can't do this alone."

            "She thinks of Raj in the kitchen. Liz's hand on hers. Lucas's silence. Ella's voice on the phone."

            if sarah_alive:
                thought "Sarah, in the hospital, saying: 'Why did you come?'"
                thought "Because friends don't leave."
            else:
                thought "Sarah. Who left. Who didn't mean to leave the way she did."
                thought "Who taught me that showing up is the only thing that matters."

            thought "My greatest fear is being alone with this. So I choose not to be."

            "She texts Ella:"

            "{i}amelia: i'm having a moment. can you just talk to me? about anything. just need your voice.{/i}"

            "Ella calls within thirty seconds."

            ella "Okay. So. I saw a dog today that looked like a Renaissance painting—"

            "Amelia laughs. And cries. And both at once."

        "Avoid it. Survive rather than transform.":
            $ ch11_test = "avoid"

            "She puts on her headphones. She opens Netflix."

            "The question dissolves into noise."

            thought "Not tonight. Not now."

            "She watches three episodes of something she won't remember."

            "The question will come back. Questions like this always do."

    ## =====================================================================
    ## SCENE 11.8 — RED DAWN
    ## The chapter's final image.
    ## =====================================================================

    scene bg_plymouth_hoe_dawn
    with dissolve

    "The last morning."

    "She wakes before dawn. Not by alarm — her body knows."

    "She walks to the Hoe."

    "The sky is turning."

    "Red."

    "The reddening. Rubedo. She doesn't know the word — or maybe she does, somewhere, in the part of her that reads books in dusty shops and sits in stone circles and crawls into underground chambers."

    "The sun rises over Plymouth Sound. The water is gold. The Drake memorial is black against the sky."

    "She stands at the railing."

    thought "I came here in September. I stood here. I didn't know anything."

    thought "I still don't know anything. But I know I don't know it. And I know how to stand here. And I know how to love the people I love. And I know how to sit in the dark."

    thought "Is that enough? Is that the gold?"

    "The sun crests the horizon. The light pours. Everything is red and gold."

    thought "I think it might be."

    # --- SONG SLIDESHOW: "The_Work" — Red Dawn, Rubedo, the climax ---
    call slideshow_ch11_the_work

    ## -----------------------------------------------------------------------
    ## END OF CHAPTER
    ## -----------------------------------------------------------------------

    $ complete_chapter(11)
    scene black
    with fade

    centered "{size=+6}End of Chapter Eleven{/size}"
    pause 2.0

    return
