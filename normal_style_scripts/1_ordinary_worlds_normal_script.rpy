label start_chapter_1:
    # Initial scene setup with music and transition effects
    stop music
    play music "second_child_restless_child.mp3" fadein 1.0 volume 0.5
    scene black

    # Amelia reflects on her journey, scene changes illustrating her thoughts
    show scene dreams_background with dissolve
    n "Amelia's curiosity about the mind began in a room of dreams and playful experiments."
    pause 2.0

    show scene high_school_background with dissolve
    n "High school was a theater of emotions and social hierarchies; a ripe field for observation."
    pause 2.0

    show scene university_gate_background with dissolve
    n "University, a beacon of hope, promising a sanctuary where curiosity intertwines with opportunity."
    pause 2.0

    show scene future_veiled with dissolve
    n "With every passing moment, the future lingered, veiled in an envelope yet to arrive."
    pause 2.0

    # Transition to Amelia's reaction to her university acceptance
    show scene amelia_room with amelia_excited at center
    play music "soldier_poet_king.mp3" fadein 2.0 volume 0.5
    a "I got in! I actually got in!"
    a "Holy moly, this is the best ever!"

    # Amelia contemplates who to tell first about her acceptance
    show scene amelia_room with amelia_thinking at center
    a "But... who do I tell first?"

    menu:
        "Tell Ella first":
            # Scene with Ella at a park bench, Amelia shares her excitement
            show scene park_bench with amelia_happy left, ella_happy right
            a "Ella, look! I'm going to Plymouth!"
            e "Whaaaa... That is amazing!"
            e "That's amazing, Millie! I knew you could do it!"
            e "I'm so proud of you. You've worked so hard for this."

            # Emotional support and reassurance from Ella
            a "Thank you, Ella. Your support means everything to me."
            e "Of course, you know I'll always be here for you. Even if we're miles apart."

        "Tell Parents first":
            # Scene with Amelia's parents in the living room, sharing the news
            show scene living_room with amelia_happy left, parents_happy right
            a "Mum, Dad, Plymouth said YES!"
            p "We always knew you'd make it, darling."
            p "Congratulations, sweetheart! This is wonderful news."

            # Parents express their pride and support
            a "I can hardly believe it. I'm going to university!"
            p "We're so proud of you, Amelia. You've put in so much hard work."

    # Amelia ends the day reflecting on her future
    show scene amelia_room_night with amelia_content at center
    a "Today was a big day. Tomorrow, the journey begins for real."
    fadeout 2.0

    # Reset music and prepare for the next chapter
    stop music fadeout 1.0
    jump preparing_for_university

label preparing_for_university:
    # Scene background: Amelia's bedroom during the day, a bit messy with packing in progress
    scene amelia_room_packing with dissolve
    show amelia_thinking at center
    play music "preparation_theme.mp3" fadein 2.0 volume 0.5

    a "Okay, time to make sure I have everything I need for university. There’s so much to pack!"

    # Amelia checks her list
    show amelia_list at center
    a "Let’s see, clothes... check, toiletries... check, academic supplies... Oh, I need to sort those out."

    # Decision Point: What to focus on first
    menu:
        "Organize study materials":
            $ AA += 1  # Increasing Academic Achievement points
            show amelia_study_materials at center
            a "My books and notes can't be left behind. Let's get these organized first."
            n "Amelia carefully sorted through her textbooks and notebooks, ensuring she had all her essentials."

            # Transition: Showing the packed study materials
            hide amelia_study_materials
            show amelia_packed_books at center
            a "Perfect, all my study materials are packed and ready!"

        "Pack clothes and essentials":
            $ SI += 1  # Increasing Social Interaction points
            show amelia_clothes at center
            a "I should pack enough clothes and essentials to start off. Can't forget the weather will be different there."
            n "Amelia packed her clothing thoughtfully, considering both practicality and style for her new environment."

            # Transition: Showing the packed suitcase
            hide amelia_clothes
            show amelia_packed_suitcase at center
            a "That should be enough to get me through the first few weeks."

    # Final preparations
    show amelia_final_check at center
    a "Almost done packing. Just need to double-check everything. Can’t believe I’m leaving tomorrow!"

    # Emotional reflection
    n "The room was filled with boxes and suitcases, each labeled neatly. Amelia took a moment to look around her familiar room, filled with a mix of nostalgia and excitement."

    # Closing the scene with Amelia ready for the new chapter
    a "This is it, the next big step. I’m ready for this!"
    hide amelia_final_check
    with fade
    stop music fadeout 2.0

    # Transition to the next scene or chapter
    jump dinner_with_parents

label dinner_with_parents:
    # Scene background: A cozy dining room in the evening, table set for dinner
    scene dining_room_evening with dissolve
    show amelia_sitting at left
    show parents_sitting at right
    play music "family_dinner_theme.mp3" fadein 2.0 volume 0.5

    # Amelia discusses her upcoming university life
    p "So, Amelia, you must be getting excited about university?"
    a "Yes, I am! It's a big change, but I'm really looking forward to it."

    # Decision Point: Discuss various topics with parents
    menu:
        "Talk about academic plans":
            $ AA += 1  # Increasing Academic Achievement points
            show amelia_talking at left
            a "I've been looking into the modules I can take, and there are so many interesting options."
            p "That sounds wonderful, Amelia. It's good to see you so passionate about your studies."

            # Transition: Parents showing support
            show parents_proud at right
            p "Just remember, it’s important to balance your workload and find time to relax too."

        "Share excitement and fears":
            $ MH += 1  # Increasing Mental Health points
            show amelia_concerned at left
            a "I'm excited, but honestly, I'm a bit nervous about moving so far away."
            p "It's perfectly normal to feel that way. We're always here if you need to talk, no matter where you are."

            # Transition: Emotional support
            show parents_supportive at right
            p "And remember, it's an adventure. It's okay to feel a bit scared."

        "Express gratitude":
            $ SI += 1  # Increasing Social Interaction points
            show amelia_grateful at left
            a "I really appreciate everything you’ve done for me. I couldn’t have reached this point without your support."
            p "We're just happy to see you grow and chase your dreams. You’ve always made us proud."

            # Transition: Heartfelt moment
            show parents_loving at right
            p "And you always will, no matter what. We love you, Amelia."

    # Wrap up the dinner scene
    a "Thanks for the great dinner, and for the talk. It means a lot to me."
    n "The family continued their meal, filled with light conversation and shared laughter, cherishing these moments together."

    # Emotional reflection as the scene ends
    n "As dinner concluded, Amelia felt a renewed sense of confidence and connection with her parents."
    hide amelia_sitting
    hide parents_sitting
    with fade
    stop music fadeout 2.0

    # Transition to the next scene or chapter
    jump next_scene_label

label afternoon_tea_with_ella:
    # Scene background: Cozy tea house with a warm, inviting atmosphere
    scene tea_house_interior with dissolve
    show ella_sitting at right
    show amelia_sitting at left
    play music "light_hearted_conversation.mp3" fadein 2.0 volume 0.5

    # Amelia and Ella's conversation begins
    e "I'm going to miss these little tea dates. But I'm so excited for you, Amelia!"
    a "I know, it’s going to be strange not having our weekly catch-ups here."
    
    # Decision Point: What to discuss over tea
    menu:
        "Discuss university and classes":
            $ SI += 1  # Increasing Social Interaction points
            show amelia_excited at left
            a "I’ve been planning out my classes and everything. It’s all a bit overwhelming but exciting."
            e "Just make sure to not overdo it! It’s your first year, so take time to enjoy it too."
            
            # Additional supportive dialogue from Ella
            show ella_encouraging at right
            e "You’re going to do great. I’ll be cheering for you all the way from here!"

        "Share concerns about moving away":
            $ MH += 1  # Increasing Mental Health points
            show amelia_concerned at left
            a "Honestly, I’m a bit worried about moving away from home and everyone I know."
            e "That’s totally normal, Amelia. But remember, we’re just a call away. You can always reach out."

            # Comforting reassurance from Ella
            show ella_comforting at right
            e "Plus, think of all the new people you’ll meet and the experiences you'll have. It’s going to be amazing."

        "Talk about keeping in touch":
            $ SD += 1  # Increasing Self-Discovery points
            show amelia_hopeful at left
            a "Promise me we’ll keep in touch regularly? I can’t imagine not talking to you all the time."
            e "Of course! We’ll text, call, video chat—whatever it takes. Distance won’t change a thing."

            # Ella expresses her unwavering friendship
            show ella_smiling at right
            e "And whenever you’re back, we’ll make up for lost time. It’ll be like you never left."

    # Conclusion of their tea time
    a "Thanks, Ella. Talking to you always makes things better."
    e "Anytime, Amelia. I’m here whenever you need me, okay? And I’m so proud of you."

    # Emotional wrap-up as they finish their tea
    n "As they finished their tea, the weight of Amelia’s upcoming departure lingered in the air, softened by the warmth of enduring friendship."

    hide ella_sitting
    hide amelia_sitting
    with fade
    stop music fadeout 2.0

    # Transition to the next scene or reflection
    jump exploring_the_museum

label exploring_the_museum:
    # Scene background: A grand museum with various exhibits visible
    scene museum_interior with dissolve
    show amelia_standing center
    play music "contemplative_melody.mp3" fadein 2.0 volume 0.5

    # Amelia enters the museum
    n "After saying goodbye to Ella, Amelia decided to spend some time at the museum, surrounded by history and culture."
    a "I think a little time among these ancient stories might help me sort out my thoughts."

    # Decision Point: What to explore in the museum
    menu:
        "Learn about human evolution":
            $ AA += 1  # Increasing Academic Achievement points
            show exhibit_human_evolution on screen
            a "It’s fascinating to see how far humanity has come. It really puts things into perspective."
            
            # Additional information from the exhibit
            n "Amelia spent considerable time in front of the panels detailing the progression of human societies from hunter-gatherers to modern civilizations."

        "Study ancient artifacts":
            $ SD += 1  # Increasing Self-Discovery points
            show exhibit_ancient_artifacts on screen
            a "Each of these artifacts holds so many untold stories. What were the people like who made them?"
            
            # Amelia ponders the connection between past and present
            n "Her gaze lingered on a particularly intricate bronze tool, its craftsmanship speaking of skilled hands long stilled."

        "Reflect on artistic expressions":
            $ MH += 1  # Increasing Mental Health points
            show exhibit_art_paintings on screen
            a "Art really speaks across the ages. There's something incredibly moving about that."
            
            # Description of Amelia's interaction with the art
            n "Standing before a series of poignant portraits, Amelia felt a connection to the emotions conveyed by the brushstrokes."

    # Amelia's reflective moment
    n "As she moved from exhibit to exhibit, Amelia felt a growing sense of connection with the past, and a readiness for her own future."

    # Wrap-up the museum visit
    a "I’m glad I came here today. It’s given me a lot to think about, about where I come from, and where I’m going."
    n "With a renewed sense of purpose and a heart full of history’s lessons, Amelia exited the museum, ready to face her next adventure."

    hide amelia_standing
    with fade
    stop music fadeout 2.0

    # Transition to the next scene or reflective moment
    jump evening_by_the_thames

label evening_by_the_thames:
    # Scene setup: Evening view by the Thames with the sun setting over the water
    scene thames_evening with dissolve
    show amelia_sitting side right
    play music "evening_reflection.mp3" fadein 2.0 volume 0.5

    # Amelia enjoys the peace of the riverside
    a "I love this spot. The river always makes me feel so peaceful."
    a "There's something about watching the water flow by. It's like it puts everything into perspective."

    # Decision point: What Amelia chooses to do by the river
    menu:
        "Watch the sunset and reflect":
            $ SD += 1  # Increasing Self-Discovery points
            show sunset_view center
            a "This is so beautiful. It’s like the world is full of endless possibilities."

            # Reflection on the changing skies
            n "As the sky painted itself in hues of orange and purple, Amelia felt a sense of peace washing over her."

        "Write in her journal":
            $ MH += 1  # Increasing Mental Health points
            show amelia_writing side right
            a "Writing always helps me clear my mind. Let's capture these thoughts."

            # Amelia jotting down her feelings
            n "Pen to paper, she scribbled down her fears, hopes, and dreams, each word helping to ease her mind."

        "People-watch and observe behaviors":
            $ AA += 1  # Increasing Academic Achievement points
            show people_walking background
            a "Everyone has their own story. Watching them helps me understand the diverse tapestry of human life."

            # Observing people passing by
            n "From couples strolling hand-in-hand to hurried commuters, Amelia considered the myriad lives unfolding around her."

    # Amelia sums up her evening
    a "Evening like this make me realize how much I have to look forward to—and how much I'll miss this place."
    n "Resolved and ready, Amelia stood, feeling more connected to herself and her future."

    # Transition out of the scene
    hide amelia_sitting
    fadeout 2.0
    stop music fadeout 2.0

    # Move to the next important event or location
    jump browsing_the_bookstore

label browsing_the_bookstore:
    # Scene setup: Inside a quaint and cozy bookstore
    scene bookstore_interior with dissolve
    show amelia_browsing side left
    play music "quiet_bookstore_ambience.mp3" fadein 2.0 volume 0.5

    # Amelia expresses her love for bookstores
    a "I could live in bookstores. The smell of books, the endless possibilities on every shelf..."

    # Decision point: Which section does Amelia explore?
    menu:
        "Explore the psychology section":
            $ AA += 1  # Increasing Academic Achievement points
            show psychology_books center
            a "So many fascinating topics... cognitive psychology, developmental stages, behavioral analysis..."
            n "Amelia scanned the shelves, her eyes lighting up as she picked up several books to purchase."

        "Wander into the occult section":
            $ OK += 1  # Increasing Occult Knowledge points
            show occult_books center
            a "This section always piques my curiosity. There's so much mystery and history behind these ancient texts."
            n "The musty scent of old pages filled the air as Amelia thumbed through a book on alchemical symbols."

        "Buy a meditation guide":
            $ SD += 1  # Increasing Self-Discovery points
            show meditation_books center
            a "A beginner’s guide to meditation—this might be really helpful with the stress of university life."
            n "Amelia flipped through the pages, finding peace in the simple, mindful exercises described."

    # Amelia finalizes her selections
    a "I think these will really help me prepare for what's ahead."
    n "Content with her choices, Amelia approached the checkout counter, ready to make her purchase."

    # Transition out of the bookstore scene
    hide amelia_browsing
    fadeout 2.0
    stop music fadeout 2.0

    # Moving to the next scene or returning home
    jump night_before_the_move

label night_before_the_move:
    # Scene setup: Amelia's bedroom at night, indicating reflection and anticipation
    scene amelia_bedroom_night with fade
    show amelia_sitting_on_bed side left
    play music "reflective_night_theme.mp3" fadein 2.0 volume 0.5

    # Amelia reflects on her day and the upcoming journey
    a "What a day. I can't believe tomorrow is the start of everything."
    a "It feels like I've been waiting for this moment forever, and now it's here."

    # Amelia expresses her thoughts and emotions about the new chapter in her life
    a "I wonder what university will really be like? Will I make friends easily? Will the classes be as interesting as I hope?"
    a "That's the exciting part, isn't it? The unknown, the possibilities."
    a "Even if it's scary, it's also thrilling. Like standing on the edge of a cliff, ready to fly."

    # Amelia contemplates the challenges ahead
    a "I know there will be challenges. Moments of doubt, of homesickness, of stress."
    a "But I also know I'm ready to face them. I've been preparing for this, not just academically, but emotionally too."

    # Amelia acknowledges the support she's received
    a "The conversations with Mum and Dad, with Ella... they've given me strength."
    a "And the things I've learned about myself... at the museum, by the river, in the bookstore... they've shown me that I'm capable of growth, of reflection, of resilience."

    # Amelia shares her tools and purpose
    a "I have tools now, tools I didn't have before. Meditation, writing, observing... ways to process and understand the world around me."
    a "And most importantly, I have a sense of purpose. A drive to learn, to help, to make a difference."
    a "That's what will guide me through whatever comes next."

    # Amelia prepares to embrace her journey
    a "So, as much as part of me wants to cling to the familiarity of home... I know it's time."
    a "Okay, Amelia. Time to sleep. Tomorrow... tomorrow is the first day of the rest of your life."

    # Transition to sleep, symbolizing the end of one chapter and the beginning of another
    hide amelia_sitting_on_bed
    fadeout 2.0
    stop music fadeout 1.0

    # Setting up for the next day
    show amelia_bedroom_night_window with dissolve
    a "Goodnight, London. Thank you for all you've taught me."
    a "And good morning, Plymouth. I can't wait to see what lessons you have in store."

    # End of the night scene, leading to the next chapter
    hide amelia_bedroom_night_window
    fadeout 2.0
    jump start_chapter_2

