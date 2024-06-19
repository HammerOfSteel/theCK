label special_scenes:

    # Special Scene: Farewell Party
    if SI > 3:
        scene amelia_farewell_party_full with dissolve
        show amelia at left
        show ella at center
        show mom at right
        show dad at far_right
        a "What's all this?"
        ella "Surprise! We couldn't let you leave without a proper farewell party."
        mom "We're so excited for you, Amelia. But we're going to miss you so much."
        dad "We wanted to show you how much we love and support you."
        $ SI += 2
        $ MH += 1
        a "You guys... this is amazing. I'm going to miss you all so much. Thank you for everything."
        scene black with dissolve

    # Special Scene: Meet Professor on Train
    if AA > 3 and SD > 3:
        scene amelia_meet_professor_full with dissolve
        show amelia at left
        show professor at right
        professor "Excuse me, I couldn't help but overhear your conversation earlier. You seem to have a deep passion for psychology."
        a "Oh, yes, I do! I'm actually starting my psychology degree at Plymouth University."
        professor "Wonderful! I'm a professor there, in the psychology department. It's always a delight to meet enthusiastic students."
        a "That's amazing! I'd love to hear more about your research and the program."
        n "The professor and Amelia engage in a thought-provoking discussion about various psychological theories and their applications."
        $ AA += 2
        $ SD += 1
        professor "You have a bright future ahead of you, young lady. I look forward to seeing you in class."
        a "Thank you so much, professor. This has been incredibly insightful."
        scene black with dissolve

    # Special Scene: Hidden Garden
    if SD > 5:
        scene amelia_hidden_garden_full with dissolve
        show amelia at center
        a "Oh wow, what a beautiful garden! I didn't expect to find this here."
        n "Amelia takes a moment to admire the tranquil surroundings, the gentle rustling of leaves, and the soft chirping of birds."
        a "This is perfect. A little oasis of calm amidst the bustling campus."
        $ SD += 2
        $ MH += 1
        a "I'll have to remember this spot. Whenever I need a break or a quiet place to think, I'll come here."
        scene black with dissolve

    # Special Scene: Roommate Confession
    if SI > 5 and MH > 5:
        scene amelia_roommate_confession_full with dissolve
        show amelia at left
        show liz at right
        liz "Can I confess something to you, Amelia? I'm actually really nervous about starting university."
        a "Oh Liz, that's totally understandable. It's a big change for all of us."
        liz "I've been dealing with some personal struggles lately, and I'm worried it'll affect my studies."
        a "I'm here for you, Liz. If you ever need to talk or just want some support, I'm always willing to listen."
        liz "Thank you, Amelia. That means a lot to me. I can already tell we're going to be great friends."
        $ SI += 2
        $ MH += 1
        a "I feel the same way, Liz. We'll get through this together."
        scene black with dissolve

    # Special Scene: Dinner with Faculty
    if AA > 7 and SI > 7:
        scene amelia_dinner_with_faculty_full with dissolve
        show amelia at center
        show professor at right
        a "An invitation to dinner with the psychology faculty? Wow, what an honor!"
        professor "Amelia, we've been very impressed with your participation and insights during orientation week."
        a "Thank you so much, professor. I'm just thrilled to be here and to learn from all of you."
        professor "We see great potential in you. Keep up the excellent work, and don't hesitate to come to us with any questions or ideas."
        $ AA += 2
        $ SI += 1
        a "I will, absolutely. This is an incredible opportunity. I'm so grateful to be part of this department."
        scene black with dissolve

    # Special Scene: Professor's Praise
    if AA > 10:
        scene amelia_professor_praise_full with dissolve
        show amelia at left
        show professor at right
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

    # Special Scene: Peace Garden
    if MH > 10:
        scene amelia_peace_garden_full with dissolve
        show amelia at center
        n "Amelia wanders the campus, seeking solace, and stumbles upon a beautiful garden she hadn't noticed before."
        a "Wow, what a serene spot. The perfect place for a mental reset."
        n "She sits on a bench, surrounded by lush greenery and the gentle sounds of a trickling fountain."
        a "I can feel my worries fading away. There's something about being in nature that just soothes the soul."
        $ MH += 2
        $ SD += 1
        a "I'll have to remember this spot. Whenever I need a moment of peace, I'll come here."
        scene black with dissolve

    # Special Scene: Library Discovery
    if OK > 3 and AA > 12:
        scene amelia_library_full with dissolve
        show amelia at center
        n "While browsing the library shelves, Amelia's eye is caught by an old, leather-bound book."
        a "Huh, 'The Alchemical Path to Self-Transformation'... how peculiar."
        n "She pulls the book from the shelf and starts flipping through it."
        a "Woah... this goes way beyond just turning lead into gold. It's about the transformation of the psyche, the integration of the unconscious..."
        $ OK += 2
        $ AA += 1
        n "Amelia becomes engrossed in the text, realizing that it holds profound implications for her understanding of psychology."
        a "I feel like I'm on the brink of something big here. These ancient teachings... they're not just historical curiosities. They hold wisdom that we can still apply today."
        n "She checks out the book, knowing that this is just the beginning of a deep dive into the mystical dimensions of the mind."
        scene black with dissolve

    return

