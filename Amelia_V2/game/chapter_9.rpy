###############################################################################
##
##  CHAPTER 9: THE REWARD
##
##  Hero's Journey: The hero gains something — knowledge, understanding.
##  Alchemical Stage: Late Citrinitas — gold emerging from the fire.
##  Month: March. Location: Plymouth + Cornwall.
##  Palette: Raw greens, pale sunlight. Rain still, but lighter.
##  Music: Acoustic. Strings. Something tentative and warm.
##
##  Scenes: 7–8 (varies by Sarah outcome) | Choices: 5
##  Max earnable: ~8 pts
##
###############################################################################

label chapter_9:

    $ current_chapter = 9
    stop music fadeout 1.0
    scene black
    with fade

    centered "{size=+20}Chapter Nine{/size}\n\n{size=+6}The Reward{/size}"
    pause 3.0

    ## =====================================================================
    ## SCENE 9.1 — NEW SEASON
    ## The world continues. Amelia finds she can too.
    ## =====================================================================

    scene bg_plymouth_hoe_day
    with dissolve

    # play music "audio/ch9_spring.ogg" fadein 3.0 volume 0.4

    "March."

    "The daffodils appear overnight like small yellow flags of surrender. The light changes — not warmer exactly, but longer, stretching into the evenings like someone pulling a sheet across a bed."

    "Amelia walks to the Hoe. She's doing this now — walking, most mornings. Not meditation, not exercise, just walking. Moving through the world because the alternative is sitting still and sitting still is dangerous."

    "The sea is there. Still. Always."

    "She stands at the railing and breathes."

    thought "I'm still here."

    "It's not a triumph. It's an observation. A fact she tests each morning, the way you touch a bruise to see if it still hurts."

    thought "I'm still here. And today that's enough."

    ## =====================================================================
    ## SCENE 9.2 — PROCESSING THE ORDEAL
    ## =====================================================================

    scene bg_amelia_room_plymouth_day
    with dissolve

    "The room has changed."

    "Or rather, Amelia has changed the room. The desk is clear. The books are organised. She bought a plant — a small jade, because Simmons said they're impossible to kill — and it sits on the windowsill catching the thin March light."

    "On the wall: a postcard from Ella (the Tate, blue), a photo of the flat group from Christmas (Raj cooking, Lucas pretending to help, Liz mid-laugh), and a drawing she found in one of her notebooks — a sketch of Plymouth from the Hoe that she doesn't remember making."

    "She's trying to process."

    ## =====================================================================
    ## CHOICE 9.1 — PROCESSING THE ORDEAL
    ## =====================================================================

    menu:
        "She has to make sense of what happened. Or start to."

        "Journaling and reflection — sit with it, write through it.":
            $ ch9_process = "journal"
            $ add_stat("stat_sd", 1)
            $ add_stat("stat_mh", 1)

            "She buys a new notebook. Plain, unlined. £3.50 from the campus shop."

            "She writes."

            "Not about what happened — not directly. She writes about the colour of the hospital walls, and the sound the lift made, and the way Raj's hands shook when he poured the tea."

            "She writes about her mother's voice on the phone: 'Come home, sweetheart. You can come home.' And how she said: 'I know. But I need to be here.'"

            "She writes about grief. About the space between knowing someone is hurting and being able to help. About the ceiling of her room at 3am and the way the streetlight makes a triangle in the corner."

            "She doesn't read it back. She doesn't need to. The writing isn't for reading — it's for moving things from inside to outside."

            thought "I don't understand what happened. But I'm letting myself not understand. And that feels — not good. But honest."

        "Talking it through with friends — you're not meant to carry this alone.":
            $ ch9_process = "friends"
            $ add_stat("stat_si", 1)
            $ add_stat("stat_mh", 1)

            "The kitchen. Midnight. The four of them — Amelia, Raj, Liz, Lucas."

            "They talk."

            "Not all at once. Not as a planned thing. It starts with Raj saying 'I keep thinking about that night' and then nobody stops for two hours."

            raj "I keep thinking — what if I'd knocked on her door sooner? What if I'd pushed harder?"

            liz "You can't think like that. You'll drive yourself mental."

            raj "I know. But I do."

            lucas "We all do."

            "They talk about guilt and helplessness and the specific horror of being nineteen and not knowing what to do when someone you live with wants to die."

            "Liz cries. Raj holds her hand. Lucas stares at the table."

            a "I don't think we're supposed to have answers. I think we're just supposed to be here."

            "And they are. Here. In the kitchen. Together."

        "Throw herself into work — keep moving, keep busy.":
            $ ch9_process = "work"
            $ add_stat("stat_aa", 1)

            "She writes the essay. Then the next one. Then the presentation. Then the lab report."

            "She sits in the library from 9am to 9pm and emerges blinking into the dark and does it again the next day."

            "The work is — better, actually. It's deeper. Her analysis of attachment theory isn't just theory anymore; it's lived experience. Her case study write-up has an empathy to it that wasn't there before."

            "Simmons notices."

            simmons "This is good work, Amelia. Really good."

            "But she's not sleeping. Not properly. And the work is a wall she's building between herself and the thing she needs to feel."

            thought "I'll deal with it later. Right now, I need to pass."

    ## =====================================================================
    ## SCENE 9.3 — THE FRIEND GROUP (Post-crisis)
    ## =====================================================================

    scene bg_flat_kitchen
    with dissolve

    "The flat is different."

    if sarah_alive:
        if sarah_outcome == "full_save":
            "Sarah's room is empty but her name is on the door. She's in hospital but she's coming back. Maybe. The 'maybe' hangs in the air like a held breath."
        elif sarah_outcome == "late_save":
            "Sarah's room is being kept for her. The university arranged it. Her things are still there — the books, the wren sketch, the mug with the chip."
        elif sarah_outcome == "partial_save":
            "Sarah's room has been packed up. Her parents came. They were polite. They were devastated. They took her home to Devon."
    else:
        "Sarah's room is empty. The door is closed. Someone — Raj, probably — left a small bunch of daffodils outside it."

        "Nobody goes in."

    "The group has reorganised itself around the absence. Raj cooks more. Liz talks more. Lucas talks less but stays in the kitchen longer, present in his quiet way."

    ## =====================================================================
    ## CHOICE 9.2 — FRIEND GROUP DYNAMICS
    ## =====================================================================

    menu:
        "The group needs someone. Or needs nobody. Or needs space."

        "Organise something — be the one who holds the group together.":
            $ ch9_friends = "organise"
            $ add_stat("stat_si", 1)
            $ add_rel("rel_raj", 1)

            "She plans a dinner. Not a big thing — just the four of them, proper food, a table."

            a "Saturday. I'm cooking. Nobody's allowed to help except Raj because I'll burn something."

            raj "You'll definitely burn something."

            a "That's why you're helping."

            "Saturday comes. She makes pasta — badly, then better with Raj's supervision. Liz brings wine. Lucas brings an actual tablecloth from somewhere."

            "They eat. They talk. Not about what happened — about everything else. Lucas's summer plans. Liz's internship application. Raj's mum's birthday."

            "Ordinary things. The most precious things in the world."

        "Let Raj handle it — just show up, be present.":
            $ ch9_friends = "show_up"
            $ add_stat("stat_mh", 1)

            "Raj doesn't need to be asked. He cooks every evening that week. Nobody eats alone."

            "Amelia shows up. She doesn't plan, doesn't organise. She just sits at the table and eats what Raj makes and laughs at Liz's stories and listens to Lucas's music recommendations."

            "She rests."

            thought "I don't need to hold everything. I just need to be held."

        "Need space — pull back for a while.":
            $ ch9_friends = "space"

            "She eats in her room. Not every night — but more than before."

            "She needs the quiet. The flat is too full of... everything. The concern. The checking in. The careful way people speak around the space where Sarah was."

            "She misses a few dinners. Then a few more."

            "Raj texts: {i}\"you ok? x\"{/i}"

            "She replies: {i}\"fine. just need some time. x\"{/i}"

            "He doesn't push. He leaves a bowl of daal outside her door instead."

    ## =====================================================================
    ## SCENE 9.4 — SARAH'S STATUS (Living-with-it scenes)
    ## =====================================================================

    if sarah_alive:

        if sarah_outcome == "full_save":

            scene bg_hospital_corridor
            with dissolve

            "She visits Sarah."

            "The hospital room has changed — more cards now, a stack of books, a drawing Raj sent. Sarah is sitting up. She looks tired but present."

            sarah "The therapist wants me to keep a journal."

            a "Is it helping?"

            sarah "I don't know. I keep writing the same things. 'Today I ate breakfast. Today I went outside. Today I didn't want to die.'"

            "The honesty of it."

            sarah "Sorry. That's a lot."

            a "It's not a lot. It's everything."

            "They sit. Sarah draws in her notebook — small things, birds, patterns."

            sarah "The doctor says I might be able to come back next year. Part-time."

            a "That's brilliant."

            sarah "It's terrifying."

            a "Both things can be true."

            "Sarah looks at her. Something shifts."

            sarah "You sound like someone's mentor."

            a "God, please don't tell them that."

            "A quiet laugh. Real."

        elif sarah_outcome == "late_save":

            scene bg_hospital_corridor
            with dissolve

            "The hospital."

            "Sarah is — better. If 'better' means alive, eating, speaking. She's not better if 'better' means okay."

            sarah "Don't look at me like that."

            a "Like what?"

            sarah "Like I'm made of glass."

            a "I don't think you're made of glass. I think you're made of steel and bad decisions and really strong tea."

            "The ghost of something. Not a smile. The space where a smile will be, eventually."

            sarah "They want me to stay another week."

            a "Good."

            sarah "I hate it here."

            a "I know."

            sarah "The food is terrible."

            a "I brought biscuits."

            sarah "...You're annoyingly persistent."

            a "I know."

        elif sarah_outcome == "partial_save":

            scene bg_amelia_room_plymouth_day
            with dissolve

            "She writes to Sarah. An actual letter, on paper."

            "{i}Dear Sarah,{/i}\n{i}I don't know if you want to hear from me. I wouldn't blame you if you didn't. But I wanted to say: I'm sorry. I should have been there. I wasn't. That's something I'll carry.{/i}"

            "{i}I'm not writing to make myself feel better. I'm writing because you deserve to know that someone is thinking about you. Every day.{/i}"

            "{i}If you want to write back, I'd like that. If you don't, I understand. Either way: I'm here. Still here.{/i}"

            "{i}Amelia x{/i}"

            "She posts it. First class. Then waits."

            "Three weeks later, a text:"

            "{i}sarah: i got your letter. thank you. i'm not ready to talk. but thank you.{/i}"

            thought "It's not enough. It's something."

    else:

        scene bg_campus_quad
        with dissolve

        "The memorial bench arrives mid-March."

        "A wooden bench near the library, with a small brass plaque: {i}IN MEMORY OF SARAH WHITMORE, 2003–2024. SHE WAS HERE.{/i}"

        "The group goes together. Not a ceremony — just the five of them standing in the rain."

        "Raj reads a poem. He doesn't say who wrote it. Amelia suspects it was him."

        "Liz puts down a bunch of wildflowers — scrappy ones, from the roadside, not shop-bought. Sarah would have preferred those."

        "Lucas stands with his hands in his pockets and looks at the bench and says: 'She would have hated this.'"

        "He's right. She would have."

        "They stand there until the rain gets worse, and then they go to the kitchen and Raj cooks and nobody says much."

        "The bench stays. Rain or shine. Someone always puts fresh flowers on it."

    ## =====================================================================
    ## SCENE 9.5 — ACADEMIC RECOVERY
    ## =====================================================================

    scene bg_library
    with dissolve

    "The library."

    "She hasn't been back properly since — since everything. The seat by the window is her old spot. Someone else is sitting there. She chooses a different one. It's fine."

    "She opens her laptop. The essay is on developmental psychology. 2000 words. Due Friday."

    "She starts writing."

    "And — something is different."

    "The words come. Not fast, not fluently, but with a weight they didn't have before. She writes about attachment and loss and she's not just citing Bowlby anymore — she {i}understands{/i} Bowlby."

    ## =====================================================================
    ## CHOICE 9.3 — ACADEMIC RECOVERY
    ## =====================================================================

    menu:
        "The essay. She could write something safe, or something honest."

        "Write honest work — deeper than before, informed by experience.":
            $ ch9_academic = "honest"
            $ add_stat("stat_aa", 1)
            $ add_stat("stat_sd", 1)

            "She writes about attachment theory and she leaves herself in it."

            "Not autobiography — she's too careful for that. But the examples are real. The analysis has teeth. The conclusion says something nobody else in the seminar will say: that attachment isn't just a theory of childhood bonds, it's a theory about the fabric of connection itself, and it's fragile, and it matters, and we don't value it enough."

            "She submits it at 11:47pm. Thirteen minutes before the deadline."

            "She gets 74%%."

            "It's the best mark she's ever received."

        "Write safe work — meet the requirements, keep your head down.":
            $ ch9_academic = "safe"
            $ add_stat("stat_aa", 1)

            "She writes a solid, competent essay. Well-structured. Properly referenced. Everything in the right place."

            "She gets 66%%."

            "It's fine. It passes. She can move on."

        "Take a shortcut — borrow notes, rush it, just get it done.":
            $ ch9_academic = "shortcut"
            $ add_stat("stat_mc", -1)

            "She borrows Sophia's notes. She paraphrases heavily. She submits something that is technically her own work but barely."

            "She gets 58%%."

            "She knows. She doesn't need anyone to tell her. She knows."

            thought "Sarah almost died and I'm taking shortcuts on Bowlby essays. This isn't who I am."

            "The knowledge sits in her like a splinter."

    ## =====================================================================
    ## SCENE 9.6 — CORNWALL: THE HEALING TRIP
    ## =====================================================================

    scene bg_cornwall_coast
    with dissolve

    "March break."

    "The mentor arranges a Cornwall trip. Not a test this time — a restoration. The landscape as medicine."

    # --- SONG SLIDESHOW: "jolly-rum-ba-low!" — Cornwall healing, spring energy ---
    call slideshow_ch9_jolly_rum_ba_low

    if mentor_path == "hawthorne":
        "Hawthorne drives. He puts Classic FM on and doesn't apologise for it."

        hawthorne "The Cornish landscapes have been healing people longer than psychology has existed. Take that as you will."

    elif mentor_path == "simmons":
        "Simmons takes the train and brings sandwiches."

        simmons "The Eden Project has a new installation on resilience in plant communities. I think you'll like it."

    elif mentor_path == "maya":
        "Maya drives her van. The dashboard is covered in crystals and a small figure of Ganesh."

        maya "We're not going somewhere specific. We're going where the road takes us."

    elif mentor_path == "elena":
        "Elena meets her at the station. She's wearing the same green scarf."

        elena "Dydh da. You look like someone who's been through the fire."

        a "I have."

        elena "Good. Let's walk."

    ## =====================================================================
    ## CHOICE 9.4 — CORNWALL RESTORATION
    ## =====================================================================

    menu:
        "Cornwall. The coast. The light. The wind."

        "Explore a new site — open to what comes.":
            $ ch9_cornwall = "new"
            $ add_stat("stat_sd", 1)

            if mentor_path == "hawthorne":
                scene bg_cornwall_coast
                with dissolve

                "Hawthorne takes her to Botallack."

                "The tin mines perch on the cliff edge like something from a dream — stone ruins against sky and sea. The wind is tremendous."

                hawthorne "Two hundred years ago, miners worked under the seabed itself. They could hear the boulders rolling above them."

                a "That's terrifying."

                hawthorne "Yes. And they went down every day."

                "She stands at the edge and looks out. The sea is enormous. She is small. Both things are true."

            elif mentor_path == "simmons":
                scene bg_eden_project
                with dissolve

                "The Eden Project. The biomes gleam."

                "Inside the Rainforest Biome, the humidity hits her like a wall. Green everywhere — cascading, vivid, almost aggressive in its aliveness."

                simmons "Look at this."

                "A sign: {i}This area was a quarry. Nothing grew here. Now: everything.{/i}"

                simmons "Restoration. It's not about going back. It's about what can grow next."

            elif mentor_path == "maya":
                "They end up at Kynance Cove."

                "The serpentine rock is green and red and strange. The sea is turquoise in the shallows. It looks like another planet."

                maya "Every time I come here, I see something different. That's the point."

            elif mentor_path == "elena":
                "Elena takes her to the Cheesewring."

                "A stack of granite slabs, balanced impossibly. Natural formation or ancient monument — nobody agrees."

                elena "Like you. Still standing. Against all probability."

        "Return to a significant previous site — see it with new eyes.":
            $ ch9_cornwall = "revisit"
            $ add_stat("stat_ok", 1)

            if mentor_path == "hawthorne":
                "They return to Bodmin Moor. The tor where they sat in October."

                "The same rocks. The same sky. But everything looks different — softer, or sharper."

                hawthorne "Same place. Different you."

                a "Is that the lesson?"

                hawthorne "That's the only lesson."

            elif mentor_path == "simmons":
                "They return to the Eden Project. The spot by the Mediterranean garden."

                simmons "Last time you stood here, you didn't believe that broken things could heal."

                a "I still don't. Not completely."

                simmons "That's honest. Honest is a start."

            elif mentor_path == "maya":
                "They return to Tintagel."

                "The same cliff path. The same Atlantic wind."

                "But Maya doesn't tell the Arthur stories this time. She doesn't tell any stories."

                maya "Just walk. Just be here."

                "And Amelia is. Here. Fully."

            elif mentor_path == "elena":
                "Elena takes her back to the Merry Maidens."

                "The stone circle in the field. The same stones. The same quiet."

                elena "You came here before as a student. You come here now as something else."

                a "What?"

                elena "That's not for me to tell you."

        "Stay in Plymouth — Cornwall isn't for you right now.":
            $ ch9_cornwall = "stay"

            "She declines the trip."

            "She's not ready. The landscape is too big, too open. She needs walls and ceilings and the specific quiet of her room."

            "The mentor understands."

            if mentor_path == "hawthorne":
                hawthorne "The moors aren't going anywhere. Neither are you."
            elif mentor_path == "simmons":
                simmons "Self-knowledge includes knowing what you're not ready for."
            elif mentor_path == "maya":
                maya "Sometimes the bravest thing is staying still."
            elif mentor_path == "elena":
                elena "The land will wait."

    ## =====================================================================
    ## SCENE 9.7 — MENTOR ACKNOWLEDGMENT
    ## =====================================================================

    if ch9_cornwall == "stay":
        scene bg_amelia_room_plymouth_day
        with dissolve

        "The conversation happens by phone."
    else:
        "On the drive back — or the walk, or the train — the mentor says something."

    if mentor_path == "hawthorne":
        "Hawthorne is quiet for a long time. Classic FM fills the silence. Then:"

        hawthorne "You've changed this year. I don't say that lightly. Most of my students learn to write better essays. Some of them learn to think. Very few of them learn to {i}see{/i}."

        "A pause."

        hawthorne "You see things now. People. Pain. Patterns. It will make your work extraordinary. It will also make your life harder."

    elif mentor_path == "simmons":
        simmons "Do you remember the first time you came to my office? You sat on the edge of the chair like you were ready to bolt."

        a "I probably was."

        simmons "You're not on the edge anymore. You're in the room."

        "She smiles."

        simmons "I'm proud of you. As your tutor and as someone who cares. You've done something this year that most people take a lifetime to do."

    elif mentor_path == "maya":
        maya "You're different."

        a "Everyone keeps saying that."

        maya "Because it's true. The question is whether you know it yet."

        "A long silence."

        maya "You came here uncertain of everything. You're still uncertain. But now you're uncertain on purpose. That's wisdom."

    elif mentor_path == "elena":
        elena "The Citrinitas is ending. The fire has done its work."

        a "I don't feel golden."

        elena "The gold doesn't feel golden either. Not at first. It just feels... different."

        "She looks at Amelia."

        elena "You've been through the worst of it. What comes next is the integration. The {i}making sense{/i}."

        elena "Meur ras. Thank you. For staying in the fire."

    ## =====================================================================
    ## CHOICE 9.5 — MENTOR ACKNOWLEDGMENT
    ## =====================================================================

    menu:
        "The mentor sees her clearly. Perhaps for the first time."

        "Accept the recognition with grace.":
            $ ch9_mentor = "accept"
            $ add_stat("stat_sd", 1)
            if mentor_path == "hawthorne":
                $ add_rel("rel_hawthorne", 1)
            elif mentor_path == "simmons":
                $ add_rel("rel_simmons", 1)
            elif mentor_path == "maya":
                $ add_rel("rel_maya", 1)
            elif mentor_path == "elena":
                $ add_rel("rel_elena", 1)

            a "Thank you."

            "She says it simply. No deflection. No 'oh, it's nothing.' Just:"

            a "Thank you. That means more than you know."

            thought "I've been trying so hard to become something. And someone noticed that I succeeded."

        "Deflect — \"I just did what anyone would do.\"":
            $ ch9_mentor = "deflect"
            $ add_stat("stat_mh", 1)

            a "I just did what anyone would do."

            if mentor_path == "hawthorne":
                hawthorne "That's demonstrably untrue and you know it."
            elif mentor_path == "simmons":
                simmons "Not anyone. You. That matters."
            elif mentor_path == "maya":
                maya "Not anyone. Most people don't show up at 2am."
            elif mentor_path == "elena":
                elena "You say 'anyone.' The fire knows your name."

            "She doesn't push back. But she holds the words."

    ## =====================================================================
    ## SCENE 9.8 — SMALL GOLD
    ## The chapter's final image.
    ## =====================================================================

    scene bg_amelia_room_plymouth_day
    with dissolve

    "Her room. Evening. March light — the specific gold that comes before spring properly arrives."

    "She's sitting at her desk. The jade plant is growing. The postcard from Ella is curling at the edges."

    "Her phone buzzes. A text from Raj:"

    "{i}raj: flat dinner. i'm making the thing. be there or be square.{/i}"

    "{i}liz: square doesn't even make sense raj{/i}"

    "{i}lucas: be there.{/i}"

    "She smiles."

    "She opens her notebook — the one from September, the first one. She flips to the last page of writing. Then starts a new page."

    "{i}March 14th.{/i}"

    "{i}Things I know:{/i}\n{i}1. I am not who I was.{/i}\n{i}2. That's not the same as being who I want to be. But it's closer.{/i}\n{i}3. Raj's daal cures most things. Not all things. But most.{/i}"

    thought "Gold. Just a little. Just enough."

    ## -----------------------------------------------------------------------
    ## END OF CHAPTER
    ## -----------------------------------------------------------------------

    scene black
    with fade

    centered "{size=+6}End of Chapter Nine{/size}"
    pause 2.0

    return
