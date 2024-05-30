# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Amelia")
define e = Character("Ella")
define j = Character("James")
define p = Character("Parents")
define n = Character("Narrator")
define s = Character("Student")
define prof_Williams = Character("Prof. Williams")
define music.chapter_0_2 = "chapter_0_2.mp3"
define music.chapter_1 = "chapter_1.mp3"
define music.chapter_2 = "chapter_2.mp3"

# Variables to track choices and scores
default positive_psychology_score = 0
default family_systems_score = 0

# The game starts here.

label start_alt_2:
    play music chapter_0_2 fadein 1.0 volume 0.1
    scene chapter_0
    with dissolve

    pause 4.0

    scene screen_m3
    with dissolve
    n "Amelia's curiosity about the mind began in a room of dreams and playful experiments."

    scene screen_m2
    with dissolve
    n "High school was a theater of emotions and social hierarchies; a ripe field for observation."

    scene screen_m1
    with dissolve
    n "University, a beacon of hope, promising a sanctuary where curiosity intertwines with opportunity."

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

    #### Screen 3: Player Choice: Share the News
    #- **Description**: The player decides who Amelia will share the news with first.
    menu:
        "Tell Ella first":
            $ positive_psychology_score += 1
            jump tell_ella_first
        "Tell Parents first":
            $ family_systems_score += 1
            jump tell_parents_first

label tell_ella_first:
    #### Screen 4: Telling Ella
    #- **Setting**: Amelia's room, on the phone with Ella.
    #- **Dialogue**: "Ella, guess what? I got accepted!"
    show chapter_1_screen_3
    with dissolve
    a "Ella, guess what? I got accepted!"
    e "No way! That's amazing, Amelia! I'm so proud of you!"

    #### Screen 5: Ella's Support
    #- **Setting**: Split screen showing Ella at her home, excited and happy for Amelia.
    #- **Dialogue**: "This is just the beginning. You're going to do great things."
    show chapter_1_screen_4
    with dissolve
    e "This is just the beginning. You're going to do great things."
    a "I hope so, Ella. I'm nervous but excited."
    jump after_choice

label tell_parents_first:
    #### Screen 4: Parent's Reaction
    #- **Setting**: Living room, Amelia sharing the news with her parents.
    #- **Dialogue**: "Mom, Dad, I got accepted into Plymouth University!"
    show chapter_1_screen_5
    with dissolve
    a "Mom, Dad, I got accepted into Plymouth University!"
    p "We're so proud of you, Amelia. We knew you could do it!"
    j "You've worked so hard for this. You deserve it."
    jump after_choice

label after_choice:
    #### Screen 6: Family Celebration
    #- **Setting**: Family hugging and celebrating together.
    #- **Dialogue**: "This calls for a celebration dinner tonight!"
    show chapter_1_screen_6
    with dissolve
    p "This calls for a celebration dinner tonight!"
    a "Thank you, everyone. I'm so happy!"

    #### Screen 7: Reflection
    #- **Setting**: Amelia alone in her room, reflecting on her future.
    #- **Dialogue**: "This is it, a new chapter. I can't wait to see what's ahead."
    show chapter_1_screen_7
    with dissolve
    a "This is it, a new chapter. I can't wait to see what's ahead."
    n "Amelia's thoughts wandered to the new experiences awaiting her in Plymouth."

    #### Screen 8: A Quiet Moment
    #- **Setting**: Amelia's backyard, sitting on a swing, looking at the sky.
    #- **Dialogue**: "I wonder what new friends I'll make. Will it be as hard as they say?"
    show chapter_1_screen_8
    with dissolve
    a "I wonder what new friends I'll make. Will it be as hard as they say?"
    n "The sky was clear, a vast expanse mirroring her future's uncertainty."

    #### Screen 9: Packing for Plymouth
    #- **Setting**: Amelia's room, packing her things.
    #- **Dialogue**: "Books, clothes, my journal... What else do I need?"
    show chapter_1_screen_9
    with dissolve
    a "Books, clothes, my journal... What else do I need?"
    n "Amelia's room was a mix of nostalgia and anticipation."

    #### Screen 10: Packing - Memory Lane
    #- **Setting**: Amelia finds an old photo album.
    #- **Dialogue**: "Oh, these memories... high school, family trips..."
    show chapter_1_screen_10
    with dissolve
    a "Oh, these memories... high school, family trips..."
    n "Every photo told a story, a chapter of her life in London."

    #### Screen 11: Packing - A Special Keepsake
    #- **Setting**: Amelia finds a special keepsake from her childhood.
    #- **Dialogue**: "My old diary. I should take this with me."
    show chapter_1_screen_11
    with dissolve
    a "My old diary. I should take this with me."
    n "The diary held secrets, dreams, and hopes of a younger Amelia."

    #### Screen 12: Neighborhood Walk - Reflection
    #- **Setting**: Amelia's neighborhood, walking around for the last time before leaving.
    #- **Dialogue**: "I'll miss this place, but it's time for new adventures."
    show chapter_1_screen_12
    with dissolve
    a "I'll miss this place, but it's time for new adventures."
    n "Every corner held a memory, every street a story."

    #### Screen 13: Neighborhood Walk - Childhood Park
    #- **Setting**: The local park where Amelia played as a child.
    #- **Dialogue**: "I remember playing here every weekend. Such good times."
    show chapter_1_screen_13
    with dissolve
    a "I remember playing here every weekend. Such good times."
    n "The swings, the slides, they all held echoes of her laughter."

    #### Screen 14: Neighborhood Walk - Old Friends
    #- **Setting**: Running into an old friend from school.
    #- **Dialogue**: "Hey, Amelia! Long time no see. Heard you're off to Plymouth?"
    show chapter_1_screen_14
    with dissolve
    s "Hey, Amelia! Long time no see. Heard you're off to Plymouth?"
    a "Yeah! Just got my acceptance letter. I'm really excited."
    s "That's amazing! You'll do great. Keep in touch!"

    #### Screen 15: Farewell to Ella - Meeting
    #- **Setting**: Park where Amelia and Ella meet for the last time before Amelia leaves.
    #- **Dialogue**: "I'll miss you, Ella. Keep in touch, okay?"
    show chapter_1_screen_15
    with dissolve
    a "I'll miss you, Ella. Keep in touch, okay?"
    e "Of course, Amelia. Go out there and make us proud."

    #### Screen 16: Farewell to Ella - Memories
    #- **Setting**: Amelia and Ella reminiscing about their school days.
    #- **Dialogue**: "Remember that time we got lost on the school trip?"
    show chapter_1_screen_16
    with dissolve
    a "Remember that time we got lost on the school trip?"
    e "Oh my god, yes! We were so scared but it turned out to be so much fun."

    #### Screen 17: Farewell to Ella - Gifts
    #- **Setting**: Ella gives Amelia a small gift.
    #- **Dialogue**: "Here, I got you something. A little reminder of home."
    show chapter_1_screen_17
    with dissolve
    e "Here, I got you something. A little reminder of home."
    a "Thank you, Ella. This means so much to me."

    #### Screen 18: Farewell to Ella - Promises
    #- **Setting**: Making promises to stay in touch.
    #- **Dialogue**: "Promise me we'll video call every week."
    show chapter_1_screen_18
    with dissolve
    a "Promise me we'll video call every week."
    e "Absolutely. I wouldn't miss it for the world."

    #### Screen 19: Family Dinner - Preparation
    #- **Setting**: Family dinner table, preparing for the meal.
    #- **Dialogue**: "Can you pass the salad, please?"
    show chapter_1_screen_19
    with dissolve
    p "Can you pass the salad, please?"
    a "Here you go, Mom."

    #### Screen 20: Family Dinner - Conversation
    #- **Setting**: Family dinner, discussing Amelia's plans.
    #- **Dialogue**: "What are you most excited about for university, Amelia?"
    show chapter_1_screen_20
    with dissolve
    j "What are you most excited about for university, Amelia?"
    a "Meeting new people and learning new things. It's going to be amazing."

    #### Screen 21: Family Dinner - Toast
    #- **Setting**: Family making a toast.
    #- **Dialogue**: "To Amelia, for her bright future!"
    show chapter_1_screen_21
    with dissolve
    p "To Amelia, for her bright future!"
    a "Thank you, everyone. I'll make you all proud."

    #### Screen 22: Last Night at Home - Packing Final Items
    #- **Setting**: Amelia's bedroom, lights dim, her packing almost done.
    #- **Dialogue**: "This is really happening. Tomorrow, everything changes."
    show chapter_1_screen_22
    with dissolve
    a "This is really happening. Tomorrow, everything changes."
    n "The room felt different, like a chapter closing."

    #### Screen 23: Last Night at Home - Family Chat
    #- **Setting**: Living room, last chat with family before bed.
    #- **Dialogue**: "We're going to miss you so much, Amelia."
    show chapter_1_screen_23
    with dissolve
    p "We're going to miss you so much, Amelia."
    a "I'll miss you all too. But I'll visit often."

    #### Screen 24: Departure Morning - Breakfast
    #- **Setting**: Morning, Amelia having breakfast with her family.
    #- **Dialogue**: "I'll call as soon as I get there."
    show chapter_1_screen_24
    with dissolve
    a "I'll call as soon as I get there."
    p "We'll be waiting. Take care, sweetheart."

    #### Screen 25: Departure Morning - Final Goodbyes
    #- **Setting**: At the door, hugging her parents goodbye.
    #- **Dialogue**: "I love you all. Thank you for everything."
    show chapter_1_screen_25
    with dissolve
    a "I love you all. Thank you for everything."
    p "We love you too, Amelia. Go make your dreams come true."

    #### Screen 26: The Car Ride - Reflections
    #- **Setting**: Amelia's family car, driving to the train station.
    #- **Dialogue**: "I can't believe this day has come."
    show chapter_1_screen_26
    with dissolve
    a "I can't believe this day has come."
    p "It's a big step, Amelia. We're so proud of you."

    #### Screen 27: The Car Ride - Conversations
    #- **Setting**: In the car, talking with her parents.
    #- **Dialogue**: "Do you have everything you need?"
    show chapter_1_screen_27
    with dissolve
    j "Do you have everything you need?"
    a "I think so, Dad. I'm ready."

    #### Screen 28: The Car Ride - Last Minute Advice
    #- **Setting**: Parents giving last minute advice.
    #- **Dialogue**: "Remember to stay focused and work hard."
    show chapter_1_screen_28
    with dissolve
    p "Remember to stay focused and work hard."
    a "I will, Mom. I promise."

    #### Screen 29: At the Train Station - Arrival
    #- **Setting**: Train station, Amelia and her family standing by the platform.
    #- **Dialogue**: "I'll miss you all so much."
    show chapter_1_screen_29
    with dissolve
    a "I'll miss you all so much."
    p "We'll miss you too, Amelia. Be safe and enjoy your time."

    #### Screen 30: At the Train Station - Final Hugs
    #- **Setting**: Hugging her parents goodbye.
    #- **Dialogue**: "Take care, Amelia. We're so proud of you."
    show chapter_1_screen_30
    with dissolve
    p "Take care, Amelia. We're so proud of you."
    a "Thank you, Dad. I'll make you proud."

    #### Screen 31: Boarding the Train
    #- **Setting**: Amelia boarding the train.
    #- **Dialogue**: "Goodbye, London. Hello, new beginnings."
    show chapter_1_screen_31
    with dissolve
    a "Goodbye, London. Hello, new beginnings."
    n "The train's whistle marked the start of a new journey."

    #### Screen 32: On the Train - Window Seat
    #- **Setting**: Amelia looking out the window as the train departs.
    #- **Dialogue**: "Plymouth, here I come."
    show chapter_1_screen_32
    with dissolve
    a "Plymouth, here I come."
    n "The cityscape of London slowly gave way to the countryside."

    #### Screen 33: On the Train - Reflections
    #- **Setting**: Amelia reflecting on her journey ahead.
    #- **Dialogue**: "I wonder what challenges and adventures await me."
    show chapter_1_screen_33
    with dissolve
    a "I wonder what challenges and adventures await me."
    n "Excitement and nerves danced within her."

    #### Screen 34: On the Train - Texting Ella
    #- **Setting**: Amelia texting Ella from the train.
    #- **Dialogue**: "Just left. Can't wait to tell you all about it."
    show chapter_1_screen_34
    with dissolve
    a "Just left. Can't wait to tell you all about it."
    e "Safe travels, Amelia! You're going to be amazing!"

    #### Screen 35: On the Train - Journaling
    #- **Setting**: Amelia writing in her journal.
    #- **Dialogue**: "Day 1: Leaving home, stepping into the unknown."
    show chapter_1_screen_35
    with dissolve
    a "Day 1: Leaving home, stepping into the unknown."
    n "Her journal would be her confidant, her witness to this new chapter."

    #### Screen 36: On the Train - Reading a Book
    #- **Setting**: Amelia reading a psychology book.
    #- **Dialogue**: "The human mind is so fascinating. I can't wait to learn more."
    show chapter_1_screen_36
    with dissolve
    a "The human mind is so fascinating. I can't wait to learn more."
    n "Knowledge and curiosity were her companions on this journey."

    #### Screen 37: On the Train - Scenic Views
    #- **Setting**: Amelia admiring the scenic views from the train.
    #- **Dialogue**: "The countryside is beautiful. Such a change from the city."
    show chapter_1_screen_37
    with dissolve
    a "The countryside is beautiful. Such a change from the city."
    n "Rolling hills and open fields stretched out before her."

    #### Screen 38: On the Train - Daydreaming
    #- **Setting**: Amelia lost in thought.
    #- **Dialogue**: "What will my first day at university be like?"
    show chapter_1_screen_38
    with dissolve
    a "What will my first day at university be like?"
    n "Questions and dreams filled her mind."

    #### Screen 39: On the Train - Fellow Passengers
    #- **Setting**: Amelia observing other passengers.
    #- **Dialogue**: "I wonder where everyone else is going."
    show chapter_1_screen_39
    with dissolve
    a "I wonder where everyone else is going."
    n "Each passenger a mystery, each journey a story."

    #### Screen 40: On the Train - Snack Time
    #- **Setting**: Amelia having a snack on the train.
    #- **Dialogue**: "A quick bite before I reach Plymouth."
    show chapter_1_screen_40
    with dissolve
    a "A quick bite before I reach Plymouth."
    n "She savored the simple moments, grounding herself in the present."

    #### Screen 41: On the Train - Anticipation
    #- **Setting**: Amelia feeling a mix of excitement and anxiety.
    #- **Dialogue**: "Almost there. I can do this."
    show chapter_1_screen_41
    with dissolve
    a "Almost there. I can do this."
    n "Her heart raced with anticipation."

    #### Screen 42: Arriving at Plymouth - Train Announcement
    #- **Setting**: Train speaker announcing the arrival.
    #- **Dialogue**: "Next stop, Plymouth."
    show chapter_1_screen_42
    with dissolve
    n "Next stop, Plymouth."

    #### Screen 43: Arriving at Plymouth - Gathering Belongings
    #- **Setting**: Amelia gathering her belongings.
    #- **Dialogue**: "Here we go. Time to step into my new life."
    show chapter_1_screen_43
    with dissolve
    a "Here we go. Time to step into my new life."
    n "She took a deep breath, ready for what lay ahead."

    #### Screen 44: Arriving at Plymouth - Stepping Off the Train
    #- **Setting**: Amelia stepping off the train.
    #- **Dialogue**: "Plymouth, I'm here."
    show chapter_1_screen_44
    with dissolve
    a "Plymouth, I'm here."
    n "The air felt different, filled with possibilities."

    #### Screen 45: Arriving at Plymouth - Looking Around
    #- **Setting**: Amelia looking around the Plymouth train station.
    #- **Dialogue**: "This is it. A new beginning."
    show chapter_1_screen_45
    with dissolve
    a "This is it. A new beginning."
    n "The station buzzed with activity, a gateway to her new world."

    #### Screen 46: Arriving at Plymouth - Finding Her Way
    #- **Setting**: Amelia navigating through the station.
    #- **Dialogue**: "Let's find a taxi to the university."
    show chapter_1_screen_46
    with dissolve
    a "Let's find a taxi to the university."
    n "She moved with purpose, ready to embrace her journey."

    #### Screen 47: Arriving at Plymouth - Taxi Ride
    #- **Setting**: Amelia in a taxi, heading to the university.
    #- **Dialogue**: "Plymouth University, please."
    show chapter_1_screen_47
    with dissolve
    a "Plymouth University, please."
    n "The city unfolded before her, a blend of old and new."

    #### Screen 48: Arriving at Plymouth - First Impressions
    #- **Setting**: Amelia observing the city from the taxi.
    #- **Dialogue**: "This place is beautiful. I can't wait to explore."
    show chapter_1_screen_48
    with dissolve
    a "This place is beautiful. I can't wait to explore."
    n "Every turn revealed a new aspect of her future home."

    #### Screen 49: Arriving at Plymouth - Arrival at University
    #- **Setting**: The taxi arrives at Plymouth University.
    #- **Dialogue**: "Thank you. Here we go."
    show chapter_1_screen_49
    with dissolve
    a "Thank you. Here we go."
    n "The university loomed ahead, a place of learning and growth."

    #### Screen 50: Arriving at Plymouth - Stepping Onto Campus
    #- **Setting**: Amelia stepping onto the university campus.
    #- **Dialogue**: "I'm ready. Let's do this."
    show chapter_1_screen_50
    with dissolve
    a "I'm ready. Let's do this."
    n "Her journey had just begun, filled with endless possibilities."

    return

label new_beginnings:
    play music chapter_2 fadein 1.0 volume 0.1
    scene chapter_2
    with dissolve

    #### Screen 1: First Day at University
    #- **Setting**: Plymouth University campus, Amelia walking around.
    #- **Dialogue**: "This place is huge... and beautiful."
    show chapter_2_screen_1
    with dissolve
    a "This place is huge... and beautiful."
    n "Amelia's heart raced with excitement as she explored her new surroundings."

    #### Screen 2: Orientation
    #- **Setting**: University hall, orientation session for new students.
    #- **Dialogue**: "Welcome to Plymouth University! We're excited to have you here."
    show chapter_2_screen_2
    with dissolve
    prof_Williams "Welcome to Plymouth University! We're excited to have you here."
    n "The hall was filled with new faces, each brimming with anticipation."

    #### Screen 3: Orientation Speech
    #- **Setting**: Professor Williams giving an orientation speech.
    #- **Dialogue**: "This is the beginning of an incredible journey. Embrace every moment."
    show chapter_2_screen_3
    with dissolve
    prof_Williams "This is the beginning of an incredible journey. Embrace every moment."
    a "I can't believe I'm finally here."

    #### Screen 4: Exploring Campus
    #- **Setting**: Amelia exploring the campus, spotting Zara sitting alone.
    #- **Dialogue**: "Hi, do you mind if I sit here?"
    show chapter_2_screen_4
    with dissolve
    a "Hi, do you mind if I sit here?"
    z "Not at all. I'm Zara. Nice to meet you."
    a "I'm Amelia. Nice to meet you too."

    #### Screen 5: Player Choice: Befriend Zara or Lucas
    menu:
        "Befriend Zara":
            $ family_systems_score += 1
            jump befriend_zara
        "Befriend Lucas":
            $ jungian_psychology_score += 1
            jump befriend_lucas

label befriend_zara:
    #### Screen 6: Conversation with Zara
    #- **Setting**: Amelia and Zara chatting about their backgrounds.
    #- **Dialogue**: "Where are you from, Zara?"
    show chapter_2_screen_5
    with dissolve
    a "Where are you from, Zara?"
    z "I was born in India but grew up here. What about you?"
    a "I'm from London. Excited to be here."

    #### Screen 7: Discussing University Life
    #- **Setting**: Amelia and Zara discussing their excitement and fears.
    #- **Dialogue**: "I'm a bit nervous about fitting in."
    show chapter_2_screen_6
    with dissolve
    a "I'm a bit nervous about fitting in."
    z "Me too, but I think we'll be okay. This place seems welcoming."

    #### Screen 8: Shared Interests
    #- **Setting**: Amelia and Zara finding common interests.
    #- **Dialogue**: "I love reading about psychology. It's so fascinating."
    show chapter_2_screen_7
    with dissolve
    a "I love reading about psychology. It's so fascinating."
    z "Me too! I want to understand how people's minds work."

    #### Screen 9: First Class Together
    #- **Setting**: Amelia and Zara attending their first psychology class.
    #- **Dialogue**: "This is so exciting. Our first class!"
    show chapter_2_screen_8
    with dissolve
    a "This is so exciting. Our first class!"
    z "I know! I can't wait to get started."

    #### Screen 10: Professor's Introduction
    #- **Setting**: The professor introduces the course.
    #- **Dialogue**: "Welcome to Psychology 101. I'm Professor Williams."
    show chapter_2_screen_9
    with dissolve
    prof_Williams "Welcome to Psychology 101. I'm Professor Williams."

    #### Screen 11: Class Interaction
    #- **Setting**: Professor asking questions to the class.
    #- **Dialogue**: "Can anyone tell me what psychology means to them?"
    show chapter_2_screen_10
    with dissolve
    prof_Williams "Can anyone tell me what psychology means to them?"
    a "It's the study of the mind and behavior."

    #### Screen 12: After Class Discussion
    #- **Setting**: Amelia and Zara discussing the class.
    #- **Dialogue**: "That was a great class. I learned so much already."
    show chapter_2_screen_11
    with dissolve
    a "That was a great class. I learned so much already."
    z "Me too! I'm really excited about this course."

    #### Screen 13: Lunch Break
    #- **Setting**: Amelia and Zara having lunch together.
    #- **Dialogue**: "Let's grab something to eat. I'm starving."
    show chapter_2_screen_12
    with dissolve
    a "Let's grab something to eat. I'm starving."
    z "Good idea. There's a nice café nearby."

    #### Screen 14: Discussing Cultural Differences
    #- **Setting**: Café, discussing their cultural backgrounds.
    #- **Dialogue**: "Tell me more about your culture, Zara."
    show chapter_2_screen_13
    with dissolve
    a "Tell me more about your culture, Zara."
    z "It's rich and diverse. There are so many festivals and traditions."

    #### Screen 15: Understanding Racism
    #- **Setting**: Zara sharing her experiences with racism.
    #- **Dialogue**: "I've faced some challenges because of my background."
    show chapter_2_screen_14
    with dissolve
    z "I've faced some challenges because of my background."
    a "I'm sorry to hear that. It's unfair."

    #### Screen 16: Bonding Over Stories
    #- **Setting**: Amelia and Zara bonding over shared stories.
    #- **Dialogue**: "It's great to have someone to talk to about these things."
    show chapter_2_screen_15
    with dissolve
    a "It's great to have someone to talk to about these things."
    z "I agree. I'm glad we met."

    #### Screen 17: Exploring the Campus
    #- **Setting**: Amelia and Zara exploring the campus together.
    #- **Dialogue**: "Let's check out the library. I heard it's amazing."
    show chapter_2_screen_16
    with dissolve
    a "Let's check out the library. I heard it's amazing."
    z "Sure! I'm always up for a good book."

    #### Screen 18: Library Tour
    #- **Setting**: Campus library, looking around.
    #- **Dialogue**: "Wow, this place is huge. So many books!"
    show chapter_2_screen_17
    with dissolve
    a "Wow, this place is huge. So many books!"
    z "I think I'm going to spend a lot of time here."

    #### Screen 19: Finding Study Spots
    #- **Setting**: Finding quiet spots to study in the library.
    #- **Dialogue**: "This corner looks perfect for studying."
    show chapter_2_screen_18
    with dissolve
    a "This corner looks perfect for studying."
    z "Agreed. It's quiet and has a great view."

    #### Screen 20: First Assignment
    #- **Setting**: Professor Williams giving the first assignment.
    #- **Dialogue**: "Your first assignment is due next week. Start working on it early."
    show chapter_2_screen_19
    with dissolve
    prof_Williams "Your first assignment is due next week. Start working on it early."
    n "The students quickly noted down the assignment details."

    #### Screen 21: Study Group
    #- **Setting**: Amelia and Zara decide to form a study group.
    #- **Dialogue**: "Let's form a study group to help each other out."
    show chapter_2_screen_20
    with dissolve
    a "Let's form a study group to help each other out."
    z "Great idea! We can meet here every day."

    jump after_choice

label befriend_lucas:
    #### Screen 6: Meeting Lucas
    #- **Setting**: Amelia exploring the campus, meeting Lucas in the library.
    #- **Dialogue**: "Hi, I'm Lucas. Mind if I join you?"
    show chapter_2_screen_21
    with dissolve
    l "Hi, I'm Lucas. Mind if I join you?"
    a "Not at all. I'm Amelia. Nice to meet you."

    #### Screen 7: Early Discussions
    #- **Setting**: Lucas sharing his interest in Jungian psychology.
    #- **Dialogue**: "I'm really interested in dreams and the subconscious."
    show chapter_2_screen_22
    with dissolve
    l "I'm really interested in dreams and the subconscious."
    a "That sounds fascinating. I'd love to learn more."

    #### Screen 8: Lucas' Perspective
    #- **Setting**: Lucas explaining Jungian psychology.
    #- **Dialogue**: "Jung believed that dreams reveal hidden aspects of ourselves."
    show chapter_2_screen_23
    with dissolve
    l "Jung believed that dreams reveal hidden aspects of ourselves."
    a "I've never thought of it that way. That's interesting."

    #### Screen 9: Dream Analysis
    #- **Setting**: Lucas offering to analyze their dreams.
    #- **Dialogue**: "If you ever want to talk about your dreams, let me know."
    show chapter_2_screen_24
    with dissolve
    l "If you ever want to talk about your dreams, let me know."
    a "Thanks, Lucas. I might take you up on that."

    #### Screen 10: First Class Together
    #- **Setting**: Amelia and Lucas attending their first psychology class.
    #- **Dialogue**: "This is so exciting. Our first class!"
    show chapter_2_screen_25
    with dissolve
    a "This is so exciting. Our first class!"
    l "I know! I can't wait to get started."

    #### Screen 11: Professor's Introduction
    #- **Setting**: The professor introduces the course.
    #- **Dialogue**: "Welcome to Psychology 101. I'm Professor Williams."
    show chapter_2_screen_26
    with dissolve
    prof_Williams "Welcome to Psychology 101. I'm Professor Williams."

    #### Screen 12: Class Interaction
    #- **Setting**: Professor asking questions to the class.
    #- **Dialogue**: "Can anyone tell me what psychology means to them?"
    show chapter_2_screen_27
    with dissolve
    prof_Williams "Can anyone tell me what psychology means to them?"
    a "It's the study of the mind and behavior."

    #### Screen 13: After Class Discussion
    #- **Setting**: Amelia and Lucas discussing the class.
    #- **Dialogue**: "That was a great class. I learned so much already."
    show chapter_2_screen_28
    with dissolve
    a "That was a great class. I learned so much already."
    l "Me too! I'm really excited about this course."

    #### Screen 14: Lunch Break
    #- **Setting**: Amelia and Lucas having lunch together.
    #- **Dialogue**: "Let's grab something to eat. I'm starving."
    show chapter_2_screen_29
    with dissolve
    a "Let's grab something to eat. I'm starving."
    l "Good idea. There's a nice café nearby."

    #### Screen 15: Discussing Interests
    #- **Setting**: Café, discussing their interests.
    #- **Dialogue**: "I love reading about psychology. It's so fascinating."
    show chapter_2_screen_30
    with dissolve
    a "I love reading about psychology. It's so fascinating."
    l "Me too! I want to understand how people's minds work."

    #### Screen 16: Shared Interests
    #- **Setting**: Amelia and Lucas finding common interests.
    #- **Dialogue**: "I've always been interested in how dreams work."
    show chapter_2_screen_31
    with dissolve
    a "I've always been interested in how dreams work."
    l "Dreams can tell us so much about ourselves."

    #### Screen 17: Exploring the Campus
    #- **Setting**: Amelia and Lucas exploring the campus together.
    #- **Dialogue**: "Let's check out the library. I heard it's amazing."
    show chapter_2_screen_32
    with dissolve
    a "Let's check out the library. I heard it's amazing."
    l "Sure! I'm always up for a good book."

    #### Screen 18: Library Tour
    #- **Setting**: Campus library, looking around.
    #- **Dialogue**: "Wow, this place is huge. So many books!"
    show chapter_2_screen_33
    with dissolve
    a "Wow, this place is huge. So many books!"
    l "I think I'm going to spend a lot of time here."

    #### Screen 19: Finding Study Spots
    #- **Setting**: Finding quiet spots to study in the library.
    #- **Dialogue**: "This corner looks perfect for studying."
    show chapter_2_screen_34
    with dissolve
    a "This corner looks perfect for studying."
    l "Agreed. It's quiet and has a great view."

    #### Screen 20: First Assignment
    #- **Setting**: Professor Williams giving the first assignment.
    #- **Dialogue**: "Your first assignment is due next week. Start working on it early."
    show chapter_2_screen_35
    with dissolve
    prof_Williams "Your first assignment is due next week. Start working on it early."
    n "The students quickly noted down the assignment details."

    #### Screen 21: Study Group
    #- **Setting**: Amelia and Lucas decide to form a study group.
    #- **Dialogue**: "Let's form a study group to help each other out."
    show chapter_2_screen_36
    with dissolve
    a "Let's form a study group to help each other out."
    l "Great idea! We can meet here every day."

    #### Screen 22: Meeting Zara
    #- **Setting**: Amelia and Lucas meet Zara in the library.
    #- **Dialogue**: "Hi, I'm Zara. Mind if I join you?"
    show chapter_2_screen_37
    with dissolve
    z "Hi, I'm Zara. Mind if I join you?"
    a "Not at all. I'm Amelia, and this is Lucas."

    #### Screen 23: Introducing Zara
    #- **Setting**: Introducing Zara to their study group.
    #- **Dialogue**: "We were just forming a study group. Want to join?"
    show chapter_2_screen_38
    with dissolve
    a "We were just forming a study group. Want to join?"
    z "Sure! I'd love to."

    #### Screen 24: Study Session
    #- **Setting**: Amelia, Zara, and Lucas studying together.
    #- **Dialogue**: "Let's get started on this assignment."
    show chapter_2_screen_39
    with dissolve
    a "Let's get started on this assignment."
    z "Yes, let's make a plan and divide the work."

    #### Screen 25: Study Group Dynamics
    #- **Setting**: The group discussing their strengths.
    #- **Dialogue**: "I'm good at research. I'll gather the materials."
    show chapter_2_screen_40
    with dissolve
    l "I'm good at research. I'll gather the materials."
    a "I can write the report. What about you, Zara?"
    z "I'll handle the presentation part."

    #### Screen 26: Study Break
    #- **Setting**: Taking a break from studying.
    #- **Dialogue**: "Let's take a short break. My brain is fried."
    show chapter_2_screen_41
    with dissolve
    a "Let's take a short break. My brain is fried."
    l "Good idea. We can grab a coffee."

    #### Screen 27: Coffee Break
    #- **Setting**: The group having coffee and chatting.
    #- **Dialogue**: "So, what got you interested in psychology?"
    show chapter_2_screen_42
    with dissolve
    z "So, what got you interested in psychology?"
    a "I've always been fascinated by how people think and behave."

    #### Screen 28: Discussing Aspirations
    #- **Setting**: Discussing future aspirations.
    #- **Dialogue**: "I want to be a psychologist and help people."
    show chapter_2_screen_43
    with dissolve
    a "I want to be a psychologist and help people."
    l "That's a great goal. I want to explore the depths of the mind."

    #### Screen 29: Bonding Over Goals
    #- **Setting**: The group bonding over shared goals.
    #- **Dialogue**: "We all have different interests, but that's what makes this exciting."
    show chapter_2_screen_44
    with dissolve
    a "We all have different interests, but that's what makes this exciting."
    z "Absolutely. We can learn so much from each other."

    #### Screen 30: Returning to Study
    #- **Setting**: Returning to their study session.
    #- **Dialogue**: "Alright, back to work!"
    show chapter_2_screen_45
    with dissolve
    a "Alright, back to work!"
    l "Let's do this."

    #### Screen 31: Evening Falls
    #- **Setting**: The group studying until evening.
    #- **Dialogue**: "It's getting late. We should wrap up for today."
    show chapter_2_screen_46
    with dissolve
    z "It's getting late. We should wrap up for today."
    a "Agreed. We made good progress."

    #### Screen 32: Saying Goodnight
    #- **Setting**: Saying goodnight to the group.
    #- **Dialogue**: "Goodnight, everyone. See you tomorrow."
    show chapter_2_screen_47
    with dissolve
    a "Goodnight, everyone. See you tomorrow."
    l "Goodnight, Amelia."

    #### Screen 33: Back at the Dorm
    #- **Setting**: Amelia back at her dorm, reflecting on the day.
    #- **Dialogue**: "Today was amazing. I already feel at home here."
    show chapter_2_screen_48
    with dissolve
    a "Today was amazing. I already feel at home here."
    n "Amelia's mind was filled with the day's events and new friendships."

    #### Screen 34: Journaling the Day
    #- **Setting**: Amelia writing in her journal.
    #- **Dialogue**: "Day 1 at university: Met some amazing people and had a great start."
    show chapter_2_screen_49
    with dissolve
    a "Day 1 at university: Met some amazing people and had a great start."
    n "Her journal would be her confidant, her witness to this new chapter."

    #### Screen 35: Preparing for Bed
    #- **Setting**: Amelia preparing for bed, feeling content.
    #- **Dialogue**: "I can't wait for tomorrow."
    show chapter_2_screen_50
    with dissolve
    a "I can't wait for tomorrow."
    n "With a heart full of hope and excitement, Amelia drifted off to sleep."

    return

label shadows_of_the_past:
    play music chapter_3 fadein 1.0 volume 0.1
    scene chapter_3
    with dissolve

    #### Screen 1: Settling In
    #- **Setting**: Amelia's dorm room, unpacking her things.
    #- **Dialogue**: "This is starting to feel like home."
    show chapter_3_screen_1
    with dissolve
    a "This is starting to feel like home."
    n "Amelia arranged her belongings, finding comfort in the familiar items from home."

    #### Screen 2: First Day of Classes
    #- **Setting**: Campus, Amelia walking to her first class.
    #- **Dialogue**: "I hope today goes well."
    show chapter_3_screen_2
    with dissolve
    a "I hope today goes well."
    n "The campus buzzed with activity, a blend of new and returning students."

    #### Screen 3: Classroom Tension
    #- **Setting**: Classroom, a bully makes a snide remark.
    #- **Dialogue**: "Look who thinks she's smart."
    show chapter_3_screen_3
    with dissolve
    s "Look who thinks she's smart."
    a "What was that about?"

    #### Screen 4: Ignoring the Bully
    #- **Setting**: Amelia deciding to ignore the remark.
    #- **Dialogue**: "I won't let it bother me."
    show chapter_3_screen_4
    with dissolve
    a "I won't let it bother me."
    n "Amelia tried to focus on the lecture, pushing the negativity aside."

    #### Screen 5: Encounter with Zara
    #- **Setting**: Zara notices Amelia's discomfort.
    #- **Dialogue**: "Are you okay? I saw what happened."
    show chapter_3_screen_5
    with dissolve
    z "Are you okay? I saw what happened."
    a "Yeah, just some rude comment. I'll be fine."

    #### Screen 6: Zara's Advice
    #- **Setting**: Discussing the incident with Zara.
    #- **Dialogue**: "Don't let them get to you. You're here for a reason."
    show chapter_3_screen_6
    with dissolve
    z "Don't let them get to you. You're here for a reason."
    a "Thanks, Zara. I appreciate it."

    #### Screen 7: Meeting Lucas
    #- **Setting**: Amelia meets Lucas after class.
    #- **Dialogue**: "Hey, Amelia. Everything okay?"
    show chapter_3_screen_7
    with dissolve
    l "Hey, Amelia. Everything okay?"
    a "Yeah, just some drama. Nothing I can't handle."

    #### Screen 8: Lucas's Support
    #- **Setting**: Lucas offers his support.
    #- **Dialogue**: "If you ever need to talk, I'm here."
    show chapter_3_screen_8
    with dissolve
    l "If you ever need to talk, I'm here."
    a "Thanks, Lucas. That means a lot."

    #### Screen 9: Player Choice: React to the Bully
    menu:
        "Confront directly":
            $ jungian_psychology_score += 1
            jump confront_directly
        "Seek support from Prof. Hawthorne":
            $ positive_psychology_score += 1
            jump seek_support_prof_hawthorne

label confront_directly:
    #### Screen 10: Confronting the Bully
    #- **Setting**: Amelia decides to confront the bully.
    #- **Dialogue**: "Hey, what's your problem?"
    show chapter_3_screen_9
    with dissolve
    a "Hey, what's your problem?"
    s "Oh, look. She's got a backbone."

    #### Screen 11: Reflection on Family Conflicts
    #- **Setting**: Amelia reflects on how her family handles conflicts.
    #- **Dialogue**: "My family always taught me to stand up for myself."
    show chapter_3_screen_10
    with dissolve
    a "My family always taught me to stand up for myself."
    n "Memories of her family's advice on dealing with bullies came flooding back."

    #### Screen 12: Handling the Situation
    #- **Setting**: Amelia stands her ground.
    #- **Dialogue**: "You have no right to treat me this way."
    show chapter_3_screen_11
    with dissolve
    a "You have no right to treat me this way."
    s "Whatever. Just stay out of my way."

    #### Screen 13: Aftermath
    #- **Setting**: Amelia talks to Zara and Lucas about the confrontation.
    #- **Dialogue**: "I confronted the bully today."
    show chapter_3_screen_12
    with dissolve
    a "I confronted the bully today."
    z "How did it go?"
    a "They backed off. I'm glad I stood up for myself."

    #### Screen 14: Reflecting on the Confrontation
    #- **Setting**: Amelia reflecting on her actions.
    #- **Dialogue**: "I hope I handled it the right way."
    show chapter_3_screen_13
    with dissolve
    a "I hope I handled it the right way."
    n "The experience left Amelia feeling both empowered and uncertain."

    #### Screen 15: A Quiet Evening
    #- **Setting**: Amelia spending a quiet evening in her dorm room.
    #- **Dialogue**: "Today was intense. I need to unwind."
    show chapter_3_screen_14
    with dissolve
    a "Today was intense. I need to unwind."
    n "Amelia decided to relax and gather her thoughts."

    #### Screen 16: Reflecting in Her Journal
    #- **Setting**: Amelia writing in her journal.
    #- **Dialogue**: "Today I stood up for myself. It felt good but also scary."
    show chapter_3_screen_15
    with dissolve
    a "Today I stood up for myself. It felt good but also scary."
    n "Her journal became a place to process her emotions and experiences."

    #### Screen 17: Texting Ella
    #- **Setting**: Amelia texting her friend Ella.
    #- **Dialogue**: "Hey Ella, today was tough. I had to confront a bully."
    show chapter_3_screen_16
    with dissolve
    a "Hey Ella, today was tough. I had to confront a bully."
    e "I'm proud of you, Amelia. That takes courage."

    #### Screen 18: Ella's Encouragement
    #- **Setting**: Ella encouraging Amelia through text.
    #- **Dialogue**: "Remember, you're stronger than you think."
    show chapter_3_screen_17
    with dissolve
    e "Remember, you're stronger than you think."
    a "Thanks, Ella. I needed to hear that."

    #### Screen 19: Preparing for the Next Day
    #- **Setting**: Amelia preparing for the next day of classes.
    #- **Dialogue**: "Time to get ready for tomorrow."
    show chapter_3_screen_18
    with dissolve
    a "Time to get ready for tomorrow."
    n "Despite the challenges, Amelia felt a renewed sense of determination."

    jump after_choice

label seek_support_prof_hawthorne:
    #### Screen 10: Seeking Support
    #- **Setting**: Amelia decides to seek support from Prof. Hawthorne.
    #- **Dialogue**: "I think I need to talk to someone about this."
    show chapter_3_screen_19
    with dissolve
    a "I think I need to talk to someone about this."
    n "Amelia made her way to Prof. Hawthorne's office, hoping for guidance."

    #### Screen 11: Prof. Hawthorne's Office
    #- **Setting**: Amelia knocking on Prof. Hawthorne's office door.
    #- **Dialogue**: "Come in."
    show chapter_3_screen_20
    with dissolve
    prof_Hawthorne "Come in."
    a "Hi, Professor. Do you have a moment?"

    #### Screen 12: Explaining the Situation
    #- **Setting**: Amelia explaining the situation to Prof. Hawthorne.
    #- **Dialogue**: "I've been dealing with some bullying in class."
    show chapter_3_screen_21
    with dissolve
    a "I've been dealing with some bullying in class."
    prof_Hawthorne "I'm sorry to hear that, Amelia. How can I help?"

    #### Screen 13: Seeking Advice
    #- **Setting**: Amelia seeking advice on how to handle the situation.
    #- **Dialogue**: "I don't know the best way to handle it."
    show chapter_3_screen_22
    with dissolve
    a "I don't know the best way to handle it."
    prof_Hawthorne "There are different approaches you can take."

    #### Screen 14: Discussing Psychological Perspectives
    #- **Setting**: Prof. Hawthorne discussing different psychological perspectives.
    #- **Dialogue**: "You could use techniques from positive psychology to manage stress."
    show chapter_3_screen_23
    with dissolve
    prof_Hawthorne "You could use techniques from positive psychology to manage stress."
    a "Can you tell me more about that?"

    #### Screen 15: Learning Positive Psychology Techniques
    #- **Setting**: Prof. Hawthorne teaching Amelia positive psychology techniques.
    #- **Dialogue**: "Focus on what you can control and practice self-compassion."
    show chapter_3_screen_24
    with dissolve
    prof_Hawthorne "Focus on what you can control and practice self-compassion."
    a "That sounds helpful. I'll give it a try."

    #### Screen 16: Gratitude Exercise
    #- **Setting**: Prof. Hawthorne suggests a gratitude exercise.
    #- **Dialogue**: "Try keeping a gratitude journal. It can shift your mindset."
    show chapter_3_screen_25
    with dissolve
    prof_Hawthorne "Try keeping a gratitude journal. It can shift your mindset."
    a "I'll start tonight. Thank you, Professor."

    #### Screen 17: Reflecting on the Advice
    #- **Setting**: Amelia reflecting on the advice she received.
    #- **Dialogue**: "I feel more equipped to handle this now."
    show chapter_3_screen_26
    with dissolve
    a "I feel more equipped to handle this now."
    n "Amelia left the office feeling a sense of relief and empowerment."

    #### Screen 18: Sharing with Friends
    #- **Setting**: Amelia sharing her experience with Zara and Lucas.
    #- **Dialogue**: "I talked to Prof. Hawthorne about the bullying."
    show chapter_3_screen_27
    with dissolve
    a "I talked to Prof. Hawthorne about the bullying."
    z "What did he say?"
    a "He gave me some great advice and techniques to manage stress."

    #### Screen 19: Supportive Friends
    #- **Setting**: Zara and Lucas offering their support.
    #- **Dialogue**: "We're here for you, Amelia. You don't have to face this alone."
    show chapter_3_screen_28
    with dissolve
    z "We're here for you, Amelia. You don't have to face this alone."
    l "Yeah, we've got your back."

    #### Screen 20: Practicing Gratitude
    #- **Setting**: Amelia starting her gratitude journal.
    #- **Dialogue**: "Today, I'm grateful for my supportive friends and the advice I received."
    show chapter_3_screen_29
    with dissolve
    a "Today, I'm grateful for my supportive friends and the advice I received."
    n "Writing in her gratitude journal helped Amelia focus on the positives."

    #### Screen 21: A New Perspective
    #- **Setting**: Amelia feeling a shift in her mindset.
    #- **Dialogue**: "I can handle this. One step at a time."
    show chapter_3_screen_30
    with dissolve
    a "I can handle this. One step at a time."
    n "With a renewed sense of determination, Amelia faced each day with confidence."

    #### Screen 22: Evening Reflection
    #- **Setting**: Amelia reflecting on the day's events.
    #- **Dialogue**: "I'm stronger than I thought."
    show chapter_3_screen_31
    with dissolve
    a "I'm stronger than I thought."
    n "The day's challenges had tested her, but she emerged stronger."

    #### Screen 23: Texting Ella
    #- **Setting**: Amelia texting her friend Ella.
    #- **Dialogue**: "Hey Ella, today was tough. I had to confront a bully."
    show chapter_3_screen_32
    with dissolve
    a "Hey Ella, today was tough. I had to confront a bully."
    e "I'm proud of you, Amelia. That takes courage."

    #### Screen 24: Ella's Encouragement
    #- **Setting**: Ella encouraging Amelia through text.
    #- **Dialogue**: "Remember, you're stronger than you think."
    show chapter_3_screen_33
    with dissolve
    e "Remember, you're stronger than you think."
    a "Thanks, Ella. I needed to hear that."

    #### Screen 25: Preparing for the Next Day
    #- **Setting**: Amelia preparing for the next day of classes.
    #- **Dialogue**: "Time to get ready for tomorrow."
    show chapter_3_screen_34
    with dissolve
    a "Time to get ready for tomorrow."
    n "Despite the challenges, Amelia felt a renewed sense of determination."

    return

label diving_deep:
    play music chapter_4 fadein 1.0 volume 0.1
    scene chapter_4
    with dissolve

    #### Screen 1: Reflecting on Recent Events
    #- **Setting**: Amelia's dorm room, reflecting on the recent bullying incident and her responses.
    #- **Dialogue**: "It's been a tough week. I need to find a way to cope better."
    show chapter_4_screen_1
    with dissolve
    a "It's been a tough week. I need to find a way to cope better."
    n "Amelia's mind raced with thoughts of the recent events, trying to make sense of her feelings."

    #### Screen 2: Meeting with Prof. Hawthorne
    #- **Setting**: Prof. Hawthorne's office.
    #- **Dialogue**: "Professor, I've been thinking about what you said."
    show chapter_4_screen_2
    with dissolve
    a "Professor, I've been thinking about what you said."
    prof_Hawthorne "I'm glad to hear that, Amelia. How can I help you further?"

    #### Screen 3: Exploring Different Approaches
    #- **Setting**: Prof. Hawthorne's office, discussing different psychological approaches.
    #- **Dialogue**: "I'd like to explore some different approaches to understand myself better."
    show chapter_4_screen_3
    with dissolve
    a "I'd like to explore some different approaches to understand myself better."
    prof_Hawthorne "That's a great idea. Let's talk about your options."

    #### Screen 4: Player Choice: Choose a Path
    menu:
        "Jungian Psychology":
            $ jungian_psychology_score += 2
            jump jungian_psychology
        "Positive Psychology":
            $ positive_psychology_score += 2
            jump positive_psychology
        "Family Systems":
            $ family_systems_score += 2
            jump family_systems

label jungian_psychology:
    #### Screen 5: Introduction to Jungian Psychology
    #- **Setting**: Prof. Hawthorne's office, introduction to Jungian psychology.
    #- **Dialogue**: "Jungian psychology focuses on understanding the unconscious mind."
    show chapter_4_screen_4
    with dissolve
    prof_Hawthorne "Jungian psychology focuses on understanding the unconscious mind."
    a "That sounds fascinating. How do I get started?"
    prof_Hawthorne "Start by keeping a dream journal. Write down everything you remember about your dreams."
    a "How will that help me?"
    prof_Hawthorne "Dreams are a window into your unconscious mind. By analyzing them, you can uncover hidden thoughts, fears, and desires."

    #### Screen 6: Dream Analysis Background
    #- **Setting**: Prof. Hawthorne's office, more detailed explanation.
    #- **Dialogue**: "Jung believed that dreams use symbols to communicate important messages to us."
    show chapter_4_screen_5
    with dissolve
    prof_Hawthorne "Jung believed that dreams use symbols to communicate important messages to us."
    a "So it's not just about the literal events in the dream?"
    prof_Hawthorne "Exactly. The symbols in your dreams can have multiple meanings and can help you understand your inner conflicts and emotions."

    #### Screen 7: Dream Journal Introduction
    #- **Setting**: Prof. Hawthorne's office, practical steps.
    #- **Dialogue**: "Start each day by writing down everything you remember from your dreams."
    show chapter_4_screen_6
    with dissolve
    prof_Hawthorne "Start each day by writing down everything you remember from your dreams."
    a "And then what?"
    prof_Hawthorne "Review your journal regularly. Look for patterns and recurring symbols. Over time, you'll start to see connections to your waking life."

    #### Screen 8: Starting a Dream Journal
    #- **Setting**: Amelia's dorm room, preparing to start her dream journal.
    #- **Dialogue**: "I'll keep this notebook by my bed and write down my dreams as soon as I wake up."
    show chapter_4_screen_7
    with dissolve
    a "I'll keep this notebook by my bed and write down my dreams as soon as I wake up."
    n "Amelia felt a sense of purpose as she prepared to delve into her unconscious mind."

    #### Screen 9: First Night
    #- **Setting**: Amelia's dorm room, night time.
    #- **Dialogue**: "Let's see what my dreams reveal tonight."
    show chapter_4_screen_8
    with dissolve
    a "Let's see what my dreams reveal tonight."
    n "Amelia drifted off to sleep, her mind eager to uncover its hidden messages."

    #### Screen 10: Experiencing the First Dream
    #- **Setting**: Dream sequence, a dark forest.
    #- **Dialogue**: "Where am I? Why is it so dark?"
    show chapter_4_screen_9
    with dissolve
    a "Where am I? Why is it so dark?"
    n "Amelia found herself in a dense, dark forest, the trees towering above her."

    #### Screen 11: The Chase Begins
    #- **Setting**: Dream sequence, footsteps behind her.
    #- **Dialogue**: "I can hear someone behind me. I need to run!"
    show chapter_4_screen_10
    with dissolve
    a "I can hear someone behind me. I need to run!"
    n "She felt an overwhelming sense of fear as she started to run through the forest."

    #### Screen 12: Escaping the Dream
    #- **Setting**: Dream sequence, running through the forest.
    #- **Dialogue**: "I have to keep going. I can't let them catch me."
    show chapter_4_screen_11
    with dissolve
    a "I have to keep going. I can't let them catch me."
    n "The forest seemed endless, the fear driving her forward."

    #### Screen 13: Waking Up
    #- **Setting**: Amelia's dorm room, waking up.
    #- **Dialogue**: "What a nightmare... I need to write this down."
    show chapter_4_screen_12
    with dissolve
    a "What a nightmare... I need to write this down."
    n "Amelia grabbed her notebook and began to jot down every detail she could remember."

    #### Screen 14: First Dream Journal Entry
    #- **Setting**: Amelia's dorm room, writing in her journal.
    #- **Dialogue**: "In my dream, I was being chased through a dark forest. I felt terrified."
    show chapter_4_screen_13
    with dissolve
    a "In my dream, I was being chased through a dark forest. I felt terrified."
    n "Amelia wrote down every detail, her heart still racing from the dream."

    #### Screen 15: Meeting Lucas
    #- **Setting**: Campus library, discussing dreams with Lucas.
    #- **Dialogue**: "Lucas, I've started a dream journal. Can we talk about my latest dream?"
    show chapter_4_screen_14
    with dissolve
    a "Lucas, I've started a dream journal. Can we talk about my latest dream?"
    l "Of course, Amelia. Tell me about it."

    #### Screen 16: Lucas's Insights
    #- **Setting**: Library, discussing dreams with Lucas.
    #- **Dialogue**: "Your dream about being chased could symbolize your fears and anxieties."
    show chapter_4_screen_15
    with dissolve
    l "Your dream about being chased could symbolize your fears and anxieties."
    a "That makes sense. It's been a stressful time."
    l "The dark forest might represent feeling lost or unsure about something in your life."

    #### Screen 17: Deeper Dream Analysis
    #- **Setting**: Amelia and Lucas analyzing more dreams.
    #- **Dialogue**: "I had another dream, this time about a locked door."
    show chapter_4_screen_16
    with dissolve
    a "I had another dream, this time about a locked door."
    l "A locked door often represents something you're avoiding or a barrier in your life."
    a "I felt frustrated, like I couldn't get through no matter how hard I tried."

    #### Screen 18: Dream Visualization
    #- **Setting**: Amelia's dorm room, visualizing her dream.
    #- **Dialogue**: "In the dream, I tried to open the door, but it wouldn't budge."
    show chapter_4_screen_17
    with dissolve
    a "In the dream, I tried to open the door, but it wouldn't budge."
    n "She could vividly remember the feeling of helplessness and frustration."

    #### Screen 19: Reflecting on Dream Symbols
    #- **Setting**: Campus library, further discussion with Lucas.
    #- **Dialogue**: "Do you think the locked door could relate to my fears about fitting in here?"
    show chapter_4_screen_18
    with dissolve
    a "Do you think the locked door could relate to my fears about fitting in here?"
    l "It's possible. Dreams often reflect our deepest concerns."
    a "I guess I'm still worried about not being accepted."

    #### Screen 20: Connecting with Emotions
    #- **Setting**: Amelia reflecting on the emotional connections of her dreams.
    #- **Dialogue**: "These dreams are really helping me understand my feelings."
    show chapter_4_screen_19
    with dissolve
    a "These dreams are really helping me understand my feelings."
    n "Amelia felt a growing sense of clarity as she continued her dream analysis."

    #### Screen 21: New Dream Insights
    #- **Setting**: Amelia sharing her dream insights with Zara.
    #- **Dialogue**: "Zara, I've been learning so much about myself through my dreams."
    show chapter_4_screen_20
    with dissolve
    a "Zara, I've been learning so much about myself through my dreams."
    z "That's amazing, Amelia. It's great that you're finding this helpful."

    #### Screen 22: Discovering Patterns
    #- **Setting**: Amelia identifying patterns in her dreams.
    #- **Dialogue**: "I've noticed a pattern of feeling trapped in my dreams."
    show chapter_4_screen_21
    with dissolve
    a "I've noticed a pattern of feeling trapped in my dreams."
    n "The recurring themes in her dreams provided valuable insights into her subconscious mind."

    #### Screen 23: Applying Insights to Real Life
    #- **Setting**: Amelia applying dream insights to her daily life.
    #- **Dialogue**: "Understanding my dreams is helping me face my fears."
    show chapter_4_screen_22
    with dissolve
    a "Understanding my dreams is helping me face my fears."
    n "Armed with new knowledge, Amelia felt more confident in tackling her challenges."

    #### Screen 24: Reflecting in Her Journal
    #- **Setting**: Amelia writing in her journal about her dream analysis.
    #- **Dialogue**: "Today, I realized that my dreams are guiding me through my emotions."
    show chapter_4_screen_23
    with dissolve
    a "Today, I realized that my dreams are guiding me through my emotions."
    n "Her journal entries became a testament to her growing self-awareness."

    #### Screen 25: Continued Dream Analysis
    #- **Setting**: Amelia continuing her dream analysis with Lucas.
    #- **Dialogue**: "Lucas, I had another dream last night. Let's discuss it."
    show chapter_4_screen_24
    with dissolve
    a "Lucas, I had another dream last night. Let's discuss it."
    l "Sure, Amelia. Tell me about it."

    #### Screen 26: More Dream Symbols
    #- **Setting**: Analyzing new dream symbols with Lucas.
    #- **Dialogue**: "This dream involved water and drowning."
    show chapter_4_screen_25
    with dissolve
    a "This dream involved water and drowning."
    l "Water often represents emotions, and drowning could indicate feeling overwhelmed."

    #### Screen 27: Relating Dreams to Bullying
    #- **Setting**: Relating dream symbols to the bullying incident.
    #- **Dialogue**: "Feeling overwhelmed makes sense given the recent bullying."
    show chapter_4_screen_26
    with dissolve
    a "Feeling overwhelmed makes sense given the recent bullying."
    l "It's important to address these feelings in your waking life too."

    #### Screen 28: Final Dream Analysis Session
    #- **Setting**: Amelia and Lucas having a final dream analysis session.
    #- **Dialogue**: "Thank you for helping me understand my dreams, Lucas."
    show chapter_4_screen_27
    with dissolve
    a "Thank you for helping me understand my dreams, Lucas."
    l "Anytime, Amelia. I'm glad to help."

    #### Screen 29: Evening Reflection
    #- **Setting**: Amelia reflecting on the day's events.
    #- **Dialogue**: "I'm stronger than I thought."
    show chapter_4_screen_28
    with dissolve
    a "I'm stronger than I thought."
    n "The day's challenges had tested her, but she emerged stronger."

    #### Screen 30: Texting Ella
    #- **Setting**: Amelia texting her friend Ella.
    #- **Dialogue**: "Hey Ella, today was tough. I had to confront a bully."
    show chapter_4_screen_29
    with dissolve
    a "Hey Ella, today was tough. I had to confront a bully."
    e "I'm proud of you, Amelia. That takes courage."

    #### Screen 31: Ella's Encouragement
    #- **Setting**: Ella encouraging Amelia through text.
    #- **Dialogue**: "Remember, you're stronger than you think."
    show chapter_4_screen_30
    with dissolve
    e "Remember, you're stronger than you think."
    a "Thanks, Ella. I needed to hear that."

    #### Screen 32: Preparing for the Next Day
    #- **Setting**: Amelia preparing for the next day of classes.
    #- **Dialogue**: "Time to get ready for tomorrow."
    show chapter_4_screen_31
    with dissolve
    a "Time to get ready for tomorrow."
    n "Despite the challenges, Amelia felt a renewed sense of determination."

    return

label positive_psychology:
    #### Screen 5: Introduction to Positive Psychology
    #- **Setting**: Prof. Hawthorne's office, introduction to positive psychology.
    #- **Dialogue**: "Positive psychology focuses on improving well-being and happiness."
    show chapter_4_screen_32
    with dissolve
    prof_Hawthorne "Positive psychology focuses on improving well-being and happiness."
    a "How can that help me handle my stress?"
    prof_Hawthorne "By practicing techniques like gratitude, mindfulness, and focusing on strengths, you can build resilience and a more positive outlook."

    #### Screen 6: Gratitude Exercises
    #- **Setting**: Prof. Hawthorne's office, discussing practical steps.
    #- **Dialogue**: "Start by keeping a gratitude journal. Write down three things you're grateful for every day."
    show chapter_4_screen_33
    with dissolve
    prof_Hawthorne "Start by keeping a gratitude journal. Write down three things you're grateful for every day."
    a "How will that help me?"
    prof_Hawthorne "Focusing on the positive aspects of your life can shift your mindset and help you handle stress better."

    #### Screen 7: Mindfulness Practices
    #- **Setting**: Prof. Hawthorne's office, more practical steps.
    #- **Dialogue**: "Try practicing mindfulness. Spend a few minutes each day focusing on your breathing and being present."
    show chapter_4_screen_34
    with dissolve
    prof_Hawthorne "Try practicing mindfulness. Spend a few minutes each day focusing on your breathing and being present."
    a "That sounds calming. I'll give it a try."

    #### Screen 8: Starting a Gratitude Journal
    #- **Setting**: Amelia's dorm room, preparing to start her gratitude journal.
    #- **Dialogue**: "I'll write down three things I'm grateful for each day."
    show chapter_4_screen_35
    with dissolve
    a "I'll write down three things I'm grateful for each day."
    n "Amelia felt a sense of purpose as she prepared to focus on the positives in her life."

    #### Screen 9: First Gratitude Journal Entry
    #- **Setting**: Amelia's dorm room, writing in her journal.
    #- **Dialogue**: "Today, I'm grateful for the support of my friends, the opportunity to study here, and the beautiful weather."
    show chapter_4_screen_36
    with dissolve
    a "Today, I'm grateful for the support of my friends, the opportunity to study here, and the beautiful weather."
    n "Amelia felt a small but significant shift in her mood as she focused on her gratitude."

    #### Screen 10: Practicing Mindfulness
    #- **Setting**: Amelia's dorm room, practicing mindfulness.
    #- **Dialogue**: "I'll set aside a few minutes each day to practice mindfulness."
    show chapter_4_screen_37
    with dissolve
    a "I'll set aside a few minutes each day to practice mindfulness."
    n "Amelia closed her eyes and focused on her breathing, feeling the tension slowly melt away."

    #### Screen 11: Meeting Zara
    #- **Setting**: Campus café, discussing positive psychology with Zara.
    #- **Dialogue**: "Zara, I've started a gratitude journal and mindfulness practice."
    show chapter_4_screen_38
    with dissolve
    a "Zara, I've started a gratitude journal and mindfulness practice."
    z "That's great, Amelia. How do you feel?"
    a "I already feel a bit more positive and less stressed."

    #### Screen 12: Sharing Techniques
    #- **Setting**: Campus café, sharing positive psychology techniques with Zara.
    #- **Dialogue**: "You should try it too. It really helps."
    show chapter_4_screen_39
    with dissolve
    a "You should try it too. It really helps."
    z "I think I will. Thanks for the suggestion."

    #### Screen 13: Continued Practice
    #- **Setting**: Amelia's dorm room, continuing her gratitude journal and mindfulness practice.
    #- **Dialogue**: "Today, I'm grateful for a productive study session, a delicious lunch, and a good conversation with Zara."
    show chapter_4_screen_40
    with dissolve
    a "Today, I'm grateful for a productive study session, a delicious lunch, and a good conversation with Zara."
    n "Amelia felt her resilience growing as she maintained her positive practices."

    #### Screen 14: Meeting Lucas
    #- **Setting**: Campus library, discussing positive psychology with Lucas.
    #- **Dialogue**: "Lucas, I've been practicing gratitude and mindfulness. It's really helping."
    show chapter_4_screen_41
    with dissolve
    a "Lucas, I've been practicing gratitude and mindfulness. It's really helping."
    l "That's fantastic, Amelia. I'm glad to hear it's making a difference."

    #### Screen 15: Applying Positive Techniques
    #- **Setting**: Amelia applying positive psychology techniques during stressful situations.
    #- **Dialogue**: "I'll take a deep breath and focus on the positives."
    show chapter_4_screen_42
    with dissolve
    a "I'll take a deep breath and focus on the positives."
    n "Amelia used her newfound techniques to handle stress and negativity more effectively."

    #### Screen 16: Reflecting on Progress
    #- **Setting**: Amelia reflecting on her progress.
    #- **Dialogue**: "I'm really seeing a difference in how I handle stress."
    show chapter_4_screen_43
    with dissolve
    a "I'm really seeing a difference in how I handle stress."
    n "Amelia felt a sense of pride and accomplishment as she reflected on her growth."

    #### Screen 17: Final Reflection
    #- **Setting**: Amelia writing in her gratitude journal.
    #- **Dialogue**: "Today, I'm grateful for my progress, the support of my friends, and the guidance of Prof. Hawthorne."
    show chapter_4_screen_44
    with dissolve
    a "Today, I'm grateful for my progress, the support of my friends, and the guidance of Prof. Hawthorne."
    n "Her gratitude journal became a cherished part of her daily routine, helping her maintain a positive outlook."

    return

label family_systems:
    #### Screen 5: Introduction to Family Systems
    #- **Setting**: Prof. Hawthorne's office, introduction to family systems.
    #- **Dialogue**: "Family systems theory looks at how family dynamics shape our behavior and relationships."
    show chapter_4_screen_45
    with dissolve
    prof_Hawthorne "Family systems theory looks at how family dynamics shape our behavior and relationships."
    a "How can that help me understand myself better?"
    prof_Hawthorne "By understanding your family dynamics, you can gain insight into your reactions and interactions with others."

    #### Screen 6: Family Roles
    #- **Setting**: Prof. Hawthorne's office, discussing family roles.
    #- **Dialogue**: "In every family, members take on different roles, which can affect how they relate to each other."
    show chapter_4_screen_46
    with dissolve
    prof_Hawthorne "In every family, members take on different roles, which can affect how they relate to each other."
    a "What kind of roles?"
    prof_Hawthorne "For example, one member might be the caretaker, while another might be the mediator. These roles can influence your behavior and relationships."

    #### Screen 7: Family Dynamics
    #- **Setting**: Prof. Hawthorne's office, more detailed discussion.
    #- **Dialogue**: "Family dynamics also include patterns of communication, conflict, and support."
    show chapter_4_screen_47
    with dissolve
    prof_Hawthorne "Family dynamics also include patterns of communication, conflict, and support."
    a "So by understanding these patterns, I can understand myself better?"
    prof_Hawthorne "Exactly. It can help you identify the root of certain behaviors and feelings."

    #### Screen 8: Reflecting on Family
    #- **Setting**: Amelia's dorm room, reflecting on her family.
    #- **Dialogue**: "I wonder what roles my family members play and how that affects me."
    show chapter_4_screen_48
    with dissolve
    a "I wonder what roles my family members play and how that affects me."
    n "Amelia began to think about her family dynamics, looking for patterns and roles."

    #### Screen 9: Analyzing Family Interactions
    #- **Setting**: Amelia's dorm room, thinking about specific interactions.
    #- **Dialogue**: "I remember always being the one to mediate arguments between my siblings."
    show chapter_4_screen_49
    with dissolve
    a "I remember always being the one to mediate arguments between my siblings."
    n "She realized that her role as a mediator might influence how she handles conflict now."

    #### Screen 10: Discussing with Zara
    #- **Setting**: Campus café, discussing family systems with Zara.
    #- **Dialogue**: "Zara, I've been thinking about how my family dynamics affect me."
    show chapter_4_screen_50
    with dissolve
    a "Zara, I've been thinking about how my family dynamics affect me."
    z "That's interesting. What have you discovered?"
    a "I think my role as the mediator influences how I handle conflicts."

    #### Screen 11: Zara's Perspective
    #- **Setting**: Campus café, Zara sharing her perspective.
    #- **Dialogue**: "I can see that. It's amazing how much our families shape us."
    show chapter_4_screen_51
    with dissolve
    z "I can see that. It's amazing how much our families shape us."
    a "It really is. Understanding this is helping me see things more clearly."

    #### Screen 12: Further Reflection
    #- **Setting**: Amelia's dorm room, further reflection.
    #- **Dialogue**: "I've always been the peacemaker. Maybe that's why I struggle with assertiveness."
    show chapter_4_screen_52
    with dissolve
    a "I've always been the peacemaker. Maybe that's why I struggle with assertiveness."
    n "Amelia began to connect more dots, gaining deeper insights into her behavior."

    #### Screen 13: Meeting Lucas
    #- **Setting**: Campus library, discussing family systems with Lucas.
    #- **Dialogue**: "Lucas, I've been learning about family systems. It's really enlightening."
    show chapter_4_screen_53
    with dissolve
    a "Lucas, I've been learning about family systems. It's really enlightening."
    l "That's great, Amelia. What have you discovered?"
    a "I've realized that my role as the peacemaker in my family affects how I handle conflicts now."

    #### Screen 14: Applying Insights
    #- **Setting**: Amelia applying her insights to her daily life.
    #- **Dialogue**: "I need to work on being more assertive and not always trying to mediate."
    show chapter_4_screen_54
    with dissolve
    a "I need to work on being more assertive and not always trying to mediate."
    n "Armed with new insights, Amelia felt ready to make positive changes in her interactions."

    #### Screen 15: Reflecting on Family Patterns
    #- **Setting**: Amelia reflecting on specific family patterns.
    #- **Dialogue**: "My parents' dynamic also influenced me. They always avoided conflict."
    show chapter_4_screen_55
    with dissolve
    a "My parents' dynamic also influenced me. They always avoided conflict."
    n "She saw how these patterns were mirrored in her own behavior, especially in stressful situations."

    #### Screen 16: Writing in Her Journal
    #- **Setting**: Amelia writing in her journal about her family insights.
    #- **Dialogue**: "Today, I realized that my family's patterns have a big impact on me."
    show chapter_4_screen_56
    with dissolve
    a "Today, I realized that my family's patterns have a big impact on me."
    n "Her journal entries became a way to process and solidify her new understandings."

    #### Screen 17: Continued Reflection
    #- **Setting**: Amelia continuing to reflect on her family dynamics.
    #- **Dialogue**: "Understanding my family dynamics is helping me understand myself."
    show chapter_4_screen_57
    with dissolve
    a "Understanding my family dynamics is helping me understand myself."
    n "Amelia felt a growing sense of clarity and empowerment as she delved deeper."

    #### Screen 18: Final Reflection
    #- **Setting**: Amelia writing a final reflection in her journal.
    #- **Dialogue**: "Today, I'm grateful for the insights I've gained about my family and myself."
    show chapter_4_screen_58
    with dissolve
    a "Today, I'm grateful for the insights I've gained about my family and myself."
    n "Her journal entries reflected a journey of self-discovery and growth."

    return
