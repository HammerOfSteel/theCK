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
