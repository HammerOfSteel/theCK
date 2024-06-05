$ high_scores = (AA >= 10 and SI >= 10 and MH >= 10 and MC >= 10 and OC >= 10)

label chapter_8_part_1:
    scene amelia_dorm_night with dissolve
    "The night air is thick with tension. Amelia sits at her desk, overwhelmed by the weight of her responsibilities and the uncertainty of the days ahead."

    show amelia_stressed_dorm with dissolve
    a "I feel like everything is spiraling out of control. I need to pull myself together."

    menu:
        "Focus on academic tasks":
            jump focus_academic_tasks

        "Check on Sarah":
            jump check_on_sarah

        "Reflect on recent events":
            jump reflect_recent_events

label focus_academic_tasks:
    scene amelia_studying_dorm with dissolve
    "Amelia turns her attention to her books and notes, trying to lose herself in her studies."

    show amelia_studying_hard with dissolve
    a "(I can't afford to fall behind now. My future depends on my performance here.)"

    menu:
        "Work on thesis proposal":
            jump work_thesis_proposal

        "Study for upcoming exams":
            jump study_upcoming_exams

        "Research for Prof. Hawthorne's project":
            jump research_hawthorne_project

label work_thesis_proposal:
    show amelia_typing_dorm with dissolve
    "Amelia opens her laptop and begins typing out ideas for her thesis proposal."

    show amelia_thinking_hard with dissolve
    a "(This topic needs to be impactful and original. I want to explore the ethical implications of psychological research.)"

    "Hours pass as Amelia works late into the night, refining her ideas and structuring her proposal."

    show amelia_yawning_dorm with dissolve
    a "I'm making progress, but there's still so much to do. I need to keep pushing."

    $ AA += 1
    jump end_of_day

label study_upcoming_exams:
    show amelia_studying_books with dissolve
    "Amelia spreads out her textbooks and notes, focusing on the material for her upcoming exams."

    show amelia_highlighting_notes with dissolve
    a "(I need to master these concepts. My grades are critical for my future plans.)"

    menu:
        "Take detailed notes":
            jump take_detailed_notes

        "Create a study group":
            jump create_study_group

label take_detailed_notes:
    show amelia_writing_notes with dissolve
    "Amelia meticulously writes out notes, highlighting key concepts and making connections between topics."

    show amelia_focused_notes with dissolve
    a "(This is helping. I feel more prepared for the exams already.)"

    $ AA += 1
    $ SD += 1
    jump end_of_day

label create_study_group:
    show amelia_texting_friends with dissolve
    a "I should see if Lucas, Zara, and Raj want to form a study group. We can help each other out."

    show lucas_replying with dissolve
    l "Great idea, Amelia! Let's meet tomorrow afternoon in the library."

    show zara_replying with dissolve
    z "Count me in. I've been feeling a bit lost on some of the material."

    show raj_replying with dissolve
    r "I'm in too. It'll be good to study together."

    show amelia_smiling_text with dissolve
    a "(This should be helpful. We'll all benefit from studying together.)"

    $ AA += 1
    $ SI += 1
    jump end_of_day

label research_hawthorne_project:
    scene library_research with dissolve
    "Amelia heads to the library to gather materials for Prof. Hawthorne's research project."

    show amelia_reading_books with dissolve
    a "(I need to find the most recent studies on the ethical implications of psychological experiments.)"

    show amelia_taking_notes_library with dissolve
    "Amelia takes detailed notes, carefully recording sources and key points."

    show amelia_satisfied with dissolve
    a "(This research is crucial for the project. I hope Prof. Hawthorne finds my contributions valuable.)"

    $ AA += 1
    $ SD += 1
    jump end_of_day

label check_on_sarah:
    scene sarah_dorm_room with dissolve
    "Concerned for her friend, Amelia decides to check on Sarah."

    show sarah_sitting_dorm with dissolve
    "She finds Sarah sitting on her bed, looking despondent."

    show amelia_concerned with dissolve
    a "Sarah, how are you holding up?"

    show sarah_sad with dissolve
    s "Not great, Amelia. I'm really struggling. I feel like everything is falling apart."

    menu:
        "Offer emotional support":
            jump offer_emotional_support

        "Encourage professional help":
            jump encourage_professional_help

label offer_emotional_support:
    show amelia_sitting_sarah with dissolve
    a "I'm here for you, Sarah. Whatever you're going through, you're not alone."

    show sarah_teary with dissolve
    s "Thank you, Amelia. It means a lot to know you're here. Sometimes, I feel like I'm drowning."

    show amelia_hugging_sarah with dissolve
    a "We'll get through this together. Just take it one step at a time."

    $ SI += 1
    $ MH += 1
    jump end_of_day

label encourage_professional_help:
    show amelia_sitting_sarah with dissolve
    a "Sarah, I really think you should talk to a counselor. Professional help can make a big difference."

    show sarah_nodding with dissolve
    s "I know, Amelia. I've been hesitant, but maybe it's time I reached out for help."

    show amelia_supportive with dissolve
    a "I'll go with you if you want. You're not alone in this."

    $ SI += 1
    $ MH += 1
    jump end_of_day

label reflect_recent_events:
    scene campus_night with dissolve
    "Amelia decides to take a walk around campus, reflecting on recent events."

    show amelia_walking_night with dissolve
    a "(So much has happened. I've faced challenges and made progress, but there's still a long way to go.)"

    show amelia_sitting_bench with dissolve
    "She finds a quiet bench and sits down, lost in thought."

    menu:
        "Think about academic goals":
            jump think_academic_goals

        "Reflect on friendships":
            jump reflect_friendships

        "Contemplate occult research":
            jump contemplate_occult_research

label think_academic_goals:
    show amelia_thinking_bench with dissolve
    a "(My academic goals are clear, but the path is difficult. I need to stay focused and dedicated.)"

    show amelia_determined_bench with dissolve
    a "(I can't let setbacks deter me. I have to keep pushing forward.)"

    $ AA += 1
    $ SD += 1
    jump end_of_day

label reflect_friendships:
    show amelia_thinking_bench with dissolve
    a "(My friends are so important to me. I need to make sure I'm there for them, just as they're there for me.)"

    show amelia_resolved_bench with dissolve
    a "(We all have our struggles, but together we can overcome them.)"

    $ SI += 1
    $ MH += 1
    jump end_of_day

label contemplate_occult_research:
    show amelia_thinking_bench with dissolve
    a "(My occult research has opened up new realms of understanding, but it also carries risks.)"

    show amelia_worried_bench with dissolve
    a "(I need to be cautious and deliberate in my studies. The knowledge is powerful, but I must respect it.)"

    $ OK += 1
    $ SD += 1
    jump end_of_day

label end_of_day:
    scene amelia_dorm_night with dissolve
    "As the night deepens, Amelia returns to her dorm room, feeling the weight of the day's decisions."

    show amelia_reflective_night with dissolve
    a "(Every choice I make is shaping my path. I need to stay strong and true to myself.)"

    "With a mix of resolve and trepidation, Amelia prepares for bed, knowing that tomorrow will bring new challenges and opportunities."

    jump chapter_8_part_2

label chapter_8_part_2:
    scene amelia_dorm_morning with dissolve
    "The morning sun filters through the curtains, waking Amelia with its gentle warmth."

    show amelia_stretching_dorm with dissolve
    a "I need to face whatever comes today with courage and determination."

    menu:
        "Head to the library for research":
            jump head_to_library

        "Visit the Student Union":
            jump visit_student_union

        "Check on Sarah again":
            jump check_on_sarah_again

label head_to_library:
    scene library_interior with dissolve
    "Amelia heads to the library, hoping to make significant progress on her research."

    show amelia_studying_books with dissolve
    "She finds a secluded spot and immerses herself in books and academic journals."

    show amelia_lost_in_books with dissolve
    a "(There’s so much to learn. I need to stay focused and absorb as much as I can.)"

    menu:
        "Research ethical implications in psychology":
            jump research_ethics_psychology

        "Dive into occult texts":
            jump dive_occult_texts

label research_ethics_psychology:
    show amelia_reading_ethics with dissolve
    "Amelia reads extensively about the ethical considerations in psychological research."

    show amelia_taking_notes with dissolve
    a "(These issues are complex and multifaceted. I need to consider every angle for my thesis.)"

    show amelia_intense_focus with dissolve
    "As she takes notes, she begins to see connections and patterns emerging in the ethical debates."

    menu:
        "Explore case studies":
            jump explore_case_studies

        "Analyze philosophical arguments":
            jump analyze_philosophical_arguments

label explore_case_studies:
    show amelia_reading_case_studies with dissolve
    "Amelia examines various case studies, noting the ethical dilemmas and resolutions."

    show amelia_serious with dissolve
    a "(These real-world examples highlight the importance of ethical integrity in research.)"

    show amelia_determined_study with dissolve
    "Her understanding deepens as she sees how ethical principles are applied in practice."

    $ AA += 1
    $ SD += 1
    jump end_library_session

label analyze_philosophical_arguments:
    show amelia_reading_philosophy with dissolve
    "Amelia delves into philosophical texts, analyzing different ethical theories."

    show amelia_thinking_hard with dissolve
    a "(These arguments provide a strong foundation for my thesis. I need to critically evaluate them.)"

    show amelia_writing_notes with dissolve
    "She carefully synthesizes the information, forming her own perspectives on the ethical issues."

    $ AA += 1
    $ SD += 1
    jump end_library_session

label dive_occult_texts:
    show amelia_reading_occult_books with dissolve
    "Amelia decides to explore the more esoteric texts in the library."

    show amelia_intrigued_books with dissolve
    a "(There’s so much hidden knowledge here. I need to approach it with an open but cautious mind.)"

    show amelia_taking_occult_notes with dissolve
    "She takes meticulous notes, drawing connections between ancient rituals and modern practices."

    menu:
        "Study ancient artifacts":
            jump study_ancient_artifacts

        "Interpret prophetic dreams":
            jump interpret_prophetic_dreams

label study_ancient_artifacts:
    show amelia_studying_artifacts with dissolve
    "Amelia reads about various ancient artifacts and their significance."

    show amelia_fascinated with dissolve
    a "(These artifacts hold so much history and power. Understanding them could be crucial.)"

    show amelia_documenting_artifacts with dissolve
    "She documents her findings, making detailed sketches and notes."

    $ OK += 1
    $ SD += 1
    jump end_library_session

label interpret_prophetic_dreams:
    show amelia_studying_dreams with dissolve
    "Amelia delves into texts about prophetic dreams, seeking to understand their meanings."

    show amelia_thinking_deeply with dissolve
    a "(These dreams could be messages from the subconscious or even from higher realms.)"

    show amelia_writing_dream_notes with dissolve
    "She carefully interprets the dreams, noting symbols and recurring themes."

    $ OK += 1
    $ SD += 1
    jump end_library_session

label end_library_session:
    scene library_interior with dissolve
    "After hours of intense study, Amelia takes a deep breath and closes her books."

    show amelia_satisfied with dissolve
    a "(I’ve made good progress today. This knowledge will be invaluable.)"

    jump end_of_day

label visit_student_union:
    scene student_union_interior with dissolve
    "Amelia decides to visit the Student Union, hoping to engage with her peers and find some support."

    show amelia_entering_union with dissolve
    "The atmosphere is buzzing with energy as students discuss various projects and events."

    show michael_waving with dissolve
    "Michael spots Amelia and waves her over."

    show amelia_michael_talking with dissolve
    m "Amelia! Just the person I wanted to see. We’re planning a big campaign and could use your help."

    a "What’s the campaign about, Michael?"

    m "We’re pushing for greater mental health support on campus. We need to gather signatures and organize a rally."

    menu:
        "Join the campaign":
            jump join_campaign

        "Offer moral support but decline":
            jump offer_moral_support

label join_campaign:
    show amelia_michael_planning with dissolve
    a "Count me in, Michael. This cause is important, and I want to help."

    show michael_smiling with dissolve
    m "Great! We’re meeting tomorrow to strategize. Your input will be invaluable."

    $ SI += 1
    $ MC += 1
    jump end_of_day

label offer_moral_support:
    show amelia_michael_talking with dissolve
    a "I support the cause, Michael, but I’m swamped with my studies right now. I’ll help spread the word, though."

    show michael_understanding with dissolve
    m "I understand, Amelia. Any support you can give is appreciated."

    $ SI += 1
    jump end_of_day

label check_on_sarah_again:
    scene sarah_dorm_room with dissolve
    "Amelia decides to check on Sarah again, worried about her friend's well-being."

    show sarah_sitting_dorm with dissolve
    "She finds Sarah looking slightly better but still fragile."

    show amelia_concerned with dissolve
    a "Sarah, how are you feeling today?"

    show sarah_smiling_weakly with dissolve
    s "A bit better, thanks to you. I’ve been thinking about what you said."

    menu:
        "Encourage Sarah to take small steps":
            jump encourage_small_steps

        "Discuss long-term plans":
            jump discuss_long_term_plans

label encourage_small_steps:
    show amelia_sitting_sarah with dissolve
    a "That’s great, Sarah. Just take it one day at a time. Focus on small steps, and don’t be too hard on yourself."

    show sarah_nodding with dissolve
    s "I’ll try. Having you here makes a big difference."

    show amelia_smiling_supportively with dissolve
    a "We’re all here for you, Sarah. You’re not alone."

    $ SI += 1
    $ MH += 1
    jump end_of_day

label discuss_long_term_plans:
    show amelia_sitting_sarah with dissolve
    a "Sarah, have you thought about any long-term plans? Maybe setting some goals could help."

    show sarah_thinking with dissolve
    s "I’ve been too overwhelmed to think that far ahead, but maybe it’s time I did."

    show amelia_encouraging with dissolve
    a "Take it slow. Think about what makes you happy and what you want to achieve. We can work on it together."

    $ SI += 1
    $ MH += 1
    jump end_of_day

label end_of_day:
    scene amelia_dorm_evening with dissolve
    "As the day ends, Amelia reflects on her choices and their impact."

    show amelia_reflective_evening with dissolve
    a "(Every action I take matters. I need to stay true to my values and support those around me.)"

    "With a sense of purpose, Amelia prepares for bed, knowing that the challenges are far from over."

    jump chapter_8_part_3

label chapter_8_part_3:
    scene amelia_dorm_morning with dissolve
    "Amelia wakes up to a sense of urgency. Today feels different, more intense."

    show amelia_determined with dissolve
    a "I need to be ready for whatever comes my way."

    menu:
        "Focus on an important academic project":
            jump focus_academic_project

        "Check on Sarah again":
            jump check_on_sarah_third_time

        "Attend a student union meeting":
            jump attend_student_union_meeting

label focus_academic_project:
    scene library_interior with dissolve
    "Amelia heads to the library to work on a critical academic project."

    show amelia_studying_books with dissolve
    "She immerses herself in her research, determined to make significant progress."

    menu:
        "Deep dive into theoretical frameworks":
            jump deep_dive_theoretical_frameworks

        "Conduct a practical experiment":
            jump conduct_practical_experiment

label deep_dive_theoretical_frameworks:
    show amelia_reading_books with dissolve
    "Amelia studies various theoretical frameworks, analyzing their relevance to her project."

    show amelia_thinking_hard with dissolve
    a "(These theories are complex, but understanding them is crucial for my work.)"

    show amelia_taking_notes with dissolve
    "She takes detailed notes, connecting different ideas and forming her own perspectives."

    $ AA += 1
    $ SD += 1
    jump end_academic_session

label conduct_practical_experiment:
    scene research_lab with dissolve
    "Amelia sets up a practical experiment in the psychological research lab."

    show amelia_setting_up_experiment with dissolve
    a "(This experiment will test my hypotheses and provide valuable data.)"

    show amelia_focused_experiment with dissolve
    "She carefully conducts the experiment, recording her observations and analyzing the results."

    $ AA += 1
    $ SD += 1
    jump end_academic_session

label end_academic_session:
    scene library_interior with dissolve
    "After hours of hard work, Amelia takes a moment to reflect on her progress."

    show amelia_satisfied with dissolve
    a "(I’ve made good progress today. This will be invaluable for my project.)"

    jump end_of_day

label check_on_sarah_third_time:
    scene sarah_dorm_room with dissolve
    "Amelia decides to check on Sarah once more, feeling a deep sense of concern."

    show sarah_sitting_dorm with dissolve
    "She finds Sarah looking slightly better but still fragile."

    show amelia_concerned with dissolve
    a "Sarah, how are you feeling today?"

    show sarah_smiling_weakly with dissolve
    s "A bit better, thanks to you. I’ve been thinking about what you said."

    menu:
        "Encourage Sarah to take small steps":
            jump encourage_small_steps_third_time

        "Discuss long-term plans":
            jump discuss_long_term_plans_third_time

label encourage_small_steps_third_time:
    show amelia_sitting_sarah with dissolve
    a "That’s great, Sarah. Just take it one day at a time. Focus on small steps, and don’t be too hard on yourself."

    show sarah_nodding with dissolve
    s "I’ll try. Having you here makes a big difference."

    show amelia_smiling_supportively with dissolve
    a "We’re all here for you, Sarah. You’re not alone."

    $ SI += 1
    $ MH += 1
    jump end_of_day

label discuss_long_term_plans_third_time:
    show amelia_sitting_sarah with dissolve
    a "Sarah, have you thought about any long-term plans? Maybe setting some goals could help."

    show sarah_thinking with dissolve
    s "I’ve been too overwhelmed to think that far ahead, but maybe it’s time I did."

    show amelia_encouraging with dissolve
    a "Take it slow. Think about what makes you happy and what you want to achieve. We can work on it together."

    $ SI += 1
    $ MH += 1
    jump end_of_day

label attend_student_union_meeting:
    scene student_union_meeting with dissolve
    "Amelia attends a student union meeting, eager to engage with her peers and contribute to the discussions."

    show student_union_members with dissolve
    "The meeting room is filled with passionate students discussing various issues and initiatives."

    show michael_speaking with dissolve
    m "We need more support for mental health on campus. It’s time we took action."

    show amelia_listening with dissolve
    a "(Michael is right. We need to do more to support each other.)"

    menu:
        "Volunteer to lead a mental health initiative":
            jump volunteer_mental_health_initiative

        "Suggest organizing a campus-wide event":
            jump suggest_campus_wide_event

label volunteer_mental_health_initiative:
    show amelia_speaking_union with dissolve
    a "I’d like to volunteer to lead a mental health initiative. We can organize workshops and support groups."

    show michael_nodding with dissolve
    m "That’s a great idea, Amelia. Your leadership will make a big difference."

    $ SI += 1
    $ MC += 1
    jump end_of_day

label suggest_campus_wide_event:
    show amelia_speaking_union with dissolve
    a "We should organize a campus-wide event to raise awareness and support for mental health."

    show michael_agreeing with dissolve
    m "Excellent suggestion, Amelia. We can plan a rally and invite speakers to address the issues."

    $ SI += 1
    $ MC += 1
    jump end_of_day

label end_of_day:
    scene amelia_dorm_evening with dissolve
    "As the day ends, Amelia reflects on her choices and their impact."

    show amelia_reflective_evening with dissolve
    a "(Every action I take matters. I need to stay true to my values and support those around me.)"

    "With a sense of purpose, Amelia prepares for bed, knowing that the challenges are far from over."

    jump chapter_8_part_4

label chapter_8_part_4:
    scene amelia_dorm_morning with dissolve
    "Amelia wakes up feeling the weight of her responsibilities and the challenges ahead."

    show amelia_resolved with dissolve
    a "I have to stay strong. Today is going to be tough, but I’m ready."

    menu:
        "Focus on academic integrity":
            jump focus_academic_integrity

        "Support Sarah intensively":
            jump support_sarah_intensively

        "Join Michael’s campaign":
            jump join_michaels_campaign

label focus_academic_integrity:
    scene lecture_hall with dissolve
    "Amelia heads to the lecture hall, determined to uphold her academic integrity despite the pressure."

    show amelia_lecture_hall with dissolve
    "During the lecture, she notices some students passing around what looks like an answer key for the upcoming exam."

    show sophia_lecture_hall with dissolve
    "Sophia catches her eye, and Amelia sees the conflict in her rival's eyes."

    menu:
        "Confront the cheating students":
            jump confront_cheating_students

        "Ignore the situation and focus on her own work":
            jump ignore_cheating

label confront_cheating_students:
    show amelia_confronting_students with dissolve
    a "What you’re doing is wrong. Cheating undermines everything we’re here to achieve."

    show student_cheaters_surprised with dissolve
    student_1 "Mind your own business, Amelia. This doesn’t concern you."

    show amelia_resolute with dissolve
    a "It does concern me. We should all succeed on our own merits."

    show professor_lecture_hall with dissolve
    "The professor notices the commotion and intervenes."

    show professor_serious with dissolve
    professor "What’s going on here?"

    show amelia_explaining with dissolve
    a "Professor, I saw some students passing around an answer key. I believe they’re cheating."

    show professor_stern with dissolve
    professor "Thank you for bringing this to my attention, Amelia. I will handle this."

    show sophia_grateful with dissolve
    s "That was brave of you, Amelia. It’s not easy to stand up like that."

    show amelia_humble with dissolve
    a "It’s what needed to be done. We’re here to learn, not to cheat."

    $ AA += 1
    $ MC += 1
    jump end_of_day

label ignore_cheating:
    show amelia_focused with dissolve
    "Amelia decides to focus on her own work, choosing to not get involved in the situation."

    show sophia_disappointed with dissolve
    s "Amelia, you saw what was happening. Why didn’t you say something?"

    show amelia_justifying with dissolve
    a "I have too much on my plate already. I can’t fight every battle."

    show sophia_shaking_head with dissolve
    s "Sometimes, doing the right thing means making sacrifices. I hope you remember that."

    show amelia_reflecting with dissolve
    a "(Was I wrong to stay silent? Maybe I should have said something...)"

    $ MC -= 1
    jump end_of_day

label support_sarah_intensively:
    scene hospital_room with dissolve
    "Amelia spends the entire day with Sarah, who has been admitted to the hospital for intensive care."

    show amelia_sitting_sarah_bedside with dissolve
    "She holds Sarah’s hand, offering words of comfort and support."

    show sarah_weak_smile with dissolve
    s "Thank you for being here, Amelia. I don’t know what I’d do without you."

    show amelia_gentle_smile with dissolve
    a "You’re going to get through this, Sarah. We’re all here for you."

    show doctor_hospital_room with dissolve
    "A doctor enters the room, updating Amelia on Sarah’s condition."

    show doctor_serious with dissolve
    doctor "Sarah is stable, but she has a long road to recovery. She’ll need continuous support and therapy."

    show amelia_determined with dissolve
    a "I’ll do whatever it takes to help her."

    show doctor_nodding with dissolve
    doctor "Your support makes a big difference. Keep being there for her."

    $ MH += 1
    $ SI += 1
    jump end_of_day

label join_michaels_campaign:
    scene student_union_meeting with dissolve
    "Amelia attends another meeting for Michael’s campaign, ready to take on a more active role."

    show amelia_michael_planning with dissolve
    "She discusses strategies and plans with Michael and other students."

    show michael_grateful with dissolve
    m "Your enthusiasm and ideas are exactly what we need, Amelia."

    show amelia_nodding with dissolve
    a "This cause is important. We need to make sure everyone on campus knows about it."

    menu:
        "Plan a major rally":
            jump plan_major_rally

        "Organize a petition drive":
            jump organize_petition_drive

label plan_major_rally:
    show amelia_speaking_rally with dissolve
    "Amelia takes charge of planning a major rally, coordinating with various student groups."

    show students_cheering_rally with dissolve
    "The rally is a huge success, with many students showing up to support the cause."

    show michael_speaking_rally with dissolve
    m "Thank you all for being here. Together, we can make a difference for mental health on campus!"

    show amelia_proud with dissolve
    a "(This is just the beginning. We have to keep pushing for change.)"

    $ SI += 1
    $ MC += 1
    jump end_of_day

label organize_petition_drive:
    show amelia_speaking_union with dissolve
    "Amelia organizes a petition drive, gathering signatures to demand better mental health support."

    show students_signing_petition with dissolve
    "Many students eagerly sign the petition, showing their support."

    show michael_grateful with dissolve
    m "Great job, Amelia. Every signature brings us closer to real change."

    show amelia_nodding with dissolve
    a "We’re making our voices heard. This is important work."

    $ SI += 1
    $ MC += 1
    jump end_of_day

label end_of_day:
    scene amelia_dorm_evening with dissolve
    "As the day ends, Amelia reflects on her choices and their impact."

    show amelia_reflective_evening with dissolve
    a "(Every action I take matters. I need to stay true to my values and support those around me.)"

    "With a sense of purpose, Amelia prepares for bed, knowing that the challenges are far from over."

    jump chapter_8_part_5

label chapter_8_part_5:
    scene amelia_dorm_morning with dissolve
    "Amelia wakes up feeling the weight of the previous day’s events, but also a renewed sense of determination."

    show amelia_determined with dissolve
    a "Today, I need to keep pushing forward. I have to balance everything that’s happening and stay true to myself."

    menu:
        "Focus on academics and tackle a major project":
            jump focus_academics_major_project

        "Check on Sarah and offer support":
            jump check_on_sarah

        "Seek out Maya for guidance on the occult path":
            jump seek_maya_guidance

label focus_academics_major_project:
    scene library_study_table with dissolve
    "Amelia heads to the library to work on a major project that’s due soon."

    show amelia_studying_intensely with dissolve
    "She dives into her research, losing herself in the complexities of the subject matter."

    show sophia_approaching_table with dissolve
    "Sophia approaches her table, holding a stack of books."

    show sophia_offering_help with dissolve
    s "Amelia, I know we’ve had our differences, but I see how hard you’re working. Do you need any help?"

    menu:
        "Accept Sophia’s help":
            jump accept_sophia_help

        "Refuse and continue working alone":
            jump refuse_sophia_help

label accept_sophia_help:
    show amelia_smiling_sophia with dissolve
    a "Thank you, Sophia. I appreciate it. Let’s tackle this together."

    show amelia_sophia_working_together with dissolve
    "Amelia and Sophia work side by side, sharing insights and discussing ideas."

    show sophia_impressed with dissolve
    s "You have some brilliant ideas, Amelia. This project is going to be great."

    show amelia_grateful with dissolve
    a "Thanks, Sophia. Your help means a lot."

    $ AA += 1
    $ SI += 1
    jump end_of_day_academics

label refuse_sophia_help:
    show amelia_determined_study with dissolve
    a "I appreciate the offer, Sophia, but I need to do this on my own."

    show sophia_nodding with dissolve
    s "I understand. If you change your mind, I’m here."

    show amelia_studying_harder with dissolve
    "Amelia redoubles her efforts, determined to complete the project on her own."

    show amelia_success with dissolve
    "After hours of intense focus, she finally finishes the project, feeling a deep sense of accomplishment."

    $ AA += 2
    jump end_of_day_academics

label end_of_day_academics:
    scene amelia_dorm_evening with dissolve
    "As the day ends, Amelia reflects on her hard work and the importance of collaboration."

    show amelia_reflective_evening with dissolve
    a "(Today was tough, but I pushed through. I need to remember that asking for help isn’t a weakness.)"

    "With a sense of pride and relief, Amelia prepares for bed, ready to face whatever comes next."

    jump chapter_8_part_6

label check_on_sarah:
    scene sarah_dorm_room with dissolve
    "Amelia decides to check on Sarah, feeling a deep concern for her friend."

    show sarah_sitting_bed with dissolve
    "She finds Sarah sitting on her bed, looking lost in thought."

    show amelia_sitting_beside_sarah with dissolve
    a "Sarah, how are you feeling today?"

    show sarah_sighing with dissolve
    sa "It's been tough, Amelia. Some days are better than others, but today... today is one of the harder ones."

    show amelia_concerned with dissolve
    a "I'm here for you, Sarah. You don't have to go through this alone."

    show sarah_sad_smile with dissolve
    sa "I know you're trying to help, and I appreciate it. But sometimes, it just feels like too much."

    menu:
        "Offer to take a walk together":
            jump offer_walk_sarah

        "Suggest visiting the counseling center":
            jump suggest_counseling_sarah

        "Sit and talk with her":
            jump sit_and_talk_sarah

label offer_walk_sarah:
    show amelia_hopeful with dissolve
    a "How about we take a walk? Sometimes a change of scenery can help clear your mind."

    show sarah_considering with dissolve
    sa "I suppose a walk couldn't hurt. Maybe it'll help me get out of my head for a bit."

    scene campus_path with dissolve
    "Amelia and Sarah walk through the campus, the fresh air helping to lift Sarah's spirits a little."

    show amelia_sarah_talking_walk with dissolve
    a "Sometimes when things get overwhelming, it's good to just take a step back and breathe."

    show sarah_slight_smile with dissolve
    sa "You're right. It's just hard to remember that when I'm stuck in my thoughts."

    show amelia_encouraging with dissolve
    a "Whenever you feel like that, just remember you have friends who care about you. We're here to help."

    show sarah_nodding with dissolve
    sa "Thanks, Amelia. It means a lot."

    $ MH += 1
    $ SI += 1
    jump end_of_day_sarah

label suggest_counseling_sarah:
    show amelia_gently_suggesting with dissolve
    a "Sarah, maybe it would help to talk to a professional. The counseling center has resources that could really benefit you."

    show sarah_hesitant with dissolve
    sa "I don't know, Amelia. I've tried therapy before and it didn't help much."

    show amelia_persistent with dissolve
    a "I understand, but sometimes it takes finding the right therapist or approach. It could make a big difference."

    show sarah_sighing with dissolve
    sa "Alright, I'll think about it. Maybe it's worth another try."

    show amelia_smiling with dissolve
    a "I'm glad to hear that. And I'll be here to support you every step of the way."

    $ MH += 1
    jump end_of_day_sarah

label sit_and_talk_sarah:
    show amelia_sitting_beside_sarah with dissolve
    a "Let's just sit and talk for a while. Sometimes sharing what's on your mind can help lighten the load."

    show sarah_nodding with dissolve
    sa "Okay. It's just... everything feels so heavy. Like I'm drowning and can't find the surface."

    show amelia_listening with dissolve
    a "I'm here to listen, Sarah. No judgment, just support."

    show sarah_talking with dissolve
    sa "I've been feeling so lost, like I'm a burden to everyone around me. I try to be strong, but it's exhausting."

    show amelia_compassionate with dissolve
    a "You are not a burden, Sarah. Your feelings are valid, and it's okay to ask for help. We all need support sometimes."

    show sarah_teary with dissolve
    sa "Thank you, Amelia. I don't know what I'd do without you."

    $ MH += 1
    $ SI += 1
    jump end_of_day_sarah

label end_of_day_sarah:
    scene amelia_dorm_evening with dissolve
    "After spending time with Sarah, Amelia returns to her dorm room, feeling the weight of her friend's struggles but also a sense of purpose."

    show amelia_reflective_evening with dissolve
    a "(Sarah is going through so much. I need to be there for her, but I also have to take care of myself.)"

    "With a heavy heart but a determined spirit, Amelia prepares for bed, ready to face the challenges of the next day."

    jump chapter_8_part_6

label seek_maya_guidance:
    scene maya_garden with dissolve
    "Amelia seeks out Maya for guidance on her occult path."

    show maya_smiling_welcome with dissolve
    m "Amelia, it's good to see you. How can I help you today?"

    show amelia_thoughtful with dissolve
    a "I've been feeling overwhelmed with everything that's happening. I need some guidance on how to balance my studies, my friends, and my spiritual path."

    show maya_nodding with dissolve
    m "It's important to find balance, especially when you're on a path of deep exploration. Let's meditate together and see if we can find some clarity."

    scene maya_meditation with dissolve
    "Amelia and Maya sit in meditation, focusing on their breath and the energy around them."

    show maya_advice with dissolve
    m "Listen to your inner voice, Amelia. It will guide you towards the balance you seek. Trust yourself and the journey you're on."

    show amelia_calm with dissolve
    a "Thank you, Maya. I feel a bit more centered now."

    menu:
        "Discuss recent events and seek advice":
            jump discuss_recent_events

        "Ask about a specific ritual or practice":
            jump ask_about_ritual

        "Share a personal struggle":
            jump share_personal_struggle

label discuss_recent_events:
    show amelia_concerned with dissolve
    a "I've been dealing with so many challenges lately. My friend's mental health, academic pressures, and my own spiritual journey... it's all so much."

    show maya_listening with dissolve
    m "These challenges are all part of your growth, Amelia. Each one is teaching you something valuable about yourself and your path."

    show amelia_reflective with dissolve
    a "I just feel like I'm being pulled in so many different directions. How do I know what to prioritize?"

    show maya_wisdom with dissolve
    m "Trust your intuition. It will guide you to what needs your attention the most. And remember, it's okay to ask for help and lean on those who support you."

    show amelia_grateful with dissolve
    a "Thank you, Maya. Your words always bring me clarity."

    $ OK += 1
    jump end_of_day_maya

label ask_about_ritual:
    show amelia_curious with dissolve
    a "There's a ritual I've been thinking about performing, but I'm not sure if it's the right time or if I'm ready."

    show maya_interested with dissolve
    m "Tell me more about this ritual. What is its purpose?"

    show amelia_explaining with dissolve
    a "It's a ritual for seeking deeper wisdom and guidance. I feel like it could help me find the answers I'm looking for."

    show maya_nodding with dissolve
    m "Rituals can be powerful tools for transformation. If you feel called to it, trust that instinct. But also make sure you are mentally and spiritually prepared for what it may reveal."

    show amelia_thoughtful with dissolve
    a "I'll take some time to prepare and make sure I'm ready."

    show maya_supportive with dissolve
    m "Good. And remember, I'm here to support you through it."

    $ OK += 1
    jump end_of_day_maya

label share_personal_struggle:
    show amelia_vulnerable with dissolve
    a "I've been struggling with feeling like I'm not enough. No matter how hard I try, it feels like I'm always falling short."

    show maya_compassionate with dissolve
    m "It's natural to have doubts and fears, Amelia. They are part of being human. But you must remember your worth and the unique gifts you bring to the world."

    show amelia_sighing with dissolve
    a "I try, but it's hard to shake the feeling of inadequacy."

    show maya_wisdom with dissolve
    m "Focus on the progress you've made, not on the perceived shortcomings. Celebrate your successes and be kind to yourself in moments of doubt."

    show amelia_grateful with dissolve
    a "Thank you, Maya. Your words always bring me comfort."

    $ OK += 1
    jump end_of_day_maya

label end_of_day_maya:
    scene amelia_dorm_evening with dissolve
    "After her session with Maya, Amelia returns to her dorm room, feeling more balanced and ready to face her challenges."

    show amelia_reflective_evening with dissolve
    a "(Today was another step forward. I need to keep trusting my path and the people who support me.)"

    "With a sense of peace and determination, Amelia prepares for bed, ready to face whatever comes next."

    jump chapter_8_part_6

label chapter_8_part_6:
    
    scene amelia_dorm_evening with dissolve
    "Amelia is sitting at her desk, trying to focus on her studies, when her phone buzzes with an urgent message from Sarah."

    show amelia_reading_phone with dissolve
    "Amelia, can we meet? I really need to talk. Please, it's urgent. - Sarah"
    a "(Something's wrong. I need to go to her.)"

    menu:
        "Rush to meet Sarah immediately":
            jump rush_to_sarah

        "Call Sarah first to see what's wrong":
            jump call_sarah_first

label rush_to_sarah:
    scene campus_secluded_spot with dissolve
    "Amelia rushes to the secluded spot on campus where Sarah asked to meet her. She finds Sarah in a state of deep distress, tears streaming down her face."

    show sarah_crying with dissolve
    sa "Amelia... I'm sorry... I didn't know who else to turn to..."

    show amelia_concerned with dissolve
    a "Sarah, what's wrong? You're scaring me. Talk to me, please."

    jump sarah_crisis_conversation

label call_sarah_first:
    show amelia_calling_sarah with dissolve
    "Amelia quickly dials Sarah's number, her heart pounding with worry."

    show sarah_crying_phone with dissolve
    sa "Amelia... I can't do this anymore. The pain, the emptiness... it's too much. Please come. I need you."

    show amelia_determined with dissolve
    a "I'm on my way, Sarah. Stay where you are."

    scene campus_secluded_spot with dissolve
    "Amelia rushes to the secluded spot on campus where Sarah asked to meet her. She finds Sarah in a state of deep distress, tears streaming down her face."

    jump sarah_crisis_conversation

label sarah_crisis_conversation:
    show amelia_hugging_sarah with dissolve
    "Amelia embraces Sarah, trying to offer comfort."

    show sarah_crying_amplified with dissolve
    sa "I can't... I can't do this anymore. The pain, the emptiness... it's too much. I've tried so hard, but I just can't see a way out."

    show amelia_desperate with dissolve
    a "Sarah, listen to me. You're not alone in this. I'm here for you, and we can get through this together."

    show sarah_pull_away with dissolve
    sa "No, Amelia. You don't understand. I've been fighting this darkness for so long, and I'm just... I'm so tired. I can't keep pretending that everything's okay when it's not."

    show amelia_determined with dissolve
    a "I know it's hard, Sarah. Believe me, I know. But ending your life is not the answer. You have so much to live for, even if you can't see it right now."

    show sarah_hopeless with dissolve
    sa "Do I? All I see is pain, all I feel is hopelessness. I've tried therapy, medication, everything... and nothing helps. I'm just a burden to everyone, including you."

    if high_scores:
        menu:
            
            "Reassure Sarah that she is not a burden":
                jump reassure_sarah

            "Plead with Sarah to seek help together":
                jump plead_with_sarah

    else:
        menu:

            "Feel a wave of helplessness and panic":
                jump helpless_panic

label reassure_sarah:
    show amelia_holding_sarah with dissolve
    a "Sarah, you could never be a burden. Your life has value and meaning, and there are so many people who care about you, who would be devastated if they lost you."

    show sarah_shaking_head with dissolve
    sa "I'm sorry, Amelia. I know you're trying to help, but... I've made up my mind. I just wanted to say goodbye, and to thank you for being my friend."

    show amelia_pleading with dissolve
    a "Sarah, no! Please, don't do this. Stay with me, we can call for help, we can figure this out..."

    if high_scores:
        menu:

            "Try to physically stop Sarah from leaving":
                jump physically_stop_sarah

    else:
        menu:

            "Call for emergency help immediately":
                jump call_emergency_help

label plead_with_sarah:
    show amelia_holding_sarah with dissolve
    a "Sarah, you are not alone in this. Let’s seek help together. We can go to the counseling center right now. Please, just give it another chance."

    show sarah_hesitant with dissolve
    sa "I don't know, Amelia. I've tried so many times... I'm just so tired."

    show amelia_pleading with dissolve
    a "I know you're tired, but you don't have to face this alone. We can do this together. Please, Sarah, let’s go get help."

    if high_scores:
        menu:

            "Convince Sarah to go to the counseling center":
                jump convince_counseling_center

    else:
        menu:

            "Call for emergency help immediately":
                jump call_emergency_help

label helpless_panic:
    show amelia_panic with dissolve
    a "(I don't know what to do... I can't lose her. But what if I can't save her?)"

    show sarah_pull_away with dissolve
    "Sarah pulls away from Amelia, tears streaming down her face as she backs away."

    show amelia_reaching_out with dissolve
    a "Sarah, no! Please, don't do this!"

    show sarah_running_off with dissolve
    "Despite Amelia's desperate pleas, Sarah runs off, leaving Amelia in a state of shock and terror."

    jump tragic_outcome

label physically_stop_sarah:
    show amelia_grabbing_sarah with dissolve
    "Amelia grabs Sarah's arm, trying to stop her from leaving."

    show sarah_startled with dissolve
    sa "Amelia, let go! You can't save me!"

    show amelia_desperate with dissolve
    a "I won't let you go, Sarah. You mean too much to me. We can get through this together."

    show sarah_break_away with dissolve
    sa "No, Amelia. Please, just let me go."

    if high_scores:
        menu:

            "Hold on tighter and try to convince her":
                jump hold_on_tighter
    
    else:
        menu:

            "Let go and call for help":
                jump call_emergency_help



label call_emergency_help:
    show amelia_dialing_phone with dissolve
    "Amelia quickly dials emergency services, explaining the situation as best she can."

    show sarah_breaking_down with dissolve
    "Sarah collapses to the ground, sobbing uncontrollably."

    menu:
        "Stay with Sarah until help arrives":
            jump stay_with_sarah

        "Run to get more friends to help":
            jump get_more_friends

label convince_counseling_center:
    show amelia_consoling_sarah with dissolve
    a "Please, Sarah. Let's go to the counseling center. I’ll be with you every step of the way. We can find the right support together."

    show sarah_hesitant with dissolve
    sa "Alright, Amelia. I'll go with you. But I'm so scared..."

    show amelia_supportive with dissolve
    a "I know, but you're not alone. Let's take this step together."

    show amelia_sarah_walking with dissolve
    "Amelia gently leads Sarah towards the counseling center, hoping this is the turning point for her friend."

    jump counseling_center

label stay_with_sarah:
    show amelia_sitting_sarah with dissolve
    "Amelia stays with Sarah, holding her hand and speaking softly to her, trying to keep her calm until emergency help arrives."

    show emergency_arrival with dissolve
    "Soon, the emergency team arrives, taking Sarah into their care. Amelia feels a mix of relief and sorrow."

    jump aftermath_sarah_event

label get_more_friends:
    show amelia_running with dissolve
    "Amelia runs to get more friends, hoping their presence will help. She finds Lucas and Raj, quickly explaining the situation."

    show lucas_raj_running with dissolve
    "Together, they rush back to Sarah, their combined efforts providing a stronger support network."

    jump group_support

label hold_on_tighter:
    show amelia_holding_tighter with dissolve
    a "Sarah, please. I'm begging you. Don't do this. You're stronger than you think. We can find a way out together."

    show sarah_crying_amplified with dissolve
    sa "I don't know if I can believe that anymore, Amelia..."

    menu:
        "Call for help while holding Sarah":
            jump call_emergency_help

        "Try to talk Sarah down":
            jump talk_down_sarah

label counseling_center:
    show counseling_center_entrance with dissolve
    "Amelia and Sarah arrive at the counseling center. The staff immediately takes Sarah in, providing the urgent care she needs."

    show amelia_relief with dissolve
    "Amelia feels a wave of relief wash over her, knowing that Sarah is finally getting professional help."

    jump aftermath_sarah_event

label talk_down_sarah:
    show amelia_pleading_sarah with dissolve
    a "You have to believe, Sarah. You have to hold on. For me, for everyone who loves you. We can't lose you."

    show sarah_breaking_down with dissolve
    sa "I... I'll try, Amelia. I'll try..."

    jump call_emergency_help

label tragic_outcome:
    show amelia_shocked with dissolve
    "As Sarah runs off, Amelia feels a sense of dread and helplessness. She tries to chase after her, but it's too late."

    show amelia_falling with dissolve
    "Suddenly, Amelia feels the ground give way beneath her. She is falling, spiraling into a dark void."

    show amelia_surreal_experience with dissolve
    "In this surreal experience, she sees flashes of light, strange symbols, and hears distant voices. It's as if the universe is trying to shield her from the unbearable reality."

    show amelia_waking_up with dissolve
    "Amelia wakes up on the ground, disoriented and alone. The weight of what has just happened crashes down on her, leaving her in a state of profound grief and confusion."

    "Sarah is gone. The realization hits Amelia like a tidal wave, and she collapses in tears, overwhelmed by guilt and sorrow."

    jump chapter_9_intro

label chapter_9_intro:
    scene campus_morning with dissolve
    "The next day, Amelia is a shadow of herself, moving through campus in a daze. The loss of Sarah weighs heavily on her heart."

    show amelia_resolute with dissolve
    a "(I failed her... but I can't let this break me. I have to keep going, for her sake. I have to find a way to make a difference.)"

    "With a heavy heart but a renewed sense of purpose, Amelia prepares to face the challenges ahead, determined to honor Sarah's memory by fighting for mental health awareness and support."

    jump chapter_9_part_1

