###############################################################################
##
##  CHAPTER 6: TESTS, ALLIES, AND ENEMIES
##
##  Hero's Journey: The hero faces challenges, identifies friends and foes.
##  Alchemical Stage: Albedo continued — separation of pure from impure.
##  Month: December–January. Location: Plymouth + London (Christmas).
##  Palette: White and grey. Frost. Bare branches. Fairy lights.
##  Music: Tension and warmth alternating. Christmas songs in the distance.
##
##  Scenes: 9 + 1 conditional | Choices: 7 + 1 conditional
##  Max earnable: ~10–12 pts
##
###############################################################################

label chapter_6:

    stop music fadeout 1.0
    scene black
    with fade

    ## -----------------------------------------------------------------------
    ## TITLE CARD
    ## -----------------------------------------------------------------------

    centered "{size=+20}Chapter Six{/size}\n\n{size=+6}Tests, Allies, and Enemies{/size}"
    pause 3.0

    ## =====================================================================
    ## SCENE 6.1 — TASHA'S ESCALATION
    ## She's moved from nasty to sustained. It's targeted. It's Zara.
    ## =====================================================================

    scene bg_campus_quad
    with dissolve

    # play music "audio/ch6_tension.ogg" fadein 2.0 volume 0.5

    "It starts slowly, the way fires do."

    "Week eight. A photo on Tasha's Instagram story — Zara from behind in the library, captioned with something that's technically not racist, technically not bullying, technically fine. The kind of caption that makes you feel sick and then doubt whether you're right to feel sick."

    "Forty-seven likes."

    "Week nine. Graffiti in the bathroom on the second floor. A name and a word. The word has been scrubbed off by the time Amelia sees it, but the ghost of it is still there — white paint over wet marker, the edges bleeding through."

    "Week ten. A formal complaint filed with the student union. Anonymous. Against Zara. Alleging 'intimidating behaviour' and 'aggressive communication style.'"

    "Zara reads the complaint. Her hands shake."

    zara "This is — this is made up. I never — I've never been aggressive to anyone, I've literally never—"

    "Amelia reads it too. The language is careful, legalistic, the kind of precision that comes from someone who understands exactly where the line is and has learned to weaponise it."

    thought "This is Tasha."

    "Everyone knows it's Tasha. Nobody can prove it."

    "Zara is not okay."

    zara "I came here to learn, Amelia. That's it. I came here to study and get my degree and go home and make my mum proud. I didn't come here to be {i}this{/i}."

    "She looks at Amelia."

    zara "What do I do?"

    ## =====================================================================
    ## CHOICE 6.1 — TASHA / ZARA CONFLICT
    ## =====================================================================

    menu:
        "Zara's question hangs in the air. There are no safe answers."

        "Confront Tasha directly.":
            $ ch6_tasha = "confront"
            $ add_stat("stat_mc", 2)
            $ add_rel("rel_zara", 1)
            $ add_rel("rel_tasha", 1)

            "She finds Tasha in the student union café. She's with two friends — the entourage kind, the kind that laugh when she raises her eyebrows."

            a "Can I talk to you? Alone."

            "Tasha looks at her. A calculation, rapid and precise."

            tasha "Sure."

            "They walk outside. December air. Their breath making ghosts."

            a "I know it's you. The photo. The graffiti. The complaint."

            tasha "I don't know what you're talking about."

            a "Tasha. You know exactly what I'm talking about."

            "Silence."

            a "Zara has done nothing to you. Nothing. And you're destroying her because — what? Because you can? Because hurting someone who can't fight back makes you feel powerful?"

            "Something flickers across Tasha's face. Not remorse — something underneath it. Fear, maybe. Or recognition."

            tasha "Stay out of it, Amelia."

            a "No."

            "Tasha stares at her. Then walks away."

            "The graffiti doesn't come back. The formal complaint is quietly withdrawn a week later. Tasha doesn't speak to Amelia for the rest of term."

            "That's fine."

            "What Amelia doesn't see: Tasha, in her room that night, staring at the ceiling. Because nobody has ever said it to her face before. And it landed."

        "Report it to university administration.":
            $ ch6_tasha = "report"
            $ add_stat("stat_mc", 1)
            $ add_rel("rel_zara", 1)

            "Amelia goes to the student welfare office. She brings screenshots, dates, the text of the formal complaint."

            "The administrator is sympathetic. The process is slow."

            "A formal investigation is opened. Three weeks later, Tasha receives a 'warning letter.' The complaint against Zara is dismissed."

            "Zara is relieved."

            zara "Thank you. For believing me."

            a "Of course I believed you."

            "But the process left bruises. Three weeks of formal language and review panels and the feeling that the system was designed for the person accused, not the person harmed."

            thought "I did the right thing. I think I did the right thing. But it shouldn't be this hard to do the right thing."

        "Support Zara privately, but don't act publicly.":
            $ ch6_tasha = "private"
            $ add_stat("stat_si", 1)
            $ add_rel("rel_zara", 1)

            a "I'm with you. Whatever you need."

            "They spend the evening together. Amelia makes tea. Zara talks. Then doesn't talk. Then talks again."

            "Amelia walks her to the welfare office the next morning. Sits outside while Zara goes in."

            "But she doesn't confront Tasha. She doesn't report it herself."

            "The complaint drags on. Zara fights it alone, administratively."

            "She wins. But it costs her."

            "Later:"

            zara "You were there for me. That mattered."

            "A pause."

            zara "But I wish someone had stood up. In public. Where it counts."

        "Stay out of it.":
            $ ch6_tasha = "nothing"
            $ add_rel("rel_zara", -1)

            thought "It's not my fight. I've got my own problems. Zara's strong — she can handle it."

            "She tells herself this."

            "She tells herself this while the graffiti stays up for three days. While the complaint grinds through the system. While Zara stops coming to the kitchen."

            "Raj corners Amelia one evening."

            raj "She needed you. You know that, right?"

            "Amelia looks away."

    ## =====================================================================
    ## SCENE 6.2 — SARAH'S ROOM
    ## She's missed two weeks of lectures. Texts are short.
    ## =====================================================================

    scene bg_halls_corridor
    with dissolve

    # play music "audio/ch6_sarah.ogg" fadein 2.0 volume 0.3

    "It's Raj who says it."

    raj "Has anyone seen Sarah?"

    "The kitchen goes quiet."

    liz "She was at the lecture on Monday. Wait — no. Tuesday? I'm not sure."

    lucas "I texted her yesterday. She said she was fine."

    raj "She always says she's fine."

    "A pause."

    raj "When was the last time anyone saw her outside her room?"

    "Nobody answers. The silence has a shape — the shape of something they all should have noticed sooner."

    ## =====================================================================
    ## CHOICE 6.2 — SARAH CHECK-IN
    ## =====================================================================

    menu:
        "Sarah. Room 22. Second floor. The door that's always closed."

        "Go to her room. Knock. Don't leave.":
            $ ch6_sarah = "knock"
            $ add_stat("stat_mh", 1)
            $ add_stat("stat_si", 1)
            $ add_rel("rel_sarah", 2)
            $ sarah_room_visited = True

            scene bg_halls_corridor
            with dissolve

            "She walks down the corridor. Her hand is shaking. She doesn't stop."

            "Knock. Knock. Knock."

            a "Sarah? It's Amelia. I'm not going away."

            "Silence."

            "She waits. Thirty seconds. A minute."

            a "I don't need you to open the door. I just need you to know I'm here."

            "Another minute."

            "The lock turns."

            "The door opens."

            "What's inside:"

            "Curtains closed. Dishes on the desk — unwashed, days old. An untouched textbook. The bed unmade in a way that suggests it hasn't been properly slept in, just lain on. Clothes on the floor."

            "And Sarah. On the bed. In yesterday's clothes. Or the day before's."

            "She looks at Amelia. Her eyes are red but dry — the kind of red that comes after the tears have run out."

            "Amelia doesn't react to the room. She doesn't adjust her expression. She's read enough of Simmons' material to know that the worst thing you can do is look shocked."

            a "Can I sit down?"

            "Sarah nods."

            "Amelia sits on the edge of the bed. She doesn't touch her. Doesn't try to fix it. Doesn't say any of the things people say — 'It'll be okay', 'Have you tried...', 'You just need to...'."

            "She sits."

            "Forty-five minutes. They barely speak."

            "Then:"

            sarah "I think I need help."

            a "Okay. Let's figure that out."

            "The words are quiet. But they mean everything."

        "Text her: \"I'm here if you need me.\"":
            $ ch6_sarah = "text"
            $ add_stat("stat_si", 1)
            $ add_rel("rel_sarah", 1)

            "{i}hey sarah. not seen you in a while. i'm here if you need me. no pressure. just wanted you to know x{/i}"

            "The reply comes four hours later."

            "{i}sarah: thanks. just having a rough patch. i'll be okay x{/i}"

            thought "'I'll be okay.' The future tense. Not 'I'm okay' — 'I'll be okay.' As if okay is somewhere she hasn't arrived yet."

            "Amelia stares at the message."

            thought "Is that enough? Is a text enough?"

            "She sends one more:"

            "{i}kitchen tomorrow? raj is doing pasta. you don't have to stay long x{/i}"

            "No reply."

        "Mention concern to counselling services.":
            $ ch6_sarah = "counselling"
            $ add_stat("stat_mc", 1)
            $ add_rel("rel_sarah", 1)

            "The counselling office. A poster on the wall: {i}It's okay not to be okay.{/i}"

            "The receptionist is kind. Professional."

            a "I have a friend. A flatmate. She's been missing lectures and I'm worried about her."

            "They take the details. They'll 'reach out.'"

            thought "I did the right thing. I think."

            "A week later, Amelia sees a counsellor in the halls corridor. Coming from the second floor."

            thought "Did they reach out? Did Sarah let them in?"

            "She doesn't know. The system is working. Or it isn't. And from the outside, there's no way to tell."

        "Assume she's busy. Don't follow up.":
            $ ch6_sarah = "nothing"
            $ add_rel("rel_sarah", -1)

            "She'll be fine. She's probably just stressed. Everyone's stressed. It's December."

            "Amelia sends a group text about a kitchen dinner. Sarah doesn't reply."

            "She tells herself this is normal."

            thought "She's fine. She said she was fine."

    ## =====================================================================
    ## SCENE 6.3 — LUCAS AT 3AM
    ## The kitchen. The real conversations happen in the dark.
    ## =====================================================================

    scene bg_kitchen_halls
    with dissolve

    # play music "audio/ch6_3am.ogg" fadein 2.0 volume 0.3

    "3:17am."

    "Amelia can't sleep. She pads to the kitchen for water and finds Lucas at the table with a mug of tea that's long gone cold."

    "He's staring at his phone. The screen is off."

    a "Hey."

    lucas "Hey."

    "She sits."

    "The kitchen at 3am is a different country. The fluorescent lights are off — just the under-cabinet LEDs, pale blue, casting everything in submarine light."

    a "Can't sleep?"

    lucas "Not really."

    "Silence. The fridge hums."

    lucas "My dad called."

    "He says it the way you'd say 'the weather's changed.' Factual. But underneath — a tremor."

    lucas "He does this. Once every four or five months. Calls at midnight because he's forgotten I'm in a different time zone. Or he hasn't forgotten — he's just drunk and the timezone doesn't matter."

    "He pushes the cold tea aside."

    lucas "He wanted to tell me he's proud of me. Which would be nice if it wasn't the first time he's said it in two years. And if he could remember what I'm studying."

    a "Lucas..."

    lucas "He said psychology. He said 'I hear you're in London studying psychology.' And I said 'Dad, I'm in Plymouth.' And he said 'Same thing.'"

    "A pause."

    lucas "It's not the same thing."

    ## =====================================================================
    ## CHOICE 6.3 — LUCAS AT 3AM
    ## =====================================================================

    menu:
        "3am. The kitchen. The truth is on the table."

        "Listen deeply — ask the hard questions.":
            $ ch6_lucas = "deep"
            $ add_stat("stat_si", 1)
            $ add_stat("stat_sd", 1)
            $ add_rel("rel_lucas", 2)

            a "Does he know you at all?"

            "Lucas looks at her. Surprised by the directness."

            lucas "He knows the version he built. The one where I'm grateful for the money and I don't ask why he left and I call on his birthday and pretend the presents make up for the presence."

            "He rubs his face."

            lucas "I read all this stuff. Jung. The Father archetype. The Absent King. I can name what happened to me in seventeen different theoretical frameworks. And it doesn't help. Knowing what something is doesn't make it stop hurting."

            a "Maybe the knowing isn't supposed to make it stop. Maybe it just gives you language for the hurt. And language is how you share it."

            "He looks at her. For a long time."

            lucas "That's... that's actually the most useful thing anyone's said to me about this."

            a "I stole it from Maya."

            lucas "I know. She said the same thing to me last term. It's better when you say it."

            "They talk until dawn. When the sky starts to lighten, Lucas makes fresh tea and they drink it in silence, watching the dark turn to grey."

        "Listen, but deflect with humour when it gets heavy.":
            $ ch6_lucas = "humour"
            $ add_stat("stat_si", 1)
            $ add_rel("rel_lucas", 1)

            a "To be fair, Plymouth {i}is{/i} basically London. If you squint."

            "Lucas almost smiles."

            lucas "If you squint and remove about eight million people."

            a "And the tube. And the culture. And the housing crisis."

            lucas "We have a housing crisis."

            a "Touché."

            "They talk. She listens. When it gets too close to the bone — when Lucas starts to describe the Christmas he spent alone at fourteen because his dad 'forgot' the dates — she makes a joke. Small. Kind. Enough to let him breathe."

            "He's grateful. She can tell."

            "But something stays unsaid. The conversation reaches the edge and doesn't go over."

            lucas "Thanks, Amelia."

            a "Any time."

            "She means it. But she knows, somewhere, that 'any time' isn't the same as 'right now, completely.'"

        "\"Mate, it's 3am. Can we do this tomorrow?\"":
            $ ch6_lucas = "dismiss"
            $ add_rel("rel_lucas", -1)

            a "Lucas, it's three in the morning. I can barely think. Can we talk about this tomorrow?"

            "He looks at her."

            lucas "Sure. Yeah. Tomorrow."

            "She goes back to bed."

            "Tomorrow, she catches his eye in the kitchen. He nods. Smiles."

            lucas "'Morning."

            "He doesn't bring it up again."

            "He doesn't bring it up again because he won't. Not to her. The door was open for one night and she closed it, and some doors, once closed, don't reopen."

    ## =====================================================================
    ## SCENE 6.4 — CHRISTMAS EXAMS
    ## The first real academic test.
    ## =====================================================================

    scene bg_library_study_area
    with dissolve

    # play music "audio/ch6_exams.ogg" fadein 2.0 volume 0.4

    "December. Exams."

    "The library is a battlefield. Every seat is occupied. The printers queue is twelve deep. Someone has been crying in the third-floor bathroom for three hours."

    "Amelia has four exams in five days. Developmental psychology. Statistics. Research methods. An essay on cognitive behavioural approaches that's due the day after her last exam, which feels like someone in administration is testing whether students can commit crimes of passion."

    "She studies. She makes flashcards. She colour-codes her notes (badly — Sophia's system it is not). She reads until the words swim."

    if mentor_path == "hawthorne":
        "Hawthorne sends an email: 'Don't try to know everything. Know the important things well. Everything else is furniture.'"

    elif mentor_path == "simmons":
        "Simmons texts: 'Remember to eat. Remember to sleep. The exams will still be there in the morning. ❤️'"

    elif mentor_path == "maya":
        "Maya's note under the door: 'You already know more than you think. The exam is testing whether you can access it under pressure. So breathe.'"

    elif mentor_path == "elena":
        "Elena texts: 'The alchemists called this the Test of Fire. You're supposed to feel like you're burning. It means the Work is happening.'"

    ## =====================================================================
    ## CHOICE 6.4 — CHRISTMAS EXAMS
    ## =====================================================================

    if stat_mh < 8:
        menu:
            "The exams loom. Amelia's mental health score is low."

            "Study hard. Prepare. Push through.":
                $ ch6_exams = "study"
                $ add_stat("stat_aa", 1)

                "She locks herself in the library for three days. She eats sandwiches that taste like cardboard. She drinks coffee that tastes like a grudge."

                "She passes. Not brilliantly. But she passes."

                thought "I survived. That's not the same as excelling. But right now, survival is enough."

            "Cram at the last minute. Hope for the best.":
                $ ch6_exams = "cram"

                "She tries. She really does. But the material slips through her fingers like water."

                "She passes two out of four on the first attempt. The others will need resits in January."

                thought "I should feel worse about this. The fact that I don't is either growth or apathy. I genuinely can't tell."

            "Too overwhelmed to study properly.":
                $ ch6_exams = "overwhelmed"
                $ add_stat("stat_mh", -1)

                "She sits in front of her notes. The words are there. She can see them. She cannot make them mean anything."

                "The panic comes back — not the full attack, but its shadow. The feeling that the world is slightly too loud and slightly too close."

                "She passes one exam. The rest are blank enough to require resits."

                thought "I'm failing. Not just the exams. I'm failing at the thing I came here to do and I don't know how to stop it and I can't ask for help because asking for help means admitting I can't cope and I—"

                "She stops."

                thought "Breathe."
    else:
        menu:
            "The exams arrive. Amelia is ready."

            "Study hard. Prepare. Do well.":
                $ ch6_exams = "study"
                $ add_stat("stat_aa", 1)

                "She's prepared. Not over-prepared — Simmons warned her about that — but solidly, genuinely prepared."

                "She sits in the exam hall. She reads the questions. She knows the answers — not all of them, but enough."

                "She writes."

                "When she comes out, the December air hits her face. Cold. Clean."

                thought "I did that. I actually did that. I'm not Sophia — I didn't ace it. But I didn't just survive it either. I... did it well."

            "Cram at the last minute. Scrape through.":
                $ ch6_exams = "cram"

                "She meant to start earlier. She always means to start earlier."

                "Two days before the first exam, she discovers she has opinions about developmental psychology. That helps. You can bullshit your way through a lot if you have genuine opinions."

                "She scrapes through. Not elegant. But through."

    ## =====================================================================
    ## SCENE 6.5 — CHRISTMAS AT HOME
    ## London. Family. The familiar made strange.
    ## =====================================================================

    scene bg_family_home
    with dissolve

    # play music "audio/ch6_christmas.ogg" fadein 2.0 volume 0.4

    "Home."

    "The house smells the same. Ginger and pine and the specific lavender fabric softener Grace has used since the nineties. Lily has put fairy lights around everything includingthe cat."

    "Christmas Day is loud and warm and exactly as it's always been: Grace in the kitchen performing a three-hour symphonic cooking event; David hovering, being shooed away, hovering again; Lily on her phone, periodically forced to set the table."

    "And Amelia. Home. But not quite home. Standing in the kitchen that made her, feeling like a guest."

    grace "You're thin."

    a "I'm not thin, Mum."

    grace "You're thin and you have bags under your eyes and you're drinking wine, which you didn't used to do."

    a "I'm a university student. Wine is basically part of the curriculum."

    david "Leave her alone, Grace."

    grace "I'm not doing anything! I'm observing! I'm a {i}mother{/i}, I'm allowed to observe!"

    "After dinner. The living room. David is asleep in the chair. Lily has retreated upstairs. Grace is washing up — she insists on it, always, as though the dishwasher is a personal insult."

    "Amelia dries."

    grace "So. How is it? Really?"

    "The question. The real one. Grace doesn't look at her — she watches the water, the soap, her hands. But she's listening with her entire body."

    ## =====================================================================
    ## CHOICE 6.5 — CHRISTMAS AT HOME — TALKING TO PARENTS
    ## =====================================================================

    menu:
        "Grace is waiting. The plates are an excuse."

        "Honest: \"It's been harder than I expected.\"":
            $ ch6_christmas = "honest"
            $ add_stat("stat_mh", 1)

            a "It's been harder than I expected, Mum."

            "Grace stops washing."

            a "Not bad. Not all bad. I've got good friends and I love the course. But I had a panic attack in the library and there's a girl who bullies people and my friend — my friend Sarah — she's not doing well, and I don't know how to help her."

            "Grace turns around. Her eyes are wet."

            grace "Why didn't you tell me?"

            a "Because I wanted to handle it. Because telling you means it's real."

            "Grace puts down the washing-up gloves. She pulls Amelia into a hug — the kind of hug that smells of ginger and washing-up liquid and the specific warmth of a mother who is frightened and fierce in equal measure."

            grace "It is real. And you don't have to handle it alone. That's not what being grown-up means."

            "Later, David finds Amelia on the stairs. He sits beside her. He doesn't hug — he's not a hugger. He puts his hand on her shoulder."

            david "Your mum told me."

            a "I'm okay, Dad."

            david "I know you are. But I want you to know: if you need to come home, even for a weekend, even for a day — you come home. That's what home is for."

        "Performance: \"Everything's great!\"":
            $ ch6_christmas = "perform"

            a "It's brilliant, Mum! The course is great, the friends are great, Plymouth is — well, it's Plymouth, but it's growing on me."

            "Grace looks at her."

            grace "I believe the Plymouth part."

            a "Honestly, Mum. I'm fine."

            "Grace goes back to washing up. She doesn't push. But something in the kitchen dims — the temperature of the honesty drops a degree."

            thought "She knows I'm performing. She knows and she's letting me because she's always believed that I have the right to my own privacy, even when I'm using my privacy to hide."

        "Deflect: talk about friends, places, not feelings.":
            $ ch6_christmas = "deflect"
            $ add_stat("stat_si", 1)

            a "Oh, you'd love it. My friend Raj cooks the best daal you've ever tasted. And there's this girl Maya who's genuinely the most fascinating person I've ever met. And the Hoe — the promenade, Mum, not the—"

            grace "I know what the Hoe is!"

            "They laugh. Amelia tells stories. The flatmates, the lectures, the Cornwall trip. She makes it sound easy and warm and exactly what a mother wants to hear."

            "Grace is smiling. But—"

            grace "And you? How are {i}you{/i}?"

            a "I'm part of all of that, Mum. That's how I am."

            "It's not a lie. It's also not the whole truth."

    ## =====================================================================
    ## SCENE 6.6 — ELLA DURING CHRISTMAS
    ## =====================================================================

    scene bg_london_cafe
    with dissolve

    "Ella. Message received: three crying-laughing emojis and a location pin."

    ## =====================================================================
    ## CHOICE 6.6 — ELLA DURING CHRISTMAS
    ## =====================================================================

    menu:
        "Christmas break. Ella. The anchor."

        "Proper meet-up — long, honest conversation.":
            $ ch6_ella = "meet"
            $ add_stat("stat_si", 1)
            $ add_rel("rel_ella", 1)

            "They meet at a café in Bromley. Ella arrives seventeen minutes late, out of breath, carrying three bags of Boxing Day sales."

            ella "I'M HERE. DON'T START WITHOUT ME."

            a "Start what?"

            ella "The emotional reunion. I've rehearsed it."

            "They order coffee. Ella orders cake. Then more cake. Then a third slice because 'it's Christmas.'"

            "And they talk."

            "Not the surface talk — not the 'how's uni' talk. The real talk. Amelia tells Ella about the panic attack, about Sarah, about the mentor trip, about the feeling that she's becoming someone she didn't plan to be."

            ella "That's not scary. That's the whole point."

            a "Of what?"

            ella "Of leaving. You left so you could become someone who wasn't just Amelia-from-Bromley. And you have. And it's scary because becoming means the old version has to die a bit."

            "Amelia stares at her."

            a "When did you get wise?"

            ella "I've always been wise. You just didn't notice because of my incredible fashion sense and sparkling personality."

            "They stay for three hours. They laugh until crying. It's the best afternoon Amelia has had in months."

        "Quick coffee — both busy.":
            $ ch6_ella = "quick"

            "They get coffee. Forty minutes. It's warm and fond and slightly rushed."

            ella "We need to do this properly next time."

            a "We will."

            "They both know they won't."

        "Don't manage to meet up at all.":
            $ ch6_ella = "miss"
            $ add_rel("rel_ella", -1)

            "They text. They make plans. The plans fall through — family commitments, work shifts, the gravitational pull of sofas during the dead days between Christmas and New Year."

            "{i}ella: next time for sure!!! miss you ❤️{/i}"

            "{i}amelia: miss you too. definitely next time ❤️{/i}"

            thought "We used to see each other every day. Now 'next time' is a promise that keeps getting smaller."

    ## =====================================================================
    ## SCENE 6.7 — MIDWINTER OCCULT (Conditional)
    ## Only triggers if OK ≥ 4 AND (Elena mentor OR Maya rel ≥ 3)
    ## =====================================================================

    if stat_ok >= 4 and (mentor_path == "elena" or rel_maya >= 3):

        scene bg_cornwall_night
        with dissolve

        # play music "audio/ch6_midwinter.ogg" fadein 3.0 volume 0.3

        "December 21st. The shortest day. The longest night."

        if mentor_path == "elena":
            "Elena's text arrives at sunset."

            "{i}elena: midwinter. the longest dark. some traditions mark it. madron. tonight. if you're ready.{/i}"

            "No explanation. No itinerary. That's Elena — she gives you enough to choose and not enough to be safe."

        else:
            "Maya mentions it during a group dinner, oblique and casual, like dropping a pebble into water."

            maya "The solstice is tonight. Some people mark it. Light fires, stay up all night, watch the dawn. It's the oldest human ritual — facing the darkest night and trusting the light returns."

            "She catches Amelia's eye."

            maya "There's a group. In Cornwall. If you're interested."

        ## =====================================================================
        ## CHOICE 6.7 — MIDWINTER SOLSTICE
        ## =====================================================================

        menu:
            "The longest night. An invitation into the dark."

            "Participate fully.":
                $ ch6_midwinter = "full"
                $ add_stat("stat_ok", 2)

                if mentor_path == "elena":
                    $ add_rel("rel_elena", 1)
                    $ elena_key_midwinter = True

                    "She goes."

                    "Madron. The holy well in the woods. She's been here before — but not at night, and not like this."

                    "Elena has lit candles. Dozens of them, in jars, lining the path through the trees. The effect is extraordinary — a trail of light through the darkness, each flame a warm breath against the cold."

                    "Other people are there. Quiet. Standing in the ruined baptistry by candlelight. Not chanting, not praying — just standing."

                    elena "Dydh da, Amelia."

                    a "It's night."

                    elena "In Cornish, 'dydh da' is also a greeting for moments that matter. Day or night."

                    "They stand by the water. The candles flicker. The stars are out — fierce, mid-winter stars, the kind you forget exist until the city falls away."

                    elena "Tonight we sit with the dark. Not to defeat it — to understand it. The dark isn't the absence of light. It's the condition from which light emerges."

                    "The hours pass. Tea from a thermos. Silence. The occasional sound of someone moving in the trees. The water running, always running."

                    "At dawn — grey, then pale, then gold — Elena speaks."

                    elena "Meur ras. Thank you. For being here."

                    "Amelia doesn't speak. She doesn't need to."

                    thought "I've been in the Nigredo all term. I didn't know it had a name. But this — this watching, this waiting, this trust that the light returns — this is the Albedo. The whitening. I can feel it."

                else:
                    $ add_rel("rel_maya", 1)

                    "They drive to Cornwall in someone's borrowed van. Six people. Maya. Two others Amelia doesn't know. A woman with long grey hair who says nothing the entire journey."

                    "A hilltop. A fire, small but bright. Stars."

                    "They sit in a circle. Nobody speaks for the first hour. The fire crackles. The cold is absolute."

                    "Maya takes her hand."

                    maya "This is the oldest night. Everything that's been building — the learning, the crisis, the growth — it's all been the darkening. And now we sit in the bottom of it and wait."

                    "At dawn: a single line of light on the eastern horizon. The group stands. Someone plays a drum — soft, rhythmic, like a heartbeat."

                    thought "I understand something I didn't understand before. I can't articulate it. It's bigger than language."

            "Observe, but don't engage.":
                $ ch6_midwinter = "observe"
                $ add_stat("stat_ok", 1)

                if mentor_path == "elena":
                    "She goes. She watches. She stands at the edge."

                    "The candles, the water, the silence — it's beautiful. But she can't let go. Can't let her weight settle into the moment."

                    elena "You're thinking."

                    a "Isn't that the point?"

                    elena "No."

                else:
                    "She goes. She sits at the edge of the circle. She watches."

                    "It's beautiful. And strange. And she's not quite part of it."

                    maya "It's okay to be on the edge. That's where doors are."

            "Decline.":
                $ ch6_midwinter = "decline"

                if mentor_path == "elena":
                    "{i}amelia: i can't tonight. sorry. merry christmas.{/i}"

                    "{i}elena: the light returns whether you watch it or not. meur ras.{/i}"

                else:
                    a "I think I'll pass. Thanks, Maya."

                    maya "No worries."

                    "She smiles. But the invitation won't come again. Not like this. Not at the turning of the year."

    else:
        $ ch6_midwinter = "none"

    ## =====================================================================
    ## SCENE 6.8 — RETURN TO PLYMOUTH
    ## January. The new term begins.
    ## =====================================================================

    scene bg_plymouth_hoe_day
    with dissolve

    "January."

    "She comes back. The Tamar Bridge again. Plymouth in winter — grey and gleaming, the sea like hammered metal."

    "The room is as she left it. Her books. Her notes. The dried leaf. The photo of the group on the coast."

    "But something's shifted."

    "The group reconvenes in the kitchen. Raj cooks. Of course Raj cooks."

    "Liz has a new haircut and a story about her nan who is recovering. Lucas has a stack of new books. Maya has been in India for two weeks and has a henna pattern on her hands and a brightness in her eyes. Zara is wearing a cardigan her grandmother knitted and it is enormous and wonderful."

    if ch6_sarah == "knock":
        "Sarah comes. She's thinner. She's quieter. But she comes."

        "She sits at the table. Raj puts a plate in front of her."

        raj "Eat."

        "She eats."

        "It's not fixed. But she's here."
    elif ch6_sarah == "text" or ch6_sarah == "counselling":
        "Sarah texts: {i}back in plymouth. sorry i was weird last term. going to try harder this term x{/i}"

        thought "'Try harder.' As if she owes us effort. As if healing is a performance for other people."
    else:
        "Sarah's room is dark. She came back — her name's still on the door. But the light is off."

    "Term two. The second act. The approach to whatever's coming."

    ## -----------------------------------------------------------------------
    ## END OF CHAPTER
    ## -----------------------------------------------------------------------

    scene black
    with fade

    centered "{size=+6}End of Chapter Six{/size}"
    pause 2.0

    return
