# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Amelia")
define e = Character("Ella")
define j = Character("James")
define p = Character("Parents")
define n = Character("Narrator")
define s = Character("Student")
define prof_Williams = Character("Pr. Williams")
define music.chapter_0_2 = "chapter_0_2.mp3"
define music.chapter_1 = "chapter_1.mp3"
define music.chapter_2 = "chapter_2.mp3"


# The game starts here.

label start:
    play music chapter_0_2 fadein 1.0 volume 0.1
    scene chapter_0
    with dissolve

    pause 4.0

    scene screen_m3
    with dissolve
    n "Amelias curiosity about the mind began in a room of dreams and playful experiments."

    scene screen_m2
    with dissolve
    n "High school was a theater of emotions and social hierarchies; a ripe field for observation"

    scene screen_m1
    with dissolve
    n "University, a beacon of hope, promising a sanctuary where curiosity intertwines with opportunit"

    scene screen_0
    with dissolve
    n "With every passing moment, the future lingered, veiled in an envelope yet to arrive."


    stop music fadeout 1.0
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene chapter_1
    with dissolve

    pause 4.0

    scene screen_1
    with dissolve
    play music chapter_1 fadein 1.0 volume 0.1
    
    a "I got in! I actually got in!"
    a "Holy moly, this is the best ever!"


    show screen_2
    with dissolve
    a "Whooohooo!"
    a "Plymouth, here I come!"




#### Screen 3: Moment of Reflection
#- **Description**: Amelia's thoughtful pause.
#- **Dialogue**: "But... who do I tell first?"
#- **Choice**: "Tell Ella first" | "Tell Parents first."#

    show screen_3
    with dissolve

    a "But... who do I tell first?"

    menu:
        "Tell Ella first":

            #### Screen 4: Sharing with Ella (Choice: Ella)
            #- **Setting**: Park bench outside.
            #- **Description**: Amelia sitting with Ella, showing her the letter.
            #- **Dialogue**: "Ella, look! I'm going to Plymouth!"#

            show screen_4
            with dissolve
            a "Ella, look! I'm going to Plymouth!"

            #### Screen 5: Ella's Reaction
            #- **Description**: Ella's joyful expression.
            #- **Dialogue**: "That's amazing, Millie! I knew you could do it!"#

            show screen_5
            with dissolve
            e "Whaaaa... That is amazing!"
            e "That's amazing, Millie! I knew you could do it!"

            #### Screen 6: Emotional Farewell
            #- **Description**: Amelia and Ella sharing a tight hug.
            #- **Dialogue**: "It won't be the same without you here."#

            show screen_6
            with dissolve
            e "It won't be the same without you here"
            a "I'll write every day!"

            #### Screen 7: Thoughts on Change
            #- **Description**: Amelia's reflective expression.
            #- **Dialogue**: "I'll miss you too. But it's a new start, a new journey."#

            show screen_7
            with dissolve
            a "I'll miss you too. But it's a new start, a new journey"


            #### Screen 8: Parents' Joy (Choice: Parents)
            #- **Setting**: Amelia's living room.
            #- **Description**: Amelia displaying the letter to her parents.
            #- **Dialogue**: "Mum, Dad, Plymouth said YES!"#

            show screen_8
            with dissolve
            a "Mum, Dad, Plymouth said YES!"

            #### Screen 9: Parents' Pride
            #- **Description**: Parents beam with pride.
            #- **Dialogue**: "We always knew you'd make it, darling."#

            show screen_9
            with dissolve
            p "We always knew you'd make it, darling"

            #### Screen 10: Family Embrace
            #- **Description**: Amelia hugging both parents tightly.
            #- **Dialogue**: "Thank you for always believing in me."#

            show screen_10
            with dissolve
            a "Thank you for always believing in me"

            #### Screen 11: Imagined Adventures
            #- **Setting**: Amelia's bedroom.
            #- **Description**: Amelia laying down, deep in daydreams.
            #- **Dialogue**: "University life... I wonder what it'll be like."#

            show screen_11
            with dissolve
            a "University life... I wonder what it'll be like"


            #### Screen 12: Texted Plans
            #- **Description**: Amelia's phone vibrates with a new message.
            #- **Text Notification**: Ella: "Let's meet up before you leave?"#

            show screen_12
            with dissolve
            e "Let's meet up before you leave?"


        "Tell Parents first":
            #### Screen 8: Parents' Joy (Choice: Parents)
            #- **Setting**: Amelia's living room.
            #- **Description**: Amelia displaying the letter to her parents.
            #- **Dialogue**: "Mum, Dad, Plymouth said YES!"#

            show screen_8
            with dissolve
            a "Mum, Dad, Plymouth said YES!"

            #### Screen 9: Parents' Pride
            #- **Description**: Parents beam with pride.
            #- **Dialogue**: "We always knew you'd make it, darling."#

            show screen_9
            with dissolve
            p "We always knew you'd make it, darling"

            #### Screen 10: Family Embrace
            #- **Description**: Amelia hugging both parents tightly.
            #- **Dialogue**: "Thank you for always believing in me."#

            show screen_10
            with dissolve
            a "Thank you for always believing in me"

            #### Screen 11: Imagined Adventures
            #- **Setting**: Amelia's bedroom.
            #- **Description**: Amelia laying down, deep in daydreams.
            #- **Dialogue**: "University life... I wonder what it'll be like."#

            show screen_11
            with dissolve
            a "University life... I wonder what it'll be like"


            #### Screen 4: Sharing with Ella (Choice: Ella)
            #- **Setting**: Park bench outside.
            #- **Description**: Amelia sitting with Ella, showing her the letter.
            #- **Dialogue**: "Ella, look! I'm going to Plymouth!"#

            show screen_4
            with dissolve
            a "Ella, look! I'm going to Plymouth!"

            #### Screen 5: Ella's Reaction
            #- **Description**: Ella's joyful expression.
            #- **Dialogue**: "That's amazing, Millie! I knew you could do it!"#

            show screen_5
            with dissolve
            e "Whaaaa... That is amazing!"
            e "That's amazing, Millie! I knew you could do it!"

            #### Screen 6: Emotional Farewell
            #- **Description**: Amelia and Ella sharing a tight hug.
            #- **Dialogue**: "It won't be the same without you here."#

            show screen_6
            with dissolve
            e "It won't be the same without you here"
            a "I'll write every day!"

            #### Screen 7: Thoughts on Change
            #- **Description**: Amelia's reflective expression.
            #- **Dialogue**: "I'll miss you too. But it's a new start, a new journey."#

            show screen_7
            with dissolve
            a "I'll miss you too. But it's a new start, a new journey"


    #### Screen 13: Cafe Memories
    #- **Setting**: Local café.
    #- **Description**: Amelia and Ella sitting together, chatting.
    #- **Dialogue**: "Promise you'll write to me?"#

    show screen_13
    with dissolve
    e "Promise you'll write to me?"


    #### Screen 14: Promised Correspondence
    #- **Description**: Amelia, with a warm smile.
    #- **Dialogue**: "Every week. Promise."#

    show screen_14
    with dissolve
    a "Every week. Promise"


    #### Screen 15: Packing Up
    #- **Setting**: Amelia's bedroom.
    #- **Description**: Amelia packing her belongings, preparing for Plymouth.
    #- **Narrative**: "The days seemed to pass quickly."#

    show screen_15
    with dissolve
    n "The days seemed to pass quickly"


    #### Screen 16: Keepsakes
    #- **Description**: Amelia holds a framed picture of her family and Ella.
    #- **Dialogue**: "I'll carry a piece of home with me."#

    show screen_16
    with dissolve
    a "I'll carry a piece of home with me"

    #### Screen 17: Departure Day
    #- **Setting**: Train station.
    #- **Description**: Amelia, suitcase in tow, waiting.
    #- **Narrative**: "The day of departure."#


    show screen_17
    with dissolve
    n "The day of departure"

    #### Screen 18: Parents' Blessings
    #- **Description**: Amelia's parents waving goodbye.
    #- **Dialogue**: "Take care, Amelia. Call us when you reach."#

    show screen_18
    with dissolve
    p "Take care, Amelia. Call us when you reach."

    #### Screen 19: Journey Starts
    #- **Description**: Amelia boarding the train.
    #- **Dialogue**: "A new chapter awaits."#


    show screen_19
    with dissolve
    n "A new chapter awaits"

    #### Screen 20: Moving Landscapes
    #- **Setting**: Inside the moving train.
    #- **Description**: Amelia gazes out, watching the landscape change.
    #- **Narrative**: "From the familiar streets of London to the unknown paths of Plymouth."#

    show screen_20
    with dissolve
    n "From the familiar streets of London to the unknown paths of Plymouth"

    #### Screen 21: Diary Entries
    #- **Description**: Amelia writing in her diary.
    #- **Narrative**: "Thoughts, dreams, and a tinge of nervousness."#

    show screen_21
    with dissolve
    n "Thoughts, dreams, and a tinge of nervousness"

    #### Screen 22: Ella's Concern
    #- **Description**: Amelia's phone vibrates with another message.
    #- **Text Notification**: Ella: "Reached safely?"#

    show screen_22
    with dissolve
    e "Reached safely?"

    #### Screen 23: Quick Response
    #- **Description**: Amelia swiftly typing a reply.
    #- **Text**: "On my way. I'll call you when I'm there."#

    show screen_23
    with dissolve
    a "On my way. I'll call you when I'm there"

    #### Screen 24: Plymouth Arrival
    #- **Setting**: Plymouth train station.
    #- **Description**: Amelia steps out, observing her new surroundings.
    #- **Dialogue**: "This is it."#

    show screen_24
    with dissolve
    a "This is it"

    #### Screen 25: University Entrance
    #- **Setting**: Plymouth University entrance.
    #- **Description**: Amelia, with building excitement, approaches the university.
    #- **Narrative**: "The beginning of her university journey."#

    show screen_25
    with dissolve
    n "The beginning of her university journey"

    #### Screen 26: First Interactions
    #- **Description**: Amelia introduces herself to fellow students.
    #- **Dialogue**: "Hi, I'm Amelia. First year psychology."#

    show screen_26
    with dissolve
    a "Hi, I'm Amelia. First year psychology"

    #### Screen 27: New Dorm
    #- **Setting**: University hostel room.
    #- **Description**: Amelia begins to set up her new space.
    #- **Narrative**: "Home away from home."#

    show screen_27
    with dissolve
    n "Home away from home"

    

    # Chapter 2
    ## New Beginnings#
    stop music fadeout 1.0

    #### Screen 1: Introduction to University Life
    #- **Setting**: University's main hall.
    #- **Description**: A grand hall bustling with students and banners of various societies and clubs.
    #- **Narrative**: "The heart of Plymouth University."#
    scene chapter_2
    with dissolve
    play music chapter_2 fadein 1.0 volume 0.1

    pause 4.0

    show chapter_2_screen_1
    with dissolve
    n "The heart of Plymouth University"


    #### Screen 2: Guide Tours
    #- **Description**: Student guides offering tours.
    #- **Dialogue**: "Hi there! First year? Want a tour of the campus?"#

    show chapter_2_screen_2
    with dissolve
    s "Hi there! First year? Want a tour of the campus?"

    #### Screen 3: Decision Time
    #- **Description**: Amelia contemplating the offer.
    #- **Choice**: "Accept the tour" | "Decline and explore on your own."#

    show chapter_2_screen_3
    with dissolve
    menu:
        "Sure, I'd love one!":

            #### Screen 4: Tour Begins (Choice: Accept the tour)
            #- **Setting**: Starting at the main hall.
            #- **Description**: A student guide leading a group, including Amelia.
            #- **Narrative**: "A whirlwind tour of the sprawling campus begins."#

            show chapter_2_screen_4
            with dissolve
            n "A whirlwind tour of the sprawling campus begins?"

            #### Screen 5: History Lesson
            #- **Description**: Guide explaining the university's history.
            #- **Dialogue**: "Plymouth Uni has been standing strong since 1862!"#

            show chapter_2_screen_5
            with dissolve
            s "Plymouth Uni has been standing strong since 1862!"

            #### Screen 6: A Friendly Face
            #- **Description**: Amelia spots a familiar face in the crowd.
            #- **Dialogue**: "James? Is that you? From summer camp!"#

            show chapter_2_screen_6
            with dissolve
            a "James? Is that you? From summer camp!"

            #### Screen 7: Reunion
            #- **Description**: James approaches with a smile.
            #- **Dialogue**: "Amelia! It's been ages! How have you been?"#

            show chapter_2_screen_7
            with dissolve
            a "Amelia! It's been ages! How have you been?"

            #### Screen 8: Shared Courses
            #- **Description**: Both discussing their chosen courses.
            #- **Dialogue**: "You're in psychology too? This should be fun!"#

            show chapter_2_screen_8
            with dissolve
            j "You're in psychology too? This should be fun!"

        "No, I'll be okay thanks":
            
            #### Screen 9: Exploring Alone (Choice: Decline the tour)
            #- **Setting**: University gardens.
            #- **Description**: Amelia strolling amidst beautiful flowerbeds.
            #- **Narrative**: "A quiet moment to soak in the new surroundings."#

            show chapter_2_screen_9
            with dissolve
            n "A quiet moment to soak in the new surroundings"

            #### Screen 10: Chance Encounters
            #- **Description**: Amelia bumping into a senior student.
            #- **Dialogue**: "Lost, newbie? I can help!"#

            show chapter_2_screen_10
            with dissolve
            s "Lost, newbie? I can help!"

            #### Screen 11: Helpful Directions
            #- **Description**: The senior student pointing out important locations.
            #- **Narrative**: "The library's that way, and the psychology department? Right behind you."#

            show chapter_2_screen_11
            with dissolve
            s "The library's that way, and the psychology department? Right behind you"
            a "This place is huge hehe.. Thank you so much"

            #### Screen 6: A Friendly Face
            #- **Description**: Amelia spots a familiar face in the crowd.
            #- **Dialogue**: "James? Is that you? From summer camp!"#

            show chapter_2_screen_6
            with dissolve
            a "James? Is that you? From summer camp!"

            #### Screen 7: Reunion
            #- **Description**: James approaches with a smile.
            #- **Dialogue**: "Amelia! It's been ages! How have you been?"#

            show chapter_2_screen_7
            with dissolve
            a "Amelia! It's been ages! How have you been?"

            #### Screen 8: Shared Courses
            #- **Description**: Both discussing their chosen courses.
            #- **Dialogue**: "You're in psychology too? This should be fun!"#

            show chapter_2_screen_8
            with dissolve
            j "You're in psychology too? This should be fun!"

    #### Screen 12: First Lecture
    #- **Setting**: Lecture hall.
    #- **Description**: Students settling down, professor at the front.
    #- **Narrative**: "The real journey begins."#

    show chapter_2_screen_12
    with dissolve
    n "The real journey begins"

    #### Screen 13: Prof. Williams
    #- **Description**: A charismatic professor addressing the class.
    #- **Dialogue**: "Welcome, future psychologists!"#

    show chapter_2_screen_13
    with dissolve
    prof_Williams "Welcome, future psychologists!"

    #### Screen 14: Ice-Breaking Session
    #- **Description**: Students introducing themselves.
    #- **Dialogue**: "Hello, I'm Amelia. From London. Excited to be here!"#

    show chapter_2_screen_14
    with dissolve
    a "Hello, I'm Amelia. From London. Excited to be here!"

    #### Screen 15: Class Insights
    #- **Description**: Prof. Williams discussing the course structure.
    #- **Narrative**: "Three specializations, countless possibilities."#

    show chapter_2_screen_15
    with dissolve
    prof_Williams "Three specializations, countless possibilities"

    #### Screen 16: After Lecture
    #- **Setting**: University cafe.
    #- **Description**: Amelia and James discussing the lecture over coffee.
    #- **Dialogue**: "What did you think of Prof. Williams?"#

    show chapter_2_screen_16
    with dissolve
    a "What did you think of Prof. Williams?"
    j "Well, it was a good introduction but I feel like I know him from somewhere"
    a "Oh really?"
    j "Yeah but I can't really place where.."

    #### Screen 17: Fellow Psychologists
    #- **Description**: Meeting other first-year psychology students.
    #- **Dialogue**: "Join us for study sessions?"#

    show chapter_2_screen_17
    with dissolve
    s "Join us for study sessions?"

    #### Screen 18: Study Plans
    #- **Setting**: Library.
    #- **Description**: Amelia immersed in books.
    #- **Narrative**: "A world of knowledge awaits."#

    show chapter_2_screen_18
    with dissolve
    n "A world of knowledge awaits."

    #### Screen 19: First Assignment
    #- **Description**: Amelia scribbling down assignment details.
    #- **Narrative**: "The real work begins."#

    show chapter_2_screen_19
    with dissolve
    n "The real work begins."

    #### Screen 20: Group Projects
    #- **Setting**: Classroom.
    #- **Description**: Forming groups for assignments.
    #- **Dialogue**: "James, want to team up?"#

    show chapter_2_screen_20
    with dissolve
    a "James, want to team up?"
    j "Hey, great idea!"


    #### Screen 21: Late Night Brainstorming
    #- **Setting**: Dorm room.
    #- **Description**: Papers scattered, Amelia and James deep in discussion.
    #- **Dialogue**: "We need a unique angle for this assignment."#

    show chapter_2_screen_21
    with dissolve
    j "We need a unique angle for this assignment."

    #### Screen 22: Unfamiliar Territory
    #- **Setting**: Advanced psychology lab.
    #- **Description**: Students trying out advanced equipment.
    #- **Narrative**: "Diving deep into the mind's mysteries."#

    show chapter_2_screen_22
    with dissolve
    n "Diving deep into the mind's mysteries."

    #### Screen 23: Mentorship
    #- **Setting**: Professor's office.
    #- **Description**: Prof. Williams counseling Amelia.
    #- **Dialogue**: "Always remember why you chose psychology, Amelia."#

    show chapter_2_screen_23
    with dissolve
    prof_Williams "Always remember why you chose psychology, Amelia."

    #### Screen 24: Weekend Getaway
    #- **Setting**: Plymouth's coastline.
    #- **Description**: Amelia taking a moment of respite by the sea.
    #- **Narrative**: "Nature's beauty provides a perfect escape."#

    show chapter_2_screen_24
    with dissolve
    n "Nature's beauty provides a perfect escape"

    #### Screen 25: Unexpected News
    #- **Description**: Amelia receiving a concerning email.
    #- **Narrative**: "A sudden family emergency back home."#

    show chapter_2_screen_25
    with dissolve
    n "A sudden family emergency back home"

    #### Screen 26: Support System
    #- **Setting**: Dorm room.
    #- **Description**: Friends comforting Amelia.
    #- **Dialogue**: "We're here for you, Amelia."#

    show chapter_2_screen_26
    with dissolve
    n "We're here for you, Amelia"

    #### Screen 27: Decision Crossroad
    #- **Description**: Amelia pondering her next steps.
    #- **Choice**: "Head home for a while" | "Stay and focus on studies."#

    show chapter_2_screen_27
    with dissolve
    n "Amelia pondering her next steps"

    menu:
        "Head home for a while":

            #### Screen 28: Homeward Bound (Choice: Head home)
            #- **Setting**: Plymouth train station.
            #- **Description**: Amelia boarding a train, looking contemplative.
            #- **Narrative**: "Returning to family and familiarity."#

            show chapter_2_screen_28
            with dissolve
            n "Returning to family and familiarity"

            #### Screen 29: Family Ties
            #- **Setting**: Amelia's family home.
            #- **Description**: Embraces and shared concerns.
            #- **Dialogue**: "It's okay, mum. We'll get through this together."#

            show chapter_2_screen_29
            with dissolve
            a "It's okay, mum. We'll get through this together"

            #### Screen 30: The Weight of Reality
            #- **Setting**: Hospital room.
            #- **Description**: A family member in recovery, Amelia by their side.
            #- **Narrative**: "Facing life's unpredictable turns."#

            show chapter_2_screen_30
            with dissolve
            n "Facing life's unpredictable turns"

        "Stay and focus on studies":

            #### Screen 31: Regaining Focus (Choice: Stay)
            #- **Setting**: Library.
            #- **Description**: Amelia engrossed in her books.
            #- **Narrative**: "Channeling worry into work."#

            show chapter_2_screen_31
            with dissolve
            n "Channeling worry into work"

            #### Screen 32: Bonds Strengthened
            #- **Setting**: University grounds.
            #- **Description**: Friends offering silent support.
            #- **Dialogue**: "You're not alone in this, Amelia."#

            show chapter_2_screen_32
            with dissolve
            j "You're not alone in this, Amelia."

    #### Screen 33: Midterm Madness
    show chapter_2_screen_33
    with dissolve
    n "The crunch before exams."

    #### Screen 34: Test of Will
    show chapter_2_screen_34
    with dissolve
    n "The culmination of weeks of hard work."

    #### Screen 35: Results Day
    show chapter_2_screen_35
    with dissolve
    n "Anticipation in the air."

    #### Screen 35_1: Aftermath
    show chapter_2_screen_35_1
    with dissolve
    n "The expressions varied from relief to dread as scores settled in."

    #### Screen 36: Celebrations and Concerns
    show chapter_2_screen_36
    with dissolve
    j "I did well! But that one paper... ugh."

    #### Screen 37: Extra-Curriculars
    show chapter_2_screen_37
    with dissolve
    n "There's more to uni life than just studies."

    #### Screen 37_1: Choosing a Club
    show chapter_2_screen_37_1
    with dissolve
    n "Amelia finds herself gravitating towards the psychology club's booth."

    #### Screen 38: Unexpected Invitation
    show chapter_2_screen_38
    with dissolve
    a "A guest lecture by Dr. Eleanor Wright. Can't miss it!"

    #### Screen 39: Seminar Insights
    show chapter_2_screen_39
    with dissolve
    n "Exploring uncharted terrains of the mind."

    #### Screen 39_1: Profound Impact
    show chapter_2_screen_39_1
    with dissolve
    n "The words of Dr. Wright lingered, seeding new curiosities in Amelia's mind."

    #### Screen 40: Networking
    show chapter_2_screen_40
    with dissolve
    a "Your insights on Jungian psychology were intriguing!"

    #### Screen 41: End of Semester Party
    show chapter_2_screen_41
    with dissolve
    n "A well-deserved break from the rigors of academic life."

    #### Screen 42: Reflective Evenings
    show chapter_2_screen_42
    with dissolve
    n "Documenting the highs and lows."

    #### Screen 42_1: Starlit Pondering
    show chapter_2_screen_42_1
    with dissolve
    n "Underneath the celestial curtain, Amelia contemplated future possibilities."

    #### Screen 43: Hopes for the Future
    show chapter_2_screen_43
    with dissolve
    a "Next up, exploring positive psychology."

    #### Screen 44: End of Semester Reflections
    show chapter_2_screen_44
    with dissolve
    n "The semester's challenges, friendships, and learnings."

    #### Screen 44_1: An Enclosed Letter
    show chapter_2_screen_44_1
    with dissolve
    n "Amelia found an old letter from her parents, showering love and encouragement."

    #### Screen 45: Looking Ahead
    show chapter_2_screen_45
    with dissolve
    a "Next semester, here I come."
    #- **Narrative**: "A well-deserved break from the rigors of academic life."#




    return