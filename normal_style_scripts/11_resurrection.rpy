label chapter_11_part_1:
    show amelia_studying_in_dorm_room
    with dissolve
    
    "Amelia sits at her desk, surrounded by a sea of textbooks, notes, and empty coffee cups. The end of her first year at Plymouth University is approaching, and with it, a daunting array of final exams and projects."
    
    show amelia_looking_at_calendar_stressed
    with dissolve
    
    a "(Two weeks. Just two more weeks and I'll have made it through my first year. But there's still so much to do...)"
    
    "She glances at her calendar, every square packed with deadlines, study sessions, and final events."
    
    show amelia_receives_text_from_lucas
    with dissolve
    
    "Just as she's about to dive back into her study guide, her phone buzzes with a text from Lucas."

    lucas "{i}Hey Amelia! A bunch of us are getting together at the Union tonight to blow off some pre-exam steam. You in?{/i}"
    
    show amelia_considering_text_message
    with dissolve
    
    "Amelia hesitates, glancing back at her pile of work. The responsible part of her knows she should stay focused. But another part, the part that's been feeling increasingly burned out and isolated, yearns for a break and some friendly company."
    
    menu:
        "Agree to meet up with friends":
            $ SI += 1
            jump meet_up_with_friends_2
        
        "Decline and focus on studying":
            $ AA += 1
            jump decline_and_study
        
label meet_up_with_friends_2:
    show amelia_texting_lucas_yes
    with dissolve
    
    a "{i}Count me in! I could definitely use a breather. See you there!{/i}"
    
    show amelia_getting_ready_to_go_out
    with dissolve
    
    "Amelia closes her books, deciding that a few hours of relaxation and socialization will probably do her more good than trying to cram any more information into her exhausted brain."
    
    scene bg student_union_night
    with dissolve
    
    show amelia_arriving_at_student_union
    with dissolve
    
    "A short while later, Amelia enters the bustling Student Union, spotting her friends gathered around a table in the corner."
    
    show amelia_greeting_friends_at_table
    with dissolve
    
    a "Hey everyone! Thanks for the invite, Lucas. I didn't realize how much I needed this until right now."
    
    show lucas_smiling_at_amelia
    with dissolve
    
    lucas "Anytime, Amelia. We're all in the same boat here - just trying to survive finals season."
    
    show zara_raising_glass_to_toast
    with dissolve
    
    zara "And what better way to do that than with good friends and a few drinks? Cheers to making it through our first year!"
    
    show raj_and_others_raising_glasses
    with dissolve
    
    "Everyone raises their glasses, clinking them together in a toast."
    
    show amelia_smiling_and_drinking
    with dissolve
    
    "As the evening progresses, Amelia finds herself relaxing and laughing more than she has in weeks. The stresses of exams and the bittersweet anticipation of the year's end seem to fade, replaced by the warmth of camaraderie."
    
    show lucas_leaning_in_to_talk_to_amelia
    with dissolve
    
    lucas "So, Amelia, what's your plan for the summer? Heading back home?"
    
    show amelia_thinking_about_summer_plans
    with dissolve
    
    a "I think so, at least for a bit. It'll be good to spend some time with my family and recharge. But I'm also considering applying for a summer research position here. I feel like I'm just starting to hit my stride with my studies, you know?"

    show zara_curious_about_research
    with dissolve
    
    zara "Ooh, a summer research position? That sounds amazing! What area are you thinking of focusing on?"
    
    menu:
        "Discuss interest in clinical psychology":
            $ AA += 1
            $ SD += 1
            show amelia_passionate_about_clinical_psych
            with dissolve
            
            a "I'm really drawn to clinical psychology. After everything that happened with Sarah this year, I feel more determined than ever to understand mental health and how to support those who are struggling."
            
            show lucas_impressed_by_amelia
            with dissolve
            
            lucas "That's incredible, Amelia. Your passion and empathy are truly inspiring."
            
            show raj_agreeing_with_lucas
            with dissolve
            
            raj "I second that. The world needs more people like you, Amelia - people who are dedicated to making a real difference in others' lives."
            
        "Express fascination with neuropsychology":
            $ AA += 1
            $ SD += 1
            show amelia_excited_about_neuropsych
            with dissolve
            
            a "I've been absolutely fascinated by my neuropsychology classes this semester. The way the brain works, how it shapes our thoughts, emotions, and behaviors... I feel like I could spend a lifetime exploring it and still barely scratch the surface."
            
            show zara_relating_to_amelia
            with dissolve
            
            zara "I totally get that. Every time I learn something new about the brain, it's like a whole new world opens up. It's thrilling and humbling all at once."
            
            show lucas_curious_about_research
            with dissolve
            
            lucas "That's so cool, Amelia. What kind of neuropsych research are you interested in pursuing?"
            
    show amelia_reflecting_on_goals
    with dissolve
        
    a "Honestly, I'm still figuring that out. But I know I want to contribute to the field in a meaningful way, whether that's through research, clinical work, or both."
        
    show amelia_thanking_friends
    with dissolve
        
    a "I'm just grateful to have had such an incredible first year, and to have met all of you. I feel like I've grown so much, both academically and personally."
        
    show friends_smiling_at_amelia
    with dissolve
        
    "Amelia's friends all smile at her, clearly sharing the sentiment."
        
    lucas "We're grateful for you too, Amelia. And we're all excited to see where your journey takes you."
        
    show amelia_feeling_supported
    with dissolve
        
    "Amelia feels a rush of warmth and gratitude. Despite the challenges of the year - or perhaps because of them - she feels a deep sense of belonging and purpose."
        
    jump chapter_11_part_2
        
label decline_and_study:
    show amelia_texting_lucas_no
    with dissolve
    
    a "{i}Sorry Lucas, I'd better focus on studying tonight. Raincheck? Good luck with your exams!{/i}"
    
    show amelia_sighing_and_studying
    with dissolve
    
    "With a sigh, Amelia silences her phone and turns back to her books. As much as she'd love a break, she knows how crucial these final exams are."
    
    a "(I can relax once it's all over. For now, I need to stay focused.)"
    
    "She dives back into her notes, the words blurring slightly from the long hours of reading. She rubs her eyes, trying to clear her vision and her mind."
    
    show amelia_thinking_about_year
    with dissolve
    
    "As she studies, Amelia's thoughts wander to the events of the year. The classes that inspired her, the friends she made, the challenges she overcame."
    
    if sarah_alive:
        show amelia_reflecting_on_sarah
        with dissolve
        
        "She thinks of Sarah, of how close she came to losing her friend. The memory is still painful, but it's also a reminder of Amelia's own strength and the importance of her chosen path."
        
    else:
        show amelia_grieving_sarah
        with dissolve
        
        "She thinks of Sarah, the pain of her loss still raw and heavy. Amelia knows she'll carry this grief forward, but she also knows that it has given her a profound sense of purpose. She studies not just for herself, but in memory of her friend."
        
    show amelia_determined_to_succeed
    with dissolve
    
    "With a renewed sense of determination, Amelia refocuses on her work. She knows the road ahead won't be easy, but she's ready to face it head-on."
    
    a "(One exam at a time, one day at a time. I've got this.)"
    
    "She studies late into the night, the quiet of her dorm room broken only by the turning of pages and the scratching of her pen."
    
    jump chapter_11_part_2

label chapter_11_part_2:
    scene bg library
    with dissolve
    
    show amelia_studying_in_library
    with dissolve
    
    "The days leading up to finals pass in a blur of caffeine-fueled study sessions and last-minute assignments. Amelia feels like she's running on adrenaline and sheer determination."
    
    show amelia_looking_exhausted
    with dissolve
    
    a "(Just a little longer. I can do this. I have to do this.)"
    
    "She's in the library, surrounded by towering stacks of books and notes, when she feels a tap on her shoulder."
    
    show sophia_standing_by_amelia
    with dissolve
    
    sophie "Amelia, hey. I thought I might find you here."
    
    show amelia_surprised_to_see_sophia
    with dissolve
    
    a "Sophia! Hi. Yeah, I've pretty much been living here the past week. What's up?"
    
    show sophia_looking_nervous
    with dissolve
    
    sophie "I... I was hoping we could talk. About the research assistant position for next year."
    
    show amelia_curious
    with dissolve
    
    a "Oh? What about it?"
    
    sophie "Well, I know we've both applied, and I just wanted to say... if you get it, I'll be really happy for you. You deserve it."
    
    show amelia_touched
    with dissolve
    
    a "Sophia, that's... that's really kind of you. But you deserve it too. Your work has been incredible this year."
    
    show sophia_smiling
    with dissolve
    
    sophie "Thanks, Amelia. I guess what I'm trying to say is, no matter who gets it, I'm glad we've had each other to push us this year. Your brilliance has inspired me to work harder."
    
    show amelia_smiling_at_sophia
    with dissolve
    
    a "I feel the same way, Sophia. We've come a long way from being rivals, haven't we?"
    
    show sophia_laughing
    with dissolve
    
    sophie "We have. And I'm grateful for that. Friends?"
    
    show amelia_shaking_sophias_hand
    with dissolve
    
    a "Friends."
    
    hide sophia_laughing
    with dissolve
    
    "As Sophia leaves, Amelia feels a warmth in her chest. It's funny how competition can turn into camaraderie, how challenges can forge connections."
    
    jump final_exams

label final_exams:
    show amelia_taking_exams
    with dissolve
    
    "The final exams are as grueling as Amelia anticipated. She pours everything she's learned, all her hard-won knowledge and insights, into each answer."
    
    show amelia_looking_pensive
    with dissolve
    
    a "(This is it. The culmination of everything. I've given it my all. I can only hope it's enough.)"
    
    if AA >= 15:
        show amelia_feeling_confident
        with dissolve
        "As she turns in her last exam, Amelia feels a sense of satisfaction. She's tackled every challenge head-on, and she knows her hard work will pay off."
    else:
        show amelia_looking_uncertain
        with dissolve
        "As she turns in her last exam, Amelia feels a mix of relief and uncertainty. She's done her best, but the year has been full of so many challenges. She can only hope she's done enough."
        
    jump end_of_year_event

label end_of_year_event:
    scene bg banquet_hall
    with dissolve
    
    show amelia_arriving_at_event
    with dissolve
    
    "The end-of-year banquet is a bittersweet affair, a celebration of all that's been achieved and a farewell to the graduating class."
    
    show amelia_mingling_with_friends
    with dissolve
    
    "Amelia mingles with her friends and classmates, exchanging memories and well-wishes."
    
    show lucas_raising_glass
    with dissolve
    
    lucas "To the end of an era, and to new beginnings!"
    
    show amelia_and_friends_toasting
    with dissolve
    
    a "Cheers!"
    
    if SI >= 15:
        show amelia_receiving_gift
        with dissolve
        "As the night goes on, Amelia's friends pull her aside. They present her with a scrapbook, filled with photos and mementos from their year together."
        
        show zara_smiling
        with dissolve
        zara "We wanted you to have something to remember us by, Amelia. You've been such an important part of our lives this year."
        
        show amelia_hugging_friends
        with dissolve
        a "You guys... this is incredible. I don't know what to say. I'm going to miss you all so much."
        
        show raj_putting_hand_on_amelias_shoulder
        with dissolve
        raj "We'll miss you too, Amelia. But we know you're going to do amazing things. This is just the beginning for you."
        
    else:
        "Amelia enjoys the celebration, but she can't shake a feeling of disconnection. It's like she's observing the festivities from outside, not quite a part of them."
        
        show amelia_looking_pensive
        with dissolve
        a "(So much has changed this year, myself most of all. Do I still fit in here? Do I still belong?)"
        
        "She slips out of the banquet hall early, preferring the quiet of her own thoughts to the noise of the crowd."
        
    jump final_meeting_with_mentor

label final_meeting_with_mentor:
    if mentor == "Professor Hawthorne":
        show amelia_knocking_on_hawthornes_door
        with dissolve
        "The day after the banquet, Amelia finds herself standing outside Professor Hawthorne's office. She takes a deep breath and knocks."
        
        show hawthorne_inviting_amelia_in
        with dissolve
        hawthorne "Amelia, come in. I've been expecting you."
        
        show amelia_sitting_with_hawthorne
        with dissolve
        "Amelia sits down, suddenly feeling nervous. Professor Hawthorne has been such an important figure in her journey this year. His opinion matters to her, more than she realized."
        
        show hawthorne_leaning_forward
        with dissolve
        hawthorne "Amelia, I wanted to tell you how impressed I've been with your work this year. You've shown a dedication and insight that's rare in a first-year student."
        
        if AA >= 18:
            show hawthorne_smiling_proudly
            with dissolve
            hawthorne "In fact, I've recommended you for the Psychological Science Award. It's given to the first-year student who's shown the most promise in the field."
            
            show amelia_surprised_and_honored
            with dissolve
            a "Professor Hawthorne, I... I don't know what to say. Thank you. This means so much to me."
            
            show hawthorne_nodding
            with dissolve
            hawthorne "You've earned it, Amelia. Your work speaks for itself. Keep following your passions, and there will be no limit to what you can achieve."
            
        else:
            show hawthorne_looking_serious
            with dissolve
            hawthorne "I know this year has been challenging for you, Amelia. You've faced obstacles that would have set back many students. But you've persevered, and you've grown. That's a testament to your strength of character."
            
            show amelia_looking_grateful
            with dissolve
            a "Thank you, Professor. I couldn't have done it without your guidance and support. You've taught me so much, not just about psychology, but about myself."
            
            show hawthorne_smiling_warmly
            with dissolve
            hawthorne "That's the true value of education, Amelia. It's not just about the knowledge we gain, but the wisdom. And you've shown a great capacity for both."
            
    elif mentor == "Dr. Simmons":
        show amelia_meeting_with_simmons
        with dissolve
        "Amelia meets with Dr. Simmons in her cozy office, the same one where they've had so many heart-to-heart conversations over the year."
        
        show simmons_smiling_at_amelia
        with dissolve
        simmons "Amelia, it's hard to believe the year is over. It feels like just yesterday you walked into my office for the first time, eager and a little bit nervous."
        
        show amelia_laughing
        with dissolve
        a "I remember that day. I had no idea then how much I was going to learn, not just about psychology, but about life."
        
        show simmons_looking_proud
        with dissolve
        simmons "And you've learned so much, Amelia. You've grown in ways that have been truly inspiring to watch."
        
        if MH >= 18:
            show simmons_handing_amelia_a_gift
            with dissolve
            simmons "I have something for you. It's a little token of my appreciation for all your hard work and dedication."
            
            show amelia_opening_gift
            with dissolve
            "Amelia opens the gift. It's a beautifully bound journal, with an inscription on the first page: 'To Amelia, who has the courage to face her truth and the compassion to help others do the same.'"
            
            show amelia_tearing_up
            with dissolve
            a "Dr. Simmons, this is... this is so meaningful. I don't know how to thank you."
            
            show simmons_hugging_amelia
            with dissolve
            simmons "You already have, Amelia. By being who you are, and by never giving up on yourself or others. Keep writing your story. I know it's going to be an extraordinary one."
            
        else:
            show simmons_looking_serious
            with dissolve
            simmons "Amelia, I know this year has been a rollercoaster for you. You've faced challenges that have tested your strength and your faith in yourself."
            
            show amelia_nodding
            with dissolve
            a "It has been tough. There were times I wasn't sure I could keep going. But I did, thanks in large part to your support and guidance."
            
            show simmons_smiling_gently
            with dissolve
            simmons "You did the hard work, Amelia. You faced your fears, your doubts, your pain. And you've come out the other side stronger and wiser. That's all you."
            
            show amelia_looking_determined
            with dissolve
            a "I still have a lot to learn. But I feel ready now, ready to keep growing and facing whatever comes next."
            
            simmons "And I have no doubt you will, Amelia. Remember, my door is always open to you. Even after you leave Plymouth, you'll always have a supporter and a friend in me."
            
    elif mentor == "Maya":
        show amelia_walking_with_maya
        with dissolve
        "Amelia and Maya walk through the blooming university gardens, a place that's become sacred to their friendship and spiritual journey."
        
        show maya_admiring_flowers
        with dissolve
        maya "The cycle of life, of death and rebirth, is so beautifully represented in nature. The flowers bloom, they wither, and then they bloom again. Just like us."
        
        show amelia_looking_thoughtful
        with dissolve
        a "I feel like I've gone through that cycle this year. Parts of me have died, parts have been reborn. It's been painful, but also transformative."
        
        show maya_smiling_wisely
        with dissolve
        maya "That's the path of growth, Amelia. It's not always comfortable, but it's always worthwhile."
        
        if OK >= 18:
            show maya_holding_amelias_hands
            with dissolve
            maya "Amelia, your spiritual journey this year has been truly remarkable. You've delved into the mysteries of the universe with a courage and openness that's rare."
            
            show amelia_looking_peaceful
            with dissolve
            a "I feel like I'm just starting to understand the depth of it all, Maya. There's so much more I want to explore, to understand."
            
            show maya_nodding
            with dissolve
            maya "And you will, Amelia. The path of wisdom is a lifelong one. But you've taken the first and most important step: you've opened yourself to the journey."
            
            show amelia_receiving_a_talisman
            with dissolve
            "Maya presses a small, intricately carved stone into Amelia's hand."
            
            maya "This is a talisman of protection and guidance. It's been blessed by the spirits. Keep it with you, and it will remind you of your inner strength and connection to the divine."
            
            show amelia_looking_grateful
            with dissolve
            a "Maya, I don't know how to thank you. For this, for everything. You've opened my eyes to a whole new way of understanding the world and myself."
            
            maya "You've always had this wisdom within you, Amelia. I just helped you find the path to it. Keep walking that path, and trust where it leads you. Your journey is just beginning."
            
        else:
            show maya_looking_at_amelia
            with dissolve
            maya "Amelia, this year has been a time of great challenges and changes for you. You've been tested in ways that have shaken your understanding of yourself and the world."
            
            show amelia_nodding
            with dissolve
            a "It's true. There were times I felt lost, times I questioned everything. But through it all, our talks, the practices you've taught me, they've been a lifeline."
            
            show maya_smiling_gently
            with dissolve
            maya "And they will continue to be, Amelia. The wisdom of the ages, the connection to the divine, these are not fleeting things. They are always with you, always accessible to you."
            
            show amelia_looking_determined
            with dissolve
            a "I'm starting to understand that now. Starting to feel it. Even in the midst of confusion and pain, there's a peace, a truth that I can tap into."
            
            maya "That's the gift of the spiritual path, Amelia. It's not about avoiding life's challenges, but about meeting them with grace and wisdom. And you have shown such grace this year."
            
            show amelia_hugging_maya
            with dissolve
            a "Thank you, Maya. For being my guide, my friend, my spiritual companion. I feel so blessed to have you in my life."
            
            maya "And I feel blessed to walk this path with you, Amelia. Remember, wherever you go, you carry this wisdom, this connection, within you. It's your light to shine."
            
    jump chapter_11_part_3

label chapter_11_part_3:
    show amelia_sitting_in_auditorium
    with dissolve

    "The end-of-year ceremony is held in the grand university auditorium, a sea of students in caps and gowns filling the seats. Amelia feels a swirl of emotions as she takes her place among her peers."

    show amelia_looking_around_auditorium 
    with dissolve

    a "(To think, just a year ago, I was a bundle of nerves sitting in this very room for orientation. So much has happened since then...)"

    "Her mind floods with memories - the friendships forged, the challenges conquered, the painful losses and profound revelations. She replays key moments like flickering films in her mind's eye."

    show amelia_remembering_classes
    with dissolve

    a "(Those first few classes where everything felt so new and overwhelming... that lecture on cognitive psychology that sparked my fascination with the mind...)"

    show amelia_remembering_social_events  
    with dissolve

    a "(The night at the pub where I truly connected with Lucas, Zara and Raj... Sarah's birthday party, full of so much joy and possibility...)"

    if sarah_alive:
        show amelia_thankful_for_sarah
        with dissolve

        a "(And Sarah... our friendship, stronger than I ever could have dreamed after that dark night. She's living, breathing proof that miracles can happen.)"

    else:
        show amelia_grieving_sarah
        with dissolve

        a "(Sarah... my heart still aches when I think of her vibrant spirit, extinguished too soon. But in her memory, I've found strength and purpose I never knew I had.)"

    show dean_approaching_podium
    with dissolve

    "The dean's approach to the podium breaks Amelia from her reverie. After a pomp-filled opening, she begins reading out the names of distinguished students."

    if AA >= 20:
        show amelia_receives_top_academic_award
        with dissolve

        dean "...and for truly exceptional academic achievement, the highest honor a first-year student can receive, the Provost's Award goes to Amelia [Last Name]."

        show amelia_stunned_then_proud
        with dissolve
        
        "Amelia's jaw drops, her eyes widening in disbelief. Then a look of profound pride washes over her face. She rises and makes her way to the stage, cheered on by her awestruck friends and classmates."

        show amelia_receiving_award_from_dean
        with dissolve

        dean "Amelia has displayed a staggering breadth of intellect, dedication, and insight. Her contributions to the field of psychology have been invaluable, even at this early stage."
        
        dean "We can only imagine what profound impact her future work will have on our understanding of the human mind and experience. Congratulations, Amelia."

        show amelia_waving_to_friends  
        with dissolve

        "With her award in hand, Amelia waves to her beaming friends, overwhelmed with gratitude and a renewed sense of purpose. In this moment, she feels that anything is possible."

        $ AA += 3

    elif AA >= 18:
        show amelia_receives_academic_award
        with dissolve
        
        dean "...and for outstanding academic achievement in the field of psychological science, the award goes to Amelia [Last Name]."
        
        show amelia_stunned_then_proud
        with dissolve
        
        "Amelia's jaw drops, then her face breaks into a wide, proud grin. She rises and makes her way to the stage, cheered on by her friends and classmates."
        
        show amelia_receiving_award
        with dissolve
        
        dean "Amelia has displayed remarkable intellect, dedication, and insight throughout her first year. We have no doubt she will go on to make invaluable contributions to her chosen field."
        
        show amelia_waving_to_friends
        with dissolve
        
        "With her award in hand, Amelia waves to her beaming friends. In this moment, all her hard work has paid off in ways she could have never imagined."  
        
        $ AA += 2

    show amelia_looking_proud
    with dissolve

    a "(Who would have thought, a year ago, that I'd be standing here feeling so accomplished, so... capable? This was more than I could have ever dreamed.)"

    show michael_approaching_amelia  
    with dissolve

    michael "Amelia, congratulations! I have to admit, I'm a little jealous. But also totally inspired by you. You've really raised the bar for all of us." 

    show amelia_appreciating_michael
    with dissolve

    a "Michael, that's so kind of you to say. But you've been an inspiration to me as well, pushing me to work harder and think bigger. I'm honored to be your academic rival."

    michael "Here's to another year of friendly competition, then. May we continue to push each other towards greatness."

    show amelia_nodding
    with dissolve

    a "I'll drink to that."

    if SI >= 20:
        
        scene bg university_gardens
        with dissolve
        
        "After the ceremony, Amelia's friends surprise her by leading her to a quiet, secluded part of the university gardens she's never explored before."
        
        show zara_presenting_gift
        with dissolve
        
        zara "We know we gave you that first gift already, but we wanted you to have one more thing to remember all of us by. This time, from a very special place."
        
        show amelia_opening_gift  
        with dissolve
        
        "Amelia opens the delicately wrapped gift to reveal a pristine marble bench, an inscription along the backrest reading 'For Amelia, friend extraordinaire.'"
        
        show lucas_grinning  
        with dissolve
        
        lucas "We knew you loved finding little quiet nooks around campus to study or just... be. So we wanted to give you your own permanent sanctuary."
        
        show amelia_touched_by_gift
        with dissolve
        
        a "You guys... I'm speechless. This is, without a doubt, one of the most incredibly thoughtful gifts I've ever received."
        
        raj "That's because you've been one of the most incredibly thoughtful, caring friends we could have ever asked for, Amelia."
        
        show amelia_hugging_friends  
        with dissolve
        
        a "I don't know what I did to deserve all of you in my life, but I'm eternally grateful. No matter where our paths lead, we'll always have this place... and each other."
        
        $ SI += 2

    elif SI >= 18:
        
        show friends_giving_amelia_gift
        with dissolve
        
        "After the ceremony, Amelia's friends approach her with a gift, wrapped in colorful paper."
        
        show zara_smiling
        with dissolve
        
        zara "We know we gave you that scrapbook already, but we wanted you to have one more thing to remember us by."
        
        show amelia_opening_gift
        with dissolve
        
        "Amelia opens the gift to reveal a beautiful engraved picture frame. Inside is a photo of the entire group, arms around each other, laughing and radiating joy."
        
        show lucas_grinning
        with dissolve
        
        lucas "That was taken at the start of spring term. We wanted to capture that feeling of new beginnings and endless possibilities."
        
        show amelia_touched_by_gift
        with dissolve
        
        a "You guys... I'll cherish this forever. You've been the most incredible friends, supporting me through everything. I don't know where I'd be without all of you."
        
        show raj_hugging_amelia  
        with dissolve
        
        raj "And we're the ones who are grateful for you, Amelia. You've touched all our lives in ways you can't even imagine."
        
        $ SI += 1

    if OK >= 20:
        
        scene bg peaceful_garden  
        with dissolve
        
        show amelia_sitting_in_garden
        with dissolve
        
        "After the ceremony, Amelia seeks out a quiet moment of solitude in the university's most tranquil, secluded gardens. She sits beneath an ancient oak tree, soaking in the beauty and stillness around her."
        
        show amelia_looking_inward  
        with dissolve
        
        a "(A year ago, I couldn't have imagined how profoundly my soul would be tested and transformed. There were times I felt hopelessly lost...)"
        
        show amelia_remembering_struggles  
        with dissolve
        
        "She replays her darkest moments - the night Sarah was assaulted, her own brush with despair, the churning existential doubts that bubbled up within her."
        
        show amelia_finding_strength 
        with dissolve
        
        a "(But each time, I found the courage to face my truth, to embrace the mysteries of this universe and my place within it. Maya's teachings, her wisdom, gave me that strength.)"
        
        show amelia_holding_talisman  
        with dissolve
        
        "She runs her fingers over the intricately carved talisman, its powerful symbolism and energies flowing through her."
        
        a "(This physical world, this reality, is but a fragile illusion, a fleeting veil over the infinite cosmos.)"
        
        show amelia_looking_upward  
        with dissolve
        
        "Amelia lifts her gaze towards the filtered sunlight playing through the oak's branches, her eyes reflecting the eternal dance of energy and existence."
        
        show amelia_serene_smile
        with dissolve
        
        a "I am a part of that dance, always have been, always will be. And no matter how choreographed this reality may seem, I have the power to improvise."
        
        show amelia_releasing_talisman
        with dissolve
        
        "With a deep, cleansing breath, Amelia opens her hand and releases the talisman into the cosmic slipstream. She watches as it tumbles towards the ground, reality shifting around its descent."
        
        show amelia_at_peace  
        with dissolve
        
        a "(I am limitless, eternal, ever-becoming. The veil has lifted.)"
        
        $ OK += 2
        $ MH += 2

    elif OK >= 18:

        scene bg peaceful_garden
        with dissolve
        
        show amelia_sitting_in_garden  
        with dissolve
        
        "After the ceremony, Amelia seeks out a quiet moment of solitude in the university's tranquil gardens. She sits on a stone bench, soaking in the beauty and stillness around her."
        
        show amelia_looking_inward
        with dissolve
        
        a "(So much has happened this year, so much change and growth. And yet, in this moment, I feel a profound sense of peace.)"
        
        show amelia_holding_talisman
        with dissolve
        
        "She runs her fingers over the carved talisman Maya gifted her, feeling its rugged textures and imbuing it with all the wisdom and resilience she's cultivated."
        
        show amelia_serene_smile
        with dissolve
        
        a "(I know now that no matter what life brings, I can face it with grace. I am part of the eternal cycle, the dance of becoming. And I will keep dancing.)"
        
        show amelia_releasing_talisman  
        with dissolve
        
        "With a deep, cleansing breath, Amelia opens her hand and releases the talisman. She watches as it tumbles into the burbling stream beside her bench, carried away by the ever-flowing waters."
        
        show amelia_at_peace
        with dissolve
        
        a "(Onward. Always onward. Change is the only constant.)"
        
        $ OK += 1
        $ MH += 1  

    show amelia_looking_to_future  
    with dissolve

    "As the day's festivities wind down, Amelia finds herself alone for a few precious moments of quiet reflection on the year that has passed and all that is yet to come."

    menu:
        "Reflect on personal growth":
            $ MH += 2
            $ SD += 1
            
            show amelia_thoughtful
            with dissolve
            
            a "(A year ago, I was a such a different person - uncertain, insecure, struggling to find my place in the world.)"
            
            show amelia_remembering_challenges
            with dissolve
            
            "She revisits her deepest struggles - her crisis of identity upon arriving at university, the darkest moments with Sarah and her own brush with depression and doubt."
            
            show amelia_appreciating_growth
            with dissolve
            
            a "(But each hurdle was an invitation to dig deeper, to uncover new reserves of strength, resilience and self-understanding.)"
            
            a "I look at myself now and I barely recognize that scared, insecure girl from a year ago. The woman I've become is stronger, wiser, more compassionate and in tune with her true self."
            
            show amelia_determined_smile
            with dissolve
            
            a "(And this is just the beginning. With each new challenge awaiting me, I'll continue to evolve and grow into my highest self.)"
            
        "Focus on academic goals":
            $ AA += 2
            $ SD += 1
            
            show amelia_envisioning_future
            with dissolve
            
            a "(Just one year in, and already I've gained so much invaluable knowledge and experience. But it's merely a drop in the vast ocean of all there is left to discover.)"
            
            show amelia_pondering
            with dissolve
            
            "Her mind wanders to the realms of research and academia that lie ahead - complex theories to unravel, cutting-edge studies to assist with, perhaps even groundbreaking discoveries waiting to be unearthed."  
            
            a "(Whether my path leads me towards clinical work or a research vocation, I know my role is to elucidate the mysteries of the human mind and psyche.)"
            
            show amelia_resolute
            with dissolve
            
            a "I have the determination, the intellectual courage to face this lofty challenge. The truths I uncover in the years ahead could forever alter how we understand ourselves."
            
            a "(No pressure, of course. I'm ready to embrace the weight of such responsibility. The fate of humanity's self-knowledge lies in the minds of thinkers like me.)"

        "Appreciate meaningful connections":
            $ SI += 2
            
            show amelia_grateful
            with dissolve
            
            a "(This year has been as much about the people as it has the experiences. I arrived at Plymouth feeling so alone, so adrift. Now I can't imagine my life without these incredible souls.)" 
            
            show amelia_remembering_friends
            with dissolve
            
            "She thinks of each of her friends in turn - Zara's warmth and loyalty, Lucas's steadfast support, Raj's infectious optimism and ability to buoy her spirits."
            
            if sarah_alive:
                show amelia_thankful
                with dissolve
                
                a "And my dear Sarah... our bond transcends anything I could have dared hope for. After everything she's been through, she remains my inspiration, my guiding light."
                
            else:
                show amelia_mourning
                with dissolve
                
                a "(My dearest Sarah... I only wish she could be here to share in what we've built together, this tribe of love and acceptance.)"
                
            show amelia_resolute
            with dissolve
            
            a "No matter where our respective paths lead, I'll carry the spirits of these beautiful humans with me always. Our connections are forged in the fires of our shared experiences."
            
            a "(Theirs are the faces, the essences, that will fuel me through whatever challenges await in the years to come. I am because we are.)"

    if sarah_alive:
        show sarah_approaching_amelia
        with dissolve
        
        sarah "There you are, Amelia. I was hoping I'd find you."
        
        show amelia_hugging_sarah  
        with dissolve
        
        a "Sarah! I can't believe the year is over. It feels like everything has changed, but you've been my constant."
        
        show sarah_smiling_at_amelia
        with dissolve
        
        sarah "We've been through so much together, you and I. The highest highs and the lowest lows. And we've come out the other side stronger for it."
        
        show amelia_looking_determined
        with dissolve

        a "And it's only the beginning. With you by my side, I know I can take on anything in the years ahead."
        sarah "Always, Amelia. I'll always be here, come what may. We've forged an unbreakable bond."

        show amelia_feeling_nostalgic
        with dissolve

        "Sarah takes Amelia's hand, and the two friends stay like that for a long moment, allowing the enormity of the year's journey to wash over them."
        a "Can you believe everything we've faced together? The darkness, the light, the sheer intensity of it all?"
        sarah "Honestly, there were times I didn't think we'd make it to this point. But something deep within me wouldn't let me give up."
        
        show sarah_looking_proud
        with dissolve
        
        sarah "You inspired that resilience in me, Amelia. Your strength, your refusal to abandon me even at my lowest... it gave me the courage to keep fighting."
        show amelia_tearing_up
        
        with dissolve
        a "Sarah... you'll never know how much your friendship means to me. How utterly lost I would be without your spirit lighting my way."
        
        show sarah_hugging_amelia
        with dissolve
        
        "The two embrace tightly, drawing strength from their unbreakable connection. For a timeless moment, the world around them falls away."
        show amelia_looking_outward
        with dissolve
        
        a "A entire universe of possibility awaits us, Sarah. And we'll take it on side-by-side, like we've taken on every challenge before it."
        sarah "Bring it on, Amelia. As long as we have each other, we can conquer anything this world throws at us."


    else:
        show amelia_looking_pensive
        with dissolve

        a "(Sarah... I wish you could see me now, could see how much I've grown because of you. Part of me will always carry your memory, your light.)"

        show amelia_determined_smile
        with dissolve

        a "(But I know you'd also want me to embrace the future, to keep moving forward with purpose. That's what I'll do, Sarah. For both of us.)" 

        show amelia_raising_fist
        with dissolve

        a "Your spirit lives on in me, Sarah. In every courageous choice, every blind leap of faith, every time I decide to face my fears instead of running."

        a "The path ahead won't be easy, but I'll walk it boldly, with your eternal light guiding my way. I owe you nothing less than the bravest, truest version of myself."

        show amelia_looking_upward
        with dissolve

        a "Wherever you are now, I hope you can feel my love and gratitude radiating across the universe. You'll never leave me, Sarah. We're intertwined forever."

        show amelia_taking_in_view
        with dissolve

        "Amelia takes a deep breath of the crisp spring air, letting it fill her lungs. She gazes out over the iconic university buildings, letting this pivotal moment etch itself into her mind and soul."
        
        show amelia_journaling
        with dissolve

        "She takes out a pen and the journal gifted by Dr. Simmons, inscribing her first entry with slow, purposeful strokes:"
        a "{i}The end of beginnings and the beginning of something new. The cycle continues ever onward, the journey transcending shallow perceptions of origin and destination.{/i}"
        a "{i}A year ago, I was a different person, encumbered by fears, doubts and a shattered self-perception. Now I emerge like a butterfly taking flight, my true nature revealed.{/i}"
        
        show amelia_closing_journal
        with dissolve

        "Amelia pauses, looking up with a beaming, contented smile. There will be time to chronicle the rest later. For now, she wants only to breathe in this moment, this profound metamorphosis."
        a "Life and death, joy and sorrow, love and loss. I've experienced it all, and I'm ready. Let the next transformation begin."
    
    return