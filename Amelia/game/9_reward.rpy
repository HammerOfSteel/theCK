label chapter_9_part_1:
    show university_campus
    with dissolve

    "In the days following the ordeal with Sarah, Amelia feels a mix of exhaustion, grief, and a newfound sense of purpose."

    if sarah_alive:
        "The knowledge that Sarah is getting the help she needs is a comfort, but Amelia knows there is still much work to be done."
    else:
        "The loss of Sarah weighs heavily on Amelia's heart, but she is determined to honor her friend's memory by advocating for mental health awareness and support."

    show amelia_determined_campus
    with dissolve
    
    a "(I can't change what happened, but I can choose how I move forward. I have to use my experiences to make a difference.)"

    show amelia_walking_campus
    with dissolve
    
    "As Amelia walks across campus, she notices the sympathetic looks and hushed whispers from her classmates."

    show amelia_overhearing_gossip
    with dissolve
    
    "Amelia takes a deep breath, trying to ignore the gossip and focus on her own healing."

    menu:
        "Reflect on personal growth":
            $ SD += 1
            show amelia_reflecting_campus
            with dissolve
            
            a "(The challenges I've faced have taught me so much about myself and what I'm capable of. I'm not the same person I was when I started this journey.)"
            a "(I've learned the importance of asking for help, of being there for others, and of never giving up even in the darkest times.)"
            a "(I know I still have a lot of growing to do, but I'm proud of how far I've come.)"

            show amelia_sense_of_purpose
            with dissolve
            
            "As Amelia reflects on her personal growth, she feels a sense of clarity and purpose."

            a "(I need to channel this growth into something meaningful. I need to use my experiences to help others.)"

        "Focus on moving forward":
            $ AA += 1
            show amelia_focusing_campus
            with dissolve
            
            a "(I can't dwell on the past. I need to focus on what I can do now, on how I can apply what I've learned to my studies and my future.)"
            a "(There are so many opportunities to make a difference, to use my knowledge and experiences to help others.)"

            show amelia_determined_walking
            with dissolve
            
            "Amelia walks with renewed determination, her mind already racing with ideas on how to make a positive impact."

        "Avoid processing":
            $ MH -= 1
            show amelia_avoiding_thoughts
            with dissolve
            
            a "(I can't think about what happened. It's too painful, too overwhelming.)"
            a "(I just need to keep busy, to throw myself into my work and not let myself feel too much.)"

            show amelia_walking_quickly
            with dissolve
            
            "Amelia quickens her pace, as if trying to outrun her own thoughts and emotions."

    show amelia_sees_professor
    with dissolve
    
    "Lost in thought, Amelia almost bumps into Professor Hawthorne."

    show professor_hawthorne_concerned
    with dissolve
    
    h "Amelia! I'm so sorry, I wasn't watching where I was going. Are you alright?"

    show amelia_surprised
    with dissolve
    
    a "Professor Hawthorne! No, no, it's my fault. I was a bit distracted."

    h "Understandable, given everything you've been through recently. How are you holding up?"

    menu:
        "Open up to Professor Hawthorne":
            $ SI += 1
            $ MH += 1
            show amelia_opening_up
            with dissolve
            
            a "To be honest, Professor, it's been really tough. I'm still processing everything that happened with Sarah."
            a "I know I did everything I could to help her, but part of me still feels like I failed her somehow."

            show professor_hawthorne_listening
            with dissolve
            
            h "Amelia, you mustn't blame yourself. What Sarah went through, what she chose to do... that's not on you."
            h "You were there for her when she needed you most. You may well have saved her life. That's not a failure, that's a testament to your strength and compassion."

            show amelia_comforted
            with dissolve
            
            a "Thank you, Professor. I needed to hear that. It's just... it's a lot to process."

            show professor_hawthorne_supportive
            with dissolve
            
            h "Of course it is. And it's okay to not be okay. Don't feel like you have to rush your healing process."
            h "If you ever need to talk, my door is always open. You don't have to go through this alone."

            show amelia_grateful_smile
            with dissolve
            
            a "I appreciate that, Professor. Truly. It means a lot to know I have your support."

        "Keep the conversation brief":
            $ SI -= 1
            show amelia_keeping_distance
            with dissolve
            
            a "I'm managing, Professor. It's been a challenging time, but I'm trying to focus on moving forward."
            a "I don't want to dwell on what happened. I just want to keep busy and not let it derail my studies."

            show professor_hawthorne_concerned
            with dissolve
            
            h "I understand the impulse to throw yourself into your work, Amelia. But it's important to give yourself time and space to process your emotions too."
            h "Bottling things up, trying to push through on your own... it's a recipe for burnout. Trust me, I've been there."

            show amelia_resistant
            with dissolve
            
            a "I appreciate your concern, Professor, but I'll be fine. I just need to keep moving."

            show professor_hawthorne_respecting_boundaries
            with dissolve
            
            h "I respect that, Amelia. Just remember, you don't have to deal with this alone. If you ever do want to talk, I'm here."
            h "And not just as your professor, but as someone who cares about your well-being."

            show amelia_quick_nod
            with dissolve
            
            a "Thank you, Professor. I'll keep that in mind."

    show professor_hawthorne_remembering
    with dissolve
    
    h "Actually, Amelia, I'm glad I ran into you. There's something I wanted to discuss with you."

    show amelia_curious
    with dissolve
    
    a "Oh? What is it, Professor?"

    h "Well, in light of recent events, the psychology department has decided to host a series of workshops and seminars on mental health awareness and support."
    h "We were hoping you might be willing to speak at one of the events, to share your experiences and insights."

    show amelia_surprised
    with dissolve
    
    a "Me? You want me to speak?"

    show professor_hawthorne_encouraging
    with dissolve
    
    h "I think you have a powerful story to share, Amelia. One that could make a real difference for students who are struggling."
    h "But I also understand if it's too much too soon. There's absolutely no pressure."

    menu:
        "Agree to speak":
            $ MC += 1
            $ MH += 1
            show amelia_determined
            with dissolve
            
            a "No, I... I think I want to do this. If my experiences can help even one person, it's worth it."
            a "I'm tired of the stigma around mental health, of the silence and the shame. It's time we start having these conversations openly."

            show professor_hawthorne_proud
            with dissolve
            
            h "I'm proud of you, Amelia. This is a brave thing you're doing. I know it's not easy."
            h "The department will support you in any way we can. If you need help preparing your talk, or if you just need a listening ear, we're here for you."

            show amelia_grateful
            with dissolve
            
            a "Thank you, Professor. That means more than you know."

        "Decline the offer":
            $ MC -= 1
            show amelia_hesitant
            with dissolve
            
            a "I... I don't know, Professor. It's a lot to ask. I'm not sure I'm ready to share my story so publicly."
            a "I'm still trying to make sense of it all myself. I don't know if I have any wisdom to offer."

            show professor_hawthorne_understanding
            with dissolve
            
            h "I completely understand, Amelia. It was not my intention to pressure you."
            h "Everyone processes trauma differently and on their own timeline. There's no right or wrong way to heal."

            show amelia_relieved
            with dissolve
            
            a "Thank you for understanding, Professor. Maybe... maybe one day I'll be ready to share my story. But right now, I think I need to focus on my own healing journey."

            show professor_hawthorne_supportive
            with dissolve
            
            h "Of course, Amelia. You need to do what's right for you. Just know that the offer stands, now or in the future. Whenever you're ready, if you're ever ready, we'll be here to support you."

    show professor_hawthorne_encouraging
    with dissolve
    
    h "In the meantime, Amelia, don't hesitate to reach out if you need anything. My door is always open."
    h "And remember, the university has resources available - counseling services, support groups. You don't have to navigate this alone."

    show amelia_grateful
    with dissolve
    
    a "I appreciate that, Professor. Truly. It's good to know I have a support network here."

    show professor_hawthorne_smiling
    with dissolve
    
    h "Always, Amelia. You're a valued member of our community. We're here for you."

    show amelia_determined
    with dissolve
    
    a "Thank you, Professor. I should get going now, but... thank you. For everything."

    show professor_hawthorne_nodding
    with dissolve
    
    h "You're more than welcome, Amelia. Take care of yourself."

    hide professor_hawthorne_nodding
    with dissolve
    
    "With a grateful nod, Amelia continues on her way, feeling a bit lighter than before."

    if (AA + SI + MH) > 5:
        show amelia_hopeful
        with dissolve
        
        a "(Professor Hawthorne is right. I don't have to do this alone. I have people who care about me, who want to support me.)"
        a "(Maybe... maybe it's time I start leaning on that support a bit more.)"
        $ MH += 1

    else:
        show amelia_pensive
        with dissolve
        
        a "(I know Professor Hawthorne means well, but I don't know if I'm ready to open up like that.)"
        a "(I need to process this in my own way, on my own time.)"

    jump chapter_9_part_2

label chapter_9_part_2:
    show amelia_in_dorm_room
    with dissolve
    
    "A few days later, Amelia is back in her dorm room, trying to catch up on the coursework she missed during the tumultuous events with Sarah."

    show amelia_studying_textbooks
    with dissolve
    
    a "(I need to focus. I can't let my grades slip now, not after everything I've worked for.)"

    "Just as she's about to delve into her psychology textbook, there's a knock on the door."

    show amelia_surprised
    with dissolve
    
    a "Come in!"

    show lucas_entering_room
    with dissolve
    
    l "Hey, Amelia. I hope I'm not interrupting."

    show amelia_smiling
    with dissolve
    
    a "Lucas, no, of course not. It's good to see you."

    show lucas_concerned
    with dissolve
    
    l "I just wanted to check in, see how you're doing. I know it's been... a lot."

    menu:
        "Open up to Lucas":
            $ SI += 1
            $ MH += 1
            show amelia_opening_up
            with dissolve
            
            a "It has been a lot. Honestly, I'm still processing it all."
            a "I keep thinking about Sarah, about what I could have done differently..."

            show lucas_supportive
            with dissolve
            
            l "Amelia, you can't blame yourself. You did everything you could. You were there for Sarah when she needed you most."

            show amelia_teary
            with dissolve
            
            a "I know, but... it's hard not to wonder, you know? If I had seen the signs earlier, if I had been a better friend..."

            show lucas_comforting
            with dissolve
            
            l "You are an amazing friend, Amelia. To Sarah, to all of us. Don't doubt that."

            show amelia_grateful
            with dissolve
            
            a "Thanks, Lucas. I needed to hear that."

        "Put on a brave face":
            $ MH -= 1
            show amelia_brave_face
            with dissolve
            
            a "I'm doing okay, Lucas. Just trying to stay focused on my studies, you know?"

            show lucas_worried
            with dissolve
            
            l "Amelia, it's okay to not be okay. What you went through... it's not something you just bounce back from."

            show amelia_dismissive
            with dissolve
            
            a "I know, but... I can't afford to fall behind. I need to keep moving forward."

            show lucas_unconvinced
            with dissolve
            
            l "I understand that impulse, but... don't bottle it up, Amelia. It's okay to lean on your friends, to ask for help."

            show amelia_hesitant
            with dissolve
            
            a "I... I'll try to remember that. Thanks, Lucas."

    show lucas_remembering
    with dissolve
    
    l "Actually, Amelia, I didn't just come to check in. I also wanted to ask you something."

    show amelia_curious
    with dissolve
    
    a "Oh? What is it?"

    show lucas_excited
    with dissolve
    
    l "Well, you know how I've been getting more involved with the student mental health advocacy group on campus?"

    show amelia_nodding
    with dissolve
    
    a "Yeah, you've mentioned that. It sounds like they're doing great work."

    show lucas_passionate
    with dissolve
    
    l "They are. And, well... we're organizing a big awareness event next month. Workshops, guest speakers, resources for students who are struggling..."
    l "And I was hoping... maybe you'd be willing to speak? Share your story, your experience with Sarah?"

    show amelia_surprised
    with dissolve

    a "Me? You want me to speak at your event?"

    show lucas_encouraging
    with dissolve
    
    l "I think your voice could make a real difference, Amelia. You've seen firsthand how important this issue is, how much work there is still to do."
    l "But I totally understand if it's too much. There's no pressure, I just wanted to ask."

    menu:
        "Agree to speak at the event":
            $ SI += 1
            $ MC += 1
            show amelia_determined
            with dissolve
            
            a "You know what? I'll do it. If my story can help even one person, it's worth it."

            show lucas_excited
            with dissolve
            
            l "Really? Amelia, that's amazing! This means so much, truly."

            show amelia_smiling
            with dissolve
            
            a "I'm nervous, but... I think this is something I need to do. For Sarah, for myself, for everyone who's struggling."

            show lucas_proud
            with dissolve
            
            l "You're incredible, Amelia. The event is in a month, so you have time to prepare. And I'm here to help in any way I can."

            show amelia_grateful
            with dissolve
            
            a "Thanks, Lucas. I know I can always count on you."

        "Decline the offer":
            $ MC -= 1
            show amelia_unsure
            with dissolve
            
            a "I... I don't know, Lucas. It's a lot to ask. I'm not sure I'm ready to share my story like that."

            show lucas_understanding
            with dissolve
            
            l "Hey, that's totally okay, Amelia. I understand. It was a big ask, and you need to do what's right for you."

            show amelia_apologetic
            with dissolve
            
            a "I'm sorry, Lucas. It's not that I don't think the event is important, because it is. I just..."

            show lucas_supportive
            with dissolve
            
            l "You don't need to explain, Amelia. Your well-being comes first, always. If you're not ready, you're not ready."

            show amelia_grateful
            with dissolve
            
            a "Thanks for understanding, Lucas. Maybe... maybe one day I'll be ready to share my story. But not yet."

            show lucas_smiling
            with dissolve
            
            l "And that's perfectly valid, Amelia. No one should pressure you into something you're not comfortable with."

    show amelia_thoughtful
    with dissolve
    
    a "You know, Lucas, this conversation has actually given me an idea."

    show lucas_curious
    with dissolve
    
    l "Oh yeah? What's that?"

    show amelia_determined
    with dissolve
    
    a "I think... I think I want to start a support group. For students who have been affected by mental illness, either their own or a loved one's."
    a "A safe space where people can share their experiences, support each other, maybe even advocate for change on campus."

    show lucas_impressed
    with dissolve
    
    l "Amelia, that's a fantastic idea! I think that could really make a difference for a lot of people."

    show amelia_excited
    with dissolve
    
    a "You think so? I know it's a big undertaking, but... I feel like it's something I need to do. Something I want to do."

    show lucas_supporting
    with dissolve
    
    l "Absolutely. And you know what? I'll help you. We can work on this together."

    show amelia_grateful
    with dissolve
    
    a "Really? Lucas, that would be amazing. Thank you."

    show lucas_smiling
    with dissolve
    
    l "Of course, Amelia. This is important work. I'm proud to be a part of it, and proud of you for taking the lead."

    show amelia_hopeful
    with dissolve
    
    a "It won't be easy, but... I think it will be worth it. If we can create a space where people feel heard, understood, supported... that could change lives."

    show lucas_agreeing
    with dissolve
    
    l "It will change lives, Amelia. I have no doubt about that."

    show amelia_determined
    with dissolve
    
    a "Then let's do this. Let's make it happen."

    "With a shared sense of purpose and determination, Amelia and Lucas begin to plan out their vision for the support group."

    a "(This is for you, Sarah. This is how I'll honor your memory, by making sure no one else feels as alone as you did.)"

    if (AA + SI + MH) > 10:
        show amelia_hopeful
        with dissolve
        
        a "(And maybe... maybe in helping others, I'll find some healing for myself too.)"
        a "(I'm ready to turn this pain into something positive, something powerful.)"
        $ MH += 1
        $ MC += 1
    else:
        show amelia_pensive
        with dissolve
        
        a "(I hope I'm strong enough for this. I hope I can make a real difference.)"
        a "(I have to try. I owe it to Sarah, and to myself.)"

    jump chapter_9_part_3

label chapter_9_part_3:
    show amelia_in_meeting_room
    with dissolve
    
    "A few weeks later, Amelia and Lucas are in a meeting room, preparing for the first session of their new support group."

    show amelia_nervous
    with dissolve
    
    a "I'm so nervous, Lucas. What if no one shows up? What if I say the wrong thing?"

    show lucas_reassuring
    with dissolve
    
    l "Amelia, breathe. It's going to be okay. We've prepared for this, and you're going to be great."

    show amelia_taking_deep_breath
    with dissolve
    
    a "Okay, okay. You're right. I can do this."

    "Just then, the door opens and a handful of students start to trickle in."

    show students_entering_room
    with dissolve
    
    "Some look nervous, others look relieved. All of them look like they're carrying a heavy weight."

    show amelia_welcoming_students
    with dissolve
    
    a "Welcome, everyone. Please, take a seat wherever you feel comfortable."

    "As the students settle in, Amelia and Lucas exchange a glance."

    show amelia_and_lucas_glance
    with dissolve
    
    a "(We're really doing this. We're really making this happen.)"

    show amelia_starting_meeting
    with dissolve
    
    a "Thank you all for coming. I know how much courage it takes to show up to something like this."
    a "This group is a safe space. A place where we can share our experiences, support each other, and know that we're not alone."

    "Amelia takes a deep breath, steadying herself."

    show amelia_sharing_story
    with dissolve
    
    a "I want to start by sharing my own story. A few weeks ago, my best friend Sarah attempted to take her own life."
    a "It was... it was the scariest moment of my life. I felt so helpless, so afraid of losing her."
    a "Sarah is getting help now, but the experience made me realize how important it is to talk about mental health. To break the stigma and the silence."

    show students_listening
    with dissolve
    
    "The room is quiet, everyone listening intently to Amelia's words."

    show amelia_opening_discussion
    with dissolve
    
    a "I don't share this for sympathy, but to let you know that I understand. I understand how hard it is to see someone you love struggle."
    a "And if you're here because of your own struggles, I want you to know that you're not weak. You're not broken. You're incredibly strong, and your life has value."

    show students_emotional
    with dissolve
    
    "A few students nod, some wipe away tears."

    show lucas_supporting
    with dissolve
    
    l "Thank you for sharing, Amelia. That took a lot of courage."
    l "We want this to be a participatory space. You can share as much or as little as you feel comfortable with, and we're here to listen without judgment."

    show students_sharing
    with dissolve
    
    "Slowly, tentatively, students start to share their own stories."

    "One talks about their struggle with anxiety, how it feels like a constant weight on their chest."

    "Another shares about watching their parent battle depression, the helplessness they felt."

    "As the stories unfold, a sense of community starts to build. A sense of understanding and shared experience."

    show amelia_listening
    with dissolve
    
    a "(This is it. This is why we're doing this. To let people know they're not alone.)"

    show lucas_facilitating
    with dissolve
    
    l "Thank you all for your courage and vulnerability. This is a powerful start to what we hope will be a supportive and transformative group."

    show amelia_determined
    with dissolve
    
    a "We'll be meeting here every week, same time. And in between sessions, remember that you have people who care about you. You have resources and support."
    a "We're in this together. You are not alone."

    show students_applauding
    with dissolve
    
    "As the meeting wraps up, there's a palpable sense of relief and gratitude in the room."

    show students_thanking_amelia_and_lucas
    with dissolve
    
    "Students come up to Amelia and Lucas, thanking them for starting the group, for giving them a space to be heard."

    show amelia_and_lucas_proud
    with dissolve
    
    a "We did it, Lucas. We actually did it."

    l "You did it, Amelia. This was all you. I'm just here to support."

    show amelia_grateful
    with dissolve
    
    a "I couldn't have done it without you, Lucas. Thank you."

    if (AA + SI + MH) > 15:
        show amelia_hopeful
        with dissolve
        
        a "I feel... I feel like this is the start of something really important. Like we're really making a difference."
        a "For the first time since Sarah's attempt, I feel... hopeful. Like there's a purpose to all this pain."
        $ MH += 2
        $ SI += 1
    else:
        show amelia_unsure
        with dissolve
        
        a "I hope we're doing the right thing. I hope this group can really help people."
        a "It's a lot of responsibility, but... I know it's important work. I know we have to try."
        $ MH += 1

    jump chapter_9_part_4

label chapter_9_part_4:
    show amelia_in_dorm_room_night
    with dissolve
    
    "Later that night, Amelia is back in her dorm room, reflecting on the day's events."

    show amelia_journaling
    with dissolve
    
    a "(The support group, it felt... it felt right. Like I was exactly where I needed to be.)"
    a "(Hearing those stories, seeing the pain but also the strength in everyone... it was powerful.)"

    "A notification lights up Amelia's phone. It's an email from Professor Hawthorne."

    show amelia_reading_email
    with dissolve
    
    a "(An update on the department's mental health initiative... and a personal note?)"

    "Amelia reads the email, her eyes widening."

    show email_text
    with dissolve
    
    "Amelia,

    I heard about the support group you and Lucas started. What an incredible initiative. I'm so proud of you for taking this on.

    Your compassion and dedication to this issue is truly inspiring. You are making a real difference in the lives of your fellow students.

    I know this work is not easy, but please know that you have the full support of myself and the department. If there are any resources or assistance you need, don't hesitate to ask.

    Keep up the amazing work, Amelia. You are a shining example of what it means to be a leader and an advocate.

    Sincerely,
    Professor Hawthorne"

    show amelia_touched
    with dissolve
    
    a "(Wow... I didn't expect that. Professor Hawthorne, he... he's proud of me.)"
    a "(It means a lot, knowing I have his support. Knowing that the department is behind this initiative.)"

    show amelia_determined
    with dissolve
    
    a "(I have to keep going. I have to keep pushing forward. For Sarah, for everyone in that support group, for myself.)"
    a "(This is just the beginning. There's so much more work to be done.)"

    if (AA + SI + MH) > 20:
        show amelia_confident
        with dissolve
        
        a "(But I feel ready for it. I feel stronger than I ever have before.)"
        a "(I've learned so much, grown so much. I know I can handle whatever comes next.)"
        $ MH += 2
        $ AA += 1
    else:
        show amelia_hopeful
        with dissolve
        
        a "(It won't be easy, but... I'm not alone. I have support, I have people who believe in me.)"
        a "(I have to believe in myself too. I have to trust that I'm on the right path.)"
        $ MH += 1

    show amelia_looking_out_window
    with dissolve
    
    a "(The journey ahead, it's still long. There's still so much I don't know, so much I have to learn.)"
    a "(But for the first time, I feel... I feel excited for it. I feel ready to embrace it.)"

    show amelia_smiling
    with dissolve
    
    a "(Bring it on, future. I'm ready for you.)"

    "With a sense of peace and determination, Amelia turns off her light and goes to sleep, ready for whatever tomorrow will bring."

    jump chapter_10