label call_to_adventure:
    stop music fadeout 1.0

    show black
    with dissolve

    "The Call to Adventure"

    # 1. Departure Day
    show amelia_room_full
    with dissolve

    menu:
        "Spend extra time with family (+1 SI)":
            $ SI += 1
            show amelia_family_full
            a "I should spend some more time with my family before I leave. They've always been there for me."

            menu:
                "Heartfelt conversation (+1 MH)":
                    $ MH += 1
                    show amelia_family_conversation_full
                    a "Mom, Dad, I just want to thank you for everything. Your love and support mean the world to me."
                    mom "Oh, sweetie, we're so proud of you. You're going to do great things."
                    dad "We'll always be here for you, Amelia. No matter what."
                    a "I love you both so much."

                "Practical advice (+1 MC)":
                    $ MC += 1
                    show amelia_family_advice_full
                    a "Do you have any last-minute advice for me before I head off to university?"
                    mom "Just remember to stay focused on your studies, but also make time for yourself."
                    dad "And don't be afraid to ask for help if you need it. That's what professors and advisors are there for."
                    a "Thanks, I'll keep that in mind."

        "Double-check packing (+1 AA)":
            $ AA += 1
            show amelia_packing_full
            a "I better make sure I have everything I need. I don't want to forget anything important."

            menu:
                "Review study materials (+1 AA)":
                    $ AA += 1
                    show amelia_study_materials_full
                    a "Let's see... textbooks, check. Laptop, check. Notebooks and pens, check."
                    a "I think I'm all set academically. Bring on the psychology courses!"

                "Pack a sentimental item (+1 SD)":
                    $ SD += 1
                    show amelia_sentimental_item_full
                    a "I can't forget to pack this photo of me and Ella. And the bracelet Mom gave me for my birthday."
                    a "These little pieces of home will remind me of the love and support I have, even when I'm far away."

    # Special Scene (if SI > 3)
    if SI > 3:
        show amelia_farewell_party_full
        with dissolve

        a "What's all this?"

        ella "Surprise! We couldn't let you leave without a proper farewell party."
        mom "We're so excited for you, Amelia. But we're going to miss you so much."
        dad "We wanted to show you how much we love and support you."

        $ SI += 2
        $ MH += 1

        a "You guys... this is amazing. I'm going to miss you all so much. Thank you for everything."

    # 2. Train Ride to Plymouth
    show amelia_train_full
    with dissolve

    a "Well, this is it. The start of my new adventure."

    menu:
        "Engage in conversation with another student (+1 SI)":
            $ SI += 1
            show amelia_talking_student_full
            a "Hi there! Are you heading to Plymouth University too?"

            student "Yeah, I am! I'm so excited. What are you planning to study?"

            menu:
                "Discuss academic interests (+1 AA)":
                    $ AA += 1
                    show amelia_discuss_academics_full
                    a "I'm diving into psychology. I've always been fascinated by the human mind."
                    student "That's so cool! I'm more into the sciences myself, but psychology sounds really interesting."
                    a "It is! There's so much to explore. I can't wait to get started."

                "Discuss personal backgrounds (+1 SI)":
                    $ SI += 1
                    show amelia_discuss_background_full
                    a "Psychology for me. But enough about academics, tell me about yourself! Where are you from?"
                    student "I'm from Brighton originally. It's going to be a big change, moving to a new city."
                    a "I know what you mean. I'm equal parts nervous and excited. But I think it's going to be an amazing experience."

        "Reflect quietly (+1 SD)":
            $ SD += 1
            show amelia_reflect_full
            a "I think I'll take this time to reflect on my own thoughts and feelings."

            menu:
                "Write in journal (+1 MH)":
                    $ MH += 1
                    show amelia_journal_full
                    a "Writing has always been a great way for me to process my emotions."
                    "Amelia takes out her journal and begins to write."
                    a "{i}Today marks the start of a new chapter. I'm feeling so many things - excitement, nervousness, hope. But above all, I feel ready. Ready to learn, to grow, to discover who I am and who I want to be.{/i}"

                "Observe passing landscapes (+1 SD)":
                    $ SD += 1
                    show amelia_observe_landscape_full
                    a "Sometimes, just observing the world around me helps me gain perspective."
                    "Amelia gazes out the window, taking in the changing scenery."
                    a "It's beautiful, isn't it? All these different landscapes, blurring together. Kind of like life - a series of moments and experiences, each one shaping us in its own way."

    # Special Scene (if AA > 3 and SD > 3)
    if AA > 3 and SD > 3:
        show amelia_meet_professor_full
        with dissolve

        professor "Excuse me, I couldn't help but overhear your conversation earlier. You seem to have a deep passion for psychology."

        a "Oh, yes, I do! I'm actually starting my psychology degree at Plymouth University."

        professor "Wonderful! I'm a professor there, in the psychology department. It's always a delight to meet enthusiastic students."

        a "That's amazing! I'd love to hear more about your research and the program."

        "The professor and Amelia engage in a thought-provoking discussion about various psychological theories and their applications."

        $ AA += 2
        $ SD += 1

        professor "You have a bright future ahead of you, young lady. I look forward to seeing you in class."
        a "Thank you so much, professor. This has been incredibly insightful."

    # 3. Arrival at Plymouth
    show amelia_plymouth_campus_full
    with dissolve

    a "Wow, the campus is even more beautiful than I imagined."

    menu:
        "Explore the campus on her own (+1 SD)":
            $ SD += 1
            show amelia_explore_campus_full
            a "I think I'll take some time to explore on my own, get a feel for the place."

            menu:
                "Visit the library (+1 AA)":
                    $ AA += 1
                    show amelia_library_full
                    a "The library seems like a good place to start. So many books, so much knowledge!"
                    "Amelia browses the shelves, marveling at the extensive collection."
                    a "I can already tell I'm going to be spending a lot of time here."

                "Visit the psychology department (+1 SD)":
                    $ SD += 1
                    show amelia_psych_department_full
                    a "I should familiarize myself with the psychology department."
                    "Amelia walks through the department, reading the various posters and notices."
                    a "This is where I'll be spending the next few years, delving into the mysteries of the mind. How exciting!"

        "Ask for directions (+1 SI)":
            $ SI += 1
            show amelia_ask_directions_full
            a "I should probably ask someone for directions, make sure I know where I'm going."

            menu:
                "Engage with a friendly student (+1 SI)":
                    $ SI += 1
                    show amelia_friendly_student_full
                    a "Excuse me, I'm new here. Could you point me towards the student union?"
                    student "Of course! It's just down that path and to the left. I'm heading that way myself, I can walk with you if you'd like."
                    a "That would be great, thanks! I'm Amelia, by the way."
                    student "Nice to meet you, Amelia. I'm Sam. Welcome to Plymouth!"

                "Engage with a helpful staff member (+1 MC)":
                    $ MC += 1
                    show amelia_staff_member_full
                    a "Hello, I'm a new student. Could you help me find the registrar's office?"
                    staff "Certainly! It's in the main administrative building, just over there. Let me know if you need anything else."
                    a "Thank you so much. I appreciate your help."
                    staff "No problem at all. That's what we're here for. Enjoy your time at Plymouth!"

    # Special Scene (if SD > 5)
    if SD > 5:
        show amelia_hidden_garden_full
        with dissolve

        a "Oh wow, what a beautiful garden! I didn't expect to find this here."

        "Amelia takes a moment to admire the tranquil surroundings, the gentle rustling of leaves, and the soft chirping of birds."

        a "This is perfect. A little oasis of calm amidst the bustling campus."

        $ SD += 2
        $ MH += 1

        a "I'll have to remember this spot. Whenever I need a break or a quiet place to think, I'll come here."

    # 4. Moving into the Dorm
    show amelia_dorm_room_full
    with dissolve

    a "So this is my new home. It's not much, but it's mine."

    menu:
        "Decorate with academic posters (+1 AA)":
            $ AA += 1
            show amelia_academic_posters_full
            a "I think some academic posters would really inspire me to study hard."

            menu:
                "Choose famous psychologists posters (+1 AA)":
                    $ AA += 1
                    show amelia_psychologists_posters_full
                    a "Freud, Jung, Pavlov... these pioneers of psychology will remind me of the great minds that came before."
                    "Amelia hangs up posters of renowned psychologists, their faces and key theories decorating her walls."

                "Choose inspiring quotes posters (+1 MH)":
                    $ MH += 1
                    show amelia_quotes_posters_full
                    a "Some motivational quotes would be great to keep me going when times get tough."
                    "Amelia selects posters with uplifting messages and affirmations, creating a positive atmosphere in her room."

        "Decorate with personal photos (+1 SI)":
            $ SI += 1
            show amelia_personal_photos_full
            a "Some photos of my family and friends will make this place feel more like home."

            menu:
                "Display family photos (+1 SI)":
                    $ SI += 1
                    show amelia_family_photos_full
                    a "I'll put this family photo right by my bed, so they're the first thing I see in the morning."
                    "Amelia lovingly arranges pictures of her parents, siblings, and extended family around her room."

                "Display travel memories (+1 SD)":
                    $ SD += 1
                    show amelia_travel_memories_full
                    a "These photos from my travels will remind me of the adventures I've had and the ones yet to come."
                    "Amelia creates a collage of images from various trips, a visual representation of her experiences and growth."

    show amelia_meet_roommate_full
    with dissolve

    roommate "Hey there! You must be Amelia. I'm your new roommate, Liz!"

    a "Hi Liz, it's great to meet you! I'm looking forward to getting to know you."

    # Special Scene (if SI > 5 and MH > 5)
    if SI > 5 and MH > 5:
        show amelia_roommate_confession_full
        roommate "Can I confess something to you, Amelia? I'm actually really nervous about starting university."

        a "Oh Liz, that's totally understandable. It's a big change for all of us."

        roommate "I've been dealing with some personal struggles lately, and I'm worried it'll affect my studies."

        a "I'm here for you, Liz. If you ever need to talk or just want some support, I'm always willing to listen."

        roommate "Thank you, Amelia. That means a lot to me. I can already tell we're going to be great friends."

        $ SI += 2
        $ MH += 1

        a "I feel the same way, Liz. We'll get through this together."

    # 5. Orientation Week
    show amelia_orientation_week_full
    with dissolve

    a "Orientation week... so many events to choose from!"

    menu:
        "Attend an academic seminar (+1 AA)":
            $ AA += 1
            show amelia_academic_seminar_full
            a "This seminar on recent developments in psychology looks fascinating."

            menu:
                "Ask a question (+1 AA)":
                    $ AA += 1
                    show amelia_ask_question_full
                    "Amelia raises her hand during the Q&A portion of the seminar."
                    a "Professor, could you elaborate on how this new theory might be applied in clinical settings?"
                    "The professor nods, impressed by Amelia's insightful question."
                    professor "Excellent question! In practice, this theory could be used to..."

                "Take detailed notes (+1 SD)":
                    $ SD += 1
                    show amelia_take_notes_full
                    "Amelia listens attentively, jotting down key points and references."
                    a "{i}This is groundbreaking stuff. I'll need to do some more research on this later.{/i}"
                    "By the end of the seminar, Amelia's notebook is filled with valuable information and ideas to explore further."

        "Attend a social mixer (+1 SI)":
            $ SI += 1
            show amelia_social_mixer_full
            a "A social mixer could be a great way to meet new people and make friends."

            menu:
                "Join a club (+1 SI)":
                    $ SI += 1
                    show amelia_join_club_full
                    "Amelia browses the various club booths, chatting with representatives."
                    a "The Psychology Society seems perfect for me! And maybe I'll join the Hiking Club too, for some outdoor adventures."
                    "Amelia signs up for a few clubs, excited to get involved in campus life."

                "Volunteer for an event (+1 MC)":
                    $ MC += 1
                    show amelia_volunteer_event_full
                    "Amelia notices a sign-up sheet for orientation week volunteers."
                    a "Helping out with events would be a great way to give back and meet people at the same time."
                    "Amelia puts her name down for several volunteering slots, ready to make a positive impact."

    # Special Scene (if AA > 7 and SI > 7)
    if AA > 7 and SI > 7:
        show amelia_dinner_with_faculty_full
        with dissolve

        a "An invitation to dinner with the psychology faculty? Wow, what an honor!"

        professor "Amelia, we've been very impressed with your participation and insights during orientation week."

        a "Thank you so much, professor. I'm just thrilled to be here and to learn from all of you."

        professor "We see great potential in you. Keep up the excellent work, and don't hesitate to come to us with any questions or ideas."

        $ AA += 2
        $ SI += 1

        a "I will, absolutely. This is an incredible opportunity. I'm so grateful to be part of this department."

    # 6. First Classes
    show amelia_first_classes_full
    with dissolve

    a "My first official classes... I've been waiting for this moment."

    menu:
        "Participate in class discussions (+1 AA)":
            $ AA += 1
            show amelia_class_discussion_full
            a "I want to engage with the material and share my thoughts."

            menu:
                "Offer a unique perspective (+1 AA)":
                    $ AA += 1
                    show amelia_unique_perspective_full
                    "During a discussion on nature vs. nurture, Amelia raises her hand."
                    a "I think it's not just a question of nature or nurture, but how they interact. Epigenetics has shown that our experiences can actually change gene expression."
                    "The professor nods, impressed."
                    professor "Excellent point, Amelia. The interplay between genes and environment is a crucial consideration."

                "Relate to personal experiences (+1 SD)":
                    $ SD += 1
                    show amelia_personal_experiences_full
                    "The class discusses the impact of childhood experiences on adult behavior."
                    a "I can relate to this. Growing up, my parents always encouraged me to express my emotions. I think that's why I'm so drawn to psychology - to understand those early influences."
                    "The professor smiles."
                    professor "Thank you for sharing, Amelia. Personal insights like these can really enrich our understanding of the theories we study."

                "Observe and take notes (+1 SD)":
                    $ SD += 1
                    show amelia_observe_notes_full
                    a "I want to absorb as much as I can and reflect on it later."

                    menu:
                        "Focus on professor's lecture (+1 AA)":
                            $ AA += 1
                            show amelia_professor_lecture_full
                            "Amelia listens intently to the professor's every word, trying to capture the key points."
                            "She jots down the main theories, researchers, and studies mentioned."
                            a "{i}This is the foundation. I need to make sure I have a solid grasp of these core concepts.{/i}"

                        "Focus on classmates' reactions (+1 SD)":
                            $ SD += 1
                            show amelia_classmates_reactions_full
                            "Amelia observes her classmates as they react to the lecture."
                            "She notes who seems engaged, who looks confused, who has strong emotional responses."
                            a "{i}Everyone brings their own perspective. Understanding their reactions can be just as enlightening as the lecture itself.{/i}"

    # Special Scene (if AA > 10)
    if AA > 10:
        show amelia_professor_praise_full
        "After class, the professor approaches Amelia."

        professor "Amelia, I must say, your contributions to the class discussion have been outstanding."

        a "Thank you, professor. I'm just so passionate about the subject matter."

        professor "It shows. Your insights are well beyond what I typically see from first-year students."

        a "I've been reading a lot of extra material outside of class. I want to deepen my understanding as much as possible."

        professor "That's excellent. Keep up that curiosity and drive. If you ever want to discuss your ideas further, my door is always open."

        $ AA += 2
        $ MC += 1

        a "I would love that. Thank you so much for the encouragement, professor."

    # 7. Social Interactions
    show amelia_campus_cafe_full
    with dissolve

    a "University isn't just about academics. I should put myself out there socially too."

    menu:
        "Attend a study group (+1 AA)":
            $ AA += 1
            show amelia_study_group_full
            a "Collaborating with others can really enhance the learning experience."

            menu:
                "Lead a discussion (+1 AA)":
                    $ AA += 1
                    show amelia_lead_discussion_full
                    "In the study group, Amelia takes the initiative to start a discussion."
                    a "I thought we could start by each sharing our key takeaways from the last lecture, then discuss how they connect to the readings."
                    "The other students nod in agreement, impressed by Amelia's leadership."

                "Share study tips (+1 MC)":
                    $ MC += 1
                    show amelia_share_study_tips_full
                    "As the study group progresses, Amelia offers some advice."
                    a "I've found that making concept maps really helps me visualize the relationships between ideas. I'm happy to show you all how I do it."
                    "The other students appreciate Amelia's willingness to help."

        "Attend a social event (+1 SI)":
            $ SI += 1
            show amelia_social_event_full
            a "It's important to relax and have fun too. A balanced life is a healthy life."

            menu:
                "Engage in meaningful conversations (+1 SI)":
                    $ SI += 1
                    show amelia_meaningful_conversations_full
                    "At the social event, Amelia strikes up conversations with various people."
                    "She asks about their backgrounds, their interests, their hopes for the future."
                    a "Everyone has such a unique story. It's fascinating to see how our diverse experiences have brought us all here."

                "Try a new activity (+1 SD)":
                    $ SD += 1
                    show amelia_try_new_activity_full
                    "Amelia notices a group of students setting up for an impromptu theater game."
                    a "I've never tried improv before, but it looks like fun! Mind if I join in?"
                    "The students welcome Amelia enthusiastically, and she finds herself laughing and creating alongside her new friends."

    # Special Scene (if SI > 10 and MH > 7)
    if SI > 10 and MH > 7:
        show amelia_meet_lucas_full
        a "Hey, I don't think we've met before. I'm Amelia."
        lucas "Hi Amelia, I'm Lucas. Nice to meet you."
        a "So, what brings you to this event?"

        lucas "Honestly, I'm trying to push myself out of my comfort zone. I can be a bit introverted, but I know connections are important."

        a "I completely understand. It can be daunting, but we're all in the same boat here. And you never know when you'll meet someone who really gets you."

        lucas "That's so true. And speaking of getting each other... I couldn't help but overhear your conversation earlier about the psychology of emotions. Fascinating stuff."

        a "Oh, you're interested in psychology too?"

        lucas "Absolutely! I'm particularly drawn to Jungian psychology and the idea of the collective unconscious."

        a "No way! I've been delving into Jung's work myself. The archetypes, the shadow, the individuation process... it's all so rich."

        lucas "Wow, Amelia. It's not often I meet someone who shares my passion for this. We should definitely continue this conversation."

        $ SI += 2
        $ MH += 1

        a "I would love that, Lucas. I have a feeling this is the start of a great friendship."

    # 8. Facing Initial Challenges
    show amelia_dorm_room_night_full
    with dissolve

    a "Ugh, I'm feeling so overwhelmed. Balancing classes, socializing, and self-care is harder than I thought."

    menu:
        "Seek support from a friend (+1 SI)":
            $ SI += 1
            show amelia_seek_support_full
            a "I should reach out to someone. I don't have to deal with this alone."

            menu:
                "Open up about struggles (+1 MH)":
                    $ MH += 1
                    show amelia_open_up_struggles_full
                    "Amelia calls up Ella."
                    a "Hey Ella, do you have a minute to talk? I'm having a tough time adjusting to university life."
                    ella "Of course, Amelia. I'm always here for you. What's been going on?"
                    "Amelia shares her struggles, and Ella listens with empathy and understanding."

                "Ask for practical advice (+1 MC)":
                    $ MC += 1
                    show amelia_practical_advice_full
                    "Amelia sends a message to her roommate Liz."
                    a "Hey Liz, how do you manage your time effectively? I feel like I'm drowning in deadlines."
                    liz "I've found that breaking tasks down into smaller chunks and setting mini-goals helps a lot. Want me to show you my system?"
                    a "That would be amazing, Liz. Thank you!"

        "Tackle the challenge independently (+1 SD)":
            $ SD += 1
            show amelia_tackle_challenge_full
            a "I need to find ways to cope on my own. This is an opportunity for growth."

            menu:
                "Create a detailed plan (+1 AA)":
                    $ AA += 1
                    show amelia_detailed_plan_full
                    "Amelia sits down at her desk and starts organizing her tasks."
                    a "Okay, let's prioritize. Upcoming deadlines first, then long-term projects. Block out study time, break times, and sleep."
                    "She creates a color-coded schedule, feeling a sense of control return."

                "Practice self-care (+1 MH)":
                    $ MH += 1
                    show amelia_self_care_full
                    "Amelia closes her eyes and takes a deep breath."
                    a "I need to remember to take care of myself. Yoga, meditation, journaling... these are all tools I can use."
                    "She spends the next hour engaging in calming activities, feeling her stress melt away."

    # Special Scene (if MH > 10)
    if MH > 10:
        show amelia_peace_garden_full
        with dissolve

        "Amelia wanders the campus, seeking solace, and stumbles upon a beautiful garden she hadn't noticed before."

        a "Wow, what a serene spot. The perfect place for a mental reset."

        "She sits on a bench, surrounded by lush greenery and the gentle sounds of a trickling fountain."

        a "I can feel my worries fading away. There's something about being in nature that just soothes the soul."

        $ MH += 2
        $ SD += 1

        "Amelia makes a mental note to return to this garden whenever she needs a moment of peace."

    # 9. Hints of the Journey Ahead
    show amelia_lecture_hall_full
    with dissolve

    a "As the semester progresses, I feel my interests in psychology deepening and diversifying."

    menu:
        "Attend a lecture on a niche topic (+1 OK)":
            $ OK += 1
            show amelia_niche_topic_full
            a "This guest lecture on the psychology of alchemy sounds intriguing. I've never explored that intersection before."

            menu:
                "Dive into related research (+1 OK)":
                    $ OK += 1
                    show amelia_related_research_full
                    "After the lecture, Amelia's curiosity is piqued."
                    a "I need to know more about this. Time to hit the library and see what I can find on alchemical symbolism and its psychological implications."
                    "She spends hours poring over obscure texts, fascinated by the depths of this esoteric knowledge."

                "Discuss with the professor (+1 AA)":
                    $ AA += 1
                    show amelia_discuss_professor_full
                    "Amelia approaches the guest lecturer after the talk."
                    a "Professor, your lecture was fascinating. I'd love to discuss further how alchemical principles might be applied in modern psychotherapy."
                    "The professor is impressed by Amelia's innovative thinking and engages her in a stimulating discussion."

        "Attend a lecture on a broad topic (+1 AA)":
            $ AA += 1
            show amelia_broad_topic_full
            a "This overview of the different branches of psychology will give me a good foundation to build on."

            menu:
                "Consider potential specializations (+1 SD)":
                    $ SD += 1
                    show amelia_potential_specializations_full
                    "As the lecturer describes the various subfields, Amelia reflects on her own interests."
                    a "{i}Clinical psychology, developmental psychology, cognitive neuroscience... so many paths to explore. Where do I see myself making the biggest impact?{/i}"
                    "She jots down notes, excited to delve deeper into the areas that resonate with her."

                "Connect topics to personal interests (+1 SD)":
                    $ SD += 1
                    show amelia_personal_interests_full
                    "Amelia listens to the lecture, making connections to her own life."
                    a "{i}The psychology of motivation... that explains so much about my drive to understand the mind. And social psychology... I can see how that plays out in my own relationships.{/i}"
                    "She feels a growing sense of self-awareness and a desire to apply these insights to her personal growth."

    # Special Scene (if OK > 3 and AA > 12)
    if OK > 3 and AA > 12:
        show amelia_library_full
        with dissolve

        "While browsing the library shelves, Amelia's eye is caught by an old, leather-bound book."

        a "Huh, 'The Alchemical Path to Self-Transformation'... how peculiar."

        "She pulls the book from the shelf and starts flipping through it."

        a "Woah... this goes way beyond just turning lead into gold. It's about the transformation of the psyche, the integration of the unconscious..."

        $ OK += 2
        $ AA += 1

        "Amelia becomes engrossed in the text, realizing that it holds profound implications for her understanding of psychology."

        a "I feel like I'm on the brink of something big here. These ancient teachings... they're not just historical curiosities. They hold wisdom that we can still apply today."

        "She checks out the book, knowing that this is just the beginning of a deep dive into the mystical dimensions of the mind."

    show amelia_dorm_room_evening_full
    with dissolve

    a "As the first semester comes to a close, I feel like I've already grown so much."

    show amelia_motivated_full
    a "But I know this is just the beginning. There's so much more to learn, so many more challenges to face."

    show amelia_happy_full
    a "And you know what? I'm ready for it. Bring on the rest of this university adventure."

    "Thus concludes the chapter of The Call to Adventure. Amelia has taken her first steps into the world of university and the study of the mind, but the true journey of transformation is just beginning."

    return
