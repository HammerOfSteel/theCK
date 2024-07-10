define music.weight_of_gold = "weight_of_gold.mp3"
define music.i_have_made_mistakes = "i_have_made_mistakes.mp3"
define music.paperwork = "paperwork.mp3"

label chapter_12_part_1:
    show black
    window hide

    play music paperwork fadein 1.0 volume 0.8

    show amelia_returning_home
    with dissolve
    n "Amelia steps off the train at London’s bustling station, a wave of nostalgia washing over her. She sees her parents and Ella waiting eagerly, their smiles wide and welcoming."
    hide amelia_returning_home

    show black
    window hide
    show amelia_hugging_parents
    with dissolve
    n "Her parents envelop her in a warm embrace, and she feels the comfort of their familiar presence."
    dad "Welcome back, Amelia! We've missed you so much."
    mom "Look at you, all grown up and wiser."
    hide amelia_hugging_parents

    show black
    window hide   
    show amelia_smiling_happy
    with dissolve
    a "It's good to be home, Mom, Dad. I missed you both too."
    hide amelia_smiling_happy

    show black
    window hide   
    show ella_running_to_amelia
    with dissolve
    ella "Amelia! I've missed you so much!"
    hide ella_running_to_amelia

    show black
    window hide   
    show amelia_and_ella_hugging
    with dissolve
    a "Ella! I’ve missed you too. There’s so much to tell you."
    ella "Come on, let's get your bags and head home. I want to hear everything!"
    n "They spend the car ride home catching up, Ella bombarding Amelia with questions about university life."
    hide amelia_and_ella_hugging

    show black
    window hide   
    show car_ride_home
    with dissolve
    ella "So, how's Plymouth? Is it as beautiful as they say?"
    amelia "Absolutely, Ella. The campus is stunning, and the city has so much history and charm. I even visited some incredible places in Cornwall."
    ella "Oh, I'm so jealous! And how about the people? Did you make any good friends?"
    amelia "Yes, I did. There's Lucas, Zara, Raj, and Maya. We've all grown really close. And of course, my professors have been amazing."
    hide car_ride_home

    show black
    window hide   
    show amelia_smiling_reflecting
    with dissolve
    n "Back home, the James family sits around the living room, the atmosphere filled with joy and curiosity."
    mom "Tell us everything, darling. How was your first year?"
    hide amelia_smiling_reflecting

    show black
    window hide   
    show amelia_smiling_reflecting
    with dissolve
    a "It was... transformative. I learned so much, not just academically, but about myself."
    dad "We're so proud of you, Amelia. You've come a long way."
    hide amelia_smiling_reflecting

    show black
    window hide   
    show amelia_nodding_smile
    with dissolve
    a "Thank you. The experiences, the people I met, everything has contributed to my growth. It wasn't always easy, but it was worth it."
    mom "We could see the change in you the moment you stepped off the train. You've grown into such a strong, confident young woman."
    hide amelia_nodding_smile

    show black
    window hide   
    show amelia_blushing
    with dissolve
    a "Thanks, Mom. Your support meant everything to me. There were times I felt really overwhelmed, but knowing I had you all cheering for me kept me going."
    hide amelia_blushing

    jump reunion_with_ella

label reunion_with_ella:
    show black
    window hide   
    show amelia_in_room_with_ella
    with dissolve
    n "Later, at Ella’s house, the two friends sit in their favorite spot, reminiscing about old times and sharing new stories."
    ella "So, what’s the biggest change? You seem... different, in a good way."
    hide amelia_in_room_with_ella

    show black
    window hide   
    show amelia_smiling
    with dissolve
    a "I feel different. More confident, more aware of who I am and what I want to do. I guess facing so many challenges helped me discover my strengths."
    ella "I’m so proud of you, Amelia. You’re really becoming the person you were meant to be."
    hide amelia_smiling

    show black
    window hide      
    show amelia_thankful
    with dissolve
    a "Thanks, Ella. You've always believed in me, even when I didn't believe in myself. That means a lot."
    ella "Always. So, tell me more about your friends. They sound amazing."
    hide amelia_thankful

    show black
    window hide   
    show amelia_reflecting
    with dissolve
    a "They are. Lucas is my roommate, and he's into Jungian psychology, which is fascinating. Zara has faced a lot of racism but she's incredibly strong and insightful. Maya is into Zen philosophy, and she's helped me explore spiritual dimensions. And Raj is studying family systems, which has given me a lot of perspective on relationships."
    ella "Wow, it sounds like you have a diverse group of friends. It must be so enriching to learn from each other."
    hide amelia_reflecting

    show black
    window hide   
    show amelia_reflecting
    with dissolve
    a "It is. We've all supported each other through some tough times, especially with Sarah... She's had a really hard year, and we've all tried to be there for her."
    hide amelia_nodding

    jump family_dinner

label family_dinner:
    show black
    window hide   
    show amelia_family_dinner
    with dissolve
    n "At the family dinner that night, Amelia's parents toast to her successful year."
    dad "To Amelia, for tackling her first year with such grace and determination."
    hide amelia_family_dinner

    show black
    window hide   
    show amelia_smiling_teary
    with dissolve
    a "Thank you, Dad. I couldn’t have done it without all your support."
    mom "We’re so proud of you, Amelia. You’ve grown so much."
    hide amelia_smiling_teary

    show black
    window hide   
    show lily_looking_up_to_amelia
    with dissolve
    lily "Amelia, I want to hear more about your classes! What was your favorite part?"
    hide lily_looking_up_to_amelia

    show black
    window hide   
    show amelia_smiling_warmly
    with dissolve
    a "Oh, Lily, there were so many amazing moments. I think my favorite was diving into clinical psychology. Understanding mental health and how to support people has become a real passion of mine."
    lily "That sounds so interesting! I want to learn about psychology too when I grow up."
    amelia "And you will, Lily. You're already so curious and smart. Just keep asking questions and exploring what you love."
    n "They share a meal filled with laughter and love, the warmth of home enveloping Amelia."
    hide amelia_smiling_warmly

    if mentor == "None":
        n "Please select your mentor to continue"
        menu:
            "Professor Hawthorne":
                $ mentor = "Professor Hawthorne"
            
            "Dr. Simmons":
                $ mentor = "Dr. Simmons"

            "Maya":
                $ mentor = "Maya"

    jump mentor_check_in

label mentor_check_in:
    if mentor == "Professor Hawthorne":
        show black
        window hide

        show amelia_checking_email
        with dissolve
        n "The next day, Amelia checks her email and finds a message from Professor Hawthorne."
        hide amelia_checking_email

        show black
        window hide   
        show amelia_checking_email
        with dissolve
        hawthorne "{i}Dear Amelia, congratulations on completing your first year. Your growth and achievements have been remarkable. I have no doubt you'll continue to excel. Best, Prof. Hawthorne{/i}"
        hide amelia_checking_email

        show black
        window hide   
        show amelia_smiling_at_email
        with dissolve
        a "(Thank you, Professor. Your guidance meant the world to me.)"
        hide amelia_smiling_at_email

    elif mentor == "Dr. Simmons":
        show black
        window hide
        show amelia_getting_call
        with dissolve
        n "Amelia receives a call from Dr. Simmons, her voice warm and encouraging."
        hide amelia_getting_call

        show black
        window hide   
        show amelia_on_phone
        with dissolve
        simmons "Amelia, I just wanted to say how proud I am of you. Your journey has been incredible, and I know you’ll continue to make a difference."
        hide amelia_on_phone

        show black
        window hide   
        show amelia_nodding_on_phone
        with dissolve
        a "Thank you, Dr. Simmons. Your support has been invaluable."
        hide amelia_nodding_on_phone

    elif mentor == "Maya":
        show black
        window hide   
        show amelia_receiving_letter
        with dissolve
        n "Amelia finds a letter from Maya in her mailbox, filled with words of wisdom and encouragement."
        hide amelia_receiving_letter

        show black
        window hide   
        show maya_letter
        with dissolve
        maya "{i}Dear Amelia, your journey this year has been a testament to your strength and spirit. Continue to seek wisdom and embrace the path of enlightenment. With love, Maya{/i}"
        hide maya_letter

        show black
        window hide   
        show amelia_tearful_smile
        with dissolve
        a "(Maya, thank you. Your guidance has been my beacon.)"
        hide amelia_tearful_smile

    menu:
        "Go back to main menu":
            show black
            window hide
            return
        
        "Checkout the Occult hidden ending":
            show black
            window hide

            jump chapter_12_enlightenment

        "Checkout the Social butterfly ending":
            show black
            window hide

            jump chapter_12_social_butterfly

        "Checkout the Tragic ending":
            show black
            window hide

            jump chapter_12_tragic_ending


    # if AA >= 18 and SD >= 15:
    #     jump chapter_12_academic_success
    
    # if SI >= 18:
    #     jump chapter_12_social_butterfly
    
    # if MH >= 18 and MC >= 15:
    #     jump chapter_12_mental_health_advocate
    
    # if AA >= 15 and SI >= 15 and MH >= 15 and SD >= 15 and MC >= 15:
    #     jump chapter_12_balanced_growth
    
    # if OK >= 18 and SD >= 15:
    #     jump chapter_12_enlightenment

    # if MH <= 10 and SI <= 10:
    #     jump chapter_12_tragic_ending

label chapter_12_academic_success:

    stop music fadeout 5.0
    play music run_run_run fadein 2.0 volume 0.8 

    show black
    window hide  
    show as_amelia_in_room_reflecting
    with dissolve
    n "Amelia sits in her room, surrounded by the familiar comforts of home.{p=3}{nw}"
    
    show black
    window hide  
    show as_amelia_picture_park
    with dissolve
    n "She looks at the photos on her desk, memories from her first year at Plymouth University. She picks up a picture of her and her friends from a memorable day at Hoe Park.{p=4}{nw}"
    a "(So much has changed in just one year. I've grown in ways I never imagined.){p=3}{nw}"
    n "She takes a deep breath, feeling the weight of her journey.{p=2}{nw}"
    
    show black
    window hide  
    show as_amelia_journal_open
    with dissolve
    n "Amelia opens her journal, gifted by Dr. Simmons, and begins to write.{p=3}{nw}"
    a "{i}This year has been a whirlwind of experiences. I've faced challenges, made lifelong friends, and discovered so much about myself.{/i}{p=4}{nw}"
    a "{i}It's been transformative. I feel... reborn.{/i}{p=4}{nw}"
    n "Her phone buzzes, interrupting her thoughts. It's a message from Zara.{p=3}{nw}"

    show black
    window hide  
    show as_amelia_looking_at_phone
    with dissolve
    zara "{i}Hey Amelia! Just wanted to check in. How’s your break going?{/i}{p=3}{nw}"
    n "Amelia smiles and quickly types a response.{p=2}{nw}"
    a "{i}Hey Zara! It's been good. Lots of reflection. How about you?{/i}{p=3}{nw}"

    show black
    window hide  
    show as_amelia_looking_at_phone
    with dissolve
    n "A moment later, Zara's reply comes through.{p=2}{nw}"
    zara "{i}Same here. Missing everyone already. Can’t wait to catch up soon. Take care!{/i}{p=3}{nw}"
    a "{i}Miss you too, Zara. Talk soon!{/i}{p=2}{nw}"

    show black
    window hide
    show as_amelia_sitting_on_bed
    with dissolve
    n "Amelia puts her phone down and lies back on her bed, staring at the ceiling. Her thoughts drift to Sarah and the tough times they faced together.{p=4}{nw}"

    if sarah_alive:
        show black
        window hide  
        show as_amelia_reflecting_on_sarah
        with dissolve
        a "(Sarah... I'm so grateful she's still with us. Her strength inspires me every day. I remember that night vividly...){p=4}{nw}"
        n "Flashback to the night Sarah almost gave up, but Amelia and her friends managed to save her in time.{p=3}{nw}"
        n "The memory is intense, filled with fear, but also with hope and determination.{p=3}{nw}"

        show black
        window hide  
        show as_amelia_flashback_sarah
        with dissolve
        n "Sarah lying in a hospital bed, her face pale but alive. Amelia holding her hand, whispering words of comfort and promise.{p=4}{nw}"
        a "Sarah, you’re going to be okay. We’re here for you. Always.{p=3}{nw}"
        sarah "Amelia... thank you. I don't know what I'd do without you.{p=3}{nw}"
        a "(She's come so far since then. We've all come so far.){p=3}{nw}"

    else:
        show black
        window hide  
        show as_amelia_grieving_sarah
        with dissolve
        a "(Sarah... I wish things had turned out differently. The pain of losing her is still so fresh.){p=4}{nw}"
        n "Flashback to the night Sarah passed away. The grief is overwhelming, the sense of loss immeasurable.{p=4}{nw}"

        show black
        window hide  
        show as_amelia_flashback_sarah
        with dissolve
        n "Ttears streaming down her face. The room is filled with a profound silence{p=4}{nw}."
        a "Sarah, I'm so sorry. We tried everything... I miss you so much.{p=3}{nw}"
        a "(Her memory will always be with me. I'll carry her spirit forward in everything I do.){p=4}{nw}"

    show black
    window hide  
    show as_amelia_reflecting_in_mirror at fix_size
    with dissolve
    n "Amelia stands up and walks to her mirror, looking at her reflection. She sees a stronger, more determined version of herself.{p=4}{nw}"
    a "(I've faced my fears, my doubts, my pain. And I've come out the other side stronger. This is just the beginning.){p=4}{nw}"

    show black
    window hide
    show as_amelia_in_living_room_with_family at fix_size
    with dissolve
    n "Later that evening, the family gathers in the living room for a cozy night in. Amelia's parents notice her deep in thought.{p=4}{nw}"
    mom "Amelia, dear, is everything alright?{p=2}{nw}"

    show black
    window hide  
    show as_amelia_smiling_warmly at fix_size
    with dissolve
    a "Yes, Mom. Just a lot on my mind. This year has been... intense.{p=3}{nw}"
    dad "We can see that. You've grown so much. We're incredibly proud of you.{p=3}{nw}"

    show black
    window hide  
    show as_amelia_grateful at fix_size
    with dissolve
    a "Thank you, Dad. Your support has been my rock.{p=2}{nw}"
    lily "Amelia, can we play a game? Like old times?{p=2}{nw}"
    a "Of course, Lily. What do you want to play?{p=2}{nw}"
    lily "How about a board game? We haven't done that in ages.{p=2}{nw}"

    show black
    window hide  
    show as_family_playing_game at fix_size
    with dissolve
    n "The family gathers around the coffee table, playing a board game and sharing laughter. The simple joy of the moment fills the room with warmth.{p=4}{nw}"

    show black
    window hide  
    show as_amelia_grateful at fix_size
    with dissolve
    n "Amelia laughs heartily, feeling a deep sense of belonging and love.{p=3}{nw}"
    a "(This is what it's all about. Family, love, connection. These are the things that matter most.){p=4}{nw}"

    show black
    window hide  
    show as_amelia_talking_with_parents_dad at fix_size
    with dissolve
    n "After the game, Amelia sits with her parents, talking late into the night about her experiences, her dreams, and her plans for the future.{p=4}{nw}"
    dad "What's next for you, Amelia? Do you have any plans for the summer?{p=3}{nw}"

    show black
    window hide  
    show as_amelia_enthusiastic at fix_size
    with dissolve
    a "I’m thinking of applying for a summer research position at the university.{p=3}{nw}" 
    a "I want to dive deeper into my studies and maybe even contribute to some groundbreaking work.{p=4}{nw}"
   
    show black
    window hide  
    show as_mom_enthusiastic at fix_size
    with dissolve
    mom "That sounds wonderful. We're here to support you every step of the way.{p=3}{nw}"
    n "They continue to talk, the night growing deeper and the bond between them stronger than ever.{p=4}{nw}"

    show black
    window hide  
    show as_amelia_in_bed at fix_size
    with dissolve
    n "Later, as Amelia lies in bed, she reflects on the day's events and her journey so far.{p=3}{nw}"
    a "(I've come so far, and there's still so much more to explore. I can't wait to see what the future holds.){p=3}{nw}"
    n "With a contented sigh, she closes her eyes, ready to embrace the new adventures that await her.{p=3}{nw}"

    jump as_ending_credits

label as_ending_credits:
    window hide
    stop music fadeout 5.0
    play music junk_of_the_heart fadein 2.0 volume 0.8 
    show black
    # call screen credits
    
    window hide
    show as_credits_1 at fix_size
    with dissolve
    credit_text "By GizmoBot studios{p=15}{nw}"

    window hide
    show as_credits_2 at fix_size
    with dissolve
    credit_text "Story and Game design - Luna Ironfoot{p=7}{nw}"
    credit_text "Art and history - Zara Greenleaf{p=7}{nw}"    

    window hide
    show as_credits_4 at fix_size
    with dissolve
    credit_text "Sound design - Mira Silverbranch{p=7}{nw}"

    window hide
    show as_credits_5 at fix_size
    with dissolve
    credit_text "Music - Fish in a bird cage - Birds of a feather{p=7}{nw}"

    window hide
    show as_credits_6 at fix_size
    with dissolve
    credit_text "Music - Fish in a bird cage - Sand{p=7}{nw}"

    window hide
    show as_credits_7 at fix_size
    with dissolve
    credit_text "Music - Fish in a bird cage - Weight of gold{p=7}{nw}"

    window hide
    show as_credits_8 at fix_size
    with dissolve
    credit_text "Music - The Oh hellos - New river{p=7}{nw}"

    window hide
    show as_credits_9 at fix_size
    with dissolve
    credit_text "Music - The Oh hellos - Second child restless child{p=7}{nw}"
    credit_text "Music - The Oh hellos - Soldier poet king{p=7}{nw}"

    window hide
    show as_credits_10 at fix_size
    with dissolve
    credit_text "Music - The Oh hellos - I have made mistakes{p=7}{nw}"
    credit_text "Music - Fish in a bird cage - Paperwork{p=7}{nw}"

    window hide
    show as_credits_11 at fix_size
    with dissolve
    credit_text "Music - The amazing devil - Inkpot gods{p=5}{nw}"
    credit_text "Music - The amazing devil - Drinking song for the socially anxious{p=7}{nw}"

    window hide
    show as_credits_12 at fix_size
    with dissolve
    credit_text "Music - Cosmo Sheldrake - Moss{p=15}{nw}"
    credit_text "Special thanks - rubaphilos salfluere {p=15}{nw}"

    return

label chapter_12_social_butterfly:
    show black
    window hide

    stop music
    play music super_trouper fadein 1.0 volume 0.8

    show amelia_in_room_preparing
    with dissolve
    n "Amelia stands in front of her mirror, adjusting her dress and smiling at her reflection. Tonight is the big reunion with her friends from Plymouth, and she's filled with excitement and anticipation.{p=3}{nw}"
    a "(I can't wait to see everyone again. This year has been incredible, and it's all thanks to the amazing people I've met.){p=3}{nw}"
    mom "Have a great time, sweetheart! Say hello to everyone for us.{p=3}{nw}"
    dad "Enjoy yourself, Amelia. You deserve it.{p=3}{nw}"
    a "Thanks, Mom, Dad. I'll be back later tonight.{p=3}{nw}"
    hide amelia_in_room_preparing

    show black
    window hide  
    show amelia_leaving_home
    with dissolve
    n "She grabs her purse and heads out the door, waving goodbye to her parents.{p=3}{nw}"
    hide amelia_leaving_home

    show black
    window hide  
    show reunion_location
    with dissolve
    n "Amelia arrives at a trendy café in the heart of London, the chosen spot for their reunion. The place is buzzing with energy, and she immediately spots her friends at a corner table, waving enthusiastically.{p=3}{nw}"
    hide reunion_location

    show black
    window hide  
    show amelia_greeting_friends
    with dissolve
    a "Hey everyone! It's so good to see you all!{p=3}{nw}"
    lucas "Amelia! We've missed you!{p=3}{nw}"
    zara "It's been too long!{p=3}{nw}"
    raj "Our social butterfly has returned!{p=3}{nw}"
    hide amelia_greeting_friends

    show black
    window hide  
    show amelia_sitting_with_friends
    with dissolve
    n "They all sit down, and the conversation flows effortlessly. Stories of their summer so far, reminiscing about their favorite memories from the past year, and plans for the future fill the air.{p=3}{nw}"
    lucas "Remember that night at the Union when we all decided to dance like nobody was watching?{p=3}{nw}"
    hide amelia_sitting_with_friends

    show black
    window hide  
    show group_talking_and_laughing
    with dissolve
    amelia "How could I forget? That was the best night ever!{p=3}{nw}"
    zara "And the time we stayed up all night studying for that psychology exam? We were all so exhausted, but we made it through together.{p=3}{nw}"
    hide group_talking_and_laughing

    show black
    window hide  
    show amelia_nodding_sb
    with dissolve
    a "We've been through so much. I'm so grateful for each and every one of you.{p=3}{nw}"
    hide amelia_nodding_sb

    show black
    window hide  
    show raj_confiding
    with dissolve
    raj "You've brought so much joy and light into our lives, Amelia. Your energy is infectious.{p=3}{nw}"
    hide raj_confiding

    show black
    window hide  
    show amelia_blushing_sb
    with dissolve
    a "Thank you, Raj. You all have been my rock. I wouldn't have made it through the year without your support.{p=3}{nw}"
    hide amelia_blushing_sb

    show black
    window hide  
    show zara_confiding
    with dissolve
    zara "A toast, to Amelia. For being the heart and soul of our group. To friendships that last a lifetime.{p=3}{nw}"
    hide zara_confiding

    show black
    window hide  
    show friends_toasting
    with dissolve
    zara "To Amelia!{p=3}{nw}"
    hide friends_toasting

    show black
    window hide  
    show amelia_emotional_sb
    with dissolve
    n "As they clink glasses, Amelia feels a swell of emotion. She looks around at her friends, the people who have become her second family.{p=3}{nw}"
    a "(These moments, these connections, they mean everything to me. I'm so lucky to have found such incredible friends.){p=3}{nw}"
    hide amelia_emotional_sb

    show black
    window hide  
    show amelia_talking_to_lucas
    with dissolve
    n "Later in the evening, Lucas pulls Amelia aside, a serious look on his face.{p=3}{nw}"
    lucas "Amelia, can I talk to you for a moment?{p=3}{nw}"
    amelia "Of course, Lucas. What's up?{p=3}{nw}"
    hide amelia_talking_to_lucas

    show black
    window hide  
    show lucas_confiding
    with dissolve
    lucas "I just wanted to say... thank you. For everything. You've helped me come out of my shell in ways I never thought possible. You've made such a difference in my life.{p=3}{nw}"
    hide lucas_confiding

    show black
    window hide  
    show amelia_touched_sb
    with dissolve
    a "Lucas, that means so much to me. You've been an amazing friend. We've all grown together.{p=3}{nw}"
    lucas "I know I've struggled with opening up, but you made it feel safe. You've got a gift, Amelia. You bring people together.{p=3}{nw}"
    hide amelia_touched_sb

    show black
    window hide  
    show amelia_hugging_lucas
    with dissolve
    n "They share a heartfelt hug, the bond between them stronger than ever.{p=3}{nw}"
    hide amelia_hugging_lucas

    show black
    window hide  
    show amelia_talking_to_zara
    with dissolve
    n "Amelia then finds herself chatting with Zara, who looks contemplative.{p=3}{nw}"
    amelia "Zara, is everything okay?{p=3}{nw}"
    hide amelia_talking_to_zara

    show black
    window hide  
    show zara_confiding
    with dissolve
    zara "I've been reflecting a lot lately. About how far we've come, and how much you've helped me understand and cope with the challenges I've faced.{p=3}{nw}"
    hide zara_confiding

    stop music fadeout 3.0
    play music homegrown fadein 2.0 volume 0.8

    show black
    window hide  
    show amelia_listening_sb
    with dissolve
    a "Zara, you're one of the strongest people I know. You've taught me so much about resilience and courage.{p=3}{nw}"
    zara "And you've shown me the power of empathy and friendship. You've always been there, even when things were tough.{p=3}{nw}"
    hide amelia_listening_sb

    show black
    window hide  
    show amelia_smiling_sb
    with dissolve
    a "That's what friends are for. We'll always have each other's backs.{p=3}{nw}"
    hide amelia_smiling_sb

    show black
    window hide  
    show zara_hugging_amelia
    with dissolve
    n "They hug tightly, a moment of deep connection and understanding.{p=3}{nw}"
    hide zara_hugging_amelia

    show black
    window hide  
    show amelia_talking_to_raj
    with dissolve
    n "Finally, Amelia finds herself with Raj, who seems lost in thought.{p=3}{nw}"
    amelia "Raj, what’s on your mind?{p=3}{nw}"
    hide amelia_talking_to_raj

    show black
    window hide  
    show raj_confiding
    with dissolve
    raj "I’ve been thinking about the future. About how we’re all going to move forward with our lives. It’s exciting, but also a little scary.{p=3}{nw}"
    hide raj_confiding

    show black
    window hide  
    show amelia_nodding_sb
    with dissolve
    a "I know what you mean. Change can be daunting. But we have each other, no matter where life takes us.{p=3}{nw}"
    raj "You’ve given me so much confidence, Amelia. Your positivity and support have made all the difference.{p=3}{nw}"
    hide amelia_nodding_sb

    show black
    window hide  
    show amelia_touched_sb
    with dissolve
    a "And you've given me the same, Raj. We're all in this together.{p=3}{nw}"
    hide amelia_touched_sb

    show black
    window hide  
    show group_talking_and_laughing
    with dissolve
    n "The night continues with more laughter, stories, and heartfelt conversations. Amelia feels a profound sense of belonging and love.{p=3}{nw}"
    a "(These friendships are the most precious things in my life. They've shaped me, supported me, and made me who I am today.){p=3}{nw}"
    hide group_talking_and_laughing

    show black
    window hide  
    show amelia_and_friends_at_end_of_night
    with dissolve
    n "As the evening draws to a close, the group gathers outside the café, the cool night air filled with the promise of more adventures to come.{p=3}{nw}"
    lucas "This has been amazing. We need to do this more often.{p=3}{nw}"
    zara "Definitely. Let’s make it a tradition.{p=3}{nw}"
    raj "Agreed. To many more nights like this.{p=3}{nw}"
    hide amelia_and_friends_at_end_of_night

    show black
    window hide  
    show amelia_smiling_content_sb
    with dissolve
    a "To friendship, and to the amazing journey ahead of us.{p=3}{nw}"
    hide amelia_smiling_content_sb

    show amelia_walking_home_sb
    with dissolve
    n "As Amelia walks home, she reflects on the night and the incredible bonds she's formed.{p=3}{nw}"
    a "(I've come a long way from that shy, unsure girl who started university. I'm surrounded by love and friendship, and I know I can face anything with these amazing people by my side.){p=3}{nw}"
    hide amelia_walking_home_sb

    show black
    window hide  
    show amelia_smiling_upward_sb
    with dissolve
    a "Here's to the future, and to the beautiful friendships that make life so wonderful.{p=3}{nw}"
    hide amelia_smiling_upward_sb

    jump sb_ending_credits

label sb_ending_credits:
    window hide
    stop music
    play music sunshine_in_the_rain fadein 5.0 volume 0.8 
    show black
    # call screen credits
    
    window hide
    show sb_credits_1
    with dissolve
    credit_text "By GizmoBot studios{p=17}{nw}"

    window hide
    show sb_credits_2
    with dissolve
    credit_text "Story and Game design - Luna Ironfoot{p=17}{nw}"

    window hide
    show sb_credits_3
    with dissolve
    credit_text "Art and history - Zara Greenleaf{p=17}{nw}"

    window hide
    show sb_credits_4
    with dissolve
    credit_text "Sound design - Mira Silverbranch{p=17}{nw}"

    window hide
    show sb_credits_5
    with dissolve
    credit_text "Music - Fish in a bird cage - Birds of a feather{p=8}{nw}"
    credit_text "Music - Fish in a bird cage - Sand{p=8}{nw}"

    window hide
    show sb_credits_6
    with dissolve
    credit_text "Music - Fish in a bird cage - Weight of gold{p=8}{nw}"
    credit_text "Music - The Oh hellos - New river{p=8}{nw}"

    window hide
    show sb_credits_7
    with dissolve
    credit_text "Music - The Oh hellos - I have made mistakes{p=8}{nw}"
    credit_text "Music - Fish in a bird cage - Paperwork{p=8}{nw}"

    window hide
    show sb_credits_8
    with dissolve
    credit_text "Music - The amazing devil - Inkpot gods{p=8}{nw}"
    credit_text "Music - The amazing devil - Drinking song for the socially anxious{p=8}{nw}"

    window hide
    show sb_credits_9
    with dissolve
    credit_text "Music - Cosmo Sheldrake - Moss{p=8}{nw}"
    credit_text "Special thanks - Cornwalls rich history and nature {p=8}{nw}"

    window hide
    show sb_credits_10
    with dissolve
    credit_text "Special thanks - Many more {p=20}{nw}"

    return

label chapter_12_mental_health_advocate:
    stop music fadeout 5.0
    play music closer_to_the_heart fadein 2.0 volume 0.8 

    show black
    window hide  
    show mh_amelia_in_room_preparing at fix_size
    with dissolve
    n "Amelia sits at her desk, going through notes and resources she's gathered over the past year.{p=4}{nw}" 
    n "Her commitment to mental health advocacy has only grown stronger after her experiences with Sarah and her own challenges.{p=4}{nw}"
    a "(This is where I can make a real difference. I’ve seen firsthand how important it is to support those struggling with mental health issues.){p=4}{nw}"

    show black
    window hide  
    show mh_amelia_packing_bag at fix_size
    with dissolve
    n "She packs a bag with pamphlets, books, and other materials, preparing for her first volunteer session at a local mental health organization.{p=4}{nw}"
    a "(It's time to give back, to use what I've learned to help others.){p=4}{nw}"

    show black
    window hide  
    show mh_amelia_leaving_home at fix_size
    with dissolve
    n "Amelia heads out, waving goodbye to her parents.{p=2}{nw}"
    mom "Good luck today, Amelia. We're so proud of you.{p=2}{nw}"
    dad "You’re doing important work. We're here for you.{p=2}{nw}"

    show black
    window hide  
    show mh_amelia_smiling_wave at fix_size
    with dissolve
    a "Thanks, Mom, Dad. I’ll see you later.{p=2}{nw}"
    
    show black
    window hide
    show mh_mental_health_organization at fix_size
    with dissolve
    n "Amelia arrives at the mental health organization, greeted by a friendly volunteer coordinator.{p=3}{nw}"
    student "Amelia, welcome! We're so glad to have you here.{p=2}{nw}"
    amelia "Thank you. I'm excited to get started.{p=2}{nw}"

    show black
    window hide  
    show mh_amelia_helping_people at fix_size
    with dissolve
    n "Amelia spends the day talking to people, offering support, and sharing resources.{p=3}{nw}"
    n" She listens to their stories, providing a compassionate ear and valuable advice.{p=3}{nw}"
    student "It's been so hard. I feel like no one understands what I'm going through.{p=3}{nw}"

    show black
    window hide  
    show mh_amelia_listening at fix_size
    with dissolve
    a "I hear you. It's important to know that you're not alone. There are people who care and want to help.{p=4}{nw}"
    student "Thank you for listening. It means more than you know.{p=2}{nw}"
    n "As the day goes on, Amelia feels a deep sense of fulfillment and purpose.{p=3}{nw}"

    show black
    window hide  
    show mh_amelia_talking_to_coordinator at fix_size
    with dissolve
    a "This has been incredible. I feel like I'm truly making a difference.{p=3}{nw}"
    student "You are, Amelia. Your empathy and dedication are inspiring. We're lucky to have you.{p=4}{nw}"

    show black
    window hide  
    show mh_amelia_smiling at fix_size
    with dissolve
    a "Thank you. I’m grateful for this opportunity.{p=2}{nw}"

    show black
    window hide  
    show mh_amelia_reflecting_at_home at fix_size
    with dissolve
    n "Later that evening, back home, Amelia reflects on the day's experiences.{p=3}{nw}"
    a "(Today was just the beginning. There's so much more to do, so many people to help.){p=3}{nw}"

    if sarah_alive:
        show black
        window hide  
        show mh_sarah_on_phone at fix_size
        with dissolve
        n "She calls Sarah, eager to share her experiences.{p=3}{nw}"
        sarah "Amelia, I'm so proud of you. You’re doing such important work.{p=3}{nw}"

        show black
        window hide  
        show mh_amelia_smiling_phone at fix_size
        with dissolve
        a "Thanks, Sarah. You've been a huge inspiration for me.{p=3}{nw}"
        a "Seeing you fight and overcome your struggles has shown me how crucial mental health support is.{p=4}{nw}"
        sarah "And you've been my rock, Amelia. I'm so grateful for your friendship and support.{p=3}{nw}"

        show black
        window hide  
        show mh_amelia_determined at fix_size
        with dissolve
        a "We’re in this together, Sarah. Always.{p=2}{nw}"

    else:
        show black
        window hide  
        show mh_amelia_grieving_sarah at fix_size
        with dissolve
        a "(Sarah... I wish you could see what I'm doing. I hope I'm making you proud.){p=3}{nw}"
        n "Amelia looks at a photo of Sarah on her desk, a bittersweet smile on her face.{p=3}{nw}"
        a "(Your fight wasn’t in vain, Sarah. I promise to keep advocating for mental health, to make a difference in your memory.){p=4}{nw}"

    show black
    window hide  
    show mh_amelia_in_living_room_with_family at fix_size
    with dissolve
    n "At dinner, Amelia shares her experiences with her family.{p=3}{nw}"
    dad "How was your first day, Amelia?{p=2}{nw}"

    show black
    window hide  
    show mh_amelia_smiling_warmly at fix_size
    with dissolve
    a "It was amazing. I talked to so many people, heard their stories, and provided support. It felt incredibly rewarding.{p=4}{nw}"
    mom "We're so proud of you. Your compassion and dedication are truly admirable.{p=3}{nw}"

    show black
    window hide  
    show mh_amelia_thankful at fix_size
    with dissolve
    a "Thank you. I couldn’t have done this without your support and encouragement.{p=3}{nw}"

    show black
    window hide  
    show mh_lily_looking_up_to_amelia at fix_size
    with dissolve
    lily "I want to help people too when I grow up. Just like you, Amelia.{p=3}{nw}"

    show black
    window hide  
    show mh_amelia_smiling_warmly at fix_size
    with dissolve
    a "You can do anything you set your mind to, Lily. I'm sure you'll make a big difference in the world.{p=4}{nw}"

    show black
    window hide  
    show mh_amelia_writing_in_journal at fix_size
    with dissolve
    n "Later, Amelia sits at her desk, writing in her journal{p=2}{nw}."
    a "{i}Today was the start of something incredible. I'm more determined than ever to be an advocate for mental health.{/i}{p=4}{nw}"
    a "{i}To listen, to support, to make a difference.{/i}{p=2}{nw}"
    a "{i}Sarah's struggle, my own journey... they’ve taught me the importance of this work.{/i}{p=3}{nw}"
    a "{i}I will keep pushing forward, for those who need a voice, for those who need hope.{/i}{p=3}{nw}"
    a "(This is my calling. I will continue to fight for mental health awareness and support. This is just the beginning.){p=4}{nw}"
    n "As she lies in bed, Amelia feels a profound sense of purpose and hope for the future.{p=2}{nw}"
    a "(Together, we can make a difference. One step at a time.){p=4}{nw}"

    jump mh_ending_credits

label mh_ending_credits:
    window hide
    stop music fadeout 5.0
    play music wake_me_up fadein 2.0 volume 0.8 
    show black
    # call screen credits
    
    window hide
    show mh_credits_1 at fix_size
    with dissolve
    credit_text "By GizmoBot studios{p=5}{nw}"
    credit_text "Story and Game design - Luna Ironfoot{p=5}{nw}"
    credit_text "Art and history - Zara Greenleaf{p=5}{nw}"

    window hide
    show mh_credits_2 at fix_size
    with dissolve
    credit_text "Sound design - Mira Silverbranch{p=5}{nw}"
    credit_text "Music - Fish in a bird cage - Birds of a feather{p=5}{nw}"
    credit_text "Music - Fish in a bird cage - Sand{p=5}{nw}"

    window hide
    show mh_credits_3 at fix_size
    with dissolve
    credit_text "Music - Fish in a bird cage - Weight of gold{p=5}{nw}"
    credit_text "Music - The Oh hellos - New river{p=5}{nw}"
    credit_text "Music - The Oh hellos - Second child restless child{p=5}{nw}"

    window hide
    show mh_credits_4 at fix_size
    with dissolve
    credit_text "Music - The Oh hellos - Soldier poet king{p=5}{nw}"
    credit_text "Music - The Oh hellos - I have made mistakes{p=5}{nw}"
    credit_text "Music - Fish in a bird cage - Paperwork{p=5}{nw}"

    window hide
    show mh_credits_5 at fix_size
    with dissolve
    credit_text "Music - The amazing devil - Inkpot gods{p=5}{nw}"
    credit_text "Music - The amazing devil - Drinking song for the socially anxious{p=15}{nw}"
    credit_text "Music - Cosmo Sheldrake - Moss{p=5}{nw}"

    window hide
    show mh_credits_6 at fix_size
    with dissolve
    credit_text "Special thanks - rubaphilos salfluere {p=15}{nw}"

    window hide
    show mh_credits_7 at fix_size
    with dissolve
    credit_text "Special thanks - Cornwalls rich history and nature {p=15}{nw}"

    window hide
    show mh_credits_8 at fix_size
    with dissolve
    credit_text "Special thanks - Many more {p=15}{nw}"

    return

label chapter_12_balanced_growth:
    show black
    window hide  
    show amelia_in_room_preparing
    with dissolve
    n "Amelia stands in her room, taking a deep breath as she looks around at the familiar surroundings. This past year has been a journey of immense personal growth, and she's ready to bring that balance into her everyday life."
    a "(I've learned so much about balancing my academic pursuits, social life, and personal well-being. It's time to integrate all of it.)"

    show black
    window hide  
    show amelia_packing_bag
    with dissolve
    n "She packs a bag with a few essentials: a journal, a couple of books on psychology, and some photos of her friends. Today, she's meeting her mentor and later, spending time with family and friends."
    a "(It's important to remember the people who supported me and the lessons I've learned.)"


    show black
    window hide  
    show amelia_leaving_home
    with dissolve
    n "Amelia heads out, waving goodbye to her parents."
    mom "Enjoy your day, Amelia. We're so proud of you."
    dad "You've become such an amazing young woman."

    show black
    window hide  
    show amelia_smiling_wave
    with dissolve
    a "Thank you, Mom, Dad. I'll see you later."

    show black
    window hide  
    show amelia_meeting_mentor
    with dissolve
    n "Amelia arrives at a quiet café where she's meeting her mentor, Prof. Hawthorne."
    hawthorne "Amelia, it's wonderful to see you. How have you been?"

    show black
    window hide
    show amelia_smiling_sitting
    with dissolve
    a "I've been well, Professor. Reflecting on everything I've learned this year."

    show black
    window hide
    show hawthorne_nodding
    with dissolve
    hawthorne "You've had quite the journey. Balancing your studies, friendships, and personal growth isn't easy, but you've done an exemplary job."

    show black
    window hide
    show amelia_grateful
    with dissolve
    a "Thank you. Your guidance has been invaluable. I've learned to prioritize what's truly important and maintain a healthy balance."
    hawthorne "That's a lesson many struggle to learn. I'm proud of your progress. Keep nurturing those aspects of your life, and you'll continue to thrive."

    show black
    window hide
    show amelia_reflecting
    with dissolve
    a "I will, Professor. Thank you for everything."

    show black
    window hide
    show amelia_with_family
    with dissolve
    n "Later, Amelia spends time with her family in the park. They have a picnic, enjoying the sunny day and each other's company."
    mom "It's so nice to have you home, Amelia. We’ve missed these moments."

    show black
    window hide
    show amelia_smiling_warmly
    with dissolve
    a "I've missed them too. Being away has made me appreciate family time even more."

    show black
    window hide
    show lily_looking_up_to_amelia
    with dissolve
    lily "Amelia, can we play a game? Like we used to?"

    show black
    window hide
    show amelia_nodding_smile
    with dissolve
    a "Of course, Lily. What do you want to play?"
    lily "How about hide and seek?"

    show black
    window hide
    show amelia_laughing
    with dissolve
    a "Alright, you're on!"
    n "They play hide and seek, laughter echoing through the park. Amelia feels a profound sense of joy and balance."

    show black
    window hide
    show amelia_with_friends
    with dissolve
    n "In the evening, Amelia meets her friends for dinner at a local restaurant."
    lucas "Amelia! It’s great to see you."
    zara "We’ve missed you!"
    raj "Our balanced achiever is back!"

    show black
    window hide
    show amelia_smiling_at_friends
    with dissolve
    a "I've missed you all too. It's so good to be back together."

    show black
    window hide
    show group_dining
    with dissolve
    n "They enjoy a meal together, sharing stories and catching up on each other's lives."
    zara "You seem so at peace, Amelia. It's inspiring."

    show black
    window hide
    show amelia_reflecting_on_growth
    with dissolve
    a "I've learned the importance of balance. It's been a journey, but I feel like I'm in a good place now."
    raj "Your journey has been incredible to witness. You’ve grown so much."

    show black
    window hide
    show amelia_grateful
    with dissolve
    a "Thank you. We've all grown together. Your support has meant the world to me."

    show black
    window hide
    show lucas_nodding
    with dissolve
    lucas "We’re here for each other, no matter what."

    show black
    window hide
    show amelia_talking_to_group
    with dissolve
    a "I couldn’t have done it without you all. Our friendship has been my anchor."

    show black
    window hide
    show friends_toasting
    with dissolve
    n "They raise their glasses in a toast to their friendship and shared journey."
    lucas "To friendship and growth!"

    show black
    window hide
    show amelia_reflecting_in_room
    with dissolve
    n "Later that night, Amelia sits in her room, writing in her journal."
    a "{i}This year has taught me so much about balance. Balancing my academic goals, my social life, and my personal well-being has been key to my growth. I've realized the importance of nurturing each part of my life.{/i}"
    a "{i}I've grown academically, formed deep and meaningful friendships, and taken care of my mental health. It's a continuous journey, but I feel ready to face whatever comes next with this newfound sense of balance.{/i}"

    show black
    window hide
    show amelia_determined
    with dissolve
    a "(This is just the beginning. With balance, I can achieve anything.)"

    show black
    window hide
    show amelia_lying_in_bed
    with dissolve
    n "As she lies in bed, Amelia feels a profound sense of peace and readiness for the future."
    a "(I’m ready for whatever comes next. With balance and the support of my loved ones, I can face any challenge.)"

    # jump bg_ending_credits
    return

label chapter_12_enlightenment:
    show black
    window hide

    show intro_ok_ending
    with dissolve
    n "This is the ending that the player gets if they initially wandered into the occult section in the bookshop.{p=4}{nw}"
    n "If they talked to Sarah the first time they saw her.{p=4}{nw}"
    n "And if they then diligently worked to find all the hiden occult references and choices in the game.{p=4}{nw}"
    n "Eventually gaining enough OK points{p=4}{nw}"
    hide intro_ok_ending
    window hide   

    play music weight_of_gold fadein 1.0 volume 0.8

    show black
    show amelia_in_room_preparing_ritual
    with dissolve
    n "Amelia stands in her room, surrounded by alchemical texts she has begun to rely on.{p=4}{nw}"
    n "The ingredients for an intense spagyric process laying on a table infront of her.{p=4}{nw}"
    n "Tonight, she will attempt to create the philosopher's stone.{p=4}{nw}"
    n "The culmination of her alchemical journey research and studies.{p=4}{nw}"
    hide amelia_in_room_preparing_ritual
    window hide

    show black
    show amelia_beginning_ritual_3
    with dissolve
    a "(This is it. Everything I've learned has led me to this moment. It's time to see if I can create the stone.){p=4}{nw}"
    n "She begins the ritual, carefully following the intricate steps described in the ancient manuscripts.{p=4}{nw}"
    hide amelia_beginning_ritual_3
    window hide
    
    show black
    show room_anticipation_scent_2
    with dissolve
    n "The air in the room grows heavy with anticipation and the scent of the alchemical ingredients.{p=4}{nw}"
    a "(Focus, Amelia. This is about intention, about transformation.){p=4}{nw}"
    hide room_anticipation_scent_2

    show black
    show amelia_working_diligently_3
    with dissolve
    n "Hours pass as Amelia works diligently, her movements precise and her mind clear.{p=4}{nw}"
    hide amelia_working_diligently_3
    window hide

    show black
    show process_complete_5
    with dissolve
    n "Finally, the process is complete.{p=4}{nw}"
    hide process_complete_5
    window hide

    show black
    show amelia_holding_stone_2
    with dissolve
    n "Before her lies a small, glowing stone, pulsating with an otherworldly energy.{p=4}{nw}"
    n "She holds the philosopher's stone in her hands, feeling its power{p=4}{nw}"
    hide amelia_holding_stone_2
    window hide

    show black
    show amelia_no_immediate_change_2
    with dissolve
    n "But not noticing any immediate change within herself.{p=4}{nw}"
    hide amelia_no_immediate_change_2
    window hide

    show black
    show amelia_culmination_of_journey_2
    with dissolve
    a "This is it. The culmination of my journey.{p=4}{nw}"
    a "But... I don't feel any different.{p=4}{nw}"
    hide amelia_culmination_of_journey_2
    window hide

    show black
    show amelia_ingesting_stone_3
    with dissolve
    n "With a deep breath, Amelia ingests the stone.{p=4}{nw}"
    hide amelia_ingesting_stone_3
    window hide

    show black
    show amelia_doesnt_feel_different_2
    with dissolve
    n "She waits for a moment, expecting a profound transformation, but nothing happens immediately.{p=4}{nw}"
    n "Feeling slightly disappointed but hopeful, she decides to go for a walk to clear her mind.{p=4}{nw}"
    a "(Maybe the effects take time. A walk will help me think.){p=4}{nw}"
    hide amelia_doesnt_feel_different_2
    window hide
    
    show black
    show amelia_walking_outside
    with dissolve
    n "Amelia steps outside, the cool evening air refreshing her senses.{p=4}{nw}"
    hide amelia_walking_outside
    window hide

    show black
    show amelia_wandering_streets_2
    with dissolve
    n "She wanders through the streets, lost in thought about her journey and the stone's potential.{p=4}{nw}"
    a "I've come so far. Even if I don't feel different now{p=4}{nw}"
    n "The journey itself has been transformative.{p=4}{nw}"
    hide amelia_wandering_streets_2
    window hide

    stop music fadeout 5.0
    play music i_have_made_mistakes fadein 4.0 volume 0.3

    show black
    show mysterious_garden_2
    with dissolve
    n "Her wandering leads her to a garden she has never seen before.{p=4}{nw}"
    n "It's lush and vibrant, filled with flowers of every color.{p=4}{nw}"
    n "In the center, there is a fountain, and by the fountain stands a woman. She radiates a serene and powerful presence.{p=4}{nw}"
    hide mysterious_garden_2
    window hide

    show black
    show amelia_approaching_woman
    with dissolve
    n "Amelia approaches the woman, feeling a strange sense of familiarity.{p=4}{nw}"
    a "Hello. I don't think I've seen you here before.{p=4}{nw}"
    woman "Welcome, Amelia. I've been waiting for you.{p=4}{nw}"
    hide amelia_approaching_woman
    window hide

    show black
    show amelia_confused
    with dissolve
    a "Waiting for me? Who are you?{p=4}{nw}"
    hide amelia_confused
    window hide

    show black
    show woman_smiling
    with dissolve
    woman "Names are not important. What matters is the journey you are on and the wisdom you seek.{p=4}{nw}"
    hide woman_smiling
    window hide

    show black
    show amelia_listening_intently
    with dissolve
    a "What wisdom do you mean?{p=4}{nw}"
    woman "Sit with me by the fountain, and I will tell you a story.{p=4}{nw}"
    hide amelia_listening_intently
    window hide

    show black
    show amelia_sitting_by_fountain
    with dissolve
    n "Amelia sits beside the woman, the sound of the water calming her.{p=4}{nw}"
    hide amelia_sitting_by_fountain
    window hide

    show black
    show mysterious_woman_talking
    with dissolve
    n "The woman begins to speak, her voice soft and soothing.{p=4}{nw}"
    woman "Your journey began long before you set foot in Plymouth.{p=4}{nw}"
    hide mysterious_woman_talking
    window hide

    show black
    show amelia_reflecting_journey
    with dissolve
    woman "Your recent past has been marked by trials, pushing you to the edge of your very understanding of the world and your place within it.{p=4}{nw}"
    woman "You've faced academic pressures that tested your intellect and personal challenges that weighed heavily on your heart.{p=4}{nw}"
    woman "Amelia, your journey has been a crucible, shaping and refining you in ways you might not yet fully comprehend.{p=4}{nw}"
    woman "You arrived at Plymouth full of hope, yet unaware of the shadows you would encounter.{p=4}{nw}"
    hide amelia_reflecting_journey
    window hide

    show black
    show friends_puzzle_pieces
    with dissolve
    woman "The friends you've made—Ella, Zara, Lucas, Maya, Raj—each brought a piece of the puzzle that is your life.{p=4}{nw}"
    woman "They've taught you the beauty of diversity, the strength found in unity, and the power of compassion.{p=4}{nw}"
    hide friends_puzzle_pieces
    window hide

    stop music fadeout 5.0
    play music come_with_me fadein 3.0 volume 0.4

    show black
    show amelia_sarah_reflection
    with dissolve
    woman "But, my dear, it is Sarah who left the most indelible mark.{p=4}{nw}"
    show amelia_sarah_reflection_2
    with dissolve
    woman "Her struggle with depression was a mirror, reflecting the unspoken fears and hidden pains within you.{p=4}{nw}"
    show amelia_sarah_reflection_3
    with dissolve
    woman "Her fate was a profound lesson, reminding you of the fragility of life and the importance of mental health.{p=4}{nw}"
    hide amelia_sarah_reflection
    hide amelia_sarah_reflection_2
    hide amelia_sarah_reflection_3
    window hide

    hide amelia_sarah_reflection
    show black
    show amelia_shaped_experiences
    with dissolve
    woman "The day you found her, you realized the gravity of your role in this world.{p=4}{nw}"
    woman "Whether she found peace or succumbed to her pain, her story intertwined with yours, urging you to advocate for those who suffer in silence.{p=3}{nw}"
    hide amelia_shaped_experiences
    window hide

    show black
    show amelia_tears_peace
    with dissolve
    n "Tears begin to well up in her eyes as she realizes the profound truth of the woman’s words.{p=2}{nw}"
    hide amelia_tears_truth
    window hide

    show black
    show amelia_listening_emotional
    with dissolve
    a "Yes, it has been challenging... but I've learned so much.{p=2}{nw}"
    woman "These experiences have shaped you, prepared you for the path you walk now.{p=2}{nw}"
    hide amelia_listening_emotional
    window hide

    show black
    show amelia_listening_emotional
    with dissolve
    woman "Every choice you've made has led you here, standing at the threshold of true understanding.{p=2}{nw}"
    woman "You've delved into the depths of psychology, explored the mystical and the unknown, and faced your darkest fears.{p=2}{nw}"
    hide amelia_listening_emotional
    window hide

    show black
    show amelia_listening_emotional_2
    with dissolve
    woman "You've grown, Amelia, more than you can see.{p=2}{nw}"
    woman "The enlightenment you seek is not a destination but a journey, a continuous path of learning, compassion, and self-discovery.{p=2}{nw}"
    woman "Remember Sarah, remember her struggle and her strength.{p=2}{nw}"
    woman "Use that memory to fuel your resolve to make a difference.{p=2}{nw}"
    woman "Your story is far from over, and your potential is limitless.{p=2}{nw}"
    hide amelia_listening_emotional_2
    window hide

    show black
    show amelia_understanding
    with dissolve
    woman "Your heart has been forged in the fires of adversity, and through it, you have discovered your strength.{p=2}{nw}"
    woman "Embrace your past, cherish your present, and step boldly into your future.{p=2}{nw}"
    hide amelia_understanding
    window hide

    # show black
    # show woman_cryptic_tone
    # with dissolve
    # n "The woman’s voice takes on a more cryptic tone{p=3}{nw}"
    # hide woman_cryptic_tone

    # show black
    # show amelia_path_transformation
    # with dissolve
    # woman "The path ahead is one of transformation. Just as the two always become the one.{p=3}{nw}"
    # hide amelia_path_transformation

    # show black
    # show amelia_prima_materia
    # with dissolve
    # woman "The Prima Materia within you, the raw essence of your being, will undergo a sacred transformation.{p=4}{nw}"
    # hide amelia_prima_materia

    # show black
    # show amelia_nigredo_albedo
    # with dissolve
    # woman "You will navigate the Nigredo, the darkness and dissolution, and emerge into the Albedo, the purification in the double sign of your own mercury.{p=5}{nw}"
    # hide amelia_nigredo_albedo

    # show black
    # show amelia_fully_absorbed
    # with dissolve
    # n "Amelia listens, her heart and mind fully absorbed by the woman’s words.{p=3}{nw}"
    # hide amelia_fully_absorbed

    # show black
    # show amelia_citrinitas
    # with dissolve
    # woman "In the Citrinitas, the dawning of the new consciousness, you will find clarity and purpose.{p=4}{nw}"
    # hide amelia_citrinitas

    # show black
    # show amelia_rubedo
    # with dissolve
    # woman "And finally, in the Rubedo, the reddening, you will achieve the Great Work{p=4}{nw}"
    # hide amelia_rubedo

    show black
    show amelia_divine_tapestry
    with dissolve
    woman "Trust in the process, and know that every challenge, every joy, is part of the divine tapestry of your life.{p=2}{nw}"
    hide amelia_divine_tapestry
    window hide

    show black
    show amelia_weight_transmission
    with dissolve
    n "Amelia feels the weight of the mysterious womens words settling deep within her soul.{p=4}{nw}"
    hide amelia_weight_transmission
    window hide

    show black
    show amelia_embracing_past_future
    with dissolve
    a "All that I have been through, All this time, I never understood...{p=4}{nw}"
    a "Finally I understand..{p=4}{nw}"
    hide amelia_embracing_past_future
    window hide

    show black
    show woman_fading
    with dissolve
    n "The woman smiles, her form beginning to fade.{p=2}{nw}"
    n "With that, the woman vanishes, leaving Amelia alone by the fountain, her heart full and her mind buzzing with newfound insights.{p=3}{nw}"
    hide woman_fading
    window hide

    # show black
    # show amelia_waking_up_in_bed
    # with dissolve
    # n "Amelia wakes up in her bed, unsure if the encounter was real or a dream.{p=3}{nw}"
    # hide amelia_waking_up_in_bed

    # show black
    # show amelia_tears_peace
    # with dissolve
    # n "But the tears on her face and the deep sense of peace within her tell her{p=2}{nw}"
    # n "It was more than just a figment of her imagination.{p=3}{nw}"
    # hide amelia_tears_peace

    # show black
    # show amelia_beginning_achieve
    # with dissolve
    # a "(This is just the beginning, I can achieve anything.){p=3}{nw}"
    # hide amelia_beginning_achieve

    show black
    show amelia_in_room_reflecting
    with dissolve
    n "Back in her room, Amelia sits down and begins to write in her journal, capturing the emotions and insights from the encounter.{p=4}{nw}"
    a "{i}Tonight, I received a gift beyond measure. The great work, our great work...{/i}{p=4}{nw}"
    a "{i}My journey is just beginning, and I feel ready to face whatever comes next.{/i}{p=4}{nw}"
    hide amelia_in_room_reflecting
    window hide

    # show black
    # show amelia_lying_in_bed_3
    # with dissolve
    # n "As she lies in bed, Amelia feels a profound sense of peace and readiness for the future.{p=3}{nw}"
    # hide amelia_lying_in_bed_3

    show black
    show amelia_ready_challenges
    with dissolve
    a "(I’m ready for whatever comes next, I can face any challenge.){p=5}{nw}"
    hide amelia_ready_challenges
    show black
    window hide
    jump ok_ending_credits

label ok_ending_credits:
    window hide
    stop music fadeout 5.0
    play music irish_eyes fadein 2.0 volume 0.8 
    show black
    # call screen credits
    
    window hide
    show amelia_cornwall_sea_halo
    with dissolve
    credit_text "By GizmoBot studios{p=10}{nw}"

    window hide
    show ok_credits_2
    with dissolve
    credit_text "Story and Game design - Luna Ironfoot{p=5}{nw}"
    credit_text "Art and history - Zara Greenleaf{p=5}{nw}"
    credit_text "Sound design - Mira Silverbranch{p=5}{nw}"

    window hide
    show ok_credits_3
    with dissolve
    credit_text "Music - Fish in a bird cage - Birds of a feather{p=5}{nw}"
    credit_text "Music - Fish in a bird cage - Sand{p=5}{nw}"

    window hide
    show ok_credits_3
    with dissolve
    credit_text "Music - Fish in a bird cage - Weight of gold{p=5}{nw}"
    credit_text "Music - The Oh hellos - New river{p=5}{nw}"

    window hide
    show ok_credits_4
    with dissolve
    credit_text "Music - The Oh hellos - Second child restless child{p=5}{nw}"

    window hide
    show ok_credits_5
    with dissolve
    credit_text "Music - The Oh hellos - Soldier poet king{p=5}{nw}"

    window hide
    show ok_credits_6
    with dissolve
    credit_text "Music - The Oh hellos - I have made mistakes{p=5}{nw}"

    window hide
    show ok_credits_7
    with dissolve
    credit_text "Music - Fish in a bird cage - Paperwork{p=5}{nw}"

    window hide
    show ok_credits_8
    with dissolve
    credit_text "Music - The amazing devil - Inkpot gods{p=5}{nw}"

    window hide
    show ok_credits_9
    with dissolve
    credit_text "Music - The amazing devil - Drinking song for the socially anxious{p=5}{nw}"

    window hide
    show ok_credits_10
    with dissolve
    credit_text "Music - Cosmo Sheldrake - Moss{p=5}{nw}"

    window hide
    show ok_credits_11
    with dissolve
    credit_text "Special thanks - rubaphilos salfluere {p=4}{nw}"

    window hide
    show ok_credits_12
    with dissolve
    credit_text "Special thanks - Cornwalls rich history and nature {p=4}{nw}"
    credit_text "The end{p=3}{nw}"

    return

label chapter_12_tragic_ending:
    show black
    window hide

    stop music
    play music sand fadein 1.0 volume 0.8 

    show amelia_in_room_reflecting_2
    with dissolve
    n "Amelia sits in her room, surrounded by the familiar comforts of home, but the weight of the past year bears heavily on her shoulders.{p=3}{nw}"
    n "She looks at the photos on her desk, memories from her first year at Plymouth University, but one photo in particular catches her eye – a picture of her and Sarah, smiling together before everything changed.{p=3}{nw}"
    a "(Sarah... I wish things had turned out differently. The pain of losing her is still so fresh.){p=3}{nw}"
    hide amelia_in_room_reflecting_2

    show black
    window hide
    show amelia_tearful
    with dissolve
    n "Tears well up in her eyes as she remembers the night Sarah passed away. The grief is overwhelming, and the sense of loss is immeasurable.{p=3}{nw}"
    hide amelia_tearful

    show black
    window hide
    show amelia_flashback_sarah
    with dissolve
    n "Flashback to the night Sarah passed away. Amelia at Sarah's bedside, tears streaming down her face. The room is filled with a profound silence.{p=3}{nw}"
    a "Sarah, I'm so sorry. We tried everything... I miss you so much.{p=3}{nw}"
    n "The scene fades back to Amelia in her room, the weight of grief pressing down on her.{p=3}{nw}"
    a "(Her memory will always be with me. I'll carry her spirit forward in everything I do.){p=3}{nw}"
    hide amelia_flashback_sarah

    show black
    window hide
    show amelia_staring_at_wall
    with dissolve
    n "Amelia sits in silence, staring at the wall, feeling the emptiness left by Sarah's absence. Her parents, noticing her distress, enter the room quietly.{p=3}{nw}"
    dad "Amelia, sweetheart, are you okay?{p=3}{nw}"
    hide amelia_staring_at_wall

    show black
    window hide
    show amelia_shaking_head
    with dissolve
    a "No, Dad. I'm not. I miss her so much. I don't know how to move on.{p=3}{nw}"
    mom "It's okay to feel this way, Amelia. Grief is a heavy burden, but you don't have to carry it alone. We're here for you.{p=3}{nw}"
    hide amelia_shaking_head

    show black
    window hide
    show amelia_hugging_parents_2
    with dissolve
    n "Amelia breaks down, hugging her parents tightly. Their warmth and love provide some comfort, but the pain remains.{p=3}{nw}"
    a "Thank you... I just wish things were different.{p=3}{nw}"
    hide amelia_hugging_parents_2

    show black
    window hide
    show amelia_sitting_in_garden
    with dissolve
    n "Later, Amelia goes to the garden, seeking solace in nature. She sits on a bench, lost in thought.{p=3}{nw}"
    a "(Everything feels so empty without her. I don't know how to fill this void.){p=3}{nw}"
    hide amelia_sitting_in_garden

    show black
    window hide
    show amelia_receiving_text
    with dissolve
    n "Her phone buzzes with a text from Lucas.{p=3}{nw}"
    lucas "{i}Hey Amelia, just checking in. How are you holding up?{/i}{p=3}{nw}"
    hide amelia_receiving_text

    show black
    window hide
    show amelia_texting_back
    with dissolve
    n "Amelia types a response, her fingers trembling.{p=3}{nw}"
    a "{i}Hi Lucas. I'm struggling. Everything feels so heavy without Sarah.{/i}{p=3}{nw}"
    n "A moment later, Lucas's reply comes through.{p=3}{nw}"
    lucas "{i}I can't imagine how hard it is for you. Just remember, you're not alone. We're all here for you.{/i}{p=3}{nw}"
    a "{i}Thank you, Lucas. I appreciate it.{/i}{p=3}{nw}"
    hide amelia_texting_back

    show black
    window hide
    show amelia_crying_in_garden_2
    with dissolve
    n "Amelia puts her phone down and cries, the weight of her grief overwhelming her. She feels a hand on her shoulder and looks up to see Zara standing there.{p=3}{nw}"
    zara "Amelia, I’m so sorry. I know how much Sarah meant to you.{p=3}{nw}"
    hide amelia_crying_in_garden_2

    show black
    window hide
    show amelia_hugging_zara
    with dissolve
    a "Thank you, Zara. I don't know how to get through this.{p=3}{nw}"
    zara "You don't have to do it alone. We're all here for you. Lean on us when you need to.{p=3}{nw}"
    hide amelia_hugging_zara

    show black
    window hide
    show amelia_hugging_zara
    with dissolve
    a "I will. It's just so hard.{p=3}{nw}"
    n "They sit together in silence, the shared grief bringing a small measure of comfort.{p=3}{nw}"
    hide amelia_hugging_zara

    stop music
    play music come_with_me fadein 1.0 volume 0.8 

    show black
    window hide
    show amelia_talking_to_professor_hawthorne_2
    with dissolve
    n "The next day, Amelia meets with Professor Hawthorne, who has been a mentor and support throughout her journey.{p=3}{nw}"
    hawthorne "Amelia, I'm deeply sorry for your loss. Sarah was a wonderful person.{p=3}{nw}"
    amelia "Thank you, Professor. I feel lost without her.{p=3}{nw}"
    hawthorne "Grief is a difficult path to walk. It's important to allow yourself to feel, to grieve. But remember, Sarah's memory can be a source of strength as well.{p=3}{nw}"
    hide amelia_talking_to_professor_hawthorne_2

    show black
    window hide
    show amelia_talking_to_professor_hawthorne_2
    with dissolve
    a "I’ll try. It's just... everything feels so empty.{p=3}{nw}"
    hawthorne "In time, you will find ways to honor her memory and find strength in her spirit. Lean on your friends, your family. They will help you through this.{p=3}{nw}"
    hide amelia_talking_to_professor_hawthorne_2

    show black
    window hide
    show amelia_at_memorial_2
    with dissolve
    n "Later, Amelia visits a small memorial she has set up for Sarah. She lights a candle and places a photo of them together next to it.{p=3}{nw}"
    a "(Sarah, I hope you can hear me. I miss you every day. I'm trying to find my way without you.){p=3}{nw}"
    n "She sits there for a while, the flickering flame offering a small comfort.{p=3}{nw}"
    hide amelia_at_memorial_2

    show black
    window hide
    show amelia_journaling_2
    with dissolve
    n "Back in her room, Amelia writes in her journal, capturing her thoughts and feelings.{p=3}{nw}"
    a "{i}Today was another difficult day. I visited Sarah's memorial and talked to my friends. Their support means so much, but the pain is still overwhelming. I keep telling myself that it will get easier, that time will heal, but right now it feels like an endless void.{/i}{p=3}{nw}"
    hide amelia_journaling_2

    show black
    window hide
    show amelia_lying_in_bed_tg
    with dissolve
    n "As she lies in bed, Amelia feels a deep sense of loss and uncertainty about the future.{p=3}{nw}"
    a "(I don’t know what comes next. But I know I have to keep going, for Sarah and for myself.){p=3}{nw}"
    n "She closes her eyes, the tears still fresh on her cheeks, and falls into a restless sleep, hoping that one day, the pain will lessen and she will find a way to move forward.{p=3}{nw}"
    hide amelia_lying_in_bed_tg

    show black
    window hide

    jump te_ending_credits

label te_ending_credits:
    window hide
    stop music
    play music liar_and_a_thief fadein 5.0 volume 0.8 
    show black
    # call screen credits
    
    window hide
    show tragic_credits_1
    with dissolve
    credit_text "By GizmoBot studios{p=15}{nw}"

    window hide
    show tragic_credits_2
    with dissolve
    credit_text "Story and Game design - Luna Ironfoot{p=15}{nw}"

    window hide
    show tragic_credits_3
    with dissolve
    credit_text "Art and history - Zara Greenleaf{p=15}{nw}"
    credit_text "Sound design - Mira Silverbranch{p=15}{nw}"

    window hide
    show tragic_credits_4
    with dissolve

    credit_text "Music - Fish in a bird cage - Birds of a feather{p=15}{nw}"
    credit_text "Music - Fish in a bird cage - Sand{p=15}{nw}"
    credit_text "Music - Fish in a bird cage - Weight of gold{p=5}{nw}"
    credit_text "Music - The Oh hellos - New river{p=5}{nw}"


    window hide
    show tragic_credits_6
    with dissolve
    credit_text "Music - The Oh hellos - I have made mistakes{p=5}{nw}"
    credit_text "Music - Fish in a bird cage - Paperwork{p=5}{nw}"
    credit_text "Music - The amazing devil - Inkpot gods{p=5}{nw}"
    credit_text "Music - The amazing devil - Drinking song for the socially anxious{p=5}{nw}"

    window hide
    show tragic_credits_7
    with dissolve
    credit_text "Music - Cosmo Sheldrake - Moss{p=5}{nw}"
    credit_text "Special thanks - Cornwalls rich history and nature {p=5}{nw}"
    credit_text "Special thanks - Many more {p=5}{nw}"

    return