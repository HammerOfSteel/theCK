define music.weight_of_gold = "weight_of_gold.mp3"
define music.jag_finns_kvar = "jag_finns_kvar.mp3"

label chapter_12_part_1:
    show amelia_returning_home
    with dissolve

    "Amelia steps off the train at London’s bustling station, a wave of nostalgia washing over her. She sees her parents and Ella waiting eagerly, their smiles wide and welcoming."

    show amelia_hugging_parents
    with dissolve

    "Her parents envelop her in a warm embrace, and she feels the comfort of their familiar presence."
    
    mr_james "Welcome back, Amelia! We've missed you so much."

    mrs_james "Look at you, all grown up and wiser."

    show amelia_smiling_happy
    with dissolve

    a "It's good to be home, Mom, Dad. I missed you both too."

    show ella_running_to_amelia
    with dissolve

    ella "Amelia! I've missed you so much!"

    show amelia_and_ella_hugging
    with dissolve

    a "Ella! I’ve missed you too. There’s so much to tell you."

    ella "Come on, let's get your bags and head home. I want to hear everything!"

    "They spend the car ride home catching up, Ella bombarding Amelia with questions about university life."

    show car_ride_home
    with dissolve

    ella "So, how's Plymouth? Is it as beautiful as they say?"

    amelia "Absolutely, Ella. The campus is stunning, and the city has so much history and charm. I even visited some incredible places in Cornwall."

    ella "Oh, I'm so jealous! And how about the people? Did you make any good friends?"

    amelia "Yes, I did. There's Lucas, Zara, Raj, and Maya. We've all grown really close. And of course, my professors have been amazing."

    show amelia_in_living_room_with_family
    with dissolve

    "Back home, the James family sits around the living room, the atmosphere filled with joy and curiosity."

    mrs_james "Tell us everything, darling. How was your first year?"

    show amelia_smiling_reflecting
    with dissolve

    a "It was... transformative. I learned so much, not just academically, but about myself."

    mr_james "We're so proud of you, Amelia. You've come a long way."

    show amelia_nodding_smile
    with dissolve

    a "Thank you. The experiences, the people I met, everything has contributed to my growth. It wasn't always easy, but it was worth it."

    mrs_james "We could see the change in you the moment you stepped off the train. You've grown into such a strong, confident young woman."

    show amelia_blushing
    with dissolve

    a "Thanks, Mom. Your support meant everything to me. There were times I felt really overwhelmed, but knowing I had you all cheering for me kept me going."

    jump reunion_with_ella

label reunion_with_ella:
    show amelia_in_room_with_ella
    with dissolve

    "Later, at Ella’s house, the two friends sit in their favorite spot, reminiscing about old times and sharing new stories."

    ella "So, what’s the biggest change? You seem... different, in a good way."

    show amelia_smiling
    with dissolve

    a "I feel different. More confident, more aware of who I am and what I want to do. I guess facing so many challenges helped me discover my strengths."

    ella "I’m so proud of you, Amelia. You’re really becoming the person you were meant to be."

    show amelia_thankful
    with dissolve

    a "Thanks, Ella. You've always believed in me, even when I didn't believe in myself. That means a lot."

    ella "Always. So, tell me more about your friends. They sound amazing."

    show amelia_reflecting
    with dissolve

    a "They are. Lucas is my roommate, and he's into Jungian psychology, which is fascinating. Zara has faced a lot of racism but she's incredibly strong and insightful. Maya is into Zen philosophy, and she's helped me explore spiritual dimensions. And Raj is studying family systems, which has given me a lot of perspective on relationships."

    ella "Wow, it sounds like you have a diverse group of friends. It must be so enriching to learn from each other."

    show amelia_nodding
    with dissolve

    a "It is. We've all supported each other through some tough times, especially with Sarah... She's had a really hard year, and we've all tried to be there for her."

    jump family_dinner

label family_dinner:
    show amelia_family_dinner
    with dissolve

    "At the family dinner that night, Amelia's parents toast to her successful year."

    mr_james "To Amelia, for tackling her first year with such grace and determination."

    show amelia_smiling_teary
    with dissolve

    a "Thank you, Dad. I couldn’t have done it without all your support."

    mrs_james "We’re so proud of you, Amelia. You’ve grown so much."

    show lily_looking_up_to_amelia
    with dissolve

    lily "Amelia, I want to hear more about your classes! What was your favorite part?"

    show amelia_smiling_warmly
    with dissolve

    a "Oh, Lily, there were so many amazing moments. I think my favorite was diving into clinical psychology. Understanding mental health and how to support people has become a real passion of mine."

    lily "That sounds so interesting! I want to learn about psychology too when I grow up."

    amelia "And you will, Lily. You're already so curious and smart. Just keep asking questions and exploring what you love."

    "They share a meal filled with laughter and love, the warmth of home enveloping Amelia."

    jump mentor_check_in

label mentor_check_in:
    if mentor == "Professor Hawthorne":
        show amelia_checking_email
        with dissolve
        "The next day, Amelia checks her email and finds a message from Professor Hawthorne."

        show hawthorne_email
        with dissolve

        hawthorne "{i}Dear Amelia, congratulations on completing your first year. Your growth and achievements have been remarkable. I have no doubt you'll continue to excel. Best, Prof. Hawthorne{/i}"

        show amelia_smiling_at_email
        with dissolve

        a "(Thank you, Professor. Your guidance meant the world to me.)"

    elif mentor == "Dr. Simmons":
        show amelia_getting_call
        with dissolve

        "Amelia receives a call from Dr. Simmons, her voice warm and encouraging."

        show amelia_on_phone
        with dissolve

        simmons "Amelia, I just wanted to say how proud I am of you. Your journey has been incredible, and I know you’ll continue to make a difference."

        show amelia_nodding_on_phone
        with dissolve

        a "Thank you, Dr. Simmons. Your support has been invaluable."

    elif mentor == "Maya":
        show amelia_receiving_letter
        with dissolve

        "Amelia finds a letter from Maya in her mailbox, filled with words of wisdom and encouragement."

        show maya_letter
        with dissolve

        maya "{i}Dear Amelia, your journey this year has been a testament to your strength and spirit. Continue to seek wisdom and embrace the path of enlightenment. With love, Maya{/i}"

        show amelia_tearful_smile
        with dissolve

        a "(Maya, thank you. Your guidance has been my beacon.)"

    if AA >= 18 and SD >= 15:
        jump chapter_12_academic_success
    
    if SI >= 18:
        jump chapter_12_social_butterfly
    
    if MH >= 18 and MC >= 15:
        jump chapter_12_mental_health_advocate
    
    if AA >= 15 and SI >= 15 and MH >= 15 and SD >= 15 and MC >= 15:
        jump chapter_12_balanced_growth
    
    if OK >= 18 and SD >= 15:
        jump chapter_12_enlightenment

    if MH <= 10 and SI <= 10:
        jump chapter_12_tragic_ending

label chapter_12_academic_success:
    show amelia_in_room_reflecting
    with dissolve

    "Amelia sits in her room, surrounded by the familiar comforts of home. She looks at the photos on her desk, memories from her first year at Plymouth University. She picks up a picture of her and her friends from a memorable day at Hoe Park."

    a "(So much has changed in just one year. I've grown in ways I never imagined.)"

    "She takes a deep breath, feeling the weight of her journey."

    show amelia_journal_open
    with dissolve

    "Amelia opens her journal, gifted by Dr. Simmons, and begins to write."

    a "{i}This year has been a whirlwind of experiences. I've faced challenges, made lifelong friends, and discovered so much about myself. It's been transformative. I feel... reborn.{/i}"

    "Her phone buzzes, interrupting her thoughts. It's a message from Zara."

    show amelia_looking_at_phone
    with dissolve

    zara "{i}Hey Amelia! Just wanted to check in. How’s your break going?{/i}"

    "Amelia smiles and quickly types a response."

    a "{i}Hey Zara! It's been good. Lots of reflection. How about you?{/i}"

    show amelia_waiting_for_response
    with dissolve

    "A moment later, Zara's reply comes through."

    zara "{i}Same here. Missing everyone already. Can’t wait to catch up soon. Take care!{/i}"

    a "{i}Miss you too, Zara. Talk soon!{/i}"

    show amelia_sitting_on_bed
    with dissolve

    "Amelia puts her phone down and lies back on her bed, staring at the ceiling. Her thoughts drift to Sarah and the tough times they faced together."

    if sarah_alive:
        show amelia_reflecting_on_sarah
        with dissolve

        a "(Sarah... I'm so grateful she's still with us. Her strength inspires me every day. I remember that night vividly...)"

        "Flashback to the night Sarah almost gave up, but Amelia and her friends managed to save her in time. The memory is intense, filled with fear, but also with hope and determination."

        show amelia_flashback_sarah
        with dissolve

        "Sarah lying in a hospital bed, her face pale but alive. Amelia holding her hand, whispering words of comfort and promise."

        a "Sarah, you’re going to be okay. We’re here for you. Always."

        sarah "Amelia... thank you. I don't know what I'd do without you."

        "The scene fades back to Amelia in her room, tears welling up in her eyes."

        a "(She's come so far since then. We've all come so far.)"

    else:
        show amelia_grieving_sarah
        with dissolve

        a "(Sarah... I wish things had turned out differently. The pain of losing her is still so fresh.)"

        "Flashback to the night Sarah passed away. The grief is overwhelming, the sense of loss immeasurable."

        show amelia_flashback_sarah
        with dissolve

        "Amelia at Sarah's bedside, tears streaming down her face. The room is filled with a profound silence."

        a "Sarah, I'm so sorry. We tried everything... I miss you so much."

        "The scene fades back to Amelia in her room, the weight of grief pressing down on her."

        a "(Her memory will always be with me. I'll carry her spirit forward in everything I do.)"

    show amelia_reflecting_in_mirror
    with dissolve

    "Amelia stands up and walks to her mirror, looking at her reflection. She sees a stronger, more determined version of herself."

    a "(I've faced my fears, my doubts, my pain. And I've come out the other side stronger. This is just the beginning.)"

    show amelia_in_living_room_with_family
    with dissolve

    "Later that evening, the family gathers in the living room for a cozy night in. Amelia's parents notice her deep in thought."

    mrs_james "Amelia, dear, is everything alright?"

    show amelia_smiling_warmly
    with dissolve

    a "Yes, Mom. Just a lot on my mind. This year has been... intense."

    mr_james "We can see that. You've grown so much. We're incredibly proud of you."

    show amelia_grateful
    with dissolve

    a "Thank you, Dad. Your support has been my rock."

    lily "Amelia, can we play a game? Like old times?"

    show amelia_nodding_smile
    with dissolve

    a "Of course, Lily. What do you want to play?"

    lily "How about a board game? We haven't done that in ages."

    show family_playing_game
    with dissolve

    "The family gathers around the coffee table, playing a board game and sharing laughter. The simple joy of the moment fills the room with warmth."

    show amelia_laughing_with_family
    with dissolve

    "Amelia laughs heartily, feeling a deep sense of belonging and love."

    a "(This is what it's all about. Family, love, connection. These are the things that matter most.)"

    show amelia_talking_with_parents
    with dissolve

    "After the game, Amelia sits with her parents, talking late into the night about her experiences, her dreams, and her plans for the future."

    mr_james "What's next for you, Amelia? Do you have any plans for the summer?"

    show amelia_enthusiastic
    with dissolve

    a "I’m thinking of applying for a summer research position at the university. I want to dive deeper into my studies and maybe even contribute to some groundbreaking work."

    mrs_james "That sounds wonderful. We're here to support you every step of the way."

    "They continue to talk, the night growing deeper and the bond between them stronger than ever."

    show amelia_in_bed
    with dissolve

    "Later, as Amelia lies in bed, she reflects on the day's events and her journey so far."

    a "(I've come so far, and there's still so much more to explore. I can't wait to see what the future holds.)"

    "With a contented sigh, she closes her eyes, ready to embrace the new adventures that await her."

    return

label chapter_12_social_butterfly:
    show amelia_in_room_preparing
    with dissolve

    "Amelia stands in front of her mirror, adjusting her dress and smiling at her reflection. Tonight is the big reunion with her friends from Plymouth, and she's filled with excitement and anticipation."

    a "(I can't wait to see everyone again. This year has been incredible, and it's all thanks to the amazing people I've met.)"

    show amelia_leaving_home
    with dissolve

    "She grabs her purse and heads out the door, waving goodbye to her parents."

    mrs_james "Have a great time, sweetheart! Say hello to everyone for us."

    mr_james "Enjoy yourself, Amelia. You deserve it."

    show amelia_smiling_wave
    with dissolve

    a "Thanks, Mom, Dad. I'll be back later tonight."

    show reunion_location
    with dissolve

    "Amelia arrives at a trendy café in the heart of London, the chosen spot for their reunion. The place is buzzing with energy, and she immediately spots her friends at a corner table, waving enthusiastically."

    show amelia_greeting_friends
    with dissolve

    a "Hey everyone! It's so good to see you all!"

    show friends_hugging_amelia
    with dissolve

    lucas "Amelia! We've missed you!"

    zara "It's been too long!"

    raj "Our social butterfly has returned!"

    show amelia_sitting_with_friends
    with dissolve

    "They all sit down, and the conversation flows effortlessly. Stories of their summer so far, reminiscing about their favorite memories from the past year, and plans for the future fill the air."

    lucas "Remember that night at the Union when we all decided to dance like nobody was watching?"

    show group_laughing
    with dissolve

    amelia "How could I forget? That was the best night ever!"

    zara "And the time we stayed up all night studying for that psychology exam? We were all so exhausted, but we made it through together."

    show amelia_nodding
    with dissolve

    a "We've been through so much. I'm so grateful for each and every one of you."

    show raj_smiling
    with dissolve

    raj "You've brought so much joy and light into our lives, Amelia. Your energy is infectious."

    show amelia_blushing
    with dissolve

    a "Thank you, Raj. You all have been my rock. I wouldn't have made it through the year without your support."

    show zara_raising_glass
    with dissolve

    zara "A toast, to Amelia. For being the heart and soul of our group. To friendships that last a lifetime."

    show friends_toasting
    with dissolve

    all "To Amelia!"

    show amelia_emotional
    with dissolve

    "As they clink glasses, Amelia feels a swell of emotion. She looks around at her friends, the people who have become her second family."

    a "(These moments, these connections, they mean everything to me. I'm so lucky to have found such incredible friends.)"

    show amelia_talking_to_lucas
    with dissolve

    "Later in the evening, Lucas pulls Amelia aside, a serious look on his face."

    lucas "Amelia, can I talk to you for a moment?"

    amelia "Of course, Lucas. What's up?"

    show lucas_confiding
    with dissolve

    lucas "I just wanted to say... thank you. For everything. You've helped me come out of my shell in ways I never thought possible. You've made such a difference in my life."

    show amelia_touched
    with dissolve

    a "Lucas, that means so much to me. You've been an amazing friend. We've all grown together."

    lucas "I know I've struggled with opening up, but you made it feel safe. You've got a gift, Amelia. You bring people together."

    show amelia_hugging_lucas
    with dissolve

    "They share a heartfelt hug, the bond between them stronger than ever."

    show amelia_talking_to_zara
    with dissolve

    "Amelia then finds herself chatting with Zara, who looks contemplative."

    amelia "Zara, is everything okay?"

    show zara_confiding
    with dissolve

    zara "I've been reflecting a lot lately. About how far we've come, and how much you've helped me understand and cope with the challenges I've faced."

    show amelia_listening
    with dissolve

    a "Zara, you're one of the strongest people I know. You've taught me so much about resilience and courage."

    zara "And you've shown me the power of empathy and friendship. You've always been there, even when things were tough."

    show amelia_smiling
    with dissolve

    a "That's what friends are for. We'll always have each other's backs."

    show zara_hugging_amelia
    with dissolve

    "They hug tightly, a moment of deep connection and understanding."

    show amelia_talking_to_raj
    with dissolve

    "Finally, Amelia finds herself with Raj, who seems lost in thought."

    amelia "Raj, what’s on your mind?"

    show raj_confiding
    with dissolve

    raj "I’ve been thinking about the future. About how we’re all going to move forward with our lives. It’s exciting, but also a little scary."

    show amelia_nodding
    with dissolve

    a "I know what you mean. Change can be daunting. But we have each other, no matter where life takes us."

    raj "You’ve given me so much confidence, Amelia. Your positivity and support have made all the difference."

    show amelia_touched
    with dissolve

    a "And you've given me the same, Raj. We're all in this together."

    show group_talking_and_laughing
    with dissolve

    "The night continues with more laughter, stories, and heartfelt conversations. Amelia feels a profound sense of belonging and love."

    a "(These friendships are the most precious things in my life. They've shaped me, supported me, and made me who I am today.)"

    show amelia_and_friends_at_end_of_night
    with dissolve

    "As the evening draws to a close, the group gathers outside the café, the cool night air filled with the promise of more adventures to come."

    lucas "This has been amazing. We need to do this more often."

    zara "Definitely. Let’s make it a tradition."

    raj "Agreed. To many more nights like this."

    show amelia_smiling_content
    with dissolve

    a "To friendship, and to the amazing journey ahead of us."

    show amelia_walking_home
    with dissolve

    "As Amelia walks home, she reflects on the night and the incredible bonds she's formed."

    a "(I've come a long way from that shy, unsure girl who started university. I'm surrounded by love and friendship, and I know I can face anything with these amazing people by my side.)"

    show amelia_smiling_upward
    with dissolve

    a "Here's to the future, and to the beautiful friendships that make life so wonderful."

    return

label chapter_12_mental_health_advocate:
    show amelia_in_room_preparing
    with dissolve

    "Amelia sits at her desk, going through notes and resources she's gathered over the past year. Her commitment to mental health advocacy has only grown stronger after her experiences with Sarah and her own challenges."

    a "(This is where I can make a real difference. I’ve seen firsthand how important it is to support those struggling with mental health issues.)"

    show amelia_packing_bag
    with dissolve

    "She packs a bag with pamphlets, books, and other materials, preparing for her first volunteer session at a local mental health organization."

    a "(It's time to give back, to use what I've learned to help others.)"

    show amelia_leaving_home
    with dissolve

    "Amelia heads out, waving goodbye to her parents."

    mrs_james "Good luck today, Amelia. We're so proud of you."

    mr_james "You’re doing important work. We're here for you."

    show amelia_smiling_wave
    with dissolve

    a "Thanks, Mom, Dad. I’ll see you later."

    show mental_health_organization
    with dissolve

    "Amelia arrives at the mental health organization, greeted by a friendly volunteer coordinator."

    coordinator "Amelia, welcome! We're so glad to have you here."

    amelia "Thank you. I'm excited to get started."

    show amelia_helping_people
    with dissolve

    "Amelia spends the day talking to people, offering support, and sharing resources. She listens to their stories, providing a compassionate ear and valuable advice."

    person_1 "It's been so hard. I feel like no one understands what I'm going through."

    show amelia_listening
    with dissolve

    a "I hear you. It's important to know that you're not alone. There are people who care and want to help."

    person_2 "Thank you for listening. It means more than you know."

    "As the day goes on, Amelia feels a deep sense of fulfillment and purpose."

    show amelia_talking_to_coordinator
    with dissolve

    a "This has been incredible. I feel like I'm truly making a difference."

    coordinator "You are, Amelia. Your empathy and dedication are inspiring. We're lucky to have you."

    show amelia_smiling
    with dissolve

    a "Thank you. I’m grateful for this opportunity."

    show amelia_reflecting_at_home
    with dissolve

    "Later that evening, back home, Amelia reflects on the day's experiences."

    a "(Today was just the beginning. There's so much more to do, so many people to help.)"

    show amelia_on_phone_with_sarah
    with dissolve

    "She calls Sarah, eager to share her experiences."

    if sarah_alive:
        show sarah_on_phone
        with dissolve

        sarah "Amelia, I'm so proud of you. You’re doing such important work."

        show amelia_smiling
        with dissolve

        a "Thanks, Sarah. You've been a huge inspiration for me. Seeing you fight and overcome your struggles has shown me how crucial mental health support is."

        sarah "And you've been my rock, Amelia. I'm so grateful for your friendship and support."

        show amelia_determined
        with dissolve

        a "We’re in this together, Sarah. Always."

    else:
        show amelia_grieving_sarah
        with dissolve

        a "(Sarah... I wish you could see what I'm doing. I hope I'm making you proud.)"

        "Amelia looks at a photo of Sarah on her desk, a bittersweet smile on her face."

        a "(Your fight wasn’t in vain, Sarah. I promise to keep advocating for mental health, to make a difference in your memory.)"

    show amelia_in_living_room_with_family
    with dissolve

    "At dinner, Amelia shares her experiences with her family."

    mr_james "How was your first day, Amelia?"

    show amelia_smiling_warmly
    with dissolve

    a "It was amazing. I talked to so many people, heard their stories, and provided support. It felt incredibly rewarding."

    mrs_james "We're so proud of you. Your compassion and dedication are truly admirable."

    show amelia_thankful
    with dissolve

    a "Thank you. I couldn’t have done this without your support and encouragement."

    show lily_looking_up_to_amelia
    with dissolve

    lily "I want to help people too when I grow up. Just like you, Amelia."

    show amelia_smiling_at_lily
    with dissolve

    a "You can do anything you set your mind to, Lily. I'm sure you'll make a big difference in the world."

    show amelia_writing_in_journal
    with dissolve

    "Later, Amelia sits at her desk, writing in her journal."

    a "{i}Today was the start of something incredible. I'm more determined than ever to be an advocate for mental health. To listen, to support, to make a difference.{/i}"

    a "{i}Sarah's struggle, my own journey... they’ve taught me the importance of this work. I will keep pushing forward, for those who need a voice, for those who need hope.{/i}"

    show amelia_determined
    with dissolve

    a "(This is my calling. I will continue to fight for mental health awareness and support. This is just the beginning.)"

    show amelia_lying_in_bed
    with dissolve

    "As she lies in bed, Amelia feels a profound sense of purpose and hope for the future."

    a "(Together, we can make a difference. One step at a time.)"

    return

label chapter_12_balanced_growth:
    show amelia_in_room_preparing
    with dissolve

    "Amelia stands in her room, taking a deep breath as she looks around at the familiar surroundings. This past year has been a journey of immense personal growth, and she's ready to bring that balance into her everyday life."

    a "(I've learned so much about balancing my academic pursuits, social life, and personal well-being. It's time to integrate all of it.)"

    show amelia_packing_bag
    with dissolve

    "She packs a bag with a few essentials: a journal, a couple of books on psychology, and some photos of her friends. Today, she's meeting her mentor and later, spending time with family and friends."

    a "(It's important to remember the people who supported me and the lessons I've learned.)"

    show amelia_leaving_home
    with dissolve

    "Amelia heads out, waving goodbye to her parents."

    mrs_james "Enjoy your day, Amelia. We're so proud of you."

    mr_james "You've become such an amazing young woman."

    show amelia_smiling_wave
    with dissolve

    a "Thank you, Mom, Dad. I'll see you later."

    show amelia_meeting_mentor
    with dissolve

    "Amelia arrives at a quiet café where she's meeting her mentor, Prof. Hawthorne."

    hawthorne "Amelia, it's wonderful to see you. How have you been?"

    show amelia_smiling_sitting
    with dissolve

    a "I've been well, Professor. Reflecting on everything I've learned this year."

    show hawthorne_nodding
    with dissolve

    hawthorne "You've had quite the journey. Balancing your studies, friendships, and personal growth isn't easy, but you've done an exemplary job."

    show amelia_grateful
    with dissolve

    a "Thank you. Your guidance has been invaluable. I've learned to prioritize what's truly important and maintain a healthy balance."

    hawthorne "That's a lesson many struggle to learn. I'm proud of your progress. Keep nurturing those aspects of your life, and you'll continue to thrive."

    show amelia_reflecting
    with dissolve

    a "I will, Professor. Thank you for everything."

    show amelia_with_family
    with dissolve

    "Later, Amelia spends time with her family in the park. They have a picnic, enjoying the sunny day and each other's company."

    mrs_james "It's so nice to have you home, Amelia. We’ve missed these moments."

    show amelia_smiling_warmly
    with dissolve

    a "I've missed them too. Being away has made me appreciate family time even more."

    show lily_looking_up_to_amelia
    with dissolve

    lily "Amelia, can we play a game? Like we used to?"

    show amelia_nodding_smile
    with dissolve

    a "Of course, Lily. What do you want to play?"

    lily "How about hide and seek?"

    show amelia_laughing
    with dissolve

    a "Alright, you're on!"

    "They play hide and seek, laughter echoing through the park. Amelia feels a profound sense of joy and balance."

    show amelia_with_friends
    with dissolve

    "In the evening, Amelia meets her friends for dinner at a local restaurant."

    lucas "Amelia! It’s great to see you."

    zara "We’ve missed you!"

    raj "Our balanced achiever is back!"

    show amelia_smiling_at_friends
    with dissolve

    a "I've missed you all too. It's so good to be back together."

    show group_dining
    with dissolve

    "They enjoy a meal together, sharing stories and catching up on each other's lives."

    zara "You seem so at peace, Amelia. It's inspiring."

    show amelia_reflecting_on_growth
    with dissolve

    a "I've learned the importance of balance. It's been a journey, but I feel like I'm in a good place now."

    raj "Your journey has been incredible to witness. You’ve grown so much."

    show amelia_grateful
    with dissolve

    a "Thank you. We've all grown together. Your support has meant the world to me."

    show lucas_nodding
    with dissolve

    lucas "We’re here for each other, no matter what."

    show amelia_talking_to_group
    with dissolve

    a "I couldn’t have done it without you all. Our friendship has been my anchor."

    show friends_toasting
    with dissolve

    "They raise their glasses in a toast to their friendship and shared journey."

    all "To friendship and growth!"

    show amelia_reflecting_in_room
    with dissolve

    "Later that night, Amelia sits in her room, writing in her journal."

    a "{i}This year has taught me so much about balance. Balancing my academic goals, my social life, and my personal well-being has been key to my growth. I've realized the importance of nurturing each part of my life.{/i}"

    a "{i}I've grown academically, formed deep and meaningful friendships, and taken care of my mental health. It's a continuous journey, but I feel ready to face whatever comes next with this newfound sense of balance.{/i}"

    show amelia_determined
    with dissolve

    a "(This is just the beginning. With balance, I can achieve anything.)"

    show amelia_lying_in_bed
    with dissolve

    "As she lies in bed, Amelia feels a profound sense of peace and readiness for the future."

    a "(I’m ready for whatever comes next. With balance and the support of my loved ones, I can face any challenge.)"

    return

label chapter_12_enlightenment:
    play music weight_of_gold fadein 1.0 volume 0.8
    show amelia_in_room_preparing_ritual
    with dissolve

    "Amelia stands in her room, surrounded by alchemical texts she has begun to rely on{p=1}{nw}"
    "The ingredients for an intense spagyric process laying on a table infront of her.{p=1}{nw}"
    "Tonight, she will attempt to create the philosopher's stone{p=1}{nw}"
    "The culmination of her alchemical journey research and studies.{p=1}{nw}"

    a "(This is it. Everything I've learned has led me to this moment. It's time to see if I can create the stone.){p=1}{nw}"

    show amelia_beginning_ritual
    with dissolve

    "She begins the ritual, carefully following the intricate steps described in the ancient manuscripts.{p=1}{nw}"
    "The air in the room grows heavy with anticipation and the scent of the alchemical ingredients.{p=1}{nw}"

    a "(Focus, Amelia. This is about intention, about transformation.){p=1}{nw}"

    "Hours pass as Amelia works diligently, her movements precise and her mind clear.{p=1}{nw}"
    "Finally, the process is complete.{p=1}{nw}"
    
    show amelia_holding_stone
    with dissolve
    "Before her lies a small, glowing stone, pulsating with an otherworldly energy.{p=2}{nw}"
    "She holds the philosopher's stone in her hands, feeling its power{p=2}{nw}"
    "But not noticing any immediate change within herself.{p=1}{nw}"

    a "This is it. The culmination of my journey.{p=1}{nw}"
    a "But... I don't feel any different.{p=1}{nw}"

    show amelia_ingesting_stone
    with dissolve

    "With a deep breath, Amelia ingests the stone.{p=4}{nw}"
    "She waits for a moment, expecting a profound transformation, but nothing happens immediately.{p=2}{nw}"
    "Feeling slightly disappointed but hopeful, she decides to go for a walk to clear her mind.{p=2}{nw}"

    a "(Maybe the effects take time. A walk will help me think.){p=2}{nw}"
    stop music fadeout 2.0
    play music jag_finns_kvar fadein 2.0 volume 0.3

    show amelia_walking_outside
    with dissolve

    "Amelia steps outside, the cool evening air refreshing her senses.{p=2}{nw}"
    "She wanders through the streets, lost in thought about her journey and the stone's potential.{p=2}{nw}"

    a "I've come so far. Even if I don't feel different now{p=2}{nw}"
    "The journey itself has been transformative.{p=2}{nw}"

    show mysterious_garden
    with dissolve

    "Her wandering leads her to a garden she has never seen before.{p=2}{nw}"
    "It's lush and vibrant, filled with flowers of every color.{p=2}{nw}"
    "In the center, there is a fountain, and by the fountain stands a woman. She radiates a serene and powerful presence.{p=4}{nw}"

    show amelia_approaching_woman
    with dissolve

    "Amelia approaches the woman, feeling a strange sense of familiarity.{p=2}{nw}"

    a "Hello. I don't think I've seen you here before.{p=2}{nw}"

    "Welcome, Amelia. I've been waiting for you.{p=2}{nw}"

    show amelia_confused
    with dissolve

    a "Waiting for me? Who are you?{p=2}{nw}"

    show woman_smiling
    with dissolve

    "Names are not important. What matters is the journey you are on and the wisdom you seek.{p=4}{nw}"

    show amelia_listening_intently
    with dissolve

    a "What wisdom do you mean?{p=2}{nw}"

    "Sit with me by the fountain, and I will tell you a story.{p=2}{nw}"

    show amelia_sitting_by_fountain
    with dissolve

    "Amelia sits beside the woman, the sound of the water calming her.{p=2}{nw}"
    "The woman begins to speak, her voice soft and soothing.{p=2}{nw}"

    "Your journey began long before you set foot in Plymouth.{p=0.5}{nw}"
    "Your recent past has been marked by trials, pushing you to the edge of your very understanding of the world and your place within it.{p=0.5}{nw}"
    "You've faced academic pressures that tested your intellect and personal challenges that weighed heavily on your heart.{p=0.5}{nw}"
    "Amelia, your journey has been a crucible, shaping and refining you in ways you might not yet fully comprehend.{p=0.5}{nw}"

    "You arrived at Plymouth full of hope, yet unaware of the shadows you would encounter.{p=0.5}{nw}"
    "The friends you've made—Ella, Zara, Lucas, Maya, Raj—each brought a piece of the puzzle that is your life.{p=0.5}{nw}"
    "They've taught you the beauty of diversity, the strength found in unity, and the power of compassion.{p=0.5}{nw}"

    "But, my dear, it is Sarah who left the most indelible mark.{p=0.5}{nw}"
    "Her struggle with depression was a mirror, reflecting the unspoken fears and hidden pains within you.{p=0.5}{nw}"
    "Her fate was a profound lesson, reminding you of the fragility of life and the importance of mental health.{p=0.5}{nw}"
    "The day you found her, you realized the gravity of your role in this world.{p=0.5}{nw}"
    "Whether she found peace or succumbed to her pain, her story intertwined with yours, urging you to advocate for those who suffer in silence.{p=0.5}{nw}"

    "Every choice you've made has led you here, standing at the threshold of true understanding.{p=0.5}{nw}"
    "You've delved into the depths of psychology, explored the mystical and the unknown, and faced your darkest fears.{p=0.5}{nw}"
    "You've grown, Amelia, more than you can see.{p=0.5}{nw}"
    "The enlightenment you seek is not a destination but a journey, a continuous path of learning, compassion, and self-discovery.{p=0.5}{nw}"

    "Remember Sarah, remember her struggle and her strength.{p=0.5}{nw}"
    "Use that memory to fuel your resolve to make a difference.{p=0.5}{nw}"
    "Your story is far from over, and your potential is limitless.{p=0.5}{nw}"
    "Embrace your past, cherish your present, and step boldly into your future.{p=0.5}{nw}"

    show amelia_listening_emotional
    with dissolve

    a "Yes, it has been challenging... but I've learned so much.{p=1}{nw}"

    "These experiences have shaped you, prepared you for the path you walk now.{p=1}{nw}"
    "Your heart has been forged in the fires of adversity, and through it, you have discovered your strength.{p=1}{nw}"

    "The woman’s voice takes on a more cryptic tone{p=1}{nw}"

    "The path ahead is one of transformation. Just as the two always become the one.{p=1}{nw}"
    "The Prima Materia within you, the raw essence of your being, will undergo a sacred transformation.{p=1}{nw}" 
    "You will navigate the Nigredo, the darkness and dissolution, and emerge into the Albedo, the purification in the double sign of your own mercury.{p=1}{nw}"

    show amelia_fully_absorbed
    with dissolve

    "Amelia listens, her heart and mind fully absorbed by the woman’s words.{p=1}{nw}"

    "In the Citrinitas, the dawning of the new consciousness, you will find clarity and purpose.{p=1}{nw}" 
    "And finally, in the Rubedo, the reddening, you will achieve the Great Work{p=1}{nw}"
    "Trust in the process, and know that every challenge, every joy, is part of the divine tapestry of your life.{p=1}{nw}"

    "Amelia feels the weight of the transmission, settling deep within her soul.{p=1}{nw}"
    "Tears begin to well up in her eyes as she realizes the profound truth of the woman’s words.{p=1}{nw}"

    a "I... I understand. At last I understand{p=1}{nw}"

    show woman_fading
    with dissolve

    "The woman smiles, her form beginning to fade.{p=1}{nw}"

    "With that, the woman vanishes, leaving Amelia alone by the fountain, her heart full and her mind buzzing with new insights.{p=1}{nw}"

    show amelia_waking_up_in_bed
    with dissolve

    "Amelia wakes up in her bed, unsure if the encounter was real or a dream.{p=1}{nw}"
    "But the tears on her face and the deep sense of peace within her tell her{p=1}{nw}"
    "It was more than just a figment of her imagination.{p=1}{nw}"

    a "(This is just the beginning, I can achieve anything.){p=1}{nw}"

    show amelia_in_room_reflecting
    with dissolve

    "Back in her room, Amelia sits down and begins to write in her journal, capturing the emotions and insights from the encounter.{p=1}{nw}"

    a "{i}Tonight, I received a gift beyond measure. The wisdom of an ancient lineage flows through me now.{/i}{p=1}{nw}"
    a "{i}My journey is just beginning, and I feel ready to face whatever comes next.{/i}"

    show amelia_lying_in_bed_3
    with dissolve

    "As she lies in bed, Amelia feels a profound sense of peace and readiness for the future."

    a "(I’m ready for whatever comes next, I can face any challenge.)"

    return

label chapter_12_tragic_ending:
    show amelia_in_room_reflecting
    with dissolve

    "Amelia sits in her room, surrounded by the familiar comforts of home, but the weight of the past year bears heavily on her shoulders. She looks at the photos on her desk, memories from her first year at Plymouth University, but one photo in particular catches her eye – a picture of her and Sarah, smiling together before everything changed."

    a "(Sarah... I wish things had turned out differently. The pain of losing her is still so fresh.)"

    show amelia_tearful
    with dissolve

    "Tears well up in her eyes as she remembers the night Sarah passed away. The grief is overwhelming, and the sense of loss is immeasurable."

    show amelia_flashback_sarah
    with dissolve

    "Flashback to the night Sarah passed away. Amelia at Sarah's bedside, tears streaming down her face. The room is filled with a profound silence."

    a "Sarah, I'm so sorry. We tried everything... I miss you so much."

    "The scene fades back to Amelia in her room, the weight of grief pressing down on her."

    a "(Her memory will always be with me. I'll carry her spirit forward in everything I do.)"

    show amelia_staring_at_wall
    with dissolve

    "Amelia sits in silence, staring at the wall, feeling the emptiness left by Sarah's absence. Her parents, noticing her distress, enter the room quietly."

    mr_james "Amelia, sweetheart, are you okay?"

    show amelia_shaking_head
    with dissolve

    a "No, Dad. I'm not. I miss her so much. I don't know how to move on."

    mrs_james "It's okay to feel this way, Amelia. Grief is a heavy burden, but you don't have to carry it alone. We're here for you."

    show amelia_hugging_parents
    with dissolve

    "Amelia breaks down, hugging her parents tightly. Their warmth and love provide some comfort, but the pain remains."

    a "Thank you... I just wish things were different."

    show amelia_sitting_in_garden
    with dissolve

    "Later, Amelia goes to the garden, seeking solace in nature. She sits on a bench, lost in thought."

    a "(Everything feels so empty without her. I don't know how to fill this void.)"

    show amelia_receiving_text
    with dissolve

    "Her phone buzzes with a text from Lucas."

    lucas "{i}Hey Amelia, just checking in. How are you holding up?{/i}"

    show amelia_texting_back
    with dissolve

    "Amelia types a response, her fingers trembling."

    a "{i}Hi Lucas. I'm struggling. Everything feels so heavy without Sarah.{/i}"

    show amelia_waiting_for_response
    with dissolve

    "A moment later, Lucas's reply comes through."

    lucas "{i}I can't imagine how hard it is for you. Just remember, you're not alone. We're all here for you.{/i}"

    a "{i}Thank you, Lucas. I appreciate it.{/i}"

    show amelia_crying_in_garden
    with dissolve

    "Amelia puts her phone down and cries, the weight of her grief overwhelming her. She feels a hand on her shoulder and looks up to see Zara standing there."

    zara "Amelia, I’m so sorry. I know how much Sarah meant to you."

    show amelia_hugging_zara
    with dissolve

    a "Thank you, Zara. I don't know how to get through this."

    zara "You don't have to do it alone. We're all here for you. Lean on us when you need to."

    show amelia_nodding
    with dissolve

    a "I will. It's just so hard."

    "They sit together in silence, the shared grief bringing a small measure of comfort."

    show amelia_talking_to_professor_hawthorne
    with dissolve

    "The next day, Amelia meets with Professor Hawthorne, who has been a mentor and support throughout her journey."

    hawthorne "Amelia, I'm deeply sorry for your loss. Sarah was a wonderful person."

    amelia "Thank you, Professor. I feel lost without her."

    hawthorne "Grief is a difficult path to walk. It's important to allow yourself to feel, to grieve. But remember, Sarah's memory can be a source of strength as well."

    show amelia_nodding_sadly
    with dissolve

    a "I’ll try. It's just... everything feels so empty."

    hawthorne "In time, you will find ways to honor her memory and find strength in her spirit. Lean on your friends, your family. They will help you through this."

    show amelia_at_memorial
    with dissolve

    "Later, Amelia visits a small memorial she has set up for Sarah. She lights a candle and places a photo of them together next to it."

    a "(Sarah, I hope you can hear me. I miss you every day. I'm trying to find my way without you.)"

    "She sits there for a while, the flickering flame offering a small comfort."

    show amelia_journaling
    with dissolve

    "Back in her room, Amelia writes in her journal, capturing her thoughts and feelings."

    a "{i}Today was another difficult day. I visited Sarah's memorial and talked to my friends. Their support means so much, but the pain is still overwhelming. I keep telling myself that it will get easier, that time will heal, but right now it feels like an endless void.{/i}"

    show amelia_lying_in_bed
    with dissolve

    "As she lies in bed, Amelia feels a deep sense of loss and uncertainty about the future."

    a "(I don’t know what comes next. But I know I have to keep going, for Sarah and for myself.)"

    "She closes her eyes, the tears still fresh on her cheeks, and falls into a restless sleep, hoping that one day, the pain will lessen and she will find a way to move forward."

    return
