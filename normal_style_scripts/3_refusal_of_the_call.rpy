define meet_sarah = 0
define lucas_dream_project = 0

label chapter_3_part_1:
    stop music fadeout 2.0
    play music sand fadein 2.0 volume 0.3
    show amelia_determined_dorm_full
    with dissolve
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
            $ SI += 1
            hide amelia_thinking_dorm_full
            show black
            window hide

            jump prioritize_social_life

label focus_on_academics:
    show amelia_studying_library_full
    with dissolve
    n "Amelia decides to dedicate her first few weeks to getting a strong start academically. She spends long hours in the library, poring over her textbooks and notes."
    hide amelia_studying_library_full
    show black
    window hide

    show amelia_raised_hand_classroom_full
    n "In classes, she's an active participant, always ready with a question or a thoughtful comment."
    
    if AA >= 3:
        hide amelia_raised_hand_classroom_full
        show black
        window hide

        show professor_impressed_classroom_full
        n "Her professors take note of her engagement and dedication."
        professor "Amelia, your contributions to the class discussions have been excellent. Keep up the great work!"
        a "Thank you, professor. I'm really enjoying delving into the material."
        $ AA += 1
        hide professor_impressed_classroom_full
        show black
        window hide

    else:
        hide amelia_raised_hand_classroom_full
        show black
        window hide

        show professor_neutral_classroom_full
        n "Her professors appreciate her participation, but encourage her to also seek balance in her university life."
        professor "Amelia, it's great to see your enthusiasm for the subject. Remember, university is also about personal growth and exploration. Don't forget to make time for other experiences too."
        a "You're right, professor. I'll keep that in mind."
        hide professor_neutral_classroom_full
        show black
        window hide

    jump meet_liz

label prioritize_social_life:
    show amelia_exploring_barbican_full
    with dissolve
    n "Eager to immerse herself in all that Plymouth has to offer, Amelia dives into exploring the city and engaging with her peers."
    hide amelia_exploring_barbican_full
    show black
    window hide

    show amelia_chatting_student_union_full
    n "She attends social events at the Student Union, joining clubs and societies that pique her interest."


    if SI >= 3:
        hide amelia_chatting_student_union_full
        show black
        window hide

        show amelia_laughing_student_union_full
        n "Amelia quickly becomes a familiar face around campus, known for her friendly demeanor and enthusiasm."
        a "I'm loving getting to know so many different people! Everyone has such fascinating stories and perspectives."
        $ SI += 1
        hide amelia_laughing_student_union_full
        show black
        window hide
        
    else:
        hide amelia_chatting_student_union_full
        show black
        window hide

        show amelia_overwhelmed_student_union_full
        n "While Amelia enjoys the social interactions, she sometimes feels spread a bit thin."
        a "I might need to be a bit more selective with my commitments. I don't want to neglect my studies either."
        hide amelia_overwhelmed_student_union_full
        show black
        window hide

    jump meet_liz

label meet_liz:
    show amelia_liz_first_meeting_dorm_full
    with dissolve
    n "One evening, Amelia returns to her dorm room to find her roommate, Liz, crying."

    menu:
        "Comfort Liz":
            $ MH += 1
            hide amelia_overwhelmed_student_union_full
            show black
            window hide

            jump comfort_liz
        
        "Give Liz some space":
            hide amelia_overwhelmed_student_union_full
            show black
            window hide

            jump give_liz_space

label comfort_liz:
    show amelia_comforting_liz_dorm_full
    a "Liz, what's wrong? Do you want to talk about it?"
    liz "I'm just feeling so overwhelmed. I don't know if I belong here."
    a "Oh, Liz. I understand. Adjusting to university life can be really tough."

    menu:
        "Share your own struggles":
            $ SI += 1
            hide amelia_comforting_liz_dorm_full
            show black
            window hide

            jump share_struggles
        
        "Offer practical advice":
            $ MC += 1
            hide amelia_comforting_liz_dorm_full
            show black
            window hide

            jump offer_advice

label share_struggles:
    show amelia_liz_bonding_dorm_full
    a "I've been feeling overwhelmed too. It's a big transition, and it's okay to not have it all figured out."
    liz "Really? You always seem so put together."
    a "Trust me, I have my moments of doubt too. But we're in this together, Liz."
    liz "Thanks, Amelia. It's good to know I'm not alone."
    hide amelia_liz_bonding_dorm_full
    $ MH += 1
    show black
    window hide

    jump zara_incident

label offer_advice:
    show amelia_advice_liz_dorm_full
    a "Have you considered talking to your professors or a counselor? They might be able to offer some guidance and support."
    liz "I hadn't thought of that. I guess I was afraid to admit I was struggling."
    a "Seeking help is a sign of strength, not weakness. And there are so many resources available to us here."
    liz "You're right. I'll look into making an appointment. Thanks, Amelia."
    hide amelia_advice_liz_dorm_full
    show black
    window hide

    jump zara_incident

label give_liz_space:
    show amelia_concerned_liz_dorm_full
    n "Not wanting to intrude, Amelia decides to give Liz some privacy."
    a "I'll be in the lounge if you need me, Liz. Don't hesitate to reach out."
    n "Amelia leaves the room, feeling a bit uncertain about whether she made the right choice."
    $ MC -= 1
    hide amelia_concerned_liz_dorm_full
    show black
    window hide

    jump zara_incident

label zara_incident:
    show amelia_zara_concerned_quad_full
    with dissolve
    n "The next day, Amelia witnesses a disturbing incident on the quad. She sees Zara, an international student, being harassed by a group of students."
    hide amelia_zara_concerned_quad_full
    show black
    window hide

    show amelia_angry_quad_full
    n "One of the harassers shouts:"
    student_2 "Go back to where you came from! We don't want your kind here."

    menu:
        "Intervene directly":
            $ MC += 1
            hide amelia_angry_quad_full
            show black
            window hide

            jump intervene_zara
        
        "Report the incident":
            $ SI += 1
            hide amelia_angry_quad_full
            show black
            window hide

            jump report_zara

label intervene_zara:
    show amelia_confronting_harassers_quad_full
    a "Hey! Leave her alone! What you're doing is not okay."
    n "Amelia steps between Zara and the harassers, standing her ground."
    student_2 "Mind your own business. This doesn't concern you."
    a "It concerns me when I see someone being discriminated against. Your behavior is unacceptable."
    n "The harassers, not expecting resistance, back off and leave."
    hide amelia_confronting_harassers_quad_full
    show black
    window hide

    show amelia_comforting_zara_quad_full
    a "Zara, are you alright? I'm so sorry that happened to you."
    zara "I'm shaken, but I'll be okay. Thank you for standing up for me, Amelia."
    a "Of course. No one deserves to be treated like that. If you need anything, I'm here for you."
    $ MC += 1
    $ SI += 1
    hide amelia_comforting_zara_quad_full
    show black
    window hide
    
    jump sarah_introduction

label report_zara:
    show amelia_reporting_incident_office_full
    n "Amelia discreetly takes photos of the harassers and then approaches Zara."
    a "Zara, I saw what happened. That was awful. I've documented the incident, and I think we should report it to the university authorities."
    zara "I don't know, Amelia. I don't want to cause trouble."
    a "You're not causing trouble. Those students are the ones in the wrong. The university needs to know so they can take appropriate action."
    zara "Okay. Let's do it. Thank you for your support, Amelia."
    n "Together, they go to the student affairs office and file a report."
    $ SI += 1
    $ MH += 1
    hide amelia_reporting_incident_office_full
    show black
    window hide

    jump sarah_introduction

label sarah_introduction:
    show amelia_concerned_sarah_student_lounge_full
    with dissolve
    n "A few days later, Amelia is studying in the student lounge when she notices a girl sitting alone, looking distressed."

    menu:
        "Approach the girl":
            $ MH += 1
            $ meet_sarah = 1
            hide amelia_concerned_sarah_student_lounge_full
            show black
            window hide 

            jump approach_sarah
        
        "Focus on your studies":
            hide amelia_concerned_sarah_student_lounge_full
            show black
            window hide 

            jump focus_studies

label approach_sarah:
    show amelia_approaching_sarah_student_lounge_full
    a "Hi there. I couldn't help but notice that you seem a bit upset. Is everything okay?"
    n "The girl looks up, surprised that someone is talking to her."
    sarah "Oh, hi. I'm Sarah. It's just been a tough week."
    a "I'm Amelia. I'm sorry to hear that. Do you want to talk about it?"
    
    if MH >= 3:
        n "Sarah hesitates for a moment, then nods."
        hide amelia_approaching_sarah_student_lounge_full
        show black
        window hide

        show sarah_opening_up_student_lounge_full
        sarah "It's just... I've been struggling with depression for a while now. And being at university, away from my support system, has been really hard."
        a "Sarah, I'm so glad you shared that with me. Dealing with mental health issues is challenging, especially in a new environment."
        sarah "I feel so alone sometimes. Like no one understands what I'm going through."
        a "You're not alone, Sarah. There are people here who care and want to support you, myself included."
        n "The two continue to talk, forming a bond of understanding and support."
        $ MH += 1
        $ SI += 1

        show black
        window hide

    else:
        hide amelia_approaching_sarah_student_lounge_full
        show black
        window hide

        show sarah_hesitant_student_lounge_full
        sarah "Thanks for asking, but I don't really feel like talking about it right now."
        a "I understand. If you ever do want to talk, though, I'm here to listen."
        sarah "I appreciate that, Amelia. It's good to know there are kind people like you around."
        $ SI += 1
        hide sarah_hesitant_student_lounge_full
        show black
        window hide

    jump part_1_end

label focus_studies:
    n "Amelia considers approaching the girl but decides against it, not wanting to intrude."
    a "(She probably wants to be left alone. I should focus on my own work.)"
    n "She turns back to her books, but can't quite shake the feeling that she might have missed an opportunity to help someone in need."
    show black
    window hide

    jump part_1_end

label part_1_end:
    show amelia_reflecting_dorm_full
    with dissolve
    n "As the first part of the semester comes to a close, Amelia reflects on the experiences she's had so far."
    if AA >= 4 and SI >= 4:
        n "She's managed to strike a good balance between her academic pursuits and her social life, and feels she's growing in both areas."
    elif AA >= 4:
        n "She's excelled academically, but wonders if she should be putting more effort into building friendships and exploring all that university life has to offer."
    elif SI >= 4:
        n "She's made a lot of new friends and has had some memorable experiences, but realizes she may need to devote more time to her studies."
    else:
        n "She feels she's had a bit of a rocky start, and hasn't quite found her footing yet in either her academic or social life."
    
    n "But regardless of the challenges, Amelia remains determined to make the most of her time at Plymouth."
    hide amelia_reflecting_dorm_full
    show black
    window hide
    
    show amelia_determined_dorm_night_full
    a "This is just the beginning. I know I have a lot to learn, about myself and the world around me. But I'm ready for whatever comes next."
    n "With that thought, she turns off her light and goes to sleep, eager for the next part of her journey."
    hide amelia_determined_dorm_night_full
    show black
    window hide

    jump chapter_3_part_2

label chapter_3_part_2:
    show amelia_waking_dorm_full
    with dissolve
    n "Amelia wakes up to a sunny morning, feeling refreshed and ready to tackle the day."
    hide amelia_waking_dorm_full
    show black
    window hide

    show amelia_thinking_dorm_full
    a "I think I'll explore more of the city today. There's so much to see and do in Plymouth!"
    menu:
        "Visit the Marine Biological Association":
            $ AA += 1
            hide amelia_thinking_dorm_full
            show black
            window hide

            jump visit_mba
        "Explore the Hoe Park":
            $ SD += 1
            hide amelia_thinking_dorm_full
            show black
            window hide

            jump explore_hoe_park

label visit_mba:
    show amelia_visiting_mba_full
    with dissolve
    n "Amelia decides to visit the Marine Biological Association, curious about the intersection of psychology and environmental science."
    a "Wow, this place is fascinating! I never thought about how the study of marine life could relate to psychology."
    n "She attends a lecture on the behavioral patterns of marine mammals and how they respond to environmental stressors."
    hide amelia_visiting_mba_full
    show black
    window hide

    show scientist_explaining_mba_full
    scientist "Understanding the psychological impacts of environmental change on marine life can give us insights into the resilience and adaptability of these species."
    a "That's so interesting! It makes me think about how the environment shapes behavior and mental processes in all living beings."
    menu:
        "Ask a question":
            $ AA += 1
            hide scientist_explaining_mba_full
            show black
            window hide

            jump ask_question_mba
        "Take detailed notes":
            $ AA += 1
            hide scientist_explaining_mba_full
            show black
            window hide

            jump take_notes_mba

label ask_question_mba:
    show amelia_raising_hand_mba_full
    a "Excuse me, I have a question. How might the principles of behavioral psychology be applied in the context of marine conservation efforts?"
    hide amelia_raising_hand_mba_full
    show black
    window hide

    show scientist_pleased_mba_full
    scientist "That's an excellent question! By understanding the behavioral patterns and psychological needs of marine species, we can design more effective conservation strategies."
    scientist "For example, if we know that certain species have strong social bonds, we can prioritize protecting their social structures in our conservation plans."
    a "That makes a lot of sense. Thank you for the explanation!"
    $ AA += 1
    hide scientist_pleased_mba_full
    show black
    window hide

    jump meet_lucas

label take_notes_mba:
    n "Amelia takes out her notebook and starts jotting down the key points from the lecture."
    show black
    window hide

    show amelia_writing_mba_full
    a "(The connection between environmental stressors and behavioral changes in marine mammals... The potential applications in conservation efforts...)"
    n "She makes a note to follow up on these ideas and look for relevant research papers."
    $ AA += 1
    hide amelia_writing_mba_full
    show black
    window hide

    jump meet_lucas

label explore_hoe_park:
    show amelia_exploring_hoe_park_full
    with dissolve
    n "Feeling in need of some fresh air and reflection, Amelia heads to Hoe Park."
    a "The view of the Plymouth Sound is breathtaking. It's the perfect place to clear my head."
    n "As she walks along the waterfront, Amelia spots a group of people practicing tai chi."

    menu:
        "Join the tai chi group":
            $ MH += 1
            hide amelia_exploring_hoe_park_full
            show black
            window hide
            
            jump join_tai_chi
        "Find a quiet spot to journal":
            $ SD += 1
            hide amelia_exploring_hoe_park_full
            show black
            window hide

            jump journal_hoe_park

label join_tai_chi:
    show amelia_joining_tai_chi_full
    n "Intrigued, Amelia approaches the group and asks if she can join in."
    hide amelia_joining_tai_chi_full
    show black
    window hide

    show tai_chi_instructor_welcoming_full
    instructor "Of course! Welcome. Tai chi is a wonderful practice for cultivating mindfulness and inner peace."
    n "The instructor guides Amelia through the basic movements, emphasizing the importance of breath and body awareness."
    a "This is surprisingly challenging, but in a good way. I can feel myself becoming more centered and grounded."
    hide tai_chi_instructor_welcoming_full
    show black
    window hide

    show amelia_serene_tai_chi_full
    n "As she synchronizes her movements with the group, Amelia feels a sense of connection and shared presence."
    $ MH += 1
    hide amelia_serene_tai_chi_full
    show black
    window hide

    jump meet_lucas

label journal_hoe_park:
    show amelia_journaling_hoe_park_full
    n "Amelia finds a quiet bench overlooking the water and takes out her journal."
    a "(So much has happened in such a short time. The challenges, the growth, the new people I've met...)"
    n "She starts writing, pouring her thoughts and feelings onto the page."
    a "(I'm learning so much about myself and the world around me. It's not always easy, but I know I'm exactly where I'm meant to be.)"
    n "As she writes, Amelia gains clarity and perspective on her journey so far."
    $ SD += 1
    hide amelia_journaling_hoe_park_full
    show black
    window hide

    jump meet_lucas

label meet_lucas:
    show amelia_lucas_campus_full
    with dissolve
    n "On her way back to campus, Amelia runs into Lucas, who seems excited about something."
    lucas "Amelia! Just the person I was hoping to see. I have an idea I want to run by you."
    hide amelia_lucas_campus_full
    show black
    window hide

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
            show black
            window hide

            jump agree_dream_workshop
        "Express reservations":
            hide amelia_curious_lucas_campus_full
            show black
            window hide

            jump reservations_dream_workshop

label agree_dream_workshop:
    show amelia_excited_lucas_campus_full
    a "Lucas, that's a fantastic idea! It would be such a unique way to engage with the material and learn from each other."
    lucas "Right? And it would be a great opportunity to create a sense of community and shared exploration."
    a "Absolutely. Let's do it! We can talk to the professor and see if they have any guidance or resources for us."
    lucas "Perfect. I'm so glad you're on board, Amelia. With your insights and passion, I know this will be a meaningful experience for everyone involved."
    $ AA += 1
    $ SI += 1
    hide amelia_excited_lucas_campus_full
    show black
    window hide

    jump sarah_conversation

label reservations_dream_workshop:
    stop music fadeout 2.0
    play music drinking_song_for_the_socially_anxious fadein 2.0 volume 0.3

    show amelia_hesitant_lucas_campus_full
    a "I don't know, Lucas. Dream interpretation can be pretty personal and sensitive. What if people feel uncomfortable sharing?"
    lucas "That's a valid concern. We could make it clear that sharing is optional and create a safe, non-judgmental space."
    a "I suppose you're right. And it could be a powerful way to explore the unconscious mind and support each other's growth."
    lucas "Exactly. But I understand if you're not comfortable with the idea. It's just something I've been excited about."

    menu: 
        "Decide to support the idea":
            $ SI += 1
            $ lucas_dream_project = 1
            hide amelia_hesitant_lucas_campus_full
            show black
            window hide

            jump support_dream_workshop
        "Suggest an alternative":
            hide amelia_hesitant_lucas_campus_full
            show black
            window hide

            jump suggest_alternative_workshop

label support_dream_workshop:
    show amelia_supportive_lucas_campus_full
    a "You know what? Let's give it a try. If we approach it with sensitivity and care, it could be a really meaningful experience."
    lucas "Thank you, Amelia. Your support means a lot. Let's brainstorm some ideas for creating a safe and welcoming environment."
    $ SI += 1
    if meet_sarah > 0:
        hide amelia_supportive_lucas_campus_full
        show black
        window hide

        jump sarah_conversation

    else:
        hide amelia_supportive_lucas_campus_full
        show black
        window hide

        jump part_2_end

label suggest_alternative_workshop:
    show amelia_pensive_lucas_campus_full
    a "Maybe we could start with a less personal topic, like exploring Jungian archetypes in literature or film."
    lucas "That's a great idea! It would still allow us to engage with the concepts, but in a more accessible way."
    a "Exactly. And it could be a stepping stone to deeper personal exploration in the future, if people feel comfortable."
    lucas "I like the way you think, Amelia. Let's plan an archetypes in media workshop and see how it goes."

    if meet_sarah > 0:
        hide amelia_pensive_lucas_campus_full
        show black
        window hide

        jump sarah_conversation

    else:
        hide amelia_pensive_lucas_campus_full
        show black
        window hide
        
        jump part_2_end

label sarah_conversation:
    show amelia_sarah_coffee_shop_full
    with dissolve
    n "Later that day, Amelia meets Sarah at a cozy café near campus."
    sarah "Thanks for meeting with me, Amelia. I really appreciate having someone to talk to."
    hide amelia_sarah_coffee_shop_full
    show black
    window hide

    show amelia_concerned_sarah_coffee_shop_full
    a "Of course, Sarah. I'm always here for you. How have you been doing lately?"
    sarah "Honestly? Not great. The depression has been really overwhelming, and I'm falling behind in my classes."

    menu:
        "Offer emotional support":
            $ MH += 1
            hide amelia_concerned_sarah_coffee_shop_full
            show black
            window hide

            jump emotional_support_sarah

        "Suggest practical solutions":
            $ MC += 1
            hide amelia_concerned_sarah_coffee_shop_full
            show black
            window hide

            jump practical_solutions_sarah

label emotional_support_sarah:
    show amelia_compassionate_sarah_coffee_shop_full
    a "Sarah, I'm so sorry you're going through this. Please remember that your worth is not defined by your academic performance."
    a "You're dealing with a real and serious illness. Be kind to yourself and focus on your well-being first."
    hide amelia_compassionate_sarah_coffee_shop_full
    show black
    window hide

    show sarah_teary_sarah_coffee_shop_full
    sarah "Thank you, Amelia. It's hard not to be hard on myself, but I know you're right."
    a "Is there anything I can do to support you right now? Even if it's just listening or sitting with you in the difficult moments?"
    hide sarah_teary_sarah_coffee_shop_full
    show black
    window hide

    show sarah_grateful_sarah_coffee_shop_full
    sarah "Just being here and understanding means more than you know. Can we maybe study together sometime? Having a friend nearby might help me stay focused."
    a "Absolutely. Let's plan a study session. And if you ever need to take a break or talk through what you're feeling, I'm here."
    $ MH += 1
    hide sarah_grateful_sarah_coffee_shop_full
    show black
    window hide

    jump part_2_end

label practical_solutions_sarah:
    show amelia_thoughtful_sarah_coffee_shop_full
    a "Have you reached out to your professors about what you're going through? They might be able to offer extensions or accommodations."
    sarah "Not yet. I've been afraid to admit that I'm struggling."
    a "I understand that fear, but your professors are there to support your learning. They want you to succeed."
    a "And have you considered seeking help from the university counseling services? They have resources specifically for students dealing with mental health issues."
    hide amelia_thoughtful_sarah_coffee_shop_full
    show black
    window hide

    show sarah_considering_sarah_coffee_shop_full
    sarah "I've thought about it, but taking that step feels scary. Maybe if I had someone to go with me the first time..."
    hide sarah_considering_sarah_coffee_shop_full
    show black
    window hide

    show amelia_supportive_sarah_coffee_shop_full
    a "I would be more than happy to accompany you, Sarah. We can look at the counseling center website together and see what options are available."
    sarah "Thank you, Amelia. Knowing I have your support makes it feel a bit less daunting."
    $ MC += 1
    hide amelia_supportive_sarah_coffee_shop_full
    show black
    window hide

    jump part_2_end

label part_2_end:
    show amelia_reflecting_dorm_evening_full
    with dissolve
    n "Back in her dorm room, Amelia reflects on the day's events and interactions."

    if AA >= 3 and MH >= 3:
        hide amelia_reflecting_dorm_evening_full
        show black
        window hide

        show amelia_pensive_dorm_night_full
        a "Balancing academic pursuits with supporting friends through their struggles... It's not always easy, but it feels important."
        hide amelia_reflecting_dorm_evening_full
        show black
        window hide

    elif AA >= 3:
        hide amelia_reflecting_dorm_evening_full
        show black
        window hide

        show amelia_studying_dorm_night_full
        a "I'm learning so much, both in and out of the classroom. But I wonder if I'm doing enough to be there for the people in my life."
        hide amelia_studying_dorm_night_full
        show black
        window hide

    elif MH >= 3:
        hide amelia_reflecting_dorm_evening_full
        show black
        window hide

        show amelia_calling_dorm_night_full
        a "Being a supportive friend and advocating for mental health... It's a crucial part of my journey. I just need to remember to take care of myself too."
        hide amelia_calling_dorm_night_full
        show black
        window hide

    else:
        hide amelia_reflecting_dorm_evening_full
        show black
        window hide

        show amelia_tired_dorm_night_full
        a "It's been a challenging day, navigating all these different aspects of university life. But I know each experience is a chance to learn and grow."
        hide amelia_tired_dorm_night_full
        show black
        window hide

    if lucas_dream_project > 0:
        n "As Amelia gets ready for bed, she receives a text from Lucas."
        show black
        window hide

        show lucas_text_workshop_plans_full
        lucas_text "Hey Amelia! I've been brainstorming some more ideas for the Jungian workshop. Can't wait to discuss them with you!"
        hide lucas_text_workshop_plans_full
        show black
        window hide

        show amelia_smiling_dorm_night_full
        a "(Lucas's enthusiasm is contagious. It's energizing to collaborate with friends who share my passions.)"
        a "(Tomorrow is a new day, with new opportunities to make a difference. In my studies, in my friendships, in my own growth.)"
        n "Amelia falls asleep, feeling grateful for the challenges and the support that university life brings."
        hide amelia_smiling_dorm_night_full
        show black
        window hide

    jump chapter_3_part_3

label chapter_3_part_3:
    show amelia_waking_dorm_morning_full
    with dissolve
    if meet_sarah > 0:
        n "The next morning, Amelia wakes up early, her first thought being to check on Sarah."

        menu:
            "Call Sarah":
                hide amelia_waking_dorm_morning_full
                show black
                window hide

                jump call_sarah_morning
            
            "Send a text message":
                hide amelia_waking_dorm_morning_full
                show black
                window hide

                jump text_sarah_morning
    else: 
        n "The next morning, Amelia wakes up early and decided to get something to eat in the cafeteria"
        hide amelia_waking_dorm_morning_full
        show black
        window hide

        jump breakfast_with_liz

label call_sarah_morning:
    show amelia_on_phone_concerned_full
    n "Amelia dials Sarah's number, her heart racing as she waits for her to pick up."
    sarah "Hello?"
    a "Sarah, it's Amelia. I wanted to check in on you. How are you feeling today?"
    
    if MH >= 5:
        hide amelia_on_phone_concerned_full
        show black
        window hide

        show sarah_on_phone_tired_full
        sarah "Amelia... I'm okay. Tired, but okay. I called the hotline last night, like you suggested."
        a "I'm so glad to hear that, Sarah. That was a brave thing to do. How did it go?"
        sarah "It was hard, but it helped. They listened, and they gave me some resources for follow-up care. I think I'm going to make an appointment with the counseling center."
        a "That's wonderful, Sarah. I'm so proud of you for taking these steps. Remember, I'm here for you too, whenever you need me."
        sarah "Thank you, Amelia. Your support means more than you know."
        $ MH += 1
        $ SI += 1
        hide sarah_on_phone_tired_full
        show black
        window hide

    else:
        hide amelia_on_phone_concerned_full
        show black
        window hide

        show sarah_on_phone_distant_full
        sarah "I'm... I'm alive. That's about all I can say right now."
        a "Sarah, I'm so sorry. I should have done more to help you last night."
        sarah "It's not your fault, Amelia. I'm just... I'm not ready to talk about it yet."
        a "I understand. But please, don't shut me out. I'm here for you, whenever you're ready."
        sarah "...I know. Thank you, Amelia. I just need some time."
        $ MH += 1
        hide sarah_on_phone_distant_full
        show black
        window hide

    jump breakfast_with_liz

label text_sarah_morning:
    show amelia_texting_concerned_full
    n "Amelia composes a text to Sarah:"
    a "Good morning, Sarah. I just wanted to check in and see how you're doing today. I'm here if you need anything."
    n "She hits send and waits anxiously for a response."
    
    if renpy.random.randint(1,10) <= 3:
        n "Hours pass with no reply from Sarah. Amelia grows increasingly worried."
        a "(What if something happened to her? What if she's not okay?)"
        n "Just as Amelia is about to call the emergency services, her phone buzzes."
        hide amelia_texting_concerned_full
        show black
        window hide

        show sarah_text_reassuring_full
        sarah "Hey Amelia, sorry for the late reply. I was at an appointment with the counseling center. I'm okay. Thank you for checking in."
        a "Sarah, I'm so relieved to hear from you. And I'm proud of you for seeking help. That's a big step."
        sarah "It wasn't easy, but I knew I needed to do something. I'm glad I did."
        a "I'm here for you, Sarah. Always. Let's catch up in person soon, okay?"
        sarah "I'd like that. Thanks, Amelia."
        $ MH += 2
        hide sarah_text_reassuring_full
        show black
        window hide

    else:
        hide amelia_texting_concerned_full
        show black
        window hide

        show sarah_text_short_full
        sarah "I'm hanging in there. Thanks for checking in."
        a "Of course, Sarah. I'm always here if you need to talk."
        sarah "I know. I appreciate it."
        a "Let's grab coffee soon, okay? I'd love to see you."
        sarah "Sure, let's do that. I'll text you."
        $ SI += 1
        hide sarah_text_short_full
        show black
        window hide
    
    jump breakfast_with_liz

label breakfast_with_liz:
    show amelia_liz_breakfast_cafeteria_full
    with dissolve
    if meet_sarah > 0:
        n "Amelia heads to the cafeteria for breakfast, her mind still preoccupied with thoughts of Sarah."
        hide amelia_liz_breakfast_cafeteria_full
        show black
        window hide

        show liz_neutral_cafeteria_full
        l "Morning, Amelia. You look tired. Late night studying?"
        a "Not exactly. I was up late worrying about Sarah. She's going through a tough time."
        hide liz_neutral_cafeteria_full
        show black
        window hide

        show liz_concerned_cafeteria_full
        l "Oh no, I'm sorry to hear that. Is she okay?"
        show black
        window hide
        
        menu:
            "Share details about Sarah's struggles":
                $ SI += 1
                hide liz_concerned_cafeteria_full
                show black
                window hide

                jump share_sarah_details
            
            "Keep the details private":
                $ MC += 1
                hide liz_concerned_cafeteria_full
                show black
                window hide

                jump keep_sarah_private
    else:
        hide amelia_liz_breakfast_cafeteria_full
        show black
        window hide

        show liz_neutral_cafeteria_full
        n "Amelia heads to the cafeteria for breakfast"
        l "Morning, Amelia. You look tired. Late night studying?"
        a "You can say that twice, so many new things to take in."
        if OK >= 1:
            hide liz_neutral_cafeteria_full
            show black
            window hide

            jump occult_studies_intro

        else:
            n "Amelia gets a strange feeling that this day could really have turned out differently"
            n "She decided to spend the day studying and before she knows it the whole day flew by"
            show black
            window hide

            jump chapter_3_end


label share_sarah_details:
    show amelia_concerned_liz_cafeteria_full
    a "She's struggling with depression and had a bit of a crisis last night. I'm really worried about her."
    l "That's so heavy, Amelia. I'm glad she has you to support her. Have you suggested she talk to a counselor?"
    a "I have, and she's actually taking that step. I'm proud of her, but I know the road ahead won't be easy."
    l "No, it won't. But with friends like you by her side, I'm sure she'll get through this."
    a "Thanks, Liz. I hope so. I just wish I could do more."
    hide amelia_concerned_liz_cafeteria_full
    show black
    window hide

    show liz_supportive_liz_cafeteria_full
    l "You're doing a lot just by being there for her, Amelia. Don't underestimate the value of that."
    a "I guess you're right. Thanks, Liz."
    $ SI += 1
    hide liz_supportive_liz_cafeteria_full
    show black
    window hide

    jump occult_studies_intro

label keep_sarah_private:
    show amelia_reserved_liz_cafeteria_full
    a "She's just going through some personal stuff. I don't want to share the details without her permission."
    l "Of course, I understand. It's good that you respect her privacy."
    a "I just wish I knew how to help her more."
    hide amelia_reserved_liz_cafeteria_full
    show black
    window hide

    show liz_supportive_liz_cafeteria_full
    l "Sometimes, just being there is the most helpful thing you can do. Let her know you're there for her, but don't push."
    a "That's good advice. Thanks, Liz."
    l "Anytime, Amelia. And hey, make sure you're taking care of yourself too, okay?"
    a "I will. Thanks for looking out for me."
    $ MC += 1
    hide liz_supportive_liz_cafeteria_full
    show black
    window hide

    jump occult_studies_intro

label occult_studies_intro:
    show amelia_maya_library_full
    with dissolve
    n "Later that day, Amelia is in the library studying when she overhears a conversation that piques her interest."
    hide amelia_maya_library_full
    show black
    window hide

    show maya_excited_library_full
    m "I'm telling you, there's so much more to reality than what we can see. The occult studies reveal hidden truths about the nature of the universe."
    n "Intrigued, Amelia turns to see Maya engaged in an animated discussion with another student."
    
    menu:
        "Approach Maya and ask about occult studies":
            $ OK += 1
            hide maya_excited_library_full
            show black
            window hide

            jump ask_maya_occult
        
        "Continue studying":
            hide maya_excited_library_full
            show black
            window hide

            jump continue_studying

label ask_maya_occult:
    stop music fadeout 2.0
    play music inkpot_gods fadein 2.0 volume 0.3

    show amelia_curious_maya_library_full
    a "Hey Maya, I couldn't help but overhear. What are these occult studies you're talking about?"
    hide amelia_curious_maya_library_full
    show black
    window hide

    show maya_enthusiastic_maya_library_full
    m "Oh, Amelia! It's fascinating stuff. Occult studies delve into the mystical, the esoteric, the hidden knowledge of the ages."
    a "That sounds really intriguing. Where do you even start with something like that?"
    m "There are a lot of entry points. Ancient texts, secret societies, spiritual practices... It's a vast field."
    
    if renpy.random.randint(1,10) <= 2:
        hide maya_enthusiastic_maya_library_full
        show black
        window hide

        show maya_secretive_maya_library_full
        m "Actually, if you're really interested, I know of a place where you can learn more. But it's not exactly... public."
        a "What do you mean?"
        m "There's a secret society on campus, dedicated to the study of the occult. They're very selective about who they let in, but I could put in a word for you."
        a "A secret society? That's... wow. I don't know, Maya. That sounds a bit intense."
        m "I understand. It's not for everyone. But if you change your mind, the offer stands. In the meantime, I can recommend some books if you want to explore on your own."
        a "I'd appreciate that. Thanks, Maya."
        n "Maya writes down a list of titles and hands it to Amelia."
        $ OK += 2

        show black
        window hide

    else:
        m "If you're interested, I can recommend some good introductory texts. There's a great section here in the library on esoteric philosophy."
        a "That would be great, Maya. I'd love to learn more."
        m "Wonderful! I'm always happy to guide a fellow seeker. Let's see, you should start with..."
        n "Maya proceeds to give Amelia a crash course in occult studies, recommending books and sharing her own insights."
        a "This is all so fascinating, Maya. Thank you for sharing your knowledge with me."
        m "Of course, Amelia. I sense a kindred spirit in you. If you ever want to discuss these topics further, my door is always open."
        $ OK += 1
        hide maya_enthusiastic_maya_library_full
        show black
        window hide

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
    show amelia_reflecting_dorm_evening_full
    with dissolve
    n "That evening, as Amelia is reflecting on her day, her thoughts keep returning to Sarah and the conversation with Maya."
    a "(So much has happened in such a short time. Sarah's struggles, my own academic pressures, and now this whole new world of occult knowledge...)"
    
    if (OK >= 3 and renpy.random.randint(1,10) <= 3):
        hide amelia_reflecting_dorm_evening_full
        show black
        window hide

        show amelia_pensive_dorm_full
        a "(I can't stop thinking about what Maya said about that secret society. It's tempting... but also a little scary.)"
        n "As if on cue, Amelia's phone buzzes with a message from an unknown number."
        hide amelia_pensive_dorm_full
        show black
        window hide

        show secret_society_text_full
        n "Unknown: We hear you're interested in the deeper mysteries. If you seek true knowledge, come to the old chapel at midnight. Come alone."
        a "(What the... how did they get my number? Is this from the secret society Maya mentioned?)"
        n "Amelia's heart races as she considers the implications."
        menu:
            "Go to the old chapel at midnight":
                hide secret_society_text_full
                show black
                window hide

                jump secret_society_meeting

            "Ignore the message":

                a "(No, this is too weird. I'm not getting involved in this.)"
                n "Amelia deletes the message and tries to put it out of her mind."
                hide secret_society_text_full
                show black
                window hide

                jump late_night_worries
    else:
        n "Even with all the challenges and mysteries, Amelia feels a sense of growth and purpose."
        a "(I'm learning so much, about the world and about myself. I feel like I'm exactly where I'm meant to be.)"
        "With a sense of contentment, she settles into bed for the night."
        hide amelia_reflecting_dorm_evening_full
        show black
        window hide

        jump late_night_worries

label secret_society_meeting:
    $ OK += 2

    show amelia_old_chapel_night_full
    with dissolve
    n "Against her better judgment, Amelia finds herself sneaking out of her dorm room at midnight and heading towards the old chapel."
    a "(What am I doing? This is crazy. But I can't deny I'm curious...)"
    hide amelia_old_chapel_night_full
    show black
    window hide

    show amelia_entering_chapel_full
    with dissolve
    n "She enters the candlelit chapel, her footsteps echoing in the eerie silence."
    hide amelia_entering_chapel_full
    show black
    window hide

    show hooded_figure_chapel_full
    n "Hooded Figure: Welcome, seeker. We've been expecting you."
    a "Who are you? What is this place?"
    n "Hooded Figure: We are the guardians of ancient wisdom, the seekers of hidden truths. And this is where your true education begins, if you're brave enough to embark on the journey."
    a "I... I don't know. This is all so sudden."
    n "Hooded Figure: Knowledge is not for the faint of heart, Amelia. If you wish to uncover the secrets of the universe, you must be willing to step into the unknown."
    
    if renpy.random.randint(1,10) <= 4:
        n "Hooded Figure: But perhaps you are not ready. Perhaps you should return to your safe, ordinary life."
        a "No! I... I want to learn. I'm ready."
        n "A smile is just visible beneath the figure's hood."
        n "Hooded Figure: Very well. Your initiation begins now."
        hide hooded_figure_chapel_full
        show black
        window hide

        show amelia_initiation_chapel_full
        with dissolve
        n "What follows is a night of strange rituals, cryptic teachings, and esoteric knowledge that Amelia can barely comprehend."
        $ OK += 3
        hide amelia_initiation_chapel_full
        show black
        window hide

    else:
        a "I... I'm sorry. I don't think I'm ready for this. It's all too much."
        n "Hooded Figure: As you wish. The door is always open, should you change your mind."
        n "Amelia hurries out of the chapel, her heart pounding."
        $ OK += 1
        hide hooded_figure_chapel_full
        show black
        window hide
    
    jump late_night_worries

label late_night_worries:
    show amelia_dorm_room_night_dark_full
    with dissolve
    n "As Amelia lies in bed, her mind races with the events of the day and the challenges ahead."
    a "(Sarah, my studies, the secret society... It's all so overwhelming. How am I supposed to handle all of this?)"
    
    if renpy.random.randint(1,10) <= 3:
        n "Suddenly, Amelia's phone rings. It's Sarah."

        hide amelia_dorm_room_night_dark_full
        show black
        window hide

        show amelia_on_phone_night_full
        a "Sarah? Is everything okay?"
        hide amelia_on_phone_night_full
        show black
        window hide

        show sarah_on_phone_crying_full
        s "Amelia... I'm sorry. I know it's late. I just... I had a nightmare. I needed to hear your voice."
        a "It's okay, Sarah. I'm here. Do you want to talk about it?"
        n "Amelia spends the next hour on the phone with Sarah, comforting her and reassuring her until she's calm enough to sleep."
        $ MH += 2
        hide sarah_on_phone_crying_full
        show black
        window hide

    else:
        n "Despite her worries, exhaustion eventually overtakes Amelia, and she falls into a restless sleep."
        n "Her dreams are filled with strange symbols, shadowy figures, and a sense of foreboding that lingers even after she wakes."
        hide amelia_dorm_room_night_dark_full
        show black
        window hide

    jump chapter_3_end

label chapter_3_end:
    show amelia_waking_dorm_morning_light_full
    with dissolve
    n "The next morning, Amelia wakes feeling drained but determined."
    
    if (MH >= 7 and OK >= 5):
        n "Despite the challenges and mysteries she's facing, Amelia feels a sense of purpose and growth."
        a "(I'm learning so much, about myself and the world around me. I'm discovering strength I didn't know I had.)"
        a "(I don't know what the future holds, but I know I'm ready to face it, for Sarah's sake and for my own.)"
        hide amelia_waking_dorm_morning_light_full
        show black
        window hide

    else:
        n "The weight of her responsibilities and the uncertainty of the path ahead weigh heavily on Amelia."
        a "(I don't know if I'm strong enough for this. But I have to try.)"
        n "With a deep breath, Amelia steels herself for whatever comes next."
        hide amelia_waking_dorm_morning_light_full
        show black
        window hide

    n "As she prepares for the day ahead, she can't shake the feeling that everything is about to change."
    a "(I have a feeling this is just the beginning. The real challenges are still to come.)"
    n "With a mix of anticipation and trepidation, Amelia steps out into the uncertain future."
    n "Chapter 4 is still in the works"
    n "So here is what you can do now:"
    menu:
        "Go back to main menu":
            hide amelia_waking_dorm_morning_light_full
            show black
            window hide

            return
        
        "Checkout the Occult hidden ending":
            hide amelia_waking_dorm_morning_light_full
            show black
            window hide

            jump chapter_12_enlightenment
