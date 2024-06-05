label chapter_7_part_1:
    show amelia_dorm_morning with dissolve
    "Amelia wakes up in her dorm room, feeling the weight of the decisions and challenges ahead. Today, she plans to focus on her academic pursuits, but she also wants to be there for her friends and explore her growing interest in the occult."

    menu:
        "Focus on academics":
            jump focus_on_academics

        "Support friends in crisis":
            jump support_friends

        "Engage in occult research":
            jump engage_occult_research

label focus_on_academics:
    show amelia_library_morning with dissolve
    "Amelia decides to start her day in the library, determined to make progress on her thesis."

    show amelia_studying_hard with dissolve
    "She finds a quiet corner and immerses herself in her research, the silence of the library providing a perfect backdrop for her concentration."

    menu:
        "Work on thesis":
            jump work_on_thesis

        "Attend a special lecture":
            jump attend_lecture

        "Study with Sophia":
            jump study_with_sophia

label work_on_thesis:
    show amelia_library_studying_hard with dissolve
    "Amelia surrounds herself with books and notes, delving deep into her thesis on cognitive dissonance."

    show sophia_approaches with dissolve
    sophia "Hey Amelia, mind if I join you? I need to work on my own project, and I thought we could keep each other motivated."

    menu:
        "Welcome Sophia's company":
            jump welcome_sophia

        "Prefer to work alone":
            jump prefer_alone

label welcome_sophia:
    show amelia_smiling_sophia with dissolve
    a "Of course, Sophia. I'd love the company. Maybe we can bounce ideas off each other."

    show sophia_sitting with dissolve
    sophia "Great! I've been struggling with this section on cognitive biases. How's your thesis coming along?"

    menu:
        "Discuss challenges":
            jump discuss_challenges

        "Share progress":
            jump share_progress

label discuss_challenges:
    show amelia_thinking with dissolve
    a "I'm hitting a bit of a roadblock with my methodology. It's tough to design experiments that are both ethical and effective."

    show sophia_nodding with dissolve
    sophia "I hear you. I've had similar issues. Maybe we can brainstorm some solutions together?"

    show amelia_and_sophia_discussing with dissolve
    "Amelia and Sophia dive into a deep discussion, exchanging ideas and offering constructive feedback."

    a "What if we incorporate a mixed-methods approach? It could balance the quantitative and qualitative aspects."

    sophia "That's a great idea! And we could use case studies to illustrate the ethical considerations."

    show amelia_and_sophia_smiling with dissolve
    "Their collaborative effort breathes new life into their projects, strengthening their academic bond."

    $ AA += 2
    $ SI += 1
    jump academic_success

label share_progress:
    show amelia_happy with dissolve
    a "I've made some headway on my literature review. It's fascinating how much past research has shaped our current understanding."

    show sophia_smiling with dissolve
    sophia "That's fantastic! I'd love to hear more about your findings."

    show amelia_sharing_notes with dissolve
    "Amelia shares her notes with Sophia, who listens intently and asks insightful questions."

    sophia "Your approach is really thorough, Amelia. It's inspiring to see how dedicated you are."

    a "Thanks, Sophia. It's a lot of work, but I'm passionate about it."

    show amelia_and_sophia_studying with dissolve
    "Their discussion reinforces their mutual respect and academic camaraderie."

    $ AA += 1
    $ SI += 1
    jump academic_success

label prefer_alone:
    show amelia_thoughtful with dissolve
    a "I appreciate the offer, Sophia, but I think I need to focus on this alone today. Maybe we can work together another time?"

    show sophia_understanding with dissolve
    sophia "Of course, I get it. Good luck with your work, Amelia."

    "Amelia returns to her research, feeling a bit more isolated but also deeply focused."

    $ AA += 1
    jump academic_success

label academic_success:
    show amelia_library_late with dissolve
    "Hours pass as Amelia diligently works on her thesis. By the time she leaves the library, she feels a sense of accomplishment."

    show amelia_relieved with dissolve
    a "(Today was productive. I'm getting closer to completing my thesis.)"

    jump chapter_7_part_2

label attend_lecture:
    show amelia_lecture_hall with dissolve
    "Amelia attends a special lecture by a renowned psychologist. The topic is advanced cognitive theories."

    show professor_lecturing with dissolve
    professor "Today's lecture will delve into the intricacies of cognitive dissonance and its implications for behavioral psychology."

    show amelia_taking_notes with dissolve
    "Amelia listens intently, taking detailed notes and absorbing the complex material."

    menu:
        "Ask a question during the lecture":
            jump ask_question

        "Discuss the lecture with classmates afterwards":
            jump discuss_lecture

label ask_question:
    show amelia_raising_hand with dissolve
    a "Professor, could you elaborate on how cognitive dissonance theory can be applied to therapeutic practices?"

    show professor_answering with dissolve
    professor "Excellent question, Amelia. Cognitive dissonance can be a powerful tool in therapy to help clients recognize and resolve conflicting beliefs and behaviors."

    show amelia_listening with dissolve
    professor "For example, a therapist might use dissonance to challenge a client's harmful beliefs, prompting them to adopt healthier, more consistent attitudes."

    a "Thank you, Professor. That provides a lot of clarity."

    "Amelia feels a sense of pride and satisfaction from engaging with the material on a deeper level."

    $ AA += 1
    jump academic_success

label discuss_lecture:
    show amelia_talking_classmates with dissolve
    "After the lecture, Amelia and her classmates gather to discuss the concepts presented."

    show classmate_1 with dissolve
    classmate_1 "That lecture was mind-blowing. Cognitive dissonance really explains a lot about human behavior."

    show classmate_2 with dissolve
    classmate_2 "Agreed. I especially liked how the professor linked it to therapeutic practices."

    show amelia_sharing_ideas with dissolve
    a "It got me thinking about how we can use these theories in our own research and practice. There's so much potential here."

    show classmates_listening with dissolve
    "Amelia's enthusiasm sparks a lively discussion, deepening their understanding of the topic and fostering a sense of academic community."

    $ AA += 1
    $ SI += 1
    jump academic_success

label study_with_sophia:
    show amelia_and_sophia_studying with dissolve
    "Amelia decides to study with Sophia, hoping to gain new perspectives and insights."

    show sophia_smiling with dissolve
    sophia "I'm glad we're studying together, Amelia. We can really push each other to excel."

    menu:
        "Focus on challenging topics":
            jump focus_challenging_topics

        "Review and discuss past lectures":
            jump review_lectures

label focus_challenging_topics:
    show amelia_and_sophia_deep_discussion with dissolve
    "Amelia and Sophia tackle the most challenging topics, debating theories and sharing insights."

    a "I've been struggling with this concept of cognitive load theory. What do you think about it?"

    show sophia_thinking with dissolve
    sophia "It's complex, but I think it has significant implications for educational psychology. Managing cognitive load can improve learning outcomes."

    a "That's a great point. And it ties into our work on memory and retention."

    show amelia_and_sophia_smiling with dissolve
    "Their intense discussion helps them both gain a deeper understanding of the material, reinforcing their academic bond."

    $ AA += 1
    $ SI += 1
    jump academic_success

label review_lectures:
    show amelia_and_sophia_reviewing_notes with dissolve
    "Amelia and Sophia review their notes from past lectures, discussing key points and clarifying any doubts."

    a "Do you remember what the professor said about the ethical implications of cognitive bias?"

    show sophia_nodding with dissolve
    sophia "Yes, it's crucial for us to consider how biases can affect our research and practice. We need to remain objective and critical."

    a "Absolutely. It's a constant challenge, but it's essential for our work."

    show amelia_and_sophia_studying with dissolve
    "Their review session strengthens their grasp of the material and their respect for each other's academic abilities."

    $ AA += 1
    $ SI += 1
    jump academic_success

label support_friends:
    show amelia_cafe_with_friends with dissolve
    "Amelia meets Lucas, Zara, and Raj at a campus cafe, ready to support them through their own challenges."

    show lucas_smiling with dissolve
    lucas "Hey Amelia, glad you could join us. We've got a lot to talk about."

    menu:
        "Discuss Lucas's personal challenges":
            jump discuss_lucas

        "Support Zara's academic struggles":
            jump support_zara

        "Help Raj with social issues":
            jump help_raj

label discuss_lucas:
    show lucas_talking with dissolve
    "Lucas opens up about the personal challenges he's been facing."

    lucas "I've been feeling overwhelmed lately. Balancing school, work, and personal life is tough."

    show amelia_listening_lucas with dissolve
    a "I'm here for you, Lucas. What's been the most challenging part?"

    lucas "Honestly, it's the pressure to succeed. I feel like I'm constantly failing to meet expectations."

    menu:
        "Offer emotional support":
            jump offer_emotional_support

        "Suggest practical solutions":
            jump suggest_practical_solutions

label offer_emotional_support:
    show amelia_comforting_lucas with dissolve
    a "Lucas, you're doing your best, and that's enough. It's okay to struggle. You're not alone."

    show lucas_relieved with dissolve
    lucas "Thanks, Amelia. That means a lot. Sometimes I just need to hear that."

    a "We're all in this together. Don't hesitate to reach out when you need support."

    "Amelia's compassion strengthens their friendship, providing Lucas with much-needed reassurance."

    $ SI += 1
    $ MH += 1
    jump friends_support_success

label suggest_practical_solutions:
    show amelia_thinking with dissolve
    a "Maybe we can come up with a plan to manage your time better. Have you tried breaking tasks into smaller, more manageable steps?"

    show lucas_nodding with dissolve
    lucas "I've thought about it, but I haven't been consistent. Maybe having a study schedule could help."

    show amelia_smiling_lucas with dissolve
    a "Let's work on one together. Sometimes having a friend to keep you accountable makes a big difference."

    "Amelia and Lucas create a study schedule, breaking down tasks into manageable steps and setting realistic goals."

    show lucas_grateful with dissolve
    lucas "This is really helpful, Amelia. I feel a lot more organized already."

    a "I'm glad. Remember, we're all here to support each other."

    "Their collaborative effort not only helps Lucas manage his time better but also strengthens their bond."

    $ SI += 1
    $ AA += 1
    jump friends_support_success

label friends_support_success:
    show amelia_cafe_with_friends_late with dissolve
    "After supporting Lucas, Amelia turns her attention to Zara and Raj, listening to their challenges and offering advice."

    show zara_talking with dissolve
    zara "I've been struggling with my coursework. It feels like no matter how much I study, I can't keep up."

    show raj_agreeing with dissolve
    raj "Same here. And on top of that, dealing with social dynamics is draining."

    menu:
        "Offer study sessions together":
            jump offer_study_sessions

        "Provide emotional support":
            jump provide_emotional_support

label offer_study_sessions:
    show amelia_smiling_friends with dissolve
    a "Why don't we form a study group? We can meet regularly, help each other out, and keep each other motivated."

    show zara_smiling with dissolve
    zara "That's a great idea, Amelia. I think it would really help."

    show raj_nodding with dissolve
    raj "Count me in. Studying together sounds way better than struggling alone."

    show amelia_group_studying with dissolve
    "Amelia, Zara, and Raj form a study group, meeting regularly to tackle their coursework together. Their collaboration not only improves their academic performance but also strengthens their friendship."

    $ SI += 2
    $ AA += 1
    jump friends_support_success

label provide_emotional_support:
    show amelia_comforting_friends with dissolve
    a "I know things are tough right now, but you're both doing your best. It's okay to ask for help and take breaks when you need to."

    show zara_relieved with dissolve
    zara "Thanks, Amelia. Your support means a lot."

    show raj_grateful with dissolve
    raj "Yeah, it's good to know we're not alone in this."

    "Amelia's emotional support helps Zara and Raj feel more confident and less isolated, reinforcing their bond."

    $ SI += 1
    $ MH += 1
    jump friends_support_success

label engage_occult_research:
    show amelia_dorm_morning with dissolve
    "Amelia feels a pull towards the esoteric and decides to spend her day delving into occult research."

    show amelia_meditating with dissolve
    "She starts her morning with a meditation session, focusing her mind and preparing herself for the deep exploration ahead."

    menu:
        "Seek out ancient artifacts":
            jump seek_ancient_artifacts

        "Interpret prophetic dreams":
            jump interpret_dreams

        "Share knowledge selectively":
            jump share_knowledge_selectively

label seek_ancient_artifacts:
    show amelia_outdoor_exploration with dissolve
    "Amelia decides to seek out ancient artifacts. She heads to the campus museum, known for its collection of historical relics."

    show amelia_exploring_museum with dissolve
    "As she explores the museum, she feels a strange energy drawing her towards a specific exhibit."

    show amelia_staring_artifact with dissolve
    "An ancient amulet catches her eye. The intricate designs seem to pulsate with a hidden power."

    menu:
        "Investigate the amulet":
            jump investigate_amulet

        "Seek guidance from Maya":
            jump seek_guidance_maya

label investigate_amulet:
    show amelia_studying_amulet with dissolve
    "Amelia examines the amulet closely, feeling a connection to its history and power."

    show museum_curator_approaches with dissolve
    curator "I see you've found one of our most intriguing artifacts. This amulet is said to hold ancient protective magic."

    show amelia_listening_curator with dissolve
    a "It's fascinating. Do you know where it came from?"

    show curator_explaining with dissolve
    curator "It was discovered in an ancient burial site. Legend has it that it was used by a powerful druid to ward off evil spirits."

    menu:
        "Ask to study the amulet further":
            jump study_amulet_further

        "Thank the curator and leave":
            jump thank_curator

label study_amulet_further:
    show amelia_studying_amulet_closer with dissolve
    a "Would it be possible to study the amulet further? I'm very interested in its history and properties."

    show curator_agreeing with dissolve
    curator "Of course. I'll arrange for you to have access to our research materials on it."

    "Amelia spends the rest of the day studying the amulet, uncovering its secrets and feeling a deeper connection to the ancient magic."

    $ OK += 2
    $ SD += 1
    jump occult_success

label thank_curator:
    show amelia_smiling_curator with dissolve
    a "Thank you for the information. It's truly fascinating."

    show curator_smiling with dissolve
    curator "You're welcome. Feel free to visit anytime you have more questions."

    "Amelia leaves the museum, her mind buzzing with the potential of the ancient artifact."

    $ OK += 1
    jump occult_success

label seek_guidance_maya:
    show amelia_meeting_maya with dissolve
    "Amelia decides to seek guidance from Maya, hoping to understand more about the amulet's power."

    show maya_listening_amelia with dissolve
    a "Maya, I found this ancient amulet at the museum. It feels like it has a deep, hidden power. Can you help me understand it?"

    show maya_thinking with dissolve
    maya "Of course, Amelia. Let's meditate on it and see what insights we can gain."

    show amelia_maya_meditating with dissolve
    "They meditate together, focusing on the amulet and its energy."

    show maya_sharing_insights with dissolve
    maya "This amulet is indeed powerful. It holds protective magic, but it also requires a pure heart and strong will to wield it effectively."

    show amelia_listening_maya with dissolve
    a "Thank you, Maya. I'll continue to study it and make sure I use its power wisely."

    $ OK += 2
    $ SI += 1
    jump occult_success

label interpret_dreams:
    show amelia_dorm_night with dissolve
    "Amelia decides to focus on interpreting her prophetic dreams, seeking guidance from the hidden messages they hold."

    show amelia_sleeping with dissolve
    "That night, she has a vivid dream. She finds herself in an ancient forest, surrounded by towering trees and mystical creatures."

    show amelia_dream_forest with dissolve
    "A wise old druid appears before her, holding a glowing staff."

    druid "Amelia, seeker of truth, you have been chosen to uncover the hidden wisdom of the ancients. Follow the signs and trust your instincts."

    show amelia_listening_druid with dissolve
    a "What signs should I look for, and how will I know I'm on the right path?"

    show druid_explaining with dissolve
    druid "The path will reveal itself through symbols and synchronicities. Pay attention to your surroundings and the guidance you receive in your dreams."

    "Amelia wakes up, feeling a sense of clarity and purpose."

    menu:
        "Write down the dream and symbols":
            jump write_down_dream

        "Share the dream with Maya":
            jump share_dream_maya

label write_down_dream:
    show amelia_writing_journal with dissolve
    "Amelia writes down her dream in detail, noting the symbols and messages she received."

    show amelia_thinking with dissolve
    a "These symbols might guide me to uncovering deeper truths. I need to stay vigilant and trust my instincts."

    $ OK += 1
    $ SD += 1
    jump occult_success

label share_dream_maya:
    show amelia_meeting_maya with dissolve
    "Amelia shares her dream with Maya, hoping for further insights."

    show maya_listening_dream with dissolve
    a "Maya, I had a prophetic dream last night. It felt so real and powerful. A druid spoke to me about uncovering hidden wisdom."

    show maya_thinking_dream with dissolve
    maya "Dreams like this are rare and significant, Amelia. The druid is a guide, showing you the path you need to follow. Trust in the symbols and your intuition."

    show amelia_grateful with dissolve
    a "Thank you, Maya. Your guidance always helps me find clarity."

    $ OK += 2
    $ SI += 1
    jump occult_success

label share_knowledge_selectively:
    show amelia_library_afternoon with dissolve
    "Amelia decides to share her knowledge selectively, carefully choosing who to trust with the occult secrets she uncovers."

    show amelia_studying_occult with dissolve
    "She spends the afternoon in the library, studying esoteric texts and making connections between ancient wisdom and modern understanding."

    menu:
        "Share knowledge with a trusted friend":
            jump share_knowledge_friend

        "Keep knowledge to herself for now":
            jump keep_knowledge_self

label share_knowledge_friend:
    show amelia_meeting_friend with dissolve
    "Amelia decides to share her knowledge with a trusted friend, Lucas."

    show lucas_listening_amelia with dissolve
    a "Lucas, I've been studying some ancient texts and uncovering fascinating occult knowledge. I trust you to understand and respect it."

    show lucas_curious with dissolve
    lucas "Wow, Amelia. That sounds incredible. I'm honored that you trust me with this. Tell me more."

    show amelia_sharing_knowledge with dissolve
    "Amelia shares her findings with Lucas, who listens with genuine interest and respect."

    show lucas_fascinated with dissolve
    lucas "This is amazing, Amelia. It's like you're uncovering a hidden world. How can I help?"

    a "Just being here and supporting me is enough. We can explore this knowledge together."

    $ OK += 2
    $ SI += 1
    jump occult_success

label keep_knowledge_self:
    show amelia_thinking_library with dissolve
    "Amelia decides to keep her knowledge to herself for now, feeling that the time isn't right to share it."

    show amelia_studying_occult_alone with dissolve
    "She continues her studies alone, feeling a sense of responsibility and purpose in safeguarding the ancient wisdom."

    $ OK += 1
    $ SD += 1
    jump occult_success

label occult_success:
    show amelia_dorm_evening with dissolve
    "As the day ends, Amelia reflects on her discoveries and experiences. She feels a deep sense of connection to the ancient wisdom and a growing confidence in her path."

    a "(Today was enlightening. I've gained new insights and strengthened my resolve to uncover and protect the hidden knowledge.)"

    jump chapter_7_part_2

label chapter_7_part_2:
    scene amelia_dorm_morning with dissolve
    "Amelia wakes up with a sense of anticipation. Today, she plans to explore more of Cornwall and deepen her connections with friends and mentors."
    a "(There's so much to learn and experience. I need to make the most of this day.)"

    menu:
        "Continue exploring Cornwall with friends":
            jump explore_cornwall_with_friends

        "Meet with your mentor for guidance":
            jump meet_mentor_for_guidance

        "Dive into solo research on the occult":
            jump solo_occult_research

label explore_cornwall_with_friends:
    scene cornwall_coastline with dissolve
    "Amelia decides to spend the day exploring Cornwall with Lucas, Zara, and Raj. They start at the picturesque coastline, the waves crashing against the rugged cliffs."
    show amelia_talking_friends with dissolve
    a "Isn't this place amazing? The energy here is so vibrant."

    show lucas_agreeing with dissolve
    lucas "Absolutely. It's like the ocean is alive with possibilities."

    show zara_smiling with dissolve
    zara "I love how peaceful it feels here. It's a nice break from the hectic university life."

    show raj_nodding with dissolve
    raj "And it's a perfect spot for some deep conversations. What do you all think is the most important thing we've learned so far this year?"

    menu:
        "Share personal growth insights":
            jump share_personal_growth

        "Discuss academic achievements":
            jump discuss_academic_achievements

        "Talk about future plans":
            jump talk_future_plans

label share_personal_growth:
    show amelia_reflective with dissolve
    a "For me, it's been all about personal growth. I've learned so much about myself and what's truly important in life."

    show lucas_listening with dissolve
    lucas "Like what?"

    show amelia_thinking with dissolve
    a "Like the importance of self-care, the value of true friendship, and the need to follow my passions even when it's challenging."

    show zara_nodding with dissolve
    zara "I feel the same way. This year has been a journey of self-discovery for all of us."

    show raj_smiling with dissolve
    raj "It's amazing how much we've all grown. I'm grateful to have friends like you to share this journey with."

    $ MH += 1
    $ SI += 1
    jump continue_cornwall_exploration

label discuss_academic_achievements:
    show amelia_proud with dissolve
    a "Academically, I've pushed myself harder than ever. The research projects, the late-night study sessions... it's been intense but rewarding."

    show lucas_proud with dissolve
    lucas "You've done amazing, Amelia. Your dedication is inspiring."

    show zara_agreeing with dissolve
    zara "And it's not just about grades. We've learned to think critically and apply our knowledge in meaningful ways."

    show raj_smiling with dissolve
    raj "Absolutely. And the best part is that we've supported each other through it all."

    $ AA += 1
    $ SI += 1
    jump continue_cornwall_exploration

label talk_future_plans:
    show amelia_thoughtful with dissolve
    a "I'm starting to think about the future. What comes after university, what kind of impact I want to make."

    show lucas_interested with dissolve
    lucas "Do you have any specific plans in mind?"

    show amelia_dreaming with dissolve
    a "I'd love to continue my studies, maybe even pursue a career in research or teaching. And of course, I want to keep exploring the occult path."

    show zara_nodding with dissolve
    zara "That sounds amazing. I can see you making a real difference in whatever you choose to do."

    show raj_smiling with dissolve
    raj "And we'll be there to support you every step of the way."

    $ SD += 1
    $ SI += 1
    jump continue_cornwall_exploration

label continue_cornwall_exploration:
    show cornwall_moorlands with dissolve
    "After the coastline, the group heads to the Cornwall moorlands, a place steeped in ancient history and mystery."

    show amelia_marveling with dissolve
    a "The moorlands are incredible. You can almost feel the history in the air."

    show lucas_nodding with dissolve
    lucas "It's like stepping back in time. I wonder what stories these lands hold."

    show zara_agreeing with dissolve
    zara "We should come back here for a hike sometime. There's so much to explore."

    show raj_smiling with dissolve
    raj "Definitely. And who knows, maybe we'll uncover some ancient secrets."

    menu:
        "Investigate an ancient stone circle":
            jump investigate_stone_circle

        "Visit a local historical site":
            jump visit_historical_site

        "Explore the natural beauty":
            jump explore_natural_beauty

label investigate_stone_circle:
    show cornwall_stone_circle with dissolve
    "The group stumbles upon an ancient stone circle, the stones weathered by time but still standing proudly."

    show amelia_entranced with dissolve
    a "Look at this! It's an ancient stone circle. These places are said to have powerful energies."

    show lucas_curious with dissolve
    lucas "What kind of energies?"

    show amelia_explaining with dissolve
    a "Some believe they were used for rituals, possibly to connect with the spiritual realm or mark astronomical events."

    show zara_thoughtful with dissolve
    zara "It's amazing to think about. Standing here, I feel a sense of connection to the past."

    show raj_agreeing with dissolve
    raj "And maybe a glimpse of the future too. It's like these stones have seen it all."

    menu:
        "Perform a small ritual":
            jump perform_small_ritual

        "Meditate in the circle":
            jump meditate_in_circle

label perform_small_ritual:
    show amelia_performing_ritual with dissolve
    a "Let's perform a small ritual. It doesn't have to be complicated, just something to honor the ancient energies here."

    show lucas_participating with dissolve
    lucas "I'm in. What do we need to do?"

    show amelia_explaining with dissolve
    a "We can each offer a small token of gratitude to the circle. Something meaningful to us."

    "The friends gather small items – a coin, a flower, a piece of jewelry – and place them in the center of the circle, silently expressing their gratitude and intentions."

    show amelia_reflecting_ritual with dissolve
    a "This feels right. Like we're connecting with something greater than ourselves."

    show lucas_smiling with dissolve
    lucas "It's a powerful experience. Thank you for suggesting it, Amelia."

    show zara_nodding with dissolve
    zara "Yes, thank you. This is a moment I'll never forget."

    show raj_agreeing with dissolve
    raj "Same here. It feels like we've made a meaningful connection."

    $ OK += 2
    $ SI += 1
    jump end_of_day

label meditate_in_circle:
    show amelia_meditating_circle with dissolve
    a "Let's meditate here, in the circle. Close your eyes and feel the energy of this place."

    show friends_meditating with dissolve
    "The friends sit in the stone circle, closing their eyes and breathing deeply, tuning into the ancient energies around them."

    show amelia_meditative_state with dissolve
    a "Focus on your breath. Feel the ground beneath you, the history around you. Let the energy of this place flow through you."

    "They meditate in silence, each finding a sense of peace and connection."

    show amelia_opening_eyes with dissolve
    a "That was incredible. I feel so calm and centered."

    show lucas_agreeing with dissolve
    lucas "Me too. This place has a special kind of magic."

    show zara_smiling with dissolve
    zara "Thank you for guiding us, Amelia. This has been a beautiful experience."

    show raj_nodding with dissolve
    raj "Absolutely. We should do this more often."

    $ OK += 1
    $ MH += 1
    $ SI += 1
    jump end_of_day

label visit_historical_site:
    show cornwall_historical_site with dissolve
    "Next, the group visits a local historical site, a preserved manor house with centuries of history."

    show amelia_entranced with dissolve
    a "This place is incredible. It's like stepping into a different era."

    show lucas_agreeing with dissolve
    lucas "The architecture, the artifacts... there's so much to learn here."

    show zara_thoughtful with dissolve
    zara "Imagine living in a place like this, surrounded by all this history."

    show raj_smiling with dissolve
    raj "It would be amazing. There's so much we can learn from the past."

    menu:
        "Take a guided tour":
            jump take_guided_tour

        "Explore on their own":
            jump explore_on_own

label take_guided_tour:
    show amelia_tour_group with dissolve
    "The friends join a guided tour, led by a knowledgeable guide who shares the manor's rich history and stories of its former inhabitants."

    show tour_guide_explaining with dissolve
    tour_guide "This manor house dates back to the 16th century. It has been home to several prominent families, each leaving their mark on its history."

    show amelia_listening_tour with dissolve
    a "The details are fascinating. Every room has its own story."

    show lucas_agreeing_tour with dissolve
    lucas "And the guide really brings it to life. I'm learning so much."

    show zara_smiling_tour with dissolve
    zara "I love hearing about the personal stories of the people who lived here. It makes history feel so real."

    show raj_nodding_tour with dissolve
    raj "It's amazing to see how the past influences the present. There's so much we can learn from these stories."

    $ SD += 1
    $ SI += 1
    jump end_of_day

label explore_on_own:
    show amelia_exploring_house with dissolve
    "The friends decide to explore the manor on their own, wandering through its grand rooms and hidden corners."

    show amelia_finds_secret_door with dissolve
    "Amelia discovers a small, hidden door leading to a secret passage."

    show amelia_curious_secret_door with dissolve
    a "Look at this! A secret passage. I wonder where it leads."

    show lucas_excited_secret_door with dissolve
    lucas "Let's find out. This is like something out of a mystery novel."

    "They cautiously enter the passage, which leads to a hidden room filled with old books and artifacts."

    show amelia_marveling with dissolve
    a "This is incredible. It's like a hidden treasure trove."

    show zara_agreeing with dissolve
    zara "And these books... some of them look really old. They might hold valuable information."

    show raj_smiling with dissolve
    raj "We should tell the guide about this. They might not even know it's here."

    $ SD += 1
    $ SI += 1
    jump end_of_day

label explore_natural_beauty:
    show cornwall_nature_trail with dissolve
    "The group decides to explore the natural beauty of Cornwall, hiking along a scenic trail through forests and fields."

    show amelia_hiking with dissolve
    a "This is so refreshing. Being out in nature always helps me clear my mind."

    show lucas_agreeing_hiking with dissolve
    lucas "And it's a great workout too. The views are stunning."

    show zara_smiling_hiking with dissolve
    zara "I love how the landscape changes with every turn. There's so much to see and appreciate."

    show raj_nodding_hiking with dissolve
    raj "It's a reminder of how beautiful the world is. We should take more time to enjoy it."

    menu:
        "Pause for a picnic":
            jump pause_for_picnic

        "Continue hiking to a viewpoint":
            jump continue_hiking_viewpoint

label pause_for_picnic:
    show amelia_picnic with dissolve
    "The friends find a picturesque spot and pause for a picnic, enjoying the fresh air and beautiful scenery."

    show amelia_eating_picnic with dissolve
    a "This was a great idea. The food tastes even better out here."

    show lucas_agreeing_picnic with dissolve
    lucas "And it's a nice break from all the exploring. We can just relax and enjoy the moment."

    show zara_smiling_picnic with dissolve
    zara "It's the perfect way to recharge. I'm so glad we decided to do this."

    show raj_nodding_picnic with dissolve
    raj "Same here. It's a reminder to slow down and appreciate the little things."

    $ MH += 1
    $ SI += 1
    jump end_of_day

label continue_hiking_viewpoint:
    show cornwall_viewpoint with dissolve
    "The friends continue their hike to a viewpoint, where they are rewarded with a breathtaking panorama of the Cornwall countryside."

    show amelia_looking_out with dissolve
    a "Wow, this view is absolutely stunning. It makes all the effort worth it."

    show lucas_agreeing_viewpoint with dissolve
    lucas "I could stay here forever. It's so peaceful and inspiring."

    show zara_smiling_viewpoint with dissolve
    zara "It's moments like this that make me feel truly alive. I'm so grateful to be here with you all."

    show raj_nodding_viewpoint with dissolve
    raj "Same here. This is a memory I'll cherish forever."

    $ MH += 1
    $ SI += 1
    jump end_of_day

label meet_mentor_for_guidance:
    scene mentor_meeting_cafe with dissolve
    "Amelia arranges to meet her mentor at a cozy cafe, seeking guidance and advice for her next steps."

    if mentor == "Prof. Hawthorne":
        show hawthorne_waiting with dissolve
        "Prof. Hawthorne is waiting for her, a thoughtful expression on his face."

        show amelia_talking_hawthorne with dissolve
        a "Thank you for meeting with me, Professor. I've been thinking a lot about my academic path and how to make the most of it."

        show hawthorne_nodding with dissolve
        h "I'm glad you reached out, Amelia. You've made remarkable progress, and it's important to keep building on that momentum."

        menu:
            "Discuss academic specialization":
                jump discuss_academic_specialization

            "Propose a thesis topic":
                jump propose_thesis_topic

            "Seek advice on balancing responsibilities":
                jump seek_balance_advice

    elif mentor == "Dr. Simmons":
        show simmons_waiting with dissolve
        "Dr. Simmons is waiting for her, a warm smile on her face."

        show amelia_talking_simmons with dissolve
        a "Thank you for meeting with me, Dr. Simmons. I've been reflecting on my journey and how to maintain my well-being while pursuing my goals."

        show simmons_nodding with dissolve
        s "I'm happy to help, Amelia. It's crucial to find a balance that allows you to thrive both personally and academically."

        menu:
            "Establish a self-care routine":
                jump establish_self_care_routine

            "Support Sarah's recovery":
                jump support_sarah_recovery

            "Seek advice on mental resilience":
                jump seek_mental_resilience_advice

    elif mentor == "Maya":
        show maya_waiting with dissolve
        "Maya is waiting for her, an aura of calm and wisdom surrounding her."

        show amelia_talking_maya with dissolve
        a "Thank you for meeting with me, Maya. I've been exploring my spiritual path and seeking deeper understanding."

        show maya_nodding with dissolve
        m "I'm glad you came, Amelia. The journey of self-discovery is ongoing, and I'm here to support you."

        menu:
            "Interpret prophetic dreams":
                jump interpret_prophetic_dreams

            "Seek out ancient artifacts":
                jump seek_ancient_artifacts

            "Share knowledge selectively":
                jump share_knowledge_selectively

label solo_occult_research:
    show amelia_library_studying with dissolve
    "Amelia decides to spend the day diving into solo research on the occult, determined to uncover new insights and knowledge."

    show amelia_studying_books with dissolve
    "She finds a quiet corner in the library and surrounds herself with ancient texts and esoteric manuscripts."

    show amelia_deep_reading with dissolve
    a "(There's so much to learn. Each book holds a piece of the puzzle, and I need to fit them together.)"

    menu:
        "Study ancient rituals":
            jump study_ancient_rituals

        "Research mystical symbols":
            jump research_mystical_symbols

        "Read about historical figures":
            jump read_historical_figures

label study_ancient_rituals:
    show amelia_reading_rituals with dissolve
    "Amelia immerses herself in the study of ancient rituals, fascinated by the intricate ceremonies and their meanings."

    show amelia_fascinated_rituals with dissolve
    a "These rituals were powerful ways to connect with the spiritual realm. Understanding them could unlock new levels of knowledge."

    menu:
        "Try a simple ritual":
            jump try_simple_ritual

        "Take detailed notes":
            jump take_detailed_notes

label try_simple_ritual:
    show amelia_performing_ritual with dissolve
    "Amelia decides to try a simple ritual, following the instructions carefully and focusing her intent."

    show amelia_mystical_experience with dissolve
    "As she performs the ritual, she feels a surge of energy and a sense of connection to the ancient wisdom."

    show amelia_revelation with dissolve
    a "(This is incredible. I can feel the power of the ritual working. There's so much more to explore.)"

    $ OK += 2
    $ SD += 1
    jump end_of_day

label take_detailed_notes:
    show amelia_writing_notes with dissolve
    "Amelia takes detailed notes on the rituals, capturing every step and its significance."

    show amelia_thinking_notes with dissolve
    a "These notes will be invaluable for my research. There's so much depth to these rituals, and I'm only scratching the surface."

    $ OK += 1
    $ SD += 1
    jump end_of_day

label research_mystical_symbols:
    show amelia_reading_symbols with dissolve
    "Amelia focuses her research on mystical symbols, intrigued by their meanings and uses."

    show amelia_fascinated_symbols with dissolve
    a "These symbols hold powerful meanings. Understanding them could reveal new insights into the occult."

    menu:
        "Draw the symbols":
            jump draw_symbols

        "Analyze their meanings":
            jump analyze_meanings

label draw_symbols:
    show amelia_drawing_symbols with dissolve
    "Amelia carefully draws the mystical symbols, paying close attention to their intricate details."

    show amelia_satisfied_drawing with dissolve
    a "These symbols are fascinating. Each one has a unique meaning and power."

    $ OK += 1
    $ SD += 1
    jump end_of_day

label analyze_meanings:
    show amelia_analyzing_symbols with dissolve
    "Amelia analyzes the meanings of the symbols, cross-referencing them with her other research."

    show amelia_thinking_symbols with dissolve
    a "There's a pattern here. These symbols are connected in ways I hadn't realized before."

    $ OK += 1
    $ SD += 1
    jump end_of_day

label read_historical_figures:
    show amelia_reading_figures with dissolve
    "Amelia reads about historical figures in the occult, learning about their lives and contributions."

    show amelia_fascinated_figures with dissolve
    a "These figures were pioneers in the field. Their stories are inspiring and full of valuable lessons."

    menu:
        "Write a research paper":
            jump write_research_paper

        "Create a presentation":
            jump create_presentation

label write_research_paper:
    show amelia_writing_paper with dissolve
    "Amelia decides to write a research paper on the historical figures, synthesizing her findings and insights."

    show amelia_proud_paper with dissolve
    a "This paper is turning out great. It's a comprehensive look at the contributions of these figures."

    $ OK += 1
    $ AA += 1
    jump end_of_day

label create_presentation:
    show amelia_creating_presentation with dissolve
    "Amelia creates a presentation on the historical figures, highlighting their achievements and impact."

    show amelia_proud_presentation with dissolve
    a "This presentation is really coming together. It's a great way to share what I've learned."

    $ OK += 1
    $ SD += 1
    jump end_of_day

label end_of_day:
    scene amelia_dorm_evening with dissolve
    "As the day comes to an end, Amelia returns to her dorm room, reflecting on the day's experiences."

    show amelia_reflective_evening with dissolve
    a "(Today was incredible. I learned so much and had such meaningful experiences. I feel more connected to my path than ever before.)"

    "With a sense of fulfillment and anticipation for what tomorrow will bring, Amelia settles into bed, ready for the next chapter of her journey."

    jump chapter_7_part_3

label chapter_7_part_3:

    scene amelia_dorm_morning with dissolve
    "The sun rises over Plymouth University, marking the beginning of another eventful day for Amelia."

    show amelia_stretching_dorm with dissolve
    a "Today feels like it's going to be significant. I need to make the most of it."

    menu:
        "Attend an important lecture":
            jump attend_important_lecture

        "Spend time with friends":
            jump spend_time_with_friends

        "Focus on occult research":
            jump focus_occult_research

label attend_important_lecture:
    scene lecture_hall with dissolve
    "Amelia heads to the lecture hall for a class that promises to be particularly engaging."

    show professor_lecturing with dissolve
    "The professor, a renowned expert in the field, begins to speak passionately about the topic."

    show amelia_listening_intently with dissolve
    professor "Today, we'll delve into the complexities of human cognition and its impact on behavior. Understanding these intricacies is crucial for any aspiring psychologist."

    show amelia_taking_notes with dissolve
    "Amelia takes diligent notes, her mind buzzing with the implications of the lecture."

    menu:
        "Ask a question during the lecture":
            jump ask_question_lecture

        "Approach the professor after the lecture":
            jump approach_professor_after

label ask_question_lecture:
    show amelia_raising_hand with dissolve
    a "Professor, how do cultural differences influence cognitive processes and behavior?"

    show professor_answering with dissolve
    professor "Excellent question, Amelia. Cultural context plays a significant role in shaping cognitive processes. For instance, research shows that individuals from collectivist cultures often exhibit different problem-solving strategies compared to those from individualist cultures. This is due to varying emphases on community versus individual achievement."

    show amelia_nodding_understanding with dissolve
    a "That's fascinating. Thank you, Professor."

    $ AA += 1
    jump end_of_lecture

label approach_professor_after:
    show amelia_talking_professor with dissolve
    a "Professor, I found today's lecture incredibly insightful. I'm particularly interested in the intersection of cognition and cultural context."

    show professor_smiling with dissolve
    professor "I'm glad to hear that, Amelia. It's a rich area of study with many opportunities for research. If you're interested, I could recommend some additional readings and perhaps even involve you in a current research project I'm supervising."

    menu:
        "Accept the offer":
            jump accept_research_offer

        "Thank the professor and decline":
            jump decline_research_offer

label accept_research_offer:
    show amelia_excited with dissolve
    a "I would love to be involved in the research project. Thank you for the opportunity!"

    show professor_nodding with dissolve
    professor "Excellent. I'll send you the details via email. Looking forward to working with you."

    $ AA += 1
    $ SD += 1
    jump end_of_lecture

label decline_research_offer:
    show amelia_thankful with dissolve
    a "Thank you, Professor. I appreciate the offer, but I need to focus on my current commitments."

    show professor_understanding with dissolve
    professor "I understand. Balancing responsibilities is important. If you ever change your mind, the offer stands."

    jump end_of_lecture

label end_of_lecture:
    scene campus_exterior with dissolve
    "After the lecture, Amelia steps outside, feeling invigorated by the knowledge she's gained."

    menu:
        "Reflect on the lecture in the library":
            jump reflect_lecture_library

        "Meet up with friends":
            jump meet_up_with_friends

label reflect_lecture_library:
    scene library_interior with dissolve
    "Amelia heads to the library to reflect on the lecture and dive deeper into the material."

    show amelia_studying_library with dissolve
    "She finds a quiet corner and begins reading the recommended texts, jotting down notes and insights."

    show amelia_lost_in_thought with dissolve
    a "(This is so engaging. I feel like I'm really starting to grasp the complexities of cognitive processes and their cultural implications.)"

    $ AA += 1
    $ SD += 1
    jump end_of_day

label meet_up_with_friends:
    scene student_union with dissolve
    "Amelia decides to meet up with her friends at the student union."

    show lucas_zara_raj_laughing with dissolve
    "Lucas, Zara, and Raj are already there, laughing and chatting."

    show amelia_joining_friends with dissolve
    a "Hey everyone, what’s so funny?"

    show zara_smiling with dissolve
    zara "Oh, just Lucas and his terrible jokes. How was your lecture, Amelia?"

    show amelia_smiling_friends with dissolve
    a "It was amazing. The professor really knows how to make complex topics interesting."

    menu:
        "Share details about the lecture":
            jump share_lecture_details

        "Ask about their day":
            jump ask_about_their_day

label share_lecture_details:
    show amelia_explaining_lecture with dissolve
    a "We talked about how cultural differences influence cognition. It's fascinating how much our environment shapes our thought processes."

    show raj_interested with dissolve
    raj "That sounds really interesting. It’s incredible how interconnected everything is."

    show lucas_joking with dissolve
    lucas "As long as you don’t start analyzing our every thought and action, Amelia."

    show zara_laughing with dissolve
    zara "Yeah, we don’t need a psychologist in our friend group."

    show amelia_laughing with dissolve
    a "Don’t worry, I won’t psychoanalyze you. But it’s good to know how these things work."

    $ SI += 1
    jump end_of_day

label ask_about_their_day:
    show amelia_listening_friends with dissolve
    a "Enough about my lecture. How was your day, everyone?"

    show lucas_smiling with dissolve
    lucas "Busy, but good. We had a guest speaker in our history class who was amazing."

    show zara_nodding with dissolve
    zara "I had a productive day in the lab. Our project is really coming together."

    show raj_happy with dissolve
    raj "I aced my math test, so I’m feeling pretty great."

    show amelia_happy_for_friends with dissolve
    a "That’s awesome! I’m glad everyone had a good day."

    $ SI += 1
    jump end_of_day

label focus_occult_research:
    scene library_interior with dissolve
    "Amelia decides to focus on her occult research, eager to uncover new insights."

    show amelia_studying_occult_books with dissolve
    "She finds a secluded spot in the library and immerses herself in ancient texts and mystical writings."

    show amelia_fascinated_occult with dissolve
    a "(The more I learn, the more I realize how much there is to discover. These texts are filled with knowledge waiting to be unlocked.)"

    menu:
        "Study ancient symbols":
            jump study_ancient_symbols

        "Research prophetic dreams":
            jump research_prophetic_dreams

        "Explore mystical rituals":
            jump explore_mystical_rituals

label study_ancient_symbols:
    show amelia_drawing_symbols with dissolve
    "Amelia spends hours studying ancient symbols, drawing them carefully and noting their meanings."

    show amelia_deep_in_thought with dissolve
    a "(These symbols hold so much power and significance. Each one is a key to deeper understanding.)"

    $ OK += 1
    $ SD += 1
    jump end_of_day

label research_prophetic_dreams:
    show amelia_reading_dreams with dissolve
    "Amelia researches prophetic dreams, reading accounts from ancient seers and modern scholars."

    show amelia_fascinated_dreams with dissolve
    a "(Dreams are a window into the subconscious. Understanding them could reveal hidden truths.)"

    menu:
        "Keep a dream journal":
            jump keep_dream_journal

        "Analyze famous dreams":
            jump analyze_famous_dreams

label keep_dream_journal:
    show amelia_writing_journal with dissolve
    "Amelia decides to keep a dream journal, recording her own dreams and interpreting their meanings."

    show amelia_lost_in_thought with dissolve
    a "(This is fascinating. My dreams are becoming clearer, and I’m starting to see patterns and symbols.)"

    $ OK += 1
    $ SD += 1
    jump end_of_day

label analyze_famous_dreams:
    show amelia_analyzing_dreams with dissolve
    "Amelia analyzes famous prophetic dreams, comparing them to her own experiences."

    show amelia_thinking_deeply with dissolve
    a "(These dreams share common themes and symbols. There’s a deeper connection here.)"

    $ OK += 1
    $ SD += 1
    jump end_of_day

label explore_mystical_rituals:
    show amelia_reading_rituals with dissolve
    "Amelia explores mystical rituals, reading about their history and significance."

    show amelia_fascinated_rituals with dissolve
    a "(These rituals are powerful ways to connect with the spiritual realm. I need to understand them fully.)"

    menu:
        "Perform a small ritual":
            jump perform_small_ritual

        "Document the rituals":
            jump document_rituals

label perform_small_ritual:
    show amelia_preparing_ritual with dissolve
    "Amelia decides to perform a small ritual, carefully following the steps outlined in her books."

    show amelia_feeling_energy with dissolve
    "As she completes the ritual, she feels a surge of energy and a deep sense of connection."

    show amelia_smiling_peacefully with dissolve
    a "(That was incredible. I feel more connected to the spiritual world.)"

    $ OK += 1
    $ MH += 1
    jump end_of_day

label document_rituals:
    show amelia_writing_rituals with dissolve
    "Amelia documents the rituals she reads about, creating detailed notes and diagrams."

    show amelia_proud_notes with dissolve
    a "(These notes will be valuable for my research. I’m building a comprehensive understanding.)"

    $ OK += 1
    $ SD += 1
    jump end_of_day

label end_of_day:
    scene amelia_dorm_evening with dissolve
    "As the day comes to an end, Amelia returns to her dorm room, reflecting on the day's experiences."

    show amelia_reflective_evening with dissolve
    a "(Today was incredible. I learned so much and had such meaningful experiences. I feel more connected to my path than ever before.)"

    "With a sense of fulfillment and anticipation for what tomorrow will bring, Amelia settles into bed, ready for the next chapter of her journey."

    jump chapter_8


