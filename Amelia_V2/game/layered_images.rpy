## The CK: Amelia V2 — Layered Image Declarations
##
## Defines `layeredimage` blocks for every character. Currently uses
## placeholder coloured rectangles. When real sprites are added to
## game/images/characters/, update the image paths below.
##
## Usage in scripts:
##   show amelia happy
##   show amelia sad casual_autumn
##   show sarah withdrawn late_c
##   show ella fierce headwrap
##
## The `layeredimage` system lets you combine outfit + expression
## in a single `show` statement. The first attribute in each group
## marked `default` is shown if no attribute is specified.

init -1:

    ############################################################################
    ## HELPER — Placeholder sprite generator
    ############################################################################

    python:
        def _sprite_placeholder(name, expression, color="#D4A574"):
            """Generates a placeholder sprite displayable for layered images."""
            return Composite(
                (700, 1400),
                (0, 0), Solid(color + "22"),
                (0, 0), Text(
                    "{size=24}{color=#FFFFFF66}[ PLACEHOLDER ]\n\n{size=32}{color=#FFFFFFAA}" + name + "\n{size=26}{color=#FFFFFF88}" + expression,
                    text_align=0.5,
                    xalign=0.5,
                    yalign=0.7,
                )
            )

    ############################################################################
    ## AMELIA JAMES — Protagonist
    ############################################################################
    ## 12 expressions × 6 outfits
    ## show amelia [expression] [outfit]

    layeredimage amelia:
        always:
            Solid("#D4A57411", xysize=(700, 1400))

        group outfit:
            attribute casual_autumn default:
                _sprite_placeholder("Amelia", "casual autumn", "#D4A574")
            attribute going_out:
                _sprite_placeholder("Amelia", "going out", "#D4A574")
            attribute home_tired:
                _sprite_placeholder("Amelia", "home tired", "#D4A574")
            attribute academic:
                _sprite_placeholder("Amelia", "academic", "#D4A574")
            attribute crisis:
                _sprite_placeholder("Amelia", "crisis", "#D4A574")
            attribute summer:
                _sprite_placeholder("Amelia", "summer", "#D4A574")

        group expression:
            attribute neutral default:
                _sprite_placeholder("", "neutral", "#00000000")
            attribute happy:
                _sprite_placeholder("", "happy", "#00000000")
            attribute sad:
                _sprite_placeholder("", "sad", "#00000000")
            attribute angry:
                _sprite_placeholder("", "angry", "#00000000")
            attribute surprised:
                _sprite_placeholder("", "surprised", "#00000000")
            attribute thinking:
                _sprite_placeholder("", "thinking", "#00000000")
            attribute worried:
                _sprite_placeholder("", "worried", "#00000000")
            attribute laughing:
                _sprite_placeholder("", "laughing", "#00000000")
            attribute anxious:
                _sprite_placeholder("", "anxious", "#00000000")
            attribute determined:
                _sprite_placeholder("", "determined", "#00000000")
            attribute tearful:
                _sprite_placeholder("", "tearful", "#00000000")
            attribute peaceful:
                _sprite_placeholder("", "peaceful", "#00000000")

    ############################################################################
    ## SARAH WHITMORE
    ############################################################################
    ## 9 expressions × 4 outfits

    layeredimage sarah:
        always:
            Solid("#A8B5C522", xysize=(700, 1400))

        group outfit:
            attribute early_a default:
                _sprite_placeholder("Sarah", "early A", "#A8B5C5")
            attribute early_b:
                _sprite_placeholder("Sarah", "early B", "#A8B5C5")
            attribute late_c:
                _sprite_placeholder("Sarah", "late C", "#8A9AAA")
            attribute recovery_d:
                _sprite_placeholder("Sarah", "recovery D", "#B8C5D5")

        group expression:
            attribute neutral default:
                _sprite_placeholder("", "neutral", "#00000000")
            attribute happy:
                _sprite_placeholder("", "happy", "#00000000")
            attribute sad:
                _sprite_placeholder("", "sad", "#00000000")
            attribute surprised:
                _sprite_placeholder("", "surprised", "#00000000")
            attribute thinking:
                _sprite_placeholder("", "thinking", "#00000000")
            attribute worried:
                _sprite_placeholder("", "worried", "#00000000")
            attribute withdrawn:
                _sprite_placeholder("", "withdrawn", "#00000000")
            attribute present:
                _sprite_placeholder("", "present", "#00000000")
            attribute flat:
                _sprite_placeholder("", "flat", "#00000000")

    ############################################################################
    ## ELLA BLACKWOOD
    ############################################################################
    ## 8 expressions × 3 outfit variants

    layeredimage ella:
        always:
            Solid("#FFD70022", xysize=(700, 1400))

        group outfit:
            attribute casual_london default:
                _sprite_placeholder("Ella", "casual london", "#FFD700")
            attribute going_out:
                _sprite_placeholder("Ella", "going out", "#FFD700")
            attribute headwrap:
                _sprite_placeholder("Ella", "headwrap", "#FFD700")

        group expression:
            attribute neutral default:
                _sprite_placeholder("", "neutral", "#00000000")
            attribute happy:
                _sprite_placeholder("", "happy", "#00000000")
            attribute sad:
                _sprite_placeholder("", "sad", "#00000000")
            attribute fierce:
                _sprite_placeholder("", "fierce", "#00000000")
            attribute worried:
                _sprite_placeholder("", "worried", "#00000000")
            attribute laughing:
                _sprite_placeholder("", "laughing", "#00000000")
            attribute exasperated:
                _sprite_placeholder("", "exasperated", "#00000000")
            attribute hurt:
                _sprite_placeholder("", "hurt", "#00000000")

    ############################################################################
    ## LUCAS HOLLOWAY
    ############################################################################
    ## 8 expressions × 2 outfits

    layeredimage lucas:
        always:
            Solid("#7BA7BC22", xysize=(700, 1400))

        group outfit:
            attribute casual default:
                _sprite_placeholder("Lucas", "casual", "#7BA7BC")
            attribute academic:
                _sprite_placeholder("Lucas", "academic", "#7BA7BC")

        group expression:
            attribute neutral default:
                _sprite_placeholder("", "neutral", "#00000000")
            attribute happy:
                _sprite_placeholder("", "happy", "#00000000")
            attribute sad:
                _sprite_placeholder("", "sad", "#00000000")
            attribute worried:
                _sprite_placeholder("", "worried", "#00000000")
            attribute surprised:
                _sprite_placeholder("", "surprised", "#00000000")
            attribute thinking:
                _sprite_placeholder("", "thinking", "#00000000")
            attribute laughing:
                _sprite_placeholder("", "laughing", "#00000000")
            attribute vulnerable:
                _sprite_placeholder("", "vulnerable", "#00000000")

    ############################################################################
    ## ZARA CHEN
    ############################################################################
    ## 8 expressions, single outfit

    layeredimage zara:
        always:
            Solid("#C0392B22", xysize=(700, 1400))

        group expression:
            attribute neutral default:
                _sprite_placeholder("Zara", "neutral", "#C0392B")
            attribute happy:
                _sprite_placeholder("Zara", "happy", "#C0392B")
            attribute annoyed:
                _sprite_placeholder("Zara", "annoyed", "#C0392B")
            attribute surprised:
                _sprite_placeholder("Zara", "surprised", "#C0392B")
            attribute thinking:
                _sprite_placeholder("Zara", "thinking", "#C0392B")
            attribute determined:
                _sprite_placeholder("Zara", "determined", "#C0392B")
            attribute laughing:
                _sprite_placeholder("Zara", "laughing", "#C0392B")
            attribute warm:
                _sprite_placeholder("Zara", "warm", "#C0392B")

    ############################################################################
    ## RAJ PATEL
    ############################################################################
    ## 8 expressions, single outfit (cooking has apron variant)

    layeredimage raj:
        always:
            Solid("#E8A87C22", xysize=(700, 1400))

        group expression:
            attribute neutral default:
                _sprite_placeholder("Raj", "neutral", "#E8A87C")
            attribute happy:
                _sprite_placeholder("Raj", "happy", "#E8A87C")
            attribute worried:
                _sprite_placeholder("Raj", "worried", "#E8A87C")
            attribute laughing:
                _sprite_placeholder("Raj", "laughing", "#E8A87C")
            attribute serious:
                _sprite_placeholder("Raj", "serious", "#E8A87C")
            attribute cooking:
                _sprite_placeholder("Raj", "cooking", "#E8A87C")
            attribute gentle:
                _sprite_placeholder("Raj", "gentle", "#E8A87C")
            attribute upset:
                _sprite_placeholder("Raj", "upset", "#E8A87C")

    ############################################################################
    ## LIZ
    ############################################################################
    ## 6 expressions, single outfit

    layeredimage liz:
        always:
            Solid("#40E0D022", xysize=(700, 1400))

        group expression:
            attribute neutral default:
                _sprite_placeholder("Liz", "neutral", "#40E0D0")
            attribute happy:
                _sprite_placeholder("Liz", "happy", "#40E0D0")
            attribute worried:
                _sprite_placeholder("Liz", "worried", "#40E0D0")
            attribute surprised:
                _sprite_placeholder("Liz", "surprised", "#40E0D0")
            attribute laughing:
                _sprite_placeholder("Liz", "laughing", "#40E0D0")
            attribute concerned:
                _sprite_placeholder("Liz", "concerned", "#40E0D0")

    ############################################################################
    ## MAYA PENROSE
    ############################################################################
    ## 6 expressions, single outfit

    layeredimage maya:
        always:
            Solid("#2E8B5722", xysize=(700, 1400))

        group expression:
            attribute warm_welcome default:
                _sprite_placeholder("Maya", "warm welcome", "#2E8B57")
            attribute intense_focus:
                _sprite_placeholder("Maya", "intense focus", "#2E8B57")
            attribute mysterious:
                _sprite_placeholder("Maya", "mysterious", "#2E8B57")
            attribute grounded:
                _sprite_placeholder("Maya", "grounded", "#2E8B57")
            attribute teaching:
                _sprite_placeholder("Maya", "teaching", "#2E8B57")
            attribute concerned:
                _sprite_placeholder("Maya", "concerned", "#2E8B57")

    ############################################################################
    ## PROF. HAWTHORNE
    ############################################################################
    ## 6 expressions, single outfit

    layeredimage hawthorne:
        always:
            Solid("#80800022", xysize=(700, 1400))

        group expression:
            attribute wry_amusement default:
                _sprite_placeholder("Hawthorne", "wry amusement", "#808000")
            attribute sharp_focus:
                _sprite_placeholder("Hawthorne", "sharp focus", "#808000")
            attribute rare_warmth:
                _sprite_placeholder("Hawthorne", "rare warmth", "#808000")
            attribute devastating_honesty:
                _sprite_placeholder("Hawthorne", "devastating honesty", "#808000")
            attribute disappointed:
                _sprite_placeholder("Hawthorne", "disappointed", "#808000")
            attribute teaching:
                _sprite_placeholder("Hawthorne", "teaching", "#808000")

    ############################################################################
    ## DR. SIMMONS
    ############################################################################
    ## 6 expressions, single outfit

    layeredimage simmons:
        always:
            Solid("#80002022", xysize=(700, 1400))

        group expression:
            attribute patient_listening default:
                _sprite_placeholder("Simmons", "patient listening", "#800020")
            attribute gentle_challenge:
                _sprite_placeholder("Simmons", "gentle challenge", "#800020")
            attribute quiet_delight:
                _sprite_placeholder("Simmons", "quiet delight", "#800020")
            attribute rare_tears:
                _sprite_placeholder("Simmons", "rare tears", "#800020")
            attribute serious:
                _sprite_placeholder("Simmons", "serious", "#800020")
            attribute encouraging:
                _sprite_placeholder("Simmons", "encouraging", "#800020")

    ############################################################################
    ## ELENA VOSKRESENSKAYA
    ############################################################################
    ## 6 expressions × 2 settings (indoors/outdoors)

    layeredimage elena:
        always:
            Solid("#A8B5C522", xysize=(700, 1400))

        group setting:
            attribute indoors default:
                _sprite_placeholder("Elena", "indoors", "#A8B5C5")
            attribute outdoors:
                _sprite_placeholder("Elena", "outdoors", "#7A8A9A")

        group expression:
            attribute appraising default:
                _sprite_placeholder("", "appraising", "#00000000")
            attribute amused:
                _sprite_placeholder("", "amused", "#00000000")
            attribute stern:
                _sprite_placeholder("", "stern", "#00000000")
            attribute vulnerable:
                _sprite_placeholder("", "vulnerable", "#00000000")
            attribute teaching:
                _sprite_placeholder("", "teaching", "#00000000")
            attribute gentle:
                _sprite_placeholder("", "gentle", "#00000000")

    ############################################################################
    ## TASHA
    ############################################################################
    ## 4 expressions, single outfit

    layeredimage tasha:
        always:
            Solid("#FFB6C122", xysize=(700, 1400))

        group expression:
            attribute pleasant default:
                _sprite_placeholder("Tasha", "pleasant", "#FFB6C1")
            attribute cruel:
                _sprite_placeholder("Tasha", "cruel", "#FFB6C1")
            attribute exposed:
                _sprite_placeholder("Tasha", "exposed", "#FFB6C1")
            attribute angry:
                _sprite_placeholder("Tasha", "angry", "#FFB6C1")

    ############################################################################
    ## SOPHIA
    ############################################################################
    ## 4 expressions, single outfit

    layeredimage sophia:
        always:
            Solid("#70809022", xysize=(700, 1400))

        group expression:
            attribute composed default:
                _sprite_placeholder("Sophia", "composed", "#708090")
            attribute calculating:
                _sprite_placeholder("Sophia", "calculating", "#708090")
            attribute genuine:
                _sprite_placeholder("Sophia", "genuine", "#708090")
            attribute conflicted:
                _sprite_placeholder("Sophia", "conflicted", "#708090")

    ############################################################################
    ## MICHAEL
    ############################################################################
    ## 4 expressions, single outfit

    layeredimage michael:
        always:
            Solid("#8B000022", xysize=(700, 1400))

        group expression:
            attribute grinning default:
                _sprite_placeholder("Michael", "grinning", "#8B0000")
            attribute serious:
                _sprite_placeholder("Michael", "serious", "#8B0000")
            attribute confused:
                _sprite_placeholder("Michael", "confused", "#8B0000")
            attribute protective:
                _sprite_placeholder("Michael", "protective", "#8B0000")

    ############################################################################
    ## DAVID JAMES (Father)
    ############################################################################
    ## 4 expressions, single outfit

    layeredimage david:
        always:
            Solid("#80808022", xysize=(700, 1400))

        group expression:
            attribute steady default:
                _sprite_placeholder("David", "steady", "#808080")
            attribute proud:
                _sprite_placeholder("David", "proud", "#808080")
            attribute worried:
                _sprite_placeholder("David", "worried", "#808080")
            attribute laughing:
                _sprite_placeholder("David", "laughing", "#808080")

    ############################################################################
    ## GRACE JAMES (Mother)
    ############################################################################
    ## 4 expressions, single outfit

    layeredimage grace:
        always:
            Solid("#E8A87C22", xysize=(700, 1400))

        group expression:
            attribute warm default:
                _sprite_placeholder("Grace", "warm", "#E8A87C")
            attribute stern:
                _sprite_placeholder("Grace", "stern", "#E8A87C")
            attribute tearful:
                _sprite_placeholder("Grace", "tearful", "#E8A87C")
            attribute proud:
                _sprite_placeholder("Grace", "proud", "#E8A87C")

    ############################################################################
    ## LILY JAMES (Sister)
    ############################################################################
    ## 4 expressions, single outfit

    layeredimage lily:
        always:
            Solid("#FF404022", xysize=(700, 1400))

        group expression:
            attribute unimpressed default:
                _sprite_placeholder("Lily", "unimpressed", "#FF4040")
            attribute grinning:
                _sprite_placeholder("Lily", "grinning", "#FF4040")
            attribute soft:
                _sprite_placeholder("Lily", "soft", "#FF4040")
            attribute laughing:
                _sprite_placeholder("Lily", "laughing", "#FF4040")

    ############################################################################
    ## MR. OSEI (Bookshop owner)
    ############################################################################
    ## 3 expressions, single outfit

    layeredimage mr_osei:
        always:
            Solid("#8B691422", xysize=(700, 1400))

        group expression:
            attribute wise_warmth default:
                _sprite_placeholder("Mr. Osei", "wise warmth", "#8B6914")
            attribute thoughtful:
                _sprite_placeholder("Mr. Osei", "thoughtful", "#8B6914")
            attribute gentle:
                _sprite_placeholder("Mr. Osei", "gentle", "#8B6914")


## ============================================================================
## HOW TO REPLACE WITH REAL ART
## ============================================================================
##
## When real sprites are ready, replace the placeholder functions with
## image file references. Example for Amelia with real art:
##
##   layeredimage amelia:
##       group outfit:
##           attribute casual_autumn default:
##               "images/characters/amelia/casual_autumn/body.png"
##           attribute going_out:
##               "images/characters/amelia/going_out/body.png"
##           ...
##
##       group expression:
##           attribute neutral default:
##               "images/characters/amelia/casual_autumn/neutral.png"
##           attribute happy:
##               "images/characters/amelia/casual_autumn/happy.png"
##           ...
##
## If using full-body single images (one image per expression, not layered):
##
##   layeredimage amelia:
##       group expression:
##           attribute neutral default:
##               "images/characters/amelia/neutral.png"
##           attribute happy:
##               "images/characters/amelia/happy.png"
##           ...
##
## The simpler single-image approach is recommended for AI-generated art.
## ============================================================================
