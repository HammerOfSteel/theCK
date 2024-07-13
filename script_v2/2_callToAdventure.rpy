label chapter_2:

    play music "call_to_adventure_theme.mp3" loop

    show 2_intro_4 with dissolve
    a "Yeah, I did. I still can't believe I'm going to Plymouth University."

    show 2_intro_5 with dissolve
    dad "It's a big step, but I know you're ready for it."

    show 2_intro_6 with dissolve
    narrator "They sit down to breakfast, enjoying the meal together. The kitchen is filled with a comfortable silence, only broken by the occasional clink of cutlery."

    menu:
        "Talk about the future":
            jump talk_future
        "Discuss fears and anxieties":
            jump discuss_fears
        "Express gratitude for Dad's support":
            jump express_gratitude

label talk_future:

    show 2_future_1 with dissolve
    a "Dad, have you thought about what it's going to be like once I leave? The house will be so quiet."

    dad "It will be different, that's for sure. But I'm excited for you, Amelia. This is a big opportunity."

    a "I know. I'm excited too, but I can't help but worry about how things will change."

    dad "Change can be good, Amelia. It's a chance for both of us to grow. I'll find new hobbies, maybe even travel a bit. And you'll be starting an incredible new chapter."

    menu:
        "Ask about his plans":
            jump ask_dad_plans
        "Share your plans":
            jump share_your_plans

label ask_dad_plans:

    show 2_dad_plans_1 with dissolve
    a "What kind of hobbies are you thinking about, Dad?"

    dad "Well, I've always wanted to learn how to play the guitar. Maybe I'll finally take some lessons."

    a "That sounds great. You'll have to play for me when I come home for holidays."

    dad "Deal. And who knows, maybe I'll come visit you at university and we can explore Plymouth together."

    jump breakfast_continue

label share_your_plans:

    show 2_your_plans_1 with dissolve
    a "I've been thinking about joining some clubs and maybe even starting a study group."

    dad "That's a great idea. Getting involved will help you make friends and settle in faster."

    a "Yeah, and it will keep me busy. I'm looking forward to it."

    dad "You'll do great, Amelia. Just remember to take things one step at a time."

    jump breakfast_continue

label discuss_fears:

    show 2_fears_1 with dissolve
    a "Dad, I'm a little scared about moving away. What if I don't make any friends? What if I can't handle the coursework?"

    dad "It's natural to feel scared, Amelia. But you're stronger than you think. You'll make friends, and if the coursework gets tough, you'll find a way through it."

    a "I guess you're right. It's just a lot to think about."

    dad "Remember, you can always call me. No matter what time it is, I'm here for you."

    menu:
        "Discuss specific fears":
            jump specific_fears
        "Seek reassurance":
            jump seek_reassurance

label specific_fears:

    show 2_specific_fears_1 with dissolve
    a "I'm worried about fitting in. What if I'm not good enough?"

    dad "Amelia, you've always been more than good enough. Just be yourself, and people will appreciate you for who you are."

    a "And what if I get homesick?"

    dad "It's okay to miss home. But think of it as a chance to grow. You'll come back stronger and with amazing stories to tell."

    jump breakfast_continue

label seek_reassurance:

    show 2_seek_reassurance_1 with dissolve
    a "I just need to hear that everything will be okay."

    dad "Everything will be okay, Amelia. You have what it takes to succeed. And remember, you're never alone. We're in this together."

    a "Thanks, Dad. That really helps."

    jump breakfast_continue

label express_gratitude:

    show 2_gratitude_1 with dissolve
    a "Dad, I just want to say thank you. For everything. Your support means the world to me."

    dad "You don't have to thank me, Amelia. It's my job to support you. And I'm so proud of you."

    a "I know, but still. You've always been there for me, and I appreciate it more than I can say."

    menu:
        "Talk about past support":
            jump past_support
        "Express hopes for future":
            jump future_hopes

label past_support:

    show 2_past_support_1 with dissolve
    a "Remember when I had that big presentation in high school and I was so nervous?"

    dad "How could I forget? You practiced in front of me for hours."

    a "You sat through all of it without complaining. That meant a lot to me."

    dad "I knew you could do it. And you were amazing. Just like you'll be at university."

    jump breakfast_continue

label future_hopes:

    show 2_future_hopes_1 with dissolve
    a "I hope I can make you proud, Dad. I want to do well at university and make the most of this opportunity."

    dad "You already make me proud, Amelia. Just do your best and enjoy the journey. That's all I can ask for."

    a "I will, Dad. Thank you."

    jump breakfast_continue

label breakfast_continue:

    show 2_intro_6 with dissolve
    narrator "They sit down to breakfast, enjoying the meal together. The kitchen is filled with a comfortable silence, only broken by the occasional clink of cutlery."

    show 2_intro_7 with dissolve
    narrator "After breakfast, Amelia heads back to her room to start packing. She looks around, taking in all the familiar sights of her childhood bedroom."

    show 2_intro_8 with dissolve
    a "This room holds so many memories... it's going to be strange leaving it behind."

    show 2_intro_9 with dissolve
    narrator "She opens her closet and begins sorting through her clothes, deciding what to take with her to university."

    show 2_intro_10 with dissolve
    narrator "As she packs, her thoughts drift to the future, filled with excitement and a touch of anxiety about the unknown."

    a "I wonder what my new dorm will be like. I hope I get along with my roommate."

    show 2_intro_11 with dissolve
    narrator "Amelia carefully packs her favorite books, some photos, and a few keepsakes that remind her of home."

    show 2_intro_12 with dissolve
    narrator "She sits down at her desk and writes a list of things she needs to do before she leaves:"

    menu:
        "Review old photos and items (Memory Lane)":
            jump memory_lane
        "Write goodbye letters (Goodbye Letters)":
            jump goodbye_letters
        "Pack emotionally significant items (Therapeutic Packing)":
            jump therapeutic_packing

label memory_lane:
    menu:
        "Choose a photo to remember":
            "A photo with Ella":
                jump ella_photos
            "A photo with Dad":
                jump dad_photos
            "A photo with Lily":
                jump lily_photos

label ella_photos:
    menu:
        "Choose a memory with Ella":
            "Childhood Playdate":
                jump ella_playdate
            "High School Graduation":
                jump ella_graduation
            "Halloween Party":
                jump ella_halloween

label ella_playdate:
    show photo_playdate with dissolve
    narrator "Amelia picks up a photo of her and Ella playing in a sandbox at the local park. She smiles at the memory of their first playdate."
    a "I remember that day so well. We were so young and carefree."
    
    menu:
        "Amelia's thoughts":
            "Remembering the laughter":
                jump ella_playdate_laughter
            "Thinking about the sandbox":
                jump ella_playdate_sandbox
            "Recalling Ella's smile":
                jump ella_playdate_smile

label ella_playdate_laughter:
    scene park_sandbox with dissolve
    narrator "The sound of laughter fills Amelia's mind as she recalls that sunny day."
    a "We laughed so much that day, building sandcastles and digging tunnels."
    show ella_young with dissolve
    e "Look, Amelia! I made a sandcastle!"
    a "That's amazing, Ella! Let's make a moat around it."
    narrator "They spent hours playing, their laughter echoing through the park. It was the beginning of a beautiful friendship."
    return

label ella_playdate_sandbox:
    scene park_sandbox with dissolve
    narrator "Amelia remembers the feel of the sand between her fingers as she and Ella played in the sandbox."
    a "We were so focused on building the perfect sandcastle. It was like our own little world."
    show ella_young with dissolve
    e "Let's make the biggest castle ever, Amelia!"
    a "Yeah! We'll need a lot of sand."
    narrator "Their imagination ran wild as they created their sandy masterpiece, solidifying a bond that would last a lifetime."
    return

label ella_playdate_smile:
    scene park_sandbox with dissolve
    narrator "Amelia's mind is filled with the image of Ella's radiant smile."
    a "Ella was always so cheerful. Her smile could light up the darkest days."
    show ella_young with dissolve
    e "This is so much fun, Amelia!"
    a "It really is. I'm glad we're friends, Ella."
    narrator "That smile, that day, marked the start of an unbreakable friendship."
    return

label ella_graduation:
    show photo_graduation with dissolve
    narrator "Amelia picks up a photo of her and Ella in their graduation gowns. The memory of their high school graduation day floods back."
    a "Graduation day. We were so proud and full of dreams."

    menu:
        "Amelia's thoughts":
            "Remembering the ceremony":
                jump ella_graduation_ceremony
            "Thinking about the speeches":
                jump ella_graduation_speeches
            "Recalling the celebrations":
                jump ella_graduation_celebrations

label ella_graduation_ceremony:
    scene graduation_ceremony with dissolve
    narrator "Amelia recalls the graduation ceremony, the excitement in the air, and the sense of accomplishment."
    a "Walking across that stage felt surreal. We had worked so hard to get there."
    show ella_graduation with dissolve
    e "We did it, Amelia! We're officially graduates!"
    a "I know! Can you believe it?"
    narrator "The sense of achievement and the thrill of reaching a milestone they had worked so hard for was palpable."
    return

label ella_graduation_speeches:
    scene graduation_ceremony with dissolve
    narrator "Amelia remembers the speeches, each one filled with wisdom and encouragement for the future."
    a "The speeches were so inspiring. They made me feel ready to take on the world."
    show ella_graduation with dissolve
    e "I loved the part about following your dreams, didn't you?"
    a "Yes, it was so motivating. We're going to do great things, Ella."
    narrator "The words of wisdom from the speakers left a lasting impression on both of them, fueling their aspirations."
    return

label ella_graduation_celebrations:
    scene graduation_party with dissolve
    narrator "Amelia's thoughts drift to the celebrations after the ceremony. The joy and camaraderie they shared."
    a "The party after graduation was so much fun. We danced and laughed all night."
    show ella_party with dissolve
    e "This is the best night ever! Let's dance, Amelia!"
    a "Absolutely! Let's make it a night to remember!"
    narrator "The celebrations marked the end of one chapter and the beginning of another, filled with hope and endless possibilities."
    return

label ella_halloween:
    show photo_halloween with dissolve
    narrator "Amelia picks up a photo of her and Ella in Halloween costumes, their faces lit up with excitement."
    a "Halloween was always so much fun with Ella. We went all out with our costumes."

    menu:
        "Amelia's thoughts":
            "Remembering the costumes":
                jump ella_halloween_costumes
            "Thinking about trick-or-treating":
                jump ella_halloween_treating
            "Recalling the haunted house":
                jump ella_halloween_haunted

label ella_halloween_costumes:
    scene halloween_party with dissolve
    narrator "Amelia recalls the effort they put into their costumes, making each Halloween special."
    a "We spent weeks planning our costumes. It was our favorite holiday."
    show ella_halloween with dissolve
    e "What do you think of my witch costume, Amelia?"
    a "It's amazing, Ella! Look at my vampire outfit!"
    narrator "Their creativity and enthusiasm made each Halloween memorable, full of fun and adventure."
    return

label ella_halloween_treating:
    scene trick_or_treating with dissolve
    narrator "Amelia remembers the thrill of trick-or-treating, going door to door with Ella."
    a "We collected so much candy that night. It was like a treasure hunt."
    show ella_halloween with dissolve
    e "Look at all this candy, Amelia! We're going to have a feast!"
    a "We sure are! Let's hit a few more houses."
    narrator "The excitement of trick-or-treating, the laughter, and the sugar rushes created unforgettable memories."
    return

label ella_halloween_haunted:
    scene haunted_house with dissolve
    narrator "Amelia's mind goes to the haunted house they visited, a mix of fear and exhilaration."
    a "The haunted house was terrifying, but we faced our fears together."
    show ella_halloween with dissolve
    e "I'm scared, Amelia. Hold my hand."
    a "Don't worry, Ella. We'll get through it together."
    narrator "Facing their fears in the haunted house strengthened their bond and created a thrilling experience they would never forget."
    return

label dad_photos:
    menu:
        "Choose a memory with Dad":
            "Fishing Trip":
                jump dad_fishing
            "Cooking Together":
                jump dad_cooking
            "Road Trip":
                jump dad_road_trip

label dad_fishing:
    show photo_fishing with dissolve
    narrator "Amelia picks up a photo of her and her dad on a fishing trip, both of them holding up their catches with proud smiles."
    a "That fishing trip was one of the best days we ever had together."

    menu:
        "Amelia's thoughts":
            "Remembering the early morning":
                jump dad_fishing_morning
            "Thinking about the big catch":
                jump dad_fishing_catch
            "Recalling the quiet moments":
                jump dad_fishing_quiet

label dad_fishing_morning:
    scene fishing_lake with dissolve
    narrator "Amelia remembers the early morning mist over the lake, the stillness broken only by the occasional splash of a fish."
    a "We woke up before dawn to get to the lake. The air was so crisp and fresh."
    show dad_fishing with dissolve
    dad "Look at that sunrise, Amelia. Isn't it beautiful?"
    a "It's amazing, Dad. I'm glad we came early."
    narrator "The tranquility of the early morning and the shared experience of watching the sunrise created a lasting memory."
    return

label dad_fishing_catch:
    scene fishing_lake with dissolve
    narrator "Amelia recalls the excitement of catching the biggest fish of the day."
    a "I couldn't believe it when I felt that tug on the line."
    show dad_fishing with dissolve
    dad "Reel it in, Amelia! You've got a big one!"
    a "I'm trying, Dad! It's really strong!"
    narrator "The thrill of the catch and the sense of accomplishment bonded them even closer."
    return

label dad_fishing_quiet:
    scene fishing_lake with dissolve
    narrator "Amelia's thoughts drift to the quiet moments, just sitting by the lake with her dad."
    a "We didn't need to talk much. Just being there together was enough."
    show dad_fishing with dissolve
    dad "Sometimes, the best part of fishing is just enjoying the peace and quiet."
    a "I agree, Dad. It's really nice out here."
    narrator "The peaceful moments by the lake fostered a deep sense of connection and mutual understanding."
    return

label dad_cooking:
    show photo_cooking with dissolve
    narrator "Amelia picks up a photo of her and her dad in the kitchen, both of them covered in flour and laughing."
    a "Cooking with Dad was always an adventure."

    menu:
        "Amelia's thoughts":
            "Remembering the first recipe":
                jump dad_cooking_recipe
            "Thinking about the kitchen mess":
                jump dad_cooking_mess
            "Recalling the taste tests":
                jump dad_cooking_taste

label dad_cooking_recipe:
    scene kitchen with dissolve
    narrator "Amelia recalls the first recipe they tried together, a complicated cake that required careful measuring and mixing."
    a "Dad was always so patient, explaining every step."
    show dad_cooking with dissolve
    dad "Okay, Amelia, now we add the flour slowly. It's all about getting the right texture."
    a "Got it, Dad. This is going to be the best cake ever!"
    narrator "The process of learning and creating something together was incredibly rewarding."
    return

label dad_cooking_mess:
    scene kitchen with dissolve
    narrator "Amelia remembers the mess they made, flour everywhere and laughter filling the room."
    a "We ended up making a huge mess, but it was so much fun."
    show dad_cooking with dissolve
    dad "Who knew baking could be so messy? But look at us, we're having a blast!"
    a "Definitely! This is the best kind of chaos."
    narrator "The joy of the experience was in the chaos and the shared laughter."
    return

label dad_cooking_taste:
    scene kitchen with dissolve
    narrator "Amelia's thoughts go to the taste tests, trying different ingredients and laughing at their mistakes."
    a "Dad always made sure we tasted everything, even the mistakes."
    show dad_cooking with dissolve
    dad "Oops, too much salt. But hey, that's how we learn, right?"
    a "Yeah, let's try it again. We'll get it perfect this time."
    narrator "The fun was in the experimentation and the journey of getting it right together."
    return

label dad_road_trip:
    show photo_road_trip with dissolve
    narrator "Amelia picks up a photo of her and her dad in front of their car, ready for a road trip."
    a "Road trips with Dad were always the best."

    menu:
        "Amelia's thoughts":
            "Remembering the scenic routes":
                jump dad_road_trip_routes
            "Thinking about the sing-alongs":
                jump dad_road_trip_sing
            "Recalling the roadside stops":
                jump dad_road_trip_stops

label dad_road_trip_routes:
    scene road_trip with dissolve
    narrator "Amelia remembers the scenic routes they took, driving through beautiful landscapes."
    a "We saw so many amazing places. The journey was just as exciting as the destination."
    show dad_road_trip with dissolve
    dad "Look at that view, Amelia. Isn't it incredible?"
    a "It's breathtaking, Dad. I'm glad we took this route."
    narrator "The beauty of the landscapes and the shared awe created unforgettable memories."
    return

label dad_road_trip_sing:
    scene road_trip with dissolve
    narrator "Amelia recalls the sing-alongs, their voices filling the car as they sang their favorite songs."
    a "We sang so many songs. It was like our own little concert."
    show dad_road_trip with dissolve
    dad "Alright, Amelia, your turn to pick the song. What's next?"
    a "How about something upbeat? Let's keep the energy high!"
    narrator "The joy of singing together made the hours on the road fly by."
    return

label dad_road_trip_stops:
    scene road_trip with dissolve
    narrator "Amelia's mind goes to the roadside stops, each one an adventure in itself."
    a "We found the most interesting places when we stopped along the way."
    show dad_road_trip with dissolve
    dad "Look, Amelia, a little diner! Let's grab some food and check it out."
    a "Great idea, Dad. I love these unexpected stops."
    narrator "The spontaneity and exploration of roadside stops added an element of surprise and delight to their trips."
    return

label lily_photos:
    menu:
        "Choose a memory with Lily":
            "Birthday Party":
                jump lily_birthday
            "Beach Day":
                jump lily_beach
            "School Play":
                jump lily_school_play

label lily_birthday:
    show photo_birthday with dissolve
    narrator "Amelia picks up a photo of Lily's birthday party, with both of them smiling and surrounded by colorful decorations."
    a "Lily's birthday parties were always so much fun."

    menu:
        "Amelia's thoughts":
            "Remembering the cake surprise":
                jump lily_birthday_cake
            "Thinking about the games":
                jump lily_birthday_games
            "Recalling the present opening":
                jump lily_birthday_presents

label lily_birthday_cake:
    scene birthday_party with dissolve
    narrator "Amelia remembers the moment they brought out the birthday cake, decorated with Lily's favorite cartoon characters."
    a "Lily was so excited when she saw the cake. Her eyes lit up like fireworks."
    show lily_birthday with dissolve
    lily "Amelia, look! It's my favorite! Thank you so much!"
    a "You're welcome, Lily. I'm so glad you like it."
    narrator "The joy on Lily's face made all the effort worth it."
    return

label lily_birthday_games:
    scene birthday_party with dissolve
    narrator "Amelia recalls the fun games they played, from musical chairs to a treasure hunt."
    a "We had so much fun playing all those games. Lily was always so competitive."
    show lily_birthday with dissolve
    lily "Come on, Amelia! You have to help me find the treasure!"
    a "Alright, let's go! We'll find it together."
    narrator "The laughter and excitement of the games created lasting memories."
    return

label lily_birthday_presents:
    scene birthday_party with dissolve
    narrator "Amelia's thoughts go to the moment Lily opened her presents, each one bringing a new wave of excitement."
    a "Lily's reaction to each present was priceless. She was so grateful and happy."
    show lily_birthday with dissolve
    lily "Oh wow! This is exactly what I wanted! Thank you!"
    a "I'm glad you like it, Lily. You deserve the best."
    narrator "The joy of giving and seeing Lily's happiness made the day unforgettable."
    return

label lily_beach:
    show photo_beach with dissolve
    narrator "Amelia picks up a photo of a sunny beach day with Lily, both of them building a sandcastle."
    a "Our beach days were always filled with fun and laughter."

    menu:
        "Amelia's thoughts":
            "Remembering the sandcastle":
                jump lily_beach_sandcastle
            "Thinking about the waves":
                jump lily_beach_waves
            "Recalling the ice cream":
                jump lily_beach_ice_cream

label lily_beach_sandcastle:
    scene beach_day with dissolve
    narrator "Amelia remembers the time they spent building a grand sandcastle, complete with towers and moats."
    a "We spent hours building that sandcastle. It was a masterpiece."
    show lily_beach with dissolve
    lily "Amelia, look! We did it! It's the best sandcastle ever!"
    a "It sure is, Lily. We make a great team."
    narrator "The sense of accomplishment and teamwork made the day special."
    return

label lily_beach_waves:
    scene beach_day with dissolve
    narrator "Amelia recalls the fun they had playing in the waves, laughing and splashing each other."
    a "We had so much fun jumping over the waves and splashing around."
    show lily_beach with dissolve
    lily "Come on, Amelia! Let's see who can jump the highest wave!"
    a "You're on, Lily! Let's go!"
    narrator "The carefree joy of playing in the waves was infectious."
    return

label lily_beach_ice_cream:
    scene beach_day with dissolve
    narrator "Amelia's thoughts go to the moment they got ice cream from a beach vendor, savoring the cold treat on a hot day."
    a "That ice cream was the perfect way to cool down after playing in the sun."
    show lily_beach with dissolve
    lily "This is the best ice cream ever! Thank you, Amelia!"
    a "You're welcome, Lily. It's the perfect treat for a beach day."
    narrator "The simple pleasure of enjoying ice cream together added to the day's happiness."
    return

label lily_school_play:
    show photo_school_play with dissolve
    narrator "Amelia picks up a photo of Lily dressed up for her school play, with both of them beaming with pride."
    a "Lily was such a star in her school play."

    menu:
        "Amelia's thoughts":
            "Remembering the rehearsal":
                jump lily_school_play_rehearsal
            "Thinking about the performance":
                jump lily_school_play_performance
            "Recalling the applause":
                jump lily_school_play_applause

label lily_school_play_rehearsal:
    scene school_play with dissolve
    narrator "Amelia remembers helping Lily rehearse her lines for the school play, offering encouragement and support."
    a "We practiced her lines so many times. She wanted to get everything perfect."
    show lily_school_play with dissolve
    lily "Amelia, do you think I'm ready?"
    a "You're more than ready, Lily. You're going to be amazing."
    narrator "The dedication and hard work paid off, and their bond grew stronger through the rehearsals."
    return

label lily_school_play_performance:
    scene school_play with dissolve
    narrator "Amelia recalls the excitement of watching Lily perform on stage, delivering her lines with confidence."
    a "Lily was a natural on stage. She remembered every line and delivered them perfectly."
    show lily_school_play with dissolve
    lily "Thank you for helping me, Amelia. I couldn't have done it without you."
    a "You did all the hard work, Lily. I'm so proud of you."
    narrator "The pride and joy of watching Lily shine on stage was a moment to cherish."
    return

label lily_school_play_applause:
    scene school_play with dissolve
    narrator "Amelia's thoughts go to the thunderous applause that followed Lily's performance, the look of pride on her face."
    a "The applause was so loud, and Lily's smile was even brighter."
    show lily_school_play with dissolve
    lily "Did you hear that, Amelia? They loved it!"
    a "Of course they did, Lily. You were fantastic."
    narrator "The overwhelming pride and the joy of seeing Lily's happiness made the evening unforgettable."
    return

label goodbye_letters:
    scene letters_intro with dissolve
    narrator "Amelia sits at her desk, ready to write heartfelt goodbye letters to her loved ones. She takes a deep breath, thinking about what to say."

    menu:
        "Who should Amelia write to first?":
            "Dad":
                jump letter_dad
            "Ella":
                jump letter_ella
            "Lily":
                jump letter_lily

label letter_dad:
    scene letter_dad with dissolve
    narrator "Amelia sits down at her desk, pulling out a fresh sheet of paper. She takes a deep breath and begins to write a heartfelt letter to her dad."

    menu:
        "Select the tone of the letter":
            "Warm and Appreciative":
                $ dad_tone = "warm"
            "Reflective and Emotional":
                $ dad_tone = "reflective"
            "Optimistic and Forward-Looking":
                $ dad_tone = "optimistic"

    if dad_tone == "warm":
        menu:
            "Expressing Gratitude":
                "Thank you for always being there for me.":
                    jump dad_gratitude_warm_1
                "I appreciate all the sacrifices you've made for me.":
                    jump dad_gratitude_warm_2
                "Your support means the world to me.":
                    jump dad_gratitude_warm_3
            "Sharing Memories":
                "I'll always cherish our Sunday breakfasts.":
                    jump dad_memory_warm_1
                "Our fishing trips were the best times of my childhood.":
                    jump dad_memory_warm_2
                "Remember that road trip? It was unforgettable.":
                    jump dad_memory_warm_3
            "Expressing Concerns/Worries":
                "I'm worried about leaving you alone.":
                    jump dad_worry_warm_1
                "I hope you won't miss me too much.":
                    jump dad_worry_warm_2
                "Please take care of yourself while I'm away.":
                    jump dad_worry_warm_3
            "Looking Forward":
                "I'm excited about this new chapter.":
                    jump dad_forward_warm_1
                "I promise to make you proud.":
                    jump dad_forward_warm_2
                "I'll keep in touch and visit as often as I can.":
                    jump dad_forward_warm_3

    if dad_tone == "reflective":
        menu:
            "Expressing Gratitude":
                "Thank you for always being there for me.":
                    jump dad_gratitude_reflective_1
                "I appreciate all the sacrifices you've made for me.":
                    jump dad_gratitude_reflective_2
                "Your support means the world to me.":
                    jump dad_gratitude_reflective_3
            "Sharing Memories":
                "I'll always cherish our Sunday breakfasts.":
                    jump dad_memory_reflective_1
                "Our fishing trips were the best times of my childhood.":
                    jump dad_memory_reflective_2
                "Remember that road trip? It was unforgettable.":
                    jump dad_memory_reflective_3
            "Expressing Concerns/Worries":
                "I'm worried about leaving you alone.":
                    jump dad_worry_reflective_1
                "I hope you won't miss me too much.":
                    jump dad_worry_reflective_2
                "Please take care of yourself while I'm away.":
                    jump dad_worry_reflective_3
            "Looking Forward":
                "I'm excited about this new chapter.":
                    jump dad_forward_reflective_1
                "I promise to make you proud.":
                    jump dad_forward_reflective_2
                "I'll keep in touch and visit as often as I can.":
                    jump dad_forward_reflective_3

    if dad_tone == "optimistic":
        menu:
            "Expressing Gratitude":
                "Thank you for always being there for me.":
                    jump dad_gratitude_optimistic_1
                "I appreciate all the sacrifices you've made for me.":
                    jump dad_gratitude_optimistic_2
                "Your support means the world to me.":
                    jump dad_gratitude_optimistic_3
            "Sharing Memories":
                "I'll always cherish our Sunday breakfasts.":
                    jump dad_memory_optimistic_1
                "Our fishing trips were the best times of my childhood.":
                    jump dad_memory_optimistic_2
                "Remember that road trip? It was unforgettable.":
                    jump dad_memory_optimistic_3
            "Expressing Concerns/Worries":
                "I'm worried about leaving you alone.":
                    jump dad_worry_optimistic_1
                "I hope you won't miss me too much.":
                    jump dad_worry_optimistic_2
                "Please take care of yourself while I'm away.":
                    jump dad_worry_optimistic_3
            "Looking Forward":
                "I'm excited about this new chapter.":
                    jump dad_forward_optimistic_1
                "I promise to make you proud.":
                    jump dad_forward_optimistic_2
                "I'll keep in touch and visit as often as I can.":
                    jump dad_forward_optimistic_3

# Warm and Appreciative Choices
label dad_gratitude_warm_1:
    a "Thank you for always being there for me, Dad. Your unwavering support has been my anchor through every storm."
    jump dad_letter_next

label dad_gratitude_warm_2:
    a "I appreciate all the sacrifices you've made for me. You've given up so much to ensure I had every opportunity."
    jump dad_letter_next

label dad_gratitude_warm_3:
    a "Your support means the world to me. Knowing you're always in my corner gives me the strength to face any challenge."
    jump dad_letter_next

label dad_memory_warm_1:
    a "I'll always cherish our Sunday breakfasts. Those mornings were filled with laughter and love, setting the perfect tone for the week."
    jump dad_letter_next

label dad_memory_warm_2:
    a "Our fishing trips were the best times of my childhood. The quiet moments by the lake, just us and nature, are memories I hold dear."
    jump dad_letter_next

label dad_memory_warm_3:
    a "Remember that road trip? It was unforgettable. The adventure, the music, and the spontaneous stops created memories that will last a lifetime."
    jump dad_letter_next

label dad_worry_warm_1:
    a "I'm worried about leaving you alone. I know you'll be fine, but I can't help but feel a little anxious about it."
    jump dad_letter_next

label dad_worry_warm_2:
    a "I hope you won't miss me too much. I'll miss our daily chats and your comforting presence."
    jump dad_letter_next

label dad_worry_warm_3:
    a "Please take care of yourself while I'm away. Your health and happiness mean everything to me."
    jump dad_letter_next

label dad_forward_warm_1:
    a "I'm excited about this new chapter. It's a big step, but I know it's the right one."
    jump dad_letter_next

label dad_forward_warm_2:
    a "I promise to make you proud. I'll work hard and strive to achieve my dreams, just like you always encouraged me to."
    jump dad_letter_next

label dad_forward_warm_3:
    a "I'll keep in touch and visit as often as I can. Our bond won't be weakened by distance, I promise."
    jump dad_letter_next

# Reflective and Emotional Choices
label dad_gratitude_reflective_1:
    a "Thank you for always being there for me. Your constant presence has been a source of comfort and strength throughout my life."
    jump dad_letter_next

label dad_gratitude_reflective_2:
    a "I appreciate all the sacrifices you've made for me. Your love and dedication have shaped who I am today."
    jump dad_letter_next

label dad_gratitude_reflective_3:
    a "Your support means the world to me. Every time I faced a challenge, knowing you were there gave me the courage to keep going."
    jump dad_letter_next

label dad_memory_reflective_1:
    a "I'll always cherish our Sunday breakfasts. Those moments were more than just meals; they were a time for us to connect and share our lives."
    jump dad_letter_next

label dad_memory_reflective_2:
    a "Our fishing trips were the best times of my childhood. The serenity of the lake and our conversations made those trips special."
    jump dad_letter_next

label dad_memory_reflective_3:
    a "Remember that road trip? It was unforgettable. The sense of adventure and freedom we felt is something I'll always treasure."
    jump dad_letter_next

label dad_worry_reflective_1:
    a "I'm worried about leaving you alone. The thought of you being by yourself makes me anxious, even though I know you're strong."
    jump dad_letter_next

label dad_worry_reflective_2:
    a "I hope you won't miss me too much. I worry that the house will feel empty without our daily interactions."
    jump dad_letter_next

label dad_worry_reflective_3:
    a "Please take care of yourself while I'm away. Your well-being is incredibly important to me, and I want you to be happy."
    jump dad_letter_next

label dad_forward_reflective_1:
    a "I'm excited about this new chapter. It's daunting, but I believe it's an opportunity for growth and new experiences."
    jump dad_letter_next

label dad_forward_reflective_2:
    a "I promise to make you proud. I'll carry the lessons you've taught me and strive to be the best version of myself."
    jump dad_letter_next

label dad_forward_reflective_3:
    a "I'll keep in touch and visit as often as I can. Our relationship is precious to me, and I won't let distance change that."
    jump dad_letter_next

# Optimistic and Forward-Looking Choices
label dad_gratitude_optimistic_1:
    a "Thank you for always being there for me. Your unwavering support has given me the confidence to pursue my dreams."
    jump dad_letter_next

label dad_gratitude_optimistic_2:
    a "I appreciate all the sacrifices you've made for me. Your dedication has been a beacon of hope and motivation for me."
    jump dad_letter_next

label dad_gratitude_optimistic_3:
    a "Your support means the world to me. With you by my side, I feel ready to tackle any challenge that comes my way."
    jump dad_letter_next

label dad_memory_optimistic_1:
    a "I'll always cherish our Sunday breakfasts. Those mornings were filled with joy and laughter, setting a positive tone for the week."
    jump dad_letter_next

label dad_memory_optimistic_2:
    a "Our fishing trips were the best times of my childhood. The peace and adventure we shared are memories I hold dear."
    jump dad_letter_next

label dad_memory_optimistic_3:
    a "Remember that road trip? It was unforgettable. The excitement and spontaneity of those moments will always stay with me."
    jump dad_letter_next

label dad_worry_optimistic_1:
    a "I'm worried about leaving you alone. It's a big step, but I know we can both handle it with strength and positivity."
    jump dad_letter_next

label dad_worry_optimistic_2:
    a "I hope you won't miss me too much. Our bond is strong, and we'll stay connected no matter the distance."
    jump dad_letter_next

label dad_worry_optimistic_3:
    a "Please take care of yourself while I'm away. Your happiness and health are my top priorities, and I want you to thrive."
    jump dad_letter_next

label dad_forward_optimistic_1:
    a "I'm excited about this new chapter. It's a thrilling adventure that I can't wait to embark on."
    jump dad_letter_next

label dad_forward_optimistic_2:
    a "I promise to make you proud. I'll take every opportunity to grow and succeed, inspired by your example."
    jump dad_letter_next

label dad_forward_optimistic_3:
    a "I'll keep in touch and visit as often as I can. Our connection will only grow stronger, no matter where life takes me."
    jump dad_letter_next

label dad_letter_next:
    menu:
        "What should Amelia express next?":
            "Expressing Gratitude" if not dad_gratitude:
                $ dad_gratitude = True
                jump letter_dad
            "Sharing Memories" if not dad_memories:
                $ dad_memories = True
                jump letter_dad
            "Expressing Concerns/Worries" if not dad_worries:
                $ dad_worries = True
                jump letter_dad
            "Looking Forward" if not dad_looking_forward:
                $ dad_looking_forward = True
                jump letter_dad
            "Finish Letter":
                jump letter_dad_finish

label letter_dad_finish:
    narrator "Amelia finishes the letter to her dad with a deep sense of gratitude and love."
    menu:
        "Who should Amelia write to next?":
            "Ella":
                jump letter_ella
            "Lily":
                jump letter_lily


label letter_ella:
    scene letter_ella with dissolve
    narrator "Amelia sits down at her desk, pulling out a fresh sheet of paper. She takes a deep breath and begins to write a heartfelt letter to her best friend, Ella."

    menu:
        "Select the tone of the letter":
            "Warm and Appreciative":
                $ ella_tone = "warm"
            "Reflective and Emotional":
                $ ella_tone = "reflective"
            "Optimistic and Forward-Looking":
                $ ella_tone = "optimistic"

    if ella_tone == "warm":
        menu:
            "Expressing Friendship":
                "You've been my rock through thick and thin.":
                    jump ella_friendship_warm_1
                "I can't imagine life without our daily chats.":
                    jump ella_friendship_warm_2
                "Thank you for always having my back.":
                    jump ella_friendship_warm_3
            "Sharing Memories":
                "Remember the time we got lost in the park?":
                    jump ella_memory_warm_1
                "Our sleepovers were the highlight of my weekends.":
                    jump ella_memory_warm_2
                "I’ll never forget our late-night study sessions.":
                    jump ella_memory_warm_3
            "Expressing Sadness":
                "I'm going to miss you so much.":
                    jump ella_sadness_warm_1
                "It's hard to imagine not seeing you every day.":
                    jump ella_sadness_warm_2
                "I wish we could take this next step together.":
                    jump ella_sadness_warm_3
            "Looking Forward":
                "I can't wait to tell you all about my adventures.":
                    jump ella_forward_warm_1
                "We'll always be best friends, no matter the distance.":
                    jump ella_forward_warm_2
                "I'm excited for our future reunions.":
                    jump ella_forward_warm_3

    if ella_tone == "reflective":
        menu:
            "Expressing Friendship":
                "You've been my rock through thick and thin.":
                    jump ella_friendship_reflective_1
                "I can't imagine life without our daily chats.":
                    jump ella_friendship_reflective_2
                "Thank you for always having my back.":
                    jump ella_friendship_reflective_3
            "Sharing Memories":
                "Remember the time we got lost in the park?":
                    jump ella_memory_reflective_1
                "Our sleepovers were the highlight of my weekends.":
                    jump ella_memory_reflective_2
                "I’ll never forget our late-night study sessions.":
                    jump ella_memory_reflective_3
            "Expressing Sadness":
                "I'm going to miss you so much.":
                    jump ella_sadness_reflective_1
                "It's hard to imagine not seeing you every day.":
                    jump ella_sadness_reflective_2
                "I wish we could take this next step together.":
                    jump ella_sadness_reflective_3
            "Looking Forward":
                "I can't wait to tell you all about my adventures.":
                    jump ella_forward_reflective_1
                "We'll always be best friends, no matter the distance.":
                    jump ella_forward_reflective_2
                "I'm excited for our future reunions.":
                    jump ella_forward_reflective_3

    if ella_tone == "optimistic":
        menu:
            "Expressing Friendship":
                "You've been my rock through thick and thin.":
                    jump ella_friendship_optimistic_1
                "I can't imagine life without our daily chats.":
                    jump ella_friendship_optimistic_2
                "Thank you for always having my back.":
                    jump ella_friendship_optimistic_3
            "Sharing Memories":
                "Remember the time we got lost in the park?":
                    jump ella_memory_optimistic_1
                "Our sleepovers were the highlight of my weekends.":
                    jump ella_memory_optimistic_2
                "I’ll never forget our late-night study sessions.":
                    jump ella_memory_optimistic_3
            "Expressing Sadness":
                "I'm going to miss you so much.":
                    jump ella_sadness_optimistic_1
                "It's hard to imagine not seeing you every day.":
                    jump ella_sadness_optimistic_2
                "I wish we could take this next step together.":
                    jump ella_sadness_optimistic_3
            "Looking Forward":
                "I can't wait to tell you all about my adventures.":
                    jump ella_forward_optimistic_1
                "We'll always be best friends, no matter the distance.":
                    jump ella_forward_optimistic_2
                "I'm excited for our future reunions.":
                    jump ella_forward_optimistic_3

# Warm and Appreciative Choices
label ella_friendship_warm_1:
    a "You've been my rock through thick and thin, Ella. Your unwavering support has meant the world to me."
    jump ella_letter_next

label ella_friendship_warm_2:
    a "I can't imagine life without our daily chats. They've been a source of comfort and joy for me."
    jump ella_letter_next

label ella_friendship_warm_3:
    a "Thank you for always having my back. Your friendship is a treasure I'll always cherish."
    jump ella_letter_next

label ella_memory_warm_1:
    a "Remember the time we got lost in the park? It was scary, but we made it through together, laughing about it later."
    jump ella_letter_next

label ella_memory_warm_2:
    a "Our sleepovers were the highlight of my weekends. The late-night talks, the movies, the fun we had—those memories will always make me smile."
    jump ella_letter_next

label ella_memory_warm_3:
    a "I’ll never forget our late-night study sessions. We managed to make even the toughest subjects enjoyable."
    jump ella_letter_next

label ella_sadness_warm_1:
    a "I'm going to miss you so much, Ella. It's hard to think about not seeing you every day."
    jump ella_letter_next

label ella_sadness_warm_2:
    a "It's hard to imagine not seeing you every day. You've been such an important part of my life."
    jump ella_letter_next

label ella_sadness_warm_3:
    a "I wish we could take this next step together. I'm so grateful for your friendship and the support you've given me."
    jump ella_letter_next

label ella_forward_warm_1:
    a "I can't wait to tell you all about my adventures. We'll have so much to catch up on when we see each other again."
    jump ella_letter_next

label ella_forward_warm_2:
    a "We'll always be best friends, no matter the distance. Our bond is strong and will withstand anything."
    jump ella_letter_next

label ella_forward_warm_3:
    a "I'm excited for our future reunions. They'll be filled with stories, laughter, and the joy of seeing each other again."
    jump ella_letter_next

# Reflective and Emotional Choices
label ella_friendship_reflective_1:
    a "You've been my rock through thick and thin, Ella. Your unwavering support has been a source of comfort and strength for me."
    jump ella_letter_next

label ella_friendship_reflective_2:
    a "I can't imagine life without our daily chats. They’ve been a lifeline for me during tough times."
    jump ella_letter_next

label ella_friendship_reflective_3:
    a "Thank you for always having my back. Your friendship is a gift I'll always treasure."
    jump ella_letter_next

label ella_memory_reflective_1:
    a "Remember the time we got lost in the park? It was a moment of fear turned into laughter and bonding. I'll never forget it."
    jump ella_letter_next

label ella_memory_reflective_2:
    a "Our sleepovers were the highlight of my weekends. The stories we shared, the dreams we dreamed—those nights were magical."
    jump ella_letter_next

label ella_memory_reflective_3:
    a "I’ll never forget our late-night study sessions. We turned stress into fun, and those nights became precious memories."
    jump ella_letter_next

label ella_sadness_reflective_1:
    a "I'm going to miss you so much, Ella. The thought of not having you close by is really hard to bear."
    jump ella_letter_next

label ella_sadness_reflective_2:
    a "It's hard to imagine not seeing you every day. You've been my confidante, my sister in spirit."
    jump ella_letter_next

label ella_sadness_reflective_3:
    a "I wish we could take this next step together. Your friendship has been my anchor, and I'll miss you deeply."
    jump ella_letter_next

label ella_forward_reflective_1:
    a "I can't wait to tell you all about my adventures. Our conversations will be filled with new experiences and discoveries."
    jump ella_letter_next

label ella_forward_reflective_2:
    a "We'll always be best friends, no matter the distance. Our bond is unbreakable and will only grow stronger."
    jump ella_letter_next

label ella_forward_reflective_3:
    a "I'm excited for our future reunions. They'll be filled with love, laughter, and the joy of reconnecting."
    jump ella_letter_next

# Optimistic and Forward-Looking Choices
label ella_friendship_optimistic_1:
    a "You've been my rock through thick and thin, Ella. Your unwavering support has given me the courage to pursue my dreams."
    jump ella_letter_next

label ella_friendship_optimistic_2:
    a "I can't imagine life without our daily chats. They've been a constant source of joy and motivation for me."
    jump ella_letter_next

label ella_friendship_optimistic_3:
    a "Thank you for always having my back. Your friendship is a treasure that fills my life with happiness."
    jump ella_letter_next

label ella_memory_optimistic_1:
    a "Remember the time we got lost in the park? It was an adventure that brought us closer and filled our hearts with laughter."
    jump ella_letter_next

label ella_memory_optimistic_2:
    a "Our sleepovers were the highlight of my weekends. The fun we had, the secrets we shared—those memories are a treasure."
    jump ella_letter_next

label ella_memory_optimistic_3:
    a "I’ll never forget our late-night study sessions. We turned stress into success and made the best of every moment."
    jump ella_letter_next

label ella_sadness_optimistic_1:
    a "I'm going to miss you so much, Ella. But I know our friendship will keep us connected, no matter where we are."
    jump ella_letter_next

label ella_sadness_optimistic_2:
    a "It's hard to imagine not seeing you every day. But our bond is strong, and we'll stay close despite the distance."
    jump ella_letter_next

label ella_sadness_optimistic_3:
    a "I wish we could take this next step together. But I know we'll always be there for each other, supporting and cheering on from afar."
    jump ella_letter_next

label ella_forward_optimistic_1:
    a "I can't wait to tell you all about my adventures. We'll have so many exciting stories to share."
    jump ella_letter_next

label ella_forward_optimistic_2:
    a "We'll always be best friends, no matter the distance. Our bond will continue to grow stronger with each passing day."
    jump ella_letter_next

label ella_forward_optimistic_3:
    a "I'm excited for our future reunions. They'll be filled with new experiences, laughter, and the joy of seeing each other again."
    jump ella_letter_next

label ella_letter_next:
    menu:
        "What should Amelia express next?":
            "Expressing Friendship" if not ella_gratitude:
                $ ella_gratitude = True
                jump letter_ella
            "Sharing Memories" if not ella_memories:
                $ ella_memories = True
                jump letter_ella
            "Expressing Sadness" if not ella_sadness:
                $ ella_sadness = True
                jump letter_ella
            "Looking Forward" if not ella_forward:
                $ ella_forward = True
                jump letter_ella
            "Finish Letter":
                jump letter_ella_finish

label letter_ella_finish:
    narrator "Amelia finishes the letter to Ella with a mix of gratitude, love, and optimism."
    menu:
        "Who should Amelia write to next?":
            "Dad":
                jump letter_dad
            "Lily":
                jump letter_lily

label letter_lily:
    scene letter_lily with dissolve
    narrator "Amelia sits down at her desk again, this time to write a heartfelt letter to her younger cousin, Lily. She thinks about the best way to express her feelings and memories."

    menu:
        "Select the tone of the letter":
            "Loving and Supportive":
                $ lily_tone = "loving"
            "Encouraging and Inspirational":
                $ lily_tone = "encouraging"
            "Playful and Nostalgic":
                $ lily_tone = "playful"

    if lily_tone == "loving":
        menu:
            "Expressing Love":
                "You're the best little cousin anyone could ask for.":
                    jump lily_love_loving_1
                "I love you so much, Lily.":
                    jump lily_love_loving_2
                "You always brighten my day.":
                    jump lily_love_loving_3
            "Sharing Encouragement":
                "Keep being the amazing person you are.":
                    jump lily_encouragement_loving_1
                "Don’t forget to always chase your dreams.":
                    jump lily_encouragement_loving_2
                "You can achieve anything you set your mind to.":
                    jump lily_encouragement_loving_3
            "Sharing Memories":
                "Our beach days were the best.":
                    jump lily_memory_loving_1
                "I loved watching your school plays.":
                    jump lily_memory_loving_2
                "Your birthday parties were so much fun.":
                    jump lily_memory_loving_3
            "Looking Forward":
                "I can't wait to hear about all your adventures.":
                    jump lily_forward_loving_1
                "We'll have so much to talk about when I come back.":
                    jump lily_forward_loving_2
                "I promise to visit and bring you lots of stories.":
                    jump lily_forward_loving_3

    if lily_tone == "encouraging":
        menu:
            "Expressing Love":
                "You're the best little cousin anyone could ask for.":
                    jump lily_love_encouraging_1
                "I love you so much, Lily.":
                    jump lily_love_encouraging_2
                "You always brighten my day.":
                    jump lily_love_encouraging_3
            "Sharing Encouragement":
                "Keep being the amazing person you are.":
                    jump lily_encouragement_encouraging_1
                "Don’t forget to always chase your dreams.":
                    jump lily_encouragement_encouraging_2
                "You can achieve anything you set your mind to.":
                    jump lily_encouragement_encouraging_3
            "Sharing Memories":
                "Our beach days were the best.":
                    jump lily_memory_encouraging_1
                "I loved watching your school plays.":
                    jump lily_memory_encouraging_2
                "Your birthday parties were so much fun.":
                    jump lily_memory_encouraging_3
            "Looking Forward":
                "I can't wait to hear about all your adventures.":
                    jump lily_forward_encouraging_1
                "We'll have so much to talk about when I come back.":
                    jump lily_forward_encouraging_2
                "I promise to visit and bring you lots of stories.":
                    jump lily_forward_encouraging_3

    if lily_tone == "playful":
        menu:
            "Expressing Love":
                "You're the best little cousin anyone could ask for.":
                    jump lily_love_playful_1
                "I love you so much, Lily.":
                    jump lily_love_playful_2
                "You always brighten my day.":
                    jump lily_love_playful_3
            "Sharing Encouragement":
                "Keep being the amazing person you are.":
                    jump lily_encouragement_playful_1
                "Don’t forget to always chase your dreams.":
                    jump lily_encouragement_playful_2
                "You can achieve anything you set your mind to.":
                    jump lily_encouragement_playful_3
            "Sharing Memories":
                "Our beach days were the best.":
                    jump lily_memory_playful_1
                "I loved watching your school plays.":
                    jump lily_memory_playful_2
                "Your birthday parties were so much fun.":
                    jump lily_memory_playful_3
            "Looking Forward":
                "I can't wait to hear about all your adventures.":
                    jump lily_forward_playful_1
                "We'll have so much to talk about when I come back.":
                    jump lily_forward_playful_2
                "I promise to visit and bring you lots of stories.":
                    jump lily_forward_playful_3

# Loving and Supportive Choices
label lily_love_loving_1:
    a "You're the best little cousin anyone could ask for, Lily. You bring so much joy into my life."
    jump lily_letter_next

label lily_love_loving_2:
    a "I love you so much, Lily. Your smile and laughter are the highlights of my day."
    jump lily_letter_next

label lily_love_loving_3:
    a "You always brighten my day, Lily. Your energy and enthusiasm are contagious."
    jump lily_letter_next

label lily_encouragement_loving_1:
    a "Keep being the amazing person you are, Lily. Your kindness and courage inspire me every day."
    jump lily_letter_next

label lily_encouragement_loving_2:
    a "Don’t forget to always chase your dreams. You're capable of achieving anything you set your mind to."
    jump lily_letter_next

label lily_encouragement_loving_3:
    a "You can achieve anything you set your mind to, Lily. I believe in you with all my heart."
    jump lily_letter_next

label lily_memory_loving_1:
    a "Our beach days were the best. Building sandcastles, swimming in the sea, and eating ice cream—it was perfect."
    jump lily_letter_next

label lily_memory_loving_2:
    a "I loved watching your school plays. You were always the star, and I was so proud of you."
    jump lily_letter_next

label lily_memory_loving_3:
    a "Your birthday parties were so much fun. The games, the cake, and the laughter—we always had a blast."
    jump lily_letter_next

label lily_forward_loving_1:
    a "I can't wait to hear about all your adventures. You'll have so many stories to tell me."
    jump lily_letter_next

label lily_forward_loving_2:
    a "We'll have so much to talk about when I come back. I'm looking forward to our long chats."
    jump lily_letter_next

label lily_forward_loving_3:
    a "I promise to visit and bring you lots of stories. We'll make even more amazing memories together."
    jump lily_letter_next

# Encouraging and Inspirational Choices
label lily_love_encouraging_1:
    a "You're the best little cousin anyone could ask for, Lily. Your spirit and determination are truly inspiring."
    jump lily_letter_next

label lily_love_encouraging_2:
    a "I love you so much, Lily. Your kindness and bravery never cease to amaze me."
    jump lily_letter_next

label lily_love_encouraging_3:
    a "You always brighten my day, Lily. Your positive attitude is something I admire greatly."
    jump lily_letter_next

label lily_encouragement_encouraging_1:
    a "Keep being the amazing person you are, Lily. You have the potential to do great things."
    jump lily_letter_next

label lily_encouragement_encouraging_2:
    a "Don’t forget to always chase your dreams. Your future is as bright as you make it."
    jump lily_letter_next

label lily_encouragement_encouraging_3:
    a "You can achieve anything you set your mind to, Lily. Remember, the sky's the limit."
    jump lily_letter_next

label lily_memory_encouraging_1:
    a "Our beach days were the best. Those moments of joy and freedom are some of my favorite memories."
    jump lily_letter_next

label lily_memory_encouraging_2:
    a "I loved watching your school plays. You always brought the characters to life with your talent."
    jump lily_letter_next

label lily_memory_encouraging_3:
    a "Your birthday parties were so much fun. Celebrating with you was always a highlight."
    jump lily_letter_next

label lily_forward_encouraging_1:
    a "I can't wait to hear about all your adventures. You'll have so many exciting experiences to share."
    jump lily_letter_next

label lily_forward_encouraging_2:
    a "We'll have so much to talk about when I come back. I'm eager to hear about everything you'll do."
    jump lily_letter_next

label lily_forward_encouraging_3:
    a "I promise to visit and bring you lots of stories. Our bond will only grow stronger with time."
    jump lily_letter_next

# Playful and Nostalgic Choices
label lily_love_playful_1:
    a "You're the best little cousin anyone could ask for, Lily. Your playful spirit always brings a smile to my face."
    jump lily_letter_next

label lily_love_playful_2:
    a "I love you so much, Lily. Your sense of adventure makes every day an exciting journey."
    jump lily_letter_next

label lily_love_playful_3:
    a "You always brighten my day, Lily. Your laughter is the sweetest sound in the world."
    jump lily_letter_next

label lily_encouragement_playful_1:
    a "Keep being the amazing person you are, Lily. Your creativity and enthusiasm will take you far."
    jump lily_letter_next

label lily_encouragement_playful_2:
    a "Don’t forget to always chase your dreams. Your imagination is your greatest strength."
    jump lily_letter_next

label lily_encouragement_playful_3:
    a "You can achieve anything you set your mind to, Lily. Your determination is unmatched."
    jump lily_letter_next

label lily_memory_playful_1:
    a "Our beach days were the best. We had so much fun building sandcastles and splashing in the waves."
    jump lily_letter_next

label lily_memory_playful_2:
    a "I loved watching your school plays. You always made the audience laugh and cheer."
    jump lily_letter_next

label lily_memory_playful_3:
    a "Your birthday parties were so much fun. We played games, ate cake, and made the best memories."
    jump lily_letter_next

label lily_forward_playful_1:
    a "I can't wait to hear about all your adventures. You'll have so many fun stories to tell."
    jump lily_letter_next

label lily_forward_playful_2:
    a "We'll have so much to talk about when I come back. I'm looking forward to our endless conversations."
    jump lily_letter_next

label lily_forward_playful_3:
    a "I promise to visit and bring you lots of stories. We'll create even more amazing memories together."
    jump lily_letter_next

label lily_letter_next:
    menu:
        "What should Amelia express next?":
            "Expressing Love" if not lily_gratitude:
                $ lily_gratitude = True
                jump letter_lily
            "Sharing Encouragement" if not lily_encouragement:
                $ lily_encouragement = True
                jump letter_lily
            "Sharing Memories" if not lily_memories:
                $ lily_memories = True
                jump letter_lily
            "Looking Forward" if not lily_forward:
                $ lily_forward = True
                jump letter_lily
            "Finish Letter":
                jump letter_lily_finish

label letter_lily_finish:
    narrator "Amelia finishes the letter to Lily with a mix of love, encouragement, and nostalgia."
    menu:
        "Who should Amelia write to next?":
            "Dad":
                jump letter_dad
            "Ella":
                jump letter_ella

label therapeutic_packing:

    # Introduction to the packing activity
    narrator "With all her standard items packed, Amelia now faces the task of deciding which keepsakes and books to bring with her to Plymouth University. These items hold deep personal significance and will provide comfort and inspiration in her new journey."

    # Keepsakes selection
    menu:
        "Choose a Family Keepsake to pack":
            "Mom's Locket":
                $ keepsake_family = "Mom's Locket"
                a "Mom's locket... It always makes me feel close to her."
                narrator "Amelia remembers the day her mom gave her the locket. It was her tenth birthday, and they were sitting in the garden, the sun shining brightly. Her mom told her the locket had been passed down through generations, and now it was her turn to keep it. Every time she holds the locket, she feels her mom's love and wisdom guiding her."
                jump choose_friendship_keepsake

            "Dad's Old Compass":
                $ keepsake_family = "Dad's Old Compass"
                a "Dad's old compass... It always pointed me in the right direction."
                narrator "Amelia remembers the first time her dad showed her the compass. They were on a hiking trip, lost in the woods, but her dad remained calm, using the compass to find their way back. The compass has always been a symbol of his guidance and steady hand, something she knows she’ll need in her new journey."
                jump choose_friendship_keepsake

            "Family Photo Album":
                $ keepsake_family = "Family Photo Album"
                a "The family photo album... So many memories."
                narrator "Flipping through the album, Amelia sees pictures from family holidays, birthday parties, and quiet Sunday afternoons. Each photo tells a story, a moment of joy and love. Taking the album means carrying these moments with her, a reminder that she is never alone."
                jump choose_friendship_keepsake

label choose_friendship_keepsake:

    menu:
        "Choose a Friendship Keepsake to pack":
            "Friendship Bracelet":
                $ keepsake_friendship = "Friendship Bracelet"
                a "The friendship bracelet from Ella... We've been through so much together."
                narrator "Amelia remembers the summer camp where Ella made the bracelet. They were inseparable, sharing secrets and dreams. The bracelet represents their unbreakable bond, a tangible piece of their friendship she can wear and feel Ella’s presence with her."
                jump choose_personal_keepsake

            "Signed Concert Ticket":
                $ keepsake_friendship = "Signed Concert Ticket"
                a "The signed concert ticket... That night was unforgettable."
                narrator "The concert was a night to remember. They sang, danced, and felt the music in their souls. The ticket is more than just a stub; it’s a reminder of the joy and freedom of that night, a piece of her high school memories she wants to carry forward."
                jump choose_personal_keepsake

            "Handwritten Notes":
                $ keepsake_friendship = "Handwritten Notes"
                a "A collection of handwritten notes from my friends... Their words always cheer me up."
                narrator "Each note and letter is a testament to the friendships she’s built. Encouraging words, inside jokes, and heartfelt messages fill the pages. Taking them means carrying her friends' support with her, a source of strength for when she feels alone."
                jump choose_personal_keepsake

label choose_personal_keepsake:

    menu:
        "Choose a Personal Keepsake to pack":
            "Childhood Stuffed Animal":
                $ keepsake_personal = "Childhood Stuffed Animal"
                a "My childhood stuffed animal... It always comforts me."
                narrator "The stuffed animal, a worn-out bunny, has been her companion through thick and thin. It’s a symbol of comfort and security, a piece of her childhood she’s not ready to part with. Taking it with her means bringing a piece of home to her new life."
                jump choose_first_book

            "Travel Souvenirs":
                $ keepsake_personal = "Travel Souvenirs"
                a "Some travel souvenirs... They remind me of happy travels."
                narrator "Each souvenir tells a story of a different place and a different adventure. A seashell from the beach, a miniature Eiffel Tower from Paris, a tiny carved elephant from India. They are tokens of her family’s love for travel and exploration, something she wants to keep close."
                jump choose_first_book

            "Journal":
                $ keepsake_personal = "Journal"
                a "My personal journal... I want to continue writing."
                narrator "The journal is a testament to her thoughts, dreams, and fears. Every page filled with her handwriting is a piece of her soul. Taking it with her means she can continue this journey of self-discovery, chronicling her new experiences."
                jump choose_first_book

# Books selection
label choose_first_book:

    menu:
        "Choose the first book to pack":

            "Introduction to Psychology":
                $ first_book = "Introduction to Psychology"
                a "This book will be essential for my studies. It covers all the basics and will help me understand the fundamentals of psychology."
                narrator "Amelia feels a sense of determination as she reads the back cover. The topics covered remind her of the initial curiosity that led her to pursue psychology. She thinks about how understanding these basics will be crucial as she builds her knowledge."
                jump choose_second_book

            "Theories of Personality":
                $ first_book = "Theories of Personality"
                a "This book will help me understand different theories of personality. It’s fascinating to think about what makes people who they are."
                narrator "As she reads the description, Amelia is reminded of her own quest for self-understanding. Theories of personality intrigue her, and she’s excited to delve into the complexities of human behavior and personality."
                jump choose_second_book

            "Cognitive Behavioral Therapy for Dummies":
                $ first_book = "Cognitive Behavioral Therapy for Dummies"
                a "Cognitive Behavioral Therapy is a key area in psychology. This book could be very useful for learning practical techniques."
                narrator "Reading the back cover, Amelia is reminded of how CBT can help in dealing with various mental health issues. She feels a sense of purpose in learning these techniques, thinking about how they could be applied to help others."
                jump choose_second_book

            "Mindfulness and You":
                $ first_book = "Mindfulness and You"
                a "Mindfulness practices could really help me manage stress, especially in a new environment."
                narrator "Amelia recalls how mindfulness exercises helped her during stressful times in high school. She feels that this book could provide her with the tools to stay calm and focused amidst the challenges of university life."
                jump choose_second_book

            "The Power of Now":
                $ first_book = "The Power of Now"
                a "This book could be really inspiring. It’s about finding peace in the present moment."
                narrator "As she reads the back cover, Amelia thinks about how often she worries about the future or dwells on the past. She feels that this book could help her live more fully in the present, something she aspires to do."
                jump choose_second_book

            "Pride and Prejudice":
                $ first_book = "Pride and Prejudice"
                a "This classic always brings me comfort. It’s like an old friend."
                narrator "Amelia thinks about the countless times she has read and re-read this novel. It’s a source of comfort and familiarity, a touchstone that makes her feel at home no matter where she is."
                jump choose_second_book

            "1984":
                $ first_book = "1984"
                a "This book is so thought-provoking. It makes you think about society and individual freedom."
                narrator "Amelia reflects on the powerful themes of the novel. It challenges her to think critically about the world around her, and she feels it will be a good companion for late-night reflections."
                jump choose_second_book

            "Meditations by Marcus Aurelius":
                $ first_book = "Meditations by Marcus Aurelius"
                a "Stoic philosophy has always fascinated me. This book could offer some deep insights."
                narrator "Amelia thinks about how the principles of Stoicism could help her maintain emotional balance and resilience. The teachings of Marcus Aurelius might provide her with the strength to face any challenge."
                jump choose_second_book

            "The Tao of Pooh":
                $ first_book = "The Tao of Pooh"
                a "This book is such a delightful blend of philosophy and fun. It could be a comforting read."
                narrator "Amelia smiles as she reads the description. The simplicity and wisdom of Pooh Bear’s adventures always bring her joy. It feels like the perfect book to keep her grounded and happy."
                jump choose_second_book

label choose_second_book:

    menu:
        "Choose the second book to pack":

            "Introduction to Psychology":
                $ second_book = "Introduction to Psychology"
                a "This book will be essential for my studies. It covers all the basics and will help me understand the fundamentals of psychology."
                narrator "Amelia feels a sense of determination as she reads the back cover. The topics covered remind her of the initial curiosity that led her to pursue psychology. She thinks about how understanding these basics will be crucial as she builds her knowledge."
                jump end_packing

            "Theories of Personality":
                $ second_book = "Theories of Personality"
                a "This book will help me understand different theories of personality. It’s fascinating to think about what makes people who they are."
                narrator "As she reads the description, Amelia is reminded of her own quest for self-understanding. Theories of personality intrigue her, and she’s excited to delve into the complexities of human behavior and personality."
                jump end_packing

            "Cognitive Behavioral Therapy for Dummies":
                $ second_book = "Cognitive Behavioral Therapy for Dummies"
                a "Cognitive Behavioral Therapy is a key area in psychology. This book could be very useful for learning practical techniques."
                narrator "Reading the back cover, Amelia is reminded of how CBT can help in dealing with various mental health issues. She feels a sense of purpose in learning these techniques, thinking about how they could be applied to help others."
                jump end_packing

            "Mindfulness and You":
                $ second_book = "Mindfulness and You"
                a "Mindfulness practices could really help me manage stress, especially in a new environment."
                narrator "Amelia recalls how mindfulness exercises helped her during stressful times in high school. She feels that this book could provide her with the tools to stay calm and focused amidst the challenges of university life."
                jump end_packing

            "The Power of Now":
                $ second_book = "The Power of Now"
                a "This book could be really inspiring. It’s about finding peace in the present moment."
                narrator "As she reads the back cover, Amelia thinks about how often she worries about the future or dwells on the past. She feels that this book could help her live more fully in the present, something she aspires to do."
                jump end_packing

            "Pride and Prejudice":
                $ second_book = "Pride and Prejudice"
                a "This classic always brings me comfort. It’s like an old friend."
                narrator "Amelia thinks about the countless times she has read and re-read this novel. It’s a source of comfort and familiarity, a touchstone that makes her feel at home no matter where she is."
                jump end_packing

            "1984":
                $ second_book = "1984"
                a "This book is so thought-provoking. It makes you think about society and individual freedom."
                narrator "Amelia reflects on the powerful themes of the novel. It challenges her to think critically about the world around her, and she feels it will be a good companion for late-night reflections."
                jump end_packing

            "Meditations by Marcus Aurelius":
                $ second_book = "Meditations by Marcus Aurelius"
                a "Stoic philosophy has always fascinated me. This book could offer some deep insights."
                narrator "Amelia thinks about how the principles of Stoicism could help her maintain emotional balance and resilience. The teachings of Marcus Aurelius might provide her with the strength to face any challenge."
                jump end_packing

            "The Tao of Pooh":
                $ second_book = "The Tao of Pooh"
                a "This book is such a delightful blend of philosophy and fun. It could be a comforting read."
                narrator "Amelia smiles as she reads the description. The simplicity and wisdom of Pooh Bear’s adventures always bring her joy. It feels like the perfect book to keep her grounded and happy."
                jump end_packing

label end_packing:
    narrator "Amelia carefully places the keepsakes and books into her suitcase, feeling a sense of comfort and readiness. These items will remind her of home and provide her with strength and inspiration as she embarks on this new journey."

    # Continue to the next part of the chapter
    jump chapter_2_outro

label chapter_2_outro:

    show 2_outro_1 with dissolve
    narrator "With her keepsakes and books carefully packed, Amelia feels a mix of excitement and nervousness. It's time to leave for Plymouth. Ella arrives at her house, ready to help her pack the car."

    show 2_outro_2 with dissolve
    e "Hey, Amelia! Ready for the big move?"
    a "Hey, Ella. Yeah, I think so. Thanks for helping me with all this."
    e "Of course! What are best friends for?"

    show 2_outro_3 with dissolve
    narrator "They spend the next few minutes packing the car. Suitcases, boxes, and a few cherished items are carefully loaded into the trunk."

    show 2_outro_4 with dissolve
    e "Alright, I think that's everything. Let's hit the road!"

    show 2_outro_5 with dissolve
    narrator "They get into the car and start the long drive to Plymouth. The sun is shining, and the road stretches out before them."

    # Initial conversation choices
    menu:
        "What should we talk about?":
            "Future plans":
                $ conversation_topic = "future_plans"
                e "So, Amelia, what are you most excited about at university?"
                a "I think... meeting new people and diving into psychology. What about you, Ella? Any big plans?"

                if random.choice([1, 2, 3, 4, 5]) == 1:
                    e "Actually, I'm thinking about taking a gap year to travel. I want to see the world before diving into work or more studies."
                    a "That sounds amazing! Any places in particular?"
                    e "Europe, for sure. Maybe some parts of Asia too. There's just so much out there to explore."
                    a "I'm sure you'll have an incredible adventure. Just make sure to send me lots of pictures."
                elif random.choice([1, 2, 3, 4, 5]) == 2:
                    e "I've been considering getting into art school. I've always loved painting, and I think it might be time to take it seriously."
                    a "Ella, that's fantastic! Your art is so beautiful. You absolutely should go for it."
                    e "Thanks, Amelia. I just hope I can make a career out of it."
                    a "With your talent, I have no doubt you will."
                elif random.choice([1, 2, 3, 4, 5]) == 3:
                    e "I'm planning to start an internship at a local NGO. I really want to make a difference in the community."
                    a "That's so inspiring, Ella. Helping people and making a real impact. I'm proud of you."
                    e "Thanks, Amelia. I just want to do something meaningful with my time."
                elif random.choice([1, 2, 3, 4, 5]) == 4:
                    e "I think I'll just work for a while, save up some money, and figure things out as I go. No rush, right?"
                    a "That's a smart plan. Taking your time to figure things out can be just as valuable."
                    e "Exactly. And who knows, maybe I'll discover something I'm passionate about along the way."
                else:
                    e "I've been thinking about writing a book. It's always been a dream of mine, and I have some ideas I want to explore."
                    a "Ella, that's incredible! Your stories have always been so captivating. I'd love to read anything you write."
                    e "Thanks, Amelia. It's a bit daunting, but I'm excited about the possibility."

            "Nostalgia about school":
                $ conversation_topic = "nostalgia_school"
                e "Do you remember that time we got lost in the park during a school trip?"
                a "Oh my gosh, yes! We were so scared, but it turned out to be an adventure. We found that little pond with the ducks."
                e "And then we pretended to be explorers discovering new lands."
                a "Those were the days. Simple joys and endless imagination."

            "Favorite memories together":
                $ conversation_topic = "favorite_memories"
                e "What's one of your favorite memories of us together, Amelia?"
                a "Hmm, I think it has to be our late-night study sessions. We were so tired but kept each other going with snacks and silly jokes."
                e "I remember those! We got through so many exams because of our 'study marathons.'"
                a "And the reward was always a big tub of ice cream at the end."
                e "Those moments are precious. I'll always cherish them."

    show 2_outro_6 with dissolve
    narrator "The English countryside rolls by, green fields and quaint villages. Amelia's thoughts drift to her world and home, and the new place she's heading to, filled with unknowns."

    a "I can't believe I'm actually leaving London. It's been my home for so long."
    e "It's a big step, but you're ready for it. And Plymouth isn't the moon, you know. We'll still see each other."
    a "I know, it's just... change is always a bit scary."
    e "True, but it's also exciting. Think of all the new experiences waiting for you."

    show 2_outro_7 with dissolve
    narrator "After a few hours on the road, they decide to make a rest stop halfway. The air is fresh, and the rest area has a small café."

    # Rest stop choices
    menu:
        "What should Amelia eat?":
            "A hearty sandwich":
                a "I think I'll go for a hearty sandwich. Need to keep my energy up."
                e "Good choice! I'll have one too."
                a "Nothing beats a good sandwich on a road trip."
                e "Agreed. It's the perfect road trip food."
            "A light salad":
                a "I'll have a light salad. Don't want to feel too heavy."
                e "Sounds healthy! I'll go for that as well."
                a "Keeping it light and fresh. Nice choice."
                e "Definitely. We need to stay energized."
            "A slice of pie":
                a "I could go for a slice of pie. A little treat for the road."
                e "Yum! I'll join you in that indulgence."
                a "Pie always hits the spot."
                e "Especially on a road trip. It's like a mini celebration."

    show 2_outro_8 with dissolve
    narrator "They sit down with their food, enjoying the break and chatting about various topics."

    # Second conversation choices
    menu:
        "What should they talk about?":
            "Folklore and Cornwall spiritual history":
                e "You know, Cornwall has a rich history of folklore and spiritual tales. We should explore some of that while you're there."
                a "Absolutely! It would be fascinating to learn about the local legends and maybe visit some of those mystical sites."
                e "Imagine all the stories we'll uncover. It sounds like an adventure in itself."
                a "I can't wait to dive into the history and maybe even find some inspiration for my studies."

            "Favorite authors and books from childhood":
                e "Do you remember the books we used to read as kids?"
                a "Of course! I loved 'Harry Potter' and 'The Chronicles of Narnia.' Those stories sparked my imagination."
                e "Same here! We should have a mini book club and read some of those again."
                a "That's a great idea. It would be fun to revisit those stories and see how we feel about them now."
                e "Plus, it would be a nice way to stay connected while you're away."

            "Ella's plans for the future":
                e "I've been thinking a lot about my future too. It's exciting but also a bit scary."
                a "You have so many talents, Ella. Whatever you choose, I know you'll excel."

                if random.choice([1, 2, 3, 4, 5]) == 1:
                    e "Thanks, Amelia. Right now, I'm leaning towards taking a gap year to travel. I want to see the world before diving into anything serious."
                    a "That sounds incredible. You have to visit all the places we've talked about."
                    e "I will! And I'll take lots of pictures to share with you."
                elif random.choice([1, 2, 3, 4, 5]) == 2:
                    e "I've been considering art school. Painting has always been my passion, and I think it's time to take it seriously."
                    a "Ella, that's fantastic! Your art is so beautiful. You absolutely should go for it."
                    e "Thanks, Amelia. I just hope I can make a career out of it."
                    a "With your talent, I have no doubt you will."
                elif random.choice([1, 2, 3, 4, 5]) == 3:
                    e "I'm thinking about an internship at a local NGO. I really want to make a difference in the community."
                    a "That's so inspiring, Ella. Helping people and making a real impact. I'm proud of you."
                    e "Thanks, Amelia. I just want to do something meaningful with my time."
                elif random.choice([1, 2, 3, 4, 5]) == 4:
                    e "I might just work for a while, save up some money, and figure things out as I go. No rush, right?"
                    a "That's a smart plan. Taking your time to figure things out can be just as valuable."
                    e "Exactly. And who knows, maybe I'll discover something I'm passionate about along the way."
                else:
                    e "I've been toying with the idea of writing a book. It's a big dream, but I think I have some stories worth telling."
                    a "Ella, that's incredible! Your stories have always been so captivating. I'd love to read anything you write."
                    e "Thanks, Amelia. It's a bit daunting, but I'm excited about the possibility."

    show 2_outro_9 with dissolve
    narrator "They finish their meal and get back on the road. The drive continues smoothly, with the countryside slowly giving way to the coastal beauty of Plymouth."

    show 2_outro_10 with dissolve
    narrator "Finally, they arrive at the university dorms. Amelia's new home for the next few years."

    a "Well, this is it. My new home."
    e "You're going to do great here, Amelia. I believe in you."

    show 2_outro_11 with dissolve
    narrator "They unload her belongings, and with a heartfelt hug, Ella prepares to leave."

    e "Call me as soon as you're settled, okay?"
    a "I will. Thank you for everything, Ella. You're the best."

    show 2_outro_12 with dissolve
    narrator "As Ella drives away, Amelia stands in front of her dorm, feeling a mix of excitement and nervousness. A new chapter has begun."

    jump chapter_3
