# Define characters
define a = Character("Amelia")
define e = Character("Ella")
define j = Character("James")
define p = Character("Parents")
define n = Character("Narrator")

default AA = 0
default SI = 0
default MH = 0
default SD = 0
default MC = 0
default OK = 0

define music.second_child_restless_child = "second_child_restless_child.mp3"
define music.soldier_poet_king = "soldier_poet_king.mp3"
define music.chapter_2 = "chapter_2.mp3"


# The game starts here.

label start:
    play music second_child_restless_child fadein 1.0 volume 0.5
    #scene chapter_0
    #with dissolve

    #pause 4.0

    scene screen_0
    with dissolve
    n "Amelias curiosity about the mind began in a room of dreams and playful experiments."

    scene screen_m3
    with dissolve
    n "High school was a theater of emotions and social hierarchies; a ripe field for observation"

    scene screen_m2
    with dissolve
    n "University, a beacon of hope, promising a sanctuary where curiosity intertwines with opportunit"

    scene screen_m1
    with dissolve
    n "With every passing moment, the future lingered, veiled in an envelope yet to arrive."


    stop music fadeout 2.0
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene chapter_1
    with dissolve

    pause 4.0

    scene screen_1
    with dissolve
    play music soldier_poet_king fadein 2.0 volume 0.5
    
    a "I got in! I actually got in!"
    a "Holy moly, this is the best ever!"


    show screen_2
    with dissolve
    a "Whooohooo!"
    a "Plymouth, here I come!"


    show screen_3
    with dissolve

    a "But... who do I tell first?"

    menu:
        "Tell Ella first":
            
            #### Screen 4: Sharing with Ella (Choice: Ella)
            #- **Setting**: Park bench outside.
            #- **Description**: Amelia sitting with Ella, showing her the letter.
            #- **Dialogue**: "Ella, look! I'm going to Plymouth!"#
            $ SD += 1
            show screen_4
            with dissolve
            a "Ella, look! I'm going to Plymouth!"
            $renpy.notify("SD + 1")

            e "Whaaaa... That is amazing!"
            e "That's amazing, Millie! I knew you could do it!"
            e "I'm so proud of you. You've worked so hard for this."
            a "Thank you, Ella. Your support means everything to me."
            e "Of course, you know I'll always be here for you. Even if we're miles apart."
            a "I know. It's going to be tough being away from you and everyone here."
            e "Hey, don't worry. We'll stay in touch. Weekly video calls, daily texts, care packages - the works!"
            a "Definitely! I'm going to spam you with so many photos of my new life."
            e "And I'll be living vicariously through all of them! But seriously, Millie, you're going to have the best time."
            a "I hope so. I'm excited but also pretty nervous. It's a big change."
            e "That's totally normal. But I know you, and I know you're going to thrive. You've got this."
            a "Thanks, Ella. I needed to hear that. I'm really going to miss our daily chats though."
            e "Me too. But hey, absence makes the heart grow fonder, right? Our friendship can handle a little distance."
            a "Absolutely. Best friends forever, no matter what."
            e "Exactly. Now, let's make the most of the time we have left. I'm thinking movie marathon and junk food this weekend?"
            a "You read my mind! It's a date."
            e "Perfect. And Millie? I'm really, really happy for you. You deserve this."
            a "Thanks, Ella. I love you."

            show screen_8
            with dissolve
            a "Mum, Dad, Plymouth said YES!"

            p "We always knew you'd make it, darling."
            p "Congratulations, sweetheart! This is wonderful news."
            a "I can hardly believe it. I'm going to university!"
            p "We're so proud of you, Amelia. You've put in so much hard work."
            a "I couldn't have done it without your support. Thank you for always believing in me."
            p "Of course, honey. We'll always be your biggest cheerleaders."
            a "I know. I'm so grateful for you both."
            p "And we're grateful to have such an amazing daughter. You're going to do great things, Amelia."
            a "I hope so. I want to make you proud."
            p "You already have, sweetheart. Every single day."
            a "Thanks, Mum. Thanks, Dad. I love you both so much."
            p "We love you too, Amelia. More than words can say."
            a "I'm going to miss you when I'm away at university."
            p "We'll miss you too, honey. But we're only a phone call away, always."
            a "I know. And I'll come home to visit as often as I can."
            p "Good. Because this will always be your home, no matter where life takes you."
            a "That means a lot. Thank you."
            p "Now, I think this calls for a celebration! How about we go out for your favorite dinner tonight?"
            a "Really? That sounds perfect!"
            p "Anything for our university-bound girl. We're so excited for you, Amelia."
            a "Me too. I can't wait to start this new chapter. But I'll always be thankful for the love and support I have here."
            p "And you'll always have it, sweetheart. Always."

            #### Screen 11: Imagined Adventures
            #- **Setting**: Amelia's bedroom.
            #- **Description**: Amelia laying down, deep in daydreams.
            #- **Dialogue**: "University life... I wonder what it'll be like."#

            show screen_11
            with dissolve
            a "University life... I wonder what it'll be like"


            #### Screen 12: Texted Plans
            #- **Description**: Amelia's phone vibrates with a new message.
            #- **Text Notification**: Ella: "Let's meet up before you leave?"#

            #show screen_12
            #with dissolve
            #e "Let's meet up before you leave?"


        "Tell Parents first":
            #### Screen 8: Parents' Joy (Choice: Parents)
            #- **Setting**: Amelia's living room.
            #- **Description**: Amelia displaying the letter to her parents.
            #- **Dialogue**: "Mum, Dad, Plymouth said YES!"#
            $ SI += 1
            show screen_8
            with dissolve
            a "Mum, Dad, Plymouth said YES!"
            $renpy.notify("SI + 1")

            p "We always knew you'd make it, darling."
            p "Congratulations, sweetheart! This is wonderful news."
            a "I can hardly believe it. I'm going to university!"
            p "We're so proud of you, Amelia. You've put in so much hard work."
            a "I couldn't have done it without your support. Thank you for always believing in me."
            p "Of course, honey. We'll always be your biggest cheerleaders."
            a "I know. I'm so grateful for you both."
            p "And we're grateful to have such an amazing daughter. You're going to do great things, Amelia."
            a "I hope so. I want to make you proud."
            p "You already have, sweetheart. Every single day."
            a "Thanks, Mum. Thanks, Dad. I love you both so much."
            p "We love you too, Amelia. More than words can say."
            a "I'm going to miss you when I'm away at university."
            p "We'll miss you too, honey. But we're only a phone call away, always."
            a "I know. And I'll come home to visit as often as I can."
            p "Good. Because this will always be your home, no matter where life takes you."
            a "That means a lot. Thank you."
            p "Now, I think this calls for a celebration! How about we go out for your favorite dinner tonight?"
            a "Really? That sounds perfect!"
            p "Anything for our university-bound girl. We're so excited for you, Amelia."
            a "Me too. I can't wait to start this new chapter. But I'll always be thankful for the love and support I have here."
            p "And you'll always have it, sweetheart. Always."

            #### Screen 11: Imagined Adventures
            #- **Setting**: Amelia's bedroom.
            #- **Description**: Amelia laying down, deep in daydreams.
            #- **Dialogue**: "University life... I wonder what it'll be like."#

            show screen_11
            with dissolve
            a "University life... I wonder what it'll be like"


            #### Screen 4: Sharing with Ella (Choice: Ella)
            #- **Setting**: Park bench outside.
            #- **Description**: Amelia sitting with Ella, showing her the letter.
            #- **Dialogue**: "Ella, look! I'm going to Plymouth!"#

            show screen_4
            with dissolve
            e "Whaaaa... That is amazing!"
            e "That's amazing, Millie! I knew you could do it!"
            e "I'm so proud of you. You've worked so hard for this."
            a "Thank you, Ella. Your support means everything to me."
            e "Of course, you know I'll always be here for you. Even if we're miles apart."
            a "I know. It's going to be tough being away from you and everyone here."
            e "Hey, don't worry. We'll stay in touch. Weekly video calls, daily texts, care packages - the works!"
            a "Definitely! I'm going to spam you with so many photos of my new life."
            e "And I'll be living vicariously through all of them! But seriously, Millie, you're going to have the best time."
            a "I hope so. I'm excited but also pretty nervous. It's a big change."
            e "That's totally normal. But I know you, and I know you're going to thrive. You've got this."
            a "Thanks, Ella. I needed to hear that. I'm really going to miss our daily chats though."
            e "Me too. But hey, absence makes the heart grow fonder, right? Our friendship can handle a little distance."
            a "Absolutely. Best friends forever, no matter what."
            e "Exactly. Now, let's make the most of the time we have left. I'm thinking movie marathon and junk food this weekend?"
            a "You read my mind! It's a date."
            e "Perfect. And Millie? I'm really, really happy for you. You deserve this."
            a "Thanks, Ella. I love you."


            jump preparing_for_university

label preparing_for_university:
    #play music "chapter_1.mp3" fadein 3.0 volume 0.5
    scene amelia_room_packing
    with dissolve

    a "There's so much to pack. I need to be organized."

    show amelia_room_closet
    with dissolve

    a "Okay, let's see. Clothes, toiletries, bedding... what else?"

    show amelia_room_bookshelf
    with dissolve

    menu:
        "Organize her study materials":
            $ AA += 1
            show amelia_room_study
            with dissolve
            a "Oh, my books! I can't forget those. And my laptop, of course."
            $renpy.notify("AA + 1")
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
            $renpy.notify("SI + 1")
            show ella_phone_screen
            with dissolve
            e "That's amazing, Amelia! I'm so happy for you. We'll definitely keep in touch."
            show amelia_phone_call_2
            with dissolve
            a "Thanks, Ella. Your support means the world to me."
            e "You'll do great. Just remember to have fun too!"
            e "Let's meet by the tea house later yeah?"
            a "Great idea Ella, I'll see you there!."
            show amelia_phone_call_end
            with dissolve
            a "Talking to Ella always makes me feel better. I'm lucky to have her as a friend."

        "Meditate to calm her nerves":
            $ MH += 1
            show amelia_meditation
            with dissolve
            n "Amelia took a deep breath and sat down to meditate. She focused on her breathing, letting the calm wash over her."
            $renpy.notify("MH + 1")
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
    a "I should probably make a list, so I don't forget anything important."
    a "I wonder what the dorms will be like? I hope my roommate is nice."
    a "It's going to be strange living away from home. But it's all part of the experience, I guess."
    a "I'm excited, but I'm also kind of nervous. It's a big change."
    a "But I know I'm ready for this. I've been preparing for it for so long."
    a "I just need to stay organized and focused. I've got this."
    a "Right, time to start packing. One step at a time."
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
            p "So, Amelia, are you excited about starting university?"
            $renpy.notify("MC + 1")
            a "I am! It's a bit overwhelming, but I'm really looking forward to it."
            p "That's great, honey. It's normal to feel a mix of emotions."
            a "Yeah, I'm excited about the classes and meeting new people, but I'm also nervous about being on my own."
            p "That's understandable. But remember, we're always here for you, no matter what."
            a "I know. And I'm so grateful for that."

            show dinner_future_plans_2
            with dissolve
            p "Have you thought about what you want to study? I know you've always been interested in psychology."
            a "Definitely. I want to learn more about how the mind works and how I can help people."
            p "That's a wonderful ambition, Amelia. You have such a kind heart."
            a "Thanks, Dad. I just want to make a difference, you know?"
            p "You will, sweetheart. We have no doubt about that."
            a "I hope so. I'm going to work really hard."
            p "We know you will. But don't forget to take care of yourself too, okay?"
            a "I won't. I promise."

        "Ask for advice from her parents":
            $ SI += 1
            show dinner_ask_advice
            with dissolve
            a "Do you have any advice for me? I want to make the most of my time at university."
            $renpy.notify("SI + 1")
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
            $renpy.notify("MH + 1")
            p "We're so proud of you, Amelia. You're going to do great things."
            show dinner_gratitude_2
            with dissolve
            a "I'll make you proud."
            p "You already have, sweetheart."

    show dinner_conversation
    with dissolve

    a "I'm going to miss these family dinners."

    p "We'll miss you too, but we know you're going to do great."

    a "I'm heading out to meet Ella, I'll be back later."

    p "Okay hun, don't stay out too late"

    jump afternoon_tea_with_ella

label afternoon_tea_with_ella:
    scene tea_house
    with dissolve

    e "I'm going to miss our afternoon teas. But I'm so excited for you!"
    a "I'll miss this too. We need to stay in touch."
    e "Definitely! I want to hear all about your university adventures."
    a "I'll make sure to call you all the time. And we can still have virtual tea dates!"
    e "Yes! It won't be the same, but it's something. I'm just so proud of you, Amelia."

    show tea_conversation
    with dissolve

    menu:
        "Discuss university plans":
            $ SI += 1
            show tea_university_plans
            with dissolve
            a "I've been thinking about my schedule and the classes I'm going to take. It's going to be intense, but I'm ready."
            $renpy.notify("SI + 1")
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
            $renpy.notify("MH + 1")
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
            $renpy.notify("SD + 1")
            e "It's normal to feel that way, but you're going to make new friends and have amazing experiences. Trust yourself."
            show tea_share_fears_2
            with dissolve
            a "Thanks, Ella. Your support means so much to me."
            e "You'll do great. Just be yourself."

    show tea_goodbye
    with dissolve

    a "Thanks, Ella. That means a lot."
    e "You've dreamed about this for so long. And now it's finally happening."
    a "I know. It's surreal. But I'm ready. At least, I think I am."
    e "Of course you are! You're Amelia freaking Johnson! You can handle anything."
    a "Ha, I'm not sure about that. But I'll certainly try my best."
    e "That's all anyone can ask. And remember, if you ever need anything, I'm just a phone call away."
    a "I know. You're the best friend anyone could ask for."
    e "Right back at you. Now, let's enjoy this tea and make some more memories before you go off and become a superstar psychologist."
    a "Sounds perfect. Cheers to new beginnings!"
    e "Cheers!"


    jump exploring_the_museum

label exploring_the_museum:
    scene museum_entrance
    with dissolve

    n "As Amelia and Ella parted ways for the way, Amelia thought she might unwind at the museum."

    n "Amelia wandered through the exhibits, taking in the history and culture."

    show museum_hall
    with dissolve

    menu:
        "Learn about human evolution":
            $ AA += 1
            show museum_human_evolution
            with dissolve
            n "Amelia spent time in the anthropology section, fascinated by the development of the human species."
            $renpy.notify("AA + 1")
            a "It's amazing how much we've evolved over time."
            show museum_human_evolution_2
            with dissolve
            a "I know I want to help people, to understand them better. Psychology feels like the right path for that."
            a "But there's still so much I have to learn. About the world, about myself."
            a "I guess that's what university is for, right? To grow and discover."
            a "I'm excited for the journey, even if it's a little scary."
            a "But places like this remind me of why I'm doing it. To understand the human experience, in all its complexity."
            show museum_human_evolution_3
            with dissolve
            n "The detailed exhibits provided a lot of insight and sparked Amelia's curiosity even more."

        "Study ancient artifacts":
            $ SD += 1
            show museum_ancient_artifacts
            with dissolve
            n "Amelia explored the exhibits on ancient civilizations, pondering the wisdom they held."
            $renpy.notify("SD + 1")
            a "There's so much we can learn from the past."
            show museum_ancient_artifacts_2
            with dissolve
            a "The anthropology exhibit is fascinating. To think about how much we've evolved over time..."
            a "And these ancient artifacts! They hold so much history and wisdom."
            a "It's humbling, isn't it? To see the span of human existence laid out like this."
            a "It makes me think about my own place in the world. What kind of impact do I want to have?"
            show museum_ancient_artifacts_3
            with dissolve
            n "The intricate designs and historical significance of each piece captivated her."

        "Reflect on the nature of humanity":
            $ MH += 1
            show museum_reflect_humanity
            with dissolve
            n "The exhibits inspired Amelia to think deeply about what it means to be human and the complexities of our existence."
            $renpy.notify("MH + 1")
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

    a "I love this spot. The river always makes me feel so peaceful."
    a "There's something about watching the water flow by. It's like it puts everything into perspective."
    a "All the changes happening in my life... they're just part of the current, you know?"
    a "I have to trust that I'm being carried in the right direction."
    a "Even if there are rapids and obstacles along the way, I'll get through them."
    a "I've got my family, my friends, my own strength to rely on."
    a "And moments like these, to remind me of the beauty in the world."
    a "I should write some of this down. Capture this feeling."
    a "Maybe I'll come back here whenever I need to clear my head."

    show thames_sunset
    with dissolve

    menu:
        "Watch the sunset":
            $ SD += 1
            show thames_sunset_closeup
            with dissolve
            n "Amelia watched the colors of the sky change, feeling inspired and hopeful about the future."
            $renpy.notify("SD + 1")
            a "This is so beautiful. It's like the world is full of endless possibilities."
            show thames_sunset_end
            with dissolve
            a "I need to hold onto this feeling of peace and carry it with me."

        "Write in her journal":
            $ MH += 1
            show thames_journal
            with dissolve
            n "Amelia took out her journal and wrote down her thoughts and feelings, helping her process her emotions."
            $renpy.notify("MH + 1")
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
            $renpy.notify("AA + 1")
            a "Everyone has their own story. I can't wait to learn more about what makes us all tick."
            show thames_people_watching_closeup
            with dissolve
            a "These observations will be useful in my studies."
            show thames_people_watching_end
            with dissolve
            a "Understanding behavior is key to understanding the mind."


    show thames_exit
    with dissolve
    a "Okay, the sun is starting to set. Time for one more stop."
    n "As the sun set over the river, Amelia felt a sense of peace."
    a "That was refreshing. Now, to the bookstore for some last-minute shopping."

    jump browsing_the_bookstore

label browsing_the_bookstore:
    scene bookstore
    with dissolve

    n "Amelia wandered through the aisles of the quaint bookstore, feeling at home among the shelves of books."
    a "I could live in bookstores. The smell of books, the endless possibilities on every shelf..."

    show bookstore_aisles
    with dissolve

    menu:
        "Explore the psychology section":
            $ AA += 1
            show bookstore_psychology
            with dissolve
            n "Amelia browsed through the latest psychology books, feeling inspired by the wealth of knowledge."
            $renpy.notify("AA + 1")
            a "Ooh, the psychology section! Let's see what they've got."
            show bookstore_psychology_closeup
            with dissolve
            a "I'll get this one on cognitive psychology and this one on developmental stages."
            a "So many fascinating topics... cognitive psychology, developmental stages, behavioral analysis..."
            a "I'll definitely need to stock up before I leave. These will be great resources."
            a "There's so much to learn. I can't wait to dive into these books."
            show bookstore_psychology_end
            with dissolve
            a "These will be great resources for my studies."

        "Wander into the occult section":
            $ OK += 1
            show bookstore_occult
            with dissolve
            n "Amelia found herself intrigued by ancient texts and mystical books, sparking a curiosity for the unknown."
            $renpy.notify("? + 1")
            a "Huh, the occult section. That's intriguing."
            a "I've always been curious about ancient wisdom and mystical traditions."
            a "Maybe I'll grab a few of these, just for some light reading."
            show bookstore_occult_closeup
            with dissolve
            a "This one on alchemy and this one on ancient wisdom seem interesting, yet.. complex?"
            show bookstore_occult_end
            with dissolve
            a "I'll add these to my collection and explore them when I have time."

        "Buy a meditation guide":
            $ SD += 1
            show bookstore_meditation
            with dissolve
            n "Amelia purchased a book on meditation, eager to explore mindfulness practices."
            $renpy.notify("SD + 1")
            a "This should help me stay calm and focused during my studies."
            show bookstore_meditation_closeup
            with dissolve
            a "Oh, and a meditation guide! That could come in handy with the stress of university."
            a "I'll start with this beginner's guide and work my way up."
            show bookstore_meditation_end
            with dissolve

            a "I'll need all the tools I can get to stay balanced."
            a "Okay, I think this is plenty for now. My suitcase might burst at the seams!"
            a "But you can never have too many books, right?"

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
    a "What a day. I can't believe tomorrow is the start of everything."
    a "It feels like I've been waiting for this moment forever, and now it's here."
    a "I wonder what university will really be like? Will I make friends easily? Will the classes be as interesting as I hope?"
    a "I guess there's no way to know until I'm there, living it."
    a "That's the exciting part, isn't it? The unknown, the possibilities."
    a "Even if it's scary, it's also thrilling. Like standing on the edge of a cliff, ready to fly."
    a "I know there will be challenges. Moments of doubt, of homesickness, of stress."
    a "But I also know I'm ready to face them. I've been preparing for this, not just academically, but emotionally too."
    a "The conversations with Mum and Dad, with Ella... they've given me strength."
    a "And the things I've learned about myself... at the museum, by the river, in the bookstore... they've shown me that I'm capable of growth, of reflection, of resilience."
    a "I have tools now, tools I didn't have before. Meditation, writing, observing... ways to process and understand the world around me."
    a "And most importantly, I have a sense of purpose. A drive to learn, to help, to make a difference."
    a "That's what will guide me through whatever comes next."
    a "So, as much as part of me wants to cling to the familiarity of home... I know it's time."
    a "Okay, Amelia. Time to sleep. Tomorrow... tomorrow is the first day of the rest of your life."

    show amelia_bedroom_night_window
    with dissolve

    a "Time to let go, to trust myself, to embrace the journey ahead."
    a "Goodnight, London. Thank you for all you've taught me."
    a "And good morning, Plymouth. I can't wait to see what lessons you have in store."

    stop music fadeout 1.0

    return

    # jump call_to_adventure
