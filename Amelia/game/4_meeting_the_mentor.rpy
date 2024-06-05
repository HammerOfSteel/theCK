label chapter_4_part_1:
    show amelia_campus_exterior
    with dissolve
    "As Amelia settles into her routine at Plymouth University, she can't shake the feeling that she's meant for something more."
    "She's been excelling in her classes and making friends, but there's a part of her that yearns for deeper guidance and purpose."

    if AA >= 5 and MC >= 5:
        jump meet_prof_hawthorne
    elif MH >= 5 and SI >= 5:
        jump meet_dr_simmons
    elif SD >= 5 and OK >= 5:
        jump meet_maya
    else:
        "Amelia continues to focus on her studies and social life, but can't shake the feeling that she's missing something important."
        jump chapter_4_part_2

label meet_prof_hawthorne:
    show amelia_hawthorne_office
    with dissolve
    "One day, after a particularly engaging lecture, Prof. Hawthorne asks Amelia to stay behind."

    h "Amelia, I must say, I've been very impressed with your work in class. Your insights show a depth of understanding that's rare in a first-year student."

    menu:
        "Express enthusiasm":
            $ AA += 1
            show amelia_hawthorne_excited_office
            a "Thank you, Professor. I've been finding the material fascinating. It's challenging, but in a way that motivates me to learn more."
        
        "Express hesitation":
            $ MC += 1
            show amelia_hawthorne_hesitant_office
            a "That's very generous, Professor, but I don't want to take on more than I can handle. What would this involve?"

    show amelia_hawthorne_discussing_project
    h "I'm working on a research project exploring the intersection of psychology and ethics. I think you'd be a valuable addition to the team."

    h "It would involve some extra reading and discussion outside of class, and potentially assisting with some data analysis. But I believe it would greatly enrich your understanding of the field."

    menu:
        "Accept the offer":
            $ AA += 1
            show amelia_hawthorne_accepting_project
            a "That sounds like an incredible opportunity. I'm in!"
            h "Excellent. I'll email you the details. We'll have our first meeting next week."
        
        "Ask for more time":
            $ MC += 1
            show amelia_hawthorne_considering_project
            a "Can I take a day to think it over? I want to make sure I can give it my full commitment."
            h "Of course. I appreciate your thoughtfulness. Let me know your decision by the end of the week."
    
    if AA >= 6 and MC >= 6:
        show amelia_hawthorne_inspired_office
        "As Amelia is about to leave, Prof. Hawthorne stops her."
        h "One more thing, Amelia. I sense in you a strong moral compass. Don't ever lose sight of that as you navigate this field. The world needs more psychologists who are guided by ethics."
        a "I'll remember that, Professor. Thank you."
        $MC += 1
    
    jump first_lesson_hawthorne

label meet_dr_simmons:
    show amelia_simmons_lecture_hall
    with dissolve
    "Amelia is attending a guest lecture on positive psychology when the speaker, Dr. Simmons, catches her eye."

    s "...and that's why focusing on strengths and cultivating positive emotions can be transformative for mental health."

    "Amelia is fascinated by the talk. Afterwards, she approaches Dr. Simmons."

    show amelia_simmons_talking_lecture_hall
    a "Dr. Simmons, thank you for the insightful lecture. I'm Amelia, a first-year psychology student."

    menu:
        "Discuss the personal resonance":
            $ MH += 1
            show amelia_simmons_discussing_mental_health
            a "I've been struggling with my own mental health lately, and the idea of focusing on positives really resonated with me."
        
        "Discuss the academic implications":
            $ SI += 1
            show amelia_simmons_discussing_research
            a "I was intrigued by the research you presented on social connections and well-being. It made me think about the importance of community in university life."

    s "That's a keen observation, Amelia. You know, I run a weekly discussion group where we explore these topics further. I think you'd be a great addition."

    menu:
        "Accept the invitation":
            $ SI += 1
            show amelia_simmons_accepting_invitation
            a "I'd love to join! When and where do you meet?"
        
        "Express hesitation":
            $ MH += 1
            show amelia_simmons_hesitant_invitation
            a "That sounds interesting, but I'm not sure if I'm ready to share in a group setting yet. Could I maybe talk with you one-on-one sometime?"
    
    show amelia_simmons_agreeing_to_meet
    s "I understand, Amelia. My door is always open. Why don't you come by my office hours next week, and we can chat more?"

    a "That would be great. Thank you, Dr. Simmons."

    if MH >= 6 and SI >= 6:
        show amelia_simmons_supportive_lecture_hall
        "As Amelia is leaving, Dr. Simmons calls after her."
        s "Amelia, remember, it's okay to not be okay. Seeking help is a sign of strength, not weakness. I'm here if you need support."
        a "Thank you, Dr. Simmons. That means a lot."
        $ MH += 1
    
    jump first_lesson_simmons

label meet_maya:
    show amelia_maya_university_garden
    with dissolve
    "Amelia is taking a break in the university garden when she notices a girl meditating under a tree."

    "Something about her peaceful presence draws Amelia in. As she approaches, the girl opens her eyes and smiles."

    m "Hello. I'm Maya. I don't think we've met before."

    menu:
        "Share personal experience":
            $ SD += 1
            show amelia_maya_discussing_meditation
            a "I'm Amelia. I'm sorry if I disturbed you. I was just curious about your meditation practice."
            a "A little. I've tried some mindfulness apps, but I struggle to make it a regular practice."
        
        "Express academic interest":
            $ OK += 1
            show amelia_maya_discussing_spirituality
            a "I'm Amelia. I'm sorry if I disturbed you. I was just curious about your meditation practice."
            a "Not personally, but I've been learning about the psychological benefits in my classes. I'd love to understand more about the spiritual side of it."
    
    show amelia_maya_listening_garden
    m "Meditation has been a transformative practice for me. It's helped me to find peace and clarity in the midst of the chaos of university life."

    m "I'm actually part of a group that meets weekly to explore various spiritual practices. You're welcome to join us sometime."

    menu:
        "Accept the invitation":
            $ SD += 1
            show amelia_maya_accepting_invitation
            a "That sounds fascinating. I'd love to learn more."
        
        "Express hesitation":
            $ OK += 1
            show amelia_maya_hesitant_invitation
            a "I'm not sure if I'm ready for a group experience yet. But maybe we could meet one-on-one sometime to talk more about your practice?"

    show amelia_maya_agreeing_to_meet
    m "Of course, Amelia. I'm here to support you in whatever way feels right. Why don't we plan to meet for tea next week? I can share some resources with you then."

    a "That sounds wonderful. Thank you, Maya."

    if SD >= 6 and OK >= 6:
        show amelia_maya_intuition_garden
        "As Amelia is about to leave, Maya touches her arm."
        m "Amelia, I sense a deep curiosity and openness in you. Trust that instinct. It will lead you to the answers you seek."
        a "I will. Thank you, Maya. I feel like this is the beginning of an important journey for me."
        $ SD += 1
    
    jump first_lesson_maya

label first_lesson_hawthorne:
    show amelia_hawthorne_library
    with dissolve
    "The following week, Amelia meets with Prof. Hawthorne in his office to discuss the research project."
    
    h "Amelia, I'm glad you decided to join the project. I think you'll find it both challenging and rewarding."

    h "To start, I'd like you to read this article on the ethical implications of psychological research. We'll discuss it in depth at our next meeting."

    menu:
        "Express gratitude":
            $ SI += 1
            show amelia_hawthorne_grateful_library
            a "Thank you, Professor. That means a lot coming from you. I'm grateful for the opportunity."
        
        "Express determination":
            $ AA += 1
            show amelia_hawthorne_determined_library
            a "I won't let you down, Professor. I'm committed to giving this project my all."

    show amelia_hawthorne_advice_library
    h "I have faith in you, Amelia. Remember, the goal is not perfection, but growth. Embrace the challenges and learn from them."

    a "I will, Professor. I'm ready to grow."

    if renpy.random.randint(1, 10) <= 3:
        show amelia_hawthorne_book_library
        "As Amelia is leaving, Prof. Hawthorne hands her a book."
        h "Amelia, I think you might find this book interesting. It's a philosophical exploration of the nature of the self. It's not directly related to our project, but I think it might resonate with some of your own questions."
        a "Thank you, Professor. I'm touched that you thought of me. I'll read it carefully."
        $ SD += 1
    
    jump amelia_reflection

label first_lesson_simmons:
    show amelia_simmons_office
    with dissolve
    "The next week, Amelia visits Dr. Simmons during her office hours."

    s "Amelia, I'm so glad you came. I've been thinking about our conversation after the lecture."

    s "I remember what it was like to be a first-year student, trying to find my place and purpose. It can be overwhelming at times."

    menu:
        "Share a personal struggle":
            $ MH += 1
            show amelia_simmons_sharing_struggles
            a "It really can be. I alternate between feeling excited and inspired, and feeling completely lost and inadequate."
            a "I've been struggling with my mental health lately. Some days, it's hard to find the motivation to keep going."
        
        "Ask for advice":
            $ SI += 1
            show amelia_simmons_asking_advice
            a "It really can be. I alternate between feeling excited and inspired, and feeling completely lost and inadequate."
            a "How do you recommend dealing with those feelings of inadequacy? How do you stay motivated when things get tough?"
    
    show amelia_simmons_receiving_support
    s "The most important thing is to be kind to yourself. Recognize that you're doing your best, and that's enough."

    s "It also helps to focus on your strengths and victories, no matter how small. Keep a journal of things you're proud of or grateful for each day."

    a "That's great advice. I'll try to incorporate that into my daily routine."

    s "Wonderful. And remember, my door is always open if you need to talk. You don't have to go through this alone."

    if renpy.random.randint(1, 10) <= 3:
        show amelia_simmons_workshop_flyer
        "As Amelia is about to leave, Dr. Simmons hands her a flyer."
        s "Amelia, I thought this might interest you. It's a mindfulness workshop happening next weekend. I think you might find it helpful for managing stress and anxiety."
        a "Thank you, Dr. Simmons. I appreciate you thinking of me. I'll definitely try to attend."
        $ MH += 1
    
    jump amelia_reflection

label first_lesson_maya:
    show amelia_maya_tea_shop
    with dissolve
    "The following week, Amelia meets Maya at a cozy tea shop near campus."

    m "Amelia, I'm so glad we could meet. I've been looking forward to continuing our conversation."

    menu:
        "Share a spiritual experience":
            $ SD += 1
            show amelia_maya_spiritual_experience
            a "Me too, Maya. I've been thinking a lot about what you said about meditation and finding peace."
            a "I've had some moments in my life where I've felt a deep sense of connection to something greater than myself. But I've never known how to cultivate that feeling."
        
        "Express curiosity":
            $ OK += 1
            show amelia_maya_curious_tea_shop
            a "Me too, Maya. I've been thinking a lot about what you said about meditation and finding peace."
            a "I'm curious about the different spiritual traditions and practices out there. How did you find your path?"

    show amelia_maya_tea_shop_advice
    m "For me, it was a process of exploration and listening to my intuition. I tried many different practices before finding the ones that resonated with me."

    m "The key is to approach it with an open mind and heart. Don't be afraid to try new things and see what speaks to you."

    a "That makes sense. I guess I need to trust my own journey and not compare myself to others."

    m "Exactly. And remember, I'm here to support you in any way I can. Whether it's lending an ear, recommending resources, or just sharing a cup of tea."

    if renpy.random.randint(1, 10) <= 3:
        show amelia_maya_mindfulness_journal
        "As they're leaving the tea shop, Maya hands Amelia a small journal."
        m "Amelia, I want you to have this. It's a mindfulness journal. I find it helpful for tracking my spiritual practices and reflections."
        a "Maya, thank you. This is so thoughtful. I'll definitely put it to good use."
        $ SD += 1
    
    jump amelia_reflection

label amelia_reflection:
    show amelia_dorm_night_thoughtful
    with dissolve
    "That night, as Amelia lies in bed, she reflects on her encounter with her new mentor."

    if prof_points >= dr_points and prof_points >= maya_points:
        a "(Prof. Hawthorne is brilliant. I can already tell I'm going to learn so much from him. But he's also intimidating...I hope I can live up to his expectations.)"
        a "(The research project is going to be challenging, but I'm excited to dive in. This is exactly the kind of deep, meaningful work I came to university for.)"
    
    elif dr_points >= prof_points and dr_points >= maya_points:
        a "(Dr. Simmons is so kind and understanding. I feel like I can really be myself around her, flaws and all.)"
        a "(Her advice about self-care and focusing on strengths...I think that's going to be a game-changer for me. I feel more motivated already.)"
    
    elif maya_points >= prof_points and maya_points >= dr_points:
        a "(There's something about Maya that just radiates peace and wisdom. I feel drawn to her in a way I can't quite explain.)"
        a "(Exploring spirituality and mindfulness...it's not something I ever thought I'd be into, but it feels right. Like a part of myself I've been neglecting.)"
    
    show amelia_dorm_night_determined
    a "(I can feel that this is the start of something big. I don't know exactly where this path will lead me, but I trust that it's where I'm meant to be.)"
    a "(I'm ready to learn, to grow, to become the best version of myself. And with [mentor]'s guidance, I know I can face whatever challenges come my way.)"
    a "(Bring it on, university. I'm ready for you.)"
    
    jump chapter_4_part_2

label chapter_4_part_2:
    show amelia_dorm_morning
    with dissolve
    "Amelia wakes up feeling energized and inspired after her first meeting with her mentor."
    a "(I can't wait to see what insights and experiences this mentorship will bring. I feel like I'm on the cusp of something transformative.)"

    if mentor == "Prof. Hawthorne":
        show amelia_studying_library
        "Amelia dives into the research materials Prof. Hawthorne provided, losing herself in the complex ethical debates."
    elif mentor == "Dr. Simmons":
        show amelia_jogging_park
        "Amelia starts her day with a mindful jog, putting Dr. Simmons' advice about self-care into practice."
    elif mentor == "Maya":
        show amelia_meditating_garden
        "Amelia finds a quiet spot in the university garden to meditate, following the techniques Maya taught her."

    show amelia_mentor_coffee_shop
    "Later that day, Amelia meets up with [mentor] at a cozy coffee shop to discuss her progress and upcoming plans."

    if mentor == "Prof. Hawthorne":
        h "Amelia, I'm impressed with your grasp of the ethical nuances in the research. You have a keen analytical mind."
    elif mentor == "Dr. Simmons":
        s "You're glowing, Amelia! I can see the positive effects of your self-care routine already."
    elif mentor == "Maya":
        m "The energy around you feels more balanced and harmonious, Amelia. The meditation is really benefiting you."

    menu:
        "Discuss challenges and doubts":
            $ MH += 1
            $ SI += 1
            show amelia_mentor_serious_talk
            a "To be honest, I've been grappling with some doubts and insecurities. I sometimes question if I'm really cut out for this path."
            "Amelia opens up about her fears and uncertainties, and [mentor] listens with empathy and understanding."
            if mentor == "Prof. Hawthorne":
                h "Doubt is a natural part of the intellectual journey, Amelia. It means you're engaging deeply with the material. Embrace the questions, and let them fuel your curiosity."
            elif mentor == "Dr. Simmons":
                s "Everyone faces self-doubt at times, Amelia. The key is to not let it overpower you. Remember your strengths, and lean on your support system. You're capable of more than you realize."
            elif mentor == "Maya":
                m "Uncertainty is a gateway to growth, Amelia. When we question ourselves, we open the door to new perspectives and possibilities. Trust the journey, even when the path is unclear."
        
        "Express excitement about learning":
            $ AA += 1
            $ SD += 1
            show amelia_mentor_excited_talk  
            a "I'm really enjoying diving into these new ideas and practices. It's challenging, but in a way that motivates me to learn more."
            if mentor == "Prof. Hawthorne":
                h "That's the mark of a true scholar, Amelia. Never lose that passion for learning. It will serve you well in your academic career and beyond."
            elif mentor == "Dr. Simmons":
                s "Your enthusiasm is contagious, Amelia! Keep nurturing that love of learning, and don't forget to apply those insights to your own life and well-being."
            elif mentor == "Maya":
                m "The pursuit of knowledge is a sacred journey, Amelia. Approach it with reverence and an open heart, and it will transform you in ways you never expected."

    show mentor_suggesting_trip
    "[mentor] leans forward, a sparkle in their eye."
    if mentor == "Prof. Hawthorne":
        h "Amelia, I have a proposition for you. There's a fascinating archaeological site in Cornwall that I think would greatly enrich your understanding of the historical context of psychology."
    elif mentor == "Dr. Simmons":
        s "Amelia, I have an idea. Cornwall is known for its stunning natural beauty and peaceful atmosphere. I think a trip there could do wonders for your mental well-being and personal growth."
    elif mentor == "Maya":
        m "Amelia, I feel called to share something with you. There are ancient sacred sites in Cornwall that hold deep wisdom and spiritual power. I think a pilgrimage there could be transformative for you."

    menu:
        "Embrace the opportunity":
            $ SD += 1
            show amelia_excited
            a "That sounds incredible, [mentor]! I would love to explore Cornwall and learn from the experience."
        
        "Express hesitation":
            $ AA += 1
            show amelia_hesitant
            a "I'm intrigued, but I'm not sure if I can take time away from my studies right now. Can I think about it and let you know?"

    "After some discussion, Amelia and [mentor] agree on a date for the Cornwall trip. Amelia leaves the meeting feeling excited and curious about what insights the journey will bring."

    if OK >= 8:
        show amelia_sensing_energy
        "As Amelia walks back to her dorm, she suddenly feels a strange tingling sensation, as if the air around her is vibrating with energy."
        a "(What is this feeling? It's like the whole world is alive and trying to tell me something.)"
        "She closes her eyes and takes a deep breath, trying to tune into the sensation."
        show amelia_vision_druid
        "In her mind's eye, she sees a vivid image: a cloaked figure standing in a misty forest, holding a staff adorned with intricate Celtic knots."
        "The figure speaks, their voice echoing in Amelia's mind:"
        druid "Seeker of wisdom, the ancient paths are calling. In the sacred groves of Cornwall, you will find the keys to unlock the mysteries within and without."
        "As quickly as it appeared, the vision fades, leaving Amelia breathless and puzzled."
        a "(Was that real? What does it mean? I guess I'll find out in Cornwall...)"
        $ OK += 2
    else:
        show amelia_walking_campus
        "Amelia makes her way back to her dorm, her mind buzzing with anticipation for the Cornwall trip and the new experiences it will bring."

    jump cornwall_trip

label cornwall_trip:
    show amelia_train_cornwall
    "The day of the Cornwall trip arrives, and Amelia finds herself on a train speeding through the lush English countryside."
    "[mentor] sits beside her, pointing out landmarks and sharing stories about the region's rich history and folklore."

    if mentor == "Prof. Hawthorne":
        show amelia_hawthorne_studying_map
        "They pore over maps and historical documents, discussing the archaeological significance of the sites they plan to visit."
    elif mentor == "Dr. Simmons":
        show amelia_simmons_admiring_view
        "They engage in a heartfelt conversation about the therapeutic benefits of nature and the importance of taking time for self-reflection."
    elif mentor == "Maya":
        show amelia_maya_meditating_train
        "They sit in comfortable silence, meditating and attuning themselves to the energy of the land they're approaching."

    if OK >= 8:
        show amelia_sensing_energy_train
        "As the train crosses into Cornwall, Amelia feels that strange tingling sensation again, even stronger than before."
        a "(It's like the land itself is welcoming me, calling me to explore its secrets.)"
        show mentor_noticing_amelia
        "[mentor] notices Amelia's shift in energy and smiles knowingly."
        if mentor == "Prof. Hawthorne":
            h "You feel it, don't you? The pull of the ancient mysteries. Cornwall is steeped in them."
        elif mentor == "Dr. Simmons":
            s "There's a special energy in Cornwall, isn't there? It's no wonder so many people find healing and inspiration here."
        elif mentor == "Maya":
            m "The veil between worlds is thin in Cornwall, Amelia. Open yourself to the wisdom of the land, and it will guide you."
        $ OK += 1

    show cornwall_station
    "The train pulls into the station, and Amelia and [mentor] gather their belongings and step out onto the platform."
    a "Wow, the air feels different here. It's so crisp and invigorating!"
    show mentor_smiling
    "Mentor" "Welcome to Cornwall, Amelia. Let the adventure begin!"
    a "I don't want to leave too late. But there's always time for a quick walk in nature!"
    "[mentor] smiles, knowing the true purpose of this trip is just beginning to unfold."

    jump rustic_village_visit

label rustic_village_visit:
    show village_street 
    with dissolve
    "Before heading to their main destination, Amelia and her mentor decide to visit a nearby village known for its traditional way of life."
    show amelia_village_street
    a "This place feels like it's from another time. It's so charming and peaceful."
    show mentor_points_at_cottage
    "[mentor] points to a quaint cottage with a colorful flower garden."
    "Mentor" "See that cottage there? It belongs to a local herbalist who's known for her knowledge of traditional plant lore."
    
    if OK >= 8:
        show villager_invites_amelia
        "Suddenly, an elderly woman emerges from the cottage and locks eyes with Amelia."
        show amelia_mentor_surprised
        "Woman" "You there, young lady. I can see you have a spark of the Old Ways in you. Come, let me show you something."
        "[mentor] raises an eyebrow, intrigued, and nods for Amelia to follow the woman."
        show cottage_interior
        "Inside the cottage, the woman shows Amelia her collection of dried herbs, talismans, and ancient texts."
        "Woman" "The wisdom of the druids runs deep in this land, child. The plants, the stones, the very earth itself holds secrets for those who know how to listen."
        show amelia_examines_herbs
        a "I've always felt a connection to nature, but I never knew it held such power and knowledge."
        "Woman" "The power is within you, too. Trust your instincts, and let the land guide you on your journey."
        $ OK += 2
    else:
        show amelia_admires_cottage
        a "It's beautiful. I can only imagine the knowledge and stories she must hold."
        "[mentor] nods."
        "Mentor" "The traditional wisdom passed down through generations is a treasure. It's important to honor and learn from it."

    menu:
        "Visit the village greengrocer":
            $ SD += 1
            show village_greengrocer 
            with dissolve
            a "I'd love to check out the local greengrocer. I bet they have some delicious, fresh produce."
            show amelia_buys_apples
            "Amelia browses the colorful displays of fruits and vegetables, marveling at their vibrancy."
            "Shopkeeper" "All grown right here in Cornwall, miss. You won't find any fresher!"
            a "I'll take some of these beautiful apples, please. There's nothing like the taste of local, seasonal food."
            "Amelia savors the crisp sweetness of the apple as they continue their stroll through the village."
        
        "Explore the village green":
            $ SI += 1
            show village_green 
            with dissolve
            a "Let's take a walk around the village green. It looks like a hub of community activity."
            show amelia_talks_to_villagers
            "Amelia and [mentor] wander around the green, observing the villagers going about their daily lives."
            "They strike up conversations with friendly locals, learning about the village's history and traditions."
            show amelia_mentor_listening
            "Villager" "...and every summer solstice, we gather on the green for a grand celebration. There's music, dancing, and a big bonfire. It's a time to come together as a community."
            a "That sounds wonderful. There's such a strong sense of connection and shared heritage here."
            $ SI += 1

    "After their village exploration, Amelia and [mentor] continue on to their main destination, the sacred site of [site_name]."

    jump sacred_site_visit

label sacred_site_visit:
    if mentor == "Prof. Hawthorne":
        show ancient_stones 
        with dissolve
        "Prof. Hawthorne takes Amelia to an ancient stone circle, believed to date back to the Neolithic era."
        show amelia_hawthorne_examining_stones
        h "Archaeologists believe this site was used for ceremonial purposes, possibly linked to astronomical events."
        a "I can feel the history and energy emanating from these stones. It's humbling to think about the ancient people who gathered here."
        show amelia_touches_stone_thoughtful
        "Amelia runs her hand over the weathered surface of one of the stones, closing her eyes and trying to imagine the rituals and celebrations that once took place here."
    elif mentor == "Dr. Simmons":
        show coastal_path 
        with dissolve
        "Dr. Simmons leads Amelia on a hike along the Cornish coastal path, taking in the breathtaking views of the sea cliffs and hidden coves."
        show amelia_simmons_hiking
        s "Spending time in nature is one of the most powerful ways to reconnect with ourselves and find inner peace."
        a "I can see why. The beauty and vastness of this landscape put everything into perspective."
        show amelia_meditating_overlook
        "They pause at a scenic overlook, and Dr. Simmons guides Amelia through a mindfulness meditation, encouraging her to tune into the sights, sounds, and sensations of the environment."
    elif mentor == "Maya":
        show ancient_well 
        with dissolve
        "Maya brings Amelia to an ancient holy well, nestled in a tranquil grove."
        show amelia_maya_at_well
        m "Wells like this were considered portals to the otherworld in Celtic tradition. They were places of healing, divination, and communication with the spirits."
        a "I can sense the sacredness of this place. It feels like a thin veil between worlds."
        show amelia_makes_offering
        "Maya teaches Amelia how to make an offering to the well spirits, thanking them for their wisdom and guidance."

    if OK >= 10:
        show amelia_vision_druid_staff
        "As Amelia immerses herself in the experience, she suddenly finds herself transported to a different realm."
        "She stands in a misty grove, face to face with the druid figure from her earlier vision."
        show druid_holding_staff
        "Druid" "You have heeded the call, seeker. Now, it is time for you to receive the wisdom of the ancients."
        "The druid hands Amelia a staff, intricately carved with Celtic symbols."
        show amelia_receives_staff_vision
        "Druid" "This staff is a conduit for the power of the land. It will guide and protect you on your journey of self-discovery."
        "Amelia takes the staff, feeling a surge of energy coursing through her body."
        show amelia_vision_fades
        "As suddenly as it began, the vision fades, and Amelia finds herself back at the sacred site, holding a small, polished stone in her hand."
        a "What just happened? Was that real?"
        "[mentor] looks at Amelia with a mix of awe and understanding."
        "Mentor" "You've been given a great gift, Amelia. The spirits of the land have chosen you for a special purpose."
        $ OK += 3
    else:
        show amelia_mentor_sacred_site
        "Amelia and [mentor] spend time at the sacred site, absorbing the energies and reflecting on the lessons of the day."
        "[mentor] shares more insights and stories, deepening Amelia's understanding and appreciation for the ancient wisdom of Cornwall."
        show amelia_inspired_sacred_site
        a "I feel so connected to something greater here. It's like I'm tapping into a deep well of knowledge and inspiration."
        "Mentor" "That's the power of these sacred places, Amelia. They have a way of awakening the wisdom within us."

    jump return_to_plymouth

label return_to_plymouth:
    show train_interior 
    with dissolve
    "As the train carries them back to Plymouth, Amelia's mind buzzes with all the experiences of the day"
    show train_interior 
    with dissolve
    "As the train carries them back to Plymouth, Amelia's mind buzzes with all the new insights and experiences from their Cornwall trip."
    a "I feel like I've learned so much, not just about Cornwall and its history, but about myself and my own path."
    show mentor_smiling_train
    "Mentor" "That's the beauty of these kinds of journeys, Amelia. They have a way of revealing truths we may not have seen before."
    a "I'm so grateful for this opportunity, [mentor]. It's given me a lot to think about and explore further."
    "Mentor" "And I'm grateful to be a part of your journey, Amelia. Watching you grow and discover your potential is a true privilege."

    show amelia_reflecting_train
    "Amelia gazes out the window, watching the countryside roll by and reflecting on the events of the trip."
    if OK >= 10:
        a "(The visions, the druid, the staff... what does it all mean? What is this special purpose the spirits have chosen me for?)"
        "She clutches the small stone from the sacred site, feeling its weight and warmth in her palm."
        a "(I may not have all the answers yet, but I know this is just the beginning of a profound journey. I must trust the path as it unfolds before me.)"
    else:
        a "(The ancient wisdom, the sacred sites, the connection to nature... it all feels so resonant and important.)"
        a "(I may not fully understand it all yet, but I know I want to keep exploring and learning. This trip has opened up a whole new world of possibilities.)"

    show plymouth_station_evening
    "As the train pulls into Plymouth station, Amelia feels a renewed sense of purpose and excitement for what lies ahead."

    jump chapter_4_part_3

label chapter_4_part_3:
    show amelia_dorm_evening
    with dissolve
    "Back in her dorm room, Amelia takes some time to unpack and process her experiences from the Cornwall trip."
    a "I feel like I've learned so much, but I also have so many new questions. It's both exciting and overwhelming."

    show amelia_studying_dorm
    "She dives into her studies with renewed vigor, seeking to integrate the wisdom and insights gained from her mentor and the sacred sites."

    if mentor == "Prof. Hawthorne":
        show amelia_research_paper
        "Amelia works diligently on the research project, exploring the ethical implications of psychological practices and the importance of culturally sensitive approaches."
    elif mentor == "Dr. Simmons":
        show amelia_mindfulness_journal
        "She starts a daily mindfulness practice, using the techniques Dr. Simmons taught her to manage stress and cultivate emotional resilience."
    elif mentor == "Maya":
        show amelia_reading_esoteric_texts
        "Amelia delves into the esoteric texts and practices Maya introduced her to, seeking to deepen her understanding of the mystical traditions."

    show amelia_receives_email
    "One evening, as Amelia is studying, she receives an email from [mentor]."
    "Mentor" "Amelia, I have an exciting opportunity for you. There's an upcoming conference on [conference_topic] that I think would be incredibly valuable for your growth and development."

    menu:
        "Accept the invitation":
            $ AA += 1
            $ SD += 1
            show amelia_excited_email
            a "Wow, this sounds amazing! I would love to attend the conference. Thank you so much for thinking of me."
            "Mentor" "Wonderful! I'll send you the registration details. I think you'll find it a truly enriching experience."
            jump conference_preparation
        
        "Decline the invitation":
            $ SI += 1
            show amelia_hesitant_email
            a "I'm honored that you thought of me, but I'm not sure if I can take on another commitment right now. I'm feeling a bit overwhelmed with my current workload."
            "Mentor" "I understand, Amelia. It's important to know your limits and prioritize your well-being. If you change your mind, just let me know."
            jump mentor_meeting

    label conference_preparation:
    show amelia_packing_suitcase
    "In the days leading up to the conference, Amelia immerses herself in preparation, reading up on the topics and speakers."
    "As she packs her suitcase, she can't help but feel a mix of excitement and nervousness."

    if OK >= 10:
        show amelia_holding_stone
        "She tucks the stone from the sacred site into her pocket, feeling its reassuring weight and warmth."
        a "(I don't know what challenges or revelations this conference will bring, but I feel like I'm meant to be there. The spirits are guiding me.)"
    else:
        show amelia_reflecting_suitcase
        a "(This conference is a big step for me. I'm pushing myself out of my comfort zone, but I know that's where growth happens.)"

    jump conference_event

    label mentor_meeting:
    show amelia_mentor_cafe
    "Instead of attending the conference, Amelia meets with [mentor] at their usual cafe to discuss her progress and challenges."
    "Mentor" "I'm proud of you for recognizing your limits, Amelia. Self-awareness is a crucial skill in both personal and professional development."
    a "Thank you, [mentor]. I'm learning to trust my instincts and advocate for my needs, even when it's difficult."

    menu:
        "Discuss academic concerns":
            $ AA += 1
            show amelia_mentor_serious_talk
            a "I've been struggling with one of my classes. The material is really challenging, and I'm worried about falling behind."
            "Mentor" "Let's break it down and come up with a plan. What specifically are you finding difficult?"
            "Amelia and [mentor] spend time strategizing study techniques and identifying resources for extra support."
        
        "Discuss personal growth":
            $ SD += 1
            show amelia_mentor_heart_to_heart
            a "I've been reflecting a lot on my personal values and goals. I feel like I'm starting to see the bigger picture of what I want to do with my life."
            "Mentor" "That's a profound realization, Amelia. Tell me more about your vision for your future."
            "Amelia shares her thoughts and dreams, and [mentor] offers guidance and encouragement."

    show amelia_mentor_toasting_tea
    "As they sip their tea, Amelia feels a deep sense of gratitude for [mentor]'s presence in her life."
    a "I don't know where I'd be without your guidance and support. Thank you for being my mentor and my friend."
    "Mentor" "It's an honor to walk alongside you on this journey, Amelia. I have no doubt that you will go on to do amazing things."

    jump unexpected_encounter

    label conference_event:
    show conference_hall
    with dissolve
    "Amelia arrives at the conference venue, buzzing with anticipation."
    "The halls are filled with scholars, researchers, and students from all over the world, all united by their passion for [conference_topic]."

    if mentor == "Prof. Hawthorne":
        show amelia_hawthorne_conference
        "Prof. Hawthorne is there to greet her, introducing her to colleagues and engaging her in thought-provoking discussions."
    elif mentor == "Dr. Simmons":
        show amelia_simmons_conference
        "Dr. Simmons is presenting a workshop on mindfulness in therapy, and invites Amelia to assist her, recognizing her growth and potential."
    elif mentor == "Maya":
        show amelia_maya_conference
        "Maya is there as well, participating in a panel on integrating spiritual practices into psychological frameworks."

    show amelia_conference_presentation
    "As Amelia attends the various sessions and presentations, she finds herself absorbing new knowledge and perspectives at a rapid pace."
    "She takes copious notes, asking insightful questions and engaging in lively debates with her peers."

    menu:
        "Present your own research":
            $ AA += 2
            show amelia_presenting_research
            "On the second day of the conference, Amelia takes a deep breath and steps up to the podium to present her own research."
            "She shares her findings on [research_topic], making a compelling case for the importance of ethical and culturally sensitive practices in psychology."
            show audience_impressed
            "The audience is impressed by her depth of knowledge and clear passion for the subject. After her presentation, several attendees approach her to discuss her work further."
            if mentor == "Prof. Hawthorne":
                show hawthorne_proud
                "Prof. Hawthorne beams with pride, congratulating Amelia on a job well done."
                h "You're a natural, Amelia. Your research has the potential to make a real impact in the field."
        
        "Attend a specialized workshop":
            $ SD += 2
            show amelia_workshop_participation
            "Amelia chooses to attend a specialized workshop on [workshop_topic], eager to deepen her understanding of this particular area."
            "The workshop leader guides the participants through a series of exercises and discussions, challenging them to think critically and creatively."
            show amelia_workshop_breakthrough
            "During one of the exercises, Amelia has a sudden breakthrough, a moment of clarity that shifts her perspective on a key issue."
            a "(Wow, I never thought about it that way before. This changes everything!)"
            "She shares her insight with the group, sparking a lively and productive dialogue."

    jump unexpected_encounter

    label unexpected_encounter:
    if OK >= 12:
        show amelia_alone_conference
        "On the final evening of the conference (or after her meeting with [mentor]), Amelia finds herself wandering alone, lost in thought."
        show shadowy_figure_appears
        "Suddenly, a shadowy figure appears before her, emanating an aura of power and mystery."
        show elena_reveals_herself
        "As the figure steps into the light, Amelia gasps. It's Elena, the mysterious woman Maya had spoken of."
        show elena_speaks_to_amelia
        e "Amelia, I've been watching your journey. You have the potential for great wisdom and power within you."
        a "Elena? What are you doing here? What do you mean, watching my journey?"
        e "Your path is intertwined with the ancient ways, Amelia. The spirits have chosen you for a higher purpose."
        show amelia_surprised_elena
        a "I... I don't understand. What purpose? What do the spirits want from me?"
        e "To reclaim the lost wisdom, to bridge the worlds, to heal the rift between the mundane and the sacred."
        e "But you must be willing to delve deep, to face the shadows and the mysteries. It will not be an easy path."
        menu:
            "Accept Elena's guidance":
                $ OK += 3
                show amelia_determined_elena
                a "I feel the truth of your words, Elena. I don't fully understand it yet, but I know this is the path I'm meant to walk."
                a "I'm ready to learn, to face whatever challenges come my way. Will you teach me?"
                show elena_smiles_amelia
                e "Yes, Amelia. I will guide you. But the true wisdom must come from within. Trust your instincts, and the way will reveal itself."
                e "We will meet again soon. Until then, keep seeking, keep questioning. The answers are closer than you think."
            
            "Refuse Elena's guidance":
                $ OK -= 1
                show amelia_refuses_elena
                a "I'm sorry, Elena. While I'm intrigued by what you're saying, I don't think I'm ready for this."
                a "I have so much still to learn and understand in the mundane world. I can't take on this mystical path right now."
                show elena_disappointed_amelia
                e "I understand, Amelia. The choice must be yours. But know that the call will not cease."
                e "When you are ready, the way will be open to you. Until then, continue your studies, but do not forget the deeper truths."
        show elena_disappears
        "With that, Elena vanishes as suddenly as she appeared, leaving Amelia alone with her thoughts."

    scene amelia_dorm_night
    with dissolve
    show amelia_reflecting_night
    "Back in her dorm room, Amelia tries to make sense of all that has happened."

    if OK >= 12:
        a "(The conference, the revelations, Elena's appearance... it's all so much to process.)"
        a "(But I feel like I'm on the cusp of something profound. The veil is thinning, and I'm being called to a higher purpose.)"
        show amelia_holding_stone_night
        "She takes out the stone from the sacred site, feeling its energy pulsing in her hand."
        a "(I don't know where this path will lead me, but I know I must walk it. The spirits are guiding me, and I must trust in their wisdom.)"
    else:
        a "(The conference (or the meeting with [mentor]) was intense, but so enlightening. I feel like I've grown so much in such a short time.)"
        a "(But I know this is just the beginning. There's so much more to learn, so many more ways to grow.)"
        show amelia_determined_night
        a "(Whatever challenges come my way, I feel more prepared than ever to face them. I have the knowledge, the skills, and the support network to see me through.)"
        a "(And most importantly, I have a clearer sense of my own strength and potential. I'm ready for whatever the future holds.)"

    "With a mix of excitement and uncertainty, but a strong sense of purpose, Amelia turns off her light and drifts off to sleep."
    "Her dreams are filled with ancient symbols, whispered prophecies, and the promise of a journey yet to unfold."

    jump chapter_5