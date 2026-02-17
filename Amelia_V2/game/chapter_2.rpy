###############################################################################
##
##  CHAPTER 2: THE CALL TO ADVENTURE
##
##  Hero's Journey: The summons to leave the ordinary world.
##  Alchemical Stage: Early Nigredo — the initial dissolution; leaving the vessel.
##  Month: Early October. Location: London → Plymouth.
##  Palette: Greys, slate blues, sea-silver, motorway monotone to coastal light.
##  Music: Movement. Engine hum. Wind. Then — the sea.
##
##  Scenes: 9 (+1 conditional) | Choices: 5 (+1 conditional) | Max: ~8-10 pts
##
###############################################################################

label chapter_2:

    $ current_chapter = 2
    stop music fadeout 1.0
    scene black
    with fade

    ## -----------------------------------------------------------------------
    ## TITLE CARD
    ## -----------------------------------------------------------------------

    centered "{size=+20}Chapter Two{/size}\n\n{size=+6}The Call to Adventure{/size}"
    pause 3.0

    ## -----------------------------------------------------------------------
    ## SCENE 2.1 — MORNING OF THE MOVE
    ## The James household. Early morning. The car is packed.
    ## -----------------------------------------------------------------------

    # play music "audio/ch2_morning.ogg" fadein 2.0 volume 0.5
    scene bg_james_house_morning
    with dissolve

    "Six-thirty in the morning. The sky hasn't decided what colour it wants to be yet — that uncertain grey-pink of early autumn dawn."

    "The car is packed with a precision that would make a Tetris player weep. David has loaded everything — twice, because Grace rearranged it the first time. The boot is full. The back seat is full. The front passenger footwell contains a Tupperware tower of food that Grace has been assembling since 4am."

    grace "There's rice and peas in the blue one, ackee in the green, and patties in the bag. The patties are for the drive. David, don't eat all the patties on the M5."

    david "I won't eat the patties."

    grace "You will eat the patties. I know you."

    "Amelia stands at the front door with her bag over one shoulder. The house smells of coffee and garlic and Grace's anxious love."

    "Lily is leaning against the hallway wall in her pyjamas. She is barefoot. Her arms are crossed and her face is doing that thing sixteen-year-olds do when they're trying very hard not to feel anything."

    lily "Bit early, isn't it."

    a "It's a four-hour drive."

    lily "Could've left at a normal time like normal people."

    "The silence that follows is louder than the words."

    ## CHOICE 2.1 — Goodbye to Lily
    menu:
        "Amelia looks at her sister. Lily isn't looking back."

        "\"Look after mum and dad for me, yeah?\"":
            $ ch2_lily_goodbye = "protective"
            $ add_stat("stat_si", 1)
            $ add_rel("rel_lily", 1)

            a "Lils. Look after mum and dad for me, yeah?"

            "Lily's jaw tightens."

            lily "They don't need looking after."

            a "Yeah, they do. Mum's going to pretend she's fine for about three days and then cry in Asda. And Dad's going to start a new project in the garage that nobody asked for."

            "A beat. The tiniest crack in Lily's armour."

            lily "...He's already bought wood."

            a "See? You're the one who's here now. You're the one who matters."

            "Lily unfolds her arms. Steps forward. Hugs Amelia with the particular ferocity of someone who's been pretending they don't want to."

            lily "You'd better text me. Like, actually text me. Not just heart-react my Instagram stories."

            a "Every day."

            lily "Liar."

        "\"You can call me anytime. About anything. I mean it.\"":
            $ ch2_lily_goodbye = "mentoring"
            $ add_stat("stat_mc", 1)
            $ add_rel("rel_lily", 1)

            a "Lils. You can call me anytime. About anything. I mean it."

            "Lily looks at the floor."

            lily "Why would I need to call you?"

            a "Because you're sixteen and the world is rubbish and sometimes you need someone who isn't Mum and Dad."

            "A pause."

            a "I'm serious. Three in the morning. Doesn't matter. If something's going on — if you need to talk about anything, anything at all — you ring me."

            "Lily blinks. Something in the way Amelia says 'anything at all' lands differently."

            lily "...Okay."

            a "Promise?"

            lily "God, you're so dramatic."

            "But she nods. And when she hugs Amelia, she holds on for longer than expected."

    "Grace appears in the doorway. Eyes already red."

    grace "Right. Are we — is it time?"

    david "It's time, love."

    "Grace hugs Amelia. The kind of hug that has a whole speech compressed into it. She smells of cocoa butter and kitchen and home."

    grace "You call me when you arrive."

    a "I will."

    grace "You eat proper food."

    a "I will."

    grace "You don't let anyone make you feel small."

    "That one isn't a question."

    a "I won't, Mum."

    "Grace holds her face between her hands. Studies it. Files it away."

    grace "My girl."

    "David is already in the car. Engine running. Pretending he's not emotional by being logistical."

    "Amelia gets in. Seatbelt on. The Tupperware on top of the Tupperware on top of her left foot."

    "In the rear-view mirror: Grace waving. Lily standing behind her, one hand raised, then quickly dropped."

    "The car pulls away."

    ## -----------------------------------------------------------------------
    ## SCENE 2.2 — THE DRIVE
    ## The M5 southbound. Four hours. Grey motorway.
    ## -----------------------------------------------------------------------

    scene bg_motorway_daytime
    with dissolve

    # play music "audio/ch2_drive.ogg" fadein 2.0 volume 0.4

    # --- SONG SLIDESHOW: "Lighthouse in the Fog" — The drive to Plymouth ---
    call slideshow_ch2_lighthouse_in_the_fog

    "The M25. The M3. The M5. England unspooling through the windscreen in shades of grey and green."

    "David drives the way he does everything — steady, careful, both hands on the wheel. Radio 2 on low. The wipers going intermittently because it's that annoying kind of rain that can't commit."

    "They pass Stonehenge. It's smaller than you'd think — it always is."

    "Somewhere past Exeter, David clears his throat. This is how he begins difficult sentences: with a mechanical sound, like an engine turning over."

    # Conditional: If dinner speech was "degree" (first in family)
    if ch1_dinner_speech == "degree":
        david "About what you said. At dinner."

        a "Which bit?"

        david "The degree. Being the first."

        "He checks his mirror. Changes lanes. Checks it again."

        david "You know we're proud of you whatever happens, right? Degree or no degree. Your mum didn't say it because she was — well, you know your mum. But I'm saying it now."

        "He grips the steering wheel a fraction tighter."

        david "You don't owe us anything, Amelia. You understand? You being happy is enough."

        "She looks at him. His jaw is set. His eyes are on the road."

        a "Thanks, Dad."

        david "Right. Good. That's — right."

        "He turns the radio up slightly. Subject closed."

    elif ch1_dinner_speech == "self":
        david "About what you said last night. About finding out who you are."

        a "Yeah?"

        david "I didn't find out who I was until I was about thirty-five. And even then I wasn't sure. So don't be too hard on yourself if it takes a while."

        a "What changed at thirty-five?"

        david "Your mum told me to stop trying to be someone and just be someone. I still don't know exactly what she meant. But something clicked."

        "He gives her the smallest smile."

        david "You'll work it out. You're smarter than me."

        a "That's a low bar, Dad."

        david "Oi."

    elif ch1_dinner_speech == "esoteric":
        david "That alchemy stuff you were talking about."

        a "You don't have to pretend to be interested, Dad."

        david "I'm not pretending. I don't understand it, but I could see in your face that it matters to you. And the things that matter to you matter to me."

        "He pauses."

        david "Just... don't join a cult, yeah?"

        a "Dad."

        david "I'm serious. No cults. That's the one rule."

        a "No cults. Promise."

        david "Right."

    "The miles pass. Service station tea that tastes like regret. A sandwich that Grace packed that tastes like love. Rain on the windscreen, then none, then rain again."

    "David eats exactly three of the patties. He was never not going to eat the patties."

    ## -----------------------------------------------------------------------
    ## SCENE 2.3 — FIRST SIGHT OF PLYMOUTH
    ## The crest of a hill. The city appears.
    ## -----------------------------------------------------------------------

    scene bg_plymouth_first_sight
    with dissolve

    "And then — between one hill and the next — the sea."

    "It arrives without warning. The road rises, and there it is: Plymouth spread out below, grey rooftops tumbling down to the waterfront, the Sound wide and silver-blue, and beyond it — open ocean. Sky and water meeting in a line so faint it might be imagined."

    "Amelia's breath catches."

    thought "Oh."

    "She's seen the sea before. Brighton with Ella. Margate with Mum. But this is different. This sea is not beside something — it's at the edge of everything. This is where the land runs out."

    david "There it is."

    "He says it quietly, like he's seeing it too."

    thought "This is real. I'm actually doing this."

    "They follow the signs to the university. Down through streets she doesn't know, past shops she's never been to, roundabouts that don't exist on her mental map. Everything is new. Everything is slightly too bright."

    ## -----------------------------------------------------------------------
    ## SCENE 2.4 — HALLS OF RESIDENCE
    ## University campus. A corridor. Doors numbered and impersonal.
    ## -----------------------------------------------------------------------

    scene bg_halls_corridor
    with dissolve

    "The corridor smells of paint and bleach and industrial carpet. Fluorescent light. Numbered doors. A fire extinguisher mounted on the wall like a threat."

    "David carries the heaviest box. Amelia carries the rest. They make three trips."

    "Her room is Room 14. Single bed, single desk, single wardrobe. A window that looks out onto the car park. (Not the sea. The car park.)"

    "David puts the last box down and stands in the middle of the room, hands in his pockets, looking at the dimensions of his daughter's new life."

    david "It's... cosy."

    a "It's tiny, Dad."

    david "Cosy. That's what I said."

    "He helps her make the bed. Grace-standard hospital corners. He stacks the Tupperware in the minifridge and labels them with a Sharpie he brought specifically for this purpose."

    "And then it's time."

    david "Right, then."

    a "Yeah."

    "He pulls her into a hug. David doesn't hug often, but when he does, he means it — solid, silent, his hand on the back of her head like she's still five years old."

    david "You call your mum."

    a "I know."

    david "And eat the food. It'll go off."

    a "I know, Dad."

    david "Right."

    "He leaves. She listens to his footsteps down the corridor — that particular heavy, steady tread. A door opens. Closes. A car engine starts in the car park below."

    "She watches from the window. The van pulling away. The indicator light blinking left. Gone."

    "She sits on the bed. The duvet is wrong — it's the one from home, but it smells like a new room instead of her old one."

    thought "This is it."

    "The walls are white. The desk is empty. The wardrobe is open and waiting."

    thought "This is — actually, completely — it."

    ## -----------------------------------------------------------------------
    ## SCENE 2.5 — MEETING LIZ
    ## Amelia's corridor. Twenty minutes later. A knock.
    ## -----------------------------------------------------------------------

    "She's been sitting on the bed for seventeen minutes, staring at the wall and trying to determine whether the paint colour is 'eggshell' or 'institutional despair,' when—"

    # play sound "audio/sfx_knock.ogg"
    "Three rapid knocks. A muffled voice:"

    liz "Hiya! Are you — oh, hang on, which one's yours — yeah! Are you the new person in fourteen?"

    "Before Amelia can answer, the door opens — she hadn't locked it — and a head appears. Short curly hair. Green eyes. A grin so wide it could be a weather system."

    liz "Oh brilliant, you're here! I'm Liz, I'm in fifteen, I heard you arrive through the wall — these walls are like paper, honestly, you'll hear everything, sorry about that in advance — are you okay? You look a bit..."

    a "Shell-shocked?"

    liz "I was going to say 'new,' but yeah, that too."

    "She comes in without waiting to be invited, which Amelia would normally find stressful but somehow doesn't, because Liz moves through the world like a Labrador — enthusiastic, harmless, slightly too much."

    liz "I'm Marine Biology. Cardiff. My name's Elizabeth officially but literally no one calls me that except my nan and she's in Swansea, so. Liz. Where are you from? What are you doing? Have you seen the kitchen yet? It's grim."

    "She takes a breath."

    liz "Also — and this is important — I have a dog at home called Marvin and if you want to see photos you only have to ask. Or not ask. I'll show you anyway."

    ## CHOICE 2.3 — Responding to Liz's energy
    menu:
        "Amelia looks at this whirlwind of a person who has invaded her grief-nest."

        "\"Tell me everything about Marvin immediately.\"":
            $ ch2_liz_response = "warm"
            $ add_stat("stat_si", 1)
            $ add_rel("rel_liz", 1)

            a "Tell me everything about Marvin immediately."

            "Liz's face lights up like Christmas."

            liz "Oh my GOD. Right. So. He's a cockapoo — that's a cockerspaniel-poodle mix, not a rude word, I've had to explain this to three people already — and he's got this one ear that sticks up and one that flops down and he SITS on the sofa like a person, like actually sits, back against the cushion—"

            "She pulls out her phone. The camera roll is approximately 80%% Marvin."

            a "He does sit like a person."

            liz "I KNOW! My mum says he's got more emotional intelligence than my brother, which is honestly fair. Right, come on, let me show you the kitchen. I'm warning you: the oven is suspicious."

            "And just like that, the silence in Room 14 is gone. Replaced by Liz, who is exactly the opposite of silence."

        "\"It's nice to meet you too, Liz.\"":
            $ ch2_liz_response = "reserved"
            $ add_stat("stat_mh", 1)

            a "It's nice to meet you too, Liz."

            "She says it with a smile that's genuine but careful. Guarding energy she might need later."

            liz "Oh — yeah! Course. Sorry, I'm a lot, I know. My mum says I'm like a fire alarm that's also a person."

            a "That's... quite an image."

            liz "It's accurate, to be fair."

            "She rocks on her heels."

            liz "Well — if you want tea or anything, I'm right next door. I brought my own kettle. A rebel, I know."

            "She leaves with a wave. The room is quiet again, but it's a different kind of quiet — the kind that has someone in the next room, making tea, being alive."

    ## -----------------------------------------------------------------------
    ## SCENE 2.6 — THE KITCHEN
    ## Communal kitchen, evening. The first gathering.
    ## -----------------------------------------------------------------------

    scene bg_halls_kitchen_evening
    with dissolve

    # play music "audio/ch2_kitchen.ogg" fadein 2.0 volume 0.5

    "Seven o'clock. The communal kitchen has the aesthetic of a place designed by someone who has never enjoyed a meal. Beige counters. Strip lighting. A microwave that looks like it has witnessed crimes."

    "But it's warm, and it smells of something good, and people are here."

    "A boy sits at the table with headphones around his neck, eating cereal from a bowl, reading a book. He's dressed simply — dark hoodie, neat hair. He looks up when Amelia enters, gives a nod that contains approximately the minimum viable amount of social interaction, and goes back to his cereal."

    "That's Lucas."

    "At the hob, a broader figure is stirring a pot with the confidence of someone who has been trusted with food his entire life. The steam carries cumin and garlic and something sweeter — cardamom?"

    raj "Hey! New person. You hungry? There's always enough."

    "He says it like a fact about the universe. There is always enough. He will make sure."

    "That's Raj."

    "And in the corner — on the windowsill, bare feet tucked under her, a cup of tea held in both hands like a small warm animal — a girl with short, unevenly cut blonde hair and eyes that seem to be looking at something very far away."

    "She looks up when Amelia enters. Their eyes meet."

    "She almost smiles. Then she looks away."

    "That's Sarah."

    ## CHOICE 2.4 — Who does Amelia approach first?
    menu:
        "Three people. Three doorways. Amelia stands at the kitchen threshold with a mug she brought from home and a heart that's beating slightly too fast."

        "Raj — the food smells incredible and he's already talking to her.":
            $ ch2_kitchen_approach = "raj"
            $ add_stat("stat_si", 1)
            $ add_rel("rel_raj", 1)

            "She goes to Raj. It's the easiest choice — he's already invited her, and the food smells like someone's home."

            a "What are you making?"

            raj "Dhal. My nan's recipe. Well, my nan's recipe adjusted for the fact that this kitchen has two working burners and a hob that's got a vendetta against me."

            "He ladles some into a bowl and hands it to her."

            raj "I'm Raj. Manchester."

            a "Amelia. Bromley."

            raj "London girl. Nice. Psychology?"

            a "How did you—"

            raj "Everyone on this floor is Psychology or Marine Biology. We are the emotional support floor."

            "They eat standing at the counter. The dhal is spectacular."

            a "This is amazing."

            raj "Tell my dad that. He thinks I should be running a shop instead of making dhal in a student kitchen."

            "He says it lightly. But there's a weight under it that she files away for later."

        "Lucas — she's curious about what he's reading.":
            $ ch2_kitchen_approach = "lucas"
            $ add_stat("stat_sd", 1)
            $ add_rel("rel_lucas", 1)

            "She goes to the table. Sits across from the boy with the cereal and the book."

            a "Hi."

            "He looks up. Studies her for exactly the right amount of time — long enough to show he's listening, short enough to not be weird."

            lucas "Hi."

            "Pause."

            lucas "Lucas."

            a "Amelia."

            "Another pause. He doesn't fill it. She realises she doesn't have to either."

            a "What are you reading?"

            "He turns the book so she can see the cover. {i}The Archetypes and the Collective Unconscious{/i}. Jung."

            a "Is that for the course?"

            lucas "No."

            "Beat."

            lucas "It's for me."

            "Something about the way he says it — without apology or explanation — makes Amelia like him immediately."

            if ch1_reading == "jung":
                a "I've been reading Jung too. {i}Man and His Symbols{/i}. Someone wrote notes in the margins."

                lucas "...Notes in the margins?"

                a "Yeah. In pencil. Things like 'pay attention to the Shadow.'"

                "He looks at her. Really looks at her. Something shifts behind his eyes."

                lucas "That's — yeah. We should talk about that."

                "He almost smiles."

        "Sarah — something about her draws Amelia across the room.":
            $ ch2_kitchen_approach = "sarah"
            $ add_stat("stat_mh", 1)
            $ add_rel("rel_sarah", 1)

            "She goes to the window. She doesn't entirely know why."

            "The girl looks up. Blue eyes. The kind that remind you of water in winter — clear but cold."

            a "Hi. I'm Amelia."

            "A pause. Just long enough that Amelia wonders if she's made a mistake."

            sarah "Sarah."

            "She says her name like it's something she's not sure she's allowed to have."

            a "Are you psychology too?"

            sarah "Yeah."

            "Sarah takes a sip of her tea. Then, as if deciding something:"

            sarah "It's a weird night, isn't it? Like — all these strangers in a kitchen pretending we know how to be adults."

            a "I've been pretending for about six hours. I'm getting quite good at it."

            "Sarah almost-smiles. It's brief and beautiful, like a bird landing on a branch and immediately leaving."

            sarah "I think I've been pretending for longer than that."

            "They sit in silence for a moment. Outside the window, the car park lights flicker on. Beyond them: darkness, and somewhere in it, the sea."

    "The kitchen fills slowly. More people. A girl from Marine Biology. A boy from Sports Science who got the wrong floor. Liz arrives and immediately starts telling Raj about Marvin."

    "It's not home. But it's warm, and there's food, and for a moment — just a moment — the loneliness lifts."

    ## -----------------------------------------------------------------------
    ## SCENE 2.7 — FRESHERS' WEEK (Montage)
    ## A rapid sequence. Registration, tours, overwhelm.
    ## -----------------------------------------------------------------------

    scene bg_campus_daytime
    with dissolve

    "The next five days hit like a wave."

    "Registration: a queue that snakes around the building. A photocard that makes her look like a guilty person. A lanyard that says PSYCHOLOGY with more enthusiasm than she feels."

    scene bg_campus_tour
    with dissolve

    "Campus tour: a third-year student walking backwards at speed, pointing at buildings like an auctioneer. \"That's the gym, that's the library, that's the SU — you'll spend most of your money there — and that's the medical centre, which you won't need unless it's freshers' flu season, which is always.\""

    scene bg_psych_building
    with dissolve

    "The psychology department: a building that smells of new carpet and old books. Posters on the walls — Freud, Milgram, that one Pavlov joke that's in every psychology department on Earth."

    "Societies fair: too many leaflets, too many people in branded hoodies, a capella groups singing at her while she tries to escape."

    thought "This is a lot. This is — genuinely — a lot."

    "She texts Ella:"

    "{i}it's so much ella. there are so many people. someone in a mascot costume tried to hug me{/i}"

    "Ella replies in four seconds:"

    "{i}DID YOU HUG THE MASCOT{/i}"

    "{i}i did not hug the mascot{/i}"

    "{i}COWARD{/i}"

    ## -----------------------------------------------------------------------
    ## SCENE 2.8 — THE SU NIGHT OUT
    ## Student Union. First night out. Neon. Chaos.
    ## -----------------------------------------------------------------------

    scene bg_su_night
    with dissolve

    # play music "audio/ch2_su_night.ogg" fadein 1.5 volume 0.7

    "Thursday night. The SU."

    "From outside it looks like a regular building having a seizure — coloured lights strobing through the windows, bass vibrating the pavement, a queue of freshers in too little clothing for October."

    "Inside: sticky floors. Cheap drinks. A DJ playing music that's simultaneously too loud and wrong. Neon wristbands. Someone has already been sick in the toilets and it's only nine o'clock."

    "Liz has dragged Amelia here. Liz is already dancing. Liz was born dancing."

    liz "COME ON!"

    "Amelia stands at the edge of the dance floor with a vodka cranberry that cost two pounds and tastes like cough medicine and regret."

    ## CHOICE 2.5 — How does Amelia navigate the night?
    menu:
        "The music pounds. People she doesn't know shout over it."

        "Throw herself in — dances, meets people, stays till close.":
            $ ch2_su_night = "party"
            $ add_stat("stat_si", 1)

            "She drinks the cough medicine. She goes to the dance floor. She dances."

            "She doesn't dance well — she never has, she knows this, she dances like someone who's read about dancing in a book — but she dances. And after a while, it doesn't matter."

            "She meets people. A girl from History who's already lost her shoes. A boy from Engineering who can only communicate by shouting. Someone's name that she'll forget by morning but who right now, in this moment, is the funniest person alive."

            "Liz is delighted."

            liz "SEE! I TOLD YOU! THIS IS WHAT UNI IS!"

            "It's not what uni is. But it's one thing uni is, and tonight, that's enough."

            "She stays until the lights come on at 2am and the magic breaks and everyone spills onto the pavement, shivering, euphoric, slightly deaf."

            thought "I did that. I actually did that."

        "Find a quiet corner and people-watch.":
            $ ch2_su_night = "observe"
            $ add_stat("stat_sd", 1)

            "She finds a spot near the wall, behind a pillar, where the music is loud but the crowd thins out."

            "And she watches."

            "The girl by the bar who keeps checking her phone. The two boys trying to impress each other with dance moves that are genuinely terrible. The couple in the corner who've known each other approximately thirty-five minutes and are already acting like nobody else exists."

            thought "Everybody in this room is performing a version of themselves. The confident ones, the loud ones, the ones trying to look like they don't care. We're all doing it."

            "It's like watching a Milgram experiment in real time. Social pressure, conformity, the desperate human need to belong. She finds it fascinating."

            "Liz appears, sweaty and glowing."

            liz "You okay? You've been standing here for ages."

            a "I'm fine. Honestly. I'm enjoying this."

            liz "From... over here? By the pillar?"

            a "Best seat in the house."

            "Liz doesn't get it, but she respects it. She brings Amelia another drink and returns to the dance floor."

        "Leave early and call Ella from outside.":
            $ ch2_su_night = "ella"
            $ add_stat("stat_mh", 1)
            $ add_rel("rel_ella", 1)

            "It's too much. The noise, the people, the sticky floor, the smell of someone's perfume mixing with someone else's sweat."

            "She slips out. The night air hits her like a mercy."

            "She finds a bench outside the SU, away from the smokers, and calls Ella."

            "Ella picks up on the second ring."

            ella "Oi. Aren't you supposed to be out? It's freshers'. You're meant to be making bad decisions."

            a "I was inside for about forty minutes and I think my soul left my body."

            ella "That bad?"

            a "Ella. The floor was so sticky. I could feel it through my shoes. Through my actual shoes."

            ella "Okay, gross, but also — that's the experience? Like, sticky floors are basically a rite of passage?"

            a "I'm not ready for this rite of passage. I want the rite of passage where I sit quietly and read."

            ella "Babe. That's a library. You already know how to do that."

            "They talk for an hour. About nothing. About everything. About the mascot she didn't hug and the dhal Raj made and the girl in the next room who has a dog called Marvin."

            "By the end, the panic has dissolved. Not gone — dissolved. A solid becoming a liquid."

            ella "Go back to your room. Make tea. You survived your first night out by not having a night out. That's very you and I support it fully."

    ## -----------------------------------------------------------------------
    ## SCENE 2.9 — THE PSYCHOLOGY WELCOME LECTURE
    ## Psych building, lecture theatre. Monday morning.
    ## -----------------------------------------------------------------------

    scene bg_lecture_theatre
    with dissolve

    # play music "audio/ch2_lecture.ogg" fadein 2.0 volume 0.4

    "Monday. Nine a.m. Lecture Theatre 1."

    "The room is tiered — seats rising in rows, too many of them, each with a tiny folding desk that's designed to hold either a laptop or a notebook but not a human's actual arm."

    "Two hundred first-year psychology students, hung over and anxious, clutching coffee and good intentions."

    "At the front: a man in his sixties. Tall, slightly stooped, grey hair that was once dark. He wears a tweed jacket without irony and looks at the assembled students the way a surgeon looks at a complicated case."

    "He lets the silence grow."

    "And grow."

    "Someone coughs. Someone else whispers. A phone vibrates."

    "Then:"

    hawthorne "Psychology."

    "He lets the word sit there."

    hawthorne "The study of behaviour and mind. The logos of the psyche. You have enrolled in a programme dedicated to understanding why human beings do what they do, feel what they feel, and believe what they believe."

    "His voice is quiet. The room gets quieter to match."

    hawthorne "It is also — if you are paying attention — the study of everything you are afraid to look at in yourself."

    "Total silence."

    hawthorne "I don't say that to alarm you. I say it because it is the truth, and I would be doing you a disservice to begin with anything less. Psychology is not an abstract subject. It is not a subject that allows you to keep a comfortable distance from your material. Your material is you."

    "He picks up a piece of chalk. Writes on the board, in large letters: KNOW THYSELF."

    hawthorne "Inscribed above the entrance to the Temple of Apollo at Delphi. The oldest directive in Western philosophy. And, I would argue, the hardest."

    "He looks at the room."

    hawthorne "My name is Professor Hawthorne. I will be teaching your Foundations of Psychology module. I set the exams. I mark the essays. I maintain office hours. I drink Earl Grey and I do not accept late submissions."

    "A ripple of nervous laughter."

    hawthorne "You may find this programme difficult. You may find it rewarding. If you are very lucky, and if you do the work, you may find it both. Any questions?"

    "No one raises a hand."

    hawthorne "Good. Then we begin."

    ## CHOICE 2.6 — Amelia's reaction to Hawthorne
    menu:
        "Amelia sits in the fourth row, pen in hand, heart in throat."

        "{i}Intimidating. But I want to impress him.{/i}":
            $ ch2_hawthorne_reaction = "impress"
            $ add_stat("stat_aa", 1)

            thought "He's terrifying. In the best way."

            "She writes the date at the top of her notebook. Underlines it twice."

            thought "I'm going to work so hard he has no choice but to notice. I'm going to read every text on the list — both the compulsory and the recommended. I'm going to ask questions in seminars. I'm going to get a first."

            "Hawthorne begins the lecture. She writes down every word."

        "{i}He's right. That's exactly why I'm here.{/i}":
            $ ch2_hawthorne_reaction = "purposeful"
            $ add_stat("stat_sd", 1)

            thought "That's exactly why I'm here."

            "Not for the degree. Not for the career. Not for the proud look on her dad's face when she graduates."

            thought "I'm here because I don't know myself. I don't know why I think the things I think. I don't know why I feel the things I feel. I'm here because there's a whole world inside me that I've never explored."

            "She writes 'KNOW THYSELF' in her notebook and draws a box around it."

            thought "Let's find out."

        "{i}\"Everything you're afraid to look at.\" That's either brilliant or terrifying.{/i}":
            $ ch2_hawthorne_reaction = "ominous"
            $ add_stat("stat_ok", 1)

            thought "Everything you're afraid to look at in yourself."

            "The words land somewhere below her ribs. Not her mind — her body recognises them before her brain catches up."

            thought "There's something I'm afraid to look at. I don't know what it is yet. But when he said it, something... flinched."

            "She writes the words down. Below them, almost without thinking, she writes: {i}What am I not seeing?{/i}"

            if ch1_bookshop == "paracelsus":
                thought "The Paracelsus book said something similar. 'He who knows himself knows all things.' The alchemists and the psychologists are asking the same question."

    ## -----------------------------------------------------------------------
    ## CONDITIONAL SCENE 2.C — THE FLAT PARTY (MAYA AND TAROT)
    ## Triggers if SI >= 3 OR Liz relationship >= 1
    ## -----------------------------------------------------------------------

    if stat_si >= 3 or rel_liz >= 1:

        scene bg_flat_party
        with dissolve

        # play music "audio/ch2_party.ogg" fadein 2.0 volume 0.5

        "Friday night. Liz appears at Amelia's door with the energy of someone who has already decided the outcome of the conversation."

        liz "We're going to a party."

        a "We are?"

        liz "Third-floor flat. Someone called Jake? I don't know him but Raj says it's good and Raj has never been wrong about a social gathering."

        "The party is in a flat that looks identical to theirs but with more fairy lights and significantly more people. Music Amelia doesn't recognise. A boy doing something awful to a guitar in the corner."

        "She drifts through. Liz is absorbed immediately — talking to a marine biology student about octopus cognition with the intensity of a diplomatic summit."

        "And then Amelia walks into the kitchen."

        "A woman is sitting at the kitchen table with a deck of cards spread before her. Not playing cards — tarot cards. She's in her early twenties, long curly black hair in a messy braid, an embroidered jacket, and the kind of calm that makes the chaos of the party seem very far away."

        "Three people are watching her. She turns a card. Looks at it. Looks at the person across from her."

        maya "The Lovers. Which doesn't mean what you think it means. It's about choice, not romance."

        "The person across from her looks relieved."

        maya "Or it's about romance. Cards are ambiguous like that. Very on-brand for the universe."

        "She looks up. Her eyes find Amelia."

        maya "Want to know your fortune?"

        a "I... sure?"

        "The woman — Maya, she learns later, Maya Patel, Philosophy with Psychology, second year — shuffles the deck with hands that know what they're doing."

        maya "Cut the deck. Left hand. Don't think about it."

        "Amelia cuts the deck."

        "Maya turns the top card."

        "The card shows a tower being struck by lightning. Flames. Figures falling."

        maya "The Tower."

        "Maya looks at it for a long moment. Then looks at Amelia with an expression that's half-amused, half-something else."

        maya "Don't worry. It's actually a good card."

        a "That doesn't look like a good card."

        maya "It means destruction. But it means {i}necessary{/i} destruction. Burning away what isn't real so what is real can emerge."

        "She taps the card."

        maya "Everything that isn't you is about to fall away. Eventually, you'll be grateful."

        a "Eventually?"

        maya "Eventually."

        "She smiles. It's warm and slightly unsettling."

        maya "I'm Maya, by the way. Come find me if you want to talk about it. I'm always in the philosophy corridor. Or meditating. Or making extremely weird tea."

        $ add_rel("rel_maya", 1)
        $ add_stat("stat_ok", 1)

    ## -----------------------------------------------------------------------
    ## SCENE 2.10 — END OF CHAPTER
    ## Amelia's room, late. Alone. The first Sunday night.
    ## -----------------------------------------------------------------------

    scene bg_amelia_room_plymouth_night
    with dissolve

    "Sunday night. The first full week is done."

    "Amelia sits at her desk with a cup of tea that's gone cold. Outside, the car park. Beyond it, the faint sound of the city, and beyond that, if she listens closely — or imagines she listens closely — the sea."

    "Her phone is open to the group chat Liz started. Messages from Raj about leftovers. A photo from Liz of a seagull that stole someone's pasty. A single message from Lucas: 'anyone want the library tomorrow.'"

    "Nothing from Sarah."

    "She picks up the phone. Types a text to Ella:"

    "{i}first week done. still alive. miss you x{/i}"

    "Ella replies immediately:"

    "{i}course you're alive. you're you. tell me everything tomorrow ok? i want every detail. every SINGLE detail{/i}"

    "{i}even the sticky floor story?{/i}"

    "{i}ESPECIALLY the sticky floor story{/i}"

    "Amelia puts the phone down. Pulls the curtain aside."

    "She came here not knowing anyone. Not knowing where the lecture theatre was, or how to work the oven, or which way the sea was."

    "She knows now."

    thought "I'm here. I'm actually here. And tomorrow — another week. Another chance to figure this out."

    "She doesn't know yet what she's figuring out. She doesn't know about the moors or the standing stones or the pellar in Penzance or the Tower card that Maya turned over in a stranger's kitchen."

    "She doesn't know about any of it."

    "But something has started. Under the surface. Like a tide turning in the dark."

    $ complete_chapter(2)
    scene black
    with fade

    centered "{size=+6}End of Chapter Two{/size}"
    pause 2.0

    return
