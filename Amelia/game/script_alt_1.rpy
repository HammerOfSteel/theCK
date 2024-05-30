# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Amelia")
define e = Character("Ella")
define j = Character("James")
define p = Character("Parents")
define n = Character("Narrator")
define s = Character("Student")
define prof_Williams = Character("Pr. Williams")
define music.chapter_0_2 = "chapter_0_2.mp3"
define music.chapter_1 = "chapter_1.mp3"
define music.chapter_2 = "chapter_2.mp3"


# The game starts here.

label start_alt_1:
    play music chapter_0_2 fadein 1.0 volume 0.1
    scene chapter_0
    with dissolve

    pause 4.0

    scene screen_m3
    with dissolve
    n "Amelias curiosity about the mind began in a room of dreams and playful experiments."

    scene screen_m2
    with dissolve
    n "High school was a theater of emotions and social hierarchies; a ripe field for observation"

    scene screen_m1
    with dissolve
    n "University, a beacon of hope, promising a sanctuary where curiosity intertwines with opportunit"

    scene screen_0
    with dissolve
    n "With every passing moment, the future lingered, veiled in an envelope yet to arrive."


    stop music fadeout 1.0

    #### Screens 1-20: A New Beginning

    #### Screen 1: A New Beginning
    #- **Setting**: Amelia's bedroom.
    #- **Description**: Walls adorned with posters of bands, books, and motivational quotes. Amelia reads her acceptance letter from Plymouth University.
    #- **Dialogue**: "I got in! I actually got in!"
    scene chapter_1
    with dissolve
    play music chapter_1 fadein 1.0 volume 0.1

    pause 4.0

    show chapter_1_screen_1
    with dissolve
    a "I got in! I actually got in!"

    #### Screen 2: Burst of Joy
    #- **Description**: Amelia's ecstatic expression, she jumps on her bed.
    #- **Dialogue**: "Plymouth, here I come!"
    show chapter_1_screen_2
    with dissolve
    a "Plymouth, here I come!"

    #### Screen 3: Moment of Reflection
    #- **Description**: Amelia's thoughtful pause.
    #- **Dialogue**: "But... who do I tell first?"
    #- **Choice**: "Tell Ella first" | "Tell Parents first."
    show chapter_1_screen_3
    with dissolve
    a "But... who do I tell first?"

    menu:
        "Tell Parents first":
            #### Screen 4: Telling Parents
            #- **Setting**: Amelia's living room.
            #- **Description**: Amelia displaying the letter to her parents.
            #- **Dialogue**: "Mum, Dad, Plymouth said YES!"
            show chapter_1_screen_4
            with dissolve
            a "Mum, Dad, Plymouth said YES!"

            #### Screen 5: Parents' Reaction
            #- **Description**: Parents beam with pride.
            #- **Dialogue**: "We always knew you'd make it, darling."
            show chapter_1_screen_5
            with dissolve
            parents "We always knew you'd make it, darling."

            #### Screen 6: Family Embrace
            #- **Description**: Amelia hugging both parents tightly.
            #- **Dialogue**: "Thank you for always believing in me."
            show chapter_1_screen_6
            with dissolve
            a "Thank you for always believing in me."

            #### Screen 7: Planning for the Future
            #- **Description**: Family discusses Amelia's upcoming move.
            #- **Dialogue**: "Let's start planning your move to Plymouth."
            show chapter_1_screen_7
            with dissolve
            parents "Let's start planning your move to Plymouth."

            #### Screen 8: Preparing for Departure
            #- **Setting**: Amelia's bedroom.
            #- **Description**: Amelia and her parents discuss packing and moving logistics.
            #- **Dialogue**: "We need to start packing soon."
            show chapter_1_screen_8
            with dissolve
            parents "We need to start packing soon."

            #### Screen 9: Packing Together
            #- **Description**: Amelia and her parents packing boxes.
            #- **Dialogue**: "Don't forget to label the boxes."
            show chapter_1_screen_9
            with dissolve
            parents "Don't forget to label the boxes."

            #### Screen 10: Finding Keepsakes
            #- **Description**: Amelia finds an old family photo.
            #- **Dialogue**: "I'll take this with me."
            show chapter_1_screen_10
            with dissolve
            a "I'll take this with me."

            #### Screen 11: Reflective Evening
            #- **Setting**: Amelia's bedroom.
            #- **Description**: Amelia sits on her bed, looking at the packed boxes.
            #- **Dialogue**: "This is really happening."
            show chapter_1_screen_11
            with dissolve
            a "This is really happening."

            #### Screen 12: Farewell Dinner
            #- **Setting**: Dining room.
            #- **Description**: Family dinner, celebrating Amelia's new journey.
            #- **Dialogue**: "To new beginnings!"
            show chapter_1_screen_12
            with dissolve
            family "To new beginnings!"

            #### Screen 13: Parent's Advice
            #- **Description**: Parents give Amelia advice for university life.
            #- **Dialogue**: "Study hard, but also enjoy yourself."
            show chapter_1_screen_13
            with dissolve
            parents "Study hard, but also enjoy yourself."

            #### Screen 14: Night Before Departure
            #- **Setting**: Amelia's bedroom.
            #- **Description**: Amelia finishes packing and prepares for bed.
            #- **Dialogue**: "Tomorrow's a big day."
            show chapter_1_screen_14
            with dissolve
            a "Tomorrow's a big day."

            #### Screen 15: Early Morning
            #- **Setting**: Amelia's bedroom.
            #- **Description**: Amelia wakes up early, feeling a mix of excitement and nerves.
            #- **Dialogue**: "Today's the day."
            show chapter_1_screen_15
            with dissolve
            a "Today's the day."

            #### Screen 16: Final Goodbyes
            #- **Setting**: Living room.
            #- **Description**: Amelia says goodbye to her parents.
            #- **Dialogue**: "I'll miss you both so much."
            show chapter_1_screen_16
            with dissolve
            a "I'll miss you both so much."

            #### Screen 17: Leaving Home
            #- **Setting**: Front door.
            #- **Description**: Amelia steps out of her house with her suitcase.
            #- **Dialogue**: "Here I go."
            show chapter_1_screen_17
            with dissolve
            a "Here I go."

            #### Screen 18: Car Ride to Train Station
            #- **Setting**: Car.
            #- **Description**: Amelia and her parents drive to the train station.
            #- **Dialogue**: "Remember to call us when you arrive."
            show chapter_1_screen_18
            with dissolve
            parents "Remember to call us when you arrive."

            #### Screen 19: Arrival at Train Station
            #- **Setting**: Train station.
            #- **Description**: Amelia and her parents arrive at the station.
            #- **Dialogue**: "Time to catch my train."
            show chapter_1_screen_19
            with dissolve
            a "Time to catch my train."

            #### Screen 20: Final Hugs
            #- **Description**: Amelia hugs her parents one last time.
            #- **Dialogue**: "Take care, Amelia."
            show chapter_1_screen_20
            with dissolve
            parents "Take care, Amelia."

        "Tell Ella first":
            #### Screen 21: Meeting Ella
            #- **Setting**: Park bench.
            #- **Description**: Amelia meets Ella to share the news.
            #- **Dialogue**: "Ella, look! I'm going to Plymouth!"
            show chapter_1_screen_21
            with dissolve
            a "Ella, look! I'm going to Plymouth!"

            #### Screen 22: Ella's Reaction
            #- **Description**: Ella's joyful expression.
            #- **Dialogue**: "That's amazing, Millie! I knew you could do it!"
            show chapter_1_screen_22
            with dissolve
            ella "That's amazing, Millie! I knew you could do it!"

            #### Screen 23: Emotional Farewell
            #- **Description**: Amelia and Ella sharing a tight hug.
            #- **Dialogue**: "It won't be the same without you here."
            show chapter_1_screen_23
            with dissolve
            ella "It won't be the same without you here."

            #### Screen 24: Thoughts on Change
            #- **Description**: Amelia's reflective expression.
            #- **Dialogue**: "I'll miss you too. But it's a new start, a new journey."
            show chapter_1_screen_24
            with dissolve
            a "I'll miss you too. But it's a new start, a new journey."

            #### Screen 25: Reminiscing
            #- **Setting**: Park.
            #- **Description**: Amelia and Ella reminisce about their childhood.
            #- **Dialogue**: "Do you remember our first day at school?"
            show chapter_1_screen_25
            with dissolve
            a "Do you remember our first day at school?"

            #### Screen 26: Flashback
            #- **Setting**: School playground.
            #- **Description**: Flashback to Amelia and Ella's first day at school.
            #- **Dialogue**: "We were so nervous back then."
            show chapter_1_screen_26
            with dissolve
            a "We were so nervous back then."

            #### Screen 27: Shared Memories
            #- **Description**: Ella recalls a funny memory.
            #- **Dialogue**: "And then you spilled paint all over yourself!"
            show chapter_1_screen_27
            with dissolve
            ella "And then you spilled paint all over yourself!"

            #### Screen 28: Laughter
            #- **Description**: Both laugh at the memory.
            #- **Dialogue**: "Those were the days."
            show chapter_1_screen_28
            with dissolve
            a "Those were the days."

            #### Screen 29: Promises
            #- **Setting**: Park bench.
            #- **Description**: Amelia and Ella make promises to stay in touch.
            #- **Dialogue**: "Promise you'll write to me?"
            show chapter_1_screen_29
            with dissolve
            ella "Promise you'll write to me?"

            #### Screen 30: Pinky Swear
            #- **Description**: They pinky swear.
            #- **Dialogue**: "Every week. Promise."
            show chapter_1_screen_30
            with dissolve
            ella "Every week. Promise."

            #### Screen 31: Farewell Gift
            #- **Setting**: Park.
            #- **Description**: Ella gives Amelia a farewell gift.
            #- **Dialogue**: "I got you something."
            show chapter_1_screen_31
            with dissolve
            ella "I got you something."

            #### Screen 32: Unwrapping the Gift
            #- **Description**: Amelia unwraps the gift.
            #- **Dialogue**: "It's beautiful! Thank you, Ella."
            show chapter_1_screen_32
            with dissolve
            a "It's beautiful! Thank you, Ella."

            #### Screen 33: Evening Walk
            #- **Setting**: Park.
            #- **Description**: Amelia and Ella take an evening walk.
            #- **Dialogue**: "Let's make the most of our time together."
            show chapter_1_screen_33
            with dissolve
            a "Let's make the most of our time together."

            #### Screen 34: Sunset
            #- **Description**: They watch the sunset together.
            #- **Dialogue**: "I'll never forget this moment."
            show chapter_1_screen_34
            with dissolve
            ella "I'll never forget this moment."

            #### Screen 35: Nightfall
            #- **Setting**: Park.
            #- **Description**: It gets dark, and they prepare to leave.
            #- **Dialogue**: "I should head home."
            show chapter_1_screen_35
            with dissolve
            a "I should head home."

            #### Screen 36: Parting Ways
            #- **Description**: Amelia and Ella part ways with a hug.
            #- **Dialogue**: "Take care, Ella."
            show chapter_1_screen_36
            with dissolve
            a "Take care, Ella."

            #### Screen 37: Reflecting on Friendship
            #- **Setting**: Walking home.
            #- **Description**: Amelia reflects on her friendship with Ella.
            #- **Narrative**: "Ella has always been there for me."
            show chapter_1_screen_37
            with dissolve
            n "Ella has always been there for me."

            #### Screen 38: Home Arrival
            #- **Setting**: Amelia's home.
            #- **Description**: Amelia arrives home, feeling emotional.
            #- **Dialogue**: "I'll miss her so much."
            show chapter_1_screen_38
            with dissolve
            a "I'll miss her so much."

            #### Screen 39: Late Night Thoughts
            #- **Setting**: Amelia's bedroom.
            #- **Description**: Amelia lays in bed, thinking about the future.
            #- **Dialogue**: "University life... I wonder what it'll be like."
            show chapter_1_screen_39
            with dissolve
            a "University life... I wonder what it'll be like."

            #### Screen 40: Dreaming of Plymouth
            #- **Description**: Amelia dreams about her new life in Plymouth.
            #- **Narrative**: "Excitement and nerves mix in my dreams."
            show chapter_1_screen_40
            with dissolve
            n "Excitement and nerves mix in my dreams."

    #### Screens 41-60: Spending the Day with Ella

    #### Screen 41: Morning Plans
    #- **Setting**: Amelia's bedroom.
    #- **Description**: Amelia wakes up and checks her phone.
    #- **Text Notification**: Ella: "Ready for our day together?"
    show chapter_1_screen_41
    with dissolve
    a "Ready for our day together?"

    #### Screen 42: Getting Ready
    #- **Description**: Amelia gets dressed and prepares to meet Ella.
    #- **Dialogue**: "Today's going to be great."
    show chapter_1_screen_42
    with dissolve
    a "Today's going to be great."

    #### Screen 43: Meeting at the Park
    #- **Setting**: Park.
    #- **Description**: Amelia and Ella meet at their usual spot.
    #- **Dialogue**: "Good morning!"
    show chapter_1_screen_43
    with dissolve
    a "Good morning!"

    #### Screen 44: Picnic Setup
    #- **Description**: They set up a picnic blanket and food.
    #- **Dialogue**: "I brought your favorite sandwiches."
    show chapter_1_screen_44
    with dissolve
    ella "I brought your favorite sandwiches."

    #### Screen 45: Eating and Chatting
    #- **Description**: They enjoy their picnic while chatting.
    #- **Dialogue**: "So, what's on the agenda for today?"
    show chapter_1_screen_45
    with dissolve
    a "So, what's on the agenda for today?"

    #### Screen 46: Exploring the Park
    #- **Description**: They walk around the park, exploring different areas.
    #- **Dialogue**: "Let's check out the new garden."
    show chapter_1_screen_46
    with dissolve
    a "Let's check out the new garden."

    #### Screen 47: Garden Visit
    #- **Setting**: Park garden.
    #- **Description**: They admire the flowers and plants.
    #- **Dialogue**: "These roses are beautiful."
    show chapter_1_screen_47
    with dissolve
    ella "These roses are beautiful."

    #### Screen 48: Taking Photos
    #- **Description**: They take selfies and photos of the garden.
    #- **Dialogue**: "Smile for the camera!"
    show chapter_1_screen_48
    with dissolve
    a "Smile for the camera!"

    #### Screen 49: Childhood Play Area
    #- **Setting**: Park playground.
    #- **Description**: They visit the playground where they used to play as kids.
    #- **Dialogue**: "Remember the swings?"
    show chapter_1_screen_49
    with dissolve
    ella "Remember the swings?"

    #### Screen 50: Swinging
    #- **Description**: They take turns on the swings, laughing.
    #- **Dialogue**: "Just like old times."
    show chapter_1_screen_50
    with dissolve
    a "Just like old times."

    #### Screen 51: Ice Cream Break
    #- **Setting**: Ice cream stand.
    #- **Description**: They buy ice cream cones.
    #- **Dialogue**: "One last treat before I go."
    show chapter_1_screen_51
    with dissolve
    a "One last treat before I go."

    #### Screen 52: Sharing Secrets
    #- **Setting**: Park bench.
    #- **Description**: They sit and share secrets.
    #- **Dialogue**: "There's something I've been meaning to tell you."
    show chapter_1_screen_52
    with dissolve
    ella "There's something I've been meaning to tell you."

    #### Screen 53: Heartfelt Conversation
    #- **Description**: They have a deep and heartfelt conversation.
    #- **Dialogue**: "I'll always be here for you, no matter what."
    show chapter_1_screen_53
    with dissolve
    ella "I'll always be here for you, no matter what."

    #### Screen 54: Final Walk
    #- **Setting**: Park path.
    #- **Description**: They take one last walk around the park.
    #- **Dialogue**: "This place holds so many memories."
    show chapter_1_screen_54
    with dissolve
    a "This place holds so many memories."

    #### Screen 55: Saying Goodbye
    #- **Setting**: Park entrance.
    #- **Description**: They hug tightly, saying goodbye.
    #- **Dialogue**: "Take care, Ella."
    show chapter_1_screen_55
    with dissolve
    a "Take care, Ella."

    #### Screen 56: Walking Home
    #- **Setting**: Street.
    #- **Description**: Amelia walks home, feeling emotional.
    #- **Dialogue**: "I can't believe this is goodbye."
    show chapter_1_screen_56
    with dissolve
    a "I can't believe this is goodbye."

    #### Screen 57: Evening Reflections
    #- **Setting**: Amelia's bedroom.
    #- **Description**: Amelia reflects on the day's events.
    #- **Dialogue**: "What a perfect day."
    show chapter_1_screen_57
    with dissolve
    a "What a perfect day."

    #### Screen 58: Writing in Diary
    #- **Description**: Amelia writes in her diary about the day.
    #- **Narrative**: "Today was unforgettable."
    show chapter_1_screen_58
    with dissolve
    n "Today was unforgettable."

    #### Screen 59: Bedtime Thoughts
    #- **Description**: Amelia gets ready for bed, thinking about Ella.
    #- **Dialogue**: "I hope she visits me in Plymouth."
    show chapter_1_screen_59
    with dissolve
    a "I hope she visits me in Plymouth."

    #### Screen 60: Dreaming of the Future
    #- **Description**: Amelia dreams about her future in Plymouth.
    #- **Narrative**: "New adventures await."
    show chapter_1_screen_60
    with dissolve
    n "New adventures await."

    #### Screens 61-80: Journey to Plymouth

    #### Screen 61: Early Morning Departure
    #- **Setting**: Amelia's bedroom.
    #- **Description**: Amelia wakes up early, feeling excited and nervous.
    #- **Dialogue**: "Today's the day."
    show chapter_1_screen_61
    with dissolve
    a "Today's the day."

    #### Screen 62: Final Preparations
    #- **Setting**: Living room.
    #- **Description**: Amelia and her parents make final preparations.
    #- **Dialogue**: "Do you have everything you need?"
    show chapter_1_screen_62
    with dissolve
    parents "Do you have everything you need?"

    #### Screen 63: Car Ride to Station
    #- **Setting**: Car.
    #- **Description**: Amelia and her parents drive to the train station.
    #- **Dialogue**: "Remember to call us when you arrive."
    show chapter_1_screen_63
    with dissolve
    parents "Remember to call us when you arrive."

    #### Screen 64: Arriving at Station
    #- **Setting**: Train station.
    #- **Description**: Amelia and her parents arrive at the station.
    #- **Dialogue**: "Time to catch my train."
    show chapter_1_screen_64
    with dissolve
    a "Time to catch my train."

    #### Screen 65: Final Hugs
    #- **Description**: Amelia hugs her parents one last time.
    #- **Dialogue**: "Take care, Amelia."
    show chapter_1_screen_65
    with dissolve
    parents "Take care, Amelia."

    #### Screen 66: Boarding the Train
    #- **Description**: Amelia boards the train with her suitcase.
    #- **Dialogue**: "Here I go."
    show chapter_1_screen_66
    with dissolve
    a "Here I go."

    #### Screen 67: Finding a Seat
    #- **Setting**: Inside the train.
    #- **Description**: Amelia finds a seat and settles in.
    #- **Dialogue**: "Perfect spot."
    show chapter_1_screen_67
    with dissolve
    a "Perfect spot."

    #### Screen 68: Train Departure
    #- **Description**: The train starts moving.
    #- **Narrative**: "A new chapter begins."
    show chapter_1_screen_68
    with dissolve
    n "A new chapter begins."

    #### Screen 69: Watching the Scenery
    #- **Description**: Amelia looks out the window, watching the scenery change.
    #- **Narrative**: "From the familiar streets of London to the unknown paths of Plymouth."
    show chapter_1_screen_69
    with dissolve
    n "From the familiar streets of London to the unknown paths of Plymouth."

    #### Screen 70: Diary Entry
    #- **Description**: Amelia writes in her diary about her journey.
    #- **Narrative**: "Thoughts, dreams, and a tinge of nervousness."
    show chapter_1_screen_70
    with dissolve
    n "Thoughts, dreams, and a tinge of nervousness."

    #### Screen 71: Text from Ella
    #- **Description**: Amelia's phone vibrates with a message from Ella.
    #- **Text Notification**: Ella: "How's the journey?"
    show chapter_1_screen_71
    with dissolve
    a "How's the journey?"

    #### Screen 72: Quick Reply
    #- **Description**: Amelia replies to Ella's message.
    #- **Text**: "So far, so good. I'll call you when I get there."
    show chapter_1_screen_72
    with dissolve
    a "So far, so good. I'll call you when I get there."

    #### Screen 73: Train Snack
    #- **Setting**: Train dining car.
    #- **Description**: Amelia buys a snack from the dining car.
    #- **Dialogue**: "A sandwich, please."
    show chapter_1_screen_73
    with dissolve
    a "A sandwich, please."

    #### Screen 74: Friendly Stranger
    #- **Description**: Amelia strikes up a conversation with a fellow passenger.
    #- **Dialogue**: "Heading to Plymouth too?"
    show chapter_1_screen_74
    with dissolve
    stranger "Heading to Plymouth too?"

    #### Screen 75: Learning About Plymouth
    #- **Description**: The stranger shares tips about Plymouth.
    #- **Dialogue**: "It's a great city. You'll love it."
    show chapter_1_screen_75
    with dissolve
    stranger "It's a great city. You'll love it."

    #### Screen 76: Arrival Announcement
    #- **Description**: The train conductor announces the upcoming stop.
    #- **Narrative**: "Next stop, Plymouth."
    show chapter_1_screen_76
    with dissolve
    n "Next stop, Plymouth."

    #### Screen 77: Gathering Belongings
    #- **Description**: Amelia gathers her belongings, preparing to disembark.
    #- **Dialogue**: "Almost there."
    show chapter_1_screen_77
    with dissolve
    a "Almost there."

    #### Screen 78: Stepping Off the Train
    #- **Setting**: Plymouth train station.
    #- **Description**: Amelia steps off the train, feeling a mix of excitement and nerves.
    #- **Dialogue**: "This is it."
    show chapter_1_screen_78
    with dissolve
    a "This is it."

    #### Screen 79: Observing New Surroundings
    #- **Description**: Amelia takes in her new surroundings.
    #- **Narrative**: "A new city, a new start."
    show chapter_1_screen_79
    with dissolve
    n "A new city, a new start."

    #### Screen 80: Heading to the University
    #- **Description**: Amelia heads towards the university.
    #- **Dialogue**: "Let's find my new home."
    show chapter_1_screen_80
    with dissolve
    a "Let's find my new home."

    #### Screens 81-100: Exploring the University and Arriving at the Dorm

    #### Screen 81: University Entrance
    #- **Setting**: Plymouth University entrance.
    #- **Description**: Amelia approaches the university with building excitement.
    #- **Narrative**: "The beginning of her university journey."
    show chapter_1_screen_81
    with dissolve
    n "The beginning of her university journey."

    #### Screen 82: Campus Tour
    #- **Setting**: Various university landmarks.
    #- **Description**: Amelia explores the campus, discovering key locations.
    #- **Dialogue**: "The library looks amazing... and there's the psychology department!"
    show chapter_1_screen_82
    with dissolve
    a "The library looks amazing... and there's the psychology department!"

    #### Screen 83: Meeting New Students
    #- **Description**: Amelia introduces herself to fellow students.
    #- **Dialogue**: "Hi, I'm Amelia. First year psychology."
    show chapter_1_screen_83
    with dissolve
    a "Hi, I'm Amelia. First year psychology."

    #### Screen 84: Cafeteria Visit
    #- **Setting**: University cafeteria.
    #- **Description**: Amelia grabs a quick snack.
    #- **Dialogue**: "I could use a coffee."
    show chapter_1_screen_84
    with dissolve
    a "I could use a coffee."

    #### Screen 85: Orientation Session
    #- **Setting**: University auditorium.
    #- **Description**: Amelia attends the orientation session.
    #- **Narrative**: "Welcome to Plymouth University!"
    show chapter_1_screen_85
    with dissolve
    n "Welcome to Plymouth University!"

    #### Screen 86: Orientation Speech
    #- **Description**: The university dean gives an inspiring speech.
    #- **Dialogue**: "You are the future, and we are here to guide you."
    show chapter_1_screen_86
    with dissolve
    dean "You are the future, and we are here to guide you."

    #### Screen 87: Psychology Department
    #- **Setting**: Psychology department.
    #- **Description**: Amelia visits the psychology department.
    #- **Dialogue**: "This is where I'll be spending most of my time."
    show chapter_1_screen_87
    with dissolve
    a "This is where I'll be spending most of my time."

    #### Screen 88: Meeting Professors
    #- **Description**: Amelia meets some of her future professors.
    #- **Dialogue**: "Welcome to the psychology program. We are excited to have you."
    show chapter_1_screen_88
    with dissolve
    prof "Welcome to the psychology program. We are excited to have you."

    #### Screen 89: Finding Her Way
    #- **Setting**: Campus.
    #- **Description**: Amelia tries to find her way around campus.
    #- **Dialogue**: "Where's the dormitory?"
    show chapter_1_screen_89
    with dissolve
    a "Where's the dormitory?"

    #### Screen 90: Asking for Directions
    #- **Description**: Amelia asks a fellow student for directions.
    #- **Dialogue**: "Excuse me, do you know where the dorms are?"
    show chapter_1_screen_90
    with dissolve
    a "Excuse me, do you know where the dorms are?"

    #### Screen 91: Friendly Help
    #- **Description**: The student helps Amelia with directions.
    #- **Dialogue**: "Sure, follow me."
    show chapter_1_screen_91
    with dissolve
    student "Sure, follow me."

    #### Screen 92: Walking to the Dorm
    #- **Description**: Amelia follows the student to the dormitory.
    #- **Dialogue**: "Thanks for your help."
    show chapter_1_screen_92
    with dissolve
    a "Thanks for your help."

    #### Screen 93: First Glimpse of the Dorm
    #- **Setting**: Dormitory entrance.
    #- **Description**: Amelia sees her new home for the first time.
    #- **Narrative**: "This looks nice."
    show chapter_1_screen_93
    with dissolve
    n "This looks nice."

    #### Screen 94: Checking In
    #- **Setting**: Dormitory reception.
    #- **Description**: Amelia checks in and gets her room key.
    #- **Dialogue**: "Hi, I'm here to check in."
    show chapter_1_screen_94
    with dissolve
    a "Hi, I'm here to check in."

    #### Screen 95: Receiving Room Key
    #- **Description**: The receptionist hands Amelia her room key.
    #- **Dialogue**: "Room 101. Welcome to your new home."
    show chapter_1_screen_95
    with dissolve
    receptionist "Room 101. Welcome to your new home."

    #### Screen 96: Finding Her Room
    #- **Setting**: Dormitory hallway.
    #- **Description**: Amelia walks down the hallway, looking for her room.
    #- **Dialogue**: "Room 101... here it is."
    show chapter_1_screen_96
    with dissolve
    a "Room 101... here it is."

    #### Screen 97: Opening the Door
    #- **Description**: Amelia opens the door to her dorm room.
    #- **Narrative**: "Moment of truth."
    show chapter_1_screen_97
    with dissolve
    n "Moment of truth."

    #### Screen 98: Entering the Room
    #- **Description**: Amelia steps into her new room, taking it all in.
    #- **Dialogue**: "This is it. My new home."
    show chapter_1_screen_98
    with dissolve
    a "This is it. My new home."

    #### Screen 99: Settling In
    #- **Description**: Amelia starts unpacking and setting up her room.
    #- **Narrative**: "Making this place feel like home."
    show chapter_1_screen_99
    with dissolve
    n "Making this place feel like home."

    #### Screen 100: Reflecting on the Day
    #- **Description**: Amelia sits on her bed, reflecting on the day's events.
    #- **Dialogue**: "What a day... and this is just the beginning."
    show chapter_1_screen_100
    with dissolve
    a "What a day... and this is just the beginning."

    # -------------------------------------------------------------------------------------------------

    # Chapter 2
    ## New Beginnings

    stop music fadeout 1.0

    #### Screens 1-20: Settling In and Orientation

    #- **Setting**: Dormitory entrance.
    #- **Description**: Amelia arrives with her luggage.
    #- **Dialogue**: "This is it. My new home."
    scene chapter_2
    with dissolve
    play music chapter_2 fadein 1.0 volume 0.1

    pause 4.0

    show chapter_2_screen_1
    with dissolve
    a "This is it. My new home."

    #- **Description**: Resident Assistant (RA) gives a tour of the dormitory and offers guidance.
    #- **Dialogue**: "Hi, I'm your RA. Welcome to Plymouth!"
    show chapter_2_screen_2
    with dissolve
    ra "Hi, I'm your RA. Welcome to Plymouth!"

    #- **Description**: Amelia receives her room key.
    #- **Dialogue**: "Room 203. Let's find it."
    show chapter_2_screen_3
    with dissolve
    a "Room 203. Let's find it."

    #- **Description**: Amelia enters her new room.
    #- **Narrative**: "Time to unpack and settle in."
    show chapter_2_screen_4
    with dissolve
    n "Time to unpack and settle in."

    #- **Description**: Amelia meets her roommate.
    #- **Dialogue**: "Hi, I'm Amelia. Nice to meet you."
    show chapter_2_screen_5
    with dissolve
    a "Hi, I'm Amelia. Nice to meet you."

    #- **Description**: Amelia starts unpacking.
    #- **Dialogue**: "I should make this place feel like home."
    show chapter_2_screen_6
    with dissolve
    a "I should make this place feel like home."

    #- **Description**: Amelia and her roommate chat.
    #- **Dialogue**: "Where are you from?"
    show chapter_2_screen_7
    with dissolve
    roommate "Where are you from?"

    #- **Description**: Dorm Introduction by the RA.
    #- **Dialogue**: "This is the common room where we all hang out."
    show chapter_2_screen_8
    with dissolve
    ra "This is the common room where we all hang out."

    #- **Description**: Campus Tour Offer by the RA.
    #- **Dialogue**: "Would you like a tour of the campus?"
    show chapter_2_screen_9
    with dissolve
    ra "Would you like a tour of the campus?"

    menu:
        "Sure, I'd love one!":
            #### Branch 1: Join the Tour

            #- **Setting**: Main hall.
            #- **Description**: A student guide leading a group, including Amelia.
            #- **Narrative**: "A guided tour of the sprawling campus begins."
            show chapter_2_screen_10
            with dissolve
            n "A guided tour of the sprawling campus begins."

            #- **Description**: Guide explaining the university's history.
            #- **Dialogue**: "Plymouth Uni has been standing strong since 1862!"
            show chapter_2_screen_11
            with dissolve
            guide "Plymouth Uni has been standing strong since 1862!"

            #- **Description**: Amelia spots a familiar face in the crowd.
            #- **Dialogue**: "James? Is that you? From summer camp!"
            show chapter_2_screen_12
            with dissolve
            a "James? Is that you? From summer camp!"

            #- **Description**: James approaches with a smile.
            #- **Dialogue**: "Amelia! It's been ages! How have you been?"
            show chapter_2_screen_13
            with dissolve
            j "Amelia! It's been ages! How have you been?"

            #- **Description**: Both discussing their chosen courses.
            #- **Dialogue**: "You're in psychology too? This should be fun!"
            show chapter_2_screen_14
            with dissolve
            j "You're in psychology too? This should be fun!"

        "No, I'll be okay thanks":
            #### Branch 2: Explore on Your Own

            #- **Setting**: University gardens.
            #- **Description**: Amelia strolling amidst beautiful flowerbeds.
            #- **Narrative**: "A quiet moment to soak in the new surroundings."
            show chapter_2_screen_15
            with dissolve
            n "A quiet moment to soak in the new surroundings."

            #- **Description**: Amelia bumping into a senior student.
            #- **Dialogue**: "Lost, newbie? I can help!"
            show chapter_2_screen_16
            with dissolve
            senior "Lost, newbie? I can help!"

            #- **Description**: The senior student pointing out important locations.
            #- **Narrative**: "The library's that way, and the psychology department? Right behind you."
            show chapter_2_screen_17
            with dissolve
            senior "The library's that way, and the psychology department? Right behind you."
            a "This place is huge hehe.. Thank you so much."

            #- **Description**: Amelia spots a familiar face in the crowd.
            #- **Dialogue**: "James? Is that you? From summer camp!"
            show chapter_2_screen_12
            with dissolve
            a "James? Is that you? From summer camp!"

            #- **Description**: James approaches with a smile.
            #- **Dialogue**: "Amelia! It's been ages! How have you been?"
            show chapter_2_screen_13
            with dissolve
            j "Amelia! It's been ages! How have you been?"

            #- **Description**: Both discussing their chosen courses.
            #- **Dialogue**: "You're in psychology too? This should be fun!"
            show chapter_2_screen_14
            with dissolve
            j "You're in psychology too? This should be fun!"

    #### Screens 11-20: Meeting Mentors and Allies

    #- **Setting**: Auditorium.
    #- **Description**: University dean gives a welcoming speech, inspiring the new students.
    #- **Dialogue**: "Welcome to Plymouth University!"
    show chapter_2_screen_18
    with dissolve
    dean "Welcome to Plymouth University!"

    #- **Description**: Various activities for freshmen, including ice-breaking games and introductions.
    #- **Narrative**: "Ice-breaking games and introductions."
    show chapter_2_screen_19
    with dissolve
    n "Ice-breaking games and introductions."

    #- **Setting**: Lecture hall.
    #- **Description**: Introduction to the first psychology lecture.
    #- **Narrative**: "The first psychology lecture."
    show chapter_2_screen_20
    with dissolve
    n "The first psychology lecture."

    #- **Description**: Amelia meets her psychology professors.
    #- **Dialogue**: "Looking forward to learning from you."
    show chapter_2_screen_21
    with dissolve
    prof_Williams "Looking forward to learning from you."

    #- **Setting**: Library.
    #- **Description**: Amelia discovers the library, where she meets fellow students.
    #- **Dialogue**: "This place is amazing!"
    show chapter_2_screen_22
    with dissolve
    a "This place is amazing!"

    #- **Description**: Fellow students invite Amelia to join their study group.
    #- **Dialogue**: "Want to join our study group?"
    show chapter_2_screen_23
    with dissolve
    student "Want to join our study group?"

    #- **Description**: Amelia meets her study group and they start planning their studies.
    #- **Dialogue**: "Let's meet up tomorrow to start."
    show chapter_2_screen_24
    with dissolve
    student "Let's meet up tomorrow to start."

    #### Screens 21-40: Meeting New People and First Classes

    #- **Setting**: Classroom.
    #- **Description**: Amelia attends her first psychology lecture and meets her classmates.
    #- **Narrative**: "The real journey begins."
    show chapter_2_screen_25
    with dissolve
    n "The real journey begins."

    #- **Description**: Engaging discussions in psychology class.
    #- **Dialogue**: "Today's topic is fascinating!"
    show chapter_2_screen_26
    with dissolve
    a "Today's topic is fascinating!"

    #- **Description**: Details about the first assignment are given.
    #- **Dialogue**: "Make sure to research thoroughly."
    show chapter_2_screen_27
    with dissolve
    prof_Williams "Make sure to research thoroughly."

    #- **Setting**: Professor's office.
    #- **Description**: Amelia seeks guidance from Prof. Williams during office hours.
    #- **Dialogue**: "Can you help me with this topic?"
    show chapter_2_screen_28
    with dissolve
    a "Can you help me with this topic?"

    #- **Setting**: Cafeteria.
    #- **Description**: Amelia and friends grab lunch and discuss their classes.
    #- **Dialogue**: "What do you think of the lecture?"
    show chapter_2_screen_29
    with dissolve
    friend "What do you think of the lecture?"

    #- **Setting**: Psychology lab.
    #- **Description**: Hands-on learning experience in the psychology lab.
    #- **Dialogue**: "This experiment is so interesting!"
    show chapter_2_screen_30
    with dissolve
    a "This experiment is so interesting!"

    #- **Description**: Amelia is invited to a campus event.
    #- **Dialogue**: "Want to come to the event tonight?"
    show chapter_2_screen_31
    with dissolve
    friend "Want to come to the event tonight?"

    menu:
        "Attend the event":
            #### Branch 1: Attend the Event

            #- **Description**: Amelia participates in the event, meeting new people.
            #- **Dialogue**: "Hi, I'm Amelia."
            show chapter_2_screen_32
            with dissolve
            a "Hi, I'm Amelia."

            #- **Description**: Making connections with students from different faculties.
            #- **Dialogue**: "Nice to meet you. I'm in the engineering department."
            show chapter_2_screen_33
            with dissolve
            student "Nice to meet you. I'm in the engineering department."

        "Join an extra-curricular activity":
            #### Branch 2: Join an Extra-Curricular Activity

            #- **Description**: Exploring different clubs and societies.
            #- **Dialogue**: "Let's see what clubs they have here."
            show chapter_2_screen_34
            with dissolve
            a "Let's see what clubs they have here."

            #- **Description**: Amelia decides to join a club that interests her.
            #- **Dialogue**: "The psychology club sounds interesting."
            show chapter_2_screen_35
            with dissolve
            a "The psychology club sounds interesting."

    #### Screens 31-40: Building Bonds

    #- **Setting**: Library.
    #- **Description**: Study group meets to work on the first assignment.
    #- **Dialogue**: "Let's divide the tasks."
    show chapter_2_screen_36
    with dissolve
    student "Let's divide the tasks."

    #- **Setting**: Campus grounds.
    #- **Description**: Amelia takes a relaxing evening walk with her friends.
    #- **Dialogue**: "This campus is beautiful at night."
    show chapter_2_screen_37
    with dissolve
    a "This campus is beautiful at night."

    #- **Setting**: Dorm room.
    #- **Description**: Writing in her journal about her experiences.
    #- **Narrative**: "Reflecting on the day's events."
    show chapter_2_screen_38
    with dissolve
    n "Reflecting on the day's events."

    #- **Setting**: Dormitory common room.
    #- **Description**: Watching a movie with friends.
    #- **Dialogue**: "What movie should we watch?"
    show chapter_2_screen_39
    with dissolve
    friend "What movie should we watch?"

    #- **Setting**: Campus grounds.
    #- **Description**: Walking and talking under the stars with her roommate.
    #- **Dialogue**: "It's so peaceful here at night."
    show chapter_2_screen_40
    with dissolve
    roommate "It's so peaceful here at night."

    #- **Description**: Amelia struggles to balance her academic and social life.
    #- **Dialogue**: "I need to manage my time better."
    show chapter_2_screen_41
    with dissolve
    a "I need to manage my time better."

    #### Screens 41-60: Establishing Routine and Forming Friendships

    #- **Description**: Amelia feels homesick and calls her parents for support.
    #- **Dialogue**: "Hi, Mum. Just wanted to check in."
    show chapter_2_screen_42
    with dissolve
    a "Hi, Mum. Just wanted to check in."

    #- **Description**: Friends offer support, helping her cope with homesickness.
    #- **Dialogue**: "We’re here for you, Amelia."
    show chapter_2_screen_43
    with dissolve
    friend "We’re here for you, Amelia."

    #- **Description**: Friends help Amelia create a schedule to manage her time better.
    #- **Dialogue**: "Let's make a schedule together."
    show chapter_2_screen_44
    with dissolve
    friend "Let's make a schedule together."

    #- **Description**: Amelia tries yoga or meditation for stress relief.
    #- **Dialogue**: "Yoga should help me relax."
    show chapter_2_screen_45
    with dissolve
    a "Yoga should help me relax."

    #- **Description**: Attending club meetings and participating in activities.
    #- **Dialogue**: "I'm excited for the club meeting."
    show chapter_2_screen_46
    with dissolve
    a "I'm excited for the club meeting."

    #- **Description**: Amelia feels overwhelmed by the amount of work.
    #- **Dialogue**: "I have so much to do."
    show chapter_2_screen_47
    with dissolve
    a "I have so much to do."

    #- **Description**: She seeks help from her professors and study group.
    #- **Dialogue**: "Can you help me with this assignment?"
    show chapter_2_screen_48
    with dissolve
    a "Can you help me with this assignment?"

    #- **Description**: Amelia's friends plan a weekend outing.
    #- **Dialogue**: "Let's go explore the city this weekend."
    show chapter_2_screen_49
    with dissolve
    friend "Let's go explore the city this weekend."

    menu:
        "Join the outing":
            #### Branch 1: Join the Outing

            #- **Setting**: Plymouth city.
            #- **Description**: Discovering new spots in Plymouth city with friends.
            #- **Dialogue**: "This place is amazing!"
            show chapter_2_screen_50
            with dissolve
            a "This place is amazing!"

            #- **Description**: Strengthening friendships through shared experiences.
            #- **Dialogue**: "I’m glad we did this."
            show chapter_2_screen_51
            with dissolve
            friend "I’m glad we did this."

        "Stay and focus on studies":
            #### Branch 2: Stay and Focus on Studies

            #- **Setting**: Library.
            #- **Description**: Intensive study session in the library.
            #- **Dialogue**: "I need to catch up on my reading."
            show chapter_2_screen_52
            with dissolve
            a "I need to catch up on my reading."

            #- **Description**: Making significant progress in her assignments.
            #- **Dialogue**: "I'm making good progress."
            show chapter_2_screen_53
            with dissolve
            a "I'm making good progress."

    #### Screens 61-80: Dealing with Challenges and Adjustments

    #- **Setting**: Examination hall.
    #- **Description**: Preparing for and taking the midterm exams.
    #- **Narrative**: "The midterm exams are here."
    show chapter_2_screen_54
    with dissolve
    n "The midterm exams are here."

    #- **Description**: Checking grades and discussing results with friends.
    #- **Dialogue**: "I hope I did well."
    show chapter_2_screen_55
    with dissolve
    a "I hope I did well."

    #- **Description**: Receiving feedback on her assignments and improving her work.
    #- **Dialogue**: "Thank you for the feedback, Professor."
    show chapter_2_screen_56
    with dissolve
    a "Thank you for the feedback, Professor."

    #- **Description**: Participating in psychology discussion groups.
    #- **Dialogue**: "This discussion group is so insightful."
    show chapter_2_screen_57
    with dissolve
    a "This discussion group is so insightful."

    #- **Description**: Amelia is invited to another social event.
    #- **Dialogue**: "There's a party this weekend. Want to come?"
    show chapter_2_screen_58
    with dissolve
    friend "There's a party this weekend. Want to come?"

    menu:
        "Attend the event":
            #### Branch 1: Attend the Event

            #- **Description**: Building her social network and meeting new people.
            #- **Dialogue**: "Hi, I'm Amelia. Nice to meet you."
            show chapter_2_screen_59
            with dissolve
            a "Hi, I'm Amelia. Nice to meet you."

            #- **Description**: Reflecting on her growing social circle.
            #- **Dialogue**: "I’m really enjoying university life."
            show chapter_2_screen_60
            with dissolve
            a "I’m really enjoying university life."

        "Spend time with study group":
            #### Branch 2: Spend Time with Study Group

            #- **Setting**: Study room.
            #- **Description**: Deepening her knowledge and bonding with study group members.
            #- **Dialogue**: "Let's go over this material together."
            show chapter_2_screen_61
            with dissolve
            student "Let's go over this material together."

            #- **Description**: Late-night study session with the group.
            #- **Dialogue**: "We’re almost done."
            show chapter_2_screen_62
            with dissolve
            student "We’re almost done."

    #### Screens 76-80: New Alliances

    #- **Description**: Exploring and joining a new club.
    #- **Dialogue**: "I think I’ll join the debate club."
    show chapter_2_screen_63
    with dissolve
    a "I think I’ll join the debate club."

    #- **Description**: Participating actively in club activities and events.
    #- **Dialogue**: "This debate topic is fascinating."
    show chapter_2_screen_64
    with dissolve
    a "This debate topic is fascinating."

    #- **Description**: Reflecting on her personal growth and new experiences.
    #- **Dialogue**: "I’ve grown so much since I arrived."
    show chapter_2_screen_65
    with dissolve
    a "I’ve grown so much since I arrived."

    #### Screens 81-100: Building Connections and Looking Forward

    #- **Description**: Starting the day with a structured routine.
    #- **Dialogue**: "Time to start the day."
    show chapter_2_screen_66
    with dissolve
    a "Time to start the day."

    #- **Description**: Morning conversations with friends about their plans.
    #- **Dialogue**: "What’s on your agenda today?"
    show chapter_2_screen_67
    with dissolve
    friend "What’s on your agenda today?"

    #- **Setting**: Professor’s office.
    #- **Description**: Seeking further guidance during office hours.
    #- **Dialogue**: "I need help with this topic, Professor."
    show chapter_2_screen_68
    with dissolve
    a "I need help with this topic, Professor."

    #- **Setting**: Psychology lab.
    #- **Description**: Continuing hands-on learning in the lab.
    #- **Dialogue**: "This lab work is really helping me understand the material."
    show chapter_2_screen_69
    with dissolve
    a "This lab work is really helping me understand the material."

    #- **Setting**: Study room.
    #- **Description**: Collaborating on a group project.
    #- **Dialogue**: "Let's divide the project tasks."
    show chapter_2_screen_70
    with dissolve
    student "Let's divide the project tasks."

    #- **Description**: Planning another weekend outing with friends.
    #- **Dialogue**: "Let’s visit the museum this weekend."
    show chapter_2_screen_71
    with dissolve
    friend "Let’s visit the museum this weekend."

    #- **Setting**: Plymouth museum.
    #- **Description**: Visiting a local museum and learning about Plymouth’s history.
    #- **Dialogue**: "This exhibit is so interesting."
    show chapter_2_screen_72
    with dissolve
    a "This exhibit is so interesting."

    #- **Setting**: Local café.
    #- **Description**: Relaxing and chatting over coffee at a local café.
    #- **Dialogue**: "This café has the best coffee."
    show chapter_2_screen_73
    with dissolve
    a "This café has the best coffee."

    #- **Setting**: Dorm room.
    #- **Description**: Writing about the week’s experiences.
    #- **Narrative**: "Reflecting on the week."
    show chapter_2_screen_74
    with dissolve
    n "Reflecting on the week."

    #- **Description**: Reflecting on the first week and setting goals for the future.
    #- **Dialogue**: "Next week will be even better."
    show chapter_2_screen_75
    with dissolve
    a "Next week will be even better."

    #- **Description**: Preparing for the upcoming weeks and making plans.
    #- **Narrative**: "Looking forward to the upcoming weeks."
    show chapter_2_screen_76
    with dissolve
    n "Looking forward to the upcoming weeks."

    return


    # ------------------------------------------------------------------------------------------------------------

    define a = Character("Amelia")
    define roommate = Character("Roommate")
    define counselor = Character("Counselor")
    define prof = Character("Professor")
    define friend = Character("Friend")
    define dean = Character("Dean")
    define senior = Character("Senior Student")
    define bully = Character("Bully")
    define stranger = Character("Stranger")
    define music.chapter_3 = "chapter_3.mp3"

    play music chapter_3 fadein 1.0 volume 0.1
    scene chapter_3
    with dissolve

    #### Screens 1-20: Initial Challenges

    #### Screen 1: Settling into Routine
    #- **Setting**: Dorm room.
    #- **Description**: Amelia wakes up and prepares for her day.
    show chapter_3_screen_1
    with dissolve
    a "Another day, another class. I hope today goes well."

    #### Screen 2: Morning Class
    #- **Setting**: Classroom.
    #- **Description**: Amelia attends her morning class.
    #- **Dialogue**: "Good morning, class."
    show chapter_3_screen_2
    with dissolve
    prof "Good morning, class."

    #### Screen 3: Subtle Bullying
    #- **Description**: Amelia hears whispers and feels stares.
    #- **Narrative**: "Why are they whispering about me?"
    show chapter_3_screen_3
    with dissolve
    n "Why are they whispering about me?"

    #### Screen 4: Lunch Break
    #- **Setting**: Cafeteria.
    #- **Description**: Amelia sits alone, feeling isolated.
    #- **Dialogue**: "I feel so alone."
    show chapter_3_screen_4
    with dissolve
    a "I feel so alone."

    #### Screen 5: Friend's Support
    #- **Description**: A friend joins Amelia for lunch.
    #- **Dialogue**: "Hey, mind if I join you?"
    show chapter_3_screen_5
    with dissolve
    friend "Hey, mind if I join you?"

    #### Screen 6: Bullying Escalates
    #- **Description**: Amelia finds a nasty note in her locker.
    #- **Narrative**: "Why are they doing this to me?"
    show chapter_3_screen_6
    with dissolve
    n "Why are they doing this to me?"

    #### Screen 7: Seeking Comfort
    #- **Setting**: Dorm room.
    #- **Description**: Amelia calls her parents for comfort.
    #- **Dialogue**: "Hi, Mum. I just needed to hear your voice."
    show chapter_3_screen_7
    with dissolve
    a "Hi, Mum. I just needed to hear your voice."

    #### Screen 8: Emotional Toll
    #- **Description**: Amelia feels the emotional toll of the bullying.
    #- **Dialogue**: "I don't know how much more of this I can take."
    show chapter_3_screen_8
    with dissolve
    a "I don't know how much more of this I can take."

    #### Screen 9: Witnessing Racism
    #- **Setting**: Campus.
    #- **Description**: Amelia witnesses a racist incident.
    #- **Dialogue**: "Did that really just happen?"
    show chapter_3_screen_9
    with dissolve
    a "Did that really just happen?"

    #### Screen 10: Reflective Evening
    #- **Setting**: Dorm room.
    #- **Description**: Amelia reflects on the day's events.
    #- **Dialogue**: "This day has been so draining."
    show chapter_3_screen_10
    with dissolve
    a "This day has been so draining."

    #### Screen 11: Seeking Support
    #- **Setting**: Dorm room.
    #- **Description**: Amelia talks to her roommate about her experiences.
    #- **Dialogue**: "I don't know how to deal with this."
    show chapter_3_screen_11
    with dissolve
    a "I don't know how to deal with this."

    menu:
        "Seek Help":
            jump seek_help_branch

        "Self-Reliance":
            jump self_reliance_branch

    label seek_help_branch:
        #### Screen 12: Roommate's Advice
        #- **Description**: Roommate offers advice and support.
        #- **Dialogue**: "You should talk to someone about this."
        show chapter_3_screen_12
        with dissolve
        roommate "You should talk to someone about this."

        #### Screen 13: Visiting the Counselor
        #- **Setting**: Counselor's office.
        #- **Description**: Amelia visits the campus counselor.
        #- **Dialogue**: "I need help dealing with some issues."
        show chapter_3_screen_13
        with dissolve
        a "I need help dealing with some issues."

        menu:
            "Confront Bullies":
                jump confront_bullies_branch

            "Seek Authority":
                jump seek_authority_branch

    label self_reliance_branch:
        #### Screen 12: Turning to Books
        #- **Description**: Amelia turns to books for solace and wisdom.
        #- **Dialogue**: "Maybe I can find some answers here."
        show chapter_3_screen_12_alt
        with dissolve
        a "Maybe I can find some answers here."

        menu:
            "Confront Bullies":
                jump confront_bullies_alone_branch

            "Philosophical Wisdom":
                jump philosophical_wisdom_branch

    label confront_bullies_branch:
        #### Screen 14: Confronting Bullies
        #- **Setting**: Campus.
        #- **Description**: Amelia confronts the bullies.
        #- **Dialogue**: "Why are you doing this to me?"
        show chapter_3_screen_14
        with dissolve
        a "Why are you doing this to me?"

        #### Screen 15: Bullies' Response
        #- **Description**: The bullies laugh and dismiss her.
        #- **Dialogue**: "We're just having fun."
        show chapter_3_screen_15
        with dissolve
        bullies "We're just having fun."

        menu:
            "Stand Ground":
                jump stand_ground_branch

            "Avoidance":
                jump avoidance_branch

    label seek_authority_branch:
        #### Screen 14: Reporting to Dean
        #- **Setting**: Dean's office.
        #- **Description**: Amelia reports the bullying to the dean.
        #- **Dialogue**: "I need to report some bullying."
        show chapter_3_screen_14_alt
        with dissolve
        a "I need to report some bullying."

        #### Screen 15: Dean's Response
        #- **Description**: The dean listens and promises to take action.
        #- **Dialogue**: "We'll look into this matter immediately."
        show chapter_3_screen_15_alt
        with dissolve
        dean "We'll look into this matter immediately."

        menu:
            "Follow-Up":
                jump follow_up_branch

            "Take Action":
                jump take_action_branch

    label confront_bullies_alone_branch:
        #### Screen 14: Confronting Bullies Alone
        #- **Setting**: Campus.
        #- **Description**: Amelia confronts the bullies alone.
        #- **Dialogue**: "Why are you doing this to me?"
        show chapter_3_screen_14_alt_2
        with dissolve
        a "Why are you doing this to me?"

        #### Screen 15: Bullies' Reaction
        #- **Description**: The bullies react aggressively.
        #- **Dialogue**: "Mind your own business."
        show chapter_3_screen_15_alt_2
        with dissolve
        bullies "Mind your own business."

        menu:
            "Defensive":
                jump defensive_branch

            "Retreat":
                jump retreat_branch

    label philosophical_wisdom_branch:
        #### Screen 14: Seeking Wisdom in Books
        #- **Setting**: Library.
        #- **Description**: Amelia seeks wisdom in philosophical texts.
        #- **Dialogue**: "Maybe these words can guide me."
        show chapter_3_screen_14_alt_3
        with dissolve
        a "Maybe these words can guide me."

        #### Screen 15: Reflecting on Philosophy
        #- **Description**: Amelia reflects on a philosophical quote.
        #- **Dialogue**: "'The wound is the place where the Light enters you.'"
        show chapter_3_screen_15_alt_3
        with dissolve
        a "'The wound is the place where the Light enters you.'"

        menu:
            "Apply Wisdom":
                jump apply_wisdom_branch

            "Seek Practical Help":
                jump seek_practical_help_branch

    label stand_ground_branch:
        #### Screen 16: Standing Firm
        #- **Setting**: Campus.
        #- **Description**: Amelia stands her ground against the bullies.
        #- **Dialogue**: "I'm not going to let you intimidate me."
        show chapter_3_screen_16
        with dissolve
        a "I'm not going to let you intimidate me."

        #### Screen 17: Bullies Intensify
        #- **Description**: The bullying intensifies.
        #- **Dialogue**: "You'll regret this."
        show chapter_3_screen_17
        with dissolve
        bullies "You'll regret this."

        menu:
            "Seek Help":
                jump seek_help_branch_2

            "Inner Strength":
                jump inner_strength_branch

    label avoidance_branch:
        #### Screen 16: Avoiding Confrontation
        #- **Setting**: Campus.
        #- **Description**: Amelia tries to avoid the bullies.
        #- **Dialogue**: "I'll just stay away from them."
        show chapter_3_screen_16_alt
        with dissolve
        a "I'll just stay away from them."

        #### Screen 17: Isolation
        #- **Description**: Amelia feels isolated and alone.
        #- **Dialogue**: "I feel so alone."
        show chapter_3_screen_17_alt
        with dissolve
        a "I feel so alone."

        menu:
            "Socialize":
                jump socialize_branch

            "Accept Isolation":
                jump accept_isolation_branch

    label follow_up_branch:
        #### Screen 16: Following Up with Dean
        #- **Setting**: Dean's office.
        #- **Description**: Amelia follows up with the dean.
        #- **Dialogue**: "Any updates on the bullying issue?"
        show chapter_3_screen_16_alt_2
        with dissolve
        a "Any updates on the bullying issue?"

        #### Screen 17: Dean's Support
        #- **Description**: The dean provides support and updates.
        #- **Dialogue**: "We've taken steps to address the issue."
        show chapter_3_screen_17_alt_2
        with dissolve
        dean "We've taken steps to address the issue."

        menu:
            "Advocate":
                jump advocate_branch

            "Personal Focus":
                jump personal_focus_branch

    label take_action_branch:
        #### Screen 16: Taking Immediate Action
        #- **Setting**: Campus.
        #- **Description**: Amelia decides to take action herself.
        #- **Dialogue**: "I need to address this immediately."
        show chapter_3_screen_16_alt_3
        with dissolve
        a "I need to address this immediately."

        #### Screen 17: Addressing the Issue
        #- **Description**: Amelia confronts the issue directly.
        #- **Dialogue**: "This has to stop now."
        show chapter_3_screen_17_alt_3
        with dissolve
        a "This has to stop now."

        menu:
            "Resolve":
                jump resolve_branch

            "Move On":
                jump move_on_branch

    label defensive_branch:
        #### Screen 16: Defending Self
        #- **Setting**: Campus.
        #- **Description**: Amelia defends herself against the bullies.
        #- **Dialogue**: "Leave me alone!"
        show chapter_3_screen_16_alt_4
        with dissolve
        a "Leave me alone!"

        #### Screen 17: Bullies' Reaction
        #- **Description**: The bullies back off.
        #- **Dialogue**: "Fine, we'll leave you alone."
        show chapter_3_screen_17_alt_4
        with dissolve
        bullies "Fine, we'll leave you alone."

        menu:
            "Seek Help":
                jump seek_help_branch_2

            "Inner Strength":
                jump inner_strength_branch

    label retreat_branch:
        #### Screen 16: Retreating to Safe Space
        #- **Setting**: Dorm room.
        #- **Description**: Amelia retreats to her dorm room for safety.
        #- **Dialogue**: "I need to stay safe."
        show chapter_3_screen_16_alt_5
        with dissolve
        a "I need to stay safe."

        #### Screen 17: Feeling Safe
        #- **Description**: Amelia feels a sense of safety in her dorm room.
        #- **Dialogue**: "At least I'm safe here."
        show chapter_3_screen_17_alt_5
        with dissolve
        a "At least I'm safe here."

        menu:
            "Seek Help":
                jump seek_help_branch_2

            "Inner Strength":
                jump inner_strength_branch

    label apply_wisdom_branch:
        #### Screen 16: Applying Philosophical Wisdom
        #- **Setting**: Campus.
        #- **Description**: Amelia applies the wisdom she learned.
        #- **Dialogue**: "I need to let the light in."
        show chapter_3_screen_16_alt_6
        with dissolve
        a "I need to let the light in."

        #### Screen 17: New Perspective
        #- **Description**: Amelia gains a new perspective on her situation.
        #- **Dialogue**: "I feel a bit better now."
        show chapter_3_screen_17_alt_6
        with dissolve
        a "I feel a bit better now."

        menu:
            "Seek Help":
                jump seek_help_branch_2

            "Inner Strength":
                jump inner_strength_branch

    label seek_practical_help_branch:
        #### Screen 16: Seeking Practical Help
        #- **Setting**: Mentor's office.
        #- **Description**: Amelia seeks practical help from her mentor.
        #- **Dialogue**: "I need your advice on dealing with bullying."
        show chapter_3_screen_16_alt_7
        with dissolve
        a "I need your advice on dealing with bullying."

        #### Screen 17: Mentor's Guidance
        #- **Description**: The mentor provides practical guidance.
        #- **Dialogue**: "Here's what you can do."
        show chapter_3_screen_17_alt_7
        with dissolve
        mentor "Here's what you can do."

        menu:
            "Follow Advice":
                jump follow_advice_branch

            "Forge Own Path":
                jump forge_own_path_branch

    label seek_help_branch_2:
        #### Screen 18: Seeking Further Help
        #- **Setting**: Counselor's office.
        #- **Description**: Amelia seeks further help from the counselor.
        #- **Dialogue**: "I need more help dealing with this."
        show chapter_3_screen_18
        with dissolve
        a "I need more help dealing with this."

        #### Screen 19: New Coping Strategies
        #- **Description**: The counselor offers new coping strategies.
        #- **Dialogue**: "Let's try these new strategies."
        show chapter_3_screen_19
        with dissolve
        counselor "Let's try these new strategies."

        #### Screen 20: Emotional Growth
        #- **Description**: Amelia experiences emotional growth.
        #- **Dialogue**: "I feel stronger now."
        show chapter_3_screen_20
        with dissolve
        a "I feel stronger now."

        jump ending_1

    label inner_strength_branch:
        #### Screen 18: Finding Inner Strength
        #- **Setting**: Campus.
        #- **Description**: Amelia finds inner strength to cope with the bullying.
        #- **Dialogue**: "I need to stay strong."
        show chapter_3_screen_18_alt
        with dissolve
        a "I need to stay strong."

        #### Screen 19: Developing Resilience
        #- **Description**: Amelia develops resilience.
        #- **Dialogue**: "I can handle this."
        show chapter_3_screen_19_alt
        with dissolve
        a "I can handle this."

        #### Screen 20: Resilient Mind
        #- **Description**: Amelia's mind becomes more resilient.
        #- **Dialogue**: "I feel more resilient now."
        show chapter_3_screen_20_alt
        with dissolve
        a "I feel more resilient now."

        jump ending_2

    label socialize_branch:
        #### Screen 18: Trying to Socialize
        #- **Setting**: Campus.
        #- **Description**: Amelia tries to socialize more to cope with loneliness.
        #- **Dialogue**: "I should try to make more friends."
        show chapter_3_screen_18_alt_2
        with dissolve
        a "I should try to make more friends."

        #### Screen 19: Socializing Attempt
        #- **Description**: Amelia attempts to socialize with other students.
        #- **Dialogue**: "Hi, I'm Amelia."
        show chapter_3_screen_19_alt_2
        with dissolve
        a "Hi, I'm Amelia."

        #### Screen 20: Social Success
        #- **Description**: Amelia successfully makes new friends.
        #- **Dialogue**: "I feel more connected now."
        show chapter_3_screen_20_alt_2
        with dissolve
        a "I feel more connected now."

        jump ending_3

    label accept_isolation_branch:
        #### Screen 18: Accepting Isolation
        #- **Setting**: Dorm room.
        #- **Description**: Amelia accepts her isolation.
        #- **Dialogue**: "Maybe being alone isn't so bad."
        show chapter_3_screen_18_alt_3
        with dissolve
        a "Maybe being alone isn't so bad."

        #### Screen 19: Reflecting on Isolation
        #- **Description**: Amelia reflects on her isolation.
        #- **Dialogue**: "I can use this time for self-discovery."
        show chapter_3_screen_19_alt_3
        with dissolve
        a "I can use this time for self-discovery."

        #### Screen 20: Solitude
        #- **Description**: Amelia finds peace in solitude.
        #- **Dialogue**: "I feel at peace now."
        show chapter_3_screen_20_alt_3
        with dissolve
        a "I feel at peace now."

        jump ending_4

    label advocate_branch:
        #### Screen 18: Becoming an Advocate
        #- **Setting**: Campus.
        #- **Description**: Amelia decides to advocate for change.
        #- **Dialogue**: "I need to speak up about this."
        show chapter_3_screen_18_alt_4
        with dissolve
        a "I need to speak up about this."

        #### Screen 19: Advocating for Change
        #- **Description**: Amelia advocates for change on campus.
        #- **Dialogue**: "We need to address this issue."
        show chapter_3_screen_19_alt_4
        with dissolve
        a "We need to address this issue."

        #### Screen 20: Advocate for Change
        #- **Description**: Amelia becomes a strong advocate for change.
        #- **Dialogue**: "I feel empowered now."
        show chapter_3_screen_20_alt_4
        with dissolve
        a "I feel empowered now."

        jump ending_5

    label personal_focus_branch:
        #### Screen 18: Focusing on Self
        #- **Setting**: Dorm room.
        #- **Description**: Amelia decides to focus on herself.
        #- **Dialogue**: "I need to focus on my own growth."
        show chapter_3_screen_18_alt_5
        with dissolve
        a "I need to focus on my own growth."

        #### Screen 19: Personal Growth
        #- **Description**: Amelia experiences personal growth.
        #- **Dialogue**: "I feel more fulfilled now."
        show chapter_3_screen_19_alt_5
        with dissolve
        a "I feel more fulfilled now."

        #### Screen 20: Personal Fulfillment
        #- **Description**: Amelia finds personal fulfillment.
        #- **Dialogue**: "I feel fulfilled."
        show chapter_3_screen_20_alt_5
        with dissolve
        a "I feel fulfilled."

        jump ending_6

    label resolve_branch:
        #### Screen 18: Resolving Conflict
        #- **Setting**: Campus.
        #- **Description**: Amelia works to resolve the conflict.
        #- **Dialogue**: "We need to resolve this."
        show chapter_3_screen_18_alt_6
        with dissolve
        a "We need to resolve this."

        #### Screen 19: Resolving Issues
        #- **Description**: Amelia resolves the issues with the bullies.
        #- **Dialogue**: "We came to an understanding."
        show chapter_3_screen_19_alt_6
        with dissolve
        a "We came to an understanding."

        #### Screen 20: Conflict Resolution
        #- **Description**: Amelia successfully resolves the conflict.
        #- **Dialogue**: "I feel at peace now."
        show chapter_3_screen_20_alt_6
        with dissolve
        a "I feel at peace now."

        jump ending_7

    label move_on_branch:
        #### Screen 18: Moving On
        #- **Setting**: Campus.
        #- **Description**: Amelia decides to move on from the situation.
        #- **Dialogue**: "I need to move on."
        show chapter_3_screen_18_alt_7
        with dissolve
        a "I need to move on."

        #### Screen 19: Moving Forward
        #- **Description**: Amelia moves forward with her life.
        #- **Dialogue**: "I'm moving forward."
        show chapter_3_screen_19_alt_7
        with dissolve
        a "I'm moving forward."

        #### Screen 20: New Beginnings
        #- **Description**: Amelia finds new beginnings.
        #- **Dialogue**: "This is a fresh start."
        show chapter_3_screen_20_alt_7
        with dissolve
        a "This is a fresh start."

        jump ending_8

    label follow_advice_branch:
        #### Screen 18: Following Mentor's Advice
        #- **Setting**: Campus.
        #- **Description**: Amelia follows her mentor's advice.
        #- **Dialogue**: "I'll follow your advice."
        show chapter_3_screen_18_alt_8
        with dissolve
        a "I'll follow your advice."

        #### Screen 19: Mentor's Path
        #- **Description**: Amelia follows the path set by her mentor.
        #- **Dialogue**: "This is the right path for me."
        show chapter_3_screen_19_alt_8
        with dissolve
        a "This is the right path for me."

        #### Screen 20: Mentor's Path
        #- **Description**: Amelia finds success following her mentor's guidance.
        #- **Dialogue**: "Thank you for your guidance."
        show chapter_3_screen_20_alt_8
        with dissolve
        a "Thank you for your guidance."

        jump ending_9

    label forge_own_path_branch:
        #### Screen 18: Forging Own Path
        #- **Setting**: Campus.
        #- **Description**: Amelia decides to forge her own path.
        #- **Dialogue**: "I need to find my own way."
        show chapter_3_screen_18_alt_9
        with dissolve
        a "I need to find my own way."

        #### Screen 19: Personal Path
        #- **Description**: Amelia forges her own path.
        #- **Dialogue**: "This is my journey."
        show chapter_3_screen_19_alt_9
        with dissolve
        a "This is my journey."

        #### Screen 20: Own Path
        #- **Description**: Amelia finds success forging her own path.
        #- **Dialogue**: "I'm proud of myself."
        show chapter_3_screen_20_alt_9
        with dissolve
        a "I'm proud of myself."

        jump ending_10

    label ending_1:
        #### Ending 1: Empowered
        #- **Setting**: Campus.
        #- **Description**: Amelia feels empowered by her emotional growth.
        #- **Dialogue**: "I am stronger now."
        show chapter_3_ending_1
        with dissolve
        a "I am stronger now."

        return

    label ending_2:
        #### Ending 2: Resilient
        #- **Setting**: Campus.
        #- **Description**: Amelia feels resilient after developing inner strength.
        #- **Dialogue**: "I can handle anything."
        show chapter_3_ending_2
        with dissolve
        a "I can handle anything."

        return

    label ending_3:
        #### Ending 3: Social Success
        #- **Setting**: Campus.
        #- **Description**: Amelia feels socially successful after making new friends.
        #- **Dialogue**: "I feel connected and supported."
        show chapter_3_ending_3
        with dissolve
        a "I feel connected and supported."

        return

    label ending_4:
        #### Ending 4: Solitude
        #- **Setting**: Campus.
        #- **Description**: Amelia finds peace in solitude.
        #- **Dialogue**: "Solitude has its own beauty."
        show chapter_3_ending_4
        with dissolve
        a "Solitude has its own beauty."

        return

    label ending_5:
        #### Ending 5: Advocate
        #- **Setting**: Campus.
        #- **Description**: Amelia becomes a strong advocate for change.
        #- **Dialogue**: "I will continue to fight for justice."
        show chapter_3_ending_5
        with dissolve
        a "I will continue to fight for justice."

        return

    label ending_6:
        #### Ending 6: Fulfilled
        #- **Setting**: Campus.
        #- **Description**: Amelia finds personal fulfillment.
        #- **Dialogue**: "I am content with my growth."
        show chapter_3_ending_6
        with dissolve
        a "I am content with my growth."

        return

    label ending_7:
        #### Ending 7: Resolver
        #- **Setting**: Campus.
        #- **Description**: Amelia successfully resolves conflicts.
        #- **Dialogue**: "Conflict resolution is a valuable skill."
        show chapter_3_ending_7
        with dissolve
        a "Conflict resolution is a valuable skill."

        return

    label ending_8:
        #### Ending 8: New Beginnings
        #- **Setting**: Campus.
        #- **Description**: Amelia embraces new beginnings.
        #- **Dialogue**: "I am ready for a fresh start."
        show chapter_3_ending_8
        with dissolve
        a "I am ready for a fresh start."

        return

    label ending_9:
        #### Ending 9: Mentor's Path
        #- **Setting**: Campus.
        #- **Description**: Amelia finds success following her mentor's guidance.
        #- **Dialogue**: "Mentorship has guided me well."
        show chapter_3_ending_9
        with dissolve
        a "Mentorship has guided me well."

        return

    label ending_10:
        #### Ending 10: Own Path
        #- **Setting**: Campus.
        #- **Description**: Amelia finds success forging her own path.
        #- **Dialogue**: "I am proud of my journey."
        show chapter_3_ending_10
        with dissolve
        a "I am proud of my journey."

        return
