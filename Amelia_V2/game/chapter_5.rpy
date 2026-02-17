###############################################################################
##
##  CHAPTER 5: CROSSING THE THRESHOLD
##
##  Hero's Journey: The hero commits to the adventure; the unfamiliar world.
##  Alchemical Stage: Albedo — purification, separation, gaining clarity.
##  Month: November–December. Location: Plymouth.
##  Palette: Grey-white. Clean lines. Occasional sunbreaks.
##  Music: Rhythm established. Study playlists. Rain on windows. Laughter.
##
##  Scenes: 7 + 1 conditional | Choices: 5 + 1 dice + 1 conditional
##  Max earnable: ~8–10 pts
##
###############################################################################

label chapter_5:

    $ current_chapter = 5
    stop music fadeout 1.0
    scene black
    with fade

    ## -----------------------------------------------------------------------
    ## TITLE CARD
    ## -----------------------------------------------------------------------

    centered "{size=+20}Chapter Five{/size}\n\n{size=+6}Crossing the Threshold{/size}"
    pause 3.0

    ## =====================================================================
    ## SCENE 5.1 — ACADEMIC RHYTHM
    ## November. Amelia finds her groove.
    ## =====================================================================

    scene bg_psych_building_lecture
    with dissolve

    # play music "audio/ch5_rhythm.ogg" fadein 2.0 volume 0.4

    "November. The clocks have gone back. The mornings are dark and the evenings arrive at four o'clock, sudden and final, like a verdict."

    "But something has changed."

    "Amelia has a routine now. She didn't plan it — it assembled itself, the way a language assembles once you've learned enough words."

    "Monday: 9am lecture with Hawthorne. Developmental psychology. He's terrifying and brilliant."
    "Tuesday: study group in the library. Lucas always early. Sophia always earlier."
    "Wednesday: Simmons' seminar, which is less a seminar and more a conversation that happens to have a reading list."
    "Thursday: free. She spends it in the library or walking the Hoe."
    "Friday: statistics lab. The one module that makes her want to cry into a spreadsheet, but Raj has a gift for turning equations into stories and he explains things at exactly the right speed."

    "She reads. She takes notes. She writes essays that are getting better — not brilliant, not yet, but better in a way she can feel. The sentences are tighter. The arguments hold."

    if mentor_path == "hawthorne":
        "Hawthorne's feedback is still brutal, but she's beginning to hear the structure underneath. Every criticism is a direction. Every 'This isn't good enough' is followed, eventually, by a very specific instruction about how to make it good enough."

    elif mentor_path == "simmons":
        "Simmons checks in weekly. Not about essays — about Amelia. 'How's your sleep? Have you been outside today? Have you eaten something that isn't toast?' The care is so persistent it starts to feel like a safety net."

    elif mentor_path == "maya":
        "Maya has started leaving articles under her door — not from journals, but from obscure websites and old magazines. 'Read this,' a Post-it says on one. 'Then sit with it.' No deadlines. No assessment. Just the invitation to think differently."

    elif mentor_path == "elena":
        "Elena texts occasionally. Brief, strange, precise. 'Look at the sky at 4:17 today.' 'The word for November in Kernewek is {i}Du{/i}. It means black.' 'Come to the bookshop Saturday. I found something.'"

    thought "I am becoming a student. Not the pretending kind — the real kind. The kind that reads because she wants to know, not because someone will test her on it."

    ## =====================================================================
    ## SCENE 5.2 — MICHAEL'S PROTEST
    ## Campus cuts to mental health services.
    ## =====================================================================

    scene bg_campus_quad
    with dissolve

    # play music "audio/ch5_protest.ogg" fadein 2.0 volume 0.5

    "It starts with paper."

    "One morning, the campus is covered in flyers. Printed in black on fluorescent yellow — the kind of colour that refuses to be ignored."

    "{b}THEY CUT OUR COUNSELLING.{/b}"
    "{b}4 COUNSELLORS FOR 27,000 STUDENTS.{/b}"
    "{b}THE WAIT LIST IS 14 WEEKS.{/b}"
    "{b}WHAT ARE THEY WAITING FOR?{/b}"

    "A student union meeting. Standing room only. And at the front, a boy Amelia hasn't seen before."

    "Michael Osei."

    "He's not tall. He's not physically imposing. But when he speaks, the room changes."

    michael "Fourteen weeks. That's what they told my friend when she asked for help. Fourteen weeks. Do you know what can happen in fourteen weeks?"

    "His voice doesn't shake. It cuts."

    michael "This university spent two point four million pounds on a new business school lobby last year. Glass and chrome and a reception desk that looks like a spaceship. And they can't afford a fifth counsellor."

    "Murmurs. Agreement."

    michael "So we're going to stand outside the vice-chancellor's office tomorrow at noon. We're going to be polite. We're going to be persistent. And we're not going to leave until someone with an actual budget looks us in the eye and tells us our mental health matters less than a lobby."

    "Silence. Then applause."

    "Amelia looks around. Lucas is there, quiet, nodding. Raj has his arms folded, jaw tight. Liz is filming on her phone. Maya is at the back, watching with the kind of intensity that suggests she's read every pamphlet Michael's ever written."

    "Zara is beside Amelia."

    zara "He's good. He's really good."

    a "Yeah."

    zara "The question is — are we going?"

    ## =====================================================================
    ## CHOICE 5.1 — MICHAEL'S PROTEST
    ## =====================================================================

    menu:
        "Tomorrow. Noon. The vice-chancellor's office."

        "Join the protest — carry a sign, stand with Michael.":
            $ ch5_protest = "join"
            $ add_stat("stat_mc", 1)
            $ add_rel("rel_michael", 1)

            "She's there."

            "Noon. A crowd of maybe sixty students outside the admin building. Handmade signs. Someone has a megaphone. Michael is at the front in a coat that's too thin for December."

            "Amelia holds a sign that says {b}THE WAIT IS THE CRISIS{/b}. She didn't make it — someone handed it to her. She holds it like it matters."

            "A security guard watches from the doors. A photographer from the student paper. A few lecturers in the crowd — Simmons among them, in a massive scarf, looking proud."

            michael "Thank you for being here."

            "He says it to everyone. But he's looking at Amelia when he says it."

            "An administrator appears after forty minutes. Promises a 'review.' Nobody believes it, but the fact that they came out is something."

            michael "That's step one. Step one is always just showing up."

        "Attend, observe, write about it afterwards.":
            $ ch5_protest = "observe"
            $ add_stat("stat_sd", 1)

            "She goes. But she stands at the edge."

            "She watches Michael speak. Watches the crowd respond. Watches the security guard's face — bored, then uncomfortable, then something else."

            "She takes notes on her phone. Not because anyone asked her to, but because the gap between what she's feeling and what she understands is exactly the kind of gap that writing can bridge."

            "That evening, she writes something. Not an essay. Not a blog post. Something between a paragraph and a prayer."

            thought "Sometimes the best thing you can do is witness. Sometimes the best thing you can do is notice, and remember, and write it down so that it happened — not just in the moment, but in language."

        "Stay away — don't want to be involved.":
            $ ch5_protest = "avoid"
            $ add_stat("stat_mh", 1)

            "She doesn't go."

            "She tells herself it's because she has a deadline. She tells herself it's because protests make her anxious. She tells herself it's not her fight."

            "She studies in the library instead. Productive. Focused. Fine."

            "At dinner, Michael's name comes up."

            liz "You missed it. It was brilliant."

            a "I had an essay—"

            liz "Amelia, everyone has an essay. That's not a reason."

            "The comment stings. Not because Liz is wrong."

    ## =====================================================================
    ## SCENE 5.3 — SOPHIA PROJECT
    ## Assigned to the same group for developmental psych.
    ## =====================================================================

    scene bg_library_study_area
    with dissolve

    "The email arrives at 8:04am. Group assignments for the developmental psychology project."

    "Group 7: James, A. | Kowalski, S. | Others."

    thought "Of course."

    "They meet in the library. Sophia arrives precisely on time — her notebook already open, her colour-coded pens laid out in a row that makes Amelia want to both admire and burn them."

    sophia "Right. I've done a preliminary review of the literature. Here's the reading list I've drawn up."

    "She slides a printed sheet across the table. Twenty-three sources. Annotated."

    sophia "I've also outlined a possible structure for the report. Obviously open to changes."

    "It is not, from the tone of her voice, obviously open to changes."

    "The other group members exchange the look of people who recognise that they are either very lucky or very doomed."

    ## =====================================================================
    ## CHOICE 5.2 — SOPHIA PROJECT APPROACH
    ## =====================================================================

    menu:
        "Sophia has laid out the battlefield. What does Amelia do?"

        "Match her energy — compete, push for top marks.":
            $ ch5_sophia = "compete"
            $ add_stat("stat_aa", 1)
            $ add_rel("rel_sophia", 1)

            a "Good list. But you've missed Bowlby's 1956 revision — the one where he partially retracts the maternal deprivation hypothesis. It's important because it shows how the field evolved."

            "Sophia's pen stops."

            sophia "...Where did you read that?"

            a "Hawthorne's recommended reading. The extended list."

            "A silence. Then Sophia smiles. It's not a warm smile — it's the smile of a chess player who's just realised their opponent can actually play."

            sophia "Fine. Add it. And read Rutter's counter-study while you're at it — it's the response to Bowlby that actually holds up."

            "They work for three hours. It's exhausting and exhilarating. Neither gives an inch."

            thought "I don't like her. But I respect her. And I think she might — reluctantly, grudgingly — respect me."

        "Suggest dividing work equally, collaborating.":
            $ ch5_sophia = "collaborate"
            $ add_stat("stat_si", 1)
            $ add_rel("rel_sophia", 1)

            a "This is great, Sophia. Really thorough. Can we divide it up so everyone's playing to their strengths?"

            "Sophia looks at her. Evaluating."

            sophia "What are your strengths?"

            a "I'm good at synthesis — pulling different arguments together. You're better at methodology. Let's use that."

            "A beat."

            sophia "...That's actually sensible."

            "They divide the work. It's efficient and surprisingly easy once Sophia stops trying to control everything and Amelia stops trying to avoid confrontation."

            "At the end of the session:"

            sophia "You're better at this than I expected."

            a "Thank you. I think."

            sophia "It was a compliment. Mostly."

        "Let Sophia lead, do the minimum.":
            $ ch5_sophia = "passive"
            $ add_rel("rel_sophia", -1)

            a "Looks great. Just tell me what you need me to do."

            "Sophia's expression flattens."

            sophia "I need you to do your share. Not your minimum. Your share."

            "Amelia takes her section. Does it competently. On time."

            "But something between them closes. Sophia stops including her in the discussions. The other group members follow Sophia's lead."

            thought "I didn't lose anything. So why does it feel like I did?"

    ## =====================================================================
    ## SCENE 5.4 — RAJ'S FAMILY CALL
    ## Kitchen. Evening. Something's wrong.
    ## =====================================================================

    scene bg_kitchen_halls
    with dissolve

    # play music "audio/ch5_kitchen_evening.ogg" fadein 2.0 volume 0.4

    "Wednesday evening. The kitchen."

    "Raj is cooking. Daal. The flat smells extraordinary — cumin, turmeric, the warm sweetness of onions that have been simmering for an hour."

    "His phone rings. He glances at it. His face changes."

    raj "Sorry — one sec."

    "He steps into the corridor. Through the door, Amelia can hear his voice — in Gujarati, then English, then Gujarati again. The pattern is familiar from when she's heard him talk to his mum before, but the tone isn't."

    "The tone is careful. Controlled. The voice of someone who is trying very hard not to raise his voice."

    "Minutes pass. The daal needs stirring. Lucas does it."

    "Raj comes back. Sits down. Smiles."

    raj "Family, innit."

    "The smile doesn't reach his eyes."

    ## =====================================================================
    ## CHOICE 5.3 — RAJ'S FAMILY CALL
    ## =====================================================================

    menu:
        "The smile is a door. Amelia can knock or walk past."

        "\"Raj... it doesn't sound fine. You can talk to me.\"":
            $ ch5_raj = "push"
            $ add_stat("stat_si", 1)
            $ add_rel("rel_raj", 2)

            "The kitchen goes quiet. Lucas looks at his daal. Liz suddenly finds her phone very interesting."

            "Raj's smile doesn't move. But his eyes do something — a flicker. Like a lock turning."

            raj "My mum thinks I should switch to medicine."

            a "...Oh."

            raj "Yeah. She's — she's not wrong, exactly. Medicine is stable. It's respected. In our culture — I mean, in any culture, but in ours especially — stable and respected is the whole game, you know?"

            "He stirs the daal. Not because it needs stirring."

            raj "And I'm here doing psychology. Which she calls 'the talking degree.' She doesn't mean it nastily. She's just scared. She left Uganda with nothing and built something and she wants me to build something too. Something solid."

            a "But you love this."

            raj "Yeah."

            a "So what do you do?"

            raj "I don't know. I love her and I love this and those two things don't fit in the same sentence right now."

            "He smiles. A real one, this time — tired, but real."

            raj "Thanks for asking, though. Most people don't."

        "Respect his privacy — change the subject.":
            $ ch5_raj = "respect"
            $ add_stat("stat_mh", 1)
            $ add_rel("rel_raj", 1)

            a "This daal is incredible, Raj. Seriously."

            "He looks at her. Grateful."

            raj "Secret's in the tempering. You've got to let the cumin seeds pop before you add anything else."

            "The conversation moves on. The tension drains, slowly, like water from a bath."

            "He doesn't bring it up again. But later, as she's leaving the kitchen, he catches her arm."

            raj "Thanks."

            a "For what?"

            raj "For not making me talk about it."

        "Don't notice — caught up in her own world.":
            $ ch5_raj = "miss"

            "The daal is good. The conversation moves on. Lucas tells a story about a lecturer who accidentally projected his Tinder profile instead of his slides."

            "Everyone laughs."

            "Raj laughs too. But his phone stays face-down on the table for the rest of the evening, and Amelia doesn't notice."

    ## =====================================================================
    ## SCENE 5.5 — KARMA DICE EVENT
    ## Something unexpected. The universe rolls the dice.
    ## =====================================================================

    scene bg_campus_quad
    with dissolve

    "It comes from nowhere."

    python:
        import renpy.random
        dice_options = ["liz", "zara", "lucas"]
        ch5_dice_target = renpy.random.choice(dice_options)

    if ch5_dice_target == "liz":

        scene bg_halls_corridor
        with dissolve

        "Liz's door is open. She's sitting on her bed with her suitcase half-packed."

        a "Liz? What's—"

        liz "My nan's in hospital. She had a fall. I need to go home."

        "Her voice is flat. The way voices get when the feelings are too big for the throat."

        liz "I can't miss the seminar though. It's assessed. If I miss it I lose ten percent of—"

        a "Liz."

        liz "I know. I know. But—"

        "She starts crying. Not dramatically. Just — leaking. Tears arriving without permission."

    elif ch5_dice_target == "zara":

        scene bg_halls_corridor
        with dissolve

        "Zara is in the kitchen, staring at her phone."

        "She doesn't look up when Amelia comes in. That's unusual — Zara always greets people."

        a "Hey. You okay?"

        zara "Tasha's posted something."

        "She turns her phone around. A photo. Zara, from behind, in the library. With a caption that's technically not bullying, technically not racist, technically within the lines — but the implication drips from every word."

        zara "Forty-seven likes."

        "Her voice is steady. Too steady."

        zara "Forty-seven people thought that was funny."

    elif ch5_dice_target == "lucas":

        scene bg_lucas_room
        with dissolve

        "Lucas isn't at the study group. He's never not at the study group."

        "Amelia knocks on his door. No answer. She texts."

        "An hour later:"

        "{i}lucas: sorry. bad day. don't worry about it.{/i}"

        "She goes to his door anyway. It opens. He's sitting on his bed in the dark, headphones on, staring at the wall."

        a "Lucas."

        "He pulls off the headphones. His face looks different — raw. Like the version of himself he shows the world has been temporarily stripped away."

        lucas "My dad called."

        "He doesn't say anything else for a long time."

    ## =====================================================================
    ## CHOICE 5.D — KARMA DICE RESPONSE
    ## =====================================================================

    menu:
        "Someone needs help. Right now."

        "Drop everything — be there completely.":
            $ ch5_dice = "help"

            if ch5_dice_target == "liz":
                $ add_stat("stat_si", 1)
                $ add_rel("rel_liz", 1)

                a "Go. I'll email the seminar lead and explain. I'll send you my notes."

                liz "You can't just—"

                a "I can, actually. Go see your nan. The seminar will survive."

                "She emails the lecturer. She takes the most detailed notes she's ever taken. She sends them to Liz at 11pm with a message: {i}she's going to be okay. call me if you need x{/i}"

            elif ch5_dice_target == "zara":
                $ add_stat("stat_mh", 1)
                $ add_rel("rel_zara", 1)

                a "Let me see."

                "She takes Zara's phone. Reports the post. Screenshots it first."

                a "We're going to the student union tomorrow. This is documented harassment now. But tonight — do you want to watch something stupid and eat an entire packet of biscuits?"

                zara "...Yeah. Actually, yeah."

                "They watch three episodes of a cooking competition and don't talk about it again until Zara's ready."

            elif ch5_dice_target == "lucas":
                $ add_stat("stat_si", 1)
                $ add_rel("rel_lucas", 1)

                "She sits on the edge of his bed. She doesn't speak."

                "Twenty minutes. He talks, eventually. About his father, who is alive but unreachable. Who sends money but not messages. Who Lucas has been waiting four years for a conversation that's never going to come."

                "She listens."

                lucas "Sorry. That was a lot."

                a "Don't apologise. I asked."

                lucas "You didn't, actually. You just showed up."

                a "Same thing."

        "Help when it's convenient — check in later.":
            $ ch5_dice = "later"

            if ch5_dice_target == "liz":
                a "That's awful. Let me know if you need anything, yeah? I'll send the seminar notes after."

                liz "Thanks."

                "Amelia means it. She does send the notes. But she sends them the next day, and Liz is already on the train by then."

            elif ch5_dice_target == "zara":
                a "That's disgusting. You should report it."

                zara "Yeah. Maybe."

                "She says it the way people say 'yeah, maybe' when they know they won't."

            elif ch5_dice_target == "lucas":
                a "I'll come back later, yeah? When you're ready to talk."

                lucas "Sure."

                "She comes back after dinner. He's fine by then — or he's performing fine, which is the same thing from the outside."

    ## =====================================================================
    ## SCENE 5.6 — GROUP CORNWALL TRIP
    ## The group goes together. Not a mentor trip — a friend trip.
    ## =====================================================================

    scene bg_cornwall_coast
    with dissolve

    # play music "audio/ch5_cornwall.ogg" fadein 3.0 volume 0.5

    "December. A Saturday that's somehow not raining. The group goes to Cornwall."

    "Not a mentor trip — a {i}friend{/i} trip. Raj's idea. He books a minibus. Lucas brings a Bluetooth speaker. Maya brings enough snacks for twice the number of people."

    "Liz brings coats for everyone who forgot theirs, which is most of them."

    "The coastline near Newquay. Wind-sculpted cliffs, sea the colour of green glass, waves that crash like applause."

    "They walk. They talk. They laugh at things that aren't funny and don't explain why."

    "Raj takes photos of everything — the sea, the cliffs, Liz pretending to be blown away by the wind, Lucas sitting on a rock looking accidentally artistic."

    "Sarah comes."

    "She's quiet. She walks at the back. But she came. She's here."

    "Amelia falls into step beside her."

    a "You okay?"

    sarah "Yeah. It's nice out here."

    "A pause."

    sarah "Thanks for making me come."

    a "I didn't make you."

    sarah "You texted three times. That's basically making me."

    "A smile. Brief. Like a match struck in a dark room."

    # --- SONG SLIDESHOW: "Circles in the Sand" — Group Cornwall trip ---
    call slideshow_ch5_circles_in_the_sand

    ## =====================================================================
    ## CHOICE 5.4 — GROUP CORNWALL TRIP
    ## =====================================================================

    menu:
        "The coast stretches ahead. The group spreads out. Amelia can follow or wander."

        "Stay with the group — laugh, explore, take photos.":
            $ ch5_cornwall = "group"
            $ add_stat("stat_si", 1)

            "She stays."

            "They find a beach. Raj tries to skim stones and fails spectacularly. Maya does it perfectly, first try, five skips."

            maya "It's all in the wrist."

            raj "It is NOT all in the wrist."

            "Liz builds a cairn. Lucas sits beside it and reads. Zara and a friend take a selfie with the cliff behind them that will get a hundred likes."

            "Amelia takes a photo of all of them. She doesn't post it. She just keeps it."

            thought "This. This is the thing I didn't know I came here for."

        "Wander off alone to a quiet spot — think.":
            $ ch5_cornwall = "alone"
            $ add_stat("stat_sd", 1)

            "She peels off from the group. Not far — just enough to be alone with the sea."

            "She sits on a rock and watches the waves. The rhythm is hypnotic — crash, draw back, crash, draw back. The same two movements, forever."

            thought "I'm different now. I don't know when it happened. Somewhere between the first lecture and the panic attack and Cornwall and the mentor and Sarah on the bench — I became someone I didn't recognise. Not unrecognisable. Just... more."

            "She picks up a stone. Smooth. Grey. She puts it in her pocket."

            "Later, the group calls her back. Tea from a flask. Warmth."

        "{s}(IF on OK path){/s} Notice a standing stone near the path — investigate." if stat_ok >= 3:
            $ ch5_cornwall = "stone"
            $ add_stat("stat_ok", 1)

            "The group turns a corner. And there, set back from the path, half-hidden by gorse — a standing stone."

            "Not a famous one. No sign. No plaque. Just a single upright stone, taller than Amelia, leaning slightly, as though it's been listening to the wind for so long it's started to lean into it."

            "She stops."

            maya "That's a menhir. Prehistoric. Nobody knows what they're for — boundary marker, astronomical alignment, ceremonial. Everyone has a theory."

            if mentor_path == "elena":
                elena "The Cornish word is {i}men hir{/i}. Long stone. The language is honest — it describes what it sees."

            "Amelia touches it. The granite is rough and cold and impossibly old."

            thought "People put this here. They had a reason. The reason is lost. But the stone remains. And the fact that I'm standing here, touching it, wondering — that connects something. A thread across centuries."

            "She takes a photo. Then puts her phone away. Some things don't need to be recorded. They need to be {i}felt{/i}."

    ## =====================================================================
    ## SCENE 5.7 — THE OCCULT THREAD (Conditional)
    ## Only triggers if OK ≥ 3
    ## =====================================================================

    if stat_ok >= 3:

        scene bg_barbican_bookshop
        with dissolve

        "The following week. The bookshop on the Barbican."

        "Amelia isn't looking for anything specific — she's browsing the way you browse when you know the thing you need will find you before you find it."

        "Back corner. A shelf with no label. Between a water-damaged book about star maps and a copy of Agrippa's {i}De Occulta Philosophia{/i} that's seen better centuries:"

        "{i}The St. Michael Line: Ley Energy and the Cornish Landscape{/i}. Published 1978. Author: someone she's never heard of."

        "She opens it."

        "The first chapter is about the alignment of sacred sites from St Michael's Mount in Cornwall to Avebury in Wiltshire — churches, stone circles, holy wells, all falling along the same invisible line."

        "It sounds mad."

        "It also sounds familiar."

        ## =====================================================================
        ## CHOICE 5.5 — OCCULT THREAD: THE LEY LINE BOOK
        ## =====================================================================

        menu:
            "The book is in her hands. Seven pounds fifty."

            "Buy it. Read it that night.":
                $ ch5_occult = "buy"
                $ add_stat("stat_ok", 1)

                "She buys it."

                "That night, in her room, she reads it cover to cover. The arguments are half-science, half-mysticism, the kind of thing that would make Hawthorne's eyebrow achieve orbit."

                "But the maps. The maps are extraordinary. Sites she's visited — Madron Well, Mên-an-Tol — falling on the line. The coincidence is too neat."

                if mentor_path == "elena":
                    "She texts Elena."

                    "{i}amelia: i found the ley line book. is this real?{/i}"

                    "The reply comes at 1am."

                    "{i}elena: define real. then come back to me.{/i}"

                else:
                    thought "Either ancient people really did align their sacred sites along invisible lines of energy, or the human brain is so desperate for patterns that it'll draw them on any map."

                    thought "Both options are terrifying. Both are beautiful."

            "Note it down. Move on.":
                $ ch5_occult = "note"

                "She photographs the title and the author. Puts the book back."

                "Maybe later. There's a statistics deadline that won't meet itself."

    else:
        $ ch5_occult = "none"

    ## =====================================================================
    ## SCENE 5.8 — SETTLING
    ## End of chapter. The threshold is crossed.
    ## =====================================================================

    scene bg_amelia_room_plymouth_night
    with dissolve

    # play music "audio/ch5_close.ogg" fadein 2.0 volume 0.3

    "Late November. She's in her room. It's raining — it's always raining — but the sound of it has changed. When she arrived, rain sounded like exile. Now it sounds like home."

    "Her desk is covered in notes. Her bookshelf is full. The walls are no longer bare — photos, postcards, a print she bought at the Barbican, a dried leaf from the Cornwall trip that she pressed in a book."

    "She picks up her phone. Opens the group chat."

    "{i}raj: who's cooking tomorrow? i vote not me for once{/i}"
    "{i}liz: IMPOSSIBLE. the kitchen hasn't known another chef{/i}"
    "{i}lucas: i can make toast{/i}"
    "{i}maya: i'll bring fairy lights. that counts as a contribution{/i}"
    "{i}raj: it really doesn't{/i}"
    "{i}maya: it absolutely does{/i}"

    "She smiles."

    thought "I crossed something. I don't know when. But I'm on the other side now."

    "The threshold wasn't a door. It wasn't a moment. It was all of it — the lectures and the tears and the mentor and Cornwall and the kitchen at midnight and the friend who came to the coast even though she didn't want to."

    "She is becoming."

    "Not finished. Not whole. But becoming."

    ## -----------------------------------------------------------------------
    ## END OF CHAPTER
    ## -----------------------------------------------------------------------

    scene black
    with fade

    centered "{size=+6}End of Chapter Five{/size}"
    pause 2.0

    return
