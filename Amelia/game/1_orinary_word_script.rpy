# Define characters
define a = Character("Amelia")
define e = Character("Ella")
define j = Character("James")
define p = Character("Parents")
define n = Character("Narrator")

# The game starts here.
label start_3:
    play music "chapter_0_2.mp3" fadein 1.0 volume 0.1
    scene amelia_bedroom_morning
    with dissolve

    n "Amelia James, a bright-eyed young woman with an insatiable curiosity about the human mind, is about to embark on a life-changing journey."

    show amelia_bedroom_closeup
    with dissolve

    a "Today is the day... I can't believe it's finally here."

    n "Her room is a testament to her passions - books on psychology and notebooks filled with her thoughts and observations."

    show amelia_bedroom_books
    with dissolve

    n "High school was a theater of emotions and social hierarchies; a ripe field for observation."

    show amelia_highschool
    with dissolve

    a "I learned so much about people just by watching and listening. But there's so much more to understand."

    scene amelia_family_living_room
    with dissolve

    n "Amelia's family dynamics are equally important. Her parents have always been supportive, though sometimes a bit overprotective."

    show amelia_family_breakfast
    with dissolve

    p "Amelia, breakfast is ready!"

    a "Coming, Mom!"

    show amelia_breakfast_table
    with dissolve

    p "Are you excited about the big news today?"

    a "I am. I just hope everything goes as planned."

    n "Her parents' support has always been her anchor."

    show amelia_hugging_parents
    with dissolve

    a "Thank you both for always being there for me. I couldn't have done it without you."

    p "We're so proud of you, Amelia. You're going to do great things."

    scene amelia_park_day
    with dissolve

    n "A walk in the park often helps Amelia clear her mind. Today, it's especially important."

    show amelia_park_entrance
    with dissolve

    a "It's such a beautiful day. The park is always so calming."

    show amelia_park_bench
    with dissolve

    a "I'll just sit here for a while and think about everything."

    menu:
        "Reflect on her future":
            $ SD += 1
            show amelia_park_future
            with dissolve
            n "Amelia sat on a bench, her mind drifting to thoughts of the future. Plymouth University was a fresh start, a place to pursue her passion for psychology."
            a "I wonder what my life will be like there. So many new opportunities and challenges await."
            show amelia_park_future2
            with dissolve
            a "I hope I can handle everything that's coming my way. It's exciting but also a bit scary."
            show amelia_park_future3
            with dissolve
            n "The sound of children playing and birds singing brought a sense of peace, but Amelia couldn't shake the nervousness about the unknown."
            a "I need to stay positive and open to all the new experiences. This is a chance to grow."

        "Think about her current relationships":
            $ SI += 1
            show amelia_park_walk
            with dissolve
            n "Amelia walked slowly, thinking about her friends and family. She felt a mix of excitement and sadness, knowing she would miss them."
            a "I hope I can keep in touch with everyone. Ella, my parents, and even my teachers. They've all been such a big part of my life."
            show amelia_park_walk2
            with dissolve
            a "It's going to be hard to say goodbye, but I know this is the right step for me."
            show amelia_park_walk3
            with dissolve
            n "She watched families and couples enjoying the park, feeling a pang of longing for the familiar comfort of home."
            a "I'll make new friends and create new memories, just like I did here."

    show amelia_park_exit
    with dissolve

    a "It's time to head home and start preparing. There's so much to do."

    jump preparing_for_university

label preparing_for_university:
    play music "chapter_1.mp3" fadein 1.0 volume 0.1
    scene amelia_room_packing
    with dissolve

    a "There's so much to pack. I need to be organized."

    show amelia_room_closet
    with dissolve

    a "Clothes, check. Books, check. What else do I need?"

    show amelia_room_bookshelf
    with dissolve

    menu:
        "Organize her study materials":
            $ AA += 1
            show amelia_room_study
            with dissolve
            n "Amelia carefully sorted her textbooks and notes, making sure everything was in order for her studies."
            a "These books will be my lifeline at university. I need to make sure I have everything."
            show amelia_room_desk
            with dissolve
            a "Notes, check. Pens and highlighters, check. Laptop, check."
            show amelia_room_study_done
            with dissolve
            a "Alright, I think I'm all set academically. I feel a bit more prepared now."

        "Call Ella to talk about her excitement":
            $ SI += 1
            show amelia_phone_call
            with dissolve
            a "Hi Ella! I just wanted to share how excited I am about Plymouth. I can't wait to start!"
            show ella_phone_screen
            with dissolve
            e "That's amazing, Amelia! I'm so happy for you. We'll definitely keep in touch."
            show amelia_phone_call_2
            with dissolve
            a "Thanks, Ella. Your support means the world to me."
            e "You'll do great. Just remember to have fun too!"
            show amelia_phone_call_end
            with dissolve
            a "Talking to Ella always makes me feel better. I'm lucky to have her as a friend."

        "Meditate to calm her nerves":
            $ MH += 1
            show amelia_meditation
            with dissolve
            n "Amelia took a deep breath and sat down to meditate. She focused on her breathing, letting the calm wash over her."
            a "I need to stay calm and focused. Everything will be fine."
            show amelia_meditation_2
            with dissolve
            a "Inhale... exhale... Just let the tension go."
            show amelia_meditation_3
            with dissolve
            n "With each breath, she felt her anxiety melting away, replaced by a sense of peace and readiness."
            a "I can do this. I'm ready for whatever comes next."

    show amelia_room_finished_packing
    with dissolve

    a "All done! Now to have dinner with my parents."

    jump dinner_with_parents

label dinner_with_parents:
    scene dinner_table
    with dissolve

    p "So, Amelia, are you excited about starting university?"
    a "I am! It's a bit overwhelming, but I'm really looking forward to it."

    show dinner_family_talking
    with dissolve

    menu:
        "Discuss her future plans":
            $ MC += 1
            show dinner_future_plans
            with dissolve
            a "I've been thinking a lot about how I want to contribute to society through psychology. It's so important to understand and help people."
            p "That's wonderful, Amelia. We're so proud of your ambitions."
            show dinner_future_plans_2
            with dissolve
            a "Thank you. I really hope I can make a difference."
            p "With your dedication and passion, we know you will."

        "Ask for advice from her parents":
            $ SI += 1
            show dinner_ask_advice
            with dissolve
            a "Do you have any advice for me? I want to make the most of my time at university."
            p "Just be yourself, work hard, and don't be afraid to ask for help when you need it."
            show dinner_ask_advice_2
            with dissolve
            a "Thanks, Mom and Dad. I really appreciate your support."
            p "Remember, it's okay to make mistakes. It's all part of the learning process."

        "Express her gratitude to her parents":
            $ MH += 1
            show dinner_gratitude
            with dissolve
            a "Thank you both for all your support. I couldn't have done this without you."
            p "We're so proud of you, Amelia. You're going to do great things."
            show dinner_gratitude_2
            with dissolve
            a "I'll make you proud."
            p "You already have, sweetheart."

    show dinner_conversation
    with dissolve

    a "I'm going to miss these family dinners."

    p "We'll miss you too, but we know you're going to do great."

    jump afternoon_tea_with_ella

label afternoon_tea_with_ella:
    scene tea_house
    with dissolve

    e "I'm going to miss our afternoon teas. But I'm so excited for you!"
    a "I'll miss this too. We need to stay in touch."

    show tea_conversation
    with dissolve

    menu:
        "Discuss university plans":
            $ SI += 1
            show tea_university_plans
            with dissolve
            a "I've been thinking about my schedule and the classes I'm going to take. It's going to be intense, but I'm ready."
            e "You’ve got this, Amelia. Just remember to take breaks and enjoy the experience."
            show tea_university_plans_2
            with dissolve
            a "I will. Thanks for the advice, Ella."
            e "No problem! I'm here for you."

        "Reminisce about school days":
            $ MH += 1
            show tea_remember_school
            with dissolve
            a "Remember that time in high school when we stayed up all night studying for finals?"
            e "How could I forget? We were so stressed, but we made it through together."
            show tea_remember_school_2
            with dissolve
            a "Those were some tough times, but also some of the best memories."
            e "Definitely. We'll make more memories, even with you away."

        "Share fears about the future":
            $ SD += 1
            show tea_share_fears
            with dissolve
            a "I have to admit, I'm a bit scared about moving and starting over. What if I don't fit in?"
            e "It's normal to feel that way, but you're going to make new friends and have amazing experiences. Trust yourself."
            show tea_share_fears_2
            with dissolve
            a "Thanks, Ella. Your support means so much to me."
            e "You'll do great. Just be yourself."

    show tea_goodbye
    with dissolve

    e "I'll miss you, but I know you'll do great. Let's keep in touch."

    a "Absolutely. Thanks, Ella."

    jump exploring_the_museum

label exploring_the_museum:
    scene museum_entrance
    with dissolve

    n "Amelia wandered through the exhibits, taking in the history and culture."

    show museum_hall
    with dissolve

    menu:
        "Learn about human evolution":
            $ AA += 1
            show museum_human_evolution
            with dissolve
            n "Amelia spent time in the anthropology section, fascinated by the development of the human species."
            a "It's amazing how much we've evolved over time."
            show museum_human_evolution_2
            with dissolve
            a "I can't wait to study more about human behavior and psychology."
            show museum_human_evolution_3
            with dissolve
            n "The detailed exhibits provided a lot of insight and sparked Amelia's curiosity even more."

        "Study ancient artifacts":
            $ SD += 1
            show museum_ancient_artifacts
            with dissolve
            n "Amelia explored the exhibits on ancient civilizations, pondering the wisdom they held."
            a "There's so much we can learn from the past."
            show museum_ancient_artifacts_2
            with dissolve
            a "These artifacts tell such fascinating stories."
            show museum_ancient_artifacts_3
            with dissolve
            n "The intricate designs and historical significance of each piece captivated her."

        "Reflect on the nature of humanity":
            $ MH += 1
            show museum_reflect_humanity
            with dissolve
            n "The exhibits inspired Amelia to think deeply about what it means to be human and the complexities of our existence."
            a "What does it truly mean to be human? It's such a profound question."
            show museum_reflect_humanity_2
            with dissolve
            a "I want to understand the deeper aspects of our nature."
            show museum_reflect_humanity_3
            with dissolve
            n "Amelia felt a deep sense of connection with the human journey through time."

    show museum_exit
    with dissolve

    a "That was enlightening. Time to head to the river for some fresh air."

    jump evening_by_the_thames

label evening_by_the_thames:
    scene thames_evening
    with dissolve

    n "As the sun set over the river, Amelia felt a sense of peace."

    show thames_sunset
    with dissolve

    menu:
        "Watch the sunset":
            $ SD += 1
            show thames_sunset_closeup
            with dissolve
            n "Amelia watched the colors of the sky change, feeling inspired and hopeful about the future."
            a "This is so beautiful. It's like the world is full of endless possibilities."
            show thames_sunset_end
            with dissolve
            a "I need to hold onto this feeling of peace and carry it with me."

        "Write in her journal":
            $ MH += 1
            show thames_journal
            with dissolve
            n "Amelia took out her journal and wrote down her thoughts and feelings, helping her process her emotions."
            a "Writing always helps me clear my mind."
            show thames_journal_closeup
            with dissolve
            a "I feel more at ease now, putting my thoughts into words."
            show thames_journal_end
            with dissolve
            a "I'll look back on these notes whenever I need encouragement."

        "People-watch and observe behaviors":
            $ AA += 1
            show thames_people_watching
            with dissolve
            n "Amelia observed the people around her, practicing her skills of observation and thinking about the different aspects of human behavior."
            a "Everyone has their own story. I can't wait to learn more about what makes us all tick."
            show thames_people_watching_closeup
            with dissolve
            a "These observations will be useful in my studies."
            show thames_people_watching_end
            with dissolve
            a "Understanding behavior is key to understanding the mind."

    show thames_exit
    with dissolve

    a "That was refreshing. Now, to the bookstore for some last-minute shopping."

    jump browsing_the_bookstore

label browsing_the_bookstore:
    scene bookstore
    with dissolve

    n "Amelia wandered through the aisles of the quaint bookstore, feeling at home among the shelves of books."

    show bookstore_aisles
    with dissolve

    menu:
        "Explore the psychology section":
            $ AA += 1
            show bookstore_psychology
            with dissolve
            n "Amelia browsed through the latest psychology books, feeling inspired by the wealth of knowledge."
            a "There's so much to learn. I can't wait to dive into these books."
            show bookstore_psychology_closeup
            with dissolve
            a "I'll get this one on cognitive psychology and this one on developmental stages."
            show bookstore_psychology_end
            with dissolve
            a "These will be great resources for my studies."

        "Wander into the occult section":
            $ OK += 1
            show bookstore_occult
            with dissolve
            n "Amelia found herself intrigued by ancient texts and mystical books, sparking a curiosity for the unknown."
            a "These books look fascinating. I wonder what secrets they hold."
            show bookstore_occult_closeup
            with dissolve
            a "This one on alchemy and this one on ancient wisdom seem interesting."
            show bookstore_occult_end
            with dissolve
            a "I'll add these to my collection and explore them when I have time."

        "Buy a meditation guide":
            $ SD += 1
            show bookstore_meditation
            with dissolve
            n "Amelia purchased a book on meditation, eager to explore mindfulness practices."
            a "This should help me stay calm and focused during my studies."
            show bookstore_meditation_closeup
            with dissolve
            a "I'll start with this beginner's guide and work my way up."
            show bookstore_meditation_end
            with dissolve
            a "Meditation will be a great tool for managing stress."

    show bookstore_exit
    with dissolve

    a "I think I have everything I need now. Time to head home and get some rest."

    jump ordinary_world_end

label ordinary_world_end:
    scene amelia_bedroom_night
    with dissolve

    n "As Amelia lay in bed, she felt a mix of excitement and nervousness. Tomorrow, she would embark on a new journey, leaving her old life behind."

    show amelia_bedroom_night_closeup
    with dissolve

    a "It's really happening. Tomorrow, everything changes. I'm ready for this."

    show amelia_bedroom_night_window
    with dissolve

    a "Goodnight, London. Next stop, Plymouth."

    stop music fadeout 1.0
    jump call_to_adventure
