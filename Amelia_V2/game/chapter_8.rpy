###############################################################################
##
##  CHAPTER 8: THE ORDEAL
##
##  Hero's Journey: The supreme crisis — death and rebirth.
##  Alchemical Stage: Citrinitas — the yellowing; burning in the furnace.
##  Month: February. Location: Plymouth.
##  Palette: Dark. Rain. Occasional terrible gold where the light breaks.
##  Music: Sparse. Piano. Silence. The sound of rain.
##
##  CONTENT WARNING: This chapter deals with depression, self-harm,
##  suicidal ideation, and (potentially) suicide.
##
##  Scenes: 7–10 (varies by Sarah outcome) | Choices: 4–5
##  Max earnable: ~8–10 pts (negatives possible)
##
###############################################################################

label chapter_8:

    $ current_chapter = 8
    stop music fadeout 1.0
    scene black
    with fade

    ## -----------------------------------------------------------------------
    ## CONTENT WARNING
    ## -----------------------------------------------------------------------

    centered "{size=+6}Content Warning{/size}\n\nThis chapter contains depictions of depression, self-harm,\nand suicidal ideation.\n\nIf you or someone you know is struggling:\n\n{b}Samaritans (UK):{/b} 116 123 (24hr, free)\n{b}Shout Crisis Text Line:{/b} Text SHOUT to 85258\n{b}CALM:{/b} 0800 58 58 58\n{b}Papyrus (under 35):{/b} 0800 068 4141"

    pause 6.0

    ## -----------------------------------------------------------------------
    ## TITLE CARD
    ## -----------------------------------------------------------------------

    scene black

    centered "{size=+20}Chapter Eight{/size}\n\n{size=+6}The Ordeal{/size}"
    pause 3.0

    ## =====================================================================
    ## ACT 1: THE CRACKS WIDEN
    ## Amelia's own mental health frays.
    ## =====================================================================

    ## SCENE 8.1 — AMELIA'S OWN CRISIS

    scene bg_amelia_room_plymouth_night
    with dissolve

    # play music "audio/ch8_crisis.ogg" fadein 3.0 volume 0.3

    "February. The rain hasn't stopped for eleven days."

    "Amelia sits at her desk. The essay is due tomorrow. The screen is open. The cursor blinks."

    "She has written: {i}'Discuss the role of attachment theory in understanding adult relationships.'{/i}"

    "That's the title. She's been staring at it for three hours."

    "The room is dark. She hasn't turned the light on because turning the light on would mean admitting she's awake, which would mean admitting the essay isn't written, which would mean admitting she is failing."

    thought "I can't do this."

    "The thought arrives with the weight of fact."

    thought "I can't do this. I'm not smart enough. I was never smart enough. Sophia could write this in her sleep. Hawthorne would read my draft and his eyebrow would do the thing and—"

    "The spiral."

    thought "I missed the statistics deadline. I missed it and I didn't tell anyone. That's fourteen percent of the module gone. Just gone. And the developmental essay got 62%% and I thought I'd done well and 62%% is not doing well. 62%% is mediocre. Mediocre is—"

    "She pushes back from the desk."

    "It's 2am. She hasn't eaten since noon. She's slept four hours in the last two days."

    "The rain is louder than it should be."

    ## =====================================================================
    ## CHOICE 8.1 — AMELIA'S OWN CRISIS
    ## =====================================================================

    menu:
        "It's 2am. She can't write. She can't sleep. She can barely think."

        "Reach out to her mentor.":
            $ ch8_crisis = "mentor"
            $ add_stat("stat_mh", 1)
            if mentor_path == "hawthorne":
                $ add_rel("rel_hawthorne", 1)
            elif mentor_path == "simmons":
                $ add_rel("rel_simmons", 1)
            elif mentor_path == "maya":
                $ add_rel("rel_maya", 1)
            elif mentor_path == "elena":
                $ add_rel("rel_elena", 1)

            "She emails. At 2am. She doesn't care."

            "{i}\"I'm struggling. I've missed a deadline. I can't write this essay. I don't know what to do.\"{/i}"

            "She doesn't expect a response until morning."

            if mentor_path == "hawthorne":
                "At 2:14am:"

                "{i}\"Miss James. Extensions exist for a reason. Email the department. Write your essay tomorrow. Go to bed. — AH\"{/i}"

                thought "He's awake at 2am answering student emails. That's either dedication or insomnia. Either way — he answered."

            elif mentor_path == "simmons":
                "At 7:30am, her phone rings."

                simmons "Right. You're having a bad night. We've all had bad nights. Here's what's going to happen: you're going to eat breakfast, you're going to walk to my office, and we're going to work this out. Okay?"

                a "Okay."

                simmons "Good girl. Bring biscuits."

            elif mentor_path == "maya":
                "At 6am, a text:"

                "{i}maya: meet me on the hoe. sunrise. we breathe first. the essay comes after.{/i}"

            elif mentor_path == "elena":
                "At 3am:"

                "{i}elena: the fire burns hottest before the work is done. you're in it now. don't fight it. let it transform you. but also — email the department for an extension. both things can be true.{/i}"

        "Reach out to friends.":
            $ ch8_crisis = "friends"
            $ add_stat("stat_si", 1)

            "She texts the group chat."

            "{i}amelia: i'm having a really really bad night and i don't know what to do{/i}"

            "2:03am."

            "{i}raj: kitchen. now. i'm putting the kettle on.{/i}"

            "Within fifteen minutes, Raj and Liz are in the kitchen. Lucas appears five minutes later, bleary-eyed, carrying his duvet."

            "Nobody tells her it'll be okay. Raj makes tea. Liz puts on her playlist — the one she calls 'Songs for When the Brain is Being a Dick.' Lucas sits beside her with his duvet and says nothing, which is somehow exactly right."

            "At 3am, she's laughing about something stupid — Raj's impression of Hawthorne, or the fact that Lucas brought an entire duvet to the kitchen like a medieval knight bringing a shield."

            thought "I'm still failing. The essay still isn't written. But I'm here. I'm not alone. And that's the difference between drowning and just... being in deep water."

        "Isolate. Try to handle it alone.":
            $ ch8_crisis = "isolate"
            $ add_stat("stat_mh", -1)

            "She closes the laptop. She gets into bed."

            "She doesn't text anyone. She doesn't email. She lies in the dark and listens to the rain and waits for morning."

            "Morning comes. The essay isn't written. The deadline passes."

            "She goes to lectures. She sits at the back. She doesn't speak."

            thought "I'm fine. I'm handling it. This is what handling it looks like."

            "It isn't."

    ## =====================================================================
    ## SCENE 8.2 — TASHA'S HARMFUL ACT
    ## Consequences for someone Amelia cares about.
    ## =====================================================================

    scene bg_campus_quad
    with dissolve

    "Three days later."

    "Tasha does something."

    "Not the usual — not a photo, not a comment, not the subtle blade of social exclusion."

    "Something worse."

    "Zara's presentation in Simmons' seminar. She's been working on it for weeks — a case study on inherited trauma and resilience in immigrant communities. It's personal. It's brave. It's the best thing Zara has ever produced."

    "In the middle of the presentation, Tasha's phone pings. Then Liz's. Then three others."

    "An anonymous Instagram account has posted Zara's presentation slides — screenshot after screenshot — with comments. Mocking the personal sections. Mocking the grammar. Mocking the topic."

    "{i}'Imagine making your dead grandma your entire personality 💀'{/i}"

    "Zara sees the notifications. Mid-sentence. She stops speaking."

    "The room is silent."

    "Simmons, to her credit, shuts it down instantly."

    simmons "Phones away. All of you. Now."

    "But the damage is done. Zara stands at the front. Her mouth opens. Nothing comes out."

    "She picks up her notes. Walks out."

    ## =====================================================================
    ## CHOICE 8.2 — TASHA'S HARMFUL ACT
    ## =====================================================================

    menu:
        "Zara walks past Amelia. The corridor is ahead. The decision is now."

        "Confront Tasha with compassion — \"Why are you doing this?\"":
            $ ch8_tasha = "compassion"
            $ add_stat("stat_mc", 1)
            $ add_stat("stat_si", 1)
            $ add_rel("rel_tasha", 2)

            "After checking Zara is with Simmons, Amelia finds Tasha. Not in the café — in the bathroom. Alone."

            "Tasha is looking at her phone. Her expression is — complicated. Not triumphant. Something else."

            a "Why?"

            tasha "I don't know what you're—"

            a "Tasha. Please. Just — why?"

            "The bathroom is white tile and fluorescent light and the sound of a dripping tap. Nowhere to hide."

            a "Zara hasn't done anything to you. Her presentation was about her family. Her grandmother. Why would you do that?"

            "Tasha's jaw tightens."

            tasha "Because—"

            "Something crosses her face. Fear. Or pain."

            tasha "Because she had something to say. And I don't."

            "Silence."

            tasha "Her presentation was real. It was about something real. And mine was about... data. Just data. Nobody's ever going to cry over my data."

            "She looks at Amelia. For the first time, the mask is off."

            tasha "I know that's not an excuse."

            a "It's not."

            tasha "I know."

            "A pause."

            a "You need to take it down. And you need to apologise. To Zara's face."

            tasha "I—"

            a "Not for me. For yourself. Because if you don't, this is who you'll be forever."

        "Confront Tasha with anger — \"This ends now.\"":
            $ ch8_tasha = "anger"
            $ add_stat("stat_mc", 1)
            $ add_rel("rel_tasha", -1)

            "She finds Tasha in the corridor. She doesn't wait."

            a "Take it down."

            tasha "Take what—"

            a "The account. The posts. Take it all down right now or I go to the dean and I bring screenshots and I bring names and I will make sure everyone knows it was you."

            "Tasha stares at her."

            a "You've been doing this all year. The photos. The graffiti. The complaint. And now this — her grandmother, Tasha. Her {i}grandmother{/i}."

            "Tasha's face is rigid. Stone."

            a "Take it down. Now."

            "An hour later, the account is deleted."

            "Tasha doesn't speak to Amelia again. Not for the rest of term. Not a word."

        "Report it formally.":
            $ ch8_tasha = "report"
            $ add_stat("stat_mc", 1)

            "Amelia goes to Simmons. Then to the student welfare office. Then to the dean of students."

            "She brings everything — screenshots, the history, the pattern."

            "The formal process is longer this time. More serious."

            "Tasha receives a final warning and mandatory counselling. The anonymous account is traced and deleted."

            "It's the right thing. It's the institutional thing. It works."

            "But Tasha, in the counselling sessions, sits in silence. The mechanism processed her. It didn't reach her."

        "Do nothing.":
            $ ch8_tasha = "nothing"
            $ add_stat("stat_mc", -1)

            "Amelia watches Zara leave."

            "She tells herself she'll do something. Later. When she's figured out what."

            "She doesn't."

            "Zara handles it herself. Simmons helps. The account comes down."

            "But the text Amelia gets from Zara says more than words:"

            "{i}zara: thanks for nothing.{/i}"

    ## =====================================================================
    ## ACT 2: SARAH'S CRISIS — THE CENTRAL EVENT
    ## =====================================================================

    # --- SONG SLIDESHOW: "Oh Sarah" — Reaching out to someone in darkness ---
    call slideshow_ch8_oh_sarah

    scene black
    with dissolve

    # play music "audio/ch8_sarah_crisis.ogg" fadein 3.0 volume 0.3

    "Three days of silence."

    "Sarah's door stays closed."

    "The first day, nobody thinks much of it."

    "The second day, Raj knocks. No answer."

    "The third day—"

    ## -----------------------------------------------------------------------
    ## SARAH SCORE CALCULATION
    ## -----------------------------------------------------------------------

    python:
        sarah_score = (rel_sarah * 3) + stat_mh + stat_si + stat_mc + int(rel_ella * 0.5)

        # Elena bonus
        if mentor_path == "elena" and stat_ok >= 18:
            sarah_score += 10

        # Determine tier
        if sarah_score >= 45:
            sarah_outcome = "full_save"
        elif sarah_score >= 30:
            sarah_outcome = "late_save"
        elif sarah_score >= 15:
            sarah_outcome = "partial_save"
        else:
            sarah_outcome = "tragic"
            sarah_alive = False

    ## =====================================================================
    ## TIER 1: FULL SAVE (sarah_score >= 45)
    ## Amelia gets there before the attempt. Early intervention.
    ## =====================================================================

    if sarah_outcome == "full_save":

        scene bg_halls_corridor
        with dissolve

        "The third day."

        "Amelia doesn't wait for a reply. She doesn't text. She goes to Sarah's door."

        "She knocks."

        a "Sarah."

        "No answer."

        a "Sarah, I'm coming in."

        "The door is unlocked."

        "Inside: the room is dark. Curtains closed. The air is stale — days of not opening a window. On the desk, a notebook open to a page of handwriting. Sarah's handwriting. A list."

        "A list of people. A list of things she wants them to know."

        "Sarah is on the bed. She's not asleep. She's staring at the ceiling."

        "Amelia sees the notebook. Sees the list. Sees the bottle of pills on the desk beside a glass of water."

        "Her hands go cold."

        "She doesn't panic. Something in her — everything she's learned, everything she's become — holds."

        a "Sarah. I'm here."

        sarah "Go away."

        a "No."

        "She sits on the bed."

        a "I'm not leaving. I'm calling someone who can help. And I'm staying here while they come."

        "She calls 999. Her voice is steady. She doesn't know how."

        "The ambulance takes seventeen minutes. In those seventeen minutes, Amelia sits beside Sarah and says nothing that matters and everything that matters."

        a "I'm here."

        "Again and again."

        a "I'm here."

        "Sarah doesn't speak. But she doesn't move towards the pills. And when the paramedics knock, she lets them in."

    ## =====================================================================
    ## TIER 2: LATE SAVE (sarah_score 30–44)
    ## The attempt has happened. Sarah is found in time.
    ## =====================================================================

    elif sarah_outcome == "late_save":

        scene bg_halls_corridor
        with dissolve

        "The third day."

        "Amelia goes to Sarah's door. A feeling — not logic, not deduction, something older than both."

        "The door is unlocked."

        "Inside—"

        "Sarah."

        "She's on the floor. The pills are scattered. She's conscious but barely."

        "Amelia's body moves before her mind does. She's on the floor beside her. She's calling 999. She's saying things — Sarah's name, the address, the situation — and her voice sounds like it belongs to someone else."

        "The ambulance takes twelve minutes."

        sarah "Why did you come?"

        "Her voice is a thread."

        a "Because I'm your friend."

        sarah "Why couldn't you just leave me alone?"

        "Amelia holds her hand."

        a "Because friends don't leave."

        "The paramedics arrive. They work with the calm efficiency of people who have seen this before. They take Sarah. Amelia rides in the ambulance because she refuses to let go of her hand."

    ## =====================================================================
    ## TIER 3: PARTIAL SAVE (sarah_score 15–29)
    ## Sarah is found by someone else. Survives. Damaged.
    ## =====================================================================

    elif sarah_outcome == "partial_save":

        scene bg_amelia_room_plymouth_night
        with dissolve

        "Amelia's phone rings."

        "It's Liz."

        liz "Amelia. You need to come to the hospital."

        "The floor tilts."

        a "What—"

        liz "It's Sarah. The cleaner found her. She took — she took pills. She's alive. But you need to come."

        "The words arrive one at a time, like stones dropped into still water."

        "Sarah is alive."

        "Sarah took pills."

        "The cleaner found her. Not Amelia. The cleaner."

    ## =====================================================================
    ## TIER 4: TRAGIC (sarah_score < 15)
    ## Sarah is gone.
    ## =====================================================================

    elif sarah_outcome == "tragic":

        scene bg_counsellor_office
        with dissolve

        "A room she's never been in. Beige walls. A box of tissues on the desk."

        "A counsellor. A woman with kind eyes and a name badge that says DR. ANWEN PRICE."

        "She says: 'Please sit down, Amelia.'"

        "The words come."

        "Sarah is dead."

        "The counsellor says more. Words. The shapes of words. Time of discovery. Emergency services. Next of kin notified."

        "Amelia hears none of it."

        "Sarah is dead."

        "She sits in the beige room and the world rearranges itself into the shape of a world without Sarah Whitmore in it, and the new shape is wrong, fundamentally wrong, like a building without a load-bearing wall."

        "She doesn't cry. She will. Later. But now — just the fact. The fact sitting in her chest like a stone."

    ## =====================================================================
    ## CHOICE 8.3 — THE MOMENT (If in save tier)
    ## =====================================================================

    if sarah_alive:

        if sarah_outcome == "full_save" or sarah_outcome == "late_save":

            menu:
                "Sarah is in the ambulance. Amelia is in the corridor. The paramedics have taken over."

                "Stay with her. Don't leave her side.":
                    $ ch8_moment = "stay"
                    $ add_stat("stat_mh", 1)
                    $ add_stat("stat_mc", 1)
                    $ add_rel("rel_sarah", 2)

                    "She goes with the ambulance. She sits in the hospital corridor. She calls nobody. She waits."

                    "Four hours. The fluorescent lights. The squeaking shoes. The specific hospital smell of disinfectant and fear."

                    "A nurse comes out."

                    "She's stable."

                    "Amelia puts her head in her hands and cries. In the hospital corridor, at 3am, under fluorescent lights that make everything look like the end of the world."

                    "She cries because it worked. It worked. All of it — the texts, the doorknock, the listening, the staying — it worked."

                    "And she cries because it almost didn't."

                "Run for help — get Raj, Liz, let people know.":
                    $ ch8_moment = "help"
                    $ add_stat("stat_mc", 1)
                    $ add_rel("rel_sarah", 1)

                    "She runs. Back to the flat. Wakes Raj, wakes Liz."

                    raj "What — Amelia, what's—"

                    a "It's Sarah. She needs — the hospital — please just come."

                    "They come. All of them. The whole flat, in pyjamas and coats, in Raj's car and a taxi."

                    "The hospital waiting room. Five students sitting in plastic chairs at 1am. Nobody speaks."

                    "When the news comes — stable, alive, being treated — Raj puts his head on the table and Liz holds his hand and Lucas stares at the wall and Amelia thinks: {i}this is what a net looks like. A human net.{/i}"

                "Freeze — overwhelmed by the situation.":
                    $ ch8_moment = "freeze"

                    "She can't move."

                    "The paramedics has taken Sarah. The corridor is empty. The door is open. Sarah's room — the pills, the list, the stale air."

                    "Amelia stands there."

                    "How long? She doesn't know. Long enough for Liz to find her. Long enough for Liz to say 'Amelia? Amelia, look at me' and take her hand and lead her to the kitchen and make tea."

                    "Sarah is alive. Amelia is standing in a corridor. These are facts."

                    "She clings to them."

        elif sarah_outcome == "partial_save":

            "Amelia goes to the hospital."

            "She sits in the waiting room. The fluorescent lights hum."

            "A nurse tells her Sarah is stable. She can visit tomorrow."

            "Tomorrow."

            menu:
                "Sarah survived. But the distance between them has never felt wider."

                "Go see her tomorrow, regardless.":
                    $ ch8_moment = "visit"
                    $ add_stat("stat_si", 1)
                    $ add_rel("rel_sarah", 1)

                    "She goes."

                    "Sarah is in a hospital bed. She looks small. She doesn't look at Amelia."

                    sarah "Where were you?"

                    "The question is a knife."

                    a "I'm sorry. I should have—"

                    sarah "It doesn't matter."

                    "But it does."

                "Give her space. You've done enough damage.":
                    $ ch8_moment = "space"

                    thought "I wasn't there. I should have been there and I wasn't."

                    "She texts: {i}i'm so sorry. i'm here when you're ready. x{/i}"

                    "No reply. Not for a long time."

    ## =====================================================================
    ## ACT 3: IN THE ASHES
    ## =====================================================================

    # --- SONG SLIDESHOW: "Bare With Me" — The emotional centre of the game ---
    call slideshow_ch8_bare_with_me

    scene black
    with fade

    # play music "audio/ch8_ashes.ogg" fadein 3.0 volume 0.3

    ## =====================================================================
    ## PATH: SARAH LIVES
    ## =====================================================================

    if sarah_alive:

        scene bg_plymouth_hoe_day
        with dissolve

        "The days after."

        "The rain stops. Not because the universe is kind but because weather is weather. The sun comes out and Plymouth gleams, oblivious."

        if sarah_outcome == "full_save":
            "Sarah is in hospital. She's stable. She's eating. She's talking to a psychiatrist. She's going to be okay — not in the tidy, resolved way of television. In the real way, which is slow and uneven and full of days that are better and days that aren't."

            "Amelia visits. Reading material. Ginger biscuits. A drawing Raj did of the wren tattoo, done from memory, brilliant."

            "Sarah looks at it."

            sarah "Tell him he got the wing wrong."

            a "Tell him yourself."

            "A pause. Then a ghost of a smile."

            sarah "I will. When I'm out."

        elif sarah_outcome == "late_save":
            "Sarah is in hospital. The damage is real — physically, emotionally. She's angry. Not at Amelia specifically. At everything."

            "When Amelia visits, Sarah sometimes talks and sometimes stares at the wall."

            sarah "I don't want your pity."

            a "This isn't pity."

            sarah "Then what is it?"

            a "It's me. In a chair. With biscuits."

            "A long silence."

            sarah "...What kind of biscuits?"

            "It's not forgiveness. It's a start."

        elif sarah_outcome == "partial_save":
            "Sarah's parents come from Devon. Her father stands in the hospital corridor in a coat that smells of farm soil and says nothing. Her mother cries. They take her home."

            "Amelia helps pack Sarah's room. The books. The notebooks. The wren sketch she'd pinned to the wall."

            "When the room is empty, she stands in it. The same four walls. But the person who lived in them is gone."

            thought "She survived. That's what matters. She survived."

            "But the word 'survived' sounds different now. It sounds like the minimum. And the minimum isn't enough."

        ## =====================================================================
        ## CHOICE 8.5 — AFTERMATH (Sarah lives)
        ## =====================================================================

        menu:
            "The crisis is over. The living comes next."

            "Visit Sarah regularly — be there, consistently.":
                $ ch8_aftermath = "visit"
                $ add_stat("stat_si", 1)
                $ add_rel("rel_sarah", 1)

                if sarah_outcome == "full_save" or sarah_outcome == "late_save":
                    "She goes every other day. Not because someone told her to. Because showing up is the only language that works right now."

                    "Some visits they talk. Some visits they sit in silence and watch the car park through the window."

                    "One afternoon, Sarah draws in her notebook while Amelia reads. It's the most peaceful hora either of them has spent in months."
                else:
                    "She sends letters. Actual letters — handwritten, on paper, because Sarah's mum said she's not looking at her phone."

                    "The first letter gets no reply. The second gets a text from Sarah's mum: {i}'She read it. Thank you.'{/i}"

                    "The third letter gets a reply. Sarah's handwriting. Three words: {i}'I'm trying. S.'{/i}"

            "Give Sarah space — check in, but don't crowd her.":
                $ ch8_aftermath = "space"
                $ add_stat("stat_mh", 1)
                $ add_rel("rel_sarah", 1)

                "She texts. Once a week. Small things. A photo of the sunset from the Hoe. A link to a song. 'Thinking of you x.'"

                "Sarah replies sometimes. Not always. But the thread stays alive."

                thought "I can't fix this. I couldn't have fixed this. All I can do is make sure she knows someone is here."

            "Feel relieved. Pull away.":
                $ ch8_aftermath = "pull_away"
                $ add_rel("rel_sarah", -1)

                thought "She's alive. She's getting help. I can breathe."

                "The relief is enormous. So enormous it swallows everything else."

                "She doesn't visit as often. Then not at all. Texts become less frequent."

                "It's not callous. It's survival. She was so close to the fire she needs to step back."

                "But Sarah notices. And that distance becomes part of what Sarah carries."

    ## =====================================================================
    ## PATH: SARAH DIES
    ## =====================================================================

    else:

        scene bg_campus_quad
        with dissolve

        "The days after."

        "The campus continues. That's the worst part. The lectures go on. The library opens. People queue for coffee. The machine of the university grinds forward as though a girl didn't die in a room on the second floor."

        "There's a memorial. Flowers outside Sarah's door. A teddy bear someone left. A card from her parents."

        "Raj cooks Sarah's favourite meal one night. Daal with extra cumin. He makes enough for an extra person, sets an extra plate, and nobody can eat."

        "The plate sits there for the entire meal. Nobody moves it."

        "Liz cries in the bathroom every morning for a week. Lucas stops going to lectures. Maya lights candles in her room and sits with them in silence."

        "Amelia goes through the motions. She attends. She eats. She responds to emails. She performs the surface-level function of being alive."

        "Underneath: nothing. A numbness so complete it feels architectural. As though someone has removed a structural element from the building of her mind and the whole thing is standing by habit, not by engineering."

        # --- SONG SLIDESHOW: "Forgetmeknot" — A friend lost in first year ---
        call slideshow_ch8_forgetmeknot

        ## =====================================================================
        ## CHOICE 8.4 — AFTERMATH (Sarah dies)
        ## =====================================================================

        menu:
            "Sarah is gone. The world asks Amelia to keep going."

            "Let yourself grieve. Lean on friends.":
                $ ch8_aftermath = "grieve"
                $ add_stat("stat_mh", 1)
                $ add_stat("stat_si", 1)

                "She lets it in."

                "In the kitchen, one evening, she starts crying and can't stop. Raj holds her shoulder. Lucas makes tea that goes cold. Liz just sits there, and the sitting is enough."

                "She calls Ella."

                ella "Oh my god. Amelia."

                "She cries on the phone for twenty minutes. Ella doesn't hang up. Ella stays on the line and breathes with her."

                "She goes to counselling. She talks. The counsellor doesn't tell her it'll be okay. She says: 'It's okay to feel this. All of it. There's no wrong way to grieve.'"

                "It doesn't fix it. Nothing fixes it. But the grief, shared, becomes slightly less than the grief alone."

            "Channel it into purpose — \"Never again.\"":
                $ ch8_aftermath = "purpose"
                $ add_stat("stat_mc", 1)
                $ add_stat("stat_sd", 1)

                "She emails Michael."

                "{i}\"The mental health services on this campus failed my friend. She needed help and the wait was fourteen weeks. I want to do something about it. Tell me what you need.\"{/i}"

                "Michael replies within the hour."

                "They meet. They plan. The campaign for funding becomes Amelia's focus — not a replacement for grief, she knows that, but a {i}channel{/i}. A direction for the rage."

                "She doesn't let herself feel the grief properly. Not yet. But the energy goes somewhere. And somewhere is better than nowhere."

            "Shut down. Withdraw from everyone.":
                $ ch8_aftermath = "shutdown"
                $ add_stat("stat_mh", -2)
                $ add_stat("stat_si", -1)

                "She closes her door."

                "Texts go unanswered. Calls decline. She goes to lectures and sits at the back. She eats alone."

                "Raj knocks. She says she's fine."

                "Ella calls. She doesn't pick up."

                "The withdrawal is a room inside a room. She builds it brick by brick and sits in it and tells herself it's safety."

                "It isn't."

    ## =====================================================================
    ## SCENE 8.6 — THE MENTOR IN THE ASHES
    ## Each mentor meets Amelia after the crisis.
    ## =====================================================================

    if mentor_path == "hawthorne":

        scene bg_hawthorne_office
        with dissolve

        "Hawthorne's office. The door is open. He's sitting. Not at his desk — in the other chair. The student's chair."

        "He stands when she comes in. He doesn't usually stand."

        hawthorne "Sit down, Amelia."

        "It's the first time he's used her first name."

        if sarah_alive:
            hawthorne "Your friend is in good hands. The hospital and the professionals will do what they do. Your job now is to decide what {i}you{/i} do."
        else:
            hawthorne "Grief is not a problem to be solved. It is a process to be endured. And it is endured — not alone, if you have any sense."

        "He pours two cups of Earl Grey. Hands her one."

        hawthorne "I told you about my student. The one I missed. Twenty years and I still think about her every time I sit in this office."

        "He looks at her."

        hawthorne "The question you're asking — 'could I have done more?' — will follow you. The answer is: yes, probably. And also: you did what you could with what you had. Both of those things are true. The challenge is holding them at the same time."

    elif mentor_path == "simmons":

        scene bg_simmons_office
        with dissolve

        "Simmons' office. She doesn't speak when Amelia comes in."

        "She just opens her arms."

        "Amelia walks into the hug and cries."

        "They sit there for a long time. The plants grow quietly around them. The small fountain trickles."

        "When Amelia stops, Simmons makes tea."

        if sarah_alive:
            simmons "She's going to need help for a long time. And so are you. Those aren't separate things."
        else:
            simmons "You're going to want to blame yourself. I need you to hear this: it is not your fault. Depression is an illness. You are not a hospital."

        simmons "But you {i}are{/i} a person who cared enough to be here. That matters. Please hear that."

    elif mentor_path == "maya":

        scene bg_plymouth_hoe_dawn
        with dissolve

        "Maya takes her to the Hoe at dawn."

        "They don't talk."

        "They sit on the grass and watch the sun come up. Again. Like the first time."

        "After twentyminutes, Maya speaks."

        if sarah_alive:
            maya "She found the bottom. And she's still here. And you — you were part of why."
        else:
            maya "The hero's journey includes this. The thing you can't fix. The loss that doesn't make sense. The fire."

        maya "I can't make this better with words. But I can sit here with you. And the sun will come up. It always does."

    elif mentor_path == "elena":

        scene bg_madron_well
        with dissolve

        "Elena takes her to the well."

        "They sit beside the water. The clooties flutter."

        if sarah_alive:
            elena "The fire didn't ask permission. You're in it now. Breathe."

            "She ties a cloth to a branch. White."

            elena "For her."

        else:
            elena "The fire doesn't ask permission. It takes what it takes."

            "She ties a cloth to a branch. White."

            elena "For her. And for you."

        "They sit in silence until the light changes."

    ## =====================================================================
    ## CHOICE 8.6 — ACCEPTING HELP
    ## =====================================================================

    menu:
        "The mentor is here. Amelia can let them in. Or not."

        "Let the mentor in. Be honestly broken.":
            $ ch8_help = "let_in"
            $ add_stat("stat_sd", 1)
            $ add_stat("stat_mh", 1)
            if mentor_path == "hawthorne":
                $ add_rel("rel_hawthorne", 1)
            elif mentor_path == "simmons":
                $ add_rel("rel_simmons", 1)
            elif mentor_path == "maya":
                $ add_rel("rel_maya", 1)
            elif mentor_path == "elena":
                $ add_rel("rel_elena", 1)

            a "I don't know what to do."

            "She says it. The truest thing she's said in days."

            a "I don't know how to study and grieve and help and be okay all at the same time. I don't know how to be the person I was last week."

            if mentor_path == "hawthorne":
                hawthorne "You're not that person. You won't be again. That's not tragedy — that's growth. Painful growth. But growth."

            elif mentor_path == "simmons":
                simmons "You don't have to do all of those things. You just have to do the next one."

            elif mentor_path == "maya":
                maya "You're not supposed to know. Nobody knows. We just keep showing up until the shape of things changes."

            elif mentor_path == "elena":
                elena "This is the Citrinitas. The yellowing. It burns. But on the other side — gold."

        "\"I'm fine. Tell me what I need to do for my course.\"":
            $ ch8_help = "deflect"
            $ add_stat("stat_aa", 1)

            a "What do I need to submit? What deadlines have I missed?"

            if mentor_path == "hawthorne":
                "Hawthorne looks at her."

                hawthorne "Your friend is in hospital and you're asking about deadlines."

                a "I need structure. Please."

                "He gives her the deadlines. He understands."

            elif mentor_path == "simmons":
                simmons "I'll send you the extension forms. But Amelia — modules can be resat. People can't."

            elif mentor_path == "maya":
                maya "Work will wait. You won't."

            elif mentor_path == "elena":
                elena "An gwella. The sight. You have it but you're choosing not to use it."

    ## =====================================================================
    ## SCENE 8.7 — THE BOTTOM
    ## The chapter's final image.
    ## =====================================================================

    scene bg_amelia_room_plymouth_night
    with dissolve

    "Night. Her room. The rain has started again."

    # --- SONG SLIDESHOW: "Living on the Moon" — The bottom, isolation ---
    call slideshow_ch8_living_on_the_moon

    if sarah_alive:
        "Sarah is alive."

        "Amelia lies in bed and thinks about this. Turns it over like a stone in her pocket."

        "Sarah is alive because — because of luck, or timing, or the accumulated weight of a hundred small choices over eight months. Texts sent. Doors knocked on. Questions asked. Hands held."

        thought "I didn't save her. I can't save anyone. But I was there. I keep being there. And that's not the same as saving, but it's the thing that made saving possible."

    else:
        "Sarah is gone."

        "Her room is empty. The corridor is quiet. The flat is one person smaller."

        "Amelia lies in bed and tries to remember the sound of Sarah's laugh. She can almost hear it. Almost."

        thought "You couldn't have saved her. You could have been there."

        thought "But saving was never in your hands."

    "The rain on the window. The dark. The fire has burned."

    "Something survived."

    ## -----------------------------------------------------------------------
    ## HELPLINE REMINDER
    ## -----------------------------------------------------------------------

    scene black
    with fade

    centered "If anything in this chapter affected you,\nplease reach out.\n\n{b}Samaritans:{/b} 116 123 (24hr, free)\n{b}Shout:{/b} Text SHOUT to 85258\n{b}CALM:{/b} 0800 58 58 58"

    pause 5.0

    ## -----------------------------------------------------------------------
    ## END OF CHAPTER
    ## -----------------------------------------------------------------------

    centered "{size=+6}End of Chapter Eight{/size}"
    pause 2.0

    return
