# 1_prologue.rpy
# Highly detailed and structured introduction for the prologue of "The CK - Amelia"

# Define characters
define a = Character("Amelia", window_style="window", what_xpos=30, what_text_align=0.0, who_xpos=-180, who_ypos=+15)
define amelia = Character("Amelia", window_style="window", what_xpos=30, what_text_align=0.0, who_xpos=-180, who_ypos=+15)
define e = Character("Ella", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define ella = Character("Ella", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define lily = Character("Lily", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define j = Character("James", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define p = Character("Parents", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define n = Character("", window_style="window_n", what_xpos=620, what_text_align=0.0, who_xpos=+400, who_ypos=+15)
define narrator = Character("", window_style="window_n", what_xpos=620, what_text_align=0.0, who_xpos=+400, who_ypos=+15)
define student = Character("Student", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define roommate = Character("Liz", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define mom = Character("Mom", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define m = Character("Mom", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define dad = Character("Dad", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define d = Character("Dad", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define staff = Character("Staff", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define professor = Character("Professor", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define woman = Character("Mysterious woman", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define maya = Character("Maya", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define l = Character("Lucas", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define liz = Character("Liz", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define instructor = Character("Instructor", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define scientist = Character("Scientist", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define zara = Character("Zara", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define sarah = Character("Sarah", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define student_2 = Character("Student", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define lucas = Character("Lucas", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define lucas_text = Character("Lucas", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define credit_text = Character(window_style="window_c", what_xpos=620, what_text_align=0.0, who_xpos=+400, who_ypos=+15)
define hawthorne = Character("Hawthorne", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)
define raj = Character("Raj", window_style="window_2", what_xpos=1160, what_text_align=0.0, who_xpos=+920, who_ypos=+15)


default art_style = "default"


label prologue:
    play music "intro_theme.mp3" fadein 2.0
    scene bg aerial_uk with pan
    narrator "Above the verdant tapestry of the United Kingdom, our view descends from the tranquil skies. We pass over rolling hills and age-old cities, bustling with life and rich with history."

    scene bg aerial_london with pan
    narrator "As we approach London, the landscape shifts from green fields to the dense, vibrant sprawl of urban life. We zoom into the quieter outskirts, where family homes dot the landscape like quaint islands amidst the city's rush."

    scene bg suburban_home_exterior_day with pan
    narrator "Here in a peaceful suburb, we find a modest home with a well-tended garden, the late afternoon sun casting long shadows across the lawn."

    scene bg amelia_bedroom_night with dissolve
    narrator "Inside, the bedroom of eighteen-year-old Amelia is bathed in the soft glow of twilight. Stuffed animals line the shelves, and books are stacked neatly by the bed. Amelia herself lies asleep, her chest rising and falling with each deep, even breath."

    narrator "As night deepens, the boundaries between reality and dreams begin to blur. We dive into Amelia's subconscious, entering a dreamscape crafted from her memories and imaginations."

    scene bg dream_landscape with dissolve
    narrator "Amelia finds herself in a vast park, sunlight filtering through the leaves, casting patterns of light and shadow. This is no ordinary park; it's a realm where her childhood memories come to life, populated by figures both familiar and fantastical."

    show m and d at center
    m "Amelia, dear, enjoy your adventure!"
    d "We'll be right here if you need us."

    # Introducing characters for each story path
    define child1 = Character('Child from the Golden Path', color="#f2c2d0")
    define child2 = Character('Child from the Quiet Grove', color="#d4a190")
    define child3 = Character('Child from the Forgotten Trail', color="#b6c8a2")
    define adult1 = Character('Mentor from the Golden Path', color="#c7a1c2")
    define adult2 = Character('Guide from the Quiet Grove', color="#a2b6c8")
    define adult3 = Character('Historian from the Forgotten Trail', color="#a2c8c2")

    show child1 at left
    show child2 at right
    show child3 at center
    child1 "Let's explore the festival and find the lost toy!"
    child2 "Come, let's find peace in the grove."
    child3 "Join me on an adventure to discover hidden treasures."

    narrator "Around her, the air buzzes with the energy of past joys and adventures, each path offering a journey through different aspects of her childhood."

    menu:
        "Which memory path will Amelia explore? Each is filled with its own set of characters and emotional journeys.":
            "The Festival - Vibrant and joyful, with games and community spirit":
                jump festival_memory
            "The Quiet Grove - Solitary and introspective, a place for reflection":
                jump grove_memory
            "The Forgotten Trail - Adventurous and mysterious, uncovering family legacies":
                jump trail_memory

# Expanded dialogue and interaction for "The Golden Path: The Festival Day" in "The CK - Amelia"

label golden_path:
    scene bg golden_path with dissolve
    play music "magical_festival_tune.mp3" loop
    narrator "Following a trail paved with golden bricks, Amelia ventures through a grove that parts to reveal the enchanting entrance to a festival, reminiscent of the joyful fairs of her early childhood."

    show amelia at center
    a "It’s just like the festivals I visited with Mom. Everything’s pulsing with life and color!"

    # Scene 1: Entering the Festival
    scene bg festival_entrance with dissolve
    narrator "The festival gates tower above, ornate and welcoming, beckoning all who approach to enter a world of wonder and laughter."
    
    show vendor at right
    vendor "Well met, young traveler! What brings you to our merry gathering?"
    a "I’d love some tickets, please! I can’t wait to see everything!"
    vendor "Ah, in this realm, your currency is wonder and your ticket is curiosity. Explore to your heart's content, little adventurer!"

    # Scene 2: House of Mirrors
    scene bg house_of_mirrors_entrance with dissolve
    narrator "Curiosity piqued, Amelia steps into the House of Mirrors. Within, the world bends and twists, reality stretching into fantastical shapes and sizes."
    
    show amelia_child at center
    narrator "Caught in a twisted mirror, Amelia glimpses herself as a child, her reflection echoing her inner youthfulness."
    a "Am I really that little again? Or is it just the magic of this place playing tricks on me?"

    # Scene 3: Meeting the Lost Boy
    scene bg house_of_mirrors_inside with dissolve
    show boy at left
    boy "Ah! You startled me!"
    a "I didn’t mean to scare you. Are you alright?"
    boy "I’m lost... I was chasing my teddy when I got turned around in here."
    a "Let’s find your teddy together. It’s easy to get lost in here, but I’ll help you."

    # Scene 4: Journey to the Ferris Wheel
    scene bg festival_grounds with dissolve
    narrator "Together, they navigate the labyrinth of mirrors, emerging into the carnival's heart, where the Ferris wheel spins majestically against the sky."
    
    show ferris_wheel_operator at right
    ferris_wheel_operator "To reach the sky and touch the stars, solve me this, and you shall pass."
    menu:
        "What goes up but never comes down?":
            "Your age"
            "A balloon"
            "The sun"
    narrator "Amused by the spirit of your answer, the operator ushers you both aboard."
    ferris_wheel_operator "Right you are! Up you go, to the heavens above!"

    # Scene 5: Atop the Ferris Wheel
    scene bg ferris_wheel_top with dissolve
    narrator "As the wheel climbs, Amelia's heart soars with it, the entire festival sprawling below them like a kingdom of joy."
    boy "There! Look! My teddy’s caught up there!"
    

    narrator "Summoning her courage, Amelia reaches daringly into the sky, snagging the teddy bear from its lofty perch."
    a "Got it! Here’s your teddy, safe and sound."
    boy "You’re amazing, Amelia! I can’t thank you enough."
    menu:
        "Hold the boy's hand":
            boy "You’re really brave, you know that?"
            a "blushing, feeling a flutter in her heart."
        "Smile at the boy":
            a "Just doing what friends do!"
            boy "stammers his thanks, cheeks tinted with a shy blush."

    # Scene 6: Waking from the Dream
    scene bg golden_path_return with dissolve
    narrator "As the Ferris wheel gently descends, the enchanting edges of the festival blur into the mists of awakening."
    a "Was it all a dream? It felt so real, so vivid."
    narrator "Amelia's heart is full as she steps off the golden path, the echoes of laughter and newfound courage warming her as she stirs awake."

    show dad at distance
    dad "Time to wake up, Amelia."
    
    narrator "With her father’s call, Amelia awakens, her spirit carrying the joy and magic of the festival day into the waking world."

    jump full_english

label shaded_grove:
    scene bg_grove_entrance with fade
    play music "calm_woods.mp3" loop
    narrator "As Amelia leaves the clamor of the festival, a serene path lined with ancient trees draws her into its embrace, whispering promises of peace."

    show amelia centered at t11
    a "This silence... it feels like it's washing over me, washing the chaos away."
    
    # Scene 1: Deep into the Grove
    scene bg_shaded_grove with dissolve
    narrator "Stepping deeper into the grove, the cool shade envelops Amelia, each breath mingling with the earthy scent of moss and leaf."
    
    # Scene 2: Finding the Reading Nook
    narrator "A familiar nook under an ancient oak seems almost prepared for her, scattered with soft, green moss perfect for sitting and reflecting."
    
    show amelia at right with dissolve
    a "This spot... I remember feeling at peace here before. Maybe it can help me again."

    # Scene 3: Discovery of Old Journal
    narrator "Beside the nook, Amelia discovers an old journal, its pages filled with thoughtful entries from past visitors."
    a "Others have found sanctuary here too. Their words could guide me."

    # Scene 4: Reflection on Solitude
    menu:
        "Read the journal entries":
            $ SD += 2
            narrator "Amelia reads entries of solitude and introspection, each story echoing her own need for peace."
            a "These stories... they're like echoes of my own thoughts."
        
        "Sit in quiet reflection":
            $ MH += 2
            narrator "Choosing to sit quietly, Amelia lets the silence of the grove seep into her, her thoughts slowly untangling."
            a "Sometimes, silence speaks louder than words."

    # Scene 5: Encounter with an Old Tree
    narrator "Amelia wanders to a grand old tree, its branches sprawling skyward like open arms."
    a "You've stood here through so much. What stories could you tell?"
    
    # Scene 6: Meditation by the Stream
    scene bg_stream with dissolve
    narrator "A gentle stream flows through the grove, its soothing sounds inviting Amelia to sit and meditate by its banks."
    a "The flow of water, always moving forward... maybe I can learn from it."

    # Scene 7: Insight from Nature
    narrator "As she meditates, the rhythm of nature offers Amelia insights into her own life's rhythms, the ups and downs, the cycles of conflict and resolution."
    a "Nature endures, adapts, and thrives. I guess I can too."

    # Scene 8: Writing in Her Journal
    narrator "Inspired, Amelia begins to write in her own journal, each word a step towards understanding her emotions about the family argument."
    a "Writing this down, I'm starting to see things more clearly."

    # Scene 9: Meeting a Wise Owl
    show owl at left
    narrator "An owl perches nearby, watching Amelia with wise, knowing eyes."
    a "What wisdom do you hold, old watcher?"
    owl "The wisdom to see in the dark, to listen more than speak."

    # Scene 10: Lessons from the Owl
    narrator "The owl’s presence reminds Amelia of the need to look deeper into her own thoughts, to find the wisdom hidden in her own experiences."
    a "Maybe there's more to learn from this argument than I thought."

    # Scene 11: Sunset in the Grove
    scene bg_sunset_grove with dissolve
    narrator "As the sun sets, painting the grove in hues of gold and amber, Amelia feels a profound connection to the world around her."
    a "It's beautiful... how the end of the day brings such peace."

    # Scene 12: Final Reflection
    narrator "Sitting back under the oak, Amelia reflects on the day’s journey through the grove, the lessons learned, and the peace found."
    a "I've found a little of what I lost today, not just in the grove, but in myself."

    # Scene 13: Dream Fades
    scene bg_dream_fade with dissolve
    narrator "As the grove begins to fade, the edges of her dream blurring, Amelia senses her return to the waking world."
    a "Was it all just a dream? It felt so real."

    # Scene 14: Waking Up
    scene bg_amelia_room_morning with fade
    narrator "Amelia awakens in her room, the first rays of morning light creeping through the curtains, the peace of the grove still lingering in her heart."
    a "I’ll hold onto this calm, even awake. It's part of me now."

    # Scene 15: New Day, New Insights
    narrator "Emboldened by her experiences, Amelia resolves to carry the lessons of the grove into her daily life, using her newfound peace to navigate the complexities ahead."
    a "Today feels like a new beginning, thanks to the grove."

    jump full_english

label forgotten_trail:
    scene bg_festival_path with fade
    play music "mystical_forest.mp3" loop
    narrator "Amelia leaves the lively festival behind, drawn to a winding path strewn with fallen leaves and overgrown roots, beckoning her towards the unknown."

    show amelia centered at t11
    a "This path... it feels like it's calling me."

    # Scene 1: Entering the Trail
    scene bg_forgotten_trail with dissolve
    narrator "Amelia steps onto the forgotten trail, the sounds of the festival fading away as the earthy scent of the forest fills the air."

    # Scene 2: Discovery of a Map
    show amelia at right with dissolve
    narrator "Caught in the branches of a tree, Amelia finds an old, weathered map, its edges frayed but the markings clear. A handwritten note reads, 'Discover what was left behind.'"
    a "A map? I wonder where it leads."

    # Scene 3: Journey Along the Trail
    narrator "With curiosity guiding her steps, Amelia follows the map, reflecting on the stories her mother used to tell about exploring similar paths."

    # Scene 4: Encounter with Historical Markers
    scene bg_historical_markers with dissolve
    narrator "As she walks, Amelia discovers markers that tell stories of her ancestors, including a great-grandmother known for her herbal remedies."
    a "These markers... they're like pieces of my family's history."

    # Scene 5: First Major Discovery
    scene bg_buried_box with dissolve
    narrator "The map leads her to a marked spot. Digging gently, she uncovers a buried box, old and rusted but clearly well cared for."
    show amelia at left with dissolve
    a "What could be inside?"

    # Scene 6: Investigation of Contents
    scene bg_box_contents with dissolve
    narrator "Inside the box, Amelia finds various heirlooms: old photographs, letters, and a broken watch, each piece whispering stories of the past."
    a "These must have belonged to my mother and her family."

    # Scene 7: Interactive Choice - Investigate Heirlooms or Restore an Item
    menu:
        "Investigate Heirlooms":
            $ OK += 5
            narrator "Amelia carefully examines the photographs, discovering images of her mother as a young woman, alongside unknown faces."
            show amelia with photo at right
            a "She looks so happy... who are these people with her?"
        
        "Restore an Old Item":
            $ MC += 5
            narrator "Choosing to fix the broken watch, Amelia carefully cleans and adjusts it, feeling a sense of accomplishment as it ticks to life."
            show amelia with watch at right
            a "It works... it's like bringing a piece of the past back to life."

    # Scene 8: Emotional Reflection
    narrator "Handling her mother’s belongings, Amelia feels a surge of connection and loss, her heart heavy yet full as she learns more about her mother’s younger days."
    a "I never knew she had all these adventures."

    # Scene 9: Significant Revelation
    show letter at center with dissolve
    narrator "Among the letters, Amelia finds one written by her mother to a dear friend, revealing a passionate pursuit of psychology and philosophy, mirroring Amelia's own interests."
    a "She was just like me... this is incredible."

    # Scene 10: Encounter with a Spirit Guide
    show spirit_guide at left with dissolve
    narrator "A mysterious figure appears on the trail, resembling her mother in her youth. This spirit guide offers wisdom about the importance of preserving family legacy and making peace with the past."
    spirit_guide "Amelia, our paths are intertwined. Your journey continues where mine left off."

    # Scene 11: Dialogue with the Spirit Guide
    show amelia at right with dissolve
    narrator "The guide shares stories from her mother’s youth, including her struggles and triumphs, and how she found solace and direction in the same philosophical and psychological pursuits that Amelia is now following."
    spirit_guide "Your mother faced many challenges, but she found strength in understanding the mind and the world around her."

    # Scene 12: Lesson on Legacy
    narrator "The guide emphasizes that legacies are not just about preserving the past but also about shaping the future with the lessons learned. Amelia realizes her mother’s influence on her own passions and career path."
    spirit_guide "Carry these lessons forward, Amelia. They are the roots that will support your growth."

    # Scene 13: Dream Symbolism Intensifies
    scene bg_forest_awakens with dissolve
    narrator "As the conversation deepens, the surrounding forest seems to come alive, the trees whispering, the wind carrying voices of the past, each leaf a note in the symphony of her ancestry. Amelia feels a profound connection to her mother and a clearer understanding of her own path."
    a "I feel... like I'm part of something much bigger."

    # Scene 14: Conclusion of the Encounter
    narrator "The guide fades away as Amelia promises to keep the memories alive, ensuring her family's legacy continues through her actions and remembrances."
    spirit_guide "Remember, Amelia. You are never alone on your journey."

    # Scene 15: Waking from the Dream
    scene bg_amelia_room_morning with fade
    narrator "Amelia wakes up, clutching a photograph from the box, now sitting on her nightstand in the real world. She feels a renewed sense of purpose, understanding that her mother’s legacy is alive within her, guiding her decisions and fueling her passions."
    a "Thank you, Mom. I understand now."

    jump full_english


label full_english:
    scene bg_amelia_room_morning with fade
    play music "morning_birds.mp3" loop
    narrator "Amelia wakes up slowly, the remnants of her dream still clinging to her mind. The light filters through her curtains, casting patterns on her bed. As she stirs, her thoughts turn to the day ahead, and her father's usual Sunday routine."

    show amelia_bed at center with dissolve
    a "That dream... it felt so real. I could almost feel Mom's presence."

    scene bg_kitchen_morning with fade
    narrator "Amelia descends the stairs to the smell of sizzling bacon and the sound of eggs frying. Her father, Mr. James, stands at the stove, his back to her."
    show amelia_kitchen at right with dissolve
    show dad_stove at left with dissolve
    a "Dad always tries to make Sundays special with a full English breakfast. He believes in starting the week off right, even if his jokes are as overdone as his bacon sometimes. Despite his cheesy humor, his steadfast presence has always been the bedrock of our home."

    dad "Morning, Amelia! Just in time for the Sunday special. How do you like your eggs today?"

    menu:
        "Smells great, Dad. Need any help?":
            $ SI += 2
            a "Smells great, Dad. Need any help?"
            dad "Always the helper, huh? No need today, love. Just sit yourself down and get ready for a feast!"

            menu:
                "Sure, Dad. I'll set the table.":
                    $ SI += 1
                    a "Sure, Dad. I'll set the table."
                    dad "Thanks, Amelia. You're the best."

                "I could make some coffee.":
                    $ SI += 1
                    a "I could make some coffee."
                    dad "Perfect. A full English isn't complete without a good cup of coffee."

        "I had the strangest dream about the park we used to go to.":
            $ MH += 2
            a "I had the strangest dream about the park we used to go to."
            dad "Oh? Dreams can be quite the riddle. Tell me about it while we eat; maybe we can figure it out together."

            menu:
                "It was so vivid. I felt like a child again.":
                    $ MH += 1
                    a "It was so vivid. I felt like a child again."
                    dad "Those dreams can be powerful. Maybe it's a sign you're reconnecting with your inner child."

                "There were so many colors and people.":
                    $ MH += 1
                    a "There were so many colors and people."
                    dad "Sounds like a celebration. Maybe it's a reflection of all the changes happening in your life right now."

        "Do you ever miss Mum when you cook breakfast like this?":
            $ MC += 2
            a "Do you ever miss Mum when you cook breakfast like this?"
            dad "Every day, Amelia. But making this breakfast reminds me of all the good times we had as a family. It’s bittersweet."

            menu:
                "She loved these breakfasts, didn't she?":
                    $ MC += 1
                    a "She loved these breakfasts, didn't she?"
                    dad "She did. It was her favorite way to start the weekend. We had some great mornings together."

                "I wish she were here.":
                    $ MH += 1
                    a "I wish she were here."
                    dad "Me too, love. But she's always with us in spirit. We keep her memory alive through these little traditions."

        "Can we skip the heavy breakfast today? Just not feeling it.":
            $ MH += 2
            a "Can we skip the heavy breakfast today? Just not feeling it."
            dad "Of course, we can adjust. How about some fruit and yogurt instead? Want to keep it light."

            menu:
                "That sounds good, thanks.":
                    $ MH += 1
                    a "That sounds good, thanks."
                    dad "No problem at all. Sometimes it's good to keep it light."

                "Maybe just some toast and tea?":
                    $ MH += 1
                    a "Maybe just some toast and tea?"
                    dad "Toast and tea it is. Simple and comforting."

    # Breakfast conversation
    scene bg_breakfast_table with fade
    show amelia_table at right with dissolve
    show dad_table at left with dissolve
    narrator "After choosing an option, they sit down to eat together. The conversation flows from light banter to more serious topics, such as Amelia's upcoming plans for university, reflecting the choice made by the player."

    dad "So, are you excited about starting at Plymouth? It's a big step, but I know you'll do great."

    a "Yeah, I'm excited but also a bit nervous. It's a whole new chapter, you know?"

    dad "That's completely normal. Just remember, it's okay to feel nervous. It's a sign that you care about what you're doing. And don't forget, you can always call home if you need anything."

    # Additional dialogue choices during breakfast
    menu:
        "What was university like for you, Dad?":
            a "What was university like for you, Dad?"
            dad "Ah, university was a wild ride. Lots of studying, but also some of the best times of my life. Made lifelong friends and learned a lot about myself."

            menu:
                "Tell me more about your friends from university.":
                    a "Tell me more about your friends from university."
                    dad "We were quite the motley crew. There was Jack, always the prankster, and Susan, who kept us all in line. We still keep in touch, you know."

                "What did you study?":
                    a "What did you study?"
                    dad "I majored in history. I've always been fascinated by the stories of the past and how they shape our present and future."

        "Do you think I'll fit in?":
            a "Do you think I'll fit in?"
            dad "Absolutely. Just be yourself, and you'll find your people. Everyone's in the same boat, trying to figure things out."

            menu:
                "What if I don't make friends right away?":
                    a "What if I don't make friends right away?"
                    dad "Give it time. Friendships take time to build. Just be open and kind, and people will naturally gravitate towards you."

                "I'm worried about the academic pressure.":
                    a "I'm worried about the academic pressure."
                    dad "It's important to stay organized and ask for help when you need it. Don't try to do everything on your own."

        "Any advice for making the most of it?":
            a "Any advice for making the most of it?"
            dad "Get involved in different activities, meet new people, and don't be afraid to step out of your comfort zone. University is as much about personal growth as it is about academics."

            menu:
                "What activities were you involved in?":
                    a "What activities were you involved in?"
                    dad "I was in the debate club and played for the university's rugby team. Those experiences taught me a lot about teamwork and leadership."

                "How did you balance everything?":
                    a "How did you balance everything?"
                    dad "It wasn't always easy, but keeping a schedule and prioritizing what was important helped. And remember to take breaks and enjoy the journey."

        "I'm really going to miss home.":
            a "I'm really going to miss home."
            dad "We'll miss you too, Amelia. But remember, home is always here for you. And you'll be back for holidays and breaks. It'll be a new adventure."

            menu:
                "I'll miss our Sunday breakfasts.":
                    a "I'll miss our Sunday breakfasts."
                    dad "We can always have virtual breakfasts. I'll cook, and you can join me on video call. It'll be just like old times."

                "I'm worried about feeling homesick.":
                    a "I'm worried about feeling homesick."
                    dad "It's natural to feel that way, but you'll find your rhythm. Stay connected with us, and make new memories at university. It'll get easier with time."

    # Transition to Amelia's Room - The First Hub
    scene bg_amelia_room_day with fade
    narrator "Post-breakfast, Amelia heads back to her room, the narrative following her thoughts."
    show amelia_room at center with dissolve
    a "This room is more than just four walls to me; it’s a capsule of my life. Every poster, every book on that shelf, and the keepsakes from our family trips—they all tell stories of who I was and who I’m hoping to become."

    narrator "Amelia sits down at her desk, looking at the various items that have defined her over the years. Her thoughts drift to the future, to the new experiences awaiting her at Plymouth, but also to the comfort and security of her home."

    a "Change is scary, but it's also exciting. I just need to remember to stay true to myself and keep moving forward."

    narrator "Feeling a mix of nostalgia and anticipation, Amelia begins to organize her day, ready to tackle the tasks ahead and embrace the journey that awaits her."

    return

label amelia_room_hub:
    scene bg_amelia_room_day with fade
    play music "amelia_theme.mp3" loop
    narrator "Post-breakfast, Amelia heads back to her room, the narrative following her thoughts."
    show amelia_room at center with dissolve
    a "This room is more than just four walls to me; it’s a capsule of my life. Every poster, every book on that shelf, and the keepsakes from our family trips—they all tell stories of who I was and who I’m hoping to become."

    # Hub description
    narrator "Amelia’s room serves as her personal hub. From here, she can explore different activities, complete tasks, and reflect on her journey."

    # Bookshelf Quote Challenge
    menu:
        "Interact with the bookshelf":
            jump bookshelf_challenge

        "Check the To-Do List":
            jump todo_list

label bookshelf_challenge:
    scene bg_bookshelf with fade
    narrator "Amelia’s bookshelf is an eclectic collection of literature, psychology, and mysticism. It reflects her wide-ranging interests and her journey of self-discovery."

    # Example quote challenge
    $ quote, correct_author, wrong_author1, wrong_author2, wrong_author3 = renpy.random.choice([
        ("The unexamined life is not worth living.", "Socrates", "Plato", "Aristotle", "Epicurus"),
        ("To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.", "Ralph Waldo Emerson", "Henry David Thoreau", "Walt Whitman", "Mark Twain"),
        ("In the end, we will remember not the words of our enemies, but the silence of our friends.", "Martin Luther King Jr.", "Malcolm X", "Nelson Mandela", "Mahatma Gandhi"),
        # Add more quotes as needed
    ])

    narrator "{quote}"
    menu:
        correct_author:
            $ AA += 1
            a "Oh yeah, that's right, isn't it... It was {correct_author}. Always resonates with me."
            return
        wrong_author1:
            $ SD += 1
            a "Wait, who said that again? Wasn’t it... no, that doesn’t sound right."
            return
        wrong_author2:
            $ SD += 1
            a "Wait, who said that again? Wasn’t it... no, that doesn’t sound right."
            return
        wrong_author3:
            $ SD += 1
            a "Wait, who said that again? Wasn’t it... no, that doesn’t sound right."
            return

label todo_list:
    scene bg_todolist with fade
    narrator "Amelia reviews her to-do list for the day, deciding which task to tackle first."

    menu:
        "Meeting with Ella":
            jump meeting_ella

        "Visit to the Bookstore":
            jump visit_bookstore

        "Buy a Birthday Gift for Dad":
            jump buy_gift

label meeting_ella:
    scene bg_amelia_room_day with fade
    narrator "Amelia decides to meet with Ella. She considers the best place to catch up and enjoy their time together."
    
    menu:
        "Café":
            jump ella_cafe
        "Park":
            jump ella_park
        "Art Gallery":
            jump ella_gallery

label ella_cafe:
    scene bg_cafe with fade
    narrator "Amelia and Ella sit down at a cozy café, the aroma of fresh coffee filling the air."
    a "It's so nice to catch up, Ella. I feel like it's been ages."
    e "I know, right? So, how are you feeling about Plymouth?"

    menu:
        "Excited but a bit nervous.":
            a "Excited but a bit nervous. It's a big change, but I think I'm ready."
            e "You'll do great, Amelia. Just be yourself, and you'll make friends in no time."
        "Mostly excited! I can't wait to start.":
            a "Mostly excited! I can't wait to start and meet new people."
            e "That's the spirit! You'll have an amazing time, I'm sure of it."

    e "Have you thought about what clubs or activities you might join?"

    menu:
        "I'm thinking of joining a debate club.":
            a "I'm thinking of joining a debate club. It sounds challenging but fun."
            e "That sounds perfect for you! You'll be great at it."
        "Maybe something more relaxed, like a book club.":
            a "Maybe something more relaxed, like a book club. I love reading, and it would be a good way to unwind."
            e "A book club sounds wonderful. You can share all those quotes you love so much."

    a "How about you, Ella? Any plans for the upcoming semester?"
    e "Just focusing on my studies and maybe picking up a new hobby. We'll see."

    narrator "The conversation flows easily between them, filled with laughter and shared memories."

    return

label ella_park:
    scene bg_park with fade
    narrator "Amelia and Ella walk through the park, the sound of rustling leaves and chirping birds creating a peaceful atmosphere."
    a "This place always brings back memories. We spent so much time here as kids."
    e "Yeah, it's like our little sanctuary."

    menu:
        "I remember playing hide and seek here.":
            a "I remember playing hide and seek here. You were always so good at hiding."
            e "And you were always so determined to find me! Good times."
        "Do you remember our treehouse?":
            a "Do you remember our treehouse? We used to think it was a castle."
            e "Yes! We had such vivid imaginations back then. I miss those days."

    e "So, are you feeling ready for university life?"

    menu:
        "I'm ready for a fresh start.":
            a "I'm ready for a fresh start. It's time for new adventures."
            e "Absolutely! Embrace every moment, Amelia."
        "It's a bit daunting, but I'm excited.":
            a "It's a bit daunting, but I'm excited. Change is always a bit scary."
            e "You'll adapt quickly, I'm sure. Just take it one step at a time."

    narrator "They continue their walk, talking about their hopes and dreams for the future."

    return

label ella_gallery:
    scene bg_art_gallery with fade
    narrator "Amelia and Ella explore the art gallery, taking in the beautiful and thought-provoking pieces."
    a "Art has a way of speaking to the soul, doesn't it?"
    e "Absolutely. It's like a window into the artist's mind."

    menu:
        "This piece reminds me of our trip to Paris.":
            a "This piece reminds me of our trip to Paris. Do you remember that?"
            e "How could I forget? It was such an amazing experience."
        "I love the colors in this one.":
            a "I love the colors in this one. They evoke such strong emotions."
            e "Yes, it's like the artist captured a piece of their soul on the canvas."

    e "So, what are you most looking forward to at Plymouth?"

    menu:
        "Meeting new people and making friends.":
            a "Meeting new people and making friends. It's a chance to start fresh."
            e "You'll be great at that. You're so friendly and open."
        "Diving deep into my studies and learning new things.":
            a "Diving deep into my studies and learning new things. I can't wait to expand my knowledge."
            e "That's the Amelia I know. Always eager to learn."

    narrator "Their conversation continues, filled with excitement and anticipation for the future."

    return

label visit_bookstore:
    scene bg_bookstore with fade
    narrator "Amelia heads to the bookstore, excited to explore new books and expand her knowledge."
    
    menu:
        "Self-help":
            jump bookstore_self_help
        "New age spirituality":
            jump bookstore_new_age
        "Advanced psychology textbooks":
            jump bookstore_psychology

label bookstore_self_help:
    scene bg_bookstore_shelf with fade
    narrator "Amelia picks up a self-help book, hoping to find practical advice for personal growth."
    a "This looks interesting. I could use some tips on staying positive and motivated."

    menu:
        "Read a passage about positive thinking.":
            a "Positive thinking can change your life by changing your perspective."
            narrator "Amelia feels a bit more hopeful and motivated."

        "Skim through the chapter on overcoming fear.":
            a "Overcoming fear is about facing it head-on and not letting it control you."
            narrator "Amelia feels a bit more courageous."

    narrator "She decides to buy the book, thinking it will be a helpful companion at university."

    return

label bookstore_new_age:
    scene bg_bookstore_shelf with fade
    narrator "Amelia picks up a book on new age spirituality, intrigued by the unconventional ideas."
    a "This might give me a fresh perspective on life and the universe."

    menu:
        "Read about meditation techniques.":
            a "Meditation helps you connect with your inner self and find peace."
            narrator "Amelia feels a sense of calm and clarity."

        "Explore the section on energy healing.":
            a "Energy healing is about balancing your inner energies for overall well-being."
            narrator "Amelia feels intrigued and curious."

    narrator "She decides to buy the book, excited to explore new concepts and practices."

    return

label bookstore_psychology:
    scene bg_bookstore_shelf with fade
    narrator "Amelia picks up an advanced psychology textbook, eager to deepen her understanding of the mind."
    a "This will be a great resource for my studies at Plymouth."

    menu:
        "Read about cognitive behavioral therapy.":
            a "CBT helps people identify and change negative thought patterns."
            narrator "Amelia feels more knowledgeable about therapeutic techniques."

        "Explore the chapter on developmental psychology.":
            a "Understanding human development helps us better understand behavior across the lifespan."
            narrator "Amelia feels more informed about human growth and development."

    narrator "She decides to buy the book, knowing it will be invaluable for her studies."

    return

label buy_gift:
    scene bg_shop_street with fade
    narrator "Amelia decides to buy a birthday gift for her dad. She considers different stores to find the perfect present."
    
    menu:
        "Electronics Store":
            jump gift_electronics
        "Sports Shop":
            jump gift_sports
        "Vintage Record Shop":
            jump gift_record_shop

label gift_electronics:
    scene bg_electronics_store with fade
    narrator "Amelia browses the electronics store, looking for something practical and useful."
    a "Dad could use a new gadget for his home office. This looks perfect."

    menu:
        "Buy a new tablet.":
            a "A new tablet would be great for his work and leisure."
            narrator "Amelia feels confident in her choice."
            $ MC += 1

        "Pick up a smart speaker.":
            a "A smart speaker would be handy for him at home."
            narrator "Amelia thinks her dad will love this new gadget."
            $ SI += 1

    return

label gift_sports:
    scene bg_sports_shop with fade
    narrator "Amelia visits the sports shop, thinking about her dad's love for sports."
    a "Maybe a new set of golf clubs or some running gear. He'd love that."

    menu:
        "Choose new golf clubs.":
            a "He’s been talking about upgrading his clubs for a while."
            narrator "Amelia feels excited about her choice."
            $ MC += 1

        "Pick up running gear.":
            a "He’s been getting into running recently. This will be perfect."
            narrator "Amelia feels happy with her thoughtful choice."
            $ SI += 1

    return

label gift_record_shop:
    scene bg_record_shop with fade
    narrator "Amelia steps into the vintage record shop, feeling nostalgic."
    a "Dad's always loved his vinyl collection. A rare record would be a great gift."

    menu:
        "Buy a classic rock album.":
            a "He’s always loved classic rock. This will be a great addition to his collection."
            narrator "Amelia feels pleased with her choice."
            $ SD += 1

        "Pick up a jazz record.":
            a "He’s a big fan of jazz. This will make him very happy."
            narrator "Amelia feels proud of her thoughtful choice."
            $ MH += 1

    return

label amelia_room_hub_end:
    scene bg_amelia_room_day with fade
    narrator "After completing her tasks for the day, Amelia returns to her room, feeling accomplished and reflective."
    a "Today was productive. I feel more prepared for the changes ahead."
    return


label visit_british_museum:
    scene bg_british_museum_ext with fade
    play music "museum_theme.mp3" loop
    narrator "After completing her to-do list, Amelia and her Dad visit the British Museum as a pre-birthday celebration."
    show amelia and dad at center with dissolve

    a "I'm so excited to explore the museum with you, Dad. It's been a while since we last came here."
    dad "I know, right? The British Museum never fails to amaze me. There's always something new to learn."

    scene bg_british_museum_hall with fade
    narrator "They enter the grand hall of the museum, filled with towering columns and historical artifacts."

    menu:
        "Start with the Ancient Egypt Exhibit":
            jump ancient_egypt_exhibit

        "Visit the Greek and Roman Statues":
            jump greek_roman_statues

        "Explore the Medieval Europe Section":
            jump medieval_europe_section

label ancient_egypt_exhibit:
    scene bg_ancient_egypt with fade
    narrator "Amelia and her Dad stand before the grand statues of Ancient Egypt, feeling the weight of history."
    a "These statues are incredible. Just think about how old they are."
    dad "It's fascinating, isn't it? The Ancient Egyptians achieved so much with the resources they had."

    menu:
        "Discuss the significance of the Rosetta Stone":
            a "Dad, can you remind me why the Rosetta Stone is so important?"
            dad "Sure. The Rosetta Stone was key to deciphering Egyptian hieroglyphs. It had the same text in Greek, Demotic, and hieroglyphic script, which allowed scholars to finally understand the language."
            $ AA += 1
            narrator "Amelia feels a deeper appreciation for the stone's historical significance."

        "Examine the mummies and talk about their preservation techniques":
            a "The mummies are both fascinating and a bit eerie. How did they preserve them so well?"
            dad "The Egyptians had advanced techniques for mummification. They removed internal organs, used natron to dry out the body, and then wrapped it in linen. It was all part of their belief in the afterlife."
            $ AA += 1
            narrator "Amelia marvels at the ancient knowledge and their spiritual beliefs."

    a "This place always makes me think about the vastness of history and how much there is to learn."

    scene bg_british_museum_hall with fade
    narrator "They move on to the next exhibit."

    menu:
        "Visit the Greek and Roman Statues":
            jump greek_roman_statues

        "Explore the Medieval Europe Section":
            jump medieval_europe_section

label greek_roman_statues:
    scene bg_greek_roman_statues with fade
    narrator "Amelia and her Dad walk among the statues of Greek gods and Roman emperors."
    a "The craftsmanship is amazing. Look at the detail in the marble."
    dad "The Greeks and Romans were masters of art and architecture. Each statue tells a story."

    menu:
        "Discuss Greek mythology and its impact on literature":
            a "Greek mythology is so rich with stories. It must have influenced a lot of literature."
            dad "Absolutely. Many modern stories and characters are inspired by Greek myths. Heroes, gods, and epic adventures – they set the foundation for storytelling."
            $ SD += 1
            narrator "Amelia feels inspired by the timeless stories and their influence on culture."

        "Talk about Roman engineering and its lasting legacy":
            a "The Romans were incredible engineers. Their innovations are still impressive today."
            dad "Indeed. Roads, aqueducts, and architectural techniques – they revolutionized infrastructure and left a lasting legacy that we still benefit from."
            $ AA += 1
            narrator "Amelia appreciates the ingenuity and enduring impact of Roman engineering."

    a "It's amazing how much we can learn from these ancient civilizations."

    scene bg_british_museum_hall with fade
    narrator "They move on to the next exhibit."

    menu:
        "Start with the Ancient Egypt Exhibit":
            jump ancient_egypt_exhibit

        "Explore the Medieval Europe Section":
            jump medieval_europe_section

label medieval_europe_section:
    scene bg_medieval_europe with fade
    narrator "Amelia and her Dad explore the artifacts from Medieval Europe, including armor, manuscripts, and religious relics."
    a "This armor looks so heavy. Imagine wearing it in battle."
    dad "Medieval knights had to be incredibly strong to wear and fight in that armor. It was both protection and a status symbol."

    menu:
        "Discuss the impact of the Black Death on medieval society":
            a "The Black Death must have been terrifying. How did it change society?"
            dad "It had a massive impact. It decimated the population, leading to labor shortages and social upheaval. It also changed people's views on life and death, influencing art and literature."
            $ AA += 1
            narrator "Amelia gains a deeper understanding of the historical significance of the Black Death."

        "Talk about the role of the Church in medieval life":
            a "The Church was so influential during the medieval period. It affected every aspect of life."
            dad "Yes, the Church was a central institution. It provided spiritual guidance, education, and even political power. It shaped the culture and values of the time."
            $ SD += 1
            narrator "Amelia reflects on the pervasive influence of the Church in medieval society."

    a "History is so interconnected. Each period builds on the previous one."

    scene bg_british_museum_hall with fade
    narrator "They continue exploring the museum, discussing various exhibits and learning from each other."

    jump return_home

label return_home:
    scene bg_home_evening with fade
    play music "home_theme.mp3" loop
    narrator "After a day filled with learning and bonding, Amelia and her Dad return home."
    show amelia and dad at center with dissolve

    a "Today was amazing, Dad. Thanks for taking me to the museum."
    dad "I'm glad you enjoyed it, Amelia. It's always a pleasure to explore history with you."

    narrator "Amelia decides it's the perfect time to give her dad his birthday gift."

    menu:
        "Give him the tablet":
            a "I got you something practical for your home office. Happy birthday, Dad!"
            show gift_tablet at center with dissolve
            dad "A new tablet! This is perfect. Thank you so much, Amelia."
            $ MC += 1
            narrator "Her dad's appreciation for the thoughtful gift strengthens their bond."

        "Give him the golf clubs":
            a "I know you've been wanting to upgrade your golf clubs. Happy birthday, Dad!"
            show gift_golf_clubs at center with dissolve
            dad "New golf clubs! This is fantastic. Thank you, Amelia."
            $ SI += 1
            narrator "Her dad's excitement and gratitude make Amelia smile."

        "Give him the classic rock album":
            a "I found a rare classic rock album for your collection. Happy birthday, Dad!"
            show gift_rock_album at center with dissolve
            dad "A rare album! This is amazing. Thank you, Amelia."
            $ SD += 1
            narrator "Her dad's joy at the nostalgic gift warms Amelia's heart."

        "Give him the jazz record":
            a "I know how much you love jazz, so I got you this. Happy birthday, Dad!"
            show gift_jazz_record at center with dissolve
            dad "A jazz record! This is wonderful. Thank you, Amelia."
            $ MH += 1
            narrator "Her dad's appreciation for the thoughtful gift deepens their connection."

    narrator "They spend the evening together, enjoying each other's company and celebrating the special day."

    jump next_chapter

label next_chapter:
    scene bg_kitchen_morning with fade
    play music "morning_theme.mp3" loop
    narrator "The next day, Amelia descends to the kitchen where the morning light catches the edges of an envelope on the table."
    show amelia and dad at center with dissolve

    a "What's this? An envelope from Plymouth University..."
    dad "Open it, Amelia. I have a good feeling about this."

    narrator "Her heart leaps as she reads the confirmation of her acceptance. She's officially going to Plymouth University."

    a "I got in, Dad! I'm going to Plymouth University!"
    dad "I'm so proud of you, Amelia. I knew you could do it."

    narrator "Her dad joins her, expressing his pride and a touch of sadness as he realizes how much he will miss her. This emotional moment strengthens their bond and sets the emotional tone for her departure."

    scene bg_amelia_room_packing with fade
    narrator "As Amelia packs her belongings, her thoughts return to her dream, the choices she made, and how they might shape her future."

    a "This is it. A new chapter in my life. I'm ready for whatever comes next."

    narrator "The chapter closes with Amelia feeling a mix of excitement and nervousness, perfectly leading into the 'Call to Adventure' as she prepares to leave her familiar world behind."

    return
