###############################################################################
##
##  CHAPTER 3: REFUSAL OF THE CALL
##
##  Hero's Journey: The hero resists the adventure; doubt and fear.
##  Alchemical Stage: Putrefactio (Nigredo deepens) — everything rots.
##  Month: October–November. Location: Plymouth campus.
##  Palette: Greys, rain, claustrophobic corridors, strip lighting.
##  Mood: Homesickness. Doubt. The first real taste of difficulty.
##
##  Scenes: 10 (+1 hidden) | Choices: 8 (+1 negative) | Max: ~10-12 pts
##
###############################################################################

label chapter_3:

    stop music fadeout 1.0
    scene black
    with fade

    ## -----------------------------------------------------------------------
    ## TITLE CARD
    ## -----------------------------------------------------------------------

    centered "{size=+20}Chapter Three{/size}\n\n{size=+6}Refusal of the Call{/size}"
    pause 3.0

    ## =====================================================================
    ## ACT 1: THE WEIGHT (Weeks 1-3)
    ## =====================================================================

    ## -----------------------------------------------------------------------
    ## SCENE 3.1 — THE WORKLOAD
    ## Amelia's room and the library. Weeks 2-3. The honeymoon ends.
    ## -----------------------------------------------------------------------

    # play music "audio/ch3_rain.ogg" fadein 2.0 volume 0.5
    scene bg_amelia_room_plymouth_rain
    with dissolve

    "Weeks two and three. This is when it stops being an adventure and starts being a Tuesday."

    "The reading list is seven pages long. Single-spaced. Amelia has read approximately one page worth of it and already feels like she's drowning in a very academic sea."

    "She sits at her desk with three tabs open on her laptop: the lecture notes, the library catalogue, and — if she's honest — Instagram, which she opens every forty-five minutes like a nervous tic."

    thought "I don't understand any of this. Why is there so much statistics in a psychology degree? Nobody mentioned statistics. I was told there would be minds and feelings and interesting experiments with rats."

    "Her phone pings:"

    "{i}ella: hows it going  x{/i}"

    "{i}killing it obviously{/i}"

    "{i}ella: liar{/i}"

    "{i}there's so much reading ella. there's an obscene amount of reading. i think they want me to read every book ever written{/i}"

    "{i}ella: welcome to university babe its just reading ina fancy building{/i}"

    "She puts the phone down. Opens the Eysenck chapter. Reads about personality factors. Her eyes slide off the page like rain off a window."

    thought "Everyone else seems to be managing. Sophia — I've seen her in the library, she colour-codes her highlighters. She has a system. I don't have a system. I have anxiety and an internet connection."

    ## -----------------------------------------------------------------------
    ## SCENE 3.2 — LIZ'S HOMESICKNESS
    ## The communal kitchen, 2am. A Wednesday.
    ## -----------------------------------------------------------------------

    scene bg_halls_kitchen_night
    with dissolve

    "Two in the morning. Amelia is going to the kitchen for water because she's been staring at the ceiling for an hour and hydration seems like a reasonable excuse to stop."

    "The kitchen light is on."

    "Liz is at the table. Not talking. Not on her phone. Just sitting there, in her pyjamas, with a mug of something that's gone cold."

    "She's been crying. Her eyes are red and her face has that blotchy, swollen look that comes after the tears have stopped but the feeling hasn't."

    "She looks up."

    liz "Oh — sorry, I — it's nothing, I'm fine—"

    "She's not fine. The sentence breaks halfway through, like someone stepping on ice."

    ## CHOICE 3.1 — Liz's Homesickness
    menu:
        "It's 2am. The kitchen light hums. Liz is not fine."

        "Sit down, make tea, listen.":
            $ ch3_liz_response = "compassion"
            $ add_stat("stat_si", 1)
            $ add_stat("stat_mh", 1)
            $ add_rel("rel_liz", 1)

            "Amelia sits down. She fills the kettle. She makes two cups of tea — the proper way, with the bag left in, the way Grace taught her."

            "She puts one in front of Liz and sits opposite."

            a "You don't have to be fine."

            "That's all it takes. The dam breaks."

            liz "I miss my dog. I know that sounds stupid but I miss Marvin so much — he sleeps on my bed, he always sleeps on my bed, and the bed here is so {i}small{/i} and there's no warm patch where he—"

            "She can't finish the sentence."

            liz "And I miss my mum's roast. And I miss being able to walk to the shop and everyone knows your name. And Cardiff is only three hours away but it might as well be another country."

            "Amelia doesn't say 'it'll get better.' She doesn't say 'everyone feels this way.' She just sits there, holding her tea, and lets Liz talk."

            "They stay until three. Then four. At some point Liz starts laughing at herself, and then crying again, and then laughing. Amelia learns about Marvin's habit of sitting on the sofa like a person and Liz's brother who can't cook and her nan in Swansea who sends Welsh cakes in the post."

            "By the time they go back to bed, something has shifted. The homesickness isn't gone. But it's shared now, and that makes it lighter."

        "Check on her briefly, then go back to bed.":
            $ ch3_liz_response = "brief"
            $ add_stat("stat_mh", 1)

            a "Hey. Are you okay?"

            liz "Yeah, just — homesick. It's daft."

            a "It's not daft."

            "She means it. But she's also exhausted, and there's a 9am lecture, and the guilt of leaving mixes with the guilt of staying."

            a "Do you want me to sit for a bit?"

            liz "No, no. Honestly. Go back to sleep. I'm fine."

            "Amelia hesitates. Then nods."

            a "If you need anything — I'm right next door."

            "'Right next door' is about four metres of plasterboard. She lies in bed listening, but the kitchen goes silent."

            thought "I should have stayed. Maybe. I don't know."

        "Pretend she hasn't seen and go back to bed.":
            $ ch3_liz_response = "avoid"
            $ add_rel("rel_liz", -1)

            "Amelia pauses in the kitchen doorway. Her hand on the light switch."

            "She could go in. She could sit down. She could be the person who stays."

            "She fills a glass with water and goes back to her room."

            "Through the wall, she hears Liz blow her nose. Then silence."

            thought "She'll be okay. People are always okay eventually. Aren't they?"

            "She stares at the ceiling until sleep comes. It takes a long time."

    ## -----------------------------------------------------------------------
    ## SCENE 3.3 — TASHA'S FIRST ATTACK
    ## Corridor outside a seminar room. Mid-morning.
    ## -----------------------------------------------------------------------

    scene bg_psych_building_corridor
    with dissolve

    "Week three. The corridor outside the seminar room. People milling about with coffee and notes."

    "A voice — smooth, precise, calibrated to carry just far enough:"

    tasha "Oh, love, is that a {i}charity shop{/i} jacket?"

    "Amelia looks up. A blonde woman leaning against the wall with a takeaway coffee that costs more than Amelia's lunch. Perfect makeup. Expensive bag. The kind of smile that has teeth in it."

    tasha "No, genuinely, I think that's sweet. Very... sustainable."

    "Two of her friends — Amelia doesn't know their names yet — laugh on cue. It's not cruel laughter, exactly. It's worse: it's practised. They've done this before."

    "Amelia's coat is from a charity shop. It's corduroy. Grace found it last year and washed it three times until it smelled like home."

    ## CHOICE 3.2 — Tasha's First Attack
    menu:
        "The corridor is full of people. Several are watching."

        "Stand up to her calmly.":
            $ ch3_tasha_response = "confront"
            $ add_stat("stat_mc", 1)
            $ add_rel("rel_tasha", 1)

            "Amelia looks at this woman. Looks at the jacket. Looks back."

            a "Yeah, it is. My mum found it. Washed it three times." 
            
            "Beat."
            
            a "It's corduroy. In case you were wondering about the fabric."

            "She says it without heat. Without apology. Just a fact delivered at the same volume and with the same eye contact."

            "Tasha's smile flickers. Just for a moment — a micro-expression, the kind Amelia is learning about in class. Surprise. Something that might even be respect."

            tasha "Right. Well. It suits you."

            "She says it differently now. Not warm, exactly, but the blade has been withdrawn."

            "Later, Raj says: 'That's Tasha Reynolds. She's second year. She eats first-years for breakfast.' He pauses. 'But I think you gave her indigestion.'"

        "Walk away. Don't engage.":
            $ ch3_tasha_response = "walk_away"
            $ add_stat("stat_mh", 1)

            "Amelia says nothing. She picks up her bag, turns, and walks into the seminar room."

            "Behind her, she hears the laughter swell and then subside, like a wave that's found the shore and has nowhere else to go."

            thought "Don't react. That's what she wants. That's literally what she wants."

            "Her hands are shaking. She's glad her back is turned."

            "She sits down. Opens her notebook. The words swim."

            thought "It's just a coat. It's just a stupid coat."

            "But she pulls it tighter around herself. Grace's coat. Washed three times until it smelled like home."

        "Laugh along to fit in.":
            $ ch3_tasha_response = "comply"
            $ add_stat("stat_mc", -1)
            $ add_stat("stat_si", -1)
            $ add_rel("rel_tasha", 1)

            "Amelia hears herself laugh. It comes out before she's decided to make it — a reflex, a survival mechanism, the sound of a person choosing camouflage."

            a "Yeah, I know, it's a bit vintage, isn't it?"

            "Tasha smiles. The real kind, or at least the kind that looks real."

            tasha "Vintage. That's one word for it."

            "They laugh together. The corridor relaxes. Amelia is one of them, for a moment."

            "She hates how good it feels."

            thought "What was that? What did I just do?"

            "Later, alone, she thinks about Grace in the charity shop, holding the jacket up to the light: {i}'This one's you, Amelia. Feel the quality.'  {/i}"

            "She feels sick."

    ## =====================================================================
    ## ACT 2: CRACKS AND CONNECTIONS (Weeks 4-6)
    ## =====================================================================

    ## -----------------------------------------------------------------------
    ## SCENE 3.4 — ZARA'S CONFRONTATION
    ## Seminar room. Tasha says something racist. Zara responds.
    ## -----------------------------------------------------------------------

    scene bg_seminar_room
    with dissolve

    "Week four. A seminar on cognitive bias and social perception. Twelve students around a table. The tutor — a postgrad who's only three years older than them — leads the discussion tentatively."

    "The topic turns to implicit bias testing. Tasha raises her hand."

    tasha "I just think the whole 'unconscious bias' thing is a bit — isn't it just another way of saying everyone's secretly racist? Which seems a bit unfair, frankly."

    "She says 'frankly' like she's being brave, not ignorant."

    tasha "And if it's unconscious, then it's not really your fault, is it?"

    "The room shifts. Some people look at their notes. The tutor opens his mouth."

    "But it's Zara who speaks."

    "She's been sitting at the end of the table. Braids pulled back, a pen turning slowly in her hand, watching Tasha the way a boxer watches a clock."

    zara "Would you like me to explain how unconscious bias works? I've got a few examples. Lived ones. Real recent."

    "Her voice is level. But the room feels it — the temperature dropping, the air thinning."

    tasha "I wasn't saying—"

    zara "You were saying it's not anyone's fault. Which is convenient, isn't it? Because if nobody's at fault, nobody has to change. And if nobody has to change, then people like me keep having the same conversations in every classroom, every corridor, every Tuesday afternoon of our lives."

    "The silence is total."

    zara "But you know what — you're half right. It {i}is{/i} unconscious. For most people. The question is what you do when someone makes it conscious. When someone like me stands in front of you and says 'this is what it looks like.' Do you listen? Or do you call it unfair?"

    "Tasha says nothing. Her face is a mask."

    "The tutor says something about moving on. Nobody moves on."

    ## CHOICE 3.3 — Zara's Confrontation
    menu:
        "The seminar is over. People are packing up. Zara is putting her pen in her bag like nothing happened. Tasha has already left."

        "Go to Zara publicly, in front of everyone. \"That was brilliant.\"":
            $ ch3_zara_response = "public"
            $ add_stat("stat_mc", 1)
            $ add_stat("stat_si", 1)
            $ add_rel("rel_zara", 1)
            $ add_rel("rel_tasha", -1)

            a "That was brilliant."

            "She says it in the corridor. In front of people. Loud enough."

            "Zara looks at her. Assesses her. Decides."

            zara "You're in my corridor, aren't you? First floor?"

            a "Amelia. Room 14."

            zara "Zara. I'm second year. I know Tasha. She does this."

            a "I figured."

            zara "Most people just watch, you know. Like it's telly."

            a "That felt less like something you watch and more like something you stand next to."

            "The ghost of a smile."

            zara "Stand next to. I like that."

            "She nods, once, like something has been decided."

            zara "Come to the library sometime. I'm usually on third floor. We can complain about the reading list together."

        "Find Zara afterwards, privately. Talk to her.":
            $ ch3_zara_response = "private"
            $ add_stat("stat_si", 1)
            $ add_rel("rel_zara", 1)

            "Amelia waits until the room clears. Catches Zara in the stairwell."

            a "Hey — I just wanted to say. What you said in there. It mattered."

            "Zara looks at her. The guard is still up."

            zara "Thanks."

            a "I should have said something too. I wanted to."

            zara "But you didn't."

            "It's not an accusation. Just an observation."

            a "No. I didn't."

            zara "It's hard the first time. It's hard every time, honestly. But the first time is the worst."

            "She pauses."

            zara "Next time."

            a "Next time."

            "Zara nods. It's not approval, exactly. It's an invitation to be better."

        "Stay out of it entirely.":
            $ ch3_zara_response = "silent"

            "Amelia picks up her bag. Leaves the room. Says nothing."

            "She sees Zara in the corridor, walking alone, back straight, face composed. They make eye contact."

            "Zara notes the silence. Her expression doesn't change. But something closes — a door that was half-open, clicking shut."

            thought "I should have said something. I know I should have said something."

            "She didn't."

            thought "Next time. I'll say something next time."

            "But next time is always easier to promise than this time is to live."

    ## -----------------------------------------------------------------------
    ## SCENE 3.5 — LUCAS'S JUNG READING GROUP
    ## Lucas's room. Evening. Three people and a radical idea.
    ## -----------------------------------------------------------------------

    scene bg_lucas_room
    with dissolve

    "A note appeared on the kitchen noticeboard. Written in Lucas's small, precise handwriting:"

    "{i}Jung Reading Group. My room (17). Wednesday, 7pm. Bring the book or just bring yourself. — L{/i}"

    "Three people show up. Amelia. A second-year called James who leaves after twenty minutes. And Lucas, cross-legged on his bed with {i}The Archetypes and the Collective Unconscious{/i} open on his lap."

    lucas "Right. So. The collective unconscious."

    "He says it like someone testing whether the words will hold."

    lucas "Jung says we're all carrying these... patterns. Archetypes. Stories that are older than us, older than language. The Hero. The Shadow. The Anima. And we don't choose them — they choose us."

    "He looks up."

    lucas "I find this either the most terrifying idea in psychology or the most comforting. Haven't decided which."

    ## CHOICE 3.4 — Lucas's Jung Reading Group
    menu:
        "The room is small. Books stacked on the desk. A single lamp casting warm-dark shadows."

        "Engage deeply — this is what she's been thinking about.":
            $ ch3_jung_group = "engage"
            $ add_stat("stat_sd", 1)
            $ add_rel("rel_lucas", 1)

            a "I think it's both."

            lucas "Both?"

            a "Terrifying because it means there are parts of ourselves we don't control. Patterns we didn't choose that are running underneath everything we do. And comforting because—"

            "She pauses. Finds the thought."

            a "—because it means we're not alone in it. Everyone has a Shadow. Everyone has the same archetypes. The specifics are yours, but the structure is... universal."

            "Lucas is very still. The way he gets when he's really listening."

            lucas "That's... exactly right."

            "They talk for two hours. About the Shadow. About dreams. About whether the collective unconscious is real or a metaphor and whether it matters."

            if ch1_reading == "jung":
                a "The copy I got from a charity shop — someone wrote 'pay attention to the Shadow' in the margin."

                lucas "Pay attention to the Shadow."

                "He lets the phrase sit in the room."

                lucas "Someone was trying to pass something on. Through the margin of a book. That's basically what Jung would do."

            "By the end, the tea is cold and the light has changed and something between them has become real."

        "Attend but she's distracted by the workload.":
            $ ch3_jung_group = "distracted"
            $ add_stat("stat_aa", 1)

            "She tries to engage. She does. But her mind keeps sliding back to the essay that's due Friday and the Eysenck chapter she hasn't finished and the statistics problem set that's sitting on her desk like a threat."

            a "Sorry — can you say that again? I'm a bit..."

            lucas "Overwhelmed?"

            a "Is it that obvious?"

            lucas "You've checked your phone three times in twenty minutes. And you're holding your pen like a weapon."

            "She puts the pen down."

            a "I want to be here for this. I really do. I just—"

            lucas "Go. Do the essay. We can talk about Jung anytime."

            "He means it. There's no judgement in it — just the quiet pragmatism of someone who understands that sometimes the urgent defeats the important."

        "Skip it — too overwhelmed.":
            $ ch3_jung_group = "skip"

            "She doesn't go."

            "She sees the note on the noticeboard. Thinks about it. Starts walking towards Lucas's room at 6:55pm, then turns around and goes back to her desk."

            thought "I can't. I've got the essay. I've got the reading. I've got to — I can't just sit around talking about the collective unconscious when I'm drowning in the collective reading list."

            "She texts Lucas:"

            "{i}sorry, cant make it tonight. drowning in eysenck{/i}"

            "He replies:"

            "{i}another time. the unconscious will wait{/i}"

            "She stares at the message. There's something in that — {i}the unconscious will wait{/i} — that sounds like more than a joke."

    ## -----------------------------------------------------------------------
    ## SCENE 3.6 — MAYA'S CEREMONY
    ## Maya's room. Evening. Candles, incense, something unfamiliar.
    ## -----------------------------------------------------------------------

    scene bg_maya_room_ceremony
    with dissolve

    "Maya corners Amelia in the philosophy corridor on a Thursday afternoon."

    maya "Okay, so, I know this is going to sound weird."

    a "When you start with that, it's always going to be weird."

    maya "Fair. But listen — I'm doing a thing tonight. A meditation thing. In my room. Candles, incense, maybe some chanting if the mood takes us."

    a "...Chanting."

    maya "Gentle chanting! Meditative chanting! Not cult chanting. There's a difference."

    "She hands Amelia a flyer she's made herself — hand-drawn mandalas, the words {i}MINDFUL EVENING{/i} in purple ink."

    maya "It's about presence. Being in your body. Connecting to something beyond the academic grind."

    "She pauses."

    maya "I think you'd get something out of it. Something you're not getting from the textbooks."

    ## CHOICE 3.5 — Maya's Ceremony (★ ELENA KEY 2 of 3)
    menu:
        "Maya's room, 8pm. The invitation hangs in the air between them."

        "Attend and participate fully.":
            $ ch3_maya_ceremony = "full"
            $ add_stat("stat_ok", 1)
            $ add_rel("rel_maya", 1)
            $ elena_key_ceremony = True

            scene bg_maya_room_candlelit
            with dissolve

            "Maya's room has been transformed. The overhead light is off. Instead: candles — twenty, thirty — on every surface. The air is thick with sandalwood incense. A low drone of music from a Bluetooth speaker, something Amelia doesn't recognise — bowls, maybe, or throat singing."

            "There are four other people. They sit in a circle on cushions. Maya welcomes them with a stillness that's completely unlike her usual self — no rapid-fire tangents, no enthusiastic digressions. Just presence."

            maya "We're going to sit for twenty minutes. No talking. No phones. Just breathing. Let your thoughts come and go like clouds. Don't chase them. Don't fight them."

            "Amelia closes her eyes."

            "At first, nothing. Her brain does its usual thing — the essay, the email she forgot to send, the conversation with Tasha replaying on a loop—"

            "But then. Slowly. The chatter fades."

            "The incense becomes the whole room. The candle warmth. The sound of other people breathing."

            "She feels — she doesn't know what she feels. Present. Grounded. Like she's actually {i}in{/i} her body for the first time in weeks."

            "And then, briefly, something else. A feeling she can't name. Like standing at the edge of something vast and dark and being — not afraid. Not afraid."

            "Twenty minutes. Maya rings a small bell."

            maya "Welcome back."

            "Amelia opens her eyes. The room is the same. But she isn't, quite."

            maya "How was that?"

            a "I don't know. I felt... something."

            maya "That's the most honest answer I've ever heard."

            "She smiles. The warm, slightly unsettling Maya smile."

            maya "The something is the beginning. We'll talk about it."

        "Attend but observe from the edge.":
            $ ch3_maya_ceremony = "observe"
            $ add_stat("stat_sd", 1)
            $ add_rel("rel_maya", 1)

            scene bg_maya_room_candlelit
            with dissolve

            "Amelia goes. She sits on a cushion near the door. She doesn't close her eyes all the way."

            "She watches the others — their faces softening, their breathing slowing. Maya, cross-legged at the centre, is luminous in the candlelight. There's something almost archaeological about it — like watching a practice that's been happening for thousands of years in every culture on Earth."

            "She doesn't fully participate. The chanting feels too exposed, too vulnerable. But she watches. And watching, she learns: that this is not performance. These people mean it."

            "Afterwards, Maya finds her."

            maya "You didn't close your eyes."

            a "I wanted to see."

            maya "Seeing is its own practice. Not everyone gets that."

            "She looks at Amelia with an expression somewhere between affection and assessment."

            maya "Next time, try closing them. Not because it's better — but because what you see with closed eyes is different from what you see with open ones."

        "Decline — it's not her thing.":
            $ ch3_maya_ceremony = "decline"

            a "I appreciate the invite, Maya. I really do. But it's... not really my thing."

            maya "That's okay. The door's open."

            "She says it without judgement, without disappointment. Just a fact."

            "In her room that night, Amelia hears something through the wall — a bell, the smell of incense under the door, a low hum."

            thought "I should have gone. Maybe."

            "But she didn't. And the door stays open, but the distance grows."

    ## -----------------------------------------------------------------------
    ## SCENE 3.7 — THE PANIC ATTACK
    ## The library, fourth floor. Late evening. Midterms.
    ## -----------------------------------------------------------------------

    scene bg_library_night
    with dissolve

    # play music "audio/ch3_tension.ogg" fadein 2.0 volume 0.6

    "Week five. The library. Fourth floor. The window overlooking the city. Below: lights. Above: clouds. Inside Amelia's chest: a growing planet of anxiety that's been expanding for three days."

    "She's been here since two in the afternoon. It's now nine. The statistics textbook is open to the same page it was open to at four."

    "She can't do this."

    "The thought arrives not as an opinion but as a physical sensation — her chest tightening, her hands going cold, her breath getting shorter and shorter until—"

    thought "I can't — I can't breathe —"

    "Her heart is racing. The words on the page blur. The fluorescent light above her starts to hum — did it always hum? — and the sound gets louder—"

    thought "What's wrong with me what's wrong what's happening—"

    "She grabs the edge of the desk. Her knuckles are white."

    thought "I'm having a — this is a — I know what this is from the textbook, I read about it, it's a panic attack, I'm having a panic attack in a library about a panic I'm panicking about panicking—"

    "Her body doesn't care what the textbook says. Her body says: danger. Her body says: run."

    "She puts her head down on her arms. Breathes. Counts. Loses count. Starts again."

    "Three minutes. Five. Seven."

    "It passes. They always pass. But the aftermath — the shaky, wrung-out, jelly-legged feeling — stays."

    ## CHOICE 3.6 — The Panic Attack
    menu:
        "She's sitting in the library with the ghost of a panic attack still trembling in her limbs. She needs to do something."

        "Go to student counselling tomorrow. Ask for help.":
            $ ch3_panic_response = "counselling"
            $ add_stat("stat_mh", 2)

            "She takes out her phone. Opens the university website. Finds the student wellbeing page."

            thought "This is going to feel like admitting I'm failing."

            "She books an appointment. Tomorrow, 2pm, Dr. Simmons' office."

            thought "Or maybe it's going to feel like admitting I'm human."

            "She packs up her things. Walks home through the wet streets. It's raining — it's been raining for weeks, it's Devon, it's always raining — and for once the rain feels like what it is: just water. Not a metaphor. Not a punishment. Just water."

            "The next day, she goes. The chair in Dr. Simmons' office is, as advertised, very comfortable."

            simmons "Right, come in, sit down. Tea? I've got ginger biscuits or the ones from Aldi that taste like sadness."

            a "...Ginger, please."

            "It is the hardest and simplest thing she's ever done."

        "Push through. Finish the essay. Don't stop.":
            $ ch3_panic_response = "push_through"
            $ add_stat("stat_aa", 1)

            thought "Get up. Open the book. Read the page. Write the paragraph. Get up."

            "She gets up."

            "She reads the page. Writes the paragraph. Read the next page. Write the next paragraph."

            "The panic is a thing that happened. She files it under 'not now' and keeps going. The essay gets written. It's not her best work, but it exists, and tonight existence is enough."

            "She submits it at 11:47pm. Walks home in the rain. Lies in bed staring at the ceiling."

            thought "I'm fine. I'm managing. Everybody pushes through. That's what you do."

            "The ceiling doesn't argue."

        "Call Ella. Just hear her voice.":
            $ ch3_panic_response = "ella"
            $ add_stat("stat_si", 1)
            $ add_rel("rel_ella", 1)

            "She picks up her phone with shaking hands and calls the only person who has never, in twelve years, failed to answer."

            "Ring. Ring."

            ella "Hello?"

            a "Ella."

            "That's all she says. Ella's name. But Ella hears everything in it."

            ella "Okay. You're sitting down, right? Tell me you're sitting down."

            a "I'm in the library."

            ella "Okay. Good. Library is safe. Libraries are excellent. Tell me five things you can see."

            a "What?"

            ella "It's a grounding thing. I saw it on TikTok. Five things you can see. Go."

            a "Um — the desk. The book. The window. A girl with a red backpack. The fire exit sign."

            ella "Good. Now four things you can touch."

            "She does the exercise. Four things, three things, two things, one. By the end, the shaking has stopped."

            ella "There. Better?"

            a "How did you know to do that?"

            ella "Babe. I've been having panic attacks since Year 10. You think I was just naturally chaotic? No. Chaos is my coping mechanism."

            "They laugh. It's a thin laugh, but it holds."

            ella "Go home. Make toast. Get in bed. I'll stay on the phone till you're home."

            "She does."

    # --- SONG SLIDESHOW: "Two Birds" — Homesickness, missing Ella ---
    call slideshow_ch3_two_birds

    ## =====================================================================
    ## ACT 3: THE PIT (Weeks 7-9)
    ## =====================================================================

    ## -----------------------------------------------------------------------
    ## SCENE 3.8 — SARAH ON THE HOE
    ## Plymouth Hoe. Grey afternoon. The bench.
    ## -----------------------------------------------------------------------

    scene bg_plymouth_hoe_grey
    with dissolve

    # play music "audio/ch3_hoe.ogg" fadein 3.0 volume 0.4

    "It's not planned. They run into each other after a Tuesday lecture — Amelia heading for the library, Sarah heading... somewhere else. Somewhere that isn't a building."

    sarah "I was going to walk to the Hoe. If you want to come."

    "She says it like someone offering something they expect to have refused."

    a "Yeah. Okay."

    "They walk without talking. Through campus, down the hill, past the Naval Memorial with its long lists of names, to the Hoe — the wide green promenade that drops away to the sea."

    "The bench faces south. Grey sky. Grey water. The breakwater in the distance like a dark line drawn by someone who'd given up."

    "Smeaton's Tower is behind them — red and white, absurd and beautiful."

    "They sit."

    "Sarah holds her tea in both hands — she's always holding tea, Amelia realises, like it's the only warm thing she trusts."

    "They talk. Lectures. Weather. Whether the library café charges too much for a toastie. (It does.)"

    "And then Sarah goes quiet."

    "Not the normal quiet — not the thinking pause or the comfortable silence. A different quiet. The kind where someone is deciding whether to step onto thin ice."

    sarah "Do you ever feel like you're watching your life from outside?"

    "She says it to the sea, not to Amelia."

    sarah "Like you're in the audience and the play is happening and you can see yourself on stage but you can't get back in?"

    "The seagulls scream. The wind pulls at their coats."

    ## CHOICE 3.7 — Sarah on the Hoe ("Do you ever feel...")
    menu:
        "Sarah's question hangs in the salt air. She hasn't looked at Amelia."

        "\"Yeah... I think I do sometimes.\" (Honest vulnerability)":
            $ ch3_sarah_bench = "vulnerable"
            $ add_stat("stat_mh", 1)
            $ add_rel("rel_sarah", 2)
            $ sarah_bench_choice = "vulnerable"

            a "Yeah..."

            "She thinks about it. Really thinks about it."

            a "I think I do sometimes. Not all the time. But there are moments where — yeah. Like I'm not really here. Like I'm watching a version of me going through the motions."

            "Sarah turns. Looks at her. Her eyes are wide, and Amelia sees something in them she hasn't seen before: relief."

            sarah "You too?"

            a "Yeah."

            "Silence. But not a bad silence. The kind that has room in it."

            sarah "I thought it was just me. I thought — everyone else seems so {i}in{/i} it, you know? Like they're actually living their lives and I'm just... standing behind glass."

            a "Sometimes I think the people who look most 'in it' are just better at pretending."

            "Sarah's almost-smile. It lasts longer this time."

            sarah "Thanks for not telling me it's just stress."

            a "Is it just stress?"

            sarah "No."

            "They sit. The sea doesn't care, but the bench does, and they're on it together."

        "\"That sounds really hard. Do you want to talk about it?\"":
            $ ch3_sarah_bench = "clinical"
            $ add_stat("stat_si", 1)
            $ add_rel("rel_sarah", 1)
            $ sarah_bench_choice = "clinical"

            a "That sounds really hard. Do you want to talk about it?"

            "Sarah blinks. Recalibrates. Something closes slightly — not all the way, but enough."

            sarah "It's fine. I'm fine. Just thinking out loud."

            "She takes a sip of tea."

            sarah "University does weird things to your head, doesn't it?"

            a "Yeah. It does."

            "They talk for a bit longer. About safer things — the essays, the rain, a funny thing Raj said at dinner."

            "Sarah doesn't come back to the thing she said. The crack opened; Amelia approached it as a problem to solve, not a feeling to share. Close, but not quite."

            "When they part, Sarah's smile is polite. Grateful. But the window didn't open all the way."

        "\"I'm sure it'll pass. University is stressful for everyone.\"":
            $ ch3_sarah_bench = "dismiss"
            $ add_rel("rel_sarah", -1)
            $ sarah_bench_choice = "dismiss"

            a "I'm sure it'll pass. University is stressful for everyone."

            "Sarah nods."

            sarah "Yeah. You're right."

            "The light goes out of her voice."

            "She changes the subject. A quick question about the essay deadline. A comment about the weather. They walk back to campus."

            "At the corridor, Sarah says 'see you' with the specific brightness of someone who is closing a door."

            "She does not raise the subject again."

    ## -----------------------------------------------------------------------
    ## SCENE 3.9 — SOPHIA AND HAWTHORNE'S FEEDBACK
    ## Psych building. Assessment results. The pecking order established.
    ## -----------------------------------------------------------------------

    scene bg_lecture_theatre
    with dissolve

    "Midterm assessments."

    "The marks go up. Not publicly — this isn't secondary school — but word travels."

    "Sophia Langford got 78%%. The highest in the cohort."

    "Amelia got 62%%. Which is fine. It's a 2:1. It's respectable. It's objectively, demonstrably, irrefutably fine."

    thought "It's not fine."

    "She sees Sophia in the library. Red curly hair, highlighters arranged by colour, a study schedule that's probably laminated."

    "Sophia doesn't know Amelia exists, which is somehow worse than if she were competitive about it."

    "And then: Hawthorne's essay feedback. She checks the university portal at 7am because she can't sleep anyway. His comments appear in the margins, precise and devastating:"

    "{i}\"An adequate survey of the literature. I note, however, that adequacy is not what this programme is for. Your analysis relies on summary where it should offer critique. You can describe what Eysenck said. Can you tell me where he was wrong? Third paragraph, first sentence: citation needed. Fourth paragraph: this is an opinion, not an argument — there is a difference. Come to office hours.\" - AH{/i}"

    ## CHOICE 3.8 — Hawthorne's Essay Feedback
    menu:
        "She stares at the screen. 62%% and the most thorough dismantlement of her work she's ever received."

        "Ask for a meeting. Learn from it. Grow.":
            $ ch3_hawthorne_response = "grow"
            $ add_stat("stat_aa", 1)
            $ add_stat("stat_sd", 1)

            "She sends the email before she can talk herself out of it:"

            "{i}\"Professor Hawthorne — Thank you for your feedback. I'd like to discuss how I can improve. Would any of your office hours this week be suitable? Amelia James\"{/i}"

            "He replies within the hour. (He always replies within the hour.)"

            "{i}\"Miss James — Thursday, 2pm. Bring the essay and a willingness to be wrong about something. - AH\"{/i}"

            thought "A willingness to be wrong about something."

            "The meeting is hard. He dismantles her argument point by point, then makes her rebuild it. He asks questions she can't answer and waits while she tries. At one point, she says 'I don't know' and he says 'Good. That's where thinking begins.'"

            "She leaves his office humbled. Not broken — humbled. There's a difference."

        "Feel crushed but work harder in silence.":
            $ ch3_hawthorne_response = "silent_grind"
            $ add_stat("stat_aa", 1)

            "She reads the feedback three times. Then she opens a new document and starts rewriting the essay from scratch."

            "Not because he asked her to. Because she needs to prove — to herself, to the empty room, to the ghost of Sophia's 78%% — that she can do better."

            "She works until midnight. Until two. The new version is angrier, sharper, better."

            "She doesn't send it. It stays on her desktop, titled 'REAL_ESSAY_v2.doc', and she never opens it again."

            thought "I am going to get so good at this that he runs out of criticisms."

            "It's a productive thought. It's also, she suspects, a lonely one."

        "Compare herself to Sophia and spiral.":
            $ ch3_hawthorne_response = "spiral"
            $ add_stat("stat_mh", -1)

            thought "78%%. She got 78%%. I got 62%%. That's a sixteen-point gap. That's not a gap, that's a chasm, that's a—"

            "The spiral starts fast and goes faster."

            thought "She's smarter than me. She's always going to be smarter than me. Her parents are professors. She grew up in Oxford. She probably read Eysenck before she could walk."

            "Amelia closes the laptop."

            thought "I don't belong here. I'm from Bromley and I don't have colour-coded highlighters and my jacket is from a charity shop and I got 62%% and Sophia got 78%% and Professor Hawthorne thinks I'm adequate and {i}adequate isn't what this programme is for{/i}—"

            "She lies on her bed and stares at the ceiling. The glow-in-the-dark stars aren't here. She left them in Bromley."

            thought "I'm not good enough."

            "The thought stays. It breeds."

    ## -----------------------------------------------------------------------
    ## HIDDEN SCENE 3.H — THE LIBRARY DISCOVERY
    ## (Only triggers if player chose Paracelsus in Chapter 1)
    ## -----------------------------------------------------------------------

    if ch1_bookshop == "paracelsus":

        scene bg_library_night
        with dissolve

        "Late one night, alone in the library. She's procrastinating, which is to say she's reading the wrong book."

        "She takes the Paracelsus out of her bag. She does this sometimes — opens a random page, reads a paragraph, tries to make sense of it. She can never make sense of it."

        "But tonight, she turns to the back pages and finds something she missed before. In the same handwriting as the note inside the cover — the same neat, old-fashioned cursive — a margin note beside a passage on {i}the pellar of Penzance:{/i}"

        "{i}\"Seek the one who walks between. She is enrolled but not enrolled. She studies but not what they think. Ask her about the ouroboros.\"{/i}"

        thought "...What?"

        "She takes out her phone and searches: {i}pellar cornwall{/i}"

        "Wikipedia: {i}A pellar (from Cornish 'pellor', meaning 'to repel') was a type of Cornish cunning person — a folk healer, diviner, and magical practitioner. Pellars were consulted for healing, breaking curses, divination, and protection. The tradition is believed to have been practised in Cornwall for centuries.{/i}"

        thought "A Cornish... folk healer? Who's {i}enrolled{/i}? At the university?"

        "She reads the note again. {i}She is enrolled but not enrolled. She studies but not what they think.{/i}"

        "It can't be real. Someone wrote these notes years ago. Decades, maybe. The woman they're describing — if she ever existed — is long gone."

        thought "Unless she isn't."

        "She puts the book away."

        thought "Unless she isn't."

        $ add_stat("stat_ok", 1)

    ## -----------------------------------------------------------------------
    ## SCENE 3.10 — END OF CHAPTER / MENTOR CALCULATION
    ## Amelia's room. Night. The weight settles.
    ## -----------------------------------------------------------------------

    scene bg_amelia_room_plymouth_rain
    with dissolve

    "November. The rain hasn't stopped in a week."

    "Amelia lies in bed listening to it. The radiator clanks. Next door, Liz is watching something on her laptop — the muffled sound of marine life narrated by David Attenborough."

    "She hasn't called Ella in three days. She texts, but it's not the same."

    "She checks her phone. A message from Lucas: {i}library tomorrow?{/i}"

    "A message from Raj: {i}leftover biryani in the fridge, your name on it{/i}"

    "Nothing from Sarah."

    thought "It's getting harder to pretend I know what I'm doing."

    "She rolls over. The pillow smells like this place now. Not home. This place."

    thought "Maybe that's okay. Maybe pretending is just what everyone does. Maybe nobody actually knows and we're all just — walking through it, hoping the ground holds."

    "The rain. The radiator. Attenborough's voice through the wall."

    thought "The ground holds. I think. For now."

    ## -----------------------------------------------------------------------
    ## MENTOR ASSIGNMENT CALCULATION
    ## (Hidden — runs at end of Ch3 to determine Ch4 path)
    ## -----------------------------------------------------------------------

    # Calculate mentor scores
    python:
        scholar_score = stat_aa + stat_mc
        healer_score = stat_mh + stat_si
        seeker_score = stat_sd + stat_ok

        # Elena override: requires OK >= 5 AND both Elena keys
        if stat_ok >= 5 and elena_key_paracelsus and elena_key_ceremony:
            mentor_path = "elena"
        elif scholar_score >= healer_score and scholar_score >= seeker_score:
            mentor_path = "hawthorne"
        elif healer_score >= scholar_score and healer_score >= seeker_score:
            mentor_path = "simmons"
        else:
            mentor_path = "maya"

    scene black
    with fade

    centered "{size=+6}End of Chapter Three{/size}"
    pause 2.0

    return
