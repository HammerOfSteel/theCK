label chapter_10_part_1:
    show amelia_on_train
    with dissolve
    
    "Amelia sits on the train, watching the familiar landscape rush by. Each passing mile brings her closer to home, to the life she left behind."
    
    show amelia_looking_out_train_window
    with dissolve
    
    a "(It's been so long since I've been back. Will everything be the same? Will I be the same?)"
    
    "Her mind wanders to the events of the past year - the challenges, the growth, the losses."
    
    if sarah_alive:
        show amelia_sad_on_train
        with dissolve
        
        a "(Sarah... I wonder how she's doing. I hope she's getting the support she needs.)"
    else:
        show amelia_crying_on_train
        with dissolve
        
        a "(Sarah... I still can't believe she's gone. How am I going to face everyone at home, knowing what happened?)"
    
    show amelia_arriving_in_london
    with dissolve
    
    "As Amelia steps off the train onto the familiar streets of her London neighborhood, a wave of nostalgia washes over her."
    
    show amelia_nostalgic_in_london
    with dissolve
    
    a "(The corner store, the park, the old library... So many memories. It feels like a lifetime ago.)"
    
    show amelia_approaching_home
    with dissolve
    
    "Amelia makes her way to her family home, each step laden with anticipation and a touch of nervousness."
    
    show amelia_greeted_by_mom
    with dissolve
    
    mom "Amelia, welcome home! We've missed you so much!"
    
    show amelia_greeted_by_dad
    with dissolve
    
    dad "Welcome back, kiddo. It's good to see you."
    
    show amelia_emotional_homecoming
    with dissolve
    
    "Amelia drops her bags and rushes into her parents' embrace, suddenly overwhelmed with emotion."
    
    a "I've missed you too. So much."
    
    show amelia_talking_with_parents
    with dissolve
    
    "Over tea in the living room, Amelia's parents gently probe into her life at university."
    
    show mom_asking_about_sarah
    with dissolve
    
    mom "Sweetie, we heard about what happened with Sarah. We're so sorry. How are you coping?"
    
    menu:
        "Open up about the pain":
            $ MH += 1
            show amelia_sad_talking_to_parents
            with dissolve
            
            a "It's... it's been really hard. Sarah was my best friend. To think that she was in so much pain and I couldn't help her..."
            
            if sarah_alive:
                a "I'm just grateful she's getting help now. But the guilt, the what-ifs... they still haunt me."
            else:
                a "I keep thinking about what I could have done differently, how I could have saved her. The guilt is overwhelming."
            
            show dad_comforting_amelia
            with dissolve
            
            dad "Amelia, you can't blame yourself. Mental illness... it's a beast. You did everything you could."
            
            show mom_supporting_amelia
            with dissolve
            
            mom "Your dad's right, honey. You were there for Sarah. That's what matters. Don't carry this weight alone."
            
        "Change the subject":
            $ MH -= 1
            show amelia_uncomfortable_with_parents
            with dissolve
            
            a "It's... it's been tough. But I don't really want to talk about it right now, if that's okay."
            
            show mom_understanding_amelia
            with dissolve
            
            mom "Of course, sweetie. We're here whenever you're ready to talk."
            
            show amelia_grateful_to_parents
            with dissolve
            
            a "Thanks, Mom. I appreciate that."
            
            show dad_curious_about_amelia
            with dissolve
            
            dad "So, tell us about your classes. What's been your favorite so far?"
            
            "Amelia latches onto the change of subject, diving into a description of her coursework."

    jump conversation_with_parents

label conversation_with_parents:
    show amelia_at_dinner_with_parents
    with dissolve
    
    "The conversation continues over dinner, turning to Amelia's studies and future plans."
        
    menu:
        "Discuss academic achievements":
            $ AA += 1
            show amelia_discussing_academics
            with dissolve
            
            a "My classes have been challenging but incredibly fascinating. I feel like I'm really starting to grasp the complexities of the human mind."
            a "I'm considering applying for a research assistant position next semester, to gain some practical experience."
            
            show dad_proud_of_amelia
            with dissolve
            
            dad "That's fantastic, Amelia! Your hard work is really paying off."
            
            show mom_curious_about_amelia
            with dissolve
            
            mom "And what about after graduation? Have you given any thought to what you might want to do?"
            
            show amelia_considering_future
            with dissolve
            
            a "I'm thinking about graduate school, maybe even a PhD. But I also want to get some real-world experience, maybe in a clinical setting."
            
            show mom_supportive_of_amelia
            with dissolve
            
            mom "Whatever you decide, we know you'll excel. You have such a bright future ahead of you."
            
        "Share personal growth":
            $ SD += 1
            show amelia_discussing_personal_growth
            with dissolve
            
            a "Honestly, this year has been as much about personal growth as it has been about academics."
            a "I've learned so much about myself - my strengths, my weaknesses, what I value most in life."
            
            show dad_interested_in_amelia
            with dissolve
            
            dad "That's such an important part of the college experience, Amelia. Finding out who you are and what you stand for."
            
            show amelia_reflective_at_dinner
            with dissolve
            
            a "It hasn't always been easy. I've had to confront parts of myself that I wasn't proud of, make tough decisions."
            a "But I feel like I'm coming out the other side stronger, more self-aware. Like I'm becoming the person I want to be."
            
            show mom_proud_of_amelia
            with dissolve
            
            mom "We're so proud of you, sweetie. Not just for your achievements, but for the amazing young woman you're becoming."
            
        "Express challenges and doubts":
            $ MH += 1
            show amelia_expressing_challenges
            with dissolve
            
            a "To be honest, it's been a tough year. Academically, yes, but also emotionally."
            a "With everything that happened with Sarah, and the pressure of classes, sometimes I've felt like I was barely keeping my head above water."
            
            show mom_concerned_for_amelia
            with dissolve
            
            mom "Oh, honey. I'm so sorry you've been going through such a hard time."
            
            show dad_supportive_of_amelia
            with dissolve
            
            dad "We're here for you, Amelia. Always. Whether you need a listening ear or a shoulder to cry on."
            
            show amelia_grateful_to_parents
            with dissolve
            
            a "I know, and I'm so grateful for that. It's just... it's been a lot to process. There are days when I don't know if I'm strong enough to handle it all."
            
            show mom_reassuring_amelia
            with dissolve
            
            mom "You are strong, Amelia. Stronger than you know. And it's okay to not be okay sometimes. That's part of the human experience."
            
            show amelia_comforted_by_parents
            with dissolve
            
            a "Thanks, Mom. I'm learning that. Learning to ask for help when I need it, to lean on others. It's made all the difference."
            
    show amelia_reflecting_after_dinner
    with dissolve
    
    "After dinner, Amelia retires to her old bedroom, feeling both nostalgic and strangely distant from her former life."
    
    if AA > 10 and SD > 10:
        show amelia_balanced_reflection
        with dissolve
        
        a "(It's good to be back, to share my journey with Mom and Dad. They've always been my biggest supporters.)"
        a "(But I know my growth isn't just about grades and degrees. It's about who I am, the life I want to lead. And that journey is far from over.)"
        
    elif MH > 10:
        show amelia_heavy_reflection
        with dissolve
        
        a "(Being home, it's comforting but also strange. Like I'm trying to fit back into a life that doesn't quite fit me anymore.)"
        a "(The pain of losing Sarah, the struggle of balancing everything... it's changed me. And I'm still trying to understand how.)"
        
    else:
        show amelia_uncertain_reflection
        with dissolve
        
        a "(Talking with Mom and Dad, it's like they're seeing a snapshot of my life, not the whole picture.)"
        a "(There's so much I haven't shared, so much I'm still processing. But maybe that's okay. Maybe this visit is a chance for me to make sense of it all.)"
        
    show amelia_falling_asleep
    with dissolve
    
    "With these thoughts swirling in her mind, Amelia drifts off to sleep, ready to face the memories and realizations that await her in the coming days."
        
    jump chapter_10_part_2

label chapter_10_part_2:
    show amelia_waking_up_in_old_room
    with dissolve
    
    "Amelia wakes up in her old bedroom, momentarily disoriented by the familiar yet distant surroundings."
    
    show amelia_nostalgic_in_room
    with dissolve
    
    a "(Waking up here... it's like stepping back in time. But I'm not the same person I was when I last slept in this bed.)"
    
    "She gets dressed and heads downstairs, where her mother is preparing breakfast."
    
    show amelia_mom_cooking_breakfast
    with dissolve
    
    mom "Good morning, sweetie! I'm making your favorite, blueberry pancakes."
    
    show amelia_smiling_at_breakfast
    with dissolve
    
    a "Thanks, Mom. You didn't have to go to all this trouble."
    
    mom "Nonsense, it's no trouble at all. I want you to feel at home."
    
    show amelia_mom_eating_breakfast
    with dissolve
    
    "As they eat, Amelia's mother tentatively brings up the subject of Ella."
    
    mom "I spoke with Ella's mother the other day. She said Ella's been asking about you, hoping you two could catch up while you're in town."
    
    menu:
        "Eagerly agree to meet Ella":
            $ SI += 1
            show amelia_excited_to_see_ella
            with dissolve
            
            a "Of course! I've been thinking about Ella a lot. It will be so good to see her."
            
            mom "Wonderful! I'll let her know you're excited to meet up."
            
            show amelia_nervous_about_meeting
            with dissolve
            
            a "(But what will I say to her? How much should I share about everything that's happened?)"
        
        "Hesitate to meet Ella":
            $ MH += 1
            show amelia_hesitant_about_ella
            with dissolve
            
            a "Oh... yeah, it would be nice to see Ella. But... I don't know, things have changed so much. I'm not sure I'm ready."
            
            show mom_understanding_amelia
            with dissolve
            
            mom "I understand, honey. It's okay to take your time. If you're not ready, Ella will understand."
            
            a "(But will she? How can I explain to her where I'm at, when I barely understand it myself?)"
            
    scene bg old_hangout_spot
    with dissolve
    
    "Later that day, Amelia finds herself walking to the old park where she and Ella used to spend hours talking and dreaming about the future."
    
    show amelia_nostalgic_at_park
    with dissolve
    
    a "(We had so many plans, so many dreams. Things seemed so simple then. Now... now everything feels complicated.)"
    
    show ella_approaching_amelia
    with dissolve
    
    "Lost in thought, Amelia doesn't notice Ella approaching until she's right beside her."
    
    ella "Amelia! Oh my gosh, it's so good to see you!"
    
    show amelia_surprised_to_see_ella
    with dissolve
    
    a "Ella! Wow, hi! I didn't expect to run into you here."
    
    show amelia_ella_hugging
    with dissolve
    
    "The two friends embrace, the years of separation melting away in the warmth of the hug."
    
    ella "I've missed you so much, Ames. We have so much to catch up on!"
    
    menu:
        "Open up to Ella about everything":
            $ SI += 1
            show amelia_ella_talking_at_park
            with dissolve
            
            a "Oh, El... you have no idea. This year has been... it's been a lot."
            
            "Amelia starts to share everything - her struggles with classes, her growth in understanding mental health, and the painful loss of Sarah."
            
            show ella_comforting_amelia
            with dissolve
            
            ella "Oh, Amelia... I'm so sorry. I had no idea you were going through so much."
            
            a "I wanted to tell you, I just... I didn't know how. It's been hard to process it all myself."
            
            ella "I'm here for you, Ames. Always. No matter what."
            
        "Keep the conversation light":
            $ SI -= 1
            show amelia_ella_casual_talk
            with dissolve
            
            a "Oh, you know, just the usual college stuff. Classes, new friends, lots of studying."
            
            ella "Come on, Ames. I know you. There's more to it than that."
            
            show amelia_uncomfortable_with_ella
            with dissolve
            
            a "Maybe, but... I don't really want to get into it right now. Let's just enjoy being together again, like old times."
            
            show ella_confused_by_amelia
            with dissolve
            
            ella "...Okay, if that's what you want. But you know I'm always here if you need to talk, right?"
            
            a "I know, El. Thanks."
    
    show amelia_ella_reminiscing
    with dissolve
    
    "The two spend the afternoon reminiscing about old times, laughing at shared memories and marveling at how much has changed."
    
    if SI > 10:
        show amelia_ella_close_bond
        with dissolve
        
        a "Talking with you, Ella... it's like no time has passed at all. You know me better than anyone."
        
        ella "And that will never change, Ames. No matter where life takes us, we'll always have each other."
        
    else:
        show amelia_ella_distant
        with dissolve
        
        a "(It's good to see Ella, but... it's not the same. I'm not the same. And I don't know how to bridge that gap.)"
        
        ella "Amelia, I... I feel like there's so much you're not saying. I wish you'd let me in."
        
        a "I'm trying, El. I just... I need time."
        
    show amelia_walking_home_from_park
    with dissolve
        
    "As the sun starts to set, Amelia and Ella part ways, promising to stay in touch."
    
    show amelia_reflective_after_ella
    with dissolve
    
    a "(Seeing Ella... it stirred up so many memories, so many emotions. It's like trying to reconcile who I was with who I am now.)"
    
    a "(I know she wants to understand, to be there for me. But how can I let her in when I'm still trying to make sense of it all myself?)"
    
    "Amelia walks home deep in thought, the weight of her past and the uncertainty of her future heavy on her mind."
        
    jump chapter_10_part_3

label chapter_10_part_3:
    show amelia_waking_up_determined
    with dissolve
    
    "The next morning, Amelia wakes up with a sense of determination."
    
    a "(I can't keep avoiding the tough conversations. If I want to move forward, I need to face my past head-on.)"
    
    show amelia_texting_ella
    with dissolve
    
    "She sends a text to Ella, asking if they can meet up again to talk, really talk."
    
    show ella_texting_back
    with dissolve
    
    "Ella's response is immediate and enthusiastic, suggesting they meet at their favorite café downtown."
    
    scene bg cafe
    with dissolve
    
    show amelia_waiting_nervous
    with dissolve
    
    "A few hours later, Amelia is sitting in the café, nervously stirring her coffee as she waits for Ella to arrive."
    
    show ella_arriving_happy
    with dissolve
    
    ella "Amelia! I'm so glad you reached out. I've been hoping we could talk more."
    
    show amelia_ella_sitting
    with dissolve
    
    a "Me too, Ella. I'm sorry I wasn't more open yesterday. It's just... a lot has happened, and I'm still processing it all."
    
    ella "I understand, Ames. But I'm here for you, no matter what. You can tell me anything."
    
    menu:
        "Share about Sarah's struggle and the support group":
            $ MH += 1
            $ SI += 1
            show amelia_opening_up
            with dissolve
            
            a "The truth is, Ella... I've been through a lot this year. My friend Sarah, she... she attempted suicide. It was awful."
            
            show ella_shocked_concerned
            with dissolve
            
            ella "Oh my god, Amelia. I'm so sorry. That must have been terrifying."
            
            a "It was. But it also opened my eyes to how important mental health support is. I've actually started a support group on campus, to help others who are struggling."
            
            show ella_proud_supportive
            with dissolve
            
            ella "Wow, Ames. That's incredible. I'm so proud of you for turning your pain into something so positive."
            
            a "Thanks, El. It hasn't been easy, but it feels like important work. Like maybe I can make a difference."
            
        "Talk about personal growth and future plans":
            $ SD += 1
            show amelia_reflecting_growth
            with dissolve
            
            a "I feel like I've learned so much about myself this year, Ella. About my strengths, my passions, what I want to do with my life."
            
            show ella_listening_intently
            with dissolve
            
            ella "That's amazing, Amelia. I've always known you were destined for great things."
            
            a "I'm not sure about 'great things', but I do know I want to help people. Maybe as a therapist, or a researcher, or even a professor someday."
            
            show ella_excited_for_amelia
            with dissolve
            
            ella "I can totally see that, Ames. You've always had such a deep understanding of people and a desire to make a difference."
            
            a "Thanks, Ella. It means a lot to have your support. I know I've been distant, but your friendship still means the world to me."
            
    show amelia_ella_close_talking
    with dissolve
            
    "The conversation flows from there, the two friends reconnecting and sharing their hopes and fears for the future."
    
    if MH > 15 and SI > 15:
        show amelia_ella_heartfelt
        with dissolve
        
        a "Talking with you like this, Ella... it reminds me that I'm not alone. That I have people who love and support me, no matter what."
        
        ella "Always, Amelia. You've been my best friend since we were kids. Nothing will ever change that."
        
        a "I know. And I'm sorry I've been so distant. I'm working on letting people in, on being honest about my struggles."
        
        ella "You're doing great, Ames. I'm here for you, every step of the way."
        
    else:
        show amelia_ella_superficial
        with dissolve
        
        a "(It's good to catch up with Ella, but... I still feel like there's so much I'm not saying. So much she doesn't understand.)"
        
        ella "It's been great seeing you, Ames. Let's not let so much time pass before we talk again, okay?"
        
        a "Definitely, Ella. I'll... I'll try to be better about staying in touch."
        
        "(But will I? Can I really share my new life with my old friends?)"
        
    show amelia_walking_thoughtful
    with dissolve
        
    "As Amelia walks home from the café, she reflects on her conversation with Ella and the journey still ahead of her."
    
    a "(Talking with Ella, it's comforting but also confusing. Like trying to bridge two different worlds.)"
    
    a "(I know she wants to understand, but... can she? Can anyone who hasn't been through what I have?)"
    
    show amelia_looking_at_sky
    with dissolve
    
    a "(Maybe that's okay. Maybe I don't need everyone to fully understand. Maybe I just need to understand myself.)"
    
    a "(And part of that is being honest about my journey. With myself, and with the people I care about.)"
    
    if (MH + SI + SD) > 45:
        show amelia_hopeful_smile
        with dissolve
        
        a "(I'm not the same person I was when I left for Plymouth. And that's a good thing. It means I'm growing, changing, becoming who I'm meant to be.)"
        
        a "(And the people who truly love me... they'll grow with me. Even if it's not always easy.)"
        
        $ MH += 1
        $ SI += 1
        $ SD += 1
        
    else:
        show amelia_pensive_unsure
        with dissolve
        
        a "(But am I ready for that? Am I ready to let people see the real me, scars and all?)"
        
        a "(I don't know. But I do know I can't keep hiding. I can't keep pretending to be someone I'm not.)"
        
        a "(It's time to start being honest. With Ella, with my parents, with myself. Even if it's scary.)"
        
        $ MH += 1
        $ SI += 1
        
    show amelia_writing_in_diary
    with dissolve
        
    "That evening, Amelia sits down to write in her diary, a practice she's found helpful in processing her thoughts and emotions."
    
    a "(Today was a step forward. A step towards integrating my past and my present, towards being honest about my journey.)"
    
    a "(It wasn't perfect, and there's still so much to figure out. But it's a start.)"
    
    a "(And that's all I can ask of myself. To keep starting, keep trying, keep growing.)"
    
    a "(One day at a time. One conversation at a time. One moment of truth at a time.)"
    
    show amelia_smiling_content
    with dissolve
    
    "Amelia closes her diary, feeling a sense of peace and purpose. She knows the road ahead won't be easy, but for the first time, she feels ready to face it - all of it."
    
    "Her old life, her new self, and the beautiful, messy journey of bringing them together."
    
    return