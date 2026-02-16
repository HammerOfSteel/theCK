###############################################################################
##
##  CHAPTER 4: MEETING THE MENTOR
##
##  Hero's Journey: The hero encounters a guide.
##  Alchemical Stage: Solutio → Albedo begins — purification; a guide in darkness.
##  Month: November. Location: Plymouth + first Cornwall trip.
##  Palette: Grey lightening. First white. Mist and clarity alternating.
##  Music: Austere. Wind. Strings. The sound of a door opening.
##
##  Four variant paths: Hawthorne / Simmons / Maya / Elena
##  Scenes: 5 core (mentor-flavoured) | Choices: 4-5 | Max: ~7 pts
##
###############################################################################

label chapter_4:

    stop music fadeout 1.0
    scene black
    with fade

    ## -----------------------------------------------------------------------
    ## TITLE CARD
    ## -----------------------------------------------------------------------

    centered "{size=+20}Chapter Four{/size}\n\n{size=+6}Meeting the Mentor{/size}"
    pause 3.0

    ## =====================================================================
    ## SCENE 4.1 — THE ASSIGNMENT / FIRST MEETING
    ## How Amelia meets her mentor depends on the path.
    ## =====================================================================

    ## -----------------------------------------------------------------------
    ## HAWTHORNE PATH
    ## -----------------------------------------------------------------------

    if mentor_path == "hawthorne":

        scene bg_hawthorne_office
        with dissolve

        # play music "audio/ch4_hawthorne.ogg" fadein 2.0 volume 0.5

        "An email. Wednesday morning. From the department:"

        "{i}\"Dear Ms James, you have been assigned Prof. Arthur Hawthorne as your academic advisor for the remainder of First Year. Please schedule an introductory meeting at your earliest convenience via the portal. — Psychology Department Administration\"{/i}"

        thought "Hawthorne. Of course it's Hawthorne."

        "His office door is always slightly ajar. Not inviting — ajar. As though the concept of a closed door is a concession to institutional convention that he tolerates with minimal enthusiasm."

        "Inside: books. Floor to ceiling. Organised by era, not by author, which Amelia finds either brilliant or maddening. A green banker's lamp. A print of Caravaggio's {i}The Incredulity of Saint Thomas{/i} on the wall — the apostle pushing his finger into Christ's wound, lit from above like a laboratory."

        "Earl Grey in a bone china cup. Always."

        hawthorne "Miss James. Sit down."

        "He's reading her essay. The one he already destroyed via portal feedback. He's reading it again."

        hawthorne "I've been thinking about your essay."

        a "I've been trying not to."

        "The ghost of a smile."

        hawthorne "You summarised Eysenck's position competently. That's not a compliment — competence is the floor, not the ceiling. What I want to know is: do you think he was right?"

        a "About... personality traits being biologically determined?"

        hawthorne "Yes."

        a "I... I think there's good evidence for it."

        hawthorne "Now argue the opposite."

        a "What?"

        hawthorne "Tell me he was wrong. Convince me. You have three minutes."

        "He leans back. Tents his fingers. Waits."

        "The silence is excruciating."

    ## -----------------------------------------------------------------------
    ## SIMMONS PATH
    ## -----------------------------------------------------------------------

    elif mentor_path == "simmons":

        scene bg_simmons_office
        with dissolve

        # play music "audio/ch4_simmons.ogg" fadein 2.0 volume 0.5

        "An email. Wednesday morning:"

        "{i}\"Hi Amelia! You've been paired with me as your academic advisor — I'm Dr. Nadia Simmons, student wellbeing and developmental psych. Pop by my office when you're free, no need to book. Kettle's always on. — Nadia\"{/i}"

        thought "A smiley face in a professional email. That's either a good sign or a warning."

        "Dr. Simmons' office is on the second floor. The door is covered in postcards — sunsets, cat pictures, a card that says {i}\"Be kind to yourself (this is a threat)\"{/i}."

        "Inside: plants. So many plants. On the shelves, on the windowsill, hanging from the ceiling in macramé holders. A small fountain on the desk that makes a trickle sound. Motivational posters that should be corny but somehow aren't."

        "And the chairs. The chairs are, as promised, extremely comfortable."

        simmons "Right, come in, sit down. Tea? I've got ginger biscuits and I've got those ones from Aldi that taste like sadness. Your choice."

        a "Ginger, please."

        simmons "Smart girl. Right."

        "She makes tea with the ease of someone who's made ten thousand cups of tea in this room, each one an act of care."

        simmons "So. How are you, Amelia?"

        "She smiles."

        simmons "And I mean actually — not the version you tell your parents."

    ## -----------------------------------------------------------------------
    ## MAYA PATH
    ## -----------------------------------------------------------------------

    elif mentor_path == "maya":

        scene bg_plymouth_hoe_dawn
        with dissolve

        # play music "audio/ch4_maya.ogg" fadein 2.0 volume 0.4

        "Maya doesn't send an email. Maya sends a text at 5:47am:"

        "{i}maya: hoe. now. sunrise. bring a coat. trust me{/i}"

        thought "It is — I cannot stress this enough — five forty-seven in the morning."

        "But she goes."

        "The Hoe at dawn. She's only ever seen it in afternoon grey. But now: the sky is doing something extraordinary. Pink and gold and the palest blue, spreading from the east like a slow fire."

        "Maya is already there. Cross-legged on the grass, face tilted up, perfectly still. She looks like a painting — the kind you'd see in a gallery titled something like {i}Woman Receiving Light{/i}."

        maya "Sit."

        "Amelia sits."

        "They watch the sun come up."

        "It takes about fifteen minutes. In those fifteen minutes, Amelia doesn't think about essays or Tasha or the panic attack or the statistics module that's slowly killing her. She just watches."

        "When the sun clears the horizon, Maya speaks."

        maya "This is where it starts."

        a "...Psychology?"

        maya "Attention. Attention is the root of everything. Attention to yourself, to others, to the world. Without attention, psychology is just a collection of facts. With it — it's a practice."

        "She looks at Amelia."

        maya "I've been watching you. You pay attention. Not everyone does."

    ## -----------------------------------------------------------------------
    ## ELENA PATH
    ## -----------------------------------------------------------------------

    elif mentor_path == "elena":

        scene bg_barbican_bookshop
        with dissolve

        # play music "audio/ch4_elena.ogg" fadein 2.0 volume 0.4

        "It doesn't happen through the department."

        "It happens in the second-hand bookshop on the Barbican. A Saturday. Amelia is browsing the psychology section — looking for nothing in particular, which is when you always find something."

        "A voice behind her. Low, unhurried. A Cornish accent — not the tourist kind."

        elena "Have you found the note yet?"

        "Amelia turns. A woman in her mid-forties. Long dark hair with a single streak of silver. Green eyes. Hands that look like they've spent a lifetime outside — weathered, capable. She wears a waxed jacket and boots and a silver ring with a bird on it."

        "She's looking at Amelia like she's been expecting her."

        a "Sorry — do I know you?"

        elena "Elena Trevorran. I'm in the psychology programme."

        a "I haven't seen you in any—"

        elena "I'm part-time. I attend when I attend."

        "She glances at the bag over Amelia's shoulder. At the shape of the Paracelsus book inside it."

        elena "The note. In the front cover. Have you really read it?"

        "A cold feeling. Not unpleasant. Like stepping into a river."

        a "How did you know about the note?"

        elena "I wrote it."

        "Silence. The bookshop ambient noise — the creaking floor, a radio playing somewhere — feels very far away."

        elena "{i}Seek the pellar where the land meets the sea.{/i} You looked it up, didn't you?"

        a "I... yes. A pellar is a Cornish—"

        elena "I know what it is."

        "She smiles. Just barely."

        elena "I've been watching you in the corridor. You walk like someone who's looking for something she doesn't know the name of yet."

        a "That's... a strange thing to say."

        elena "I'm a strange person. Come to Cornwall with me next Saturday. I want to show you something."

        a "I don't even—"

        elena "Just come. Dress warm."

    ## =====================================================================
    ## CHOICE 4.1 — FIRST MEETING RESPONSE (All paths)
    ## =====================================================================

    menu:
        "The mentor has spoken. Something has opened."

        "Engage fully — eager, asking questions, leaning in.":
            $ ch4_meeting_response = "eager"
            $ add_stat("stat_sd", 1)
            $ add_rel("rel_" + mentor_path if mentor_path != "elena" else "rel_elena", 1)

            if mentor_path == "hawthorne":
                "She takes a breath. And argues."

                a "Okay. Eysenck was wrong because — because biological determinism assumes the gene is the whole story, but it's not. Environment shapes expression. Trauma rewires the brain. You can have a genetic predisposition and never trigger it if the conditions aren't—"

                hawthorne "Better. Not good. But better."

                "His eyes are sharp. But there's warmth underneath — buried deep, like coal."

                hawthorne "The ability to argue against a position you hold is the beginning of intellectual honesty. Most people never get there. You've taken one step. We have a long way to go."

            elif mentor_path == "simmons":
                a "Honestly? It's been harder than I expected."

                "Simmons nods. No surprise. No judgement."

                a "I had a panic attack in the library. And I don't know if I'm smart enough. And there's this girl — Sophia — who's better than me at everything and I know I shouldn't compare but—"

                simmons "Stop."

                "She says it gently."

                simmons "You just told me more truth in thirty seconds than most students manage in a term. That takes courage. Do you know that?"

            elif mentor_path == "maya":
                a "Why did you bring me here at sunrise? Specifically?"

                maya "Because you need to learn to be present before you can learn anything else. Psychology without presence is just pattern-matching. Which is useful. But it's not wisdom."

                a "And wisdom is what we're after?"

                maya "Wisdom is what we're always after. We just call it different things depending on the century."

            elif mentor_path == "elena":
                a "What do you want to show me?"

                elena "The land. Specifically, the parts of it that remember things the textbooks forgot."

                a "That sounds like you're trying to recruit me into something."

                elena "I am." 
                
                "Beat."
                
                elena "But not what you're thinking."

        "Stay guarded — test the mentor, hold back.":
            $ ch4_meeting_response = "guarded"
            $ add_stat("stat_mh", 1)

            if mentor_path == "hawthorne":
                a "What if I can't? Argue the opposite?"

                hawthorne "Then you don't understand the position you hold. Which means you're parroting, not thinking. And parroting will get you a 2:2 and a career in marketing."

                "Harsh. But honest."

                a "Is that your teaching style? Terrify people into thinking?"

                hawthorne "It's worked for thirty years."

            elif mentor_path == "simmons":
                a "I'm fine. Really. I'm managing."

                simmons "Okay."

                "She doesn't push. She just sits there, holding her tea, smiling slightly."

                "The silence stretches."

                simmons "...The offer's open. Not just today."

            elif mentor_path == "maya":
                a "I'm not really a sunrise person."

                maya "Nobody is, until they are."

                "She doesn't elaborate. Just sits there, infuriatingly calm."

                a "How do you know I'm worth your time?"

                maya "I don't. That's the fun part."

            elif mentor_path == "elena":
                a "I appreciate the offer. But I don't go to Cornwall with strangers."

                elena "Sensible."

                "She reaches into her jacket and produces a university ID card. Elena Trevorran. Psychology. Part-time."

                elena "Less of a stranger now?"

                a "Marginally."

                elena "That'll do."

    ## =====================================================================
    ## SCENE 4.2 — THE CORNWALL TRIP
    ## Each path visits a different location. Different lessons.
    ## =====================================================================

    ## -----------------------------------------------------------------------
    ## HAWTHORNE'S CORNWALL — Bodmin Moor / Tin Mining Heritage
    ## -----------------------------------------------------------------------

    if mentor_path == "hawthorne":
        scene bg_bodmin_moor
        with dissolve

        # play music "audio/ch4_cornwall_hawk.ogg" fadein 3.0 volume 0.5

        "Saturday. Hawthorne drives. He has a Volvo from the 1990s that smells of old leather and Earl Grey. He does not play music. He drives in silence. Amelia stares out the window."

        "Cornwall unfolds as they cross the Tamar Bridge — the world changes, subtly but unmistakably. The hedgerows are higher. The sky is wider. The field patterns are different, older."

        "Bodmin Moor. The road narrows, then vanishes. They walk."

        "The landscape is vast and stripped. No trees. Granite tors rising from the earth like vertebrae. Wild ponies in the distance. The wind is a constant, physical thing."

        hawthorne "Do you know what happened here?"

        a "It's... beautiful?"

        hawthorne "It's a graveyard."

        "He stops at the ruins of an engine house. Roofless stone walls against the sky. A chimney stack, alone."

        hawthorne "Tin mining. Three thousand years of it. Bronze Age to the twentieth century. The wealth of empires dug out of this soil by men who died at forty with lungs full of dust."

        "He looks at the ruins the way he looks at essays — seeing what's there and what isn't."

        hawthorne "Psychology without history is decoration, Miss James. If you want to understand why people suffer, you must first understand who benefits from their suffering."

    ## -----------------------------------------------------------------------
    ## SIMMONS' CORNWALL — Eden Project + Lost Gardens of Heligan
    ## -----------------------------------------------------------------------

    elif mentor_path == "simmons":
        scene bg_eden_project
        with dissolve

        # play music "audio/ch4_cornwall_sim.ogg" fadein 3.0 volume 0.5

        "Saturday. Simmons drives a small Fiat covered in bumper stickers: {i}BE KIND{/i}, {i}PLANTS BEFORE PEOPLE{/i}, {i}MY OTHER CAR IS A GREENHOUSE{/i}."

        "She plays Radio 4 and hums along to the shipping forecast."

        "The Eden Project. Two enormous biome domes sitting in a former clay pit like alien greenhouses. From the car park, they look like bubbles frozen in the landscape."

        "Inside: the tropics. Humid, warm, green beyond what the English brain can process in November."

        simmons "Breathe it in."

        "They walk through the rainforest biome. Giant leaves. Dripping water. Birdsong recorded or real — Amelia can't tell."

        simmons "You know what this place used to be? A clay pit. A scar in the ground. Mined for decades, stripped bare, left for dead."

        "She stops by a waterfall."

        simmons "And now look at it."

        a "It's incredible."

        simmons "Restoration isn't going back to what was. It's growing something new from what survived. Remember that."

    ## -----------------------------------------------------------------------
    ## MAYA'S CORNWALL — Tintagel + Mên-an-Tol
    ## -----------------------------------------------------------------------

    elif mentor_path == "maya":
        scene bg_tintagel
        with dissolve

        # play music "audio/ch4_cornwall_maya.ogg" fadein 3.0 volume 0.5

        "Saturday. Maya borrows a friend's car and drives like she lives — enthusiastically, a little too fast, narrating the journey as though it were a podcast."

        maya "Okay, so, Tintagel. Supposedly where Arthur was conceived. Except Arthur probably wasn't a single person — he was a pattern. A template. The Once and Future King isn't a prophecy, it's a psychological archetype."

        a "You're making this up."

        maya "I am NOT making this up. Joseph Campbell wrote about this. The hero with a thousand faces — Arthur is one of them, Amelia is another—"

        a "I'm not a mythic hero."

        maya "That's exactly what the mythic hero says in Act One."

        "Tintagel is dramatic. Wind-blasted cliffs, spray from the sea below, the ruins of a castle that's mostly gone but the setting remains — extraordinary, vast, the kind of place that makes your chest hurt."

        "They cross the footbridge over the chasm. Below: the cave. Merlin's Cave, supposedly. Dark, wet, full of the sound of the sea trapped in stone."

        maya "You're standing where people have stood for five thousand years asking the same questions you're asking."

        a "What questions?"

        maya "Who am I? Why am I here? What comes next?"

    ## -----------------------------------------------------------------------
    ## ELENA'S CORNWALL — Madron Holy Well + Carn Euny Fogou
    ## -----------------------------------------------------------------------

    elif mentor_path == "elena":
        scene bg_madron_well
        with dissolve

        # play music "audio/ch4_cornwall_elena.ogg" fadein 3.0 volume 0.4

        "Elena picks her up at seven. She drives a Land Rover that's older than Amelia. She doesn't play music. She drives in silence, but it's a different silence from Hawthorne's — his is intellectual. Hers is... the silence of someone listening to something Amelia can't hear."

        "Past Truro. Past Penzance. Down a narrow lane. She parks."

        elena "Walk."

        "They walk through woods. Muddy, narrow, the kind of path that exists because feet have walked here for centuries, not because anyone planned it."

        "They arrive at the Madron Holy Well."

        "Amelia's breath catches."

        "A ruined stone baptistry, roofless, in a clearing in the woods. A crude stone altar. Water seeping from the ground, dark and cold. And on every branch of every tree surrounding it — hundreds of rags. Clooties. Tied there by visitors seeking healing. Faded by sun and rain. Blues and reds and whites turned to ghost-colours."

        "The silence is total. Not empty — full. Full of something Amelia can't name."

        elena "People have been coming here for a thousand years. They tie the cloth, they make the wish, they leave the pain with the water."

        a "Does it work?"

        elena "Define {i}work.{/i}"

        "She kneels by the water. Touches it."

        elena "The water doesn't cure you. But the act of coming here — of walking through the woods, of tying the cloth, of giving your pain a shape and leaving it — that cures you. Or begins to."

        "She looks up."

        elena "Same principle as therapy. Different technology."

    # --- SONG SLIDESHOW: "Hawthorne" — Cornwall trip, ancient landscape ---
    call slideshow_ch4_hawthorne

    ## =====================================================================
    ## CHOICE 4.2 — RESPONSE TO CORNWALL LANDSCAPE (All paths)
    ## =====================================================================

    menu:
        "The land speaks. Something in Amelia responds."

        "Deeply moved — present, open, feeling it.":
            $ ch4_cornwall_response = "moved"
            $ add_stat("stat_sd", 1)
            if mentor_path == "elena":
                $ add_rel("rel_elena", 1)
            elif mentor_path == "maya":
                $ add_rel("rel_maya", 1)
            elif mentor_path == "simmons":
                $ add_rel("rel_simmons", 1)
            else:
                $ add_rel("rel_hawthorne", 1)

            if mentor_path == "hawthorne":
                "The wind pulls at her coat. The granite is grey and ancient. The silence of the moor has a weight to it — the weight of centuries."

                thought "This is real. This isn't a textbook. These aren't statistics. People lived here. Worked here. Died here. And I'm standing where they stood."

                "She doesn't say anything. Sometimes the best response to a place is to let it in."

                hawthorne "You felt that."

                a "Yeah."

                hawthorne "Good. Hold onto it. That's where the real work begins — not in the head. In the chest."

            elif mentor_path == "simmons":
                "The warmth of the biome. The impossible green of things growing where nothing should grow."

                thought "She's right. This isn't restoration. This is... creation. Something new from something ruined."

                "Amelia reaches out and touches a leaf — huge, waxy, tropical. It's real. In a clay pit in Cornwall, in November, it's real."

                a "This is extraordinary."

                simmons "Isn't it? And it didn't happen by accident. Someone had to decide it was possible."

            elif mentor_path == "maya":
                "The wind on the cliff. The sea below. The ruins against the sky."

                thought "Maya's right. This is old. This is so much older than anything I know. And the questions people asked here — they're the questions I'm asking now."

                "She stands very still. The wind does something to her — strips away the noise, the anxiety, the comparison with Sophia and the emails and the reading list."

                "For a moment, she is just a person standing on ancient ground. And that's enough."

            elif mentor_path == "elena":
                "The clooties flutter in the breeze. The water runs. The woods are old and quiet and full of something she can't define."

                thought "I've never been anywhere that felt like this. Not in a building. Not in a book. This feels... alive. Not dead, not historical — {i}alive{/i}."

                "Without thinking, she kneels beside Elena. The water is cold on her fingers."

                elena "Teg."

                a "What?"

                elena "Beautiful. The Cornish word. {i}Teg.{/i}"

        "Intellectually curious — asking questions, wanting to understand.":
            $ ch4_cornwall_response = "intellectual"
            $ add_stat("stat_aa", 1)

            if mentor_path == "hawthorne":
                a "Three thousand years? How do we know?"

                hawthorne "Carbon dating. Archaeological surveys. The written record begins with the Romans, but the land itself is the primary source. You can read the earth like a text if you know how."

                "They talk for an hour. About mining, about exploitation, about the psychology of power."

            elif mentor_path == "simmons":
                a "How long did the restoration take?"

                simmons "The clay pit was abandoned in the '90s. The Eden Project opened in 2001. About ten years of hard, unglamorous work."

                a "Ten years."

                simmons "Healing isn't fast, Amelia. Anyone who tells you otherwise is selling something."

            elif mentor_path == "maya":
                a "When you say Arthur is a pattern — what kind of pattern?"

                maya "The hero who withdraws to a sacred place, undergoes a trial, and returns transformed. It's in every culture. Campbell mapped it. Jung called it individuation. The Arthurian legends call it the Grail Quest."

                a "And you think university is... a Grail Quest?"

                maya "I think everything is, for the person living it."

            elif mentor_path == "elena":
                a "How old is this place?"

                elena "The well has been here since at least the medieval period. But water was sacred in Cornwall long before that. The Brythonic Celts. The people before them."

                a "And the clooties?"

                elena "A practice so old nobody remembers when it started. Which is usually a sign it works."

        "Uncomfortable — wanting to go back to campus.":
            $ ch4_cornwall_response = "uncomfortable"

            if mentor_path == "hawthorne":
                thought "It's cold. My feet are wet. I don't know what I'm supposed to be feeling."

                "She looks at the ruins and feels... nothing. Or something, but the something is covered by discomfort, and she can't peel it back."

                hawthorne "Not everyone takes to the moor immediately. That's fine. It'll wait."

            elif mentor_path == "simmons":
                thought "It's beautiful, I suppose. But I've got an essay due and I should really—"

                simmons "You're somewhere else, aren't you?"

                a "Sorry. I just—"

                simmons "It's okay. Being present is a skill. Skills take practice."

            elif mentor_path == "maya":
                thought "I feel stupid standing on a cliff pretending to have revelations. Maybe this works for Maya. I'm from Bromley."

                maya "You're resisting."

                a "I'm cold."

                maya "Same thing, sometimes."

            elif mentor_path == "elena":
                thought "This is — objectively — a wet wood with rags in the trees and I'm kneeling in mud."

                elena "You're not ready yet. That's fine."

                a "Ready for what?"

                elena "To hear what the water says."

                thought "I genuinely cannot tell if she's profound or mental."

    ## =====================================================================
    ## SCENE 4.3 — THE MENTOR'S TEST
    ## Each mentor tests Amelia differently.
    ## =====================================================================

    ## -----------------------------------------------------------------------
    ## HAWTHORNE'S TEST — Sarah's anonymised file
    ## -----------------------------------------------------------------------

    if mentor_path == "hawthorne":

        scene bg_hawthorne_office
        with dissolve

        "Two weeks later. Hawthorne's office. He's standing at the window, watching the car park."

        hawthorne "I've been given a student case file to review. Part of the wellbeing programme. Anonymised, of course."

        "He places a folder on the desk."

        hawthorne "I'd like your analysis. Clinical only — behavioural patterns, risk factors, recommended interventions. Treat it as a case study."

        "Amelia opens the folder. Reads."

        "Female. 18. Rural background. Recent relocation. History of anxiety. Reports feeling 'disconnected' from her surroundings. Sleep disruption. Reduced appetite. Social withdrawal increasing. Previous contact with counselling services in secondary school."

        "A tattoo of a wren on her inner wrist."

        "Amelia's heart stops."

        thought "This is Sarah."

        "She looks at Hawthorne. He's watching her. He knows she knows."

        menu:
            "The file is in her hands. The answer matters."

            "Analyse clinically. Don't reveal she knows.":
                $ ch4_test = "clinical"
                $ add_stat("stat_aa", 1)
                $ add_stat("stat_mc", 1)

                a "The profile is consistent with major depressive disorder, moderate severity. The social withdrawal is concerning — it suggests the condition is worsening, not stabilising. I'd recommend increased check-ins, possibly a referral back to counselling."

                "She says it calmly. Professionally."

                "Hawthorne watches her face."

                hawthorne "And?"

                a "And the fact that previous contact with counselling was in secondary school suggests this isn't a first episode. Which makes it more serious."

                hawthorne "Good. Anything else?"

                a "No."

                "She closes the file. Hands it back."

                hawthorne "Professional integrity is not always the same as personal instinct, Miss James. Sometimes the kindest thing you can do for someone is to treat their pain as a problem to be solved with the right tools, not as a story to be lived with the wrong ones."

            "Tell him she recognises the person. Be honest.":
                $ ch4_test = "honest"
                $ add_stat("stat_mh", 1)
                $ add_rel("rel_sarah", 1)

                a "I know who this is."

                "Hawthorne doesn't flinch."

                hawthorne "Do you."

                a "The wren tattoo. The rural background. It's... someone I know."

                "She puts the file down."

                a "I'm not sure it's appropriate for me to analyse her. Because I care about her. And caring makes me biased."

                "A long silence."

                hawthorne "That. Was the right answer."

                "He takes the file back."

                hawthorne "I wanted to know if you could see the person behind the data. Any student can analyse a profile. The question is whether you have the courage to acknowledge when analysis isn't enough."

            "Take the information and check on Sarah personally.":
                $ ch4_test = "act"
                $ add_stat("stat_si", 1)
                $ add_rel("rel_sarah", 1)

                "She reads the file. Memorises the risk factors. Closes it."

                a "Thank you for showing me this."

                hawthorne "And?"

                a "And I think I should go. If that's okay."

                "She's already standing. Already thinking about Room 22, second floor, the door that's always shut."

                hawthorne "Miss James."

                "She turns."

                hawthorne "What you're about to do is human, not clinical. Remember the difference."

    ## -----------------------------------------------------------------------
    ## SIMMONS' TEST — Student crying in the corridor
    ## -----------------------------------------------------------------------

    elif mentor_path == "simmons":

        scene bg_psych_building_corridor
        with dissolve

        "They're walking through the psych building after a session. Simmons is telling a story about a former student who's now working for the NHS — 'Lovely girl, absolutely useless at statistics, now running a whole department, goes to show —'"

        "She stops."

        "There's a student sitting on the floor outside a seminar room. Knees drawn up. Head down. Crying. The quiet kind — the kind that's been going on for a while."

        "Simmons doesn't move. She stands very still and watches Amelia."

        menu:
            "A person is in pain. Right there, in the corridor."

            "Go to them immediately.":
                $ ch4_test = "immediate"
                $ add_stat("stat_mh", 1)
                $ add_stat("stat_si", 1)

                "Amelia doesn't think. She goes."

                "She crouches beside the student. Doesn't touch them. Just crouches."

                a "Hey. Are you okay?"

                "The student looks up. Red eyes, shaking hands."

                "Amelia stays. She doesn't try to fix it. She just stays."

                "After a few minutes, Simmons appears with water and tissues and the quiet professional efficiency of someone who's done this a thousand times."

                "Later, walking back:"

                simmons "You went first. Without thinking."

                a "Was that the right thing to do?"

                simmons "It was {i}a{/i} right thing. Compassion doesn't need a plan. It needs a body that moves towards pain instead of away from it."

            "Look for a staff member first.":
                $ ch4_test = "responsible"
                $ add_stat("stat_mc", 1)

                a "I'll find someone — a lecturer, or the department—"

                simmons "Wait."

                "She puts a hand on Amelia's arm."

                simmons "Why not go yourself?"

                a "Because I'm not... I'm not qualified. I don't know what to say."

                simmons "Neither did I, the first time. The qualification isn't the degree. It's the willingness to be present with someone else's pain."

                "She pauses."

                simmons "But the instinct to get help? That's good too. Don't dismiss it. In a real crisis, getting professional help might be the most important thing you can do."

            "Freeze. Not sure what to do.":
                $ ch4_test = "freeze"

                "Amelia doesn't move."

                "She sees the student. She wants to help. She doesn't know how."

                "Her feet don't go anywhere."

                "Simmons, after a long moment, goes to the student herself. Water, tissues, the practised gentleness."

                "Afterwards:"

                simmons "You froze."

                a "I'm sorry."

                simmons "Don't be sorry. Freezing is honest. It means you cared enough to be overwhelmed."

                "She squeezes Amelia's hand."

                simmons "Next time, remember this: you don't have to be perfect. You just have to be there."

    ## -----------------------------------------------------------------------
    ## MAYA'S TEST — An hour of silence at Mên-an-Tol
    ## -----------------------------------------------------------------------

    elif mentor_path == "maya":

        scene bg_men_an_tol
        with dissolve

        "The second Cornwall trip. Just Amelia and Maya. The road to Mên-an-Tol."

        "Three stones on open moorland near Madron — two uprights and a round stone with a hole you can crawl through. Small, unassuming, impossibly ancient. No fences. No gift shop. Just a path through the heather."

        maya "I want you to sit here for an hour."

        a "...Here."

        maya "Here. By the stones. No phone. No book. No talking. Just you and whatever shows up."

        a "What's going to show up?"

        maya "That's the question."

        "She smiles."

        maya "One hour. I'll be over there."

        "She gestures to a rock fifty metres away and walks towards it."

        menu:
            "One hour. Alone. With stones that are older than language."

            "The full hour. Stay, watch, listen.":
                $ ch4_test = "full_hour"
                $ add_stat("stat_sd", 2)
                $ add_rel("rel_maya", 1)

                "She sits."

                "Five minutes. Nothing happens. The wind. The heather. A lark somewhere, singing to nobody."

                "Ten minutes. Her mind yells at her. The essay. Tasha. The statistics module. Sophia's 78%%. The panic attack—"

                "Fifteen minutes. The yelling starts to thin."

                "Twenty minutes. Something else. The stones cast no shadow — the sky is too overcast. But there's a presence to them. A weight. Not physical. More like... attention. As though the stones are paying attention to her paying attention to them."

                "Thirty minutes. She notices the lichen on the uprights — orange: and grey-green. Decades of growth. Patient."

                "Forty minutes. A thought arrives: {i}I am not the first person to sit here like this.{/i}"

                "Fifty minutes. She cries, briefly. She doesn't know why. It feels like relief."

                "One hour. Maya returns."

                maya "What did you see?"

                a "I saw... patience. The stones are patient. They've been here so long that time doesn't mean the same thing to them. And I thought — I've been living in urgency. Every day is urgent. And these stones are the opposite of urgency."

                "Maya's face does something Amelia hasn't seen before. It softens past the enthusiasm and the grandiosity into something genuine and a little awed."

                maya "That's the most beautiful thing."

            "Manage thirty minutes. Restless but trying.":
                $ ch4_test = "half_hour"
                $ add_stat("stat_sd", 1)

                "She tries. She really tries."

                "For the first twenty minutes, she's present. The wind. The stones. The heather."

                "At minute twenty-five, her mind wins. Essay. Statistics. Tasha. The reading list that's seven pages long and she's only done one—"

                "She stands up. Walks to Maya."

                a "I'm sorry. I tried."

                maya "How long?"

                a "Maybe half an hour."

                maya "That's good."

                a "It doesn't feel good."

                maya "Discomfort is information. It tells you where the edge is. Now you know where yours is. Next time, push it by five minutes."

            "Can't do it. Leave after ten minutes.":
                $ ch4_test = "leave_early"
                $ add_rel("rel_maya", -1)

                "Ten minutes."

                "The wind. The cold. The absurdity of sitting in a field staring at rocks when she has an essay due Thursday."

                "She stands up. Walks back."

                a "Maya, I'm sorry. This isn't—"

                maya "It's okay."

                "But something in Maya's face closes. Just slightly."

                maya "Not everyone is ready for this. And that's — genuinely — okay."

                "It doesn't feel okay. It feels like she's disappointed someone she was beginning to admire."

    ## -----------------------------------------------------------------------
    ## ELENA'S TEST — The droll at the Merry Maidens
    ## -----------------------------------------------------------------------

    elif mentor_path == "elena":

        scene bg_merry_maidens
        with dissolve

        "The Merry Maidens. A stone circle near Penzance. Nineteen stones in a field."

        "Elena brings her at dusk. The sky is doing extraordinary things — purple and gold, the last light of a November day clinging to the horizon like someone unwilling to let go."

        "The stones are smaller than Amelia expected. Waist-height. Weathered. Lichen-covered. They look less like a monument and more like a gathering — a group of people who stopped and chose to stay."

        elena "Sit."

        "They sit on the grass inside the circle."

        elena "I'm going to tell you a story. A droll — that's what we call them in Cornwall. Just listen."

        "She takes a breath. And something about her changes — her voice finds a register that's deeper, older, the cadence of someone telling a story that has been told a thousand times by a thousand mouths and is somehow still new."

        elena "There was a girl who lived at the edge of the world. She'd grown up in a house by the sea and she'd read every book in the village and she knew things she couldn't explain. One day she walked inland, away from the water, because someone told her the answers were in the city."

        elena "In the city she found teachers — a clever one, a kind one, a wild one. She found friends. She found an enemy who looked just like her. And she found a girl who was drowning, not in water but in silence."

        elena "She tried to save the drowning girl. She tried so hard she forgot to save herself."

        elena "A year passed. She learned what the teachers taught. But the thing she came to learn — the thing the sea had always known — she couldn't find in any classroom."

        elena "So she walked back to the edge. And standing at the boundary between land and water, she understood: the answer was never in the books or the city or the teachers. The answer was in the act of walking. The going-out and the coming-back. The journey {i}was{/i} the answer."

        "Silence. The stones stand. The wind moves through the grass."

        elena "Now. What did the story tell you that I didn't?"

        menu:
            "The droll settles in the twilight air. Elena waits."

            "Connect it to her own journey.":
                $ ch4_test = "connection"
                $ add_stat("stat_ok", 2)
                $ add_rel("rel_elena", 1)

                a "The girl is me."

                "Elena says nothing."

                a "The house by the sea is London — well, it's Bromley, but — the city is Plymouth. The teachers are... you. And the others. And the drowning girl—"

                "She stops."

                a "The drowning girl is Sarah."

                "Her voice shakes slightly."

                a "And the answer — the going-out and coming-back — that's the whole point, isn't it? It's not about what you find. It's about what the journey makes you."

                elena "{i}Lowen.{/i}"

                a "What?"

                elena "Happy. That's the Cornish word. I'm happy."

                "It's the first time Amelia has seen Elena smile without reservation."

            "Analyse it as folklore and psychology.":
                $ ch4_test = "analyse"
                $ add_stat("stat_sd", 1)

                a "It's a hero's journey. Campbell's monomyth — departure, initiation, return. The structure is universal. You find it in every—"

                elena "I didn't ask for analysis. I asked what it {i}told{/i} you."

                "Amelia pauses."

                a "I'm not sure."

                elena "That's closer to the truth."

                "She stands. Brushes the grass from her coat."

                elena "Knowing the structure isn't the same as knowing the story. You can name every bone in the body and still not know what it means to be alive."

            "\"I don't understand.\"":
                $ ch4_test = "confusion"
                $ add_stat("stat_ok", 1)

                a "I don't understand."

                "Elena looks at her. Not disappointed. Something else."

                elena "Good."

                a "How is not understanding good?"

                elena "Because confusion is the beginning. Certainty is where people stop. You haven't stopped."

                "She stands."

                elena "The story will keep working on you. Drolls do that — they don't explain themselves. They wait until you're ready to hear what they've already said."

    ## =====================================================================
    ## CHOICE 4.4 — FRIEND CHECK-IN (All paths)
    ## Back on campus. Who does Amelia reach out to?
    ## =====================================================================

    scene bg_amelia_room_plymouth_night
    with dissolve

    "Sunday evening. Back on campus. The Cornwall trip is over but something lingers — a feeling she can't quite name. Like a bell struck in another room, still resonating."

    "She picks up her phone."

    menu:
        "Who does she reach out to?"

        "Text Sarah — she hasn't seen her in lectures.":
            $ ch4_checkin = "sarah"
            $ add_stat("stat_si", 1)
            $ add_rel("rel_sarah", 1)

            "{i}hey. haven't seen you in lectures. you okay? x{/i}"

            "She stares at the phone. A minute passes. Two."

            "Read receipts on. No reply."

            "Five minutes."

            "Then:"

            "{i}sarah: yeah sorry just been a bit tired. thanks for checking x{/i}"

            thought "'A bit tired.' That's what people say when they don't want you to worry. That's what {i}I{/i} say when I don't want people to worry."

            "She types:"

            "{i}no worries. kitchen tomorrow? raj is making something. you don't have to talk just come eat x{/i}"

            "A long pause."

            "{i}sarah: maybe. i'll try x{/i}"

            thought "'I'll try.' That's more honest than 'yes.' At least it's honest."

        "Call Ella to process the Cornwall experience.":
            $ ch4_checkin = "ella"
            $ add_stat("stat_si", 1)
            $ add_rel("rel_ella", 1)

            "She calls Ella."

            ella "Hellooooo!"

            a "I went to Cornwall."

            ella "You went to CORNWALL? Without me? Rude. How was it?"

            if mentor_path == "elena":
                a "I met a woman who wrote a note in a book I bought in Bromley before I even came to Plymouth. She took me to a holy well in the woods. There were rags tied to the trees. She told me a story that was about my life."

                ella "...Amelia."

                a "I know how it sounds."

                ella "It sounds like you've joined a cult."

                a "It's not a cult!"

                ella "That's EXACTLY what people in cults say!"

            else:
                a "My mentor took me. It was — I can't really explain it. The landscape is different there. Ancient. Like everything I've been reading about suddenly became... physical."

                ella "That's either deep or you hit your head on a rock. Either way I'm glad you're experiencing things."

            "They talk for an hour. About Cornwall, about Ella's job, about the fact that Ella's flatmate has started a podcast about crystals."

            ella "I miss you, you weirdo."

            a "I miss you too."

        "Find Lucas and talk about what she learned.":
            $ ch4_checkin = "lucas"
            $ add_stat("stat_sd", 1)
            $ add_rel("rel_lucas", 1)

            "She knocks on Lucas's door. It opens. He's at his desk, headphones around his neck, Jung open on his lap."

            lucas "Hey."

            a "Can I talk to you about something?"

            "He closes the book. Gives her his full attention. He's good at that — the full attention thing."

            if mentor_path == "maya":
                a "Maya took me to Tintagel. We talked about archetypes — the Hero's Journey. And she made me sit by some ancient stones for an hour in silence."

                lucas "How was the silence?"

                a "Unbearable. And then not."

                lucas "That's the whole of Jung's project in one sentence."

            elif mentor_path == "elena":
                a "I met someone. A woman called Elena. She told me a Cornish folk tale that was about my life."

                lucas "...Go on."

                a "She knew about a book I bought in London. She knew about me before I knew about her. And she says the alchemists and the psychologists are studying the same thing."

                "Lucas is very still."

                lucas "That's exactly what Jung says."

            else:
                a "My mentor took me to Cornwall. And something happened. I can't explain it — the landscape did something to me."

                lucas "Land does that. Places carry memory. That's not mysticism — there's actual research on place attachment and—"

                a "Lucas."

                lucas "Sorry. Continue."

            "They talk until midnight. Tea turns cold. The conversation is electric."

    ## -----------------------------------------------------------------------
    ## END OF CHAPTER
    ## -----------------------------------------------------------------------

    scene black
    with fade

    centered "{size=+6}End of Chapter Four{/size}"
    pause 2.0

    return
