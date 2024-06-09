label chapter_5_part_1:
    show amelia_campus_exterior
    with dissolve

    "As Amelia continues her journey at Plymouth University, she faces new challenges and opportunities that test her resolve and shape her future."

    show amelia_studying_library
    with dissolve

    "Amelia spends hours in the library, fully immersed in her studies. The pressure of her coursework is mounting, but she remains determined to excel."

    show lucas_union
    with dissolve

    lucas "Hey Amelia, how's it going? You look like you haven't left the library in days."

    show amelia_tired_union
    with dissolve

    a "It feels like it, Lucas. There's just so much to do and so little time."

    lucas "Remember to take breaks, okay? Overworking yourself won't help in the long run."

    a "You're right. Maybe I should take a break and grab some coffee."

    menu:
        "Go for a coffee break with Lucas (+SI)":
            $ SI += 1
            jump coffee_break

        "Continue studying in the library (+AA)":
            $ AA += 1
            jump continue_studying_2

label coffee_break:
    show cafe_interior
    with dissolve

    "Amelia and Lucas head to the campus café, enjoying a much-needed break from their studies."

    show amelia_lucas_chatting_cafe
    with dissolve

    lucas "So, how are you holding up with everything? Any interesting classes?"

    a "Yeah, actually. I'm really getting into Prof. Hawthorne's psychology ethics class. It's challenging but fascinating."

    show lucas_interested_cafe
    with dissolve

    lucas "That's great to hear. Have you considered joining any study groups? It might help lighten the load."

    menu:
        "Join a study group (+SI)":
            $ SI += 1
            jump join_study_group
        
        "Focus on individual study (+AA)":
            $ AA += 1
            jump individual_study

label join_study_group:
    show study_group_library
    with dissolve

    "Amelia decides to join a study group, hoping to gain new perspectives and support from her peers."

    show amelia_study_group_discussion
    with dissolve

    a "It's really helpful to discuss these concepts with others. Everyone has such unique insights."

    show raj_study_group
    with dissolve

    raj "Absolutely. Sometimes, hearing someone else's take on a topic can make things click."

    if SI >= 3:
        show amelia_smiling_study_group
        with dissolve

        "Amelia quickly becomes an integral part of the group, known for her thoughtful contributions and willingness to help others."

        a "I'm really glad I joined this group. It's making a big difference."

    jump academic_pressure_continued

label individual_study:
    show amelia_studying_library
    with dissolve

    "Amelia decides to focus on individual study, diving deep into her textbooks and notes."

    show amelia_tired_studying
    with dissolve

    a "(This is exhausting, but I need to push through. I have to stay on top of my coursework.)"

    if AA >= 4:
        show professor_hawthorne_library
        with dissolve

        professor "Amelia, I see you're hard at work again. Remember to pace yourself. Excellence requires balance."

        a "I'll try, Professor. Thank you for the advice."

    jump academic_pressure_continued

label continue_studying_2:
    show amelia_studying_library
    with dissolve

    "Amelia decides to continue studying in the library, determined to stay on top of her coursework."

    show amelia_tired_studying
    with dissolve

    a "(This is exhausting, but I need to push through. I have to stay on top of my coursework.)"

    if AA >= 4:
        show professor_hawthorne_library
        with dissolve

        professor "Amelia, I see you're hard at work again. Remember to pace yourself. Excellence requires balance."

        a "I'll try, Professor. Thank you for the advice."

    jump academic_pressure_continued

label academic_pressure_continued:
    show amelia_dorm_evening
    with dissolve

    "Later that evening, Amelia reflects on her day and the challenges she's facing."

    show amelia_pensive_dorm
    with dissolve

    a "I need to find a way to balance everything. Maybe I should talk to someone for advice."

    menu:
        "Talk to Prof. Hawthorne (+AA, +MC)":
            $ AA += 1
            $ MC += 1
            jump talk_prof_hawthorne
        
        "Talk to Sarah (+SI, +MH)":
            $ SI += 1
            $ MH += 1
            jump talk_sarah
        
        "Talk to Maya (+SD, +OK)":
            $ SD += 1
            $ OK += 1
            jump talk_maya

label talk_prof_hawthorne:
    show professor_hawthorne_office
    with dissolve

    "Amelia schedules a meeting with Prof. Hawthorne to discuss her concerns and seek guidance."

    show amelia_prof_hawthorne_talking
    with dissolve

    professor "Amelia, it's good to see you. What can I do for you today?"

    a "I've been struggling to balance my coursework and personal life. I want to excel, but I don't want to burn out."

    show professor_thoughtful
    with dissolve

    professor "It's important to find that balance, Amelia. Excellence isn't just about hard work; it's also about knowing when to rest and recharge."

    a "Do you have any advice on how to manage it all?"

    professor "Prioritize your tasks, set realistic goals, and don't hesitate to ask for help when you need it. Also, make sure to take breaks and engage in activities that bring you joy."

    show amelia_relieved
    with dissolve

    a "Thank you, Professor. I'll try to keep that in mind."

    jump chapter_5_part_1_end

label talk_sarah:
    show amelia_sarah_dorm
    with dissolve

    "Amelia decides to talk to Sarah, hoping to find some comfort and advice."

    show sarah_smiling_dorm
    with dissolve

    sarah "Hey Amelia, what's on your mind?"

    a "I've been feeling overwhelmed with my studies. How do you manage to keep everything in balance?"

    show sarah_thoughtful
    with dissolve

    sarah "It's not easy, but I find that taking breaks and doing things I enjoy really helps. Also, don't be afraid to lean on your friends for support."

    a "Thanks, Sarah. I needed to hear that."

    show amelia_sarah_hug
    with dissolve

    "The conversation helps Amelia feel more grounded and supported."

    jump chapter_5_part_1_end

label talk_maya:
    show amelia_maya_garden
    with dissolve

    "Amelia decides to talk to Maya, seeking her wisdom and perspective."

    show maya_smiling_garden
    with dissolve

    maya "Amelia, it's good to see you. How are you holding up?"

    a "I've been struggling to balance my studies and personal life. Do you have any advice?"

    show maya_thoughtful
    with dissolve

    maya "Finding balance is a journey, not a destination. Listen to your inner voice, take time for self-care, and remember that it's okay to ask for help."

    a "Thank you, Maya. I appreciate your guidance."

    show amelia_maya_meditation
    with dissolve

    "Maya guides Amelia through a short meditation, helping her find a sense of peace and clarity."

    jump chapter_5_part_1_end

label chapter_5_part_1_end:
    show amelia_dorm_night
    with dissolve

    "As Amelia prepares for bed, she feels a renewed sense of determination and purpose."

    a "No matter what challenges come my way, I know I can face them. I'm ready for the next chapter."

    jump chapter_5_part_2


label chapter_5_part_2:
    show amelia_campus_morning
    with dissolve

    "Amelia wakes up feeling more balanced after the advice she received. Today, she's determined to make the most of her university experience."

    menu:
        "Focus on academics":
            $ AA += 1
            jump focus_academics
        
        "Spend time with friends":
            $ SI += 1
            jump spend_time_friends
        
        "Explore the occult path":
            $ OK += 1
            jump explore_occult_path

label focus_academics:
    show lecture_hall
    with dissolve

    "Amelia heads to her morning lecture, ready to dive into today's material."

    show professor_lecturing
    with dissolve

    "The lecture is engaging, and Amelia finds herself deeply absorbed in the discussion."

    show amelia_raised_hand
    with dissolve

    "During the lecture, Amelia raises her hand to ask a question."
    a "Professor, how do ethical considerations in psychological research evolve with societal changes?"

    show professor_nodding
    with dissolve

    professor "Excellent question, Amelia. Ethical standards in research are indeed influenced by societal values, which change over time. This evolution ensures that research practices remain respectful and just."

    "After the lecture, Amelia decides to visit the library to work on her assignments."

    show amelia_library
    with dissolve

    "As she works, she notices a familiar face—Sophia, her academic rival."

    show sophia_studying
    with dissolve

    sophia "Amelia, fancy seeing you here. How's the research coming along?"

    menu:
        "Engage in a friendly conversation":
            $ SI += 1
            jump friendly_conversation_sophia
        
        "Engage in a competitive conversation":
            $ AA += 1
            jump competitive_conversation_sophia

label friendly_conversation_sophia:
    show amelia_smiling_sophia
    with dissolve

    a "Hi, Sophia. It's going well. How about you?"

    show sophia_smiling
    with dissolve

    sophia "It's going great. I just finished a fascinating paper on cognitive biases. We should compare notes sometime."

    a "That sounds like a good idea. It's always interesting to hear different perspectives."

    "The friendly conversation boosts Amelia's spirits and helps her focus better on her work."

    jump academic_pressure_part2

label competitive_conversation_sophia:
    show amelia_determined_sophia
    with dissolve

    a "Hi, Sophia. It's going well. I'm working on a paper about the ethical implications of AI in psychology. It's quite challenging."

    show sophia_smiling
    with dissolve

    sophia "That sounds intense. I'm focusing on cognitive biases at the moment. Let's see who gets published first."

    a "Challenge accepted. May the best paper win."

    "The competitive exchange motivates Amelia to push herself even harder in her studies."

    jump academic_pressure_part2

label academic_pressure_part2:
    show amelia_library_night
    with dissolve

    "As night falls, Amelia realizes she's been in the library for hours. She decides to call it a day and head back to her dorm."

    menu:
        "Talk to Lucas about study techniques (+AA, +SI)":
            $ AA += 1
            $ SI += 1
            jump talk_lucas_study

        "Review notes and prepare for the next day (+AA)":
            $ AA += 1
            jump review_notes

label talk_lucas_study:
    show amelia_lucas_dorm
    with dissolve

    "Back in her dorm, Amelia finds Lucas and asks him for some study techniques."

    show lucas_smiling_dorm
    with dissolve

    lucas "Hey, Amelia. How was your day? Need some study tips?"

    a "It was productive but exhausting. I'd love some tips on managing my workload better."

    show lucas_thoughtful
    with dissolve

    lucas "Sure thing. I recommend using a time-blocking method. Allocate specific times for different tasks and stick to it. Also, make sure to take short breaks to stay refreshed."

    a "Thanks, Lucas. I'll give that a try."

    "Armed with new study techniques, Amelia feels more confident about managing her workload."

    jump chapter_5_part_2_end

label review_notes:
    show amelia_studying_dorm
    with dissolve

    "Amelia spends the rest of the evening reviewing her notes and preparing for the next day's lectures."

    show amelia_tired_dorm
    with dissolve

    a "(I need to stay on top of my studies. Tomorrow's another busy day.)"

    jump chapter_5_part_2_end

label spend_time_friends:
    show student_union
    with dissolve

    "Amelia decides to spend time with her friends at the Student Union."

    show amelia_lucas_raj_union
    with dissolve

    "She finds Lucas and Raj chatting in the lounge."

    raj "Hey, Amelia! Come join us. We're just talking about the upcoming campus festival."

    menu:
        "Discuss festival plans (+SI)":
            $ SI += 1
            jump discuss_festival_plans
        
        "Talk about personal challenges (+MH, +SI)":
            $ MH += 1
            $ SI += 1
            jump talk_personal_challenges

label discuss_festival_plans:
    show amelia_smiling_union
    with dissolve

    a "Sure! What are the plans for the festival?"

    show lucas_smiling_union
    with dissolve

    lucas "There are going to be food stalls, music performances, and even a talent show. We should all participate."

    show amelia_excited_union
    with dissolve

    a "That sounds like fun. Maybe we could do a group performance?"

    raj "Absolutely! Let's sign up and start practicing."

    "The discussion about the festival lifts everyone's spirits and strengthens their bond."

    jump festival_preparations

label talk_personal_challenges:
    show amelia_serious_union
    with dissolve

    a "Actually, I've been feeling a bit overwhelmed with everything lately. How are you guys managing?"

    show raj_nodding_union
    with dissolve

    raj "It's been tough, but I'm trying to take it one day at a time. Talking to friends helps a lot."

    show lucas_thoughtful_union
    with dissolve

    lucas "Yeah, we're all in this together. Don't hesitate to reach out if you need to talk, Amelia."

    a "Thanks, guys. It really helps to know I have your support."



    "The conversation helps Amelia feel more supported and connected to her friends."

    jump friendship_strengthening
    
label festival_preparations:
    show student_union
    with dissolve

    "As the festival approaches, Amelia and her friends start preparing for their group performance."

    show amelia_raj_lucas_practice
    with dissolve

    "They spend their evenings practicing, each bringing their unique talents to the group."

    show amelia_happy_practice
    with dissolve

    a "This is coming together really well! I can't wait for the festival."

    raj "Me too! It's going to be a blast."

    "Their preparations strengthen their friendship and build excitement for the upcoming event."

    jump friendship_strengthening
    
label friendship_strengthening:
    show amelia_dorm_night
    with dissolve

    "That night, Amelia reflects on the day and the bond she shares with her friends."

    a "(I'm so grateful for Lucas and Raj. Their support means the world to me.)"

    menu:
        "Reach out to Zara (+SI)":
            $ SI += 1
            jump reach_out_zara
        
        "Spend time reflecting (+MH)":
            $ MH += 1
            jump reflect_alone

label reach_out_zara:
    show amelia_zara_cafeteria
    with dissolve

    "Amelia decides to reach out to Zara, who she hasn't seen much of lately."

    show zara_smiling_cafeteria
    with dissolve

    zara "Hey, Amelia! It's been a while. How are you?"

    a "I'm good, Zara. Just busy with classes and everything. How about you?"

    show zara_thoughtful_cafeteria
    with dissolve

    zara "Same here. It's been a hectic semester. But I'm glad we could catch up."

    "The two spend time chatting and catching up, strengthening their friendship."

    jump chapter_5_part_2_end

label reflect_alone:

    show amelia_meditating_dorm
    with dissolve

    "Amelia spends some time alone, reflecting on her experiences and practicing self-care."

    a "(Taking time for myself is important too. I need to make sure I'm balanced and centered.)"

    "The quiet time helps Amelia recharge and gain clarity on her priorities."

    jump chapter_5_part_2_end

label explore_occult_path:
    if OK >= 5:
        show amelia_secret_meeting
        with dissolve

        "Amelia decides to attend a secret society meeting she's been invited to, curious about the occult knowledge they offer."

        show occult_leader_speaking
        with dissolve

        occult_leader "Welcome, Amelia. Tonight, we delve into the mysteries of the mind and the unseen world."

        show amelia_listening_intently
        with dissolve

        "Amelia listens intently as the leader speaks, feeling a deep connection to the knowledge being shared."

        menu:
            "Participate in a ritual (+OK, -SI)":
                $ OK += 1
                $ SI -= 1
                jump participate_ritual
            
            "Study esoteric texts (+OK, +SD)":
                $ OK += 1
                $ SD += 1
                jump study_esoteric_texts

label participate_ritual:
    show ritual_circle
    with dissolve

    "Amelia decides to participate in a ritual, eager to deepen her understanding of the occult."

    show amelia_ritual_participation
    with dissolve

    occult_leader "As we join hands and focus our energies, feel the power of the circle guiding and protecting you."

    a "(This is intense, but I can feel a profound energy here.)"

    "The ritual leaves Amelia feeling more connected to the occult path, but she knows she must balance this with her social life."

    jump occult_path_continued

label study_esoteric_texts:
    show amelia_studying_texts
    with dissolve


    "Amelia chooses to study esoteric texts, fascinated by the hidden knowledge they contain."

    show amelia_absorbed_study
    with dissolve

    a "(These texts are complex, but they offer such deep insights into the nature of reality.)"

    "Her studies deepen her understanding and spark new questions about the world and her place in it."

    jump occult_path_continued

label occult_path_continued:
    show amelia_dorm_night
    with dissolve

    "Back in her dorm, Amelia reflects on the night's events and the knowledge she's gained."

    a "(The occult path is challenging, but it's also incredibly rewarding. I need to balance this with my other commitments.)"

    menu:
        "Share experiences with Maya (+OK, +SD)":
            $ OK += 1
            $ SD += 1
            jump share_with_maya
        
        "Keep experiences to yourself (+MH)":
            $ MH += 1
            jump keep_experiences_private

label share_with_maya:
    show amelia_maya_cafe
    with dissolve

    "Amelia decides to share her experiences with Maya, seeking her perspective."

    show maya_listening_cafe
    with dissolve

    maya "It sounds like you're really connecting with the occult path, Amelia. Remember to stay grounded and balanced."

    a "Thanks, Maya. Your guidance means a lot to me."

    "Sharing her experiences helps Amelia feel more confident and supported on her journey."

    jump chapter_5_part_2_end

label keep_experiences_private:
    show amelia_reflecting_dorm
    with dissolve

    "Amelia decides to keep her experiences to herself, reflecting on what she's learned."

    a "(Sometimes it's best to process things on my own. I'll share when the time is right.)"

    "The private reflection helps Amelia integrate her experiences and gain clarity."

    jump chapter_5_part_2_end

label chapter_5_part_2_end:
    show amelia_dorm_night
    with dissolve

    "As Amelia prepares for bed, she feels a renewed sense of purpose and balance."

    a "Whatever challenges come my way, I'm ready. This is just the beginning of my journey."

    jump chapter_5_part_3

label chapter_5_part_3:
    show amelia_dorm_morning
    with dissolve

    "Amelia wakes up with a sense of anticipation for the day ahead. She knows that balancing her studies, friendships, and personal growth is essential."

    menu:
        "Focus on academic research":
            $ AA += 1
            jump academic_research

        "Spend time with friends":
            $ SI += 1
            jump social_time

        "Explore personal growth":
            $ SD += 1
            jump personal_growth

label academic_research:
    show amelia_research_lab
    with dissolve

    "Amelia heads to the psychological research lab, eager to work on her current project."

    show prof_hawthorne_research_lab
    with dissolve

    prof_hawthorne "Good morning, Amelia. I see you're ready to dive into the data analysis today."

    a "Absolutely, Professor. I'm excited to see what insights we can uncover."

    "They spend the morning reviewing data and discussing their findings."

    menu:
        "Propose a new hypothesis (+AA, +MC)":
            $ AA += 1
            $ MC += 1
            jump propose_hypothesis

        "Focus on detailed analysis (+AA, +SD)":
            $ AA += 1
            $ SD += 1
            jump detailed_analysis

label propose_hypothesis:
    show amelia_thinking_lab
    with dissolve

    a "Professor, I've been thinking. What if we explore the impact of social media usage on self-esteem and mental health in our study?"

    show prof_hawthorne_nodding
    with dissolve

    prof_hawthorne "That's an excellent idea, Amelia. It would add a contemporary angle to our research. Let's incorporate that into our next phase."

    "Amelia feels proud of her contribution and eager to see the project evolve."

    jump research_discussion

label detailed_analysis:
    show amelia_studying_lab
    with dissolve

    "Amelia focuses on a detailed analysis of the current data, uncovering subtle patterns and correlations."

    show prof_hawthorne_impressed
    with dissolve

    prof_hawthorne "Impressive work, Amelia. Your attention to detail is exactly what this project needs."

    a "Thank you, Professor. I'm learning so much through this process."

    "Her dedication to the analysis enhances the quality of their research."

    jump research_discussion

label research_discussion:
    show amelia_dorm_afternoon
    with dissolve

    "After the productive morning in the lab, Amelia heads back to her dorm for a quick break."

    menu:
        "Review notes and prepare for tomorrow (+AA)":
            $ AA += 1
            jump review_notes_tomorrow

        "Take a walk to clear your mind (+MH)":
            $ MH += 1
            jump walk_campus

label review_notes_tomorrow:
    show amelia_studying_dorm
    with dissolve

    "Amelia spends some time reviewing her notes and preparing for the next day's tasks."

    a "(Staying organized and ahead of my work really helps reduce stress.)"

    "Feeling well-prepared, Amelia looks forward to the next day."

    jump chapter_5_part_3_end

label walk_campus:
    show amelia_walking_campus
    with dissolve

    "Amelia decides to take a walk around campus to clear her mind."

    show amelia_at_hoe_park
    with dissolve

    "She finds herself at Hoe Park, taking in the fresh air and beautiful scenery."

    menu:
        "Run into Tasha (+MC)":
            $ MC += 1
            jump run_into_tasha

        "Meet a new character, Michael (+MC, +SI)":
            $ MC += 1
            $ SI += 1
            jump meet_michael

label run_into_tasha:
    show tasha_confronting
    with dissolve

    "While walking through the park, Amelia unexpectedly runs into Tasha."

    tasha "Well, if it isn't Amelia. Still playing the goody-two-shoes, I see."

    menu:
        "Stand up to Tasha (+MC)":
            $ MC += 1
            jump stand_up_tasha

        "Try to defuse the situation (+SI)":
            $ SI += 1
            jump defuse_tasha

label stand_up_tasha:
    show amelia_determined_tasha
    with dissolve

    a "I'm just trying to make the most of my time here, Tasha. There's nothing wrong with that."

    show tasha_surprised
    with dissolve

    tasha "Hmph. Well, don't get in my way."

    "Tasha walks away, and Amelia feels a sense of accomplishment for standing up for herself."

    jump walk_continued

label defuse_tasha:
    show amelia_calm_tasha
    with dissolve

    a "I'm not looking for trouble, Tasha. Let's just go our separate ways."

    show tasha_indifferent
    with dissolve

    tasha "Whatever."

    "Tasha leaves, and Amelia continues her walk, feeling relieved."

    jump walk_continued

label meet_michael:
    show michael_introducing
    with dissolve

    "While walking through the park, Amelia meets a new student, Michael, who is handing out flyers."

    michael "Hey, I'm Michael. We're organizing a protest against the university's investment in fossil fuels. Would you be interested in joining us?"

    menu:
        "Join the protest (+MC, +SI)":
            $ MC += 1
            $ SI += 1
            jump join_protest

        "Decline politely (+MC)":
            $ MC += 1
            jump decline_protest

label join_protest:
    show amelia_michael_protest
    with dissolve

    a "Sure, Michael. I think it's important to take a stand on these issues."

    michael "Great! We're meeting at the Student Union tomorrow. See you there!"

    "Amelia feels a sense of purpose as she agrees to join the protest."

    jump walk_continued

label decline_protest:
    show amelia_michael_decline
    with dissolve

    a "I support the cause, but I'm really busy with my studies right now. Maybe next time."

    michael "No problem. Thanks for considering it."

    "Amelia feels good about being honest while also standing up for her values."

    jump walk_continued

label walk_continued:
    show amelia_walking_park
    with dissolve

    "Amelia continues her walk, feeling refreshed and more balanced."

    jump chapter_5_part_3_end

label social_time:
    show student_union
    with dissolve

    "Amelia decides to spend time with her friends at the Student Union."

    show amelia_zara_sarah_union
    with dissolve

    "She finds Zara and Sarah sitting together."

    zara "Hey, Amelia! We're just planning our weekend. Want to join us?"

    menu:
        "Make weekend plans (+SI)":
            $ SI += 1
            jump weekend_plans

        "Talk to Sarah about her mental health (+MH, +SI)":
            $ MH += 1
            $ SI += 1
            jump talk_sarah_health

label weekend_plans:
    show amelia_smiling_union
    with dissolve

    a "Absolutely! What do you have in mind?"

    show zara_thoughtful_union
    with dissolve

    zara "We were thinking of going to the Barbican. There's a new art exhibit and some great cafes to check out."

    a "That sounds perfect. I'm in!"

    "They finalize their plans and enjoy the rest of the afternoon together."

    jump friendship_strengthening_part3

label talk_sarah_health:
    show amelia_concerned_sarah
    with dissolve

    a "Sarah, how have you been feeling lately? I've been worried about you."

    show sarah_sighing_union
    with dissolve

    sarah "It's been tough, Amelia. Some days are better than others, but I'm managing."

    menu:
        "Offer to help her find resources (+MH, +SI)":
            $ MH += 1
            $ SI += 1
            jump help_sarah_resources

        "Invite her to a self-care activity (+MH)":
            $ MH += 1
            jump invite_self_care

label help_sarah_resources:
    show amelia_supportive_sarah
    with dissolve

    a "Maybe we can look into some resources together? The university has great counseling services."

    show sarah_smiling_union
    with dissolve

    sarah "I'd appreciate that, Amelia. It's hard to take that first step alone."

    a "I'll be there with you. You're not alone in this."

    "Amelia feels closer to Sarah as they plan to seek help together."

    jump friendship_strengthening_part3

label invite_self_care:
    show amelia_inviting_sarah
    with dissolve

    a "How about we do something relaxing this weekend? Maybe a yoga class or a spa day?"

    show sarah_smiling_union
    with dissolve

    sarah "That sounds wonderful. I think I could really use that."

    a "It's a plan then. We'll take some time to relax and recharge."

    "Amelia feels good about supporting Sarah in a positive way."

    jump friendship_strengthening_part3

label friendship_strengthening_part3:
    show amelia_dorm_evening
    with dissolve

    "That evening, Amelia reflects on her day with a sense of fulfillment."

    a "(I'm really glad I took the time to connect with Zara and Sarah. Our friendship is stronger than ever.)"

    "She goes to bed feeling more balanced and ready for whatever comes next."

    jump chapter_5_part_3_end

label personal_growth:
    show amelia_library
    with dissolve

    "Amelia decides to focus on her personal growth by studying esoteric texts in the library."

    show amelia_studying_library
    with dissolve

    "She finds a quiet corner and immerses herself in the ancient knowledge."

    menu:
        "Study ancient philosophies (+SD)":
            $ SD += 1
            jump study_philosophies

        "Research occult practices (+OK, +SD)":
            $ OK += 1
            $ SD += 1
            jump research_occult

label study_philosophies:
    show amelia_reading_book
    with dissolve

    "Amelia delves into ancient philosophies, exploring different perspectives on life and the universe."

    a "(These ideas are so profound. They really make me think about my own beliefs and values.)"

    "She gains new insights and feels more connected to her personal growth journey."

    jump personal_growth_continued

label research_occult:
    show amelia_researching_occult
    with dissolve

    "Amelia researches various occult practices, fascinated by the hidden knowledge and rituals."

    a "(There's so much to learn about the unseen world. This is both exciting and challenging.)"

    "Her studies deepen her understanding of the occult and enhance her personal growth."

    jump personal_growth_continued

label personal_growth_continued:
    show amelia_dorm_evening
    with dissolve

    "Back in her dorm room, Amelia reflects on what she learned."

    a "(Today was a good day. I feel more grounded and enlightened.)"

    "She feels a sense of accomplishment and peace as she prepares for bed."

    jump chapter_5_part_3_end

label chapter_5_part_3_end:
    show amelia_dorm_night
    with dissolve

    "As Amelia settles in for the night, she feels a renewed sense of purpose and balance."

    a "Whatever challenges come my way, I'm ready. This is just the beginning of my journey."

    "Her dreams are filled with symbols of growth and transformation, hinting at the profound changes ahead."

    jump chapter_6
