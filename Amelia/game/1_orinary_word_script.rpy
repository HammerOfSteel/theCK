# todos:
# 0. Fix chapter 2, 3 keywords to match chapter 1 and 12 syntax
# 1. Fix music variance for chapter 1, it need more songs and at better intervals
# 2. All other endings (OK ending is done)
# 3. Chapter 4
# 4. Chapter 5
# 5. Chapter 6
# 6. Chapter 7
# 7. Chapter 8
# 8. Chapter 9
# 9. Chapter 10
# 10. Chapter 11
# 11. Chapter 12 begining

# Backgrounds
# scene bg childhood_room
# scene bg highschool
# scene bg univerity_dream
# scene bg university_dream_envelope
# scene bg london_home_bedroom
# scene bg london_home_park
# scene bg london_home_livingroom
# scene bg university_life_dream

# Characters
# show amelia_kid
# show amelia_highschooler
# show amelia_highschooler_hopeful
# show amelia_surprised
# show amelia_happy
# show amelia_thinking
# show amelia_happy
# show ella
# show ella_proud
# show amelia_thankful
# show amelia
# show ella_happy
# show mom_happy
# show dad_happy
# show amelia_excited
# show mom_proud
# show dad_proud
# show mom
# show dad
# show amelia_thinking

# Define characters
define n = Character("", window_style="window_n", what_xpos=470, what_ypos=+25, what_text_align=0.0, who_xpos=+400, who_ypos=+15)
define a = Character("Amelia", window_style="window", what_xpos=30, what_text_align=0.0, who_xpos=-180, who_ypos=+15)
define amelia = Character("Amelia", window_style="window", what_xpos=30, what_text_align=0.0, who_xpos=-180, who_ypos=+15)
define e = Character("Ella", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define ella = Character("Ella", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define lily = Character("Lily", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define j = Character("James", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define p = Character("Parents", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define student = Character("Student", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define roommate = Character("Liz", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define mom = Character("Mom", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define dad = Character("Dad", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define staff = Character("Staff", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define professor = Character("Professor", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define woman = Character("Mysterious woman", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define m = Character("Maya", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define l = Character("Lucas", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define liz = Character("Liz", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define instructor = Character("Instructor", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define scientist = Character("Scientist", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define zara = Character("Zara", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define sarah = Character("Sarah", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define student_2 = Character("Student", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define lucas = Character("Lucas", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define lucas_text = Character("Lucas", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define credit_text = Character(window_style="window_c", what_xpos=620, what_text_align=0.0, who_xpos=+400, who_ypos=+15)
define hawthorne = Character("Hawthorne", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define raj = Character("Raj", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)


default art_style = "default"

default AA = 0
default SI = 0
default MH = 0
default SD = 0
default MC = 0
default OK = 0
default told_ella = 0
default told_parents = 0
default mentor = "None"
default sarah_alive = 0

#Academic Achievement (AA) - Points accumulated based on Amelia's academic performance and her dedication to studies.
#Social Interaction (SI) - Points based on Amelia's relationships with friends, mentors, and other characters.
#Mental Health (MH) - Points reflecting Amelia's mental well-being, affected by her ability to cope with stress, depression, and personal challenges.
#Self-Discovery (SD) - Points representing Amelia's exploration of psychology, ancient wisdom, Zen, and personal growth.
#Moral Choices (MC) - Points determined by Amelia's ethical and moral decisions throughout the story.
#Occult Knowledge (OK) - Points gathered by Amelia exploring deeper occult, alchemical, and ancient wisdom themes.

define music.second_child_restless_child = "second_child_restless_child.mp3"
define music.soldier_poet_king = "soldier_poet_king.mp3"
define music.chapter_2 = "chapter_2.mp3"
define music.drinking_song_for_the_socially_anxious = "drinking_song_for_the_socially_anxious.mp3"
define music.inkpot_gods = "inkpot_gods.mp3"
define music.sand = "sand.mp3"
define music.birds_of_a_feather = "birds_of_a_feather.mp3"
define music.liar_and_a_thief = "liar_and_a_thief.mp3"
define music.come_with_me = "come_with_me.mp3"
define music.super_trouper = "super_trouper.mp3"
define music.eurus = "eurus.mp3"
define music.homegrown = "homegrown.mp3"
define music.run_run_run = "run_run_run.mp3"
define music.ghost = "ghost.mp3"
define music.junk_of_the_heart = "junk_of_the_heart.mp3"
define music.closer_to_the_heart = "closer_to_the_heart.mp3"

transform fix_size: 
    zoom 1.42 #adjust as required
    center

transform half_size_center: 
    zoom 0.5 #adjust as required
    center
transform half_size_left: 
    zoom 0.5 #adjust as required
    left
transform half_size_right: 
    zoom 0.5 #adjust as required
    right
   

transform third_size_center: 
    zoom 0.75 #adjust as required
    center
transform third_size_left: 
    zoom 0.75 #adjust as required
    left
transform third_size_right: 
    zoom 0.75 #adjust as required
    right


transform quarter_size_center:
    zoom 0.25 #adjust as required
    center
transform quarter_size_left:
    zoom 0.25 #adjust as required
    left
transform quarter_size_right:
    zoom 0.25 #adjust as required
    right

# The game starts here.
label start:
    stop music
    scene black
    $ renpy.notify(f"AA {AA} - SI {SI} - MH {MH} - SD {SD} - MC {MC} - OK {OK}")
    show thames_sunset_end
    with dissolve

    menu:
        "Chapter selection 1-6":
            hide thames_sunset_end
            jump chapter_selection_1_6

        #"Chapter selection 7-12":
        #    hide thames_sunset_end
        #    jump chapter_selection_7_12
        
        "Ending selection":
            hide thames_sunset_end
            jump ending_selection

        "Credits selection":
            hide thames_sunset_end
            jump ending_credits

label chapter_selection_1_6:
    scene black
    show thames_sunset_end
    with dissolve
    menu:
        "Go to start of chapter 1":
            hide thames_sunset_end
            jump start_chapter_1
            window hide   
           
        "Go to chapter2":
            hide thames_sunset_end
            jump call_to_adventure
            window hide

        "Go to chapter3":
            hide thames_sunset_end
            jump chapter_3_part_1
            window hide

        "Go to chapter12":
            hide thames_sunset_end
            jump chapter_12_part_1
            window hide
        #"Go to chapter4":
        #    hide thames_sunset_end
        #    jump chapter_4_part_1

        #"Go to chapter5":
        #    hide thames_sunset_end
        #    jump chapter_5_part_1

        #"Go to chapter6":
        #    hide thames_sunset_end
        #    jump chapter_6_part_1


#label chapter_selection_7_12:
    #scene black
    #show thames_sunset_end
    #with dissolve
    #menu:
        #"Go to chapter7":
        #    hide thames_sunset_end
        #    jump chapter_7_part_1

        #"Go to chapter8":
        #    hide thames_sunset_end
        #    jump chapter_8_part_1

        #"Go to chapter9":
        #    hide thames_sunset_end
        #    jump chapter_9_part_1

        #"Go to chapter10":
        #    hide thames_sunset_end
        #    jump chapter_10_part_1

        #"Go to chapter11":
        #    hide thames_sunset_end
        #    jump chapter_11_part_1

        #"Go to chapter12":
        #    hide thames_sunset_end
        #    jump chapter_12_part_1

label ending_selection:
    scene black
    show thames_sunset_end
    with dissolve
    menu:
        #"Go to AA ending":
        #    hide thames_sunset_end
        #    jump chapter_12_academic_success

        #"Go to SI ending":
        #    hide thames_sunset_end
        #    jump chapter_12_social_butterfly

        #"Go to MH ending":
        #    hide thames_sunset_end
        #    jump chapter_12_mental_health_advocate

        #"Go to SD ending":
        #    hide thames_sunset_end
        #    jump chapter_12_balanced_growth

        #"Go to MC ending":
        #    hide thames_sunset_end
        #    jump chapter_12_tragic_ending

        "Go to AS ending":
            hide thames_sunset_end
            jump chapter_12_academic_success
            window hide

        "Go to OK ending":
            hide thames_sunset_end
            jump chapter_12_enlightenment
            window hide

        "Go to SB ending":
            hide thames_sunset_end
            jump chapter_12_social_butterfly
            window hide
        
        "Go to MH ending":
            hide thames_sunset_end
            jump chapter_12_mental_health_advocate
            window hide

        "Go to Tragic ending":
            hide thames_sunset_end
            jump chapter_12_tragic_ending
            window hide

label ending_credits:
    scene black
    show thames_sunset_end
    with dissolve
    menu:

        "Go to AS credits":
            hide thames_sunset_end
            jump as_ending_credits
            window hide

        "Go to OK credits":
            hide thames_sunset_end
            jump ok_ending_credits
            window hide

        "Go to SB credits":
            hide thames_sunset_end
            jump sb_ending_credits
            window hide

        "Go to MH credits":
            hide thames_sunset_end
            jump mh_ending_credits
            window hide

        "Go to Tragic credits":
            hide thames_sunset_end
            jump te_ending_credits
            window hide

label start_chapter_1:
    window hide
    play music second_child_restless_child fadein 1.0 volume 0.5

    #pause 4.0
    scene black
    show childhood_room_2
    #scene bg childhood_room_4
    show amelia_kid_5 at half_size_center
    #show amelia_kid_2 at center
    with dissolve
    n "Amelias curiosity about the mind began in a room of dreams and playful experiments."
    hide amelia_kid_5
    window hide   

    show highschool_4
    #scene bg highschool
    show amelia_highschooler_5 at third_size_center
    #show amelia_highschooler_3 at center
    with dissolve
    n "High school was a theater of emotions and social hierarchies; a ripe field for observation"
    hide amelia_highschooler_5
    window hide

    show university_dream_2
    show amelia_highschooler_hopeful_2 at third_size_left 
    with dissolve
    n "University, a beacon of hope, promising a sanctuary where curiosity intertwines with opportunit"
    hide amelia_highschooler_hopeful_2
    window hide

    show university_dream
    with dissolve
    n "With every passing moment, the future lingered, veiled in an envelope yet to arrive."
    window hide

    stop music fadeout 2.0
    jump getting_the_envelop

label getting_the_envelop:
    scene black
    show london_home_bedroom_3
    #scene bg london_home_bedroom_4
    show amelia_surprised_3 at half_size_center
    #show amelia_surprised_4 at center
    with dissolve
    play music soldier_poet_king fadein 2.0 volume 0.5
    a "I got in! I actually got in!"
    a "Holy moly, this is the best ever!"
    hide amelia_surprised_3
    window hide

    show amelia_excited_7 at center
    #show amelia_excited_6 at center
    with dissolve
    a "Whooohooo!"
    a "Plymouth, here I come!"
    hide amelia_excited_7
    window hide

    show amelia_wonder at right
    with dissolve
    a "But... who do I tell first?"

    menu:
        "Tell Ella first":
            hide amelia_wonder
            jump tell_ella

        "Tell Parents first":
            hide amelia_wonder
            jump tell_parents

label tell_ella:
    #### Screen 4: Sharing with Ella (Choice: Ella)
    #- **Setting**: Park bench outside.
    #- **Description**: Amelia sitting with Ella, showing her the letter.
    #- **Dialogue**: "Ella, look! I'm going to Plymouth!"#
    scene black
    $ told_ella += 1
    $ SD += 1
    window hide
    show london_home_park_2

    show amelia_happy at left
    with dissolve
    a "Ella, look! I'm going to Plymouth!"
    $renpy.notify("SD + 1")
    window hide

    show ella_neutral at right
    with dissolve
    e "Whaaaa... That is amazing!"
    e "That's amazing, Millie! I knew you could do it!"
    hide ella_neutral
    window hide

    show ella_neutral_2 at right
    with dissolve
    e "I'm so proud of you. You've worked so hard for this."
    window hide

    hide amelia_happy
    show amelia_grateful_t at left
    with dissolve
    a "Thank you, Ella. Your support means everything to me."
    e "Of course, you know I'll always be here for you. Even if we're miles apart."
    hide amelia_grateful_t
    window hide

    show amelia_contemplative at left
    with dissolve
    a "I know. It's going to be tough being away from you and everyone here."
    window hide

    hide ella_neutral_2
    show ella_neutral_3 at right
    with dissolve
    e "Hey, don't worry. We'll stay in touch. Weekly video calls, daily texts, care packages - the works!"
    window hide

    hide amelia_contemplative
    show amelia_calm at left
    with dissolve
    a "Definitely! I'm going to spam you with so many photos of my new life."
    e "And I'll be living vicariously through all of them! But seriously, Millie, you're going to have the best time."
    a "I hope so. I'm excited but also pretty nervous. It's a big change."
    e "That's totally normal. But I know you, and I know you're going to thrive. You've got this."
    a "Thanks, Ella. I needed to hear that. I'm really going to miss our daily chats though."
    e "Me too. But hey, absence makes the heart grow fonder, right? Our friendship can handle a little distance."
    a "Absolutely. Best friends forever, no matter what."
    e "Exactly. Now, let's make the most of the time we have left. I'm thinking movie marathon and junk food this weekend?"
    a "You read my mind! It's a date."
    window hide

    hide amelia_calm
    hide ella_neutral_3
    show amelia_happy at left
    show ella_neutral at right
    e "Perfect. And Millie? I'm really, really happy for you. You deserve this."
    a "Thanks, Ella. I love you."
    window hide
    hide amelia_happy
    hide ella_neutral

    if told_parents > 0:
        jump room_prepare
    else:
        jump tell_parents

label tell_parents:
    $ told_parents += 1
    scene black
    show london_home_livingroom_2

    show amelia_happy at half_size_left
    with dissolve
    a "Mum, Dad, Plymouth said YES!"

    show mom_optimistic at half_size_right
    with dissolve
    mom "We always knew you'd make it, darling."

    show dad_optimistic at half_size_center
    with dissolve
    dad "Congratulations, sweetheart! This is wonderful news."

    hide amelia_happy
    show amelia_excited at half_size_left
    with dissolve
    a "I can hardly believe it. I'm going to university!"

    hide mom_optimistic
    hide dad_optimistic
    show mom_sincere at half_size_right
    with dissolve
    show dad_proud at half_size_center
    with dissolve
    p "We're so proud of you, Amelia. You've put in so much hard work."

    hide amelia_excited
    show amelia_surprised at half_size_left
    with dissolve
    a "I couldn't have done it without your support. Thank you for always believing in me."
    p "Of course, honey. We'll always be your biggest cheerleaders."
    a "I know. I'm so grateful for you both."
    p "And we're grateful to have such an amazing daughter. You're going to do great things, Amelia."
    a "I hope so. I want to make you proud."
    p "You already have, sweetheart. Every single day."

    hide amelia_surprised
    show amelia_neutral at half_size_left
    with dissolve
    a "Thanks, Mum. Thanks, Dad. I love you both so much."

    hide mom_sincere
    show mom_amused at half_size_right
    with dissolve
    with dissolve
    p "We love you too, Amelia. More than words can say."
    a "I'm going to miss you when I'm away at university."
    p "We'll miss you too, honey. But we're only a phone call away, always."
    a "I know. And I'll come home to visit as often as I can."
    p "Good. Because this will always be your home, no matter where life takes you."
    a "That means a lot. Thank you."
    p "Now, I think this calls for a celebration! How about we go out for your favorite dinner tonight?"

    hide amelia_neutral
    show amelia_excited at half_size_left
    with dissolve
    a "Really? That sounds perfect!"
    p "Anything for our university-bound girl. We're so excited for you, Amelia."

    hide amelia_excited
    show amelia_neutral at half_size_left
    with dissolve
    a "Me too. I can't wait to start this new chapter. But I'll always be thankful for the love and support I have here."
    p "And you'll always have it, sweetheart. Always."
    window hide

    hide amelia_neutral
    hide mom_amused
    hide dad_proud
    hide london_home_livingroom_2

    show university_dream_4
    show amelia_contemplative at half_size_right
    with dissolve
    a "University life... I wonder what it'll be like"
    window hide
    hide amelia_contemplative
    hide university_dream_4

    if told_ella > 0:
        jump room_prepare
    else:
        jump tell_ella

label room_prepare:
    scene black
    show london_home_bedroom_3
    show amelia_confident
    with dissolve
    a "There's so much to pack. I need to be organized."
    a "Okay, let's see. Clothes, toiletries, bedding... what else?"

    menu:
        "Organize her study materials":
            hide amelia_confident
            $ AA += 1
            window hide
            $renpy.notify("AA + 1")
            show amelia_happy
            with dissolve
            a "Oh, my books! I can't forget those. And my laptop, of course."
            n "Amelia carefully sorted her textbooks and notes, making sure everything was in order for her studies."
            a "These books will be my lifeline at university. I need to make sure I have everything."
            a "Notes, check. Pens and highlighters, check. Laptop, check."
            a "Alright, I think I'm all set academically. I feel a bit more prepared now."
            hide amelia_happy
            window hide

        "Call Ella to talk about her excitement":
            hide amelia_confident
            $ SI += 1
            window hide
            $renpy.notify("SI + 1")

            show amelia_phone_calling at half_size_right
            with dissolve
            show ella_phone_calling at half_size_left
            with dissolve
            a "Hi Ella! I just wanted to share how excited I am about Plymouth. I can't wait to start!"
            e "That's amazing, Amelia! I'm so happy for you. We'll definitely keep in touch."
            a "Thanks, Ella. Your support means the world to me."
            e "You'll do great. Just remember to have fun too!"
            e "Let's meet by the tea house later yeah?"
            a "Great idea Ella, I'll see you there!."
            hide amelia_phone_calling
            hide ella_phone_calling
            window hide

            show amelia_optimistic at third_size_center
            with dissolve
            a "Talking to Ella always makes me feel better. I'm lucky to have her as a friend."
            hide amelia_optimistic
            window hide

        "Meditate to calm her nerves":
            hide amelia_confident
            $ MH += 1
            window hide
            $renpy.notify("MH + 1")

            show amelia_grateful_t at half_size_center
            with dissolve
            n "Amelia took a deep breath and sat down to meditate. She focused on her breathing, letting the calm wash over her."
            a "I need to stay calm and focused. Everything will be fine."
            a "Inhale... exhale... Just let the tension go."
            n "With each breath, she felt her anxiety melting away, replaced by a sense of peace and readiness."
            a "I can do this. I'm ready for whatever comes next."
            hide amelia_grateful_t
            window hide

    show amelia_intrigued_t at third_size_center
    with dissolve
    a "I should probably make a list, so I don't forget anything important."
    a "I wonder what the dorms will be like? I hope my roommate is nice."
    a "It's going to be strange living away from home. But it's all part of the experience, I guess."
    a "I'm excited, but I'm also kind of nervous. It's a big change."
    a "But I know I'm ready for this. I've been preparing for it for so long."
    a "I just need to stay organized and focused. I've got this."
    a "Right, time to start packing. One step at a time."
    a "All done! Now to have dinner with my parents."
    hide amelia_intrigued_t
    show black
    window hide
    
    return
    #jump dinner_with_parents

# label dinner_with_parents:
#     show dinner_table
#     with dissolve
#     show 
#     p "So, Amelia, are you excited about starting university?"
#     a "I am! It's a bit overwhelming, but I'm really looking forward to it."
#     hide dinner_table
#     show black
#     window hide

#     show dinner_family_talking
#     with dissolve

#     menu:
#         "Discuss her future plans":
#             $ MC += 1
#             hide dinner_family_talking
#             show black
#             window hide

#             show dinner_future_plans
#             with dissolve
#             p "So, Amelia, are you excited about starting university?"
#             $renpy.notify("MC + 1")
#             a "I am! It's a bit overwhelming, but I'm really looking forward to it."
#             p "That's great, honey. It's normal to feel a mix of emotions."
#             a "Yeah, I'm excited about the classes and meeting new people, but I'm also nervous about being on my own."
#             p "That's understandable. But remember, we're always here for you, no matter what."
#             a "I know. And I'm so grateful for that."
#             hide dinner_future_plans
#             show black
#             window hide

#             show dinner_future_plans_2
#             with dissolve
#             p "Have you thought about what you want to study? I know you've always been interested in psychology."
#             a "Definitely. I want to learn more about how the mind works and how I can help people."
#             p "That's a wonderful ambition, Amelia. You have such a kind heart."
#             a "Thanks, Dad. I just want to make a difference, you know?"
#             p "You will, sweetheart. We have no doubt about that."
#             a "I hope so. I'm going to work really hard."
#             p "We know you will. But don't forget to take care of yourself too, okay?"
#             a "I won't. I promise."
#             hide dinner_future_plans_2
#             show black
#             window hide

#         "Ask for advice from her parents":
#             $ SI += 1
#             hide dinner_family_talking
#             show black
#             window hide

#             show dinner_ask_advice
#             with dissolve
#             a "Do you have any advice for me? I want to make the most of my time at university."
#             $renpy.notify("SI + 1")
#             p "Just be yourself, work hard, and don't be afraid to ask for help when you need it."
#             hide dinner_ask_advice
#             show black
#             window hide

#             show dinner_ask_advice_2
#             with dissolve
#             a "Thanks, Mom and Dad. I really appreciate your support."
#             p "Remember, it's okay to make mistakes. It's all part of the learning process."
#             hide dinner_ask_advice_2
#             show black
#             window hide

#         "Express her gratitude to her parents":
#             $ MH += 1
#             hide dinner_family_talking
#             show black
#             window hide

#             show dinner_gratitude
#             with dissolve
#             a "Thank you both for all your support. I couldn't have done this without you."
#             $renpy.notify("MH + 1")
#             p "We're so proud of you, Amelia. You're going to do great things."
#             hide dinner_gratitude
#             show black
#             window hide
            
#             show dinner_gratitude_2
#             with dissolve
#             a "I'll make you proud."
#             p "You already have, sweetheart."
#             hide dinner_gratitude_2
#             show black
#             window hide

#     show dinner_conversation
#     with dissolve
#     a "I'm going to miss these family dinners."
#     p "We'll miss you too, but we know you're going to do great."
#     a "I'm heading out to meet Ella, I'll be back later."
#     p "Okay hun, don't stay out too late"
#     hide dinner_conversation
#     show black
#     window hide
#     jump afternoon_tea_with_ella

# label afternoon_tea_with_ella:
#     scene tea_house
#     with dissolve
#     e "I'm going to miss our afternoon teas. But I'm so excited for you!"
#     a "I'll miss this too. We need to stay in touch."
#     e "Definitely! I want to hear all about your university adventures."
#     a "I'll make sure to call you all the time. And we can still have virtual tea dates!"
#     e "Yes! It won't be the same, but it's something. I'm just so proud of you, Amelia."
#     hide tea_house
#     show black
#     window hide

#     show tea_conversation
#     with dissolve

#     menu:
#         "Discuss university plans":
#             $ SI += 1
#             hide tea_conversation
#             show black
#             window hide

#             show tea_university_plans
#             with dissolve
#             a "I've been thinking about my schedule and the classes I'm going to take. It's going to be intense, but I'm ready."
#             $renpy.notify("SI + 1")
#             e "You’ve got this, Amelia. Just remember to take breaks and enjoy the experience."
#             hide tea_university_plans
#             show black
#             window hide

#             show tea_university_plans_2
#             with dissolve
#             a "I will. Thanks for the advice, Ella."
#             e "No problem! I'm here for you."
#             hide tea_university_plans_2
#             show black
#             window hide

#         "Reminisce about school days":
#             $ MH += 1
#             hide tea_conversation
#             show black
#             window hide

#             show tea_remember_school
#             with dissolve
#             a "Remember that time in high school when we stayed up all night studying for finals?"
#             $renpy.notify("MH + 1")
#             e "How could I forget? We were so stressed, but we made it through together."
#             hide tea_remember_school
#             show black
#             window hide

#             show tea_remember_school_2
#             with dissolve
#             a "Those were some tough times, but also some of the best memories."
#             e "Definitely. We'll make more memories, even with you away."
#             hide tea_remember_school_2
#             show black
#             window hide

#         "Share fears about the future":
#             $ SD += 1
#             hide tea_conversation
#             show black
#             window hide

#             show tea_share_fears
#             with dissolve
#             a "I have to admit, I'm a bit scared about moving and starting over. What if I don't fit in?"
#             $renpy.notify("SD + 1")
#             e "It's normal to feel that way, but you're going to make new friends and have amazing experiences. Trust yourself."
#             hide tea_share_fears
#             show black
#             window hide

#             show tea_share_fears_2
#             with dissolve
#             a "Thanks, Ella. Your support means so much to me."
#             e "You'll do great. Just be yourself."
#             hide tea_share_fears_2
#             show black
#             window hide

#     show tea_goodbye
#     with dissolve
#     a "Thanks, Ella. That means a lot."
#     e "You've dreamed about this for so long. And now it's finally happening."
#     a "I know. It's surreal. But I'm ready. At least, I think I am."
#     e "Of course you are! You're Amelia freaking Johnson! You can handle anything."
#     a "Ha, I'm not sure about that. But I'll certainly try my best."
#     e "That's all anyone can ask. And remember, if you ever need anything, I'm just a phone call away."
#     a "I know. You're the best friend anyone could ask for."
#     e "Right back at you. Now, let's enjoy this tea and make some more memories before you go off and become a superstar psychologist."
#     a "Sounds perfect. Cheers to new beginnings!"
#     e "Cheers!"
#     hide tea_goodbye
#     show black
#     window hide
#     jump exploring_the_museum

# label exploring_the_museum:
#     scene museum_entrance
#     with dissolve
#     n "As Amelia and Ella parted ways for the way, Amelia thought she might unwind at the museum."
#     n "Amelia wandered through the exhibits, taking in the history and culture."
#     hide museum_entrance
#     show black
#     window hide

#     show museum_hall
#     with dissolve

#     menu:
#         "Learn about human evolution":
#             $ AA += 1
#             hide museum_hall
#             show black
#             window hide

#             show museum_human_evolution
#             with dissolve
#             n "Amelia spent time in the anthropology section, fascinated by the development of the human species."
#             $renpy.notify("AA + 1")
#             a "It's amazing how much we've evolved over time."
#             hide museum_human_evolution
#             show black
#             window hide

#             show museum_human_evolution_2
#             with dissolve
#             a "I know I want to help people, to understand them better. Psychology feels like the right path for that."
#             a "But there's still so much I have to learn. About the world, about myself."
#             a "I guess that's what university is for, right? To grow and discover."
#             a "I'm excited for the journey, even if it's a little scary."
#             a "But places like this remind me of why I'm doing it. To understand the human experience, in all its complexity."
#             hide museum_human_evolution_2
#             show black
#             window hide

#             show museum_human_evolution_3
#             with dissolve
#             n "The detailed exhibits provided a lot of insight and sparked Amelia's curiosity even more."
#             hide museum_human_evolution_3
#             show black
#             window hide

#         "Study ancient artifacts":
#             $ SD += 1
#             hide museum_hall
#             show black
#             window hide

#             show museum_ancient_artifacts
#             with dissolve
#             n "Amelia explored the exhibits on ancient civilizations, pondering the wisdom they held."
#             $renpy.notify("SD + 1")
#             a "There's so much we can learn from the past."
#             hide museum_ancient_artifacts
#             show black
#             window hide

#             show museum_ancient_artifacts_2
#             with dissolve
#             a "The anthropology exhibit is fascinating. To think about how much we've evolved over time..."
#             a "And these ancient artifacts! They hold so much history and wisdom."
#             a "It's humbling, isn't it? To see the span of human existence laid out like this."
#             a "It makes me think about my own place in the world. What kind of impact do I want to have?"
#             hide museum_ancient_artifacts_2
#             show black
#             window hide

#             show museum_ancient_artifacts_3
#             with dissolve
#             n "The intricate designs and historical significance of each piece captivated her."
#             hide museum_ancient_artifacts_3
#             show black
#             window hide

#         "Reflect on the nature of humanity":
#             $ MH += 1
#             hide museum_hall
#             show black
#             window hide

#             show museum_reflect_humanity
#             with dissolve
#             n "The exhibits inspired Amelia to think deeply about what it means to be human and the complexities of our existence."
#             $renpy.notify("MH + 1")
#             a "What does it truly mean to be human? It's such a profound question."
#             hide museum_reflect_humanity
#             show black
#             window hide

#             show museum_reflect_humanity_2
#             with dissolve
#             a "I want to understand the deeper aspects of our nature."
#             hide museum_reflect_humanity_2
#             show black
#             window hide

#             show museum_reflect_humanity_3
#             with dissolve
#             n "Amelia felt a deep sense of connection with the human journey through time."
#             hide museum_reflect_humanity_3
#             show black
#             window hide

#     show museum_exit
#     with dissolve
#     a "That was enlightening. Time to head to the river for some fresh air."
#     hide museum_exit
#     show black
#     window hide
#     jump evening_by_the_thames

# label evening_by_the_thames:
#     scene thames_evening
#     with dissolve
#     a "I love this spot. The river always makes me feel so peaceful."
#     a "There's something about watching the water flow by. It's like it puts everything into perspective."
#     a "All the changes happening in my life... they're just part of the current, you know?"
#     a "I have to trust that I'm being carried in the right direction."
#     a "Even if there are rapids and obstacles along the way, I'll get through them."
#     a "I've got my family, my friends, my own strength to rely on."
#     a "And moments like these, to remind me of the beauty in the world."
#     a "I should write some of this down. Capture this feeling."
#     a "Maybe I'll come back here whenever I need to clear my head."
#     hide thames_evening
#     show black
#     window hide

#     show thames_sunset
#     with dissolve

#     menu:
#         "Watch the sunset":
#             $ SD += 1
#             hide thames_sunset
#             show black
#             window hide

#             show thames_sunset_closeup
#             with dissolve
#             n "Amelia watched the colors of the sky change, feeling inspired and hopeful about the future."
#             $renpy.notify("SD + 1")
#             a "This is so beautiful. It's like the world is full of endless possibilities."
#             hide thames_sunset_closeup
#             show black
#             window hide

#             show thames_sunset_end
#             with dissolve
#             a "I need to hold onto this feeling of peace and carry it with me."
#             hide thames_sunset_end
#             show black
#             window hide

#         "Write in her journal":
#             $ MH += 1
#             hide thames_sunset
#             show black
#             window hide

#             show thames_journal
#             with dissolve
#             n "Amelia took out her journal and wrote down her thoughts and feelings, helping her process her emotions."
#             $renpy.notify("MH + 1")
#             a "Writing always helps me clear my mind."
#             hide thames_journal
#             show black
#             window hide

#             show thames_journal_closeup
#             with dissolve
#             a "I feel more at ease now, putting my thoughts into words."
#             hide thames_journal_closeup
#             show black
#             window hide

#             show thames_journal_end
#             with dissolve
#             a "I'll look back on these notes whenever I need encouragement."
#             hide thames_journal_end
#             show black
#             window hide

#         "People-watch and observe behaviors":
#             $ AA += 1
#             hide thames_sunset
#             show black
#             window hide

#             show thames_people_watching
#             with dissolve
#             n "Amelia observed the people around her, practicing her skills of observation and thinking about the different aspects of human behavior."
#             $renpy.notify("AA + 1")
#             a "Everyone has their own story. I can't wait to learn more about what makes us all tick."
#             hide thames_people_watching
#             show black
#             window hide

#             show thames_people_watching_closeup
#             with dissolve
#             a "These observations will be useful in my studies."
#             hide thames_people_watching_closeup
#             show black
#             window hide

#             show thames_people_watching_end
#             with dissolve
#             a "Understanding behavior is key to understanding the mind."
#             hide thames_people_watching_end
#             show black
#             window hide


#     show thames_exit
#     with dissolve
#     a "Okay, the sun is starting to set. Time for one more stop."
#     n "As the sun set over the river, Amelia felt a sense of peace."
#     a "That was refreshing. Now, to the bookstore for some last-minute shopping."
#     hide thames_exit
#     show black
#     window hide
#     jump browsing_the_bookstore

# label browsing_the_bookstore:
#     scene bookstore
#     with dissolve
#     n "Amelia wandered through the aisles of the quaint bookstore, feeling at home among the shelves of books."
#     a "I could live in bookstores. The smell of books, the endless possibilities on every shelf..."
#     hide bookstore
#     show black
#     window hide

#     show bookstore_aisles
#     with dissolve

#     menu:
#         "Explore the psychology section":
#             $ AA += 1
#             hide bookstore_aisles
#             show black
#             window hide

#             show bookstore_psychology_closeup
#             with dissolve
#             n "Amelia browsed through the latest psychology books, feeling inspired by the wealth of knowledge."
#             $renpy.notify("AA + 1")
#             a "Ooh, the psychology section! Let's see what they've got."
#             hide bookstore_psychology_closeup
#             show black
#             window hide

#             show bookstore_psychology_closeup
#             with dissolve
#             a "I'll get this one on cognitive psychology and this one on developmental stages."
#             a "So many fascinating topics... cognitive psychology, developmental stages, behavioral analysis..."
#             a "I'll definitely need to stock up before I leave. These will be great resources."
#             a "There's so much to learn. I can't wait to dive into these books."
#             hide bookstore_psychology_closeup
#             show black
#             window hide

#             show bookstore_psychology_end
#             with dissolve
#             a "These will be great resources for my studies."
#             hide bookstore_psychology_end
#             show black
#             window hide

#         "Wander into the occult section":
#             $ OK += 1
#             hide bookstore_aisles
#             show black
#             window hide

#             show bookstore_occult
#             with dissolve
#             n "Amelia found herself intrigued by ancient texts and mystical books, sparking a curiosity for the unknown."
#             $renpy.notify("? + 1")
#             a "Huh, the occult section. That's intriguing."
#             a "I've always been curious about ancient wisdom and mystical traditions."
#             a "Maybe I'll grab a few of these, just for some light reading."
#             hide bookstore_occult
#             show black
#             window hide

#             show bookstore_occult_closeup
#             with dissolve
#             a "This one on alchemy and this one on ancient wisdom seem interesting, yet.. complex?"
#             hide bookstore_occult_closeup
#             show black
#             window hide

#             show bookstore_occult_end
#             with dissolve
#             a "I'll add these to my collection and explore them when I have time."
#             hide bookstore_occult_end
#             show black
#             window hide

#         "Buy a meditation guide":
#             $ SD += 1
#             hide bookstore_aisles
#             show black
#             window hide

#             show bookstore_meditation
#             with dissolve
#             n "Amelia purchased a book on meditation, eager to explore mindfulness practices."
#             $renpy.notify("SD + 1")
#             a "This should help me stay calm and focused during my studies."
#             hide bookstore_meditation
#             show black
#             window hide

#             show bookstore_meditation_closeup
#             with dissolve
#             a "Oh, and a meditation guide! That could come in handy with the stress of university."
#             a "I'll start with this beginner's guide and work my way up."
#             hide bookstore_meditation_closeup
#             show black
#             window hide

#             show bookstore_meditation_end
#             with dissolve
#             a "I'll need all the tools I can get to stay balanced."
#             a "Okay, I think this is plenty for now. My suitcase might burst at the seams!"
#             a "But you can never have too many books, right?"
#             hide bookstore_meditation_end
#             show black
#             window hide

#     show bookstore_exit
#     with dissolve
#     a "I think I have everything I need now. Time to head home and get some rest."
#     hide bookstore_exit
#     show black
#     window hide
#     jump ordinary_world_end

# label ordinary_world_end:
#     scene amelia_bedroom_night
#     with dissolve
#     n "As Amelia lay in bed, she felt a mix of excitement and nervousness. Tomorrow, she would embark on a new journey, leaving her old life behind."
#     hide amelia_bedroom_night
#     show black
#     window hide

#     show amelia_bedroom_night_closeup
#     with dissolve
#     a "What a day. I can't believe tomorrow is the start of everything."
#     a "It feels like I've been waiting for this moment forever, and now it's here."
#     a "I wonder what university will really be like? Will I make friends easily? Will the classes be as interesting as I hope?"
#     a "I guess there's no way to know until I'm there, living it."
#     a "That's the exciting part, isn't it? The unknown, the possibilities."
#     a "Even if it's scary, it's also thrilling. Like standing on the edge of a cliff, ready to fly."
#     a "I know there will be challenges. Moments of doubt, of homesickness, of stress."
#     a "But I also know I'm ready to face them. I've been preparing for this, not just academically, but emotionally too."
#     a "The conversations with Mum and Dad, with Ella... they've given me strength."
#     a "And the things I've learned about myself... at the museum, by the river, in the bookstore... they've shown me that I'm capable of growth, of reflection, of resilience."
#     a "I have tools now, tools I didn't have before. Meditation, writing, observing... ways to process and understand the world around me."
#     a "And most importantly, I have a sense of purpose. A drive to learn, to help, to make a difference."
#     a "That's what will guide me through whatever comes next."
#     a "So, as much as part of me wants to cling to the familiarity of home... I know it's time."
#     a "Okay, Amelia. Time to sleep. Tomorrow... tomorrow is the first day of the rest of your life."
#     hide amelia_bedroom_night_closeup
#     show black
#     window hide

#     show amelia_bedroom_night_window
#     with dissolve
#     a "Time to let go, to trust myself, to embrace the journey ahead."
#     a "Goodnight, London. Thank you for all you've taught me."
#     a "And good morning, Plymouth. I can't wait to see what lessons you have in store."
#     hide amelia_bedroom_night_window
#     show black
#     window hide

#     stop music fadeout 1.0
#     #$ renpy.notify(f"AA {AA} - SI {SI} - MH {MH} - SD {SD} - MC {MC} - OK {OK}")
#     jump call_to_adventure
