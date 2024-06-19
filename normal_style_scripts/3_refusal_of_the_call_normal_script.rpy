label starting_the_semester:
    stop music fadeout 2.0
    play music sand fadein 2.0 volume 0.3
    show amelia_determined_dorm_full with dissolve
    n "Amelia starts her first semester at Plymouth with a mix of excitement and nervousness, but she's determined to make the most of her university experience."
    hide amelia_determined_dorm_full
    show black
    window hide

    show amelia_thinking_dorm_full
    a "There's so much I want to do and explore here. I should make a list of all the places I want to visit and the things I want to try."

    menu:
        "Focus on academics first":
            $ AA += 1
            hide amelia_thinking_dorm_full
            show black
            window hide

            jump focus_on_academics
        
        "Prioritize social life and exploration":
            $ SI
            jump social_focus

label focus_on_academics:
    scene amelia_library_full with dissolve
    n "Amelia decides to dedicate her first few weeks to getting a strong start academically. She spends long hours in the library, poring over her textbooks and notes."
    
    show amelia at center with fadeIn
    hide amelia with fadeOut

    scene amelia_classroom_full with dissolve
    show amelia at center with fadeIn
    n "In classes, she's an active participant, always ready with a question or a thoughtful comment."

    if AA >= 3:
        hide amelia
        scene black with fadeOut
        show black with fadeIn

        scene professor_impressed_classroom_full with dissolve
        show professor at center with fadeIn
        n "Her professors take note of her engagement and dedication."
        professor "Amelia, your contributions to the class discussions have been excellent. Keep up the great work!"
        a "Thank you, professor. I'm really enjoying delving into the material."
        $ AA += 1
        hide professor
        scene black with fadeOut
        show black with fadeIn

    else:
        hide amelia
        scene black with fadeOut
        show black with fadeIn

        scene professor_neutral_classroom_full with dissolve
        show professor at center with fadeIn
        n "Her professors appreciate her participation, but encourage her to also seek balance in her university life."
        professor "Amelia, it's great to see your enthusiasm for the subject. Remember, university is also about personal growth and exploration. Don't forget to make time for other experiences too."
        a "You're right, professor. I'll keep that in mind."
        hide professor
        scene black with fadeOut
        show black with fadeIn

    jump meet_liz

label prioritize_social_life:
    scene amelia_exploring_barbican_full with dissolve
    n "Eager to immerse herself in all that Plymouth has to offer, Amelia dives into exploring the city and engaging with her peers."
    show amelia at center with fadeIn
    a "There's so much to see and experience. I want to make sure I'm not just stuck in the library all semester."

    hide amelia with fadeOut
    scene black with dissolve

    scene amelia_student_union_full with dissolve
    show amelia at left
    n "Amelia attends a welcome event at the Student Union, bustling with activities and new faces."

    menu:
        "Join the conversation at the trivia club booth":
            $ SI += 1
            show group_students at right
            a "Hey, what's this all about?"
            student "Hi! We're the trivia club. We meet weekly to challenge our minds and have some fun. Interested in joining?"
            a "Absolutely, sounds like a great way to learn random facts and meet people."
            $ SI += 1
            hide group_students
            scene black with fadeOut
            show black with fadeIn

        "Check out the outdoor adventures club":
            $ SD += 1
            show group_students at right
            a "I love being outdoors. What kind of activities do you guys do?"
            student "We do hiking, kayaking, and even some rock climbing. It's a blast and a good escape from studies."
            a "Sign me up! That sounds amazing and a perfect way to keep fit."
            $ SD += 1
            hide group_students
            scene black with fadeOut
            show black with fadeIn

    scene amelia_party_student_union_full with dissolve
    show amelia at center with fadeIn
    n "The night ends with a party where Amelia dances and laughs, making several new friends."
    a "This is exactly what I needed—a break from all the academics!"

    if SI > 3:
        show amelia_friends at sides
        a "I can't believe how many incredible people I've met tonight!"
        n "Amelia finds herself surrounded by a diverse group of students, each sharing stories from different cultures and backgrounds."
        hide amelia_friends
        scene black with fadeOut
        show black with fadeIn
        
    else:
        show amelia_dancing_alone at center
        a "It's good to let loose, but I hope I can connect more deeply with some people soon."
        hide amelia_dancing_alone
        scene black with fadeOut
        show black with fadeIn

    jump meet_liz

label meet_liz:
    scene amelia_returning_dorm_full with dissolve
    show amelia at center with fadeIn
    n "One evening, Amelia returns to her dorm room to find her roommate, Liz, crying."
    
    show liz_crying at right with fadeIn
    a "Liz, what's wrong? Do you want to talk about it?"

    menu:
        "Comfort Liz":
            $ MH += 1
            hide amelia
            show amelia_comforting_liz at left with fadeIn
            l "I'm just feeling so overwhelmed. I don't know if I belong here."
            a "Oh, Liz. I understand. Adjusting to university life can be really tough."
            hide amelia_comforting_liz
            scene black with dissolve

            menu:
                "Share your own struggles":
                    $ SI += 1
                    scene amelia_returning_dorm_full with dissolve
                    show amelia at left
                    show liz at right
                    a "I've been feeling overwhelmed too. It's a big transition, and it's okay to not have it all figured out."
                    l "Really? You always seem so put together."
                    a "Trust me, I have my moments of doubt too. But we're in this together, Liz."
                    l "Thanks, Amelia. It's good to know I'm not alone."
                    hide amelia
                    hide liz
                    scene black with dissolve
                    $ MH += 1

                "Offer practical advice":
                    $ MC += 1
                    scene amelia_returning_dorm_full with dissolve
                    show amelia at left
                    show liz at right
                    a "Have you considered talking to your professors or a counselor? They might be able to offer some guidance and support."
                    l "I hadn't thought of that. I guess I was afraid to admit I was struggling."
                    a "Seeking help is a sign of strength, not weakness. And there are so many resources available to us here."
                    l "You're right. I'll look into making an appointment. Thanks, Amelia."
                    hide amelia
                    hide liz
                    scene black with dissolve

        "Give Liz some space":
            hide amelia
            show amelia_concerned at left with fadeIn
            n "Not wanting to intrude, Amelia decides to give Liz some privacy."
            a "I'll be in the lounge if you need me, Liz. Don't hesitate to reach out."
            n "Amelia leaves the room, feeling a bit uncertain about whether she made the right choice."
            $ MC -= 1
            hide amelia_concerned
            scene black with dissolve

    jump zara_incident

label zara_incident:
    scene amelia_quad_day with dissolve
    show amelia at center with fadeIn
    n "The next day, Amelia witnesses a disturbing incident on the quad. She sees Zara, an international student, being harassed by a group of students."
    hide amelia
    show zara_concerned at right with fadeIn
    show student_2_angry at left with fadeIn
    n "One of the harassers shouts:"
    student_2 "Go back to where you came from! We don't want your kind here."

    menu:
        "Intervene directly":
            $ MC += 1
            hide zara_concerned
            hide student_2_angry
            show amelia_confronting_harassers at center with fadeIn
            a "Hey! Leave her alone! What you're doing is not okay."
            show student_2_angry at left with fadeIn
            student_2 "Mind your own business. This doesn't concern you."
            a "It concerns me when I see someone being discriminated against. Your behavior is unacceptable."
            n "The harassers, not expecting resistance, back off and leave."
            hide student_2_angry
            show zara_grateful at right with fadeIn
            a "Zara, are you alright? I'm so sorry that happened to you."
            zara "I'm shaken, but I'll be okay. Thank you for standing up for me, Amelia."
            a "Of course. No one deserves to be treated like that. If you need anything, I'm here for you."
            $ MC += 1
            $ SI += 1
            hide amelia_confronting_harassers
            hide zara_grateful
            scene black with dissolve

        "Report the incident":
            $ SI += 1
            hide zara_concerned
            hide student_2_angry
            show amelia_taking_photos at center with fadeIn
            n "Amelia discreetly takes photos of the harassers and then approaches Zara."
            hide amelia_taking_photos
            show zara_worried at right with fadeIn
            show amelia_reassuring at left with fadeIn
            a "Zara, I saw what happened. That was awful. I've documented the incident, and I think we should report it to the university authorities."
            zara "I don't know, Amelia. I don't want to cause trouble."
            a "You're not causing trouble. Those students are the ones in the wrong. The university needs to know so they can take appropriate action."
            zara "Okay. Let's do it. Thank you for your support, Amelia."
            n "Together, they go to the student affairs office and file a report."
            $ SI += 1
            $ MH += 1
            hide zara_worried
            hide amelia_reassuring
            scene black with dissolve

    jump sarah_introduction

label sarah_introduction:
    scene amelia_student_lounge_day with dissolve
    show amelia at center with fadeIn
    n "A few days later, Amelia is studying in the student lounge when she notices a girl sitting alone, looking distressed."
    hide amelia
    show sarah_distressed at right with fadeIn

    menu:
        "Approach the girl":
            $ MH += 1
            $ meet_sarah = 1
            hide sarah_distressed
            show amelia_approaching_sarah at center with fadeIn
            a "Hi there. I couldn't help but notice that you seem a bit upset. Is everything okay?"
            n "The girl looks up, surprised that someone is talking to her."
            show sarah_surprised at right with fadeIn
            sarah "Oh, hi. I'm Sarah. It's just been a tough week."
            a "I'm Amelia. I'm sorry to hear that. Do you want to talk about it?"

            menu:
                "Encourage Sarah to open up":
                    $ MH += 1
                    hide amelia_approaching_sarah
                    hide sarah_surprised
                    show sarah_opening_up at right with fadeIn
                    show amelia_listening at left with fadeIn
                    sarah "It's just... I've been struggling with depression for a while now. And being at university, away from my support system, has been really hard."
                    a "Sarah, I'm so glad you shared that with me. Dealing with mental health issues is challenging, especially in a new environment."
                    sarah "I feel so alone sometimes. Like no one understands what I'm going through."
                    a "You're not alone, Sarah. There are people here who care and want to support you, myself included."
                    n "The two continue to talk, forming a bond of understanding and support."
                    $ MH += 1
                    $ SI += 1
                    hide sarah_opening_up
                    hide amelia_listening
                    scene black with dissolve

                "Suggest seeking professional help":
                    $ MC += 1
                    hide amelia_approaching_sarah
                    hide sarah_surprised
                    show amelia_supporting_sarah at center with fadeIn
                    a "Have you thought about talking to a counselor or a mental health professional? They can offer support and guidance."
                    show sarah_considering at right with fadeIn
                    sarah "I've thought about it, but it feels so overwhelming. I don't even know where to start."
                    a "I understand. It can be daunting. But there are resources available, and taking that first step can make a huge difference."
                    sarah "Do you really think it could help?"
                    a "Absolutely. And if you want, I can go with you to your first appointment. You don't have to do it alone."
                    sarah "That... that would mean a lot to me. Thank you, Amelia."
                    $ MC += 1
                    hide amelia_supporting_sarah
                    hide sarah_considering
                    scene black with dissolve

        "Focus on your studies":
            hide sarah_distressed
            show amelia_focusing_studies at center with fadeIn
            n "Amelia considers approaching the girl but decides against it, not wanting to intrude."
            a "(She probably wants to be left alone. I should focus on my own work.)"
            n "She turns back to her books, but can't quite shake the feeling that she might have missed an opportunity to help someone in need."
            hide amelia_focusing_studies
            scene black with dissolve

    jump end_of_chapter_reflection

label end_of_chapter_reflection:
    scene amelia_reflecting_dorm_evening_full with dissolve
    show amelia at center
    n "As the first month comes to a close, Amelia reflects on the experiences she's had so far."

    if AA >= 4 and SI >= 4:
        hide amelia_reflecting_dorm_evening_full
        show black with dissolve
        scene amelia_happy_dorm_full with dissolve
        show amelia at center
        n "She's managed to strike a good balance between her academic pursuits and her social life, and feels she's growing in both areas."
        a "I'm learning so much, both in and out of the classroom. This balance is exactly what I needed."
    elif AA >= 4:
        hide amelia_reflecting_dorm_evening_full
        show black with dissolve
        scene amelia_thinking_dorm_full with dissolve
        show amelia at center
        n "She's excelled academically, but wonders if she should be putting more effort into building friendships and exploring all that university life has to offer."
        a "I'm doing great in my classes, but maybe I should be more proactive in making friends."
    elif SI >= 4:
        hide amelia_reflecting_dorm_evening_full
        show black with dissolve
        scene amelia_social_dorm_full with dissolve
        show amelia at center
        n "She's made a lot of new friends and has had some memorable experiences, but realizes she may need to devote more time to her studies."
        a "I've had such a great time socially, but I need to make sure I'm also focusing on my studies."
    else:
        hide amelia_reflecting_dorm_evening_full
        show black with dissolve
        scene amelia_thoughtful_dorm_full with dissolve
        show amelia at center
        n "She feels she's had a bit of a rocky start, and hasn't quite found her footing yet in either her academic or social life."
        a "It's been a challenging start, but I know I can find my balance."

    hide amelia_thoughtful_dorm_full
    show black with dissolve
    scene amelia_determined_dorm_night_full with dissolve
    show amelia at center
    a "This is just the beginning. I know I have a lot to learn, about myself and the world around me. But I'm ready for whatever comes next."
    n "With that thought, she turns off her light and goes to sleep, eager for the next part of her journey."
    
    hide amelia_determined_dorm_night_full
    show black with dissolve

    jump chapter_3_part_2


label chapter_3_part_2:
    scene amelia_waking_dorm_full with dissolve
    show amelia at center
    n "Amelia wakes up to a sunny morning, feeling refreshed and ready to tackle the day."

    menu:
        "Visit the Marine Biological Association":
            $ AA += 1
            hide amelia_waking_dorm_full
            show black with dissolve
            jump visit_mba

        "Explore the Hoe Park":
            $ SD += 1
            hide amelia_waking_dorm_full
            show black with dissolve
            jump explore_hoe_park

label visit_mba:
    scene amelia_visiting_mba_full with dissolve
    show amelia at center
    n "Amelia decides to visit the Marine Biological Association, curious about the intersection of psychology and environmental science."
    a "Wow, this place is fascinating! I never thought about how the study of marine life could relate to psychology."
    n "She attends a lecture on the behavioral patterns of marine mammals and how they respond to environmental stressors."

    show scientist at right
    scientist "Understanding the psychological impacts of environmental change on marine life can give us insights into the resilience and adaptability of these species."
    a "That's so interesting! It makes me think about how the environment shapes behavior and mental processes in all living beings."

    menu:
        "Ask a question":
            $ AA += 1
            hide amelia_visiting_mba_full
            show black with dissolve
            jump ask_question_mba

        "Take detailed notes":
            $ AA += 1
            hide amelia_visiting_mba_full
            show black with dissolve
            jump take_notes_mba

label ask_question_mba:
    scene amelia_raising_hand_mba_full with dissolve
    show amelia at center
    a "Excuse me, I have a question. How might the principles of behavioral psychology be applied in the context of marine conservation efforts?"
    
    show scientist at right
    scientist "That's an excellent question! By understanding the behavioral patterns and psychological needs of marine species, we can design more effective conservation strategies."
    scientist "For example, if we know that certain species have strong social bonds, we can prioritize protecting their social structures in our conservation plans."
    a "That makes a lot of sense. Thank you for the explanation!"
    
    hide amelia_raising_hand_mba_full
    show black with dissolve
    jump meet_lucas

label take_notes_mba:
    scene amelia_writing_mba_full with dissolve
    show amelia at center
    n "Amelia takes out her notebook and starts jotting down the key points from the lecture."
    a "(The connection between environmental stressors and behavioral changes in marine mammals... The potential applications in conservation efforts...)"
    n "She makes a note to follow up on these ideas and look for relevant research papers."
    
    hide amelia_writing_mba_full
    show black with dissolve
    jump meet_lucas

label explore_hoe_park:
    scene amelia_exploring_hoe_park_full with dissolve
    show amelia at center
    n "Feeling in need of some fresh air and reflection, Amelia heads to Hoe Park."
    a "The view of the Plymouth Sound is breathtaking. It's the perfect place to clear my head."
    n "As she walks along the waterfront, Amelia spots a group of people practicing tai chi."

    menu:
        "Join the tai chi group":
            $ MH += 1
            hide amelia_exploring_hoe_park_full
            show black with dissolve
            jump join_tai_chi

        "Find a quiet spot to journal":
            $ SD += 1
            hide amelia_exploring_hoe_park_full
            show black with dissolve
            jump journal_hoe_park

label join_tai_chi:
    scene amelia_joining_tai_chi_full with dissolve
    show amelia at center
    n "Intrigued, Amelia approaches the group and asks if she can join in."

    show instructor at right
    instructor "Of course! Welcome. Tai chi is a wonderful practice for cultivating mindfulness and inner peace."
    n "The instructor guides Amelia through the basic movements, emphasizing the importance of breath and body awareness."
    a "This is surprisingly challenging, but in a good way. I can feel myself becoming more centered and grounded."
    n "As she synchronizes her movements with the group, Amelia feels a sense of connection and shared presence."

    hide amelia_joining_tai_chi_full
    show black with dissolve
    jump meet_lucas

label journal_hoe_park:
    scene amelia_journaling_hoe_park_full with dissolve
    show amelia at center
    n "Amelia finds a quiet bench overlooking the water and takes out her journal."
    a "(So much has happened in such a short time. The challenges, the growth, the new people I've met...)"
    n "She starts writing, pouring her thoughts and feelings onto the page."
    a "(I'm learning so much about myself and the world around me. It's not always easy, but I know I'm exactly where I'm meant to be.)"
    n "As she writes, Amelia gains clarity and perspective on her journey so far."

    hide amelia_journaling_hoe_park_full
    show black with dissolve
    jump meet_lucas

label meet_lucas:
    scene amelia_lucas_campus_full with dissolve
    show amelia at left
    show lucas at right
    n "On her way back to campus, Amelia runs into Lucas, who seems excited about something."
    lucas "Amelia! Just the person I was hoping to see. I have an idea I want to run by you."

    show amelia_curious_lucas_campus_full
    a "Oh? What's on your mind, Lucas?"
    lucas "I've been thinking about our Jungian psychology class and how we could apply some of those concepts in a practical way."
    lucas "What if we organized a dream interpretation workshop? We could invite students to share their dreams and explore the symbolic meanings together."

    menu:
        "Enthusiastically agree":
            $ AA += 1
            $ SI += 1
            $ lucas_dream_project = 1
            hide amelia_curious_lucas_campus_full
            show black with dissolve
            jump agree_dream_workshop

        "Express reservations":
            hide amelia_curious_lucas_campus_full
            show black with dissolve
            jump reservations_dream_workshop

label agree_dream_workshop:
    scene amelia_excited_lucas_campus_full with dissolve
    show amelia at left
    show lucas at right
    a "Lucas, that's a fantastic idea! It would be such a unique way to engage with the material and learn from each other."
    lucas "Right? And it would be a great opportunity to create a sense of community and shared exploration."
    a "Absolutely. Let's do it! We can talk to the professor and see if they have any guidance or resources for us."
    lucas "Perfect. I'm so glad you're on board, Amelia. With your insights and passion, I know this will be a meaningful experience for everyone involved."

    hide amelia_excited_lucas_campus_full
    show black with dissolve
    jump sarah_conversation

label reservations_dream_workshop:
    stop music fadeout 2.0
    play music drinking_song_for_the_socially_anxious fadein 2.0 volume 0.3

    scene amelia_hesitant_lucas_campus_full with dissolve
    show amelia at left
    show lucas at right
    a "I don't know, Lucas. Dream interpretation can be pretty personal and sensitive. What if people feel uncomfortable sharing?"
    lucas "That's a valid concern. We could make it clear that sharing is optional and create a safe, non-judgmental space."
    a "I suppose you're right. And it could be a powerful way to explore the unconscious mind and support each other's growth."
    lucas "Exactly. But I understand if you're not comfortable with the idea. It's just something I've been excited about."

    menu: 
        "Decide to support the idea":
            $ SI += 1
            $ lucas_dream_project = 1
            hide amelia_hesitant_lucas_campus_full
            show black with dissolve
            jump support_dream_workshop

        "Suggest an alternative":
            hide amelia_hesitant_lucas_campus_full
            show black with dissolve
            jump suggest_alternative_workshop

label support_dream_workshop:
    scene amelia_supportive_lucas_campus_full with dissolve
    show amelia at left
    show lucas at right
    a "You know what? Let's give it a try. If we approach it with sensitivity and care, it could be a really meaningful experience."
    lucas "Thank you, Amelia. Your support means a lot. Let's brainstorm some ideas for creating a safe and welcoming environment."

    if meet_sarah > 0:
        hide amelia_supportive_lucas_campus_full
        show black with dissolve
        jump sarah_conversation
    else:
        hide amelia_supportive_lucas_campus_full
        show black with dissolve
        jump part_2_end

label suggest_alternative_workshop:
    scene amelia_pensive_lucas_campus_full with dissolve
    show amelia at left
    show lucas at right
    a "Maybe we could start with a less personal topic, like exploring Jungian archetypes in literature or film."
    lucas "That's a great idea! It would still allow us to engage with the concepts, but in a more accessible way."
    a "Exactly. And it could be a stepping stone to deeper personal exploration in the future, if people feel comfortable."
    lucas "I like the way you think, Amelia. Let's plan an archetypes in media workshop and see how it goes."

    if meet_sarah > 0:
        hide amelia_pensive_lucas_campus_full
        show black with dissolve
        jump sarah_conversation
    else:
        hide amelia_pensive_lucas_campus_full
        show black with dissolve
        jump part_2_end

label sarah_conversation:
    scene amelia_sarah_coffee_shop_full with dissolve
    show amelia at left
    show sarah at right
    n "Later that day, Amelia meets Sarah at a cozy café near campus."
    sarah "Thanks for meeting with me, Amelia. I really appreciate having someone to talk to."

    show amelia_concerned_sarah_coffee_shop_full
    a "Of course, Sarah. I'm always here for you. How have you been doing lately?"
    sarah "Honestly? Not great. The depression has been really overwhelming, and I'm falling behind in my classes."

    menu:
        "Offer emotional support":
            $ MH += 1
            hide amelia_concerned_sarah_coffee_shop_full
            show black with dissolve
            jump emotional_support_sarah

        "Suggest practical solutions":
            $ MC += 1
            hide amelia_concerned_sarah_coffee_shop_full
            show black with dissolve
            jump practical_solutions_sarah

label emotional_support_sarah:
    scene amelia_compassionate_sarah_coffee_shop_full with dissolve
    show amelia at left
    show sarah at right
    a "Sarah, I'm so sorry you're going through this. Please remember that your worth is not defined by your academic performance."
    a "You're dealing with a real and serious illness. Be kind to yourself and focus on your well-being first."

    show sarah_teary_sarah_coffee_shop_full
    sarah "Thank you, Amelia. It's hard not to be hard on myself, but I know you're right."
    a "Is there anything I can do to support you right now? Even if it's just listening or sitting with you in the difficult moments?"

    show sarah_grateful_sarah_coffee_shop_full
    sarah "Just being here and understanding means more than you know. Can we maybe study together sometime? Having a friend nearby might help me stay focused."
    a "Absolutely. Let's plan a study session. And if you ever need to take a break or talk through what you're feeling, I'm here."

    $ MH += 1
    hide amelia_compassionate_sarah_coffee_shop_full
    show black with dissolve
    jump part_2_end

label practical_solutions_sarah:
    scene amelia_thoughtful_sarah_coffee_shop_full with dissolve
    show amelia at left
    show sarah at right
    a "Have you reached out to your professors about what you're going through? They might be able to offer extensions or accommodations."
    sarah "Not yet. I've been afraid to admit that I'm struggling."
    a "I understand that fear, but your professors are there to support your learning. They want you to succeed."
    a "And have you considered seeking help from the university counseling services? They have resources specifically for students dealing with mental health issues."

    show sarah_considering_sarah_coffee_shop_full
    sarah "I've thought about it, but taking that step feels scary. Maybe if I had someone to go with me the first time..."

    show amelia_supportive_sarah_coffee_shop_full
    a "I would be more than happy to accompany you, Sarah. We can look at the counseling center website together and see what options are available."
    sarah "Thank you, Amelia. Knowing I have your support makes it feel a bit less daunting."

    $ MC += 1
    hide amelia_supportive_sarah_coffee_shop_full
    show black with dissolve
    jump part_2_end

label part_2_end:
    scene amelia_reflecting_dorm_evening_full with dissolve
    show amelia at center
    n "Back in her dorm room, Amelia reflects on the day's events and interactions."

    if AA >= 3 and MH >= 3:
        hide amelia_reflecting_dorm_evening_full
        show black with dissolve
        scene amelia_pensive_dorm_night_full with dissolve
        show amelia at center
        a "Balancing academic pursuits with supporting friends through their struggles... It's not always easy, but it feels important."
    elif AA >= 3:
        hide amelia_reflecting_dorm_evening_full
        show black with dissolve
        scene amelia_studying_dorm_night_full with dissolve
        show amelia at center
        a "I'm learning so much, both in and out of the classroom. But I wonder if I'm doing enough to be there for the people in my life."
    elif MH >= 3:
        hide amelia_reflecting_dorm_evening_full
        show black with dissolve
        scene amelia_calling_dorm_night_full with dissolve
        show amelia at center
        a "Being a supportive friend and advocating for mental health... It's a crucial part of my journey. I just need to remember to take care of myself too."
    else:
        hide amelia_reflecting_dorm_evening_full
        show black with dissolve
        scene amelia_tired_dorm_night_full with dissolve
        show amelia at center
        a "It's been a challenging day, navigating all these different aspects of university life. But I know each experience is a chance to learn and grow."

    if lucas_dream_project > 0:
        n "As Amelia gets ready for bed, she receives a text from Lucas."
        hide amelia_tired_dorm_night_full
        show black with dissolve

        scene lucas_text_workshop_plans_full with dissolve
        lucas_text "Hey Amelia! I've been brainstorming some more ideas for the Jungian workshop. Can't wait to discuss them with you!"
        
        hide lucas_text_workshop_plans_full
        show black with dissolve

        scene amelia_smiling_dorm_night_full with dissolve
        show amelia at center
        a "(Lucas's enthusiasm is contagious. It's energizing to collaborate with friends who share my passions.)"
        a "(Tomorrow is a new day, with new opportunities to make a difference. In my studies, in my friendships, in my own growth.)"
        n "Amelia falls asleep, feeling grateful for the challenges and the support that university life brings."
        
        hide amelia_smiling_dorm_night_full
        show black with dissolve

    jump chapter_3_part_3

label chapter_3_part_3:
    scene amelia_waking_dorm_morning_full with dissolve
    show amelia at center
    if meet_sarah > 0:
        n "The next morning, Amelia wakes up early, her first thought being to check on Sarah."

        menu:
            "Call Sarah":
                hide amelia_waking_dorm_morning_full
                show black with dissolve
                jump call_sarah_morning

            "Send a text message":
                hide amelia_waking_dorm_morning_full
                show black with dissolve
                jump text_sarah_morning
    else: 
        n "The next morning, Amelia wakes up early and decides to get something to eat in the cafeteria."
        hide amelia_waking_dorm_morning_full
        show black with dissolve
        jump breakfast_with_liz

label call_sarah_morning:
    scene amelia_on_phone_concerned_full with dissolve
    show amelia at center
    n "Amelia dials Sarah's number, her heart racing as she waits for her to pick up."
    sarah "Hello?"
    a "Sarah, it's Amelia. I wanted to check in on you. How are you feeling today?"
    
    if MH >= 5:
        hide amelia_on_phone_concerned_full
        show black with dissolve

        scene sarah_on_phone_tired_full with dissolve
        show sarah at center
        sarah "Amelia... I'm okay. Tired, but okay. I called the hotline last night, like you suggested."
        a "I'm so glad to hear that, Sarah. That was a brave thing to do. How did it go?"
        sarah "It was hard, but it helped. They listened, and they gave me some resources for follow-up care. I think I'm going to make an appointment with the counseling center."
        a "That's wonderful, Sarah. I'm so proud of you for taking these steps. Remember, I'm here for you too, whenever you need me."
        sarah "Thank you, Amelia. Your support means more than you know."
        $ MH += 1
        $ SI += 1
        hide sarah_on_phone_tired_full
        show black with dissolve
    else:
        hide amelia_on_phone_concerned_full
        show black with dissolve

        scene sarah_on_phone_distant_full with dissolve
        show sarah at center
        sarah "I'm... I'm alive. That's about all I can say right now."
        a "Sarah, I'm so sorry. I should have done more to help you last night."
        sarah "It's not your fault, Amelia. I'm just... I'm not ready to talk about it yet."
        a "I understand. But please, don't shut me out. I'm here for you, whenever you're ready."
        sarah "...I know. Thank you, Amelia. I just need some time."
        $ MH += 1
        hide sarah_on_phone_distant_full
        show black with dissolve

    jump breakfast_with_liz

label text_sarah_morning:
    scene amelia_texting_concerned_full with dissolve
    show amelia at center
    n "Amelia composes a text to Sarah:"
    a "Good morning, Sarah. I just wanted to check in and see how you're doing today. I'm here if you need anything."
    n "She hits send and waits anxiously for a response."
    
    if renpy.random.randint(1, 10) <= 3:
        n "Hours pass with no reply from Sarah. Amelia grows increasingly worried."
        a "(What if something happened to her? What if she's not okay?)"
        n "Just as Amelia is about to call the emergency services, her phone buzzes."
        hide amelia_texting_concerned_full
        show black with dissolve

        scene sarah_text_reassuring_full with dissolve
        show sarah_text at center
        sarah "Hey Amelia, sorry for the late reply. I was at an appointment with the counseling center. I'm okay. Thank you for checking in."
        a "Sarah, I'm so relieved to hear from you. And I'm proud of you for seeking help. That's a big step."
        sarah "It wasn't easy, but I knew I needed to do something. I'm glad I did."
        a "I'm here for you, Sarah. Always. Let's catch up in person soon, okay?"
        sarah "I'd like that. Thanks, Amelia."
        $ MH += 2
        hide sarah_text_reassuring_full
        show black with dissolve
    else:
        hide amelia_texting_concerned_full
        show black with dissolve

        scene sarah_text_short_full with dissolve
        show sarah_text at center
        sarah "I'm hanging in there. Thanks for checking in."
        a "Of course, Sarah. I'm always here if you need to talk."
        sarah "I know. I appreciate it."
        a "Let's grab coffee soon, okay? I'd love to see you."
        sarah "Sure, let's do that. I'll text you."
        $ SI += 1
        hide sarah_text_short_full
        show black with dissolve

    jump breakfast_with_liz

label breakfast_with_liz:
    scene amelia_liz_breakfast_cafeteria_full with dissolve
    show amelia at left
    show liz at right
    if meet_sarah > 0:
        n "Amelia heads to the cafeteria for breakfast, her mind still preoccupied with thoughts of Sarah."
        hide amelia_liz_breakfast_cafeteria_full
        show black with dissolve

        scene liz_neutral_cafeteria_full with dissolve
        show liz at center
        l "Morning, Amelia. You look tired. Late night studying?"
        a "Not exactly. I was up late worrying about Sarah. She's going through a tough time."
        hide liz_neutral_cafeteria_full
        show black with dissolve

        scene liz_concerned_cafeteria_full with dissolve
        show liz at center
        l "Oh no, I'm sorry to hear that. Is she okay?"
        show black with dissolve
        
        menu:
            "Share details about Sarah's struggles":
                $ SI += 1
                hide liz_concerned_cafeteria_full
                show black with dissolve
                jump share_sarah_details
            
            "Keep the details private":
                $ MC += 1
                hide liz_concerned_cafeteria_full
                show black with dissolve
                jump keep_sarah_private
    else:
        hide amelia_liz_breakfast_cafeteria_full
        show black with dissolve

        scene liz_neutral_cafeteria_full with dissolve
        show liz at center
        n "Amelia heads to the cafeteria for breakfast."
        l "Morning, Amelia. You look tired. Late night studying?"
        a "You can say that twice, so many new things to take in."
        if OK >= 1:
            hide liz_neutral_cafeteria_full
            show black with dissolve
            jump occult_studies_intro
        else:
            n "Amelia gets a strange feeling that this day could really have turned out differently."
            n "She decided to spend the day studying and before she knows it the whole day flew by."
            show black with dissolve
            jump chapter_3_end

label share_sarah_details:
    scene amelia_concerned_liz_cafeteria_full with dissolve
    show amelia at left
    show liz at right
    a "She's struggling with depression and had a bit of a crisis last night. I'm really worried about her."
    l "That's so heavy, Amelia. I'm glad she has you to support her. Have you suggested she talk to a counselor?"
    a "I have, and she's actually taking that step. I'm proud of her, but I know the road ahead won't be easy."
    l "No, it won't. But with friends like you by her side, I'm sure she'll get through this."
    a "Thanks, Liz. I hope so. I just wish I could do more."
    hide amelia_concerned_liz_cafeteria_full
    show black with dissolve

    scene liz_supportive_liz_cafeteria_full with dissolve
    show liz at center
    l "You're doing a lot just by being there for her, Amelia. Don't underestimate the value of that."
    a "I guess you're right. Thanks, Liz."
    $ SI += 1
    hide liz_supportive_liz_cafeteria_full
    show black with dissolve
    jump occult_studies_intro

label keep_sarah_private:
    scene amelia_reserved_liz_cafeteria_full with dissolve
    show amelia at left
    show liz at right
    a "She's just going through some personal stuff. I don't want to share the details without her permission."
    l "Of course, I understand. It's good that you respect her privacy."
    a "I just wish I knew how to help her more."
    hide amelia_reserved_liz_cafeteria_full
    show black with dissolve

    scene liz_supportive_liz_cafeteria_full with dissolve
    show liz at center
    l "Sometimes, just being there is the most helpful thing you can do. Let her know you're there for her, but don't push."
    a "That's good advice. Thanks, Liz."
    l "Anytime, Amelia. And hey, make sure you're taking care of yourself too, okay?"
    a "I will. Thanks for looking out for me."
    $ MC += 1
    hide liz_supportive_liz_cafeteria_full
    show black with dissolve
    jump occult_studies_intro

label occult_studies_intro:
    scene amelia_maya_library_full with dissolve
    show amelia at left
    show maya at right
    n "Later that day, Amelia is in the library studying when she overhears a conversation that piques her interest."
    hide amelia_maya_library_full
    show black with dissolve

    scene maya_excited_library_full with dissolve
    show maya at center
    m "I'm telling you, there's so much more to reality than what we can see. The occult studies reveal hidden truths about the nature of the universe."
    n "Intrigued, Amelia turns to see Maya engaged in an animated discussion with another student."
    
    menu:
        "Approach Maya and ask about occult studies":
            $ OK += 1
            hide maya_excited_library_full
            show black with dissolve
            jump ask_maya_occult
        
        "Continue studying":
            hide maya_excited_library_full
            show black with dissolve
            jump continue_studying

label ask_maya_occult:
    stop music fadeout 2.0
    play music inkpot_gods fadein 2.0 volume 0.3

    scene amelia_curious_maya_library_full with dissolve
    show amelia at left
    show maya at right
    a "Hey Maya, I couldn't help but overhear. What are these occult studies you're talking about?"
    hide amelia_curious_maya_library_full
    show black with dissolve

    scene maya_enthusiastic_maya_library_full with dissolve
    show maya at center
    m "Oh, Amelia! It's fascinating stuff. Occult studies delve into the mystical, the esoteric, the hidden knowledge of the ages."
    a "That sounds really intriguing. Where do you even start with something like that?"
    m "There are a lot of entry points. Ancient texts, secret societies, spiritual practices... It's a vast field."
    
    if renpy.random.randint(1, 10) <= 2:
        hide maya_enthusiastic_maya_library_full
        show black with dissolve

        scene maya_secretive_maya_library_full with dissolve
        show maya at center
        m "Actually, if you're really interested, I know of a place where you can learn more. But it's not exactly... public."
        a "What do you mean?"
        m "There's a secret society on campus, dedicated to the study of the occult. They're very selective about who they let in, but I could put in a word for you."
        a "A secret society? That's... wow. I don't know, Maya. That sounds a bit intense."
        m "I understand. It's not for everyone. But if you change your mind, the offer stands. In the meantime, I can recommend some books if you want to explore on your own."
        a "I'd appreciate that. Thanks, Maya."
        n "Maya writes down a list of titles and hands it to Amelia."
        $ OK += 2
        show black with dissolve
    else:
        m "If you're interested, I can recommend some good introductory texts. There's a great section here in the library on esoteric philosophy."
        a "That would be great, Maya. I'd love to learn more."
        m "Wonderful! I'm always happy to guide a fellow seeker. Let's see, you should start with..."
        n "Maya proceeds to give Amelia a crash course in occult studies, recommending books and sharing her own insights."
        a "This is all so fascinating, Maya. Thank you for sharing your knowledge with me."
        m "Of course, Amelia. I sense a kindred spirit in you. If you ever want to discuss these topics further, my door is always open."
        $ OK += 1
        hide maya_enthusiastic_maya_library_full
        show black with dissolve

    jump study_session_reflection

label continue_studying:
    n "As fascinating as the conversation sounds, Amelia decides to focus on her studies for now."
    a "(I can't afford to get distracted. These exams won't pass themselves.)"
    n "She puts her head down and immerses herself in her textbooks."
    
    if AA >= 6:
        n "Thanks to her diligent studying, Amelia feels well-prepared for her upcoming exams."
        a "(I'm glad I stayed focused. I feel confident about this material now.)"
        $ AA += 1
    else:
        n "Despite her best efforts, Amelia struggles to concentrate."
        a "(I can't stop thinking about Sarah... and now this occult stuff too. My brain is all over the place.)"
        n "She sighs and redoubles her efforts, but the studying is slow-going."
    
    jump study_session_reflection

label study_session_reflection:
    scene amelia_reflecting_dorm_evening_full with dissolve
    show amelia at center
    n "That evening, as Amelia is reflecting on her day, her thoughts keep returning to Sarah and the conversation with Maya."
    a "(So much has happened in such a short time. Sarah's struggles, my own academic pressures, and now this whole new world of occult knowledge...)"
    
    if OK >= 3 and renpy.random.randint(1, 10) <= 3:
        hide amelia_reflecting_dorm_evening_full
        show black with dissolve

        scene amelia_pensive_dorm_full with dissolve
        show amelia at center
        a "(I can't stop thinking about what Maya said about that secret society. It's tempting... but also a little scary.)"
        n "As if on cue, Amelia's phone buzzes with a message from an unknown number."
        hide amelia_pensive_dorm_full
        show black with dissolve

        scene secret_society_text_full with dissolve
        n "Unknown: We hear you're interested in the deeper mysteries. If you seek true knowledge, come to the old chapel at midnight. Come alone."
        a "(What the... how did they get my number? Is this from the secret society Maya mentioned?)"
        n "Amelia's heart races as she considers the implications."
        menu:
            "Go to the old chapel at midnight":
                hide secret_society_text_full
                show black with dissolve
                jump secret_society_meeting

            "Ignore the message":
                a "(No, this is too weird. I'm not getting involved in this.)"
                n "Amelia deletes the message and tries to put it out of her mind."
                hide secret_society_text_full
                show black with dissolve
                jump late_night_worries
    else:
        n "Even with all the challenges and mysteries, Amelia feels a sense of growth and purpose."
        a "(I'm learning so much, about the world and about myself. I feel like I'm exactly where I'm meant to be.)"
        n "With a sense of contentment, she settles into bed for the night."
        hide amelia_reflecting_dorm_evening_full
        show black with dissolve
        jump late_night_worries

label secret_society_meeting:
    $ OK += 2
    scene amelia_old_chapel_night_full with dissolve
    show amelia at center
    n "Against her better judgment, Amelia finds herself sneaking out of her dorm room at midnight and heading towards the old chapel."
    a "(What am I doing? This is crazy. But I can't deny I'm curious...)"
    hide amelia_old_chapel_night_full
    show black with dissolve

    scene amelia_entering_chapel_full with dissolve
    show amelia at center
    n "She enters the candlelit chapel, her footsteps echoing in the eerie silence."
    hide amelia_entering_chapel_full
    show black with dissolve

    scene hooded_figure_chapel_full with dissolve
    show hooded_figure at center
    n "Hooded Figure: Welcome, seeker. We've been expecting you."
    a "Who are you? What is this place?"
    n "Hooded Figure: We are the guardians of ancient wisdom, the seekers of hidden truths. And this is where your true education begins, if you're brave enough to embark on the journey."
    a "I... I don't know. This is all so sudden."
    n "Hooded Figure: Knowledge is not for the faint of heart, Amelia. If you wish to uncover the secrets of the universe, you must be willing to step into the unknown."
    
    if renpy.random.randint(1, 10) <= 4:
        n "Hooded Figure: But perhaps you are not ready. Perhaps you should return to your safe, ordinary life."
        a "No! I... I want to learn. I'm ready."
        n "A smile is just visible beneath the figure's hood."
        n "Hooded Figure: Very well. Your initiation begins now."
        hide hooded_figure_chapel_full
        show black with dissolve

        scene amelia_initiation_chapel_full with dissolve
        show amelia at center
        n "What follows is a night of strange rituals, cryptic teachings, and esoteric knowledge that Amelia can barely comprehend."
        $ OK += 3
        hide amelia_initiation_chapel_full
        show black with dissolve
    else:
        a "I... I'm sorry. I don't think I'm ready for this. It's all too much."
        n "Hooded Figure: As you wish. The door is always open, should you change your mind."
        n "Amelia hurries out of the chapel, her heart pounding."
        $ OK += 1
        hide hooded_figure_chapel_full
        show black with dissolve
    jump late_night_worries

label late_night_worries:
    scene amelia_dorm_room_night_dark_full with dissolve
    show amelia at center
    n "As Amelia lies in bed, her mind races with the events of the day and the challenges ahead."
    a "(Sarah, my studies, the secret society... It's all so overwhelming. How am I supposed to handle all of this?)"
    
    if renpy.random.randint(1, 10) <= 3:
        n "Suddenly, Amelia's phone rings. It's Sarah."
        hide amelia_dorm_room_night_dark_full
        show black with dissolve

        scene amelia_on_phone_night_full with dissolve
        show amelia at center
        a "Sarah? Is everything okay?"
        hide amelia_on_phone_night_full
        show black with dissolve

        scene sarah_on_phone_crying_full with dissolve
        show sarah at center
        s "Amelia... I'm sorry. I know it's late. I just... I had a nightmare. I needed to hear your voice."
        a "It's okay, Sarah. I'm here. Do you want to talk about it?"
        n "Amelia spends the next hour on the phone with Sarah, comforting her and reassuring her until she's calm enough to sleep."
        $ MH += 2
        hide sarah_on_phone_crying_full
        show black with dissolve
    else:
        n "Despite her worries, exhaustion eventually overtakes Amelia, and she falls into a restless sleep."
        n "Her dreams are filled with strange symbols, shadowy figures, and a sense of foreboding that lingers even after she wakes."
        hide amelia_dorm_room_night_dark_full
        show black with dissolve
    jump chapter_3_end

label chapter_3_end:
    scene amelia_waking_dorm_morning_light_full with dissolve
    show amelia at center
    n "The next morning, Amelia wakes feeling drained but determined."
    
    if MH >= 7 and OK >= 5:
        n "Despite the challenges and mysteries she's facing, Amelia feels a sense of purpose and growth."
        a "(I'm learning so much, about myself and the world around me. I'm discovering strength I didn't know I had.)"
        a "(I don't know what the future holds, but I know I'm ready to face it, for Sarah's sake and for my own.)"
        hide amelia_waking_dorm_morning_light_full
        show black with dissolve
    else:
        n "The weight of her responsibilities and the uncertainty of the path ahead weigh heavily on Amelia."
        a "(I don't know if I'm strong enough for this. But I have to try.)"
        n "With a deep breath, Amelia steels herself for whatever comes next."
        hide amelia_waking_dorm_morning_light_full
        show black with dissolve

    n "As she prepares for the day ahead, she can't shake the feeling that everything is about to change."
    a "(I have a feeling this is just the beginning. The real challenges are still to come.)"
    n "With a mix of anticipation and trepidation, Amelia steps out into the uncertain future."
    n "Chapter 4 is still in the works."
    n "So here is what you can do now:"
    menu:
        "Go back to main menu":
            hide amelia_waking_dorm_morning_light_full
            show black with dissolve
            return
        
        "Checkout the Occult hidden ending":
            hide amelia_waking_dorm_morning_light_full
            show black with dissolve
            jump chapter_12_enlightenment
