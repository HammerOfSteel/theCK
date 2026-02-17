###############################################################################
##
##  CHAPTER 12: RETURN WITH THE ELIXIR
##
##  Hero's Journey: The hero returns home transformed, bearing a gift.
##  Alchemical Stage: Post-Rubedo — the Work is done. The Stone is formed.
##  Month: June. Location: Plymouth → London.
##  Palette: All colours. Iridescent. The quality of last things.
##  Music: Ending-specific. Full, warm, resolved.
##
##  Scenes: 2 shared + 3–5 ending-specific | Choices: 2 (minimal)
##  Max earnable: ~2 pts (symbolic — the ending is determined, not chosen)
##
##  7 ENDINGS (priority order):
##  1. The Grief (sarah_died AND MH ≤ 10 AND SI ≤ 10)
##  2. The Alchemist (OK ≥ 18 AND SD ≥ 16 AND Elena path)
##  3. The Scholar (AA ≥ 18 AND SD ≥ 16)
##  4. The Companion (SI ≥ 18 AND avg_relationships ≥ 6)
##  5. The Healer (MH ≥ 18 AND MC ≥ 16)
##  6. The Whole (all stats ≥ 12 AND none < 8)
##  7. The Bittersweet (default)
##
###############################################################################

label chapter_12:

    stop music fadeout 1.0
    scene black
    with fade

    centered "{size=+20}Chapter Twelve{/size}\n\n{size=+6}Return with the Elixir{/size}"
    pause 3.0

    ## =====================================================================
    ## SHARED OPENING — THE LAST MORNING
    ## =====================================================================

    scene bg_amelia_room_plymouth_day
    with dissolve

    # play music "audio/ch12_last_morning.ogg" fadein 3.0 volume 0.4

    "June."

    "She wakes up in her room for the last time."

    "The walls are bare. The postcards are in a box. The jade plant is in a bag — she's keeping it, obviously, you don't abandon a living thing — and the books are packed, and the drawers are empty, and the room is just a room again."

    "A room that was a world. Her world. For nine months."

    "She sits on the stripped bed. The mattress is thin. She can feel the springs."

    thought "I arrived here in September. I put the photo of Ella on the desk and the fairy lights above the bed and I thought: this is what university looks like."

    thought "It didn't look like this at all."

    ## =====================================================================
    ## CHOICE 12.1 — THE LAST MORNING
    ## =====================================================================

    menu:
        "One hour before the taxi. What does she do?"

        "Walk through campus one last time.":
            $ ch12_morning = "campus"
            $ add_stat("stat_sd", 1)

            scene bg_campus_quad
            with dissolve

            "She walks."

            "The library. She touches the door handle. The specific weight of it, the cold metal, the way it creaks."

            "The lecture theatre where Hawthorne raised his eyebrow and said 'Define intelligence' on the first day and nobody could."

            "The bench outside the student union where Raj taught her to play chess and she beat him once and he never forgave her."

            if not sarah_alive:
                "Sarah's bench. The brass plaque. Fresh flowers — someone always puts fresh flowers."

                "She sits for a moment."

                a "Bye, Sarah."

            "The campus is ordinary and extraordinary and she has walked it a thousand times and she will never walk it quite this way again."

        "Spend the morning with friends.":
            $ ch12_morning = "friends"
            $ add_stat("stat_si", 1)

            scene bg_flat_kitchen
            with dissolve

            "The kitchen."

            "Raj is making eggs. Of course he is. Lucas is on the sofa. Liz is packing and unpacking the same box."

            raj "Last breakfast. I'm doing the works."

            liz "I can't eat. I'm going to cry."

            raj "You can cry and eat. I do it all the time."

            "They sit. Eggs and toast and tea. The most ordinary meal. The most important."

        "Pack efficiently — ready to go, forward-looking.":
            $ ch12_morning = "pack"
            $ add_stat("stat_aa", 1)

            "She packs the last box. Labels it. Stacks it by the door."

            "Everything she owns fits in boxes again. The same number as September, plus three. Growth measured in cardboard."

            thought "Done. I'm done."

    ## =====================================================================
    ## THE LAST GOODBYE
    ## =====================================================================

    scene bg_halls_corridor
    with dissolve

    "The corridor."

    "They're all here. Raj, Liz, Lucas. The corridor is full of boxes, bags, parents' cars arriving."

    # --- SONG SLIDESHOW: "The Quiet of Morning" — The last goodbye ---
    call slideshow_ch12_the_quiet_of_morning

    ## =====================================================================
    ## CHOICE 12.2 — THE LAST GOODBYE
    ## =====================================================================

    menu:
        "The goodbye. The moment."

        "Hug everyone. Be openly emotional.":
            $ ch12_goodbye = "hug"
            $ add_stat("stat_mh", 1)

            "She hugs Raj first. He picks her up. He always picks people up."

            raj "You're the worst chess player I've ever met."

            a "And the best friend?"

            raj "The best friend."

            "Liz next. The hug is fierce and involves a lot of Welsh cursing."

            liz "If you don't text me every day I will drive to London and cause a scene."

            a "I know you will."

            "Lucas. The hug is brief and tight and he says nothing and she says nothing and that's everything."

            "She's crying. They're all crying. The corridor smells of cardboard and tears and nine months of life."

        "Quiet nods. Meaningful looks.":
            $ ch12_goodbye = "quiet"
            $ add_stat("stat_sd", 1)

            "She looks at each of them."

            "Raj. The handshake that becomes a hug."

            "Liz. The eye contact that says everything."

            "Lucas. The nod. Just the nod."

            "Some things don't need words."

        "Promise to keep in touch — and mean it.":
            $ ch12_goodbye = "promise"
            $ add_stat("stat_si", 1)

            a "This isn't goodbye."

            raj "It's 'see you later.'"

            a "It's 'see you in September.' Or before. Summer. I'm coming to visit. All of you."

            liz "Is that a promise?"

            a "It's a promise."

            "She means it. She can feel herself meaning it."

    ## =====================================================================
    ## ENDING CALCULATION
    ## =====================================================================

    scene black
    with dissolve

    python:
        # Calculate average relationships for Companion ending
        avg_rels = (rel_ella + rel_raj + rel_liz + rel_lucas + rel_zara + rel_sarah) / 6.0

        # Calculate ending
        if not sarah_alive and stat_mh <= 10 and stat_si <= 10:
            ending = "the_grief"
        elif stat_ok >= 18 and stat_sd >= 16 and mentor_path == "elena":
            ending = "the_alchemist"
        elif stat_aa >= 18 and stat_sd >= 16:
            ending = "the_scholar"
        elif stat_si >= 18 and avg_rels >= 6:
            ending = "the_companion"
        elif stat_mh >= 18 and stat_mc >= 16:
            ending = "the_healer"
        elif stat_aa >= 12 and stat_si >= 12 and stat_mh >= 12 and stat_sd >= 12 and stat_mc >= 8 and stat_ok >= 8:
            ending = "the_whole"
        else:
            ending = "the_bittersweet"

    ## =====================================================================
    ## THE TRAIN
    ## =====================================================================

    scene bg_london_train
    with dissolve

    "The train."

    "Plymouth falls away. Devon. Somerset. The land flattens and London approaches."

    "Amelia sits by the window. Her bag is in the rack. Her journal is in her lap."

    ## =====================================================================
    ## ENDING 1: THE GRIEF
    ## Sarah died. Amelia is broken. But breaking is not the end.
    ## =====================================================================

    if ending == "the_grief":

        # play music "audio/ending_grief.ogg" fadein 3.0 volume 0.4

        "She gets off the train at Paddington."

        "London is the same. She is not."

        scene bg_london_park
        with dissolve

        "She goes to the park."

        "Not to the bench — she can't sit still, not today. She walks."

        "She walks until she finds a garden centre. Small, cramped, with trays of seedlings outside. She buys a tree. A young rowan. The woman at the counter asks if it's a gift."

        a "It's for someone."

        "The park. A corner she knows — a quiet bit near the wall, where the light is good in the afternoon."

        "She digs."

        "The soil is London soil — part clay, part grit, the earth of a city that has been lived in for two thousand years."

        "She puts the tree in the ground."

        "She's crying."

        "The sun is shining and she's crying and the tree is small and the hole is too big and the earth won't pack properly and she's on her knees in the dirt and—"

        "She pats the soil down. She sits beside the tree."

        a "This is for you."

        "She doesn't say who."

        a "I'm sorry. I'm so sorry. I should have been there. I should have knocked harder, texted more, noticed sooner."

        "The tree doesn't answer. Trees don't."

        a "But I'm going to keep trying. Not because you'd want me to — I don't know what you'd want. I never really knew what you wanted."

        "She wipes her face."

        a "But I'm going to keep trying. Because that's the only thing I know how to do now."

        "The rowan. Small, green, alive."

        "The sun. The park. The sound of London, distant."

        "She sits beside the tree for a long time."

        "Then she goes home."

        # --- SONG SLIDESHOW: "Daffodils in the Snow" — Grief ending ---
        call slideshow_ch12_daffodils_grief

        scene black
        with fade

        centered "{size=+6}THE GRIEF{/size}\n\n{size=+2}Amelia carries the loss. Not as a weight to drag but as a seed to plant.\nShe will learn to live with grief. It will take longer than a year.\nBut she will learn.{/size}"

    ## =====================================================================
    ## ENDING 2: THE ALCHEMIST
    ## The rarest ending. The hidden gold.
    ## =====================================================================

    elif ending == "the_alchemist":

        # play music "audio/ending_alchemist.ogg" fadein 3.0 volume 0.4

        "She doesn't go home."

        "Not directly."

        scene bg_cornwall_coast
        with dissolve

        "She takes the branch line. Back to Cornwall. One more time."

        "Elena is waiting at the station."

        elena "I knew you'd come."

        a "How?"

        elena "An gwella."

        "They drive to the moor."

        scene bg_men_an_tol
        with dissolve

        "The Mên-an-Tol at dawn."

        "The holed stone. The passage. The oldest medicine in Cornwall — crawl through to be healed."

        elena "Last time."

        a "Last time."

        "She crawls through."

        "On the other side—"

        "The moor is the same. But different. The colours are — vivid. Turned up. The green is greener. The granite is whiter. The sky is so blue it hurts."

        "Elena is standing on the other side. She's smiling."

        "Amelia has never seen her smile."

        elena "Welcome home."

        a "Is this — is this what it looks like? The gold?"

        elena "This is what it always looked like. You can see it now."

        "The moor. The stone. The wind."

        "Amelia stands in the centre of it like a woman standing in the centre of a fire that no longer burns."

        a "What do I do now?"

        elena "You go back. You live. You see."

        "A pause."

        elena "And you come back. When you're ready. There is always more Work."

        "The sun rises. The gold light pours over everything."

        "Amelia opens her journal. She writes one word."

        "{i}Gold.{/i}"

        # --- SONG SLIDESHOW: "Daffodils in the Snow" — Alchemist ending ---
        call slideshow_ch12_daffodils_alchemist

        scene black
        with fade

        centered "{size=+6}THE ALCHEMIST{/size}\n\n{size=+2}The Work is done — the first Work. The gold is real.\nAmelia sees the world differently now. She always will.\nSome would call it wisdom. Elena calls it sight.\nThe fire doesn't end. It just changes what it burns.{/size}"

    ## =====================================================================
    ## ENDING 3: THE SCHOLAR
    ## The mind as gold. Knowledge transformed by experience.
    ## =====================================================================

    elif ending == "the_scholar":

        # play music "audio/ending_scholar.ogg" fadein 3.0 volume 0.4

        scene bg_library
        with dissolve

        "She goes back to the library."

        "One last time. Not for an assignment — just... one last time."

        "Her seat. The corner by the history section. The afternoon light."

        "An email."

        "From Hawthorne. (Or Simmons, or the department — it doesn't matter. What matters is the words.)"

        "{i}\"Dear Amelia, We are pleased to offer you a summer research assistantship in the Department of Psychology. Based on your academic performance and the exceptional quality of your recent work, we believe you would be an excellent candidate for...\"{/i}"

        "Her hands shake."

        "She reads it twice. Three times."

        "Then she calls Ella."

        ella "Hey! Are you on the train?"

        a "I found my thing."

        ella "What?"

        a "I found my thing, Els. I actually found my thing."

        "They talk for an hour. The library empties around her. The light moves across the desk."

        "She opens a new notebook. Blank pages. The specific thrill of work that matters."

        "She writes a title. The beginning of the beginning."

        # --- SONG SLIDESHOW: "Daffodils in the Snow" — Scholar ending ---
        call slideshow_ch12_daffodils_scholar

        scene black
        with fade

        centered "{size=+6}THE SCHOLAR{/size}\n\n{size=+2}Amelia finds her vocation. Not just knowledge — understanding.\nThe mind that was hungry is still hungry, but now it knows\nwhat it's hungry for. The library is her laboratory.\nThe gold is in the thinking.{/size}"

    ## =====================================================================
    ## ENDING 4: THE COMPANION
    ## Connection as gold. The alchemist discovers the laboratory was people.
    ## =====================================================================

    elif ending == "the_companion":

        # play music "audio/ending_companion.ogg" fadein 3.0 volume 0.4

        scene bg_flat_kitchen
        with dissolve

        "She misses the first train."

        "On purpose."

        "Because Raj said 'one more lunch' and Liz said 'you can't leave on an empty stomach' and Lucas looked at her and she said 'fine, one more lunch.'"

        "The lunch stretches. Into the afternoon. Into the evening."

        "Raj cooks. Of course he does. Daal, because that's where it started."

        "Maya appears with wine — 'Elena sent it. Said it was for celebrations.' Lucas brings a speaker. Liz does a playlist."

        if sarah_alive:
            if sarah_outcome == "full_save" or sarah_outcome == "late_save":
                "Sarah calls. On speakerphone."

                sarah "I can hear Raj's daal from Devon."

                raj "That's the cumin."

                sarah "Save me a bowl. I'll be there in September."

        "They sit around the table. The kitchen — {i}their{/i} kitchen — is warm and full and the light is golden."

        lucas "I'm not making a speech."

        liz "Nobody asked you to."

        lucas "Good."

        "A pause."

        lucas "But — I'm glad you're all here."

        "It's the most Lucas has ever said about his feelings. The table goes silent."

        raj "Mate..."

        lucas "Don't."

        "But he's smiling."

        "Amelia looks at them. This ridiculous, beautiful, broken, repaired, still-repairing group of humans."

        thought "This is the gold. This table. These people. This specific, unrepeatable configuration of love."

        "She takes the last train. She texts from the carriage:"

        "{i}amelia: i'm going to miss you idiots more than is medically advisable{/i}"

        "{i}raj: same{/i}"

        "{i}liz: 😭❤️{/i}"

        "{i}lucas: see you in september{/i}"

        # --- SONG SLIDESHOW: "Daffodils in the Snow" — Companion ending ---
        call slideshow_ch12_daffodils_companion

        scene black
        with fade

        centered "{size=+6}THE COMPANION{/size}\n\n{size=+2}Amelia discovers that the great work was never solitary.\nThe laboratory was the kitchen. The fire was love.\nThe gold is in the people who stayed.{/size}"

    ## =====================================================================
    ## ENDING 5: THE HEALER
    ## Compassion as gold. The wound becomes the gift.
    ## =====================================================================

    elif ending == "the_healer":

        # play music "audio/ending_healer.ogg" fadein 3.0 volume 0.4

        scene bg_amelia_home
        with dissolve

        "Home."

        "A week passes. She sleeps. She eats Grace's cooking. She argues with Lily about the bathroom. She helps David in the garden."

        "Normal things."

        "Then, a Tuesday. An email she applied for weeks ago and forgot about."

        "{i}\"Dear Amelia, We are delighted to offer you a volunteer position at the Samaritans Plymouth branch...\"{/i}"

        scene bg_counsellor_office
        with dissolve

        "The training room. Twelve volunteers. A trainer with kind eyes and a name badge."

        "They practice. Role play. Scripts. Active listening."

        "Then the first real shift."

        "The phone rings."

        "It's 11pm. The caller is anonymous. The voice is quiet."

        "Amelia picks up."

        a "Hello. Samaritans. My name is Amelia."

        "A pause."

        "Then:"

        "'I don't know why I'm calling.'"

        a "That's okay. You don't need a reason."

        "'I just — I needed someone to be there.'"

        a "I'm here."

        "She doesn't know what to say next."

        "But she stays on the line."

        "Because that's what matters. Not the words. Not the right thing. Just — being there."

        if sarah_alive:
            "Her phone buzzes after the shift. A text from Sarah."

            "{i}sarah: photo attached{/i}"

            "A sunrise. Devon. The moor."

            "{i}sarah: i watched this today. thought of you. x{/i}"

        # --- SONG SLIDESHOW: "Daffodils in the Snow" — Healer ending ---
        call slideshow_ch12_daffodils_healer

        scene black
        with fade

        centered "{size=+6}THE HEALER{/size}\n\n{size=+2}Amelia stays on the line. She will always stay on the line.\nThe wound becomes the gift. The one who was afraid\nlearns that courage isn't the absence of fear.\nIt's the phone ringing at 11pm, and picking up anyway.{/size}"

    ## =====================================================================
    ## ENDING 6: THE WHOLE
    ## Integration. Not perfect. Enough.
    ## =====================================================================

    elif ending == "the_whole":

        # play music "audio/ending_whole.ogg" fadein 3.0 volume 0.4

        "The train. London approaching."

        "She doesn't read. She doesn't write. She watches."

        scene bg_london_train
        with dissolve

        "Devon becomes Somerset becomes Surrey becomes London."

        "Her phone has texts from everyone."

        "From Ella: {i}\"I'm at Paddington. We're getting coffee. Non-negotiable.\"{/i}"

        if mentor_path == "hawthorne":
            "From Hawthorne: {i}\"Your essay mark: 78%%. Don't let it go to your head. — AH\"{/i}"
        elif mentor_path == "simmons":
            "From Simmons: {i}\"You did beautifully. Go home and rest. That's a prescription.\"{/i}"
        elif mentor_path == "maya":
            "From Maya: {i}\"The sun rises every day. So will you.\"{/i}"
        elif mentor_path == "elena":
            "From Elena: {i}\"Meur ras. Duw genes. The Work continues.\"{/i}"

        "From Raj: a photo of the kitchen, empty, with a handwritten sign on the table: \"RESERVED FOR WORLD'S WORST CHESS PLAYER.\""

        "From her mother: {i}\"Your room is ready. Dad made bolognese. (Ragù.) Love you.\"{/i}"

        scene bg_plymouth_hoe_day
        with dissolve

        "She closes her eyes."

        "She sees: her mentor's office, golden with afternoon light. The Hoe at dawn. The library. The kitchen. Cornwall — a standing stone against sky. A candle in darkness."

        if sarah_alive:
            "She sees Sarah's face. In the hospital. Looking at her. Alive."
        else:
            "She sees Sarah's bench. The brass plaque. Fresh flowers."

        "She opens her eyes."

        scene bg_london_train
        with dissolve

        "The train. England outside the window."

        "Nothing is perfect. Her exams were good, not brilliant. Her friendships are real, not uncomplicated. She is changed, not complete. She is still afraid, still uncertain, still the woman who lies awake at 3am wondering if she's enough."

        "But."

        "She is more than she was. She knows more of herself. She carries less weight and more understanding."

        "Paddington. The doors open."

        "Ella is there. In the new leather jacket. With two oat milk flat whites."

        ella "Welcome home, stranger."

        "Amelia steps off the train."

        "The sun is shining."

        # --- SONG SLIDESHOW: "Daffodils in the Snow" — Whole ending ---
        call slideshow_ch12_daffodils_whole

        scene black
        with fade

        centered "{size=+6}THE WHOLE{/size}\n\n{size=+2}Nothing is perfect. Everything is enough.\nAmelia is not one thing — scholar, healer, seeker, friend.\nShe is all of them, imperfectly. The gold is in the balance.\nThe stone was always there. She can see it now.{/size}"

    ## =====================================================================
    ## ENDING 7: THE BITTERSWEET
    ## The most realistic ending. The most common. The most human.
    ## =====================================================================

    else:

        # play music "audio/ending_bittersweet.ogg" fadein 3.0 volume 0.4

        "The train."

        scene bg_london_train
        with dissolve

        "She watches the landscape change."

        "Cornwall disappeared behind a headland twenty minutes ago. Devon is green and rolling. Somerset is flat."

        "Some things worked this year. Some didn't."

        "She made friends. She lost someone. She passed her exams. She failed at things she didn't know she could fail at. She learned what she's made of, and it's softer and harder and stranger than she expected."

        "The train rocks. The rhythm of it."

        "She opens her journal. The first page — September. Her handwriting is different. Tighter. More afraid."

        "{i}September 15th. Plymouth. I'm here. The room is small. The bed is hard. I don't know anyone. I think I've made a terrible mistake.{/i}"

        "She turns to the last page. Blank."

        "She writes."

        "{i}June 12th. The train home.{/i}"

        "{i}I don't know what I am yet. But I know what I've been. And I think that's a start.{/i}"

        "She closes the journal."

        "The train crosses into London. The buildings multiply. The sky gets smaller."

        "Paddington."

        "She picks up her bag. She steps off the train."

        "Somewhere, a lifetime away, the sea is still there. Cornwall. The moors. The stones."

        "Still there. Even when you can't see them."

        # --- SONG SLIDESHOW: "Daffodils in the Snow" — Bittersweet ending ---
        call slideshow_ch12_daffodils_bittersweet

        scene black
        with fade

        centered "{size=+6}THE BITTERSWEET{/size}\n\n{size=+2}The most honest ending. Some gold, some lead.\nAmelia doesn't know what comes next.\nBut the sea is still there, even when you can't see it.\nThe work is never finished. And that's okay.{/size}"

    ## =====================================================================
    ## CREDITS
    ## =====================================================================

    # --- SONG SLIDESHOW: "Amelia" — The protagonist's anthem / credits theme ---
    call slideshow_ch12_amelia_credits

    scene black
    with dissolve

    pause 3.0

    centered "{size=+6}THE CK: AMELIA{/size}\n\n{size=+2}A story about a girl who went to university\nand came back different.{/size}"

    pause 4.0

    centered "Thank you for playing."

    pause 3.0

    if not sarah_alive:
        centered "If this story affected you, please reach out.\n\n{b}Samaritans:{/b} 116 123 (24hr, free)\n{b}Shout:{/b} Text SHOUT to 85258\n{b}CALM:{/b} 0800 58 58 58\n{b}Papyrus:{/b} 0800 068 4141"
        pause 5.0

    ## -----------------------------------------------------------------------
    ## END OF GAME
    ## -----------------------------------------------------------------------

    return
