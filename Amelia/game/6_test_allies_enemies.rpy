label chapter_6_part_1:
    show amelia_dorm_morning
    with dissolve

    "Amelia wakes up to a crisp morning, feeling a mixture of anticipation and anxiety. Today, she knows, will bring new challenges."

    menu:
        "Prepare for a major project":
            $ AA += 1
            jump major_project

        "Meet with friends to relax and support each other":
            $ SI += 1
            jump friends_support

        "Focus on personal growth and occult studies":
            $ SD += 1
            jump personal_growth_2

label major_project:
    show amelia_studying_library
    with dissolve

    "Amelia heads to the library, determined to make significant progress on her major project."

    show sophia_approaches_library
    with dissolve

    "As she's working, her academic rival, Sophia, approaches her desk."

    sophia "Hey, Amelia. I know we don't always see eye to eye, but I'm struggling with this part of the project. Could you help me out?"

    menu:
        "Help Sophia (+AA, +MC)":
            $ AA += 1
            $ MC += 1
            jump help_sophia

        "Focus on your own work (-SI, +AA)":
            $ SI -= 1
            $ AA += 1
            jump focus_on_work

label help_sophia:
    show amelia_sophia_working
    with dissolve

    "Amelia decides to help Sophia, putting aside her own work for the moment."

    a "Sure, Sophia. Let's figure this out together."

    "They spend the next few hours working through the complexities of the project."

    show sophia_smiling_library
    with dissolve

    sophia "Thanks, Amelia. I really appreciate it. Maybe we're not so different after all."

    "Amelia feels a sense of accomplishment and a surprising camaraderie with Sophia."

    jump academic_pressure

label focus_on_work:
    show amelia_focused_library
    with dissolve

    "Amelia decides to focus on her own project, determined to meet her deadlines."

    a "(I need to prioritize my own work right now. I can't afford any distractions.)"

    "She immerses herself in her studies, making significant progress."

    jump academic_pressure

label academic_pressure:
    show amelia_dorm_afternoon
    with dissolve

    "Back in her dorm room, Amelia takes a short break, feeling the weight of academic pressure."

    menu:
        "Take a walk to clear your mind (+MH)":
            $ MH += 1
            jump walk_campus_2

        "Push through and continue working (+AA)":
            $ AA += 1
            jump continue_working

label walk_campus_2:
    show amelia_walking_campus
    with dissolve

    "Amelia decides to take a walk around campus to clear her mind."

    show amelia_at_hoe_park
    with dissolve

    "She finds herself at Hoe Park, taking in the fresh air and beautiful scenery."

    menu:
        "Run into Tasha (+MC)":
            $ MC += 1
            jump run_into_tasha_2

        "Meet Michael and discuss activism (+MC, +SI)":
            $ MC += 1
            $ SI += 1
            jump meet_michael_2

label run_into_tasha_2:
    show tasha_confronting
    with dissolve

    "While walking through the park, Amelia unexpectedly runs into Tasha."

    tasha "Well, if it isn't Amelia. Still playing the goody-two-shoes, I see."

    menu:
        "Stand up to Tasha (+MC)":
            $ MC += 1
            jump stand_up_tasha_2

        "Try to defuse the situation (+SI)":
            $ SI += 1
            jump defuse_tasha_2

label stand_up_tasha_2:
    show amelia_determined_tasha
    with dissolve

    a "I'm just trying to make the most of my time here, Tasha. There's nothing wrong with that."

    show tasha_surprised
    with dissolve

    tasha "Hmph. Well, don't get in my way."

    "Tasha walks away, and Amelia feels a sense of accomplishment for standing up for herself."

    jump walk_continued_2

label defuse_tasha_2:
    show amelia_calm_tasha
    with dissolve

    a "I'm not looking for trouble, Tasha. Let's just go our separate ways."

    show tasha_indifferent
    with dissolve

    tasha "Whatever."

    "Tasha leaves, and Amelia continues her walk, feeling relieved."

    jump walk_continued_2

label meet_michael_2:
    show michael_introducing
    with dissolve

    "While walking through the park, Amelia meets Michael, who is handing out flyers."

    michael "Hey, Amelia. We're organizing a protest against the university's investment in fossil fuels. Would you be interested in joining us?"

    menu:
        "Join the protest (+MC, +SI)":
            $ MC += 1
            $ SI += 1
            jump join_protest_2

        "Decline politely (+MC)":
            $ MC += 1
            jump decline_protest_2

label join_protest_2:
    show amelia_michael_protest
    with dissolve

    a "Sure, Michael. I think it's important to take a stand on these issues."

    michael "Great! We're meeting at the Student Union tomorrow. See you there!"

    "Amelia feels a sense of purpose as she agrees to join the protest."

    jump walk_continued_2

label decline_protest_2:
    show amelia_michael_decline
    with dissolve

    a "I support the cause, but I'm really busy with my studies right now. Maybe next time."

    michael "No problem. Thanks for considering it."

    "Amelia feels good about being honest while also standing up for her values."

    jump walk_continued_2

label walk_continued_2:
    show amelia_walking_park
    with dissolve

    "Amelia continues her walk, feeling refreshed and more balanced."

    jump chapter_6_part_1_end

label friends_support:
    show student_union
    with dissolve

    "Amelia decides to spend time with her friends at the Student Union."

    show amelia_lucas_zara_union
    with dissolve

    "She finds Lucas and Zara sitting together."

    lucas "Hey, Amelia! We're just planning our weekend. Want to join us?"

    menu:
        "Make weekend plans (+SI)":
            $ SI += 1
            jump weekend_plans_2

        "Talk to Lucas about his challenges (+SI, +MC)":
            $ SI += 1
            $ MC += 1
            jump talk_lucas_challenges

label weekend_plans_2:
    show amelia_smiling_union
    with dissolve

    a "Absolutely! What do you have in mind?"

    show zara_thoughtful_union
    with dissolve

    zara "We were thinking of going to the Barbican. There's a new art exhibit and some great cafes to check out."

    a "That sounds perfect. I'm in!"

    "They finalize their plans and enjoy the rest of the afternoon together."

    jump friendship_strengthening_2

label talk_lucas_challenges:
    show amelia_concerned_lucas
    with dissolve

    a "Lucas, how have you been holding up? You seem a bit stressed lately."

    show lucas_sighing_union
    with dissolve

    lucas "It's been tough. Between classes and my part-time job, I feel like I'm constantly running on empty."

    menu:
        "Offer to help him with his studies (+SI, +MH)":
            $ SI += 1
            $ MH += 1
            jump help_lucas_studies

        "Suggest he take a break (+MH)":
            $ MH += 1
            jump suggest_break

label help_lucas_studies:
    show amelia_supportive_lucas
    with dissolve

    a "Maybe we can study together? I could help you with some of the material."

    show lucas_smiling_union
    with dissolve

    lucas "Thanks, Amelia. That would be great. I could really use the help."

    a "We'll get through this together."

    "Amelia feels closer to Lucas as they plan to support each other academically."

    jump friendship_strengthening_2

label suggest_break:
    show amelia_caring_lucas
    with dissolve

    a "You should take a break, Lucas. Maybe we can do something fun this weekend to help you relax."

    show lucas_nodding_union
    with dissolve

    lucas "You're right. I need to recharge. Let's plan something fun."

    "Amelia feels good about encouraging Lucas to take care of himself."

    jump friendship_strengthening_2

label friendship_strengthening_2:
    show amelia_dorm_evening
    with dissolve

    "That evening, Amelia reflects on her day with a sense of fulfillment."

    a "(I'm really glad I took the time to connect with Lucas and Zara. Our friendship is stronger than ever.)"

    "She goes to bed feeling more balanced and ready for whatever comes next."

    jump chapter_6_part_1_end

label personal_growth_2:
    show amelia_library
    with dissolve

    "Amelia decides to focus on her personal growth by studying esoteric texts in the library."

    show amelia_studying_library
    with dissolve

    "She finds a quiet corner and immerses herself in the ancient knowledge."

    menu:
        "Study ancient philosophies (+SD)":
            $ SD += 1
            jump study_philosophies_2

        "Research occult practices (+OK, +SD)":
            $ OK += 1
            $ SD += 1
            jump research_occult_2

label study_philosophies_2:
    show amelia_reading_book
    with dissolve

    "Amelia delves into ancient philosophies, exploring different perspectives on life and the universe."

    a "(These ideas are so profound. They really make me think about my own beliefs and values.)"

    "She gains new insights and feels more connected to her personal growth journey."

    jump personal_growth_2_continued

label research_occult_2:
    show amelia_researching_occult
    with dissolve

    "Amelia researches various occult practices, fascinated by the hidden knowledge and rituals."

    a "(There's so much to learn about the unseen world. This is both exciting and challenging.)"

    "Her studies deepen her understanding of the occult and enhance her personal growth."

    jump personal_growth_2_continued

label personal_growth_2_continued:
    show amelia_dorm_evening
    with dissolve

    "Back in her dorm room, Amelia reflects on what she learned."

    a "(Today was a good day. I feel more grounded and enlightened.)"

    "She feels a sense of accomplishment and peace as she prepares for bed."

    jump chapter_6_part_1_end

label chapter_6_part_1_end:
    show amelia_dorm_night
    with dissolve

    "As Amelia settles in for the night, she feels a renewed sense of purpose and balance."

    a "Whatever challenges come my way, I'm ready. This is just the beginning of my journey."

    "Her dreams are filled with symbols of growth and transformation, hinting at the profound changes ahead."

    jump chapter_6_part_2

label chapter_6_part_2:
    show amelia_dorm_morning
    with dissolve

    "Amelia wakes up feeling a mixture of excitement and apprehension. Today will bring new tests and opportunities."

    menu:
        "Focus on academic challenges":
            $ AA += 1
            jump academic_challenges

        "Support Sarah through her crisis":
            $ MH += 1
            $ SI += 1
            jump support_sarah

        "Engage in social activism with Michael":
            $ MC += 1
            jump social_activism

label academic_challenges:
    show amelia_classroom
    with dissolve

    "Amelia heads to her challenging ethics class, knowing that today’s lecture will be critical for her major project."

    show prof_hawthorne_teaching
    with dissolve

    "Prof. Hawthorne: Today, we'll be discussing the ethical implications of psychological research. This is a complex and vital topic."

    menu:
        "Participate actively in class":
            $ AA += 1
            jump participate_class

        "Take detailed notes":
            $ AA += 1
            jump take_notes_class

label participate_class:
    show amelia_raising_hand
    with dissolve

    "Amelia raises her hand and engages actively in the discussion, sharing her insights and asking thoughtful questions."

    show prof_hawthorne_impressed
    with dissolve

    prof_hawthorne "Excellent points, Amelia. Your engagement is commendable."

    "After class, Prof. Hawthorne asks to speak with Amelia."

    show amelia_prof_hawthorne_office
    with dissolve

    prof_hawthorne "Amelia, I've been impressed with your contributions. How would you like to assist me with a new research project on ethical psychology?"

    menu:
        "Accept eagerly":
            $ AA += 1
            jump accept_research_project

        "Ask for more details":
            $ MC += 1
            jump ask_details_research_project

label accept_research_project:
    show amelia_excited
    with dissolve

    a "I’d love to, Professor! This sounds like an incredible opportunity."

    prof_hawthorne "Excellent. We'll start meeting next week. Prepare by reviewing these materials."

    jump academic_pressure_continued_2

label ask_details_research_project:
    show amelia_curious
    with dissolve

    a "Can you tell me more about the project? I want to ensure I can fully commit."

    prof_hawthorne "We'll be exploring the ethical dimensions of new psychological therapies. It will involve extensive reading, discussion, and some experimental design."

    menu:
        "Accept after consideration":
            $ AA += 1
            $ MC += 1
            jump accept_after_consideration

        "Politely decline":
            $ MC += 1
            jump politely_decline

label accept_after_consideration:
    show amelia_nodding
    with dissolve

    a "It sounds challenging but rewarding. I’m in."

    prof_hawthorne "Glad to hear it. I'll send you the initial reading list."

    jump academic_pressure_continued_2

label politely_decline:
    show amelia_declining
    with dissolve

    a "I appreciate the offer, but I’m not sure I can commit to that level right now."

    prof_hawthorne "I understand. If you change your mind, the offer stands."

    jump academic_pressure_continued_2

label take_notes_class:
    show amelia_writing_notes
    with dissolve

    "Amelia takes meticulous notes during the lecture, absorbing the complexities of the subject."

    a "(This will be crucial for my project. I need to make sure I understand every aspect.)"

    "After class, she spends extra time in the library, deepening her understanding."

    jump academic_pressure_continued_2

label academic_pressure_continued_2:
    show amelia_library
    with dissolve

    "In the library, Amelia encounters Sophia again, who seems troubled."

    show sophia_approaches_library
    with dissolve

    sophia "Amelia, can I talk to you for a moment?"

    menu:
        "Agree to help Sophia (+MC)":
            $ MC += 1
            jump help_sophia_library

        "Focus on your own studies (-SI, +AA)":
            $ SI -= 1
            $ AA += 1
            jump focus_studies_library

label help_sophia_library:
    show amelia_sophia_talking
    with dissolve

    "Amelia agrees to help Sophia, putting her own work on hold."

    a "Of course, Sophia. What’s going on?"

    show sophia_upset
    with dissolve

    sophia "I’ve been accused of plagiarism. I didn’t do it, but I don’t know how to prove it."

    menu:
        "Help Sophia prove her innocence (+MC, +SI)":
            $ MC += 1
            $ SI += 1
            jump prove_innocence

        "Advise Sophia to speak with the professor directly (+MC)":
            $ MC += 1
            jump speak_professor_directly

label prove_innocence:
    show amelia_sophia_working_together
    with dissolve

    "Amelia and Sophia work together, reviewing all of Sophia’s notes and drafts to find evidence that can clear her name."

    a "Look, this timestamped draft shows you wrote this section long before the other student submitted their work."

    sophia "You’re right! Thank you, Amelia. I’ll take this to the professor right away."

    jump academic_challenges_continued

label speak_professor_directly:
    show amelia_sophia_talking
    with dissolve

    a "You need to talk to the professor directly. Explain your side and show your drafts."

    show sophia_nodding
    with dissolve

    sophia "You’re right. I’ll do that. Thanks, Amelia."

    jump academic_challenges_continued

label focus_studies_library:
    show amelia_studying_focused
    with dissolve

    "Amelia decides to focus on her own studies, pushing through the intense workload."

    a "(I have to stay focused if I want to succeed.)"

    jump academic_challenges_continued

label academic_challenges_continued:
    show amelia_dorm_evening
    with dissolve

    "That evening, Amelia feels the strain of the day but also a sense of accomplishment."

    a "(Today was tough, but I made progress. I just need to keep going.)"

    jump chapter_6_part_2_end

label support_sarah:
    show amelia_sarah_dorm
    with dissolve

    "Amelia goes to check on Sarah, who has been struggling more than usual."

    show sarah_distressed
    with dissolve

    sarah "Amelia, I don’t know how much longer I can keep going like this. Everything feels so overwhelming."

    menu:
        "Offer to help Sarah seek professional support (+MH, +SI)":
            $ MH += 1
            $ SI += 1
            jump seek_professional_support

        "Spend time with Sarah to comfort her (+MH, -AA)":
            $ MH += 1
            $ AA -= 1
            jump spend_time_comfort

label seek_professional_support:
    show amelia_sarah_talking
    with dissolve

    a "Sarah, I think it’s time to seek professional help. I can go with you to the counseling center."

    show sarah_nodding
    with dissolve

    sarah "I think you’re right. I can’t do this alone anymore. Will you really come with me?"

    a "Of course. Let’s go."

    show counseling_center
    with dissolve

    "They head to the counseling center together, where Sarah speaks to a therapist for the first time."

    jump support_sarah_continued

label spend_time_comfort:
    show amelia_sarah_hugging
    with dissolve

    "Amelia decides to spend the afternoon with Sarah, providing comfort and a listening ear."

    a "We can get through this together, Sarah. You’re not alone."

    show sarah_smiling
    with dissolve

    sarah "Thank you, Amelia. You don’t know how much this means to me."

    "They spend the evening talking and watching movies, giving Sarah a much-needed break."

    jump support_sarah_continued

label support_sarah_continued:
    show amelia_dorm_evening
    with dissolve

    "That night, Amelia reflects on how important it is to support her friends, even if it means sacrificing some of her own time."

    a "(Sarah needs me, and I need to be there for her. This is what friendship is all about.)"

    jump chapter_6_part_2_end

label social_activism:
    show student_union_meeting
    with dissolve

    "Amelia joins Michael at the Student Union for a meeting about the upcoming protest."

    show michael_speaking
    with dissolve

    michael "Thanks for coming, everyone. Today, we’re finalizing our plans for the protest against the university’s investments in fossil fuels."

    menu:
        "Take an active role in organizing (+MC, +SI)":
            $ MC += 1
            $ SI += 1
            jump active_organizer

        "Participate quietly and support (+SI)":
            $ SI += 1
            jump quiet_support

label active_organizer:
    show amelia_speaking_meeting
    with dissolve

    "Amelia takes an active role, helping to organize logistics and rallying other students to join the cause."

    a "We need to make sure our voices are heard. Let’s coordinate our signs and chants to make the biggest impact."

    show michael_impressed
    with dissolve

    michael "Great leadership, Amelia. This is exactly what we need."

    jump social_activism_continued

label quiet_support:
    show amelia_listening_meeting
    with dissolve

    "Amelia participates quietly, offering her support and following the lead of more experienced activists."

    a "(I believe in this cause, but I still have a lot to learn about activism.)"

    show michael_smiling
    with dissolve

    michael "Every bit of support helps. Thank you for being here, Amelia."

    jump social_activism_continued

label social_activism_continued:
    show protest_day
    with dissolve

    "The day of the protest arrives, and Amelia joins the crowd of students in front of the administration building."

    show amelia_protesting
    with dissolve

    "She feels a surge of adrenaline as they chant and hold their signs high, demanding change."

    show university_admin_confronts
    with dissolve

    "University administrators come out to confront the protesters, and tensions rise."

    menu:
        "Stand up to the administrators (+MC)":
            $ MC += 1
            jump stand_up_admins

        "Try to de-escalate the situation (+SI)":
            $ SI += 1
            jump deescalate_situation

label stand_up_admins:
    show amelia_confronts_admin
    with dissolve

    "Amelia steps forward and confronts the administrators."

    a "We have a right to be heard! The university’s investments are harming our future, and we demand accountability!"

    show admin_angry
    with dissolve

    admin "This is not the appropriate venue for such discussions. You are disrupting the campus."

    show michael_supports_amelia
    with dissolve

    michael "We’re not going anywhere until we’re heard."

    "The protest continues, and eventually, the administrators agree to meet with student representatives."

    jump social_activism_conclusion

label deescalate_situation:
    show amelia_calming_protesters
    with dissolve

    "Amelia steps in to try to calm the situation."

    a "Let’s keep this peaceful. We’re here to make a point, not to create chaos."

    show michael_agrees
    with dissolve

    michael "Amelia’s right. Let’s show them that we can be both passionate and respectful."

    "The protest remains peaceful, and the administrators agree to meet with student representatives."

    jump social_activism_conclusion

label social_activism_conclusion:
    show amelia_reflecting_protest
    with dissolve

    "After the protest, Amelia feels a sense of accomplishment and camaraderie with her fellow activists."

    a "(We made our voices heard today. This is just the beginning of making real change.)"

    "She and Michael discuss plans for future actions, solidifying their commitment to the cause."

    jump chapter_6_part_2_end

label chapter_6_part_2_end:
    show amelia_dorm_night
    with dissolve

    "As the day comes to a close, Amelia reflects on the challenges and triumphs she faced."

    a "Every day brings new tests, but I’m growing stronger with each one. I’m ready for whatever comes next."

    "With a sense of determination, she falls asleep, her dreams filled with the promise of tomorrow."

    jump chapter_6_part_3

label chapter_6_part_3:
    show amelia_dorm_morning
    with dissolve

    "Amelia wakes up with a sense of purpose. Today will bring further trials and opportunities for growth."

    menu:
        "Focus on a major academic project":
            $ AA += 1
            jump major_academic_project

        "Support Lucas through a personal crisis":
            $ SI += 1
            jump support_lucas

        "Confront Tasha about her bullying":
            $ MC += 1
            $ SI += 1
            jump confront_tasha

        "Engage in a high-stakes occult ritual (if OK is high)":
            $ OK += 1
            jump high_stakes_ritual

label major_academic_project:
    show amelia_library
    with dissolve

    "Amelia heads to the library to work on her major academic project, determined to excel."

    show amelia_studying_hard
    with dissolve

    "She dives deep into her research, losing track of time as she analyzes data and compiles her findings."

    menu:
        "Seek help from a mentor":
            $ AA += 1
            jump seek_help_mentor

        "Collaborate with a peer":
            $ SI += 1
            jump collaborate_peer

        "Work independently":
            $ AA += 1
            jump work_independently

label seek_help_mentor:
    show amelia_prof_hawthorne_office
    with dissolve

    "Amelia decides to seek guidance from Prof. Hawthorne, knowing his insights will be invaluable."

    prof_hawthorne "Amelia, I'm glad you're here. Let's go over your project and see how we can refine it."

    menu:
        "Discuss the theoretical framework":
            $ AA += 1
            jump discuss_theory

        "Analyze data together":
            $ AA += 1
            jump analyze_data

        "Review the ethical implications":
            $ MC += 1
            jump review_ethics

label discuss_theory:
    show amelia_prof_hawthorne_discussing
    with dissolve

    "They spend hours discussing the theoretical framework of Amelia's project, diving into complex concepts."

    prof_hawthorne "Your grasp of the theory is impressive, Amelia. This will add significant depth to your work."

    a "Thank you, Professor. I've been really fascinated by how these concepts interconnect. I have some ideas about integrating them further."

    prof_hawthorne "I'd love to hear more about your ideas. Let's schedule a time to discuss them in detail."

    a "Absolutely, Professor. I'll prepare my notes and we can go through them together."

    jump academic_success

label analyze_data:
    show amelia_prof_hawthorne_analyzing
    with dissolve

    "They analyze the data together, identifying patterns and drawing meaningful conclusions."

    prof_hawthorne "This is excellent work, Amelia. Your analytical skills are top-notch."

    a "I couldn't have done it without your guidance, Professor. I've learned so much from our sessions."

    prof_hawthorne "I'm glad to hear that. Remember, always question the data and look for new angles."

    a "Will do, Professor. I have a few more datasets I want to cross-reference."

    jump academic_success

label review_ethics:
    show amelia_prof_hawthorne_ethics
    with dissolve

    "They review the ethical implications of the research, ensuring that all protocols are followed."

    prof_hawthorne "Your attention to ethical detail is commendable, Amelia. This sets a high standard for academic integrity."

    a "It's important to me that our work respects the subjects and maintains transparency."

    prof_hawthorne "And it shows. You're setting a great example for your peers."

    a "Thank you, Professor. I believe ethics should be at the core of all research."

    jump academic_success

label collaborate_peer:
    show amelia_library_peer
    with dissolve

    "Amelia decides to collaborate with a peer, knowing that two minds are better than one."

    show amelia_peer_discussing
    with dissolve

    "She teams up with Raj, and they work together to refine their projects."

    raj "This is looking great, Amelia. I think we've got something really strong here."

    menu:
        "Focus on Raj's project":
            $ SI += 1
            jump focus_raj

        "Balance both projects":
            $ AA += 1
            $ SI += 1
            jump balance_projects

        "Prioritize your project":
            $ AA += 1
            jump prioritize_project

label focus_raj:
    show amelia_raj_project
    with dissolve

    "Amelia decides to focus more on Raj's project, helping him strengthen his work."

    raj "Thanks for your help, Amelia. I couldn't have done this without you."

    a "No problem, Raj. Your project's coming along really well. Let's make sure we address that last section."

    raj "Good idea. I was struggling with that part. Your insights are really helpful."

    a "I'm glad to help. Let's review it together."

    jump academic_success

label balance_projects:
    show amelia_balancing_projects
    with dissolve

    "Amelia and Raj balance their work, ensuring both projects are well-developed."

    a "We're a great team, Raj. Both our projects are going to shine."

    raj "Absolutely. I'm learning a lot from you, Amelia. This collaboration is really pushing me to do better."

    a "Same here, Raj. It's great to have someone to bounce ideas off of."

    jump academic_success

label prioritize_project:
    show amelia_own_project
    with dissolve

    "Amelia prioritizes her project, ensuring it meets the highest standards."

    a "(I need to focus on my own work to make sure it's the best it can be.)"

    "She puts in extra hours, refining her project until it's polished and comprehensive."

    jump academic_success

label work_independently:
    show amelia_studying_intense
    with dissolve

    "Amelia decides to work independently, pushing herself to achieve excellence."

    a "(I can do this. I just need to stay focused and dedicated.)"

    "She puts in extra hours, refining her project until it's polished and comprehensive."

    jump academic_success

label academic_success:
    show amelia_presenting_project
    with dissolve

    "Finally, the day arrives for Amelia to present her project. She stands confidently in front of her class, ready to share her work."

    a "My research explores the ethical dimensions of new psychological therapies, focusing on..."

    "Her presentation is met with applause and praise from both her peers and professors."

    show prof_hawthorne_proud
    with dissolve

    prof_hawthorne "Outstanding work, Amelia. You've set a new benchmark for excellence."

    a "(All the hard work paid off. This is just the beginning.)"

    jump chapter_6_part_3_end

label support_lucas:
    show amelia_lucas_dorm
    with dissolve

    "Amelia finds Lucas in their dorm, clearly upset and struggling with a personal issue."

    show lucas_distressed
    with dissolve

    lucas "Amelia, I need to talk. Everything's falling apart."

    menu:
        "Listen and provide emotional support":
            $ SI += 1
            $ MH += 1
            jump emotional_support_lucas

        "Help Lucas find practical solutions":
            $ SI += 1
            $ AA += 1
            jump practical_solutions_lucas

label emotional_support_lucas:
    show amelia_hugging_lucas
    with dissolve

    "Amelia decides to listen and provide emotional support, sitting beside Lucas and offering a comforting presence."

    a "I'm here, Lucas. Tell me what's going on."

    show lucas_confiding
    with dissolve

    lucas "It's my parents. They're getting a divorce, and I don't know how to handle it."

    a "I'm so sorry, Lucas. That must be incredibly hard."

    lucas "Yeah, and I feel like I'm stuck in the middle. They're both trying to get me to take sides."

    menu:
        "Encourage Lucas to talk to a counselor":
            $ MH += 1
            jump suggest_counselor

        "Offer to be there for him whenever he needs to talk":
            $ SI += 1
            jump offer_support_anytime

label suggest_counselor:
    show amelia_serious
    with dissolve

    a "Lucas, have you thought about talking to a counselor? They might be able to help you navigate this."

    lucas "I don't know, Amelia. I feel weird about talking to a stranger about this."

    a "I understand, but counselors are trained to help with exactly these kinds of issues. It might help you sort through your feelings."

    lucas "Maybe you're right. I'll think about it."

    a "And if you want, I can go with you to your first appointment for support."

    lucas "Thanks, Amelia. That means a lot."

    jump deepened_friendship

label offer_support_anytime:
    show amelia_hugging_lucas
    with dissolve

    a "Lucas, you can always talk to me. I'm here for you, no matter what."

    lucas "Thanks, Amelia. I don't know what I'd do without you."

    a "We'll get through this together. You're not alone."

    jump deepened_friendship

label deepened_friendship:
    show amelia_lucas_smiling
    with dissolve

    "Lucas gives Amelia a grateful smile, clearly feeling a bit better."

    lucas "You're the best, Amelia. Really."

    a "That's what friends are for, Lucas. We'll get through this."

    jump chapter_6_part_3_end

label confront_tasha:
    show amelia_campus_hallway
    with dissolve

    "Amelia spots Tasha in the hallway and decides it's time to confront her about the bullying."

    show amelia_confronting_tasha
    with dissolve

    a "Tasha, we need to talk."

    show tasha_surprised
    with dissolve

    tasha "Oh? What about?"

    menu:
        "Confront Tasha about her bullying":
            $ SI += 1
            $ MC += 1
            jump confront_about_bullying

        "Try to understand why Tasha is acting out":
            $ SI += 1
            $ MH += 1
            jump understand_tasha

label confront_about_bullying:
    show amelia_angry
    with dissolve

    a "Your bullying has to stop, Tasha. It's hurting people, and it's not okay."

    show tasha_defensive
    with dissolve

    tasha "What are you talking about? I'm just having a little fun."

    show amelia_serious
    with dissolve

    a "Fun? People are scared of you. You're making their lives miserable. It's not right."

    show tasha_thinking
    with dissolve

    tasha "I... I didn't realize it was that bad."

    a "It is. You have the power to change that. To be better."

    show tasha_sigh
    with dissolve

    tasha "Maybe you're right. I'll think about it."

    jump tasha_resolution

label understand_tasha:
    show amelia_thoughtful
    with dissolve

    a "Tasha, why are you acting out like this? What's going on with you?"

    show tasha_surprised
    with dissolve

    tasha "What do you care?"

    a "Because I believe people bully others for a reason. Maybe if we understand that, we can find a way to stop it."

    show tasha_sad
    with dissolve

    tasha "You wouldn't understand. My home life is a mess. It's the only way I feel in control."

    a "I'm sorry you're going through that, Tasha. But hurting others won't fix it. Let's find a better way."

    show tasha_thinking
    with dissolve

    tasha "Maybe you're right. I'll think about it."

    jump tasha_resolution

label tasha_resolution:
    show tasha_smiling
    with dissolve

    tasha "Thanks for talking to me, Amelia. Maybe things can be different."

    a "I hope so, Tasha. We can all change for the better."

    jump chapter_6_part_3_end

label high_stakes_ritual:
    show amelia_ritual_preparation
    with dissolve

    "Amelia prepares for a high-stakes occult ritual, feeling a mix of excitement and trepidation."

    show amelia_ritual_circle
    with dissolve

    "She steps into the ritual circle, feeling the energy shift around her."

    menu:
        "Perform the ritual with Maya's guidance":
            $ OK += 1
            jump ritual_with_maya

        "Attempt the ritual independently":
            $ OK += 1
            jump ritual_independently

label ritual_with_maya:
    show maya_ritual
    with dissolve

    "Maya joins Amelia, offering guidance and support as they begin the ritual."

    maya "Focus on your intentions, Amelia. Let the energy flow through you."

    a "I can feel it, Maya. It's powerful."

    maya "Good. Now, speak the incantation."

    show amelia_ritual_spell
    with dissolve

    "Amelia speaks the incantation, feeling a surge of energy as the ritual takes effect."

    a "It's working, Maya. I can feel the connection."

    maya "Excellent. You've done well, Amelia."

    jump ritual_success

label ritual_independently:
    show amelia_ritual_alone
    with dissolve

    "Amelia decides to attempt the ritual independently, trusting in her own abilities."

    a "(I can do this. I just need to focus.)"

    "She steps into the ritual circle and begins the incantation, feeling the energy build around her."

    show amelia_ritual_spell
    with dissolve

    a "I can feel the connection. It's working."

    "As she completes the ritual, she feels a powerful surge of energy, confirming her success."

    jump ritual_success

label ritual_success:
    show amelia_ritual_complete
    with dissolve

    "The ritual is a success, leaving Amelia feeling empowered and connected to the mystical forces around her."

    a "(This is just the beginning. There's so much more to learn and explore.)"

    jump chapter_6_part_3_end

label chapter_6_part_3_end:
    show amelia_dorm_evening
    with dissolve

    "Back in her dorm room, Amelia reflects on the day's events, feeling a mix of exhaustion and accomplishment."

    a "(Today was challenging, but I feel like I've grown so much. I'm ready for whatever comes next.)"

    jump chapter_7_part_1
