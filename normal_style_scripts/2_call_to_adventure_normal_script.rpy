label call_to_adventure:
    stop music fadeout 1.0
    play music paperwork fadein 1.0 volume 0.5
    show black
    with dissolve
    $ renpy.notify(f"AA {AA} - SI {SI} - MH {MH} - SD {SD} - MC {MC} - OK {OK}")
    window hide

    # Scene setup: Amelia's room, morning of departure
    scene amelia_room_full with dissolve

    # Player choice: Spend extra time with family or double-check packing
    menu:
        "Spend extra time with family (+1 SI)":
            $ SI += 1
            scene black with dissolve
            scene amelia_room_full with dissolve
            show amelia_family_full at center
            a "I should spend some more time with my family before I leave. They've always been there for me."

            # Sub-menu for interaction type
            menu:
                "Heartfelt conversation (+1 MH)":
                    $ MH += 1
                    scene black with dissolve
                    scene amelia_room_full with dissolve
                    show amelia at left
                    show mom at center
                    show dad at right
                    a "Mom, Dad, I just want to thank you for everything. Your love and support mean the world to me."
                    mom "Oh, sweetie, we're so proud of you. You're going to do great things."
                    dad "We'll always be here for you, Amelia. No matter what."
                    a "I love you both so much."
                    hide amelia_family_conversation_full
                    scene black with dissolve

                "Practical advice (+1 MC)":
                    $ MC += 1
                    scene black with dissolve
                    scene amelia_room_full with dissolve
                    show amelia at left
                    show mom at center
                    show dad at right
                    a "Do you have any last-minute advice for me before I head off to university?"
                    mom "Just remember to stay focused on your studies, but also make time for yourself."
                    dad "And don't be afraid to ask for help if you need it. That's what professors and advisors are there for."
                    a "Thanks, I'll keep that in mind."
                    hide amelia_family_advice_full
                    scene black with dissolve

        "Double-check packing (+1 AA)":
            $ AA += 1
            scene black with dissolve
            scene amelia_room_full with dissolve
            show amelia at center
            a "I better make sure I have everything I need. I don't want to forget anything important."

            # Sub-menu for packing focus
            menu:
                "Review study materials (+1 AA)":
                    $ AA += 1
                    scene black with dissolve
                    scene amelia_room_full with dissolve
                    show amelia at center
                    a "Let's see... textbooks, check. Laptop, check. Notebooks and pens, check."
                    a "I think I'm all set academically. Bring on the psychology courses!"
                    hide amelia_study_materials_full
                    scene black with dissolve

                "Pack a sentimental item (+1 SD)":
                    $ SD += 1
                    scene black with dissolve
                    scene amelia_room_full with dissolve
                    show amelia at center
                    a "I can't forget to pack this photo of me and Ella. And the bracelet Mom gave me for my birthday."
                    a "These little pieces of home will remind me of the love and support I have, even when I'm far away."
                    hide amelia_sentimental_item_full
                    scene black with dissolve

    # TODO - add some scenes as a segway to next label
    
    jump train_ride_to_plymouth

label train_ride_to_plymouth:
    stop music fadeout 1.0
    play music new_river fadein 1.0 volume 0.5
    scene black
    with dissolve
    
    # Scene setup: Amelia on the train to Plymouth
    scene amelia_train_full with dissolve
    show amelia at center
    a "Well, this is it. The start of my new adventure."

    # Player choice: Engage in conversation or reflect quietly
    menu:
        "Engage in conversation with another student (+1 SI)":
            $ SI += 1
            scene black with dissolve
            scene amelia_train_full with dissolve
            show amelia at left
            show student at right
            a "Hi there! Are you heading to Plymouth University too?"
            student "Yeah, I am! I'm so excited. What are you planning to study?"

            # Sub-menu for conversation focus
            menu:
                "Discuss academic interests (+1 AA)":
                    $ AA += 1
                    scene black with dissolve
                    scene amelia_train_full with dissolve
                    show amelia at left
                    show student at right
                    a "I'm diving into psychology. I've always been fascinated by the human mind."
                    student "That's so cool! I'm more into the sciences myself, but psychology sounds really interesting."
                    a "It is! There's so much to explore. I can't wait to get started."
                    scene black with dissolve

                "Discuss personal backgrounds (+1 SI)":
                    $ SI += 1
                    scene black with dissolve
                    scene amelia_train_full with dissolve
                    show amelia at left
                    show student at right
                    a "Psychology for me. But enough about academics, tell me about yourself! Where are you from?"
                    student "I'm from Brighton originally. It's going to be a big change, moving to a new city."
                    a "I know what you mean. I'm equal parts nervous and excited. But I think it's going to be an amazing experience."
                    scene black with dissolve

        "Reflect quietly (+1 SD)":
            $ SD += 1
            scene black with dissolve
            scene amelia_train_full with dissolve
            show amelia at center
            a "I think I'll take this time to reflect on my own thoughts and feelings."

            # Sub-menu for reflection focus
            menu:
                "Write in journal (+1 MH)":
                    $ MH += 1
                    scene black with dissolve
                    scene amelia_train_full with dissolve
                    show amelia at center
                    a "Writing has always been a great way for me to process my emotions."
                    n "Amelia takes out her journal and begins to write."
                    a "{i}Today marks the start of a new chapter. I'm feeling so many things - excitement, nervousness, hope. But above all, I feel ready. Ready to learn, to grow, to discover who I am and who I want to be.{/i}"
                    scene black with dissolve

                "Observe passing landscapes (+1 SD)":
                    $ SD += 1
                    scene black with dissolve
                    scene amelia_train_full with dissolve
                    show amelia at center
                    a "Sometimes, just observing the world around me helps me gain perspective."
                    n "Amelia gazes out the window, taking in the changing scenery."
                    a "It's beautiful, isn't it? All these different landscapes, blurring together. Kind of like life - a series of moments and experiences, each one shaping us in its own way."
                    scene black with dissolve

label arrival_at_plymouth:
    stop music fadeout 1.0
    play music new_river fadein 1.0 volume 0.5
    scene black
    with dissolve
    
    # Scene setup: Amelia arrives at Plymouth campus
    scene amelia_plymouth_campus_full with dissolve
    show amelia at center
    a "Wow, the campus is even more beautiful than I imagined."

    # Player choice: Explore campus alone or ask for directions
    menu:
        "Explore the campus on her own (+1 SD)":
            $ SD += 1
            scene black with dissolve
            scene amelia_plymouth_campus_full with dissolve
            show amelia at center
            a "I think I'll take some time to explore on my own, get a feel for the place."

            # Sub-menu for exploration focus
            menu:
                "Visit the library (+1 AA)":
                    $ AA += 1
                    scene black with dissolve
                    scene amelia_library_full with dissolve
                    show amelia at center
                    a "The library seems like a good place to start. So many books, so much knowledge!"
                    n "Amelia browses the shelves, marveling at the extensive collection."
                    a "I can already tell I'm going to be spending a lot of time here."
                    scene black with dissolve

                "Visit the psychology department (+1 SD)":
                    $ SD += 1
                    scene black with dissolve
                    scene amelia_psych_department_full with dissolve
                    show amelia at center
                    a "I should familiarize myself with the psychology department."
                    n "Amelia walks through the department, reading the various posters and notices."
                    a "This is where I'll be spending the next few years, delving into the mysteries of the mind. How exciting!"
                    scene black with dissolve

        "Ask for directions (+1 SI)":
            $ SI += 1
            scene black with dissolve
            scene amelia_plymouth_campus_full with dissolve
            show amelia at center
            a "I should probably ask someone for directions, make sure I know where I'm going."

            # Sub-menu for asking directions
            menu:
                "Engage with a friendly student (+1 SI)":
                    $ SI += 1
                    scene black with dissolve
                    scene amelia_plymouth_campus_full with dissolve
                    show amelia at left
                    show student at right
                    a "Excuse me, I'm new here. Could you point me towards the student union?"
                    student "Of course! It's just down that path and to the left. I'm heading that way myself, I can walk with you if you'd like."
                    a "That would be great, thanks! I'm Amelia, by the way."
                    student "Nice to meet you, Amelia. I'm Sam. Welcome to Plymouth!"
                    scene black with dissolve

                "Engage with a helpful staff member (+1 MC)":
                    $ MC += 1
                    scene black with dissolve
                    scene amelia_plymouth_campus_full with dissolve
                    show amelia at left
                    show staff at right
                    a "Hello, I'm a new student. Could you help me find the registrar's office?"
                    staff "Certainly! It's in the main administrative building, just over there. Let me know if you need anything else."
                    a "Thank you so much. I appreciate your help."
                    staff "No problem at all. That's what we're here for. Enjoy your time at Plymouth!"
                    scene black with dissolve

    # TODO - add some scenes as a segway to next label

    jump moving_into_dorm

label moving_into_dorm:
    stop music fadeout 1.0
    play music new_river fadein 1.0 volume 0.5
    scene black
    with dissolve
    
    # Scene setup: Amelia views her new dorm room
    scene amelia_dorm_room_full with dissolve
    show amelia at center
    a "So this is my new home. It's not much, but it's mine."

    # Player choice: Decorate with academic posters or personal photos
    menu:
        "Decorate with academic posters (+1 AA)":
            $ AA += 1
            scene black with dissolve
            scene amelia_dorm_room_full with dissolve
            show amelia at center
            a "I think some academic posters would really inspire me to study hard."

            # Sub-menu for type of posters
            menu:
                "Choose famous psychologists posters (+1 AA)":
                    $ AA += 1
                    scene black with dissolve
                    scene amelia_dorm_room_full with dissolve
                    show amelia at center
                    a "Freud, Jung, Pavlov... these pioneers of psychology will remind me of the great minds that came before."
                    scene black with dissolve

                "Choose inspiring quotes posters (+1 MH)":
                    $ MH += 1
                    scene black with dissolve
                    scene amelia_dorm_room_full with dissolve
                    show amelia at center
                    a "Some motivational quotes would be great to keep me going when times get tough."
                    scene black with dissolve

        "Decorate with personal photos (+1 SI)":
            $ SI += 1
            scene black with dissolve
            scene amelia_dorm_room_full with dissolve
            show amelia at center
            a "Some photos of my family and friends will make this place feel more like home."

            # Sub-menu for type of photos
            menu:
                "Display family photos (+1 SI)":
                    $ SI += 1
                    scene black with dissolve
                    scene amelia_dorm_room_full with dissolve
                    show amelia at center
                    a "I'll put this family photo right by my bed, so they're the first thing I see in the morning."
                    scene black with dissolve

                "Display travel memories (+1 SD)":
                    $ SD += 1
                    scene black with dissolve
                    scene amelia_dorm_room_full with dissolve
                    show amelia at center
                    a "These photos from my travels will remind me of the adventures I've had and the ones yet to come."
                    scene black with dissolve

    # Scene: Meeting the new roommate
    scene amelia_dorm_room_full with dissolve
    show amelia at left
    show roommate at right
    liz "Hey there! You must be Amelia. I'm your new roommate, Liz!"
    a "Hi Liz, it's great to meet you! I'm looking forward to getting to know you."
    liz "Me too! I've heard you're studying psychology?"
    a "Yes, that's right! What about you?"
    liz "Environmental Science for me. I think we'll have lots to chat about!"

    # Special scene if SI > 5 and MH > 5
    if SI > 5 and MH > 5:
        scene black with dissolve
        scene amelia_dorm_room_full with dissolve
        show amelia at left
        show roommate at right
        liz "Can I confess something to you, Amelia? I'm actually really nervous about starting university."
        a "Oh Liz, that's totally understandable. It's a big change for all of us."
        liz "I've been dealing with some personal struggles lately, and I'm worried it'll affect my studies."
        a "I'm here for you, Liz. If you ever need to talk or just want some support, I'm always willing to listen."
        liz "Thank you, Amelia. That means a lot to me. I can already tell we're going to be great friends."
        $ SI += 2
        $ MH += 1
        a "I feel the same way, Liz. We'll get through this together."
        scene black with dissolve

    scene black with dissolve
    jump orientation_week

label orientation_week:
    stop music fadeout 1.0
    play music the_moss fadein 1.0 volume 0.5
    scene black
    with dissolve
    
    # Scene setup: Amelia at the orientation week activities
    scene amelia_orientation_week_full with dissolve
    show amelia at center
    a "Orientation week... so many events to choose from!"

    # Player choice: Attend an academic seminar or a social mixer
    menu:
        "Attend an academic seminar (+1 AA)":
            $ AA += 1
            scene black with dissolve
            scene amelia_orientation_week_full with dissolve
            show amelia at center
            a "This seminar on recent developments in psychology looks fascinating."

            # Sub-menu for seminar activities
            menu:
                "Ask a question (+1 AA)":
                    $ AA += 1
                    scene black with dissolve
                    scene amelia_orientation_week_full with dissolve
                    show amelia at center
                    n "Amelia raises her hand during the Q&A portion of the seminar."
                    a "Professor, could you elaborate on how this new theory might be applied in clinical settings?"
                    n "The professor nods, impressed by Amelia's insightful question."
                    professor "Excellent question! In practice, this theory could be used to..."
                    scene black with dissolve

                "Take detailed notes (+1 SD)":
                    $ SD += 1
                    scene black with dissolve
                    scene amelia_orientation_week_full with dissolve
                    show amelia at center
                    n "Amelia listens attentively, jotting down key points and references."
                    a "{i}This is groundbreaking stuff. I'll need to do some more research on this later.{/i}"
                    n "By the end of the seminar, Amelia's notebook is filled with valuable information and ideas to explore further."
                    scene black with dissolve

        "Attend a social mixer (+1 SI)":
            $ SI += 1
            scene black with dissolve
            scene amelia_orientation_week_full with dissolve
            show amelia at center
            a "A social mixer could be a great way to meet new people and make friends."

            # Sub-menu for mixer activities
            menu:
                "Join a club (+1 SI)":
                    $ SI += 1
                    scene black with dissolve
                    scene amelia_orientation_week_full with dissolve
                    show amelia at center
                    n "Amelia browses the various club booths, chatting with representatives."
                    a "The Psychology Society seems perfect for me! And maybe I'll join the Hiking Club too, for some outdoor adventures."
                    n "Amelia signs up for a few clubs, excited to get involved in campus life."
                    scene black with dissolve

                "Volunteer for an event (+1 MC)":
                    $ MC += 1
                    scene black with dissolve
                    scene amelia_orientation_week_full with dissolve
                    show amelia at center
                    n "Amelia notices a sign-up sheet for orientation week volunteers."
                    a "Helping out with events would be a great way to give back and meet people at the same time."
                    n "Amelia puts her name down for several volunteering slots, ready to make a positive impact."
                    scene black with dissolve

    # Special Scene (if AA > 7 and SI > 7)
    if AA > 7 and SI > 7:
        scene black with dissolve
        scene amelia_orientation_week_full with dissolve
        show professor at center
        a "An invitation to dinner with the psychology faculty? Wow, what an honor!"
        professor "Amelia, we've been very impressed with your participation and insights during orientation week."
        a "Thank you so much, professor. I'm just thrilled to be here and to learn from all of you."
        professor "We see great potential in you. Keep up the excellent work, and don't hesitate to come to us with any questions or ideas."
        $ AA += 2
        $ SI += 1
        a "I will, absolutely. This is an incredible opportunity. I'm so grateful to be part of this department."
        scene black with dissolve

    scene black with dissolve

    # TODO - add some scenes as a segway to next label

    jump first_classes


label first_classes:
    stop music fadeout 1.0
    play music new_river fadein 1.0 volume 0.5
    scene black
    with dissolve
    
    # Scene setup: Amelia's first official classes at the university
    scene amelia_first_classes_full with dissolve
    show amelia at center
    a "My first official classes... I've been waiting for this moment."

    # Player choice: Participate in class discussions
    menu:
        "Participate in class discussions (+1 AA)":
            $ AA += 1
            scene black with dissolve
            scene amelia_first_classes_full with dissolve
            show amelia at center
            a "I want to engage with the material and share my thoughts."

            # Sub-menu for discussion focus
            menu:
                "Offer a unique perspective (+1 AA)":
                    $ AA += 1
                    scene black with dissolve
                    scene amelia_first_classes_full with dissolve
                    show amelia at center
                    n "During a discussion on nature vs. nurture, Amelia raises her hand."
                    a "I think it's not just a question of nature or nurture, but how they interact. Epigenetics has shown that our experiences can actually change gene expression."
                    n "The professor nods, impressed."
                    professor "Excellent point, Amelia. The interplay between genes and environment is a crucial consideration."
                    scene black with dissolve

                "Relate to personal experiences (+1 SD)":
                    $ SD += 1
                    scene black with dissolve
                    scene amelia_first_classes_full with dissolve
                    show amelia at center
                    n "The class discusses the impact of childhood experiences on adult behavior."
                    a "I can relate to this. Growing up, my parents always encouraged me to express my emotions. I think that's why I'm so drawn to psychology - to understand those early influences."
                    n "The professor smiles."
                    professor "Thank you for sharing, Amelia. Personal insights like these can really enrich our understanding of the theories we study."
                    scene black with dissolve

                "Observe and take notes (+1 SD)":
                    $ SD += 1
                    scene black with dissolve
                    scene amelia_first_classes_full with dissolve
                    show amelia at center
                    a "I want to absorb as much as I can and reflect on it later."

                    # Detailed note-taking menu
                    menu:
                        "Focus on professor's lecture (+1 AA)":
                            $ AA += 1
                            scene black with dissolve
                            scene amelia_first_classes_full with dissolve
                            show amelia at center
                            n "Amelia listens intently to the professor's every word, trying to capture the key points."
                            n "She jots down the main theories, researchers, and studies mentioned."
                            a "{i}This is the foundation. I need to make sure I have a solid grasp of these core concepts.{/i}"
                            scene black with dissolve

                        "Focus on classmates' reactions (+1 SD)":
                            $ SD += 1
                            scene black with dissolve
                            scene amelia_first_classes_full with dissolve
                            show amelia at center
                            n "Amelia observes her classmates as they react to the lecture."
                            n "She notes who seems engaged, who looks confused, who has strong emotional responses."
                            a "{i}Everyone brings their own perspective. Understanding their reactions can be just as enlightening as the lecture itself.{/i}"
                            scene black with dissolve

    # Special Scene (if AA > 10)
    if AA > 10:
        scene black with dissolve
        scene amelia_first_classes_full with dissolve
        show professor at center
        n "After class, the professor approaches Amelia."
        professor "Amelia, I must say, your contributions to the class discussion have been outstanding."
        a "Thank you, professor. I'm just so passionate about the subject matter."
        professor "It shows. Your insights are well beyond what I typically see from first-year students."
        a "I've been reading a lot of extra material outside of class. I want to deepen my understanding as much as possible."
        professor "That's excellent. Keep up that curiosity and drive. If you ever want to discuss your ideas further, my door is always open."
        $ AA += 2
        $ MC += 1
        a "I would love that. Thank you so much for the encouragement, professor."
        scene black with dissolve

    scene black with dissolve
