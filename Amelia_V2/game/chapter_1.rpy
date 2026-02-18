###############################################################################
##
##  CHAPTER 1: THE ORDINARY WORLD
##
##  Hero's Journey: The hero in their familiar world before the adventure.
##  Alchemical Stage: Calcination (Nigredo) — the prima materia is heated.
##  Month: Late September. Location: London.
##  Palette: Warm darks, burnt umber, deep amber, gold accents.
##  Music: Acoustic, intimate, nostalgic. Think: early evening, end of summer.
##
##  Scenes: 7 | Choices: 6 | Max earnable: ~8 pts
##
###############################################################################

label chapter_1:

    $ current_chapter = 1
    stop music fadeout 1.0
    scene black
    with fade

    ## -----------------------------------------------------------------------
    ## TITLE CARD
    ## -----------------------------------------------------------------------

    voice "audio/centered/chapter_1/line_001.ogg"
    centered "{size=+20}Chapter One{/size}\n\n{size=+6}The Ordinary World{/size}"
    pause 3.0

    ## -----------------------------------------------------------------------
    ## SCENE 1.1 — THE PARK BENCH
    ## Late September. A park in Bromley. The last gold of summer.
    ## -----------------------------------------------------------------------

    # play music "audio/ch1_park.ogg" fadein 2.0 volume 0.6
    scene bg_park_bench_sunset
    with dissolve

    voice "audio/narrator/chapter_1/line_001_L38.ogg"
    "Late September. The kind of afternoon where the light turns everything to amber and you know — without anyone saying it — that summer is ending."

    voice "audio/narrator/chapter_1/line_002_L40.ogg"
    "A park bench in Bromley. Nothing special. The same one she's sat on since she was eleven, back when she used to bring library books here and read until her mum texted her to come home for dinner."

    voice "audio/narrator/chapter_1/line_003_L42.ogg"
    "She's doing the same thing now, more or less. Except the library books have been replaced by a university reading list, and the dinner texts have a new urgency to them."

    voice "audio/narrator/chapter_1/line_004.ogg"
    thought "Two days. Two days until I leave."

    voice "audio/narrator/chapter_1/line_004_L46.ogg"
    "Amelia pushes her hair behind her ear — a tic she'll never quite shake — and looks down at the book in her lap."

    voice "audio/narrator/chapter_1/line_006.ogg"
    thought "Right. Focus. If I'm going to show up to a psychology degree pretending I know things, I should probably actually know things."

    voice "audio/narrator/chapter_1/line_005_L50.ogg"
    "She turns a page. Reads the same paragraph for the third time. Absorbs nothing."

    voice "audio/narrator/chapter_1/line_006_L52.ogg"
    "The trees in the park are just beginning to turn. Green-gold, like old coins."

    ## CHOICE 1.1 — What is Amelia reading?
    menu:
        "What catches her attention in the book?"

        "The chapter on cognitive biases — {i}Thinking, Fast and Slow{/i} by Kahneman":
            $ ch1_reading = "kahneman"
            $ add_stat("stat_aa", 1)

            voice "audio/narrator/chapter_1/line_010.ogg"
            thought "System 1 and System 2. Fast thinking and slow thinking. I like this — the idea that half our brain is running on autopilot while the other half pretends it's steering."

            voice "audio/narrator/chapter_1/line_011.ogg"
            "She underlines a sentence about anchoring bias. Then underlines the one above it too, because she can't decide which is more important."

            voice "audio/narrator/chapter_1/line_012.ogg"
            thought "I want to understand how minds work. Not just in theory — properly. Why people believe wrong things. Why I believe wrong things."

            voice "audio/narrator/chapter_1/line_013.ogg"
            "A dog barks somewhere across the park. A child laughs. Amelia reads on."

        "The illustrations in {i}Man and His Symbols{/i} by Jung":
            $ ch1_reading = "jung"
            $ add_stat("stat_sd", 1)

            voice "audio/narrator/chapter_1/line_014.ogg"
            "It's not even on the reading list. She found it in a charity shop last week — the spine cracked, someone else's pencil notes in the margins."

            voice "audio/narrator/chapter_1/line_015.ogg"
            thought "Jung says the unconscious speaks in symbols. In dreams. That everything we push down comes back wearing a costume."

            voice "audio/narrator/chapter_1/line_016.ogg"
            "She traces her thumb across a mandala illustration. Concentric circles. Something about it feels... right. Like recognising a face you've never seen."

            voice "audio/narrator/chapter_1/line_017.ogg"
            thought "I want to understand what dreams mean. What it means when you wake up at 3am with a feeling you can't name."

            voice "audio/narrator/chapter_1/line_018.ogg"
            "She turns the page. Someone has written in the margin: {i}Pay attention to the Shadow.{/i} She wonders who they were."

        "A passage about bardos in {i}The Tibetan Book of Living and Dying{/i}":
            $ ch1_reading = "tibetan"
            $ add_stat("stat_ok", 1)

            voice "audio/narrator/chapter_1/line_019.ogg"
            "She's not sure why she bought this. It was in the 'Spirituality' section of the bookshop and the cover looked serious — not crystals-and-angels serious, but actually serious."

            voice "audio/narrator/chapter_1/line_020.ogg"
            thought "Bardos. Transitional states. The Tibetans say life itself is a bardo — a space between what was and what comes next."

            voice "audio/narrator/chapter_1/line_021.ogg"
            "The paragraph she keeps returning to describes the moment of recognition: the instant when you realise the ground you've been standing on is dissolving, and what you do in that instant defines everything that follows."

            voice "audio/narrator/chapter_1/line_022.ogg"
            thought "I picked this up and I couldn't put it down. I don't know what that means yet."

            voice "audio/narrator/chapter_1/line_023.ogg"
            "A cloud passes over the sun. The amber light dims to grey for a moment, then returns."

    voice "audio/narrator/chapter_1/line_007_L98.ogg"
    "She closes the book and checks her phone. Three missed texts from Ella, each more emphatic than the last."

    ## -----------------------------------------------------------------------
    ## SCENE 1.2 — ELLA'S CALL
    ## Still the park bench. Late afternoon light.
    ## -----------------------------------------------------------------------

    # play sound "audio/sfx_phone_ring.ogg"
    voice "audio/narrator/chapter_1/line_008_L106.ogg"
    "Her phone buzzes before she even finishes reading the texts. Ella's face fills the screen — the photo is from Year 11, both of them with terrible haircuts, grinning like idiots."

    voice "audio/narrator/chapter_1/line_009_L108.ogg"
    "She picks up."

    voice "audio/ella/chapter_1/line_026.ogg"
    ella "Finally! Did you die? You literally haven't replied in four hours. Four hours, Amelia, that's a new personal record of neglect."

    voice "audio/amelia/chapter_1/line_027.ogg"
    a "I was reading."

    voice "audio/ella/chapter_1/line_028.ogg"
    ella "You've been reading since May. At some point you're going to have to accept that you've already read enough to fake it at university."

    voice "audio/narrator/chapter_1/line_010_L116.ogg"
    "Amelia smiles. This is how Ella talks — in lists and accusations and love disguised as complaints."

    voice "audio/ella/chapter_1/line_030.ogg"
    ella "Anyway. Two days."

    voice "audio/amelia/chapter_1/line_031.ogg"
    a "Two days."

    voice "audio/ella/chapter_1/line_032.ogg"
    ella "That's... mental, isn't it? Like, actually properly mental."

    voice "audio/narrator/chapter_1/line_011_L124.ogg"
    "A pause. Just long enough that Amelia hears what Ella isn't saying."

    voice "audio/ella/chapter_1/line_034.ogg"
    ella "You're going to be so far away."

    voice "audio/narrator/chapter_1/line_012_L128.ogg"
    "She says it lightly. But Ella's voice has that thing it does when she's trying not to care too much — it goes slightly higher, slightly faster, like she can outrun the feeling if she just keeps talking."

    voice "audio/ella/chapter_1/line_036.ogg"
    ella "I mean, not {i}far{/i} far. It's Plymouth, not Mars. But still. I won't be able to just... come round, will I? When something's shit. I can't just get on the bus."

    ## CHOICE 1.2 — Responding to Ella's unspoken worry
    menu:
        "Amelia wants to say the right thing. She's not sure what the right thing is."

        "\"We'll FaceTime every day. I promise.\"":
            $ ch1_ella_response = "promise"
            $ add_stat("stat_si", 1)
            $ add_rel("rel_ella", 1)

            voice "audio/amelia/chapter_1/line_038.ogg"
            a "Ella. We'll FaceTime every day. I promise. You'll be so sick of my face that by Christmas you'll be begging me to stay in Plymouth."

            voice "audio/ella/chapter_1/line_039.ogg"
            ella "Every day?"

            voice "audio/amelia/chapter_1/line_040.ogg"
            a "Every single day. And I'll send you photos of the sea."

            voice "audio/ella/chapter_1/line_041.ogg"
            ella "You'd better. And none of that artsy-angled shit. I want basic, tourist-level sea photos. Gulls and everything."

            voice "audio/narrator/chapter_1/line_042.ogg"
            "They both laugh, and the tight thing in Ella's voice loosens."

            voice "audio/ella/chapter_1/line_043.ogg"
            ella "Okay. Every day. I'm holding you to that."

        "\"It's going to be weird, isn't it? Not seeing each other all the time.\"":
            $ ch1_ella_response = "honest"
            $ add_stat("stat_mh", 1)
            $ add_rel("rel_ella", 1)

            voice "audio/amelia/chapter_1/line_044.ogg"
            a "Yeah. It's going to be weird, isn't it? Not seeing each other all the time."

            voice "audio/narrator/chapter_1/line_045.ogg"
            "Silence. But not a bad silence."

            voice "audio/ella/chapter_1/line_046.ogg"
            ella "Yeah. It is."

            voice "audio/amelia/chapter_1/line_047.ogg"
            a "Like... I know we'll be fine. I know that. But it's still going to be weird."

            voice "audio/ella/chapter_1/line_048.ogg"
            ella "It's been you and me since we were, what, twelve? That's more than half our lives, Amelia. That's longer than some marriages."

            voice "audio/amelia/chapter_1/line_049.ogg"
            a "We'd have been a very boring married couple."

            voice "audio/ella/chapter_1/line_050.ogg"
            ella "Speak for yourself. I'd have been thrilling."

            voice "audio/narrator/chapter_1/line_051.ogg"
            "They laugh, and it's the kind of laugh that lives right next door to crying."

            voice "audio/ella/chapter_1/line_052.ogg"
            ella "...We will be fine though, won't we?"

            voice "audio/amelia/chapter_1/line_053.ogg"
            a "Yeah. We will."

    voice "audio/ella/chapter_1/line_054.ogg"
    ella "Right. Good. Now go pack. And eat something — I know you haven't eaten because you've been {i}reading{/i} and you always forget to eat when you're reading."

    voice "audio/amelia/chapter_1/line_055.ogg"
    a "I ate."

    voice "audio/ella/chapter_1/line_056.ogg"
    ella "Liar."

    voice "audio/amelia/chapter_1/line_057.ogg"
    a "I ate a biscuit."

    voice "audio/ella/chapter_1/line_058.ogg"
    ella "Amelia."

    voice "audio/amelia/chapter_1/line_059.ogg"
    a "A whole biscuit, Ella. Not even a half."

    voice "audio/ella/chapter_1/line_060.ogg"
    ella "I can't believe I'm losing my best friend to the sea and a biscuit."

    voice "audio/narrator/chapter_1/line_013_L192.ogg"
    "They say goodbye the way they always do — no goodbye at all, just the conversation trailing off into 'okay' and 'okay' and 'I'll text you later' and the line going quiet."

    voice "audio/narrator/chapter_1/line_014_L194.ogg"
    "Amelia sits on the bench for another minute. The light is changing. Long shadows now."

    voice "audio/narrator/chapter_1/line_063.ogg"
    thought "Two days."

    ## -----------------------------------------------------------------------
    ## SCENE 1.3 — DINNER WITH THE FAMILY
    ## The James household, evening. Kitchen table.
    ## -----------------------------------------------------------------------

    scene bg_james_kitchen_evening
    with dissolve

    # play music "audio/ch1_home.ogg" fadein 2.0 volume 0.5

    voice "audio/narrator/chapter_1/line_015_L208.ogg"
    "The kitchen smells of ackee and saltfish and garlic and the particular warmth of a house where someone has been cooking for hours with love and mild anxiety."

    voice "audio/narrator/chapter_1/line_016_L210.ogg"
    "Grace has cooked Amelia's favourite. She does this when she's worried — feeds you until the fear goes away, or at least until you're too full to argue."

    voice "audio/mrs_james/chapter_1/line_065.ogg"
    grace "Sit down, sit down. Lily, put that phone away."

    voice "audio/lily/chapter_1/line_066.ogg"
    lily "I'm literally texting one person."

    voice "audio/mrs_james/chapter_1/line_067.ogg"
    grace "You can text them after dinner. In this house we eat with our eyes on each other, not on screens."

    voice "audio/narrator/chapter_1/line_017_L218.ogg"
    "Lily rolls her eyes but puts the phone face-down on the table. She's sixteen and everything is an injustice."

    voice "audio/narrator/chapter_1/line_018_L220.ogg"
    "David comes in from washing his hands. He's been working on the van again — there's engine grease in the creases of his knuckles that never quite washes out. He sits down and immediately starts serving ackee onto Amelia's plate."

    voice "audio/amelia/chapter_1/line_070.ogg"
    a "Dad, I can—"

    voice "audio/mr_james/chapter_1/line_071.ogg"
    david "Eat. You'll be living on pot noodles in a week. Let me have this."

    voice "audio/narrator/chapter_1/line_019_L226.ogg"
    "He says it like a joke. It's not entirely a joke."

    voice "audio/narrator/chapter_1/line_020_L228.ogg"
    "They eat. Grace asks about packing. Amelia says it's fine. Lily asks if she can have Amelia's room. Grace says no. Lily asks why. Grace says because."

    voice "audio/narrator/chapter_1/line_021_L230.ogg"
    "Then the conversation shifts. David puts his fork down."

    voice "audio/mr_james/chapter_1/line_075.ogg"
    david "So. Plymouth."

    voice "audio/amelia/chapter_1/line_076.ogg"
    a "Plymouth."

    voice "audio/mr_james/chapter_1/line_077.ogg"
    david "What are you... hoping for? From it."

    voice "audio/narrator/chapter_1/line_022_L238.ogg"
    "Grace looks at Amelia. Lily looks at her phone under the table. David looks at his hands."

    ## CHOICE 1.3 — What Amelia expects from university
    menu:
        "It's the kind of question that sounds simple and isn't."

        "\"I want to be the first person in our family with a degree.\"":
            $ ch1_dinner_speech = "degree"
            $ add_stat("stat_aa", 1)
            $ add_stat("stat_mc", 1)

            voice "audio/amelia/chapter_1/line_080.ogg"
            a "I want to be the first person in our family with a degree."

            voice "audio/narrator/chapter_1/line_081.ogg"
            "The table goes quiet. Grace's eyes shine."

            voice "audio/mr_james/chapter_1/line_082.ogg"
            david "You know that's not why we—"

            voice "audio/amelia/chapter_1/line_083.ogg"
            a "I know. I know it's not why you're sending me. But it matters to me. It matters that I do this properly. For all of us."

            voice "audio/narrator/chapter_1/line_084.ogg"
            "David nods. Slowly. His jaw works like he's chewing on words he can't quite form."

            voice "audio/mr_james/chapter_1/line_085.ogg"
            david "Your granddad worked the docks for forty years. Your mum grew up in a house with six kids and one bathroom. We didn't have—"

            voice "audio/mrs_james/chapter_1/line_086.ogg"
            grace "David."

            voice "audio/mr_james/chapter_1/line_087.ogg"
            david "I'm just saying. We're proud of you. Whatever happens."

            voice "audio/narrator/chapter_1/line_088.ogg"
            "He picks his fork back up. Subject closed. But his eyes are bright, and he keeps glancing at her like he's memorising her face."

        "\"I just want to figure out who I am, honestly.\"":
            $ ch1_dinner_speech = "self"
            $ add_stat("stat_sd", 1)
            $ add_stat("stat_mh", 1)

            voice "audio/amelia/chapter_1/line_089.ogg"
            a "I just want to figure out who I am, honestly."

            voice "audio/narrator/chapter_1/line_090.ogg"
            "A beat."

            voice "audio/mrs_james/chapter_1/line_091.ogg"
            grace "You're Amelia James. You're our daughter. You're brilliant."

            voice "audio/amelia/chapter_1/line_092.ogg"
            a "No, I mean — I know who I am {i}here{/i}. In this kitchen, in Bromley. I know who I am when I'm with you, or with Ella. But I don't know who I am on my own. I've never had to find out."

            voice "audio/narrator/chapter_1/line_093.ogg"
            "Lily looks up from her phone. For once, she's listening."

            voice "audio/mr_james/chapter_1/line_094.ogg"
            david "That's... actually quite a mature thing to say."

            voice "audio/lily/chapter_1/line_095.ogg"
            lily "Don't sound so shocked, Dad."

            voice "audio/narrator/chapter_1/line_096.ogg"
            "They laugh. Grace reaches across the table and squeezes Amelia's hand."

            voice "audio/mrs_james/chapter_1/line_097.ogg"
            grace "You'll find out. And whoever you find — bring her home for Christmas, yeah?"

        "\"I've been reading about some really interesting stuff — psychology, philosophy, older traditions...\"":
            $ ch1_dinner_speech = "esoteric"
            $ add_stat("stat_ok", 1)
            $ add_stat("stat_sd", 1)

            voice "audio/amelia/chapter_1/line_098.ogg"
            a "I've been reading about some really interesting stuff. Not just the psychology textbooks — philosophy, history of ideas... some older traditions too. Things I'd never even heard of before."

            voice "audio/mrs_james/chapter_1/line_099.ogg"
            grace "Like what kind of older traditions?"

            voice "audio/amelia/chapter_1/line_100.ogg"
            a "Well, like... did you know that alchemy wasn't just about turning lead into gold? It was a whole system for understanding transformation — how the self changes. Jung wrote about it. The psychologists and the alchemists were basically studying the same thing but from different centuries."

            voice "audio/narrator/chapter_1/line_101.ogg"
            "David blinks."

            voice "audio/mr_james/chapter_1/line_102.ogg"
            david "Right."

            voice "audio/lily/chapter_1/line_103.ogg"
            lily "Nerd."

            voice "audio/mrs_james/chapter_1/line_104.ogg"
            grace "Lily."

            voice "audio/lily/chapter_1/line_105.ogg"
            lily "I didn't say it was bad! I said she's a nerd. Nerds are doing well. That's a compliment."

            voice "audio/amelia/chapter_1/line_106.ogg"
            a "Thanks, Lily. I'll treasure that."

            "Grace watches Amelia with something between pride and worry — the look parents give when they realise their child is becoming someone they can't entirely predict."

    voice "audio/narrator/chapter_1/line_023_L315.ogg"
    "They finish dinner. Grace insists on seconds. David washes up even though it's Lily's turn. Lily takes advantage of the distraction to reclaim her phone."

    voice "audio/narrator/chapter_1/line_024_L317.ogg"
    "Amelia stands at the kitchen door for a moment, watching them. The yellow bulb over the sink. Her dad's shoulders. Her mum's humming."

    voice "audio/narrator/chapter_1/line_109.ogg"
    thought "I am going to miss this so much."

    ## -----------------------------------------------------------------------
    ## SCENE 1.4 — PACKING
    ## Amelia's bedroom, night. Boxes half-packed.
    ## -----------------------------------------------------------------------

    scene bg_amelia_bedroom_night
    with dissolve

    voice "audio/narrator/chapter_1/line_025_L329.ogg"
    "Her room is in that strange half-state between lived-in and left. Posters still on the walls — Florence and the Machine, a film print of {i}Spirited Away{/i}, a dog-eared map of London she's been annotating since Year 9. Her books are in boxes. The shelves look like missing teeth."

    voice "audio/narrator/chapter_1/line_026_L331.ogg"
    "She sits on the bed. Around her: clothes folded by Grace (too neatly), toiletries from Boots (too many), and the specific panic of trying to compress eighteen years of a life into a car boot."

    voice "audio/narrator/chapter_1/line_112.ogg"
    thought "Okay. Clothes, check. Books, check. Laptop, check. The fairy lights from above the bed—"

    voice "audio/narrator/chapter_1/line_027_L335.ogg"
    "She pauses. She's forgotten to pack the fairy lights. She unpins them from the wall and the room immediately looks less like hers."

    voice "audio/narrator/chapter_1/line_114.ogg"
    thought "Right. One more thing. There's space for one more thing."

    voice "audio/narrator/chapter_1/line_028_L339.ogg"
    "She looks around the room."

    ## CHOICE 1.4 — One last item
    menu:
        "She can only fit one more thing. What does she take?"

        "Her psychology flashcards — she's been making them all summer.":
            $ ch1_packing = "flashcards"
            $ add_stat("stat_aa", 1)

            "She picks up the stack of flashcards from her desk. Handwritten, colour-coded, held together with an elastic band that's seen better days."

            voice "audio/narrator/chapter_1/line_117.ogg"
            thought "Piaget. Erikson. Milgram. Pavlov. The entire foundation of my degree in two hundred little rectangles."

            "She flicks through them. The handwriting gets messier as the stack goes on — she'd started in June with perfect lettering and by August she was scrawling in bed at midnight."

            voice "audio/narrator/chapter_1/line_118.ogg"
            thought "I'm as ready as I'll ever be. Which is to say: not ready at all, but with flashcards."

            "She slides them into the front pocket of her bag. Within reach."

        "The photo of her and Ella from Year 11 prom.":
            $ ch1_packing = "photo"
            $ add_stat("stat_si", 1)
            $ add_rel("rel_ella", 1)

            voice "audio/narrator/chapter_1/line_119.ogg"
            "She picks up the photo from her bedside table. It's in a frame Ella painted herself — uneven, too much glitter, slightly wonky. Perfect."

            voice "audio/narrator/chapter_1/line_120.ogg"
            "In the picture, they're seventeen. Ella's dress is too big. Amelia's eyeliner is crooked. They're laughing at something off-camera — she can't remember what, but she remembers the laughing."

            voice "audio/narrator/chapter_1/line_121.ogg"
            thought "She painted this frame. Made me promise to keep it 'somewhere I'd see it every day.' It's been on my bedside table for two years."

            voice "audio/narrator/chapter_1/line_122.ogg"
            "She wraps it in a jumper and tucks it into the box. She'll put it on whatever bedside table comes next."

        "A journal — blank, for whatever comes next.":
            $ ch1_packing = "journal"
            $ add_stat("stat_sd", 1)

            voice "audio/narrator/chapter_1/line_123.ogg"
            "She picks up the journal from the shelf. She bought it three weeks ago from the stationery shop on the high street — leather cover, unlined pages, the word {i}Begin{/i} embossed on the front in small gold letters."

            voice "audio/narrator/chapter_1/line_124.ogg"
            "It's completely empty."

            voice "audio/narrator/chapter_1/line_125.ogg"
            thought "I don't know what this is for yet. Notes? Thoughts? A diary? I just... I wanted something blank. Something that doesn't have an answer key."

            voice "audio/narrator/chapter_1/line_126.ogg"
            "She runs her thumb along the spine. The leather is soft. It smells new."

            voice "audio/narrator/chapter_1/line_127.ogg"
            thought "For whatever comes next."

            voice "audio/narrator/chapter_1/line_128.ogg"
            "She puts it in her bag, next to her phone charger and her headphones. The essentials."

    voice "audio/narrator/chapter_1/line_029_L388.ogg"
    "She zips the last box. Stands up. Looks at the room."

    voice "audio/narrator/chapter_1/line_030_L390.ogg"
    "The Blu-Tack marks on the wall where the posters were. The dent in the carpet where her desk chair has been sitting for six years. The view from the window: the street, the neighbour's cat on the fence, the streetlight that flickers in winter."

    voice "audio/narrator/chapter_1/line_131.ogg"
    thought "This room will still be here. But it won't be mine anymore. Not really. Lily will probably have it by Easter."

    voice "audio/narrator/chapter_1/line_031_L394.ogg"
    "She turns off the light."

    ## -----------------------------------------------------------------------
    ## SCENE 1.5 — THE BOOKSHOP
    ## Next day. Bromley high street. Mr. Osei's bookshop.
    ## -----------------------------------------------------------------------

    scene bg_bookshop_interior
    with dissolve

    # play music "audio/ch1_bookshop.ogg" fadein 2.0 volume 0.5

    voice "audio/narrator/chapter_1/line_032_L406.ogg"
    "The bell above the door makes a sound that hasn't changed in ten years. The carpet is worn thin in a path from the entrance to the till. The shelves lean slightly — not dangerously, just eccentrically, like the whole building is eavesdropping."

    voice "audio/narrator/chapter_1/line_033_L408.ogg"
    "Mr. Osei is behind the counter, peering at a book through the bottom of his bifocals. He looks up when she enters and his face does something complicated and warm."

    voice "audio/mr_osei/chapter_1/line_135.ogg"
    mr_osei "Amelia James. My best customer."

    voice "audio/amelia/chapter_1/line_136.ogg"
    a "Mr. Osei, I'm probably your {i}only{/i} customer."

    voice "audio/mr_osei/chapter_1/line_137.ogg"
    mr_osei "Then best and only. That's even more impressive."

    voice "audio/narrator/chapter_1/line_034_L416.ogg"
    "He comes out from behind the counter. He moves slowly — he's been running this shop since before Amelia was born, and the books have aged better than his knees."

    voice "audio/mr_osei/chapter_1/line_139.ogg"
    mr_osei "Tomorrow, then?"

    voice "audio/amelia/chapter_1/line_140.ogg"
    a "Tomorrow."

    voice "audio/mr_osei/chapter_1/line_141.ogg"
    mr_osei "Plymouth. Psychology."

    voice "audio/amelia/chapter_1/line_142.ogg"
    a "That's the one."

    voice "audio/mr_osei/chapter_1/line_143.ogg"
    mr_osei "Good city. Good university. The sea will do you good. London children don't see enough sky."

    voice "audio/narrator/chapter_1/line_035_L428.ogg"
    "He looks at her the way he always does — like he's filing her away in some private index of people who actually read."

    voice "audio/mr_osei/chapter_1/line_145.ogg"
    mr_osei "You'll want a book, then. A leaving gift."

    voice "audio/amelia/chapter_1/line_146.ogg"
    a "Mr. Osei, you don't have to—"

    voice "audio/mr_osei/chapter_1/line_147.ogg"
    mr_osei "I'm not giving it to you. I'm selling it. At a modest discount. Consider it an investment in your education."

    voice "audio/narrator/chapter_1/line_036_L436.ogg"
    "He gestures at the shop."

    voice "audio/mr_osei/chapter_1/line_149.ogg"
    mr_osei "Browse."

    voice "audio/narrator/chapter_1/line_037_L440.ogg"
    "She does. The shop smells of old paper and wood polish and the faint ghost of pipe tobacco that Mr. Osei swears he gave up years ago."

    voice "audio/narrator/chapter_1/line_038_L442.ogg"
    "She wanders between the shelves. Self-help (she avoids). Fiction (she considers). History. Science. Philosophy."

    voice "audio/narrator/chapter_1/line_039_L444.ogg"
    "And in the back — the shelf she's always been a little curious about. Hand-painted label: {b}ESOTERICA{/b}."

    ## CHOICE 1.5 — Which book?
    menu:
        "She stops. Three books catch her eye."

        "A modern psychology anthology — the smart, safe choice.":
            $ ch1_bookshop = "psychology"
            $ add_stat("stat_aa", 1)

            "She picks up {i}The New Psychology: An Anthology{/i}. Recent, well-reviewed, with chapters by researchers she's read about online. It's practical. It's relevant. It will look good on her shelf when other students visit."

            voice "audio/mr_osei/chapter_1/line_153.ogg"
            mr_osei "Ah. Sensible."

            voice "audio/amelia/chapter_1/line_154.ogg"
            a "Is that a compliment or a criticism?"

            voice "audio/mr_osei/chapter_1/line_155.ogg"
            mr_osei "From me? Always both."

            "He wraps it in brown paper — he still wraps books in brown paper, even though nobody asked — and takes her money with a nod."

            voice "audio/mr_osei/chapter_1/line_156.ogg"
            mr_osei "Study hard. But not too hard. Leave room for the things you don't expect."

        "{i}Letters to a Young Poet{/i} by Rilke — the spine is cracked from love.":
            $ ch1_bookshop = "rilke"
            $ add_stat("stat_mh", 1)

            voice "audio/narrator/chapter_1/line_157.ogg"
            "It's barely a book — more like a pamphlet. {i}Letters to a Young Poet{/i} by Rainer Maria Rilke. The cover is soft from handling, and when she opens it, a sentence catches her before she's ready:"

            voice "audio/narrator/chapter_1/line_158.ogg"
            "{i}\"You must change your life.\"{/i}"

            voice "audio/narrator/chapter_1/line_159.ogg"
            thought "That's... not comforting, Rilke. But maybe comfort isn't the point."

            voice "audio/narrator/chapter_1/line_160.ogg"
            "She turns to the first letter. Written in 1903 to a young man who didn't know if he was a poet. Rilke's answer: if you can't not write, you're a poet. If you can survive the solitude, you'll survive everything."

            voice "audio/narrator/chapter_1/line_161.ogg"
            thought "If you can survive the solitude."

            voice "audio/mr_osei/chapter_1/line_162.ogg"
            mr_osei "Good choice. That one will find you when you need it."

            voice "audio/narrator/chapter_1/line_163.ogg"
            "He wraps it carefully, as though it were made of glass."

        "An old volume in the Esoterica section — {i}The Aurora of the Philosophers{/i} by Paracelsus.":
            $ ch1_bookshop = "paracelsus"
            $ add_stat("stat_ok", 1)
            $ elena_key_paracelsus = True

            voice "audio/narrator/chapter_1/line_164.ogg"
            "She doesn't know why she goes to the back shelf. Call it curiosity. Call it the fact that the book's spine is the only one in the section that isn't dusty — as if someone has been pulling it out and putting it back."

            voice "audio/narrator/chapter_1/line_165.ogg"
            "The cover is brown leather, worn smooth at the edges. Gold lettering, half-faded: {i}The Aurora of the Philosophers — Paracelsus.{/i}"

            voice "audio/narrator/chapter_1/line_166.ogg"
            "She opens it. The pages are thick, old, cream-coloured. And inside the front cover, tucked between the endpaper and the binding, is a note."

            voice "audio/narrator/chapter_1/line_167.ogg"
            "Handwritten. Neat, old-fashioned cursive:"

            voice "audio/narrator/chapter_1/line_168.ogg"
            "{i}\"The stone is not a stone. The fire is not a fire. Seek the pellar where the land meets the sea.\"{/i}"

            voice "audio/narrator/chapter_1/line_169.ogg"
            thought "...What?"

            voice "audio/narrator/chapter_1/line_170.ogg"
            "She turns it over. Nothing on the back. No name, no date."

            voice "audio/narrator/chapter_1/line_171.ogg"
            "She looks at the first page. An illustration of a sunrise over a mountain — but the mountain is also an eye, and the sun is also a crown. The text beneath begins:"

            voice "audio/narrator/chapter_1/line_172.ogg"
            "{i}\"Nature is the physician of herself, and to know the processes of Nature is to know the key to all transformation.\"{/i}"

            voice "audio/narrator/chapter_1/line_173.ogg"
            thought "I don't understand half of this. But something about it feels like it's... waiting for me."

            voice "audio/mr_osei/chapter_1/line_174.ogg"
            mr_osei "Ah."

            "She looks up. Mr. Osei is watching her from the counter with an expression she can't quite read. Surprised? No. More like... confirmed."

            voice "audio/mr_osei/chapter_1/line_175.ogg"
            mr_osei "That one's been here a long time. I wondered who it was for."

            voice "audio/amelia/chapter_1/line_176.ogg"
            a "It's about alchemy?"

            voice "audio/mr_osei/chapter_1/line_177.ogg"
            mr_osei "It's about transformation. Same thing, depending on who you ask."

            "He wraps it without taking her money."

            voice "audio/mr_osei/chapter_1/line_178.ogg"
            mr_osei "That one's on the house. Consider it a farewell from the shop."

            voice "audio/amelia/chapter_1/line_179.ogg"
            a "Mr. Osei—"

            voice "audio/mr_osei/chapter_1/line_180.ogg"
            mr_osei "Take it, Amelia. Some books choose their readers."

            "She leaves the shop with the weight of it in her bag. The note is still tucked inside the cover."

            voice "audio/narrator/chapter_1/line_181.ogg"
            thought "{i}Seek the pellar where the land meets the sea.{/i} I don't even know what a pellar is."

    voice "audio/narrator/chapter_1/line_040_L531.ogg"
    "The bell rings again as she leaves. She pauses on the doorstep and looks back. Mr. Osei is already reading again, as though she was never there."

    voice "audio/narrator/chapter_1/line_041_L533.ogg"
    "She doesn't notice the symbol carved into the door frame at eye level — a serpent eating its own tail. It's been there as long as the shop has. Nobody notices it."

    ## -----------------------------------------------------------------------
    ## SCENE 1.6 — THE THAMES AT NIGHT
    ## London, evening. The South Bank. Last night before leaving.
    ## -----------------------------------------------------------------------

    scene bg_thames_night
    with dissolve

    # play music "audio/ch1_thames.ogg" fadein 3.0 volume 0.5

    voice "audio/narrator/chapter_1/line_042_L545.ogg"
    "She walks along the South Bank because she needs to walk and she needs to be near water and she doesn't know why."

    voice "audio/narrator/chapter_1/line_043_L547.ogg"
    "London at night. The Tate Modern glowing on the opposite bank. The Thames running black and gold — streetlight on dark water, the city reflected in broken lines."

    voice "audio/narrator/chapter_1/line_044_L549.ogg"
    "It's cold for September. She's wearing the corduroy jacket and it's not enough, but she doesn't care."

    voice "audio/narrator/chapter_1/line_045_L551.ogg"
    "There are runners. A couple arguing in Italian. A busker playing something on a guitar that she almost recognises. The air smells of rain and river and the particular exhaust-and-coffee scent of London after dark."

    voice "audio/narrator/chapter_1/line_046_L553.ogg"
    "She stops at the railing and leans against it. The metal is cold."

    voice "audio/narrator/chapter_1/line_047_L555.ogg"
    "Below her, the river moves. It always moves. It doesn't care about her leaving."

    ## CHOICE 1.6 — What she thinks about
    menu:
        "She stands there, and something rises in her."

        "\"I'm going to make everyone proud.\"":
            $ ch1_thames = "proud"
            $ add_stat("stat_aa", 1)
            $ add_stat("stat_mc", 1)

            voice "audio/narrator/chapter_1/line_189.ogg"
            thought "I'm going to make everyone proud."

            voice "audio/narrator/chapter_1/line_190.ogg"
            "The thought arrives like a resolution. Clear and bright and sharp-edged."

            voice "audio/narrator/chapter_1/line_191.ogg"
            thought "Mum and Dad. Ella. Mr. Osei. The teachers who wrote my references. The granddad who worked the docks. All of them."

            voice "audio/narrator/chapter_1/line_192.ogg"
            "She tightens her grip on the railing."

            voice "audio/narrator/chapter_1/line_193.ogg"
            thought "I'm going to get a first. I'm going to understand psychology — properly, deeply. I'm going to be the person they always said I could be."

            voice "audio/narrator/chapter_1/line_194.ogg"
            "The river doesn't respond. It just keeps moving."

            voice "audio/narrator/chapter_1/line_195.ogg"
            thought "And when I come back, I'll come back different. Better. Someone who earned it."

            voice "audio/narrator/chapter_1/line_196.ogg"
            "It's a good thought. A strong thought. The kind of thought that burns like a small, bright fire in the centre of her chest."

            voice "audio/narrator/chapter_1/line_197.ogg"
            "Whether it's enough to keep warm through winter — she'll find out."

        "\"I'm terrified and I don't know if I can do this.\"":
            $ ch1_thames = "terrified"
            $ add_stat("stat_mh", 1)

            voice "audio/narrator/chapter_1/line_198.ogg"
            thought "I'm terrified and I don't know if I can do this."

            voice "audio/narrator/chapter_1/line_199.ogg"
            "The thought arrives like a wave — the kind you don't see coming, the kind that takes your legs out."

            voice "audio/narrator/chapter_1/line_200.ogg"
            thought "What if I'm not smart enough? What if everyone else is smarter and they've already read everything and they know things I don't and they can tell — they can tell by looking at me that I don't belong—"

            voice "audio/narrator/chapter_1/line_201.ogg"
            "She grips the railing. Breathes."

            voice "audio/narrator/chapter_1/line_202.ogg"
            thought "Okay. Okay."

            voice "audio/narrator/chapter_1/line_203.ogg"
            "She breathes again. The river doesn't care. That's almost comforting."

            voice "audio/narrator/chapter_1/line_204.ogg"
            thought "It's okay to be scared. That's what Dr. Williams said in the sixth-form talk. 'Courage isn't the absence of fear. It's the decision that something else is more important.'"

            voice "audio/narrator/chapter_1/line_205.ogg"
            "She looks at the water. Black and gold. Moving."

            voice "audio/narrator/chapter_1/line_206.ogg"
            thought "I'm terrified. And I'm going anyway. And maybe that's enough."

            voice "audio/narrator/chapter_1/line_207.ogg"
            "It's not a triumphant feeling. It's a quiet one. But it holds."

        "She doesn't think. She watches the water.":
            $ ch1_thames = "watches"
            $ add_stat("stat_sd", 1)

            voice "audio/narrator/chapter_1/line_208.ogg"
            "She doesn't think."

            voice "audio/narrator/chapter_1/line_209.ogg"
            "She watches."

            voice "audio/narrator/chapter_1/line_210.ogg"
            "The water moves. Streetlight catches it in lines and lets it go. A boat passes, slow and lit, and the wake spreads in silver-black Vs that reach the edges of the river and dissolve."

            voice "audio/narrator/chapter_1/line_211.ogg"
            "She watches that too."

            voice "audio/narrator/chapter_1/line_212.ogg"
            "There's a word for this — she read it somewhere. {i}Sonder.{/i} The realisation that every person around you is living a life as vivid and complex as your own."

            voice "audio/narrator/chapter_1/line_213.ogg"
            "But this isn't sonder. This is the river version. The realisation that the water was here before you and will be here after and it doesn't care about your university place or your reading list or your carefully packed boxes."

            voice "audio/narrator/chapter_1/line_214.ogg"
            "It just moves."

            voice "audio/narrator/chapter_1/line_215.ogg"
            "And something in her — the anxious, planning, over-reading part — goes quiet for a moment. Just a moment."

            voice "audio/narrator/chapter_1/line_216.ogg"
            thought "..."

            voice "audio/narrator/chapter_1/line_217.ogg"
            "She stands there until the cold gets too much. Then she walks home."

    # --- SONG SLIDESHOW: "Paper Planes" — Amelia's last London night ---
    call slideshow_ch1_paper_planes

    ## -----------------------------------------------------------------------
    ## SCENE 1.7 — THE NIGHT BEFORE
    ## Amelia's bedroom, late. No choice. Pure narrative.
    ## -----------------------------------------------------------------------

    scene bg_amelia_bedroom_dark
    with dissolve

    voice "audio/narrator/chapter_1/line_048_L643.ogg"
    "Midnight."

    voice "audio/narrator/chapter_1/line_049_L645.ogg"
    "Her room is boxes and bare walls and the ghost-shapes of things that used to hang there."

    voice "audio/narrator/chapter_1/line_050_L647.ogg"
    "She's in bed. The duvet is the same one she's had since Year 9 — she couldn't bring herself to pack it. She'll take it tomorrow. Her last act of attachment."

    voice "audio/narrator/chapter_1/line_051_L649.ogg"
    "Downstairs, she can hear her parents. Not the words — just the rhythm. Her dad's low mumble. Her mum's laugh. The clink of mugs being washed."

    voice "audio/narrator/chapter_1/line_052_L651.ogg"
    "They've been talking for hours. About her, probably. About the house without her in it."

    thought "I am eighteen years old and I have never lived more than forty-five minutes from where I was born."

    voice "audio/narrator/chapter_1/line_053_L655.ogg"
    "She stares at the ceiling. The glow-in-the-dark stars are still up there — she stuck them to the ceiling when she was nine and nobody's taken them down. They barely glow anymore. Just a faint green suggestion."

    voice "audio/narrator/chapter_1/line_224.ogg"
    thought "Tomorrow I will sit in a car with my dad for four hours and at the end of it I will be in a city where I know nobody and I will carry a box into a room that doesn't know me and I will pretend this is normal."

    voice "audio/narrator/chapter_1/line_054_L659.ogg"
    "Her phone lights up on the pillow beside her."

    # Phone screen overlay
    voice "audio/narrator/chapter_1/line_055_L662.ogg"
    "A text from Ella:"

    voice "audio/narrator/chapter_1/line_227.ogg"
    "{i}you're going to be amazing. don't forget me x{/i}"

    voice "audio/narrator/chapter_1/line_056_L666.ogg"
    "She picks up the phone. Types a reply. Deletes it. Types another. Deletes that too."

    voice "audio/narrator/chapter_1/line_057_L668.ogg"
    "She puts the phone down."

    voice "audio/narrator/chapter_1/line_230.ogg"
    thought "I won't forget you. How could I forget you? You're the realest thing I know."

    voice "audio/narrator/chapter_1/line_058_L672.ogg"
    "She closes her eyes."

    voice "audio/narrator/chapter_1/line_059_L674.ogg"
    "Sleep comes slowly, in pieces, like a tide coming in — retreating, returning, retreating again. She dozes and wakes and dozes. At some point, the house goes quiet."

    voice "audio/narrator/chapter_1/line_060_L676.ogg"
    "At some point, the night ends."

    # Transition to morning / Chapter 2
    $ complete_chapter(1)
    scene black
    with fade

    voice "audio/centered/chapter_1/line_234.ogg"
    centered "{size=+6}End of Chapter One{/size}"
    pause 2.0

    return
