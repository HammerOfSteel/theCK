###############################################################################
##
##  CHAPTER 7: THE APPROACH
##
##  Hero's Journey: The hero prepares for the central challenge.
##  Alchemical Stage: Late Albedo / Citrinitas — the yellowing; insight dawns.
##  Month: January–February. Location: Plymouth.
##  Palette: Darkening gold. Storm light. Short days, long shadows.
##  Music: Gathering intensity. Piano. Wind. Something approaching.
##
##  Scenes: 7 + 1 conditional | Choices: 6 + 1 conditional
##  Max earnable: ~8–10 pts
##
###############################################################################

label chapter_7:

    stop music fadeout 1.0
    scene black
    with fade

    ## -----------------------------------------------------------------------
    ## TITLE CARD
    ## -----------------------------------------------------------------------

    centered "{size=+20}Chapter Seven{/size}\n\n{size=+6}The Approach{/size}"
    pause 3.0

    ## =====================================================================
    ## SCENE 7.1 — THE MENTOR DEEPENS
    ## The mentor reveals something personal. Trust tested.
    ## =====================================================================

    if mentor_path == "hawthorne":

        scene bg_hawthorne_office
        with dissolve

        # play music "audio/ch7_mentor.ogg" fadein 2.0 volume 0.4

        "February. Hawthorne's office. The light is different — lower, angled, as though even the sun knows this term is harder."

        "They're reviewing her essay. It's good. She knows it's good. Hawthorne knows it's good, which he communicates by saying 'This is adequate' instead of 'This needs to be rewritten from the ground up.'"

        "Then he puts the essay down."

        hawthorne "I had a student who died."

        "The room goes still."

        hawthorne "Twenty years ago. Brilliant girl — more brilliant than anyone I've had since, and I include you in that. She had a form of depression that wasn't visible from the outside. I taught her for two years and I missed it. Every sign. Every signal."

        "He looks at his hands."

        hawthorne "I have spent twenty years trying to understand how I — a professor of psychology — failed to see a student suffering in front of me. And the answer, Miss James, is that intelligence is not empathy. Knowing the theory is not the same as recognising the person."

        "He looks at her."

        hawthorne "I tell you this because I see you making the same mistake I made. You're brilliant. But brilliance without care is just decoration."

    elif mentor_path == "simmons":

        scene bg_simmons_office
        with dissolve

        # play music "audio/ch7_mentor.ogg" fadein 2.0 volume 0.4

        "February. Simmons' office. The plants are doing something extraordinary — a cactus has flowered, a tiny pink bloom, and Simmons is more excited about it than seems reasonable for a plant."

        simmons "Look at it! Three years! Three years I've waited for this!"

        "She turns to Amelia. The excitement fades into something more grounded."

        simmons "I need to tell you something. About why I do this work."

        "She sits down. Not in her usual chair — on the floor, cross-legged, with her tea."

        simmons "When I was your age, I had an eating disorder. A bad one. Three years of it. I nearly died at twenty-one and I don't say that for drama — I say it because it's the clinical truth."

        "Amelia doesn't speak."

        simmons "I recovered. Slowly, messily, with help. And then I spent the next fifteen years becoming the person who would notice the signs I was giving and nobody saw."

        "She takes a sip of tea."

        simmons "That's why I ask how you're eating. That's why I watch. Not because I'm nosy. Because I know what it looks like when someone is hiding."

    elif mentor_path == "maya":

        scene bg_plymouth_hoe_day
        with dissolve

        # play music "audio/ch7_mentor.ogg" fadein 2.0 volume 0.4

        "February. Walking on the Hoe. It's cold but Maya doesn't seem to notice — she never seems to notice cold, as though her internal thermostat runs on enthusiasm."

        "They're talking about Jung — the Shadow, the Anima, the process of individuation — when Maya stops."

        maya "I need to tell you something."

        "She sits on the wall. Legs swinging."

        maya "I've experienced psychosis. Twice. The first time was after my mum died. The second was in my second year of uni."

        "She says it like she's reporting the weather."

        maya "I heard things. Saw patterns that weren't patterns. I was certain — absolutely certain — that the universe was sending me messages through licence plates and bird formations and the arrangement of items in my fridge."

        a "Maya..."

        maya "I'm telling you because you need to know the difference between insight and illness. Between opening the mind and losing it. I've been on both sides. And the border between them is narrower than anyone wants to admit."

    elif mentor_path == "elena":

        scene bg_madron_well
        with dissolve

        # play music "audio/ch7_mentor.ogg" fadein 2.0 volume 0.4

        "February. Elena takes her to Madron Well again. Not for the solstice — just a walk. The woods in winter. The clooties on the trees, faded."

        "They sit by the water."

        elena "My grandmother was a pellar."

        a "You've mentioned that."

        elena "I'm not mentioning it. I'm {i}telling{/i} you."

        "She pushes her hair back. The streak of silver catches the light."

        elena "She had the sight. Real or not — it doesn't matter. She believed it, her community believed it, and it worked. People came to her with their illnesses and their griefs and she helped them. With herbs, with words, with attention."

        elena "She died when I was fourteen. And I spent the next twenty years trying to understand what she knew — whether it was psychology by another name, or something else entirely."

        "She looks at the water."

        elena "I'm in the university because the language of psychology is powerful. But I'm here — in the woods, by the water — because the language of the land is older. And I think you need both. The university and the well."

    ## =====================================================================
    ## CHOICE 7.1 — MENTOR DEEPENS
    ## =====================================================================

    menu:
        "The mentor has shown something they usually hide."

        "Reciprocate — share something personal.":
            $ ch7_mentor = "reciprocate"
            $ add_stat("stat_sd", 1)
            $ add_stat("stat_si", 1)
            if mentor_path == "hawthorne":
                $ add_rel("rel_hawthorne", 2)
            elif mentor_path == "simmons":
                $ add_rel("rel_simmons", 2)
            elif mentor_path == "maya":
                $ add_rel("rel_maya", 2)
            elif mentor_path == "elena":
                $ add_rel("rel_elena", 2)

            if mentor_path == "hawthorne":
                a "I had a panic attack last term. In the library. I couldn't breathe. I thought I was dying."

                "He looks at her. Something shifts — the academic mask slips, just enough."

                hawthorne "And?"

                a "And I went to counselling. And it helped. But what helped more was... people. Friends who noticed. A girl called Liz who made me tea. A boy called Lucas who just... sat with me."

                hawthorne "Tell me something."

                a "What?"

                hawthorne "In that moment — in the library — did your textbook knowledge help?"

                a "No."

                hawthorne "Remember that. Always."

            elif mentor_path == "simmons":
                a "I... I've been anxious since I was twelve. Not the normal kind. The kind where your body decides it's dying and your brain agrees."

                simmons "Tell me about the first time."

                "Amelia tells her. Year 8. A maths test. The room went white and she couldn't breathe and her teacher said 'It's just nerves' and she spent the next four years believing it."

                simmons "It wasn't just nerves."

                a "I know that now."

                simmons "Do you? Really?"

                "A pause."

                a "I'm getting there."

                simmons "Good. 'Getting there' is perfect. 'Got there' is suspicious."

            elif mentor_path == "maya":
                a "I've been having these moments — not psychosis, not that — but moments where things feel... connected. Like the things I'm studying and the things I'm living are the same story from different angles."

                maya "That's not illness. That's perception."

                a "How do you tell the difference?"

                maya "Can you still function? Eat, sleep, talk to your friends, show up for your life?"

                a "Yes."

                maya "Then it's perception. The moment you can't function, it's illness. The border is practical, not philosophical."

            elif mentor_path == "elena":
                a "I found the note in the Paracelsus book. I've been to the ceremony. I sat at Mên-an-Tol. And I don't know what I believe, but I know something is happening to me that textbooks can't explain."

                elena "Lowen."

                a "You keep saying that."

                elena "Because it keeps being true."

        "Acknowledge their openness, but stay guarded.":
            $ ch7_mentor = "acknowledge"
            $ add_stat("stat_mh", 1)
            if mentor_path == "hawthorne":
                $ add_rel("rel_hawthorne", 1)
            elif mentor_path == "simmons":
                $ add_rel("rel_simmons", 1)
            elif mentor_path == "maya":
                $ add_rel("rel_maya", 1)
            elif mentor_path == "elena":
                $ add_rel("rel_elena", 1)

            a "Thank you for telling me that. It means a lot."

            if mentor_path == "hawthorne":
                hawthorne "It's not about meaning a lot. It's about being useful. Learn from my failure."

            elif mentor_path == "simmons":
                simmons "I don't tell many people. But I can see you're someone who needs to know that recovery is real."

            elif mentor_path == "maya":
                maya "Good. Now you know my context. It doesn't change what I've taught you. It changes {i}how{/i} it arrives."

            elif mentor_path == "elena":
                elena "Meur ras. I don't tell many people about her. You seemed ready."

        "Change the subject — it's uncomfortable.":
            $ ch7_mentor = "avoid"

            a "Shall we... shall we look at the essay feedback?"

            if mentor_path == "hawthorne":
                "Hawthorne stares at her for a long moment. Then nods."

                hawthorne "Very well."

            elif mentor_path == "simmons":
                "Simmons' face closes. Just slightly."

                simmons "Sure. Of course."

            elif mentor_path == "maya":
                maya "Okay."

                "The walk continues. But the air between them is different now."

            elif mentor_path == "elena":
                elena "..."

                "She stands. They walk back in silence."

    ## =====================================================================
    ## SCENE 7.2 — SARAH'S DARKNESS VISIBLE
    ## Something alarming. The crisis approaches.
    ## =====================================================================

    scene bg_kitchen_halls
    with dissolve

    # play music "audio/ch7_sarah.ogg" fadein 2.0 volume 0.3

    "February."

    if rel_sarah >= 5:
        "They're in the kitchen. Just the two of them. Late afternoon. Sarah is making tea — she's functioning again, sort of, but the functioning has a careful, deliberate quality, like someone walking on ice."

        "They talk about nothing. The weather. A documentary Raj recommended. The impossible length of Hawthorne's reading lists."

        "Then Sarah says it."

        sarah "I've been thinking about what I'd want people to know. If I wasn't around."

        "The world stops."

        "Amelia's hands go cold."

        sarah "Like... if something happened. I'd want my mum to know I tried. And I'd want Raj to know his cooking genuinely saved me, some nights. And I'd want you to know—"

        "She stops."

        sarah "Doesn't matter."

        "It matters. It matters more than anything anyone has ever said in this kitchen."

    elif rel_sarah >= 3:
        "Liz finds Amelia in the corridor."

        liz "Can I talk to you? About Sarah?"

        "Her face is wrong. The brightness is gone."

        liz "She gave me her favourite book yesterday. The poetry one — Plath. She said 'I want you to have it. You'll look after it better than me.'"

        "Amelia's stomach drops."

        liz "That's... that's a thing, isn't it? Giving away stuff? I read it somewhere — it's a sign."

        a "Did she say anything else?"

        liz "She said she was 'sorting things out.' That's what she said. 'Just sorting things out.'"

    else:
        "An email from a lecturer. Cc'd to the academic advisor."

        "{i}\"I'm writing to flag that Sarah Whitmore has not submitted any work for the past three weeks. Repeated reminders have not received a response. I believe this may indicate a welfare concern.\"{/i}"

        "Amelia reads it. Closes it. Opens it again."

        thought "Three weeks. She hasn't submitted anything in three weeks and I didn't know."

    ## =====================================================================
    ## CHOICE 7.2 — SARAH'S DARKNESS VISIBLE
    ## =====================================================================

    menu:
        "The alarm is sounding. What does Amelia do?"

        "Act immediately — talk to Sarah, then counselling.":
            $ ch7_sarah = "act"
            $ add_stat("stat_mc", 1)
            $ add_stat("stat_mh", 1)
            $ add_rel("rel_sarah", 2)
            $ sarah_alarm_acted = True

            "She doesn't wait. She doesn't think about it. She doesn't second-guess."

            "She goes to Sarah's room. She knocks."

            a "Sarah. Open the door."

            "The door opens."

            "Sarah looks at her. Those eyes — tired, dark-circled, the eyes of someone who has been fighting something invisible for so long she's forgotten she's fighting."

            a "I heard what you said. And I'm scared for you."

            sarah "Amelia—"

            a "I'm not going to pretend I didn't hear it. And I'm not going to pretend it's normal. I love you and I'm scared."

            "Sarah's face crumbles. Not crying — breaking. The mask coming apart."

            sarah "I'm so tired."

            a "I know. And you don't have to do this alone. Tomorrow, we're going to the counselling office together. Not to fix you — just to talk. Okay?"

            "A long silence."

            sarah "...Okay."

            "The next morning, they walk there together. Amelia sits in the waiting room for an hour. When Sarah comes out, her eyes are red."

            sarah "They said I should see my GP."

            a "Okay. I'll come with you."

            sarah "You don't have to—"

            a "I know."

        "Talk to Sarah privately — try to handle it herself.":
            $ ch7_sarah = "private"
            $ add_stat("stat_si", 1)
            $ add_rel("rel_sarah", 1)

            "She goes to Sarah's room."

            a "Can we talk?"

            "They sit on Sarah's bed. Amelia tries to say the right things. She tries to be Simmons — calm, present, patient."

            "But she's eighteen. And the gap between knowing what to say and knowing how to say it is enormous."

            a "I've noticed you've been struggling. And I want you to know it's okay."

            sarah "I know it's okay."

            a "And if you need to talk to someone—"

            sarah "I'm talking to you."

            "That stops Amelia. Because it's true. Sarah is talking to her. And maybe that's enough — or maybe Amelia is in over her head and doesn't know it."

            "They talk for an hour. Sarah opens up, a little. Not all the way. The crack widens but doesn't break."

        "Tell a friend — ask Lucas or Zara for help.":
            $ ch7_sarah = "tell_friend"
            $ add_stat("stat_si", 1)
            $ add_rel("rel_sarah", 1)

            "She finds Lucas."

            a "I'm worried about Sarah."

            "She tells him what she heard. His face goes very still."

            lucas "That's serious, Amelia."

            a "I know. I don't know what to do."

            lucas "We check on her. Together. Now."

            "They go to Sarah's room together. Lucas knocks. His voice is steady — the steadiness of someone who has read enough about this to know exactly how bad it can be."

            "Sarah lets them in. They sit with her. Lucas makes tea. Amelia holds her hand."

            "It helps. A little. But the weight of what's happening is bigger than two students in a residence hall room, and they all know it."

        "Convince yourself you misread the signs.":
            $ ch7_sarah = "deny"
            $ add_rel("rel_sarah", -2)
            $ sarah_alarm_denied = True

            thought "I'm overthinking this. She's just stressed. Everyone says things like that when they're stressed. 'If I wasn't around' — it's a figure of speech. It doesn't mean—"

            "She closes the email. She changes the subject. She looks away."

            "The signs were there. She chose not to see them."

            "This is the choice she will carry for the longest time."

    ## =====================================================================
    ## SCENE 7.3 — AMELIA'S SHADOW
    ## She snaps. The darkness inside her surfaces.
    ## =====================================================================

    scene bg_library_study_area
    with dissolve

    # play music "audio/ch7_shadow.ogg" fadein 2.0 volume 0.4

    "It happens on a Tuesday. The most ordinary day of the week."

    "The library. Study group. Lucas hasn't done the reading. Raj is explaining a concept for the third time. Sophia is pristine and prepared as always. And Amelia is running on four hours of sleep and a headache that's been there since yesterday."

    "Liz asks a question. An innocent question. A good question, actually."

    liz "I don't understand the difference between reliability and validity. Can someone—"

    "And Amelia snaps."

    a "Liz, it's literally in the textbook. Page 147. I don't understand how you can be this far into the term and not—"

    "The room freezes."

    "Liz's face. The hurt on it is immediate and absolute."

    "Amelia hears herself. Hears the echo. Recognises the voice — it's not hers. It's Tasha's. It's Sophia at her worst. It's the voice of someone who uses intelligence to cut."

    thought "What did I just do?"

    "Liz picks up her bag."

    liz "I was just asking."

    "She leaves."

    "The study group dissolves. Raj follows Liz. Lucas looks at Amelia with an expression she can't read — disappointment, or understanding, or both."

    ## =====================================================================
    ## CHOICE 7.3 — AMELIA'S SHADOW
    ## =====================================================================

    menu:
        "The words can't be unsaid. What happens next matters."

        "Apologise quickly and honestly.":
            $ ch7_shadow = "apologise"
            $ add_stat("stat_mh", 1)

            "She follows Liz to the café. Liz is sitting with her coffee, not drinking it."

            a "Liz. I'm so sorry."

            liz "It's fine."

            a "It's not fine. What I said was cruel and unfair and it wasn't about you. I'm tired and stressed and I took it out on you and that's not okay."

            "Liz looks at her."

            liz "I know you're stressed. We're all stressed."

            a "I know. And you didn't deserve that."

            "A pause."

            liz "...Thank you. For saying sorry. Not everyone does."

            "They hug. It doesn't erase it. But it starts to heal it."

        "Reflect on why — journal about it, sit with it.":
            $ ch7_shadow = "reflect"
            $ add_stat("stat_sd", 1)

            "She doesn't follow Liz. Not yet."

            "She goes to her room. Opens her journal. And writes."

            thought "I said the thing Tasha would say. I became the person I despise. Not because I'm a terrible person — but because part of me {i}is{/i} Tasha. Part of me wants to be right more than it wants to be kind. Part of me uses knowledge as a weapon."

            "She writes for an hour. About the Shadow — about Jung's idea that everyone carries a dark twin, and the only way to defuse it is to face it."

            thought "I will apologise to Liz. Tomorrow. Properly. But first I need to understand why it happened. Because if I don't understand, it'll happen again."

            "She texts Liz later that night: {i}i'm so sorry. i was awful. can i buy you a proper apology coffee tomorrow? x{/i}"

            "{i}liz: yes. large. extra shot. and one of those expensive pastries. you owe me x{/i}"

        "Justify it — she asked a stupid question.":
            $ ch7_shadow = "justify"
            $ add_stat("stat_mh", -1)

            thought "It WAS in the textbook. Page 147. How can she still not know this?"

            "She tells herself this. And the thing about telling yourself something often enough is that it starts to feel true."

            "She doesn't apologise. The study group reconvenes three days later. Liz is there. She's polite. She's distant."

            "Something between them has been damaged. Not destroyed — Liz is too kind for that. But damaged."

            "And Amelia, in the quiet moments, hears the echo of her own voice and feels sick."

    ## =====================================================================
    ## SCENE 7.4 — SOPHIA'S FAILURE
    ## The ice queen cracks.
    ## =====================================================================

    scene bg_psych_building_corridor
    with dissolve

    "Results day. The corridor outside the department office."

    "Amelia gets her marks on the portal: 67%%. 64%%. 71%%. She's pleased. Solid. Improving."

    "She looks up from her phone and sees Sophia."

    "Sophia is standing in the corridor with her phone in her hand and an expression Amelia has never seen on her face. It takes a moment to identify it. She's never seen it on {i}Sophia's{/i} face because Sophia doesn't — Sophia {i}can't{/i} —"

    "Sophia has failed."

    "58%%. Research methods. Below the pass threshold for first-class."

    "The colour-coded pens. The annotated reading lists. The twenty-three sources. All of it, and she got 58%%."

    "She's standing in the corridor looking at her phone like it's betrayed her."

    ## =====================================================================
    ## CHOICE 7.4 — SOPHIA'S FAILURE
    ## =====================================================================

    menu:
        "Sophia Kowalski, who has never needed anyone, looks like she needs someone."

        "Reach out: \"Hey, are you okay? I've been there.\"":
            $ ch7_sophia = "reach"
            $ add_stat("stat_si", 1)
            $ add_rel("rel_sophia", 2)

            a "Sophia."

            "She looks up. Her eyes are red. She's furious with herself for the red eyes."

            a "Are you okay?"

            sophia "Obviously not."

            a "I got 58 in my first stats test. I literally cried in the library toilets."

            "Sophia stares at her."

            sophia "You're telling me this to make me feel better."

            a "I'm telling you this because failing one test doesn't mean you're a failure. It means the test was hard. And you're allowed to be disappointed without it defining you."

            "A long silence."

            sophia "...Do you want to get coffee?"

            "They get coffee. Sophia talks — not in her usual controlled, precise way, but messily, vulnerably, like a person."

            sophia "My parents will be devastated."

            a "Will they?"

            sophia "My mum got a first from Warsaw. My dad got a first from Warsaw. They moved to Britain so their children could get firsts from British universities. A 58 isn't part of the plan."

            a "Plans change."

            sophia "Not in my family."

            "For the first time, Amelia sees Sophia not as a rival but as a person. And the person is terrified."

        "Offer study help — keep it academic.":
            $ ch7_sophia = "academic"
            $ add_stat("stat_aa", 1)
            $ add_rel("rel_sophia", 1)

            a "Sophia — do you want to go over the research methods material together? I found some good resources for the areas I struggled with."

            "Sophia looks at her. The offer is professional. Non-threatening."

            sophia "...That might be useful. Yes."

            "They study together. It's efficient and productive. Sophia is still the sharper mind, but Amelia has a knack for explaining things simply, and Sophia, for once, is in a position to need that."

            sophia "Thank you. I don't... thank you."

        "Privately enjoy the schadenfreude.":
            $ ch7_sophia = "schadenfreude"

            thought "58%%. Sophia Kowalski, the machine, the colour-coded perfectionist, got 58%%."

            "Amelia walks past. She doesn't stop."

            thought "I should feel guilty. I don't. I feel... relieved. She's human. She's not a robot. She bleeds."

            "It's an ugly thought. She knows it's ugly. She has it anyway."

    ## =====================================================================
    ## SCENE 7.5 — RESEARCH ETHICS DILEMMA
    ## The right thing to do isn't clear.
    ## =====================================================================

    scene bg_library_study_area
    with dissolve

    # play music "audio/ch7_ethics.ogg" fadein 2.0 volume 0.4

    "A group project. Developmental psych. The deadline is Thursday."

    "Amelia discovers that a teammate — not someone she's close to — has copied a section of their contribution from an online source. Not the whole thing. About a paragraph. Changed some words, left others."

    "Plagiarism. Borderline, but plagiarism."

    "If she flags it, the whole group loses marks while it's investigated. If she says nothing, they submit with a stolen paragraph. If she rewrites the section herself, she's covering for someone else's dishonesty."

    if mentor_path == "hawthorne":
        thought "What would Hawthorne say? He'd say 'integrity is not negotiable.' But he's never had fourteen percent of his grade on the line."

    elif mentor_path == "simmons":
        thought "What would Simmons say? She'd say 'think about the person.' But the person is putting the whole group at risk."

    elif mentor_path == "maya":
        thought "What would Maya say? She'd say 'what does your gut tell you?' My gut says this is a mess."

    elif mentor_path == "elena":
        thought "What would Elena say? She'd say something cryptic about the difference between the letter and the spirit of the law."

    ## =====================================================================
    ## CHOICE 7.5 — RESEARCH ETHICS DILEMMA
    ## =====================================================================

    menu:
        "The deadline is Thursday. The paragraph is stolen. The choice is hers."

        "Choose integrity — flag it, even at personal cost.":
            $ ch7_ethics = "integrity"
            $ add_stat("stat_mc", 1)
            if mentor_path == "hawthorne":
                $ add_rel("rel_hawthorne", 1)
            elif mentor_path == "simmons":
                $ add_rel("rel_simmons", 1)
            elif mentor_path == "maya":
                $ add_rel("rel_maya", 1)
            elif mentor_path == "elena":
                $ add_rel("rel_elena", 1)

            "She flags it. She emails the module leader. She tells her group."

            "The teammate is furious. The group is stressed. The investigation takes three weeks."

            "In the end: the teammate is given a formal warning. The rest of the group is cleared. The marks are adjusted, and Amelia's section receives commendation."

            if mentor_path == "hawthorne":
                "Hawthorne's feedback: 'This was the right decision. It was also the expensive one. Get used to that.'"

        "Choose pragmatism — rewrite the section herself.":
            $ ch7_ethics = "pragmatism"
            $ add_stat("stat_aa", 1)

            "She rewrites the paragraph. It takes forty minutes. She doesn't tell anyone."

            "They submit. They get 72%%. The teammate thanks her without knowing what she did."

            thought "I covered for someone else's dishonesty. And I got a good mark for it. And I feel... wrong. Not guilty, exactly. Just wrong."

        "Avoid the decision entirely. Submit as is.":
            $ ch7_ethics = "avoid"

            "She does nothing. She submits. She hopes."

            "They get 68%%. The plagiarism isn't caught."

            thought "I got away with it. The stolen paragraph is part of my grade now. And every time I think about it, I feel the floor shift slightly, like standing on thin ice."

    ## =====================================================================
    ## SCENE 7.6 — OCCULT THREAD (Conditional)
    ## Only triggers if OK ≥ 5
    ## =====================================================================

    if stat_ok >= 5:

        scene bg_amelia_room_plymouth_night
        with dissolve

        # play music "audio/ch7_occult.ogg" fadein 2.0 volume 0.3

        "Late one night. Reading."

        "An old text — found online, a digitised scan of a book published in 1913 by someone called Arthur Edward Waite. {i}The Secret Tradition in Alchemy.{/i}"

        "She's been following a thread. From the Paracelsus book to the ley line book to this — deeper and deeper into the history of alchemy as a psychological practice."

        "And then she finds it."

        "A passage about the three stages of the Great Work: Nigredo, Albedo, Rubedo. The blackening, the whitening, the reddening. Death, purification, and rebirth."

        "She reads the descriptions."

        "Nigredo: {i}'The dark night of the soul. The dissolution of the ego. The descent into chaos.'\"}\""

        "Albedo: {i}'The purification. The separation of elements. A guide appears. Clarity begins.'\"}\""

        "Rubedo: {i}'The reddening. Transformation complete. The philosopher's stone is born.'\"}\""

        "Her skin prickles."

        thought "September to November. The dark. The panic. The confusion. That was the Nigredo."

        thought "November to now. The mentor. Cornwall. The clarity. That's the Albedo."

        thought "And Rubedo... Rubedo hasn't happened yet."

        thought "But it's coming."

        ## =====================================================================
        ## CHOICE 7.6 — OCCULT THREAD: THE ALCHEMICAL MAP
        ## =====================================================================

        menu:
            "The pattern is visible. A map of her own year in a book published over a century ago."

            "Push deeper — research the full alchemical process.":
                $ ch7_occult = "deep"
                $ add_stat("stat_ok", 1)
                $ add_stat("stat_sd", 1)

                "She reads all night."

                "Not just Waite — Jung's {i}Psychology and Alchemy{/i}. Hillman. Von Franz. The serious scholars who took alchemy seriously as a map of the psyche."

                "By dawn, she has a notebook full of parallels. Her year — the leaving, the crisis, the mentor, the deepening — mapped onto a thousand-year-old framework."

                thought "Either the alchemists knew something about the human soul that we've forgotten. Or I'm projecting so hard I could open a cinema."

                if mentor_path == "elena":
                    "She texts Elena: {i}i found the three works. nigredo. albedo. rubedo. they're my year.{/i}"

                    "{i}elena: now you're seeing it. an gwella. the sight.{/i}"

            "Note the parallel, but stay grounded.":
                $ ch7_occult = "grounded"
                $ add_stat("stat_sd", 1)

                "She closes the book. Takes a breath."

                thought "It's interesting. It's a compelling framework. But I'm a psychology student, not a mystic. The pattern is useful because it gives me language, not because it's literally true."

                "She writes a journal entry about it. Then she goes to sleep."

            "Close the book — this is getting too strange.":
                $ ch7_occult = "close"

                "She closes the book."

                thought "No. This is — this is confirmation bias. I'm seeing patterns because I'm looking for patterns. The alchemists were wrong about chemistry and they're wrong about this."

                "She deletes the bookmark."
    else:
        $ ch7_occult = "none"

    ## =====================================================================
    ## SCENE 7.7 — THE GATHERING STORM
    ## End of chapter. Something is coming.
    ## =====================================================================

    scene bg_plymouth_hoe_day
    with dissolve

    # play music "audio/ch7_storm.ogg" fadein 2.0 volume 0.3

    "Late February."

    "The days are getting longer. Barely — two minutes a day, three — but she can feel it. The light is different. Not warmer yet, but wider."

    "She stands on the Hoe. The sea is grey-green, churning. A storm is coming — not metaphorical. Actual weather. The forecast says seventy-mile-an-hour winds by Friday."

    "But she doesn't go inside."

    "She stands there and watches the clouds build on the horizon. Black and purple and gold where the sun catches their edges."

    thought "Something is coming. I can feel it. Not the storm — something else. Something in the pattern of things. The approach to whatever I've been preparing for all year."

    if sarah_alarm_acted:
        thought "Sarah. The counselling appointment is next week. She promised to go. She promised."
    elif ch7_sarah == "private" or ch7_sarah == "tell_friend":
        thought "Sarah. I need to keep watching. I need to stay close."
    else:
        thought "Sarah..."

    "The wind picks up. The first drops of rain."

    "She stays a moment longer. Then turns, pulls up her hood, and walks back towards campus."

    "Ready or not."

    # --- SONG SLIDESHOW: "Mirror of the Mind" — The gathering storm ---
    call slideshow_ch7_mirror_of_the_mind

    ## -----------------------------------------------------------------------
    ## END OF CHAPTER
    ## -----------------------------------------------------------------------

    scene black
    with fade

    centered "{size=+6}End of Chapter Seven{/size}"
    pause 2.0

    return
