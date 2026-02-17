## The CK: Amelia V2 — Gallery Screens
##
## About sub-tabs (Overview, Characters, World, Narrative),
## Character detail screen, World map, and Chapter Select.
##

################################################################################
## Data — Characters, Chapters, Locations
################################################################################

init python:

    ## ── Chapter completion tracking ─────────────────────────────────────
    ## A chapter is unlocked when the *previous* chapter has been completed.
    ## Chapter 1 is always unlocked.

    ## ── Character Data ──────────────────────────────────────────────────
    ## (tag, display_name, role, short bio, portrait_image_or_None)
    ## portrait_image should match an image tag or path in images/characters/

    _characters = [
        ("amelia", "Amelia James", "Protagonist",
         "18, BSc Psychology at Plymouth. Curious, empathetic, conflict-avoidant. Her year maps to the alchemical Magnum Opus — from Nigredo's darkness through Albedo's reflection to Rubedo's wholeness.",
         "images/characters/amelia/amelia_anchor_image.png"),

        ("ella", "Ella Chen", "Childhood Best Friend",
         "18, English Lit at Queen Mary London. The golden thread to the ordinary world. She and Amelia have been friends since Year 3. Their friendship will be tested by distance.",
         None),

        ("lucas", "Lucas Adeyemi", "The Quiet Thinker",
         "19, Psychology. Reads Jung, quotes Fanon, listens more than he speaks. He sees things in Amelia that she hasn't noticed yet. Represents the Animus archetype.",
         None),

        ("zara", "Zara Okafor", "The Red Lion",
         "20, Psychology with Criminology. Fierce, loyal, funny. Grew up in Tottenham, carries lived experience of racism with fury and grace. She fights — for herself, for others.",
         None),

        ("raj", "Raj Sharma", "The Heart",
         "21, Psychology. Emotional centre of any group. When people are falling apart, Raj cooks. Biryani fixes everything — or at least makes it bearable.",
         None),

        ("sarah", "Sarah Whitmore", "The Mirror",
         "18, Psychology, rural Devon. Quiet, gentle, struggling beneath the surface. Her story is the game's biggest branch point. Amelia will have to decide what she's willing to do.",
         None),

        ("liz", "Liz Torres", "The Roommate",
         "18, Marine Biology, Cardiff. Cheerful, chaotic, perpetually late. Amelia's first friend at Plymouth and the one who drags her to the Student Union on the first night.",
         None),

        ("maya", "Maya Patel", "The Mystic",
         "20, Philosophy with Psychology, Bristol. Crystals, tarot, meditation at dawn. She's either deeply wise or slightly unhinged — possibly both. Represents Sulphur.",
         None),

        ("tasha", "Tasha Reynolds", "The Shadow",
         "20, Psychology, Surrey. Jungian Shadow incarnate. Insecure, sharp-tongued, miserable at home. She can change if Amelia chooses compassion over confrontation.",
         None),

        ("sophia", "Sophia Langford", "The White Queen",
         "19, Psychology, Oxford family. Brilliant, precise, lonely beneath the polish. Academic rival who might become an unexpected ally.",
         None),

        ("hawthorne", "Prof. Arthur Hawthorne", "Mentor — Salt",
         "58, Head of Psychology. Rational, precise, Earl Grey in a china cup. His office has floor-to-ceiling books and a Caravaggio print. Unlocked through academic excellence.",
         None),

        ("simmons", "Dr. Nadia Simmons", "Mentor — Mercury",
         "38, Lecturer in Positive Psychology. Warm, nurturing, believes in the science of kindness. Her office has plants everywhere and a small fountain. Unlocked through compassion.",
         None),

        ("elena", "Elena Trevorran", "Mentor — The Soror Mystica",
         "45, Cornish pellar. Keeper of old knowledge, guardian of the fogou. She appears when you're ready. Unlocked through the occult knowledge path.",
         None),

        ("david", "David James", "Amelia's Father",
         "46, IT support, Jamaican heritage. Quiet, steady, fixes things with his hands. Love expressed through actions: packed lunches, lifts to the station, a hug at the door.",
         None),

        ("grace", "Grace James", "Amelia's Mother",
         "44, Teaching assistant, Jamaican heritage. Warm, talkative, sends care packages. She's the one who asks 'Are you eating properly?' three times a week.",
         None),

        ("lily", "Lily James", "Amelia's Cousin",
         "16, still at school. Looks up to Amelia. Questioning her sexuality and trying to figure out who she is. Amelia's letters to her are some of the most honest writing in the game.",
         None),
    ]

    ## ── Chapter Data ────────────────────────────────────────────────────
    ## (number, label, hero_journey_name, subtitle, month, phase_colour)

    _chapters = [
        (1,  "chapter_1",  "The Ordinary World",
         "Final days before departure. London is golden, nostalgic — and about to be left behind.",
         "Late September", "#D4A574"),

        (2,  "chapter_2",  "The Call to Adventure",
         "The journey to Plymouth. A train, a new city, and the anxious excitement of everything beginning.",
         "Early October", "#D4A574"),

        (3,  "chapter_3",  "Refusal of the Call",
         "First semester struggles. The work is hard, the people are strange, and home feels very far away.",
         "October–November", "#D4A574"),

        (4,  "chapter_4",  "Meeting the Mentor",
         "Mentor assignment and a first trip to Cornwall. Something old and strange is waking up.",
         "November", "#A8C0D4"),

        (5,  "chapter_5",  "Crossing the Threshold",
         "Full immersion. Deepening connections, finding rhythm. Plymouth starts to feel like it could be home.",
         "November–December", "#A8C0D4"),

        (6,  "chapter_6",  "Tests, Allies & Enemies",
         "Tension, conflict, bonding. Christmas break reveals how much has changed. The Shadow appears.",
         "December–January", "#A8C0D4"),

        (7,  "chapter_7",  "The Approach",
         "Return after Christmas. Something is building. Cornwall calls again, deeper this time.",
         "January–February", "#A8C0D4"),

        (8,  "chapter_8",  "The Ordeal",
         "The supreme test. Sarah's crisis. A phone call in the night that changes everything.",
         "February", "#DAA520"),

        (9,  "chapter_9",  "The Reward",
         "Aftermath. The group regathers. Fragile hope. Something has been earned through pain.",
         "March", "#DAA520"),

        (10, "chapter_10", "The Road Back",
         "Easter at home. London is the same; Amelia is not. Bittersweet clarity.",
         "April", "#C04040"),

        (11, "chapter_11", "The Resurrection",
         "Final test. Synthesis. The fogou. Everything Amelia has learned is put to the ultimate test.",
         "May", "#C04040"),

        (12, "chapter_12", "Return with the Elixir",
         "Seven possible endings. Summer term, final weeks. Who has Amelia become?",
         "June", "#C04040"),
    ]

    ## ── World Map — Region & Location Data ─────────────────────────────
    ## Region markers on the map (id, label, pixel_x, pixel_y on 805×680 map)
    _map_regions = [
        ("london",   "LONDON",   656, 244),
        ("plymouth", "PLYMOUTH", 280, 393),
        ("cornwall", "CORNWALL", 193, 395),
    ]

    ## Region info with nested locations
    _region_data = {
        "london": {
            "name": "London",
            "summary": "South-east London. Bromley, Lewisham, the edges where the city thins into something quieter. This is where Amelia began — and where she'll return, changed.",
            "locations": [
                ("James Family Home",
                 "A terraced house where Amelia grew up. The kitchen smells of ackee and saltfish. The walls hold sixteen years of photographs."),
                ("Bromley Park",
                 "The park bench where Amelia reads. It faces west, catches the evening light. This is where the story begins."),
                ("Mr. Osei's Bookshop",
                 "A cramped, overstuffed bookshop. Mr. Osei knows every book by touch. Here, Amelia finds the Paracelsus text that opens the occult knowledge path."),
            ],
        },
        "plymouth": {
            "name": "Plymouth",
            "summary": "A port city where the moors meet the sea. Brutalist university buildings, the Hoe at sunset, the SU at 2am. This is where Amelia becomes herself.",
            "locations": [
                ("University of Plymouth",
                 "The Psychology building, the five-floor library, the lecture theatres where everything changes. Concrete and green quads."),
                ("Plymouth Hoe",
                 "Smeaton's Tower, Drake's statue, the sea stretching to the horizon. Key emotional scenes happen here — at dawn, at dusk, in the rain."),
                ("Student Union",
                 "Karaoke nights, cheap pints, friendships forged at 2am. Where Amelia's social world expands — and where tensions boil over."),
                ("Halls of Residence",
                 "Amelia's room: a single bed, a desk, a window facing the city. The communal kitchen where Raj cooks and arguments happen."),
            ],
        },
        "cornwall": {
            "name": "Cornwall",
            "summary": "The ancient peninsula. Stone circles, holy wells, the fogou. Where the veil between the rational and the numinous wears thin.",
            "locations": [
                ("Bodmin Moor",
                 "Wild ponies, granite tors, overwhelming stars. The Nigredo landscape — raw, ancient, stripped bare. At night the darkness is absolute."),
                ("Mên-an-Tol",
                 "The holed stone. Three thousand years old. Elena calls it 'the athanor opening' — the entrance to the alchemical furnace."),
                ("Merry Maidens",
                 "A stone circle near Penzance. Nineteen stones in a perfect ring. The legend says they were girls turned to stone for dancing on the Sabbath."),
                ("Madron Holy Well",
                 "Hidden in woods above Penzance. Clootie rags hang from branches. The water is cold and clear. Elena calls it 'the albedo pool'."),
                ("The Fogou",
                 "An underground chamber. Iron Age, maybe older. Cool, dark, utterly silent. The final Elena path scene takes place here. The belly of the whale."),
                ("Tintagel",
                 "Arthurian ruins on the cliff edge. Wind, spray, legend layered on legend. Maya's path leads here. The bridge between worlds."),
                ("Eden Project",
                 "Biome domes in a reclaimed quarry. Dr. Simmons brings the group here. Growth from devastation — the whole place is a metaphor."),
            ],
        },
    }


################################################################################
## Chapter completion — persistent tracking
################################################################################

default persistent.chapters_completed = set()

init python:
    def complete_chapter(ch_num):
        """Call at the end of each chapter to unlock the next."""
        if persistent.chapters_completed is None:
            persistent.chapters_completed = set()
        persistent.chapters_completed.add(ch_num)
        renpy.save_persistent()

    def is_chapter_unlocked(ch_num):
        """Chapter 1 always unlocked; others need previous completed."""
        if ch_num <= 1:
            return True
        if persistent.chapters_completed is None:
            return False
        return (ch_num - 1) in persistent.chapters_completed


################################################################################
## Language restore — reset English data when switching back from translation
################################################################################

translate None python:

    _characters = [
        ("amelia", "Amelia James", "Protagonist",
         "18, BSc Psychology at Plymouth. Curious, empathetic, conflict-avoidant. Her year maps to the alchemical Magnum Opus — from Nigredo's darkness through Albedo's reflection to Rubedo's wholeness.",
         "images/characters/amelia/amelia_anchor_image.png"),
        ("ella", "Ella Chen", "Childhood Best Friend",
         "18, English Lit at Queen Mary London. The golden thread to the ordinary world. She and Amelia have been friends since Year 3. Their friendship will be tested by distance.",
         None),
        ("lucas", "Lucas Adeyemi", "The Quiet Thinker",
         "19, Psychology. Reads Jung, quotes Fanon, listens more than he speaks. He sees things in Amelia that she hasn't noticed yet. Represents the Animus archetype.",
         None),
        ("zara", "Zara Okafor", "The Red Lion",
         "20, Psychology with Criminology. Fierce, loyal, funny. Grew up in Tottenham, carries lived experience of racism with fury and grace. She fights — for herself, for others.",
         None),
        ("raj", "Raj Sharma", "The Heart",
         "21, Psychology. Emotional centre of any group. When people are falling apart, Raj cooks. Biryani fixes everything — or at least makes it bearable.",
         None),
        ("sarah", "Sarah Whitmore", "The Mirror",
         "18, Psychology, rural Devon. Quiet, gentle, struggling beneath the surface. Her story is the game's biggest branch point. Amelia will have to decide what she's willing to do.",
         None),
        ("liz", "Liz Torres", "The Roommate",
         "18, Marine Biology, Cardiff. Cheerful, chaotic, perpetually late. Amelia's first friend at Plymouth and the one who drags her to the Student Union on the first night.",
         None),
        ("maya", "Maya Patel", "The Mystic",
         "20, Philosophy with Psychology, Bristol. Crystals, tarot, meditation at dawn. She's either deeply wise or slightly unhinged — possibly both. Represents Sulphur.",
         None),
        ("tasha", "Tasha Reynolds", "The Shadow",
         "20, Psychology, Surrey. Jungian Shadow incarnate. Insecure, sharp-tongued, miserable at home. She can change if Amelia chooses compassion over confrontation.",
         None),
        ("sophia", "Sophia Langford", "The White Queen",
         "19, Psychology, Oxford family. Brilliant, precise, lonely beneath the polish. Academic rival who might become an unexpected ally.",
         None),
        ("hawthorne", "Prof. Arthur Hawthorne", "Mentor — Salt",
         "58, Head of Psychology. Rational, precise, Earl Grey in a china cup. His office has floor-to-ceiling books and a Caravaggio print. Unlocked through academic excellence.",
         None),
        ("simmons", "Dr. Nadia Simmons", "Mentor — Mercury",
         "38, Lecturer in Positive Psychology. Warm, nurturing, believes in the science of kindness. Her office has plants everywhere and a small fountain. Unlocked through compassion.",
         None),
        ("elena", "Elena Trevorran", "Mentor — The Soror Mystica",
         "45, Cornish pellar. Keeper of old knowledge, guardian of the fogou. She appears when you're ready. Unlocked through the occult knowledge path.",
         None),
        ("david", "David James", "Amelia's Father",
         "46, IT support, Jamaican heritage. Quiet, steady, fixes things with his hands. Love expressed through actions: packed lunches, lifts to the station, a hug at the door.",
         None),
        ("grace", "Grace James", "Amelia's Mother",
         "44, Teaching assistant, Jamaican heritage. Warm, talkative, sends care packages. She's the one who asks 'Are you eating properly?' three times a week.",
         None),
        ("lily", "Lily James", "Amelia's Cousin",
         "16, still at school. Looks up to Amelia. Questioning her sexuality and trying to figure out who she is. Amelia's letters to her are some of the most honest writing in the game.",
         None),
    ]

    _chapters = [
        (1,  "chapter_1",  "The Ordinary World",
         "Final days before departure. London is golden, nostalgic — and about to be left behind.",
         "Late September", "#D4A574"),
        (2,  "chapter_2",  "The Call to Adventure",
         "The journey to Plymouth. A train, a new city, and the anxious excitement of everything beginning.",
         "Early October", "#D4A574"),
        (3,  "chapter_3",  "Refusal of the Call",
         "First semester struggles. The work is hard, the people are strange, and home feels very far away.",
         "October–November", "#D4A574"),
        (4,  "chapter_4",  "Meeting the Mentor",
         "Mentor assignment and a first trip to Cornwall. Something old and strange is waking up.",
         "November", "#A8C0D4"),
        (5,  "chapter_5",  "Crossing the Threshold",
         "Full immersion. Deepening connections, finding rhythm. Plymouth starts to feel like it could be home.",
         "November–December", "#A8C0D4"),
        (6,  "chapter_6",  "Tests, Allies & Enemies",
         "Tension, conflict, bonding. Christmas break reveals how much has changed. The Shadow appears.",
         "December–January", "#A8C0D4"),
        (7,  "chapter_7",  "The Approach",
         "Return after Christmas. Something is building. Cornwall calls again, deeper this time.",
         "January–February", "#A8C0D4"),
        (8,  "chapter_8",  "The Ordeal",
         "The supreme test. Sarah's crisis. A phone call in the night that changes everything.",
         "February", "#DAA520"),
        (9,  "chapter_9",  "The Reward",
         "Aftermath. The group regathers. Fragile hope. Something has been earned through pain.",
         "March", "#DAA520"),
        (10, "chapter_10", "The Road Back",
         "Easter at home. London is the same; Amelia is not. Bittersweet clarity.",
         "April", "#C04040"),
        (11, "chapter_11", "The Resurrection",
         "Final test. Synthesis. The fogou. Everything Amelia has learned is put to the ultimate test.",
         "May", "#C04040"),
        (12, "chapter_12", "Return with the Elixir",
         "Seven possible endings. Summer term, final weeks. Who has Amelia become?",
         "June", "#C04040"),
    ]

    _region_data = {
        "london": {
            "name": "London",
            "summary": "South-east London. Bromley, Lewisham, the edges where the city thins into something quieter. This is where Amelia began — and where she'll return, changed.",
            "locations": [
                ("James Family Home",
                 "A terraced house where Amelia grew up. The kitchen smells of ackee and saltfish. The walls hold sixteen years of photographs."),
                ("Bromley Park",
                 "The park bench where Amelia reads. It faces west, catches the evening light. This is where the story begins."),
                ("Mr. Osei's Bookshop",
                 "A cramped, overstuffed bookshop. Mr. Osei knows every book by touch. Here, Amelia finds the Paracelsus text that opens the occult knowledge path."),
            ],
        },
        "plymouth": {
            "name": "Plymouth",
            "summary": "A port city where the moors meet the sea. Brutalist university buildings, the Hoe at sunset, the SU at 2am. This is where Amelia becomes herself.",
            "locations": [
                ("University of Plymouth",
                 "The Psychology building, the five-floor library, the lecture theatres where everything changes. Concrete and green quads."),
                ("Plymouth Hoe",
                 "Smeaton's Tower, Drake's statue, the sea stretching to the horizon. Key emotional scenes happen here — at dawn, at dusk, in the rain."),
                ("Student Union",
                 "Karaoke nights, cheap pints, friendships forged at 2am. Where Amelia's social world expands — and where tensions boil over."),
                ("Halls of Residence",
                 "Amelia's room: a single bed, a desk, a window facing the city. The communal kitchen where Raj cooks and arguments happen."),
            ],
        },
        "cornwall": {
            "name": "Cornwall",
            "summary": "The ancient peninsula. Stone circles, holy wells, the fogou. Where the veil between the rational and the numinous wears thin.",
            "locations": [
                ("Bodmin Moor",
                 "Wild ponies, granite tors, overwhelming stars. The Nigredo landscape — raw, ancient, stripped bare. At night the darkness is absolute."),
                ("Mên-an-Tol",
                 "The holed stone. Three thousand years old. Elena calls it 'the athanor opening' — the entrance to the alchemical furnace."),
                ("Merry Maidens",
                 "A stone circle near Penzance. Nineteen stones in a perfect ring. The legend says they were girls turned to stone for dancing on the Sabbath."),
                ("Madron Holy Well",
                 "Hidden in woods above Penzance. Clootie rags hang from branches. The water is cold and clear. Elena calls it 'the albedo pool'."),
                ("The Fogou",
                 "An underground chamber. Iron Age, maybe older. Cool, dark, utterly silent. The final Elena path scene takes place here. The belly of the whale."),
                ("Tintagel",
                 "Arthurian ruins on the cliff edge. Wind, spray, legend layered on legend. Maya's path leads here. The bridge between worlds."),
                ("Eden Project",
                 "Biome domes in a reclaimed quarry. Dr. Simmons brings the group here. Growth from devastation — the whole place is a metaphor."),
            ],
        },
    }


################################################################################
## About Screen — Tabbed (Overview · Characters · World · Narrative)
################################################################################

screen about():
    tag menu
    default about_tab = "overview"
    default about_video = _pick_video(about_videos)
    ## World tab state (must live here — SetScreenVariable targets the shown screen)
    default selected_region = None
    default selected_loc_idx = -1
    use game_menu(_("About"), video_bg=about_video):

        vbox:
            spacing 0

            ## ── Tab bar ─────────────────────────────────────────────────
            hbox:
                spacing 30
                xalign 0.5

                for _tab_id, _tab_label in [("overview", _("Overview")), ("characters", _("Characters")), ("world", _("World")), ("narrative", _("Narrative"))]:
                    textbutton _tab_label:
                        style "about_tab_btn"
                        action SetScreenVariable("about_tab", _tab_id)
                        selected (about_tab == _tab_id)

            ## Gold divider
            null height 10
            frame:
                xalign 0.5
                xsize 500
                ysize 1
                background Solid("#D4A57444")
            null height 15

            ## ── Tab content ─────────────────────────────────────────────
            if about_tab == "overview":
                use about_overview
            elif about_tab == "characters":
                use about_characters
            elif about_tab == "world":
                use about_world(selected_region, selected_loc_idx)
            elif about_tab == "narrative":
                use about_narrative


style about_tab_btn is button:
    background None
    idle_background None
    hover_background None
    activate_background None
    selected_background None
    selected_idle_background None
    selected_hover_background None
    selected_activate_background None
    insensitive_background None
    selected_insensitive_background None
    padding (0, 0, 0, 0)
    margin (0, 0, 0, 0)

style about_tab_btn_text:
    size 20
    color "#999999"
    hover_color "#D4A574"
    selected_color "#D4A574"
    kerning 3.0
    outlines [(1, "#00000088", 0, 0)]


################################################################################
## About — Overview Tab
################################################################################

screen about_overview():
    viewport:
        mousewheel True
        draggable True
        ysize (config.screen_height - 300)

        vbox:
            spacing 15
            style_prefix "about"

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            if gui.about:
                text "[gui.about!t]\n"

            text _("{b}Art & Music{/b}\nDancing Salamanders — {a=https://dancingsalamanders.com}dancingsalamanders.com{/a}\n")
            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


################################################################################
## About — Characters Tab (portrait grid)
################################################################################

screen about_characters():
    viewport:
        mousewheel True
        draggable True
        ysize (config.screen_height - 300)
        xfill True

        vbox:
            spacing 20
            xfill True

            text _("{b}Cast of Characters{/b}"):
                color "#D4A574"
                size 30
                xalign 0.5

            null height 5

            ## Character grid — 4 columns
            grid 4 4:
                xalign 0.5
                spacing 20

                for _i, (_tag, _name, _role, _bio, _portrait) in enumerate(_characters):
                    button:
                        style "char_card"
                        action Show("character_detail", char_index=_i)

                        vbox:
                            spacing 6
                            xalign 0.5

                            ## Portrait (or placeholder circle)
                            if _portrait and renpy.loadable(_portrait):
                                add _portrait:
                                    size (120, 120)
                                    fit "cover"
                                    xalign 0.5
                            else:
                                frame:
                                    xalign 0.5
                                    xsize 120
                                    ysize 120
                                    background Solid("#1A1410")

                                    text _tag[0].upper():
                                        size 48
                                        color "#D4A574"
                                        xalign 0.5
                                        yalign 0.5

                            text _name:
                                size 16
                                color "#CCCCCC"
                                xalign 0.5
                                text_align 0.5

                            text _role:
                                size 12
                                color "#999999"
                                xalign 0.5
                                text_align 0.5


style char_card:
    xsize 260
    ysize 210
    background Solid("#0A0A0A88")
    hover_background Solid("#D4A57422")
    padding (10, 10, 10, 10)


################################################################################
## Character Detail Screen (modal overlay)
################################################################################

screen character_detail(char_index=0):
    modal True
    zorder 150

    add Solid("#00000099")

    $ _cd = _characters[char_index]
    $ _cd_tag, _cd_name, _cd_role, _cd_bio, _cd_portrait = _cd

    frame:
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 500
        background Solid("#1A1410EE")
        padding (40, 30, 40, 30)

        vbox:
            spacing 15

            hbox:
                spacing 25

                ## Portrait
                if _cd_portrait and renpy.loadable(_cd_portrait):
                    add _cd_portrait:
                        size (180, 220)
                        fit "cover"
                        yalign 0.0
                else:
                    frame:
                        xsize 180
                        ysize 220
                        background Solid("#2A201A")

                        text _cd_tag[0].upper():
                            size 72
                            color "#D4A574"
                            xalign 0.5
                            yalign 0.5

                ## Info
                vbox:
                    spacing 8
                    xfill True

                    text _cd_name:
                        size 36
                        color "#D4A574"
                        bold True

                    text _cd_role:
                        size 20
                        color "#E8C8A0"

                    null height 5

                    text _cd_bio:
                        size 18
                        color "#CCCCCC"
                        text_align 0.0

            ## Navigation + close
            hbox:
                xalign 0.5
                spacing 30

                if char_index > 0:
                    textbutton _("< Previous"):
                        style "about_tab_btn"
                        action SetScreenVariable("char_index", char_index - 1)

                textbutton _("Close"):
                    style "gm_return_button"
                    action Hide("character_detail")

                if char_index < len(_characters) - 1:
                    textbutton _("Next >"):
                        style "about_tab_btn"
                        action SetScreenVariable("char_index", char_index + 1)


################################################################################
## About — World Tab (real map with region markers)
################################################################################

screen about_world(selected_region, selected_loc_idx):
    ## Two-level map: overview → zoomed region
    ## NOTE: selected_region & selected_loc_idx are defaulted in about() screen
    ## because SetScreenVariable targets the *shown* screen, not a use'd sub-screen.

    if not selected_region:
        ## ── LEVEL 1: Overview map ───────────────────────────────────────
        hbox:
            spacing 0
            ysize (config.screen_height - 300)

            ## Map image (2/3)
            frame:
                xsize int(1220 * 0.66)
                yfill True
                background Solid("#0D1117")
                padding (0, 0, 0, 0)

                fixed:
                    xsize 805
                    ysize 680
                    align (0.5, 0.5)

                    if renpy.loadable("images/ui/world_map.png"):
                        add "images/ui/world_map.png":
                            pos (0, 0)
                    else:
                        add Solid("#0D1117")

            ## Region list panel (1/3)
            frame:
                xsize int(1220 * 0.34)
                yfill True
                background Solid("#0A0A0ACC")
                padding (25, 30, 25, 30)

                vbox:
                    spacing 20
                    yalign 0.5
                    xfill True

                    text _("Amelia's World"):
                        size 26
                        color "#D4A574"
                        xalign 0.5
                        bold True

                    text _("Click a region to explore the places in the story."):
                        size 15
                        color "#999999"
                        xalign 0.5
                        text_align 0.5

                    null height 10

                    for _rid, _rname in [("london", _("London")), ("plymouth", _("Plymouth")), ("cornwall", _("Cornwall"))]:
                        textbutton _rname:
                            style "about_tab_btn"
                            xalign 0.5
                            text_size 24
                            action SetScreenVariable("selected_region", _rid)

    else:
        ## ── LEVEL 2: Zoomed region map ──────────────────────────────────
        $ _rd = _region_data[selected_region]
        $ _map_file = "images/ui/map_" + selected_region + ".png"

        hbox:
            spacing 0
            ysize (config.screen_height - 300)

            ## Zoomed map (2/3)
            frame:
                xsize int(1220 * 0.66)
                yfill True
                background Solid("#0D1117")
                padding (0, 0, 0, 0)

                fixed:
                    xsize 805
                    ysize 680
                    align (0.5, 0.5)

                    if renpy.loadable(_map_file):
                        add _map_file:
                            pos (0, 0)
                    else:
                        add Solid("#0D1117")

            ## Info panel (1/3)
            frame:
                xsize int(1220 * 0.34)
                yfill True
                background Solid("#0A0A0ACC")
                padding (20, 20, 20, 20)

                viewport:
                    mousewheel True
                    draggable True
                    xfill True

                    vbox:
                        spacing 12
                        xfill True

                        ## Back link
                        textbutton _("< Back to overview"):
                            style "about_tab_btn"
                            text_size 14
                            action [SetScreenVariable("selected_region", None),
                                    SetScreenVariable("selected_loc_idx", -1)]

                        null height 5

                        ## Region header
                        text _rd["name"]:
                            size 28
                            color "#D4A574"
                            bold True

                        text _rd["summary"]:
                            size 15
                            color "#CCCCCC"
                            text_align 0.0

                        ## Gold divider
                        null height 5
                        frame:
                            xsize 200
                            ysize 1
                            background Solid("#D4A57444")
                        null height 5

                        ## Location list
                        text _("Locations"):
                            size 16
                            color "#999999"
                            bold True

                        for _li, (_loc_name, _loc_desc) in enumerate(_rd["locations"]):
                            $ _loc_bg = Solid("#D4A57411") if selected_loc_idx == _li else Solid("#00000000")
                            $ _loc_name_col = "#E8C8A0" if selected_loc_idx == _li else "#CCCCCC"
                            textbutton _loc_name:
                                style "about_tab_btn"
                                text_size 17
                                text_color _loc_name_col
                                text_bold True
                                action SetScreenVariable("selected_loc_idx", _li)

                            if selected_loc_idx == _li:
                                text _loc_desc:
                                    size 14
                                    color "#AAAAAA"
                                    text_align 0.0


################################################################################
## About — Narrative Tab (Hero's Journey overview)
################################################################################

screen about_narrative():
    viewport:
        mousewheel True
        draggable True
        ysize (config.screen_height - 300)
        xfill True

        vbox:
            spacing 20
            xfill True

            text _("{b}The Hero's Journey{/b}"):
                size 30
                color "#D4A574"
                xalign 0.5

            text _("Amelia's story follows the twelve stages of Joseph Campbell's Monomyth — the universal pattern that underpins every transformative journey, from Odysseus to Luke Skywalker to a first-year psychology student from south-east London."):
                size 18
                color "#CCCCCC"
                xalign 0.5
                text_align 0.5
                xsize 1000

            null height 10

            ## Journey stages
            for _ch_num, _ch_label, _ch_name, _ch_desc, _ch_month, _ch_colour in _chapters:
                hbox:
                    spacing 15
                    xalign 0.5
                    xsize 1000

                    ## Stage number (coloured dot)
                    frame:
                        xsize 36
                        ysize 36
                        yalign 0.0
                        background Solid(_ch_colour)

                        text str(_ch_num):
                            size 18
                            color "#0A0A0A"
                            xalign 0.5
                            yalign 0.5
                            bold True

                    vbox:
                        spacing 3

                        text "{b}[_ch_name]{/b}":
                            size 20
                            color _ch_colour

                        text _ch_month:
                            size 14
                            color "#999999"

                        text _ch_desc:
                            size 16
                            color "#CCCCCC"

                null height 5

            null height 15

            text _("Beneath the Hero's Journey lies a second structure: the four stages of alchemical transformation — {b}Nigredo{/b} (blackening), {b}Albedo{/b} (whitening), {b}Citrinitas{/b} (yellowing), and {b}Rubedo{/b} (reddening). The colours of the game shift with Amelia's inner work."):
                size 16
                color "#999999"
                xalign 0.5
                text_align 0.5
                xsize 1000


################################################################################
## Chapter Select Screen (from main menu)
################################################################################

screen chapter_select():
    tag menu

    add Solid("#0A0A0A")

    ## Reuse main menu video if available
    if _mm_movie:
        add _mm_movie

    add Solid("#00000066")

    ## Title
    vbox:
        xalign 0.5
        ypos 25

        text _("SELECT CHAPTER"):
            xalign 0.5
            size 42
            color "#D4A574"
            kerning 8.0
            outlines [(1, "#00000088", 0, 0)]

        null height 6
        frame:
            xalign 0.5
            xsize 80
            ysize 2
            background Solid("#D4A574")

    ## Chapter grid — 4 columns × 3 rows
    frame:
        xalign 0.5
        yalign 0.5
        yoffset 20
        background None

        grid 4 3:
            spacing 20
            xalign 0.5

            for _ch_num, _ch_label, _ch_name, _ch_desc, _ch_month, _ch_colour in _chapters:
                $ _unlocked = is_chapter_unlocked(_ch_num)

                button:
                    style "chapter_card"
                    if _unlocked:
                        action Start(_ch_label)
                    else:
                        action NullAction()

                    vbox:
                        spacing 6
                        xalign 0.5

                        ## Chapter image placeholder
                        frame:
                            xalign 0.5
                            xsize 200
                            ysize 112
                            if _unlocked:
                                background Solid(_ch_colour + "44")
                            else:
                                background Solid("#1A1A1A")

                            ## Chapter number overlay
                            text str(_ch_num):
                                size 36
                                xalign 0.5
                                yalign 0.5
                                bold True
                                if _unlocked:
                                    color _ch_colour
                                else:
                                    color "#333333"

                        ## Chapter name
                        text _ch_name:
                            size 14
                            xalign 0.5
                            text_align 0.5
                            if _unlocked:
                                color "#CCCCCC"
                            else:
                                color "#444444"

                        ## Month
                        text _ch_month:
                            size 11
                            xalign 0.5
                            if _unlocked:
                                color "#999999"
                            else:
                                color "#333333"

    ## Footer
    hbox:
        xalign 0.5
        yalign 1.0
        yoffset -25
        spacing 40

        textbutton _("Return"):
            action Return()
            style "gm_return_button"

    ## Use music player on chapter select too
    use music_player


style chapter_card:
    xsize 240
    ysize 200
    background Solid("#0A0A0A88")
    hover_background Solid("#D4A57422")
    padding (15, 12, 15, 12)
    insensitive_background Solid("#0A0A0A44")


## ── About Styles ────────────────────────────────────────────────────────────

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size
    color "#D4A574"

style about_text:
    color "#CCCCCC"
