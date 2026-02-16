###############################################################################
##
##  CHAPTER 10: THE ROAD BACK
##
##  Hero's Journey: The hero returns to the ordinary world, but changed.
##  Alchemical Stage: Early Rubedo — the reddening; integration begins.
##  Month: April (Easter break). Location: London.
##  Palette: City greys + new green. Cherry blossom. Familiar but strange.
##  Music: Piano. Something by Debussy. London sounds underneath.
##
##  Scenes: 7 | Choices: 5
##  Max earnable: ~7 pts
##
###############################################################################

label chapter_10:

    stop music fadeout 1.0
    scene black
    with fade

    centered "{size=+20}Chapter Ten{/size}\n\n{size=+6}The Road Back{/size}"
    pause 3.0

    ## =====================================================================
    ## SCENE 10.1 — LONDON AGAIN
    ## The familiar made strange.
    ## =====================================================================

    scene bg_london_train
    with dissolve

    # play music "audio/ch10_homecoming.ogg" fadein 3.0 volume 0.4

    "The train from Plymouth to Paddington takes three hours and fourteen minutes."

    "Amelia watches the landscape change — Cornwall's granite and gorse giving way to Devon's red earth, then Somerset's green, then the gradual grey thickening of the approach to London."

    # --- SONG SLIDESHOW: "The Long Way Home" — Train to London, the reverse journey ---
    call slideshow_ch10_the_long_way_home

    "At Reading, the buildings multiply. At Slough, the sky gets smaller. At Paddington, the station swallows her — noise, movement, pigeons, the smell of brake dust and Costa Coffee."

    "London."

    "It's the same. Of course it is. The Tube is the same. The escalators are the same. The specific compressed human warmth of a rush-hour District Line carriage is the same."

    "But she sees it differently."

    thought "I used to be part of this. This flow. This automatic life. I got on the escalator and stood on the right and held my Oyster card and I didn't think about any of it."

    "She walks from the station. Her bag is heavy. The streets are familiar in the way that a childhood bedroom is familiar — smaller than you remember."

    ## =====================================================================
    ## SCENE 10.2 — HOME
    ## =====================================================================

    scene bg_amelia_home
    with dissolve

    "The front door."

    "Amelia puts her key in the lock and the smell hits her first — home. Specifically: her mother's cooking (ginger, garlic), the particular wood polish they use on the stairs, and underneath it, something she can't name. Just {i}home{/i}."

    grace "Amelia!"

    "Grace appears from the kitchen. The hug is immediate, enveloping, slightly too tight."

    grace "Let me look at you. Oh, you've lost weight. Have you been eating properly?"

    a "Mum, I've been eating fine."

    grace "You look tired."

    a "I'm a student. We're all tired."

    "Grace holds her at arm's length. Studies her. Mothers see everything."

    grace "Something happened."

    "It's not a question."

    a "A lot of things happened. I'll tell you about them."

    grace "At dinner. Your father's making bolognese."

    david "I'm not making bolognese, I'm making a ragù. There's a difference."

    "David appears. The hug is shorter, tighter, more contained."

    david "Good to have you back."

    a "Good to be back."

    "Lily's room is closed. Music — something with bass — leaks under the door."

    a "How's Lily?"

    "Grace's face does something complicated."

    grace "She's... sixteen."

    ## =====================================================================
    ## SCENE 10.3 — ELLA
    ## The real test.
    ## =====================================================================

    scene bg_london_cafe
    with dissolve

    "The café in Bloomsbury. Their café — they've been coming here since sixth form. The same window seat. The same oat milk flat whites. The same barista who always gets Ella's name wrong."

    "Ella is already there."

    "She stands up. She's wearing a new jacket — leather, vintage, something Amelia doesn't recognise. Her hair is different. Shorter."

    ella "Oh my God."

    "The hug is long."

    ella "You look different."

    a "You look different."

    ella "Good different?"

    a "Always good different."

    "They sit. The coffee arrives. The barista calls Ella 'Emily.' Same as always."

    "And then—"

    "The gap."

    "They've been texting. Calling. But the thing about distance is that it fills with all the experiences the other person wasn't there for, and when you sit across from each other the gap is suddenly visible."

    ella "So. Tell me everything."

    ## =====================================================================
    ## CHOICE 10.1 — ELLA REUNION
    ## =====================================================================

    menu:
        "Seven months. A lifetime. How much does Amelia share?"

        "Everything. Complete honesty about how she's changed.":
            $ ch10_ella = "honest"
            $ add_stat("stat_mh", 1)
            $ add_stat("stat_si", 1)
            $ add_rel("rel_ella", 2)

            "She tells her."

            "Not all of it — not in order, not neatly. But the real things. The mentor. The friends. Cornwall."

            "Sarah."

            a "My friend tried to kill herself. And I—"

            "She stops. Ella's hand is on hers across the table."

            ella "You don't have to—"

            a "I want to. I need to tell someone who knew me before."

            "She tells Ella about the hospital. The waiting room. The fluorescent lights. The specific violence of a 3am phone ringing."

            "Ella doesn't interrupt. She doesn't say 'oh my God' or 'how awful.' She just listens."

            ella "And you? How are {i}you{/i}?"

            a "I'm — I don't know. I'm different. I'm not the Amelia who came to this café in September with her perfect timetable and her colour-coded notes. That person is gone."

            ella "That's okay. I'm not the same Ella either."

            a "No?"

            ella "I've started painting again. Properly. Not for anyone — for me. I'm thinking about applying to art school."

            a "Ella."

            ella "I know. It's terrifying."

            "They look at each other. The real versions of themselves. Messier, harder, more beautiful."

            a "I'm proud of you."

            ella "I'm proud of {i}you{/i}."

        "Warm but guarded — don't want to burden her.":
            $ ch10_ella = "warm"
            $ add_stat("stat_si", 1)
            $ add_rel("rel_ella", 1)

            "She tells Ella about the good things. The essays. The Hoe at dawn. Cornwall's light. The friends — Raj's cooking, Lucas's quiet presence, Liz's laugh."

            "She mentions Sarah. But carefully."

            a "A friend had a really difficult time. She's getting help now."

            ella "Are {i}you{/i} okay?"

            a "I'm getting there."

            "Ella looks at her. Ella always could read her."

            ella "You're not telling me everything."

            a "Not today. But I will."

            ella "Promise?"

            a "Promise."

            "The promise sits between them. Real."

        "Perform the old friendship — inside jokes, safe topics.":
            $ ch10_ella = "perform"
            $ add_rel("rel_ella", -1)

            "She does the Amelia-and-Ella greatest hits."

            "The barista joke. The story about the sixth-form geography trip. The mutual hatred of a specific type of podcast."

            "Ella laughs. They both laugh. It's easy and warm and completely hollow."

            "Underneath the performance, the distance grows."

            ella "Amelia."

            a "Yeah?"

            ella "You're doing the thing."

            a "What thing?"

            ella "The thing where you smile and say the right things and none of it's real."

            "Silence."

            ella "I've known you since we were fourteen. You can't fake it with me."

            "But Amelia can. That's the terrible thing. She can."

            a "I'm fine, Els. Really."

            "Ella lets it go. But something in her eyes closes."

    ## =====================================================================
    ## SCENE 10.4 — PARENTS HEART-TO-HEART
    ## =====================================================================

    scene bg_amelia_home
    with dissolve

    "Dinner."

    "David's ragù is — it's always been the same ragù. Slow-cooked. Wine. Bay leaves. The kitchen smells like every Sunday of Amelia's childhood."

    "Lily appears. She's taller. Or Amelia is shorter. The headphones are off for once."

    lily "Hey."

    a "Hey yourself. You grew."

    lily "That's what happens."

    "The four of them eat. Grace asks questions — modules, grades, living situation. David asks about the city, the coastline, whether Plymouth's got decent public transport."

    "Normal things."

    "Then Grace puts down her fork."

    grace "Amelia. We've been worried."

    "David doesn't say anything, but his hand stops cutting."

    grace "Your calls have been shorter. And sometimes you sound — I don't know. Far away."

    ## =====================================================================
    ## CHOICE 10.2 — PARENTS HEART-TO-HEART
    ## =====================================================================

    menu:
        "Grace and David are looking at their daughter. Waiting."

        "\"I'm not the same person who left.\" Be vulnerable.":
            $ ch10_parents = "vulnerable"
            $ add_stat("stat_mh", 1)

            a "You're right. I've been far away."

            "She doesn't tell them everything. She doesn't tell them about the hospital or the 3am phone calls."

            "But she tells them about the hardness of it. The loneliness at the start. The way she missed home with a physical ache. The friend who struggled. The mentor who helped her see things differently."

            a "I'm not the same person who got on that train in September. I don't know if that's good or bad. But I'm different."

            "Grace is crying. Quietly. She's always cried quietly."

            "David puts down his knife and fork."

            david "That sounds about right."

            a "Dad?"

            david "Different is what university's for. We didn't send you to Plymouth to stay the same. We sent you to find out who you are."

            "A pause."

            david "Have you? Found out?"

            a "I'm working on it."

            david "Good enough."

            "Grace wipes her eyes and reaches across the table for Amelia's hand."

            grace "We're proud of you. Whatever you found out."

        "Share the good parts, protect them from the hard parts.":
            $ ch10_parents = "protective"
            $ add_stat("stat_si", 1)

            a "It's been intense. But good? I think good."

            "She tells them about the essays, the marks, the improvement. She tells them about Cornwall. She tells them about Raj's cooking and the sunrise from the Hoe."

            "She makes it sound like an adventure. Which it was. But she edits the dark parts — the hospital, the corridor, the 3am."

            grace "And your friends? You talk about them a lot."

            a "They're the best. Truly."

            "Grace looks satisfied. David nods."

            "She's protected them. That's what children do, eventually — they start protecting their parents from the truth. It's a kind of love. It's also a kind of distance."

        "Dodge the conversation — \"Let's just enjoy dinner.\"":
            $ ch10_parents = "dodge"

            a "Can we just — not do the deep conversation tonight? I just got home. I want to eat Dad's ragù and not think for a bit."

            grace "Of course. Yes. Of course."

            "But Grace's hand shakes slightly as she picks up her fork. And David changes the subject too quickly — cricket, the garden, the neighbour's extension."

            "The dinner is pleasant and careful and Amelia hates every minute of it because she chose this and she didn't have to."

    ## =====================================================================
    ## SCENE 10.5 — LILY
    ## =====================================================================

    scene bg_lily_room
    with dissolve

    "Late evening. Amelia knocks on Lily's door."

    lily "What?"

    a "Can I come in?"

    "A pause. The music stops."

    lily "Fine."

    "Lily's room. It's changed. The walls are covered now — not with boy band posters but with art prints, photographs cut from magazines, a sketch that Amelia recognises as Lily's own hand."

    "She's always drawn. But this is different. This is serious."

    a "These are good."

    lily "They're okay."

    a "Lily, they're really good."

    "Lily shrugs. But her shoulders unknot slightly."

    a "How's school?"

    lily "Fine."

    a "How's {i}really{/i}?"

    "Lily looks at her. The calculation of a sixteen-year-old deciding whether an older sister can be trusted."

    lily "Since you left — it's been weird."

    a "Weird how?"

    lily "Mum's anxious all the time. She checks on me, like, constantly. And Dad's just... Dad. He retreats into his shed and fixes things."

    a "I'm sorry."

    lily "It's not your fault. It's just — it was better when you were here. The balance was better. You held them together."

    thought "Oh."

    lily "And school is — I don't know. Everyone's so {i}loud{/i}. And fake. They're all performing being happy and I'm just..."

    a "Not?"

    lily "Not unhappy. Just... tired of pretending."

    ## =====================================================================
    ## CHOICE 10.3 — LILY
    ## =====================================================================

    menu:
        "Lily is sixteen and trying to be honest. This is new."

        "Listen fully. Offer what you've learned.":
            $ ch10_lily = "listen"
            $ add_stat("stat_mc", 1)
            $ add_stat("stat_si", 1)
            $ add_rel("rel_lily", 2)

            "She sits on Lily's bed."

            a "Can I tell you something?"

            lily "If it's advice about studying harder—"

            a "It's not."

            "She looks at her sister."

            a "The first month at Plymouth, I thought I'd made a terrible mistake. I sat in my room and cried and didn't tell anyone. And then I started telling people. And it didn't fix anything, but it made the unfixed things bearable."

            lily "That's not the same—"

            a "I know. But the principle is the same. You don't have to pretend. Not with me. Not with Mum and Dad. Not with your friends — the real ones."

            "Lily is quiet."

            a "And your art is brilliant. Really. Have you thought about doing something with it?"

            lily "Mum wants me to do STEM."

            a "Mum wants you to be happy. She just doesn't know that art and happy can be the same thing."

            "Lily's eyes are bright."

            lily "You're different."

            a "I know."

            lily "Good different."

            a "I hope so."

            "Lily, for the first time in perhaps three years, leans her head on Amelia's shoulder."

        "Listen, but feel unqualified — \"I don't know what to say, Lil.\"":
            $ ch10_lily = "uncertain"
            $ add_stat("stat_mh", 1)
            $ add_rel("rel_lily", 1)

            a "I don't know what to say."

            lily "That's refreshing. Everyone else pretends to know."

            a "I mean — I've had a big year. I've learned some things. But I don't think I'm qualified to tell a sixteen-year-old how to be happy."

            lily "Good. Because the last three people who tried sounded like a TED Talk."

            "She laughs despite herself."

            a "Look. I don't have answers. But I have ears. And a sister who's clearly brilliant and underappreciated."

            lily "You're just saying that."

            a "I'm not. I wish someone had told me at sixteen that it's okay to not be okay. So I'm telling you."

            "Lily nods. Slowly."

            lily "Thanks."

            a "Anytime. I mean it."

        "Too caught up to notice what Lily actually needs.":
            $ ch10_lily = "miss"
            $ add_rel("rel_lily", -1)

            a "School's hard for everyone at your age. It gets better."

            "The generic response. The one adults give when they're not really listening."

            lily "Right. Sure."

            "The conversation dies. Lily puts her headphones back on."

            "Amelia leaves. She's thinking about Plymouth, about Sarah, about the essay due after Easter."

            "She doesn't notice the way Lily's shoulders curl inward when the door closes."

    ## =====================================================================
    ## SCENE 10.6 — SOLO CONTEMPLATION
    ## Revisiting old places with new eyes.
    ## =====================================================================

    scene bg_london_park
    with dissolve

    "Tuesday. Amelia goes out alone."

    "London in April. Cherry blossom in every park, drifting like pink snow. The sky is blue — proper blue, not the grey she's used to."

    "She walks."

    # --- SONG SLIDESHOW: "Here, Now, and Blues" — Solo London contemplation ---
    call slideshow_ch10_here_now_and_blues

    ## =====================================================================
    ## CHOICE 10.4 — SOLO CONTEMPLATION
    ## =====================================================================

    menu:
        "Where does she go?"

        "The bookshop — check the Esoterica shelf." if stat_ok >= 3:
            $ ch10_solo = "bookshop"
            $ add_stat("stat_ok", 1)

            scene bg_bookshop
            with dissolve

            "The bookshop in Cecil Court. The dusty window. The bell. Mr. Hargreaves behind the counter."

            "She goes straight to the Esoterica shelf."

            "The Paracelsus is gone — she bought it in September. But in its place, something new."

            "{i}The Chemical Wedding of Christian Rosenkreutz.{/i} 1616. Not the original, obviously — a translation, battered, annotated in pencil by some previous reader."

            "She opens it."

            "And there, tucked between the pages, another note. Handwritten. The same handwriting as before."

            "{i}\"The stone is not found in foreign lands. It is with you.{/i}\n{i}Look where you have already looked. See what you have already seen.{/i}\n{i}The work is almost done.\"{/i}"

            thought "Elena?"

            "She buys the book. £4.50. She reads it on the Tube home and something in her chest hums."

        "The Thames — sit where she sat before university.":
            $ ch10_solo = "thames"
            $ add_stat("stat_sd", 1)

            scene bg_thames
            with dissolve

            "The South Bank. The same bench. September's bench."

            "She sat here the night before leaving. She was terrified and excited and she wrote in her notebook about the river and the unknown."

            "She sits again."

            "The river is the same. Brown, wide, patient. The boats pass. The seagulls shout."

            "But the woman sitting on the bench is not the same woman who sat here eight months ago."

            thought "I sat here and I was afraid of everything. I was afraid of not being good enough, not being interesting, not being brave."

            thought "I'm still afraid. But now I know what bravery actually looks like. It looks like knocking on a door at 3am. It looks like saying 'I'm struggling' to a mentor at 2am. It looks like sitting in a circle of friends and crying."

            "The river. The same river."

            "No. Not the same. You can't step in the same river twice."

        "The park — where it all started.":
            $ ch10_solo = "park"
            $ add_stat("stat_sd", 1)

            scene bg_london_park
            with dissolve

            "The park."

            "She comes here without thinking about it — her feet know the way. Through the gate, along the path, past the duck pond."

            "The bench. Their bench — hers and Ella's, from all those summers of sitting and talking and not knowing what lay ahead."

            "She sits."

            "The ducks are the same ducks. Or their descendants. The pond is the same pond. The trees are taller or she is smaller."

            "A woman walks past with a toddler. A man reads a newspaper. Students — sixth-formers, probably — sit on the grass and laugh at something on a phone."

            thought "I was them. Six months ago, I was them."

            "She takes out her notebook and writes. Not about the past. About now. About the specific quality of April light through a plane tree and the way a park bench can hold so many versions of yourself."

    ## =====================================================================
    ## SCENE 10.7 — THE LAST EVENING
    ## What to take back.
    ## =====================================================================

    scene bg_amelia_home
    with dissolve

    "The last evening."

    "Her bag is packed. The train is at 10:15 tomorrow."

    "Grace has cooked too much food — always too much food, as if love can be measured in portions. David has retreated to his shed but left a card on her bed: {i}'Proud of you. Love, Dad.'{/i}"

    "Lily gave her a drawing. A small one, pencil, of a wren. She didn't explain it. She just said: 'For your wall.'"

    thought "She doesn't know about Sarah's tattoo. But she drew a wren anyway."

    ## =====================================================================
    ## CHOICE 10.5 — WHAT TO TAKE BACK
    ## =====================================================================

    menu:
        "Tomorrow she goes back to Plymouth. What does she take with her?"

        "Something from home — a piece of comfort.":
            $ ch10_takeaway = "home"

            "Grace's scarf. The green one, cashmere, that smells of her perfume."

            grace "Take it. I know it's almost summer but — take it."

            a "Mum—"

            grace "Please."

            "She takes it."

            "On the train, she wraps it around her neck even though it's April and warm, and she breathes in home, and she lets herself miss them for a few miles before the landscape opens up and she's going forward again."

        "Something new — a piece of growth.":
            $ ch10_takeaway = "new"

            "A sketchbook. Lily's recommendation."

            lily "You don't have to draw. You can write in it. Or paste things. Or just... have it."

            "Amelia buys one from the art shop in Covent Garden. Hardcover, unlined, cream pages. The kind of book that says: {i}this is for something you haven't thought of yet.{/i}"

            "On the train she opens it and draws — badly, wonderfully — the view from the window. Fields. Cows. A church spire."

        "Nothing extra — she has what she needs.":
            $ ch10_takeaway = "nothing"

            "She takes herself. And the drawing from Lily, and the card from David, and the memory of Grace's too-tight hug."

            "That's enough."

            "On the train, she reads. The book doesn't matter. What matters is the act — the quiet, forward motion. The landscape outside. The knowledge that home is still there, and so is she."

    ## =====================================================================
    ## SCENE 10.8 — THE TRAIN BACK
    ## =====================================================================

    scene bg_london_train
    with dissolve

    "Paddington. The station swallows everyone and spits them onto trains. Amelia finds her seat."

    "The train moves. London falls away — the density thinning, the sky widening."

    "At Reading, she texts Raj:"

    "{i}amelia: on my way back. eta 1:30. any daal left?{/i}"

    "{i}raj: always.{/i}"

    "She puts her phone down. Watches England scroll past."

    thought "I went home. And home was smaller. Or I was bigger."

    thought "Both, maybe."

    "Somerset. Devon. Then — there — the first glimpse of the coast. The Atlantic, flat and silver under the spring sun."

    thought "I'm going back. Not because I have to. Because I choose to."

    "The train crosses into Cornwall. The light changes — brighter, sharper, cleaner."

    thought "One more term. Then exams. Then summer. Then whatever comes next."

    thought "I don't know what comes next."

    thought "But I'm not afraid of not knowing anymore."

    ## -----------------------------------------------------------------------
    ## END OF CHAPTER
    ## -----------------------------------------------------------------------

    scene black
    with fade

    centered "{size=+6}End of Chapter Ten{/size}"
    pause 2.0

    return
