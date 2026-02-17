## The CK: Amelia V2 — Placeholder Image Declarations
##
## This file defines ALL background images as coloured Solid() displayables
## with text labels. The game runs fully without any image files.
##
## DELETE THIS FILE once real backgrounds are placed in game/images/bg/.
## Ren'Py's automatic image loading will pick up files named to match the tags
## (e.g. images/bg/bg_thames_night.png → scene bg_thames_night).
##
## Colour coding by alchemical phase:
##   Nigredo  (Ch1-3)  = warm darks   (#3D2B1F burnt umber)
##   Albedo   (Ch4-7)  = cool whites  (#7B8D9E sea grey)
##   Citrinitas (Ch8-9) = golds       (#B8860B dark goldenrod)
##   Rubedo   (Ch10-12) = reds        (#722F37 wine)
##   Cornwall = earthy green           (#2E5339)
##   Special  = deep purple            (#4A3060)

init -1:

    ###########################################################################
    ## HELPER — Builds a placeholder: coloured rectangle + white label text
    ###########################################################################

    python:
        def placeholder_bg(label, color="#3D2B1F"):
            """Return a Ren'Py displayable: solid colour with centred text label."""
            return Composite(
                (1920, 1080),
                (0, 0), Solid(color),
                (0, 0), Text(
                    "{size=40}{color=#FFFFFF88}[ PLACEHOLDER ]\n\n{size=60}{color=#FFFFFFCC}" + label,
                    text_align=0.5,
                    xalign=0.5,
                    yalign=0.5,
                )
            )

    ###########################################################################
    ## LONDON BACKGROUNDS (Nigredo — #3D2B1F warm umber)
    ###########################################################################

    image bg_james_kitchen_evening = placeholder_bg("James Kitchen — Evening", "#3D2B1F")
    image bg_amelia_bedroom_night  = placeholder_bg("Amelia's Bedroom — Night", "#3D2B1F")
    image bg_amelia_bedroom_dark   = placeholder_bg("Amelia's Bedroom — Dark", "#2A1D14")
    image bg_park_bench_sunset     = placeholder_bg("Park Bench — Sunset", "#5C3A1E")
    image bg_bookshop              = placeholder_bg("Bookshop", "#3D2B1F")
    image bg_bookshop_interior     = placeholder_bg("Bookshop Interior", "#3D2B1F")
    image bg_thames_night          = placeholder_bg("Thames — Night", "#1A1A2E")
    image bg_thames                = placeholder_bg("Thames — Day", "#3D4F5F")
    image bg_james_house_morning   = placeholder_bg("James House — Morning", "#5C4A3A")
    image bg_london_cafe           = placeholder_bg("London Café", "#4A3A2A")
    image bg_london_park           = placeholder_bg("London Park", "#3D4A30")
    image bg_london_train          = placeholder_bg("London Train", "#3A3A4A")
    image bg_amelia_home           = placeholder_bg("Amelia's London Home", "#3D2B1F")
    image bg_lily_room             = placeholder_bg("Lily's Room", "#4A2A3A")
    image bg_family_home           = placeholder_bg("Family Home", "#5C4A3A")
    image bg_motorway_daytime      = placeholder_bg("Motorway — Daytime", "#5A5A5A")

    ###########################################################################
    ## PLYMOUTH CAMPUS (Albedo — #7B8D9E sea grey)
    ###########################################################################

    image bg_plymouth_first_sight  = placeholder_bg("Plymouth — First Sight", "#5A6A7A")
    image bg_campus_tour           = placeholder_bg("Campus Tour", "#7B8D9E")
    image bg_campus_daytime        = placeholder_bg("Campus — Daytime", "#8A9AAA")
    image bg_campus_quad           = placeholder_bg("Campus Quad", "#7B8D9E")
    image bg_lecture_theatre        = placeholder_bg("Lecture Theatre", "#6A7A8A")
    image bg_psych_building        = placeholder_bg("Psychology Building", "#7B8D9E")
    image bg_psych_building_corridor = placeholder_bg("Psych Building Corridor", "#6A7A8A")
    image bg_psych_building_lecture = placeholder_bg("Psych Building Lecture Hall", "#5A6A7A")
    image bg_seminar_room          = placeholder_bg("Seminar Room", "#7B8D9E")
    image bg_library               = placeholder_bg("Library", "#8A9AAA")
    image bg_library_night         = placeholder_bg("Library — Night", "#4A5A6A")
    image bg_library_study_area    = placeholder_bg("Library Study Area", "#7B8D9E")
    image bg_su_night              = placeholder_bg("Student Union — Night", "#3A4A5A")
    image bg_barbican_bookshop     = placeholder_bg("Barbican Bookshop", "#6A7A6A")
    image bg_hawthorne_office      = placeholder_bg("Hawthorne's Office", "#8A7A5A")
    image bg_simmons_office        = placeholder_bg("Simmons's Office", "#6A5A5A")
    image bg_counsellor_office     = placeholder_bg("Counsellor's Office", "#7B8D9E")
    image bg_hospital_corridor     = placeholder_bg("Hospital Corridor", "#9AAAAA")

    ###########################################################################
    ## PLYMOUTH LIVING (Albedo — #7B8D9E tones)
    ###########################################################################

    image bg_halls_kitchen_evening = placeholder_bg("Halls Kitchen — Evening", "#6A7A6A")
    image bg_halls_kitchen_night   = placeholder_bg("Halls Kitchen — Night", "#4A5A4A")
    image bg_kitchen_halls         = placeholder_bg("Kitchen — Halls", "#6A7A6A")
    image bg_flat_kitchen          = placeholder_bg("Flat Kitchen", "#5A6A5A")
    image bg_flat_party            = placeholder_bg("Flat Party", "#5A4A6A")
    image bg_halls_corridor        = placeholder_bg("Halls Corridor", "#6A7A8A")
    image bg_amelia_room_plymouth_night = placeholder_bg("Amelia's Room Plymouth — Night", "#4A5A6A")
    image bg_amelia_room_plymouth_day   = placeholder_bg("Amelia's Room Plymouth — Day", "#8A9AAA")
    image bg_amelia_room_plymouth_rain  = placeholder_bg("Amelia's Room Plymouth — Rain", "#5A6A7A")
    image bg_lucas_room            = placeholder_bg("Lucas's Room", "#6A8A9A")
    image bg_maya_room_candlelit   = placeholder_bg("Maya's Room — Candlelit", "#5A4A3A")
    image bg_maya_room_ceremony    = placeholder_bg("Maya's Room — Ceremony", "#4A3A4A")

    ###########################################################################
    ## PLYMOUTH HOE (Albedo/dawn — mixed tones)
    ###########################################################################

    image bg_plymouth_hoe_grey     = placeholder_bg("Plymouth Hoe — Grey", "#8A8A8A")
    image bg_plymouth_hoe_dawn     = placeholder_bg("Plymouth Hoe — Dawn", "#C4956A")
    image bg_plymouth_hoe_day      = placeholder_bg("Plymouth Hoe — Day", "#8AA0B0")

    ###########################################################################
    ## CORNWALL (Earthy green — #2E5339)
    ###########################################################################

    image bg_cornwall_coast        = placeholder_bg("Cornwall Coast", "#2E5339")
    image bg_bodmin_moor           = placeholder_bg("Bodmin Moor", "#3A4A30")
    image bg_men_an_tol            = placeholder_bg("Mên-an-Tol", "#4A5A3A")
    image bg_merry_maidens         = placeholder_bg("Merry Maidens", "#3A5A3A")
    image bg_madron_well           = placeholder_bg("Madron Well", "#2A4A2A")
    image bg_fogou_entrance        = placeholder_bg("Fogou Entrance", "#1A3A2A")
    image bg_cornwall_night        = placeholder_bg("Cornwall — Night", "#1A2A1A")
    image bg_tintagel              = placeholder_bg("Tintagel", "#3A4A5A")
    image bg_eden_project          = placeholder_bg("Eden Project", "#4A6A4A")

    ###########################################################################
    ## CHARACTER SPRITE PLACEHOLDERS
    ##
    ## These define simple text-label sprites for every character so that
    ## `show amelia happy` etc. won't cause missing-image errors.
    ## Replace with layeredimage declarations when real sprites are ready.
    ###########################################################################

    python:
        def placeholder_sprite(name, color="#D4A574"):
            """Return a small centred text block acting as a character sprite placeholder."""
            return Composite(
                (400, 800),
                (0, 0), Solid(color + "33"),  # very transparent tint
                (0, 0), Text(
                    "{size=30}{color=#FFFFFFAA}" + name,
                    text_align=0.5,
                    xalign=0.5,
                    yalign=0.8,
                )
            )

    ## NOTE: Character sprites are not yet used in the scripts (all dialogue
    ## is narrated without show statements). These are here for when you add
    ## `show character expression` lines during the sprite integration pass.
    ## Uncomment the block below if you want to test with sprite placeholders.

    # image amelia neutral     = placeholder_sprite("Amelia\nneutral", "#D4A574")
    # image amelia happy       = placeholder_sprite("Amelia\nhappy", "#D4A574")
    # image amelia sad         = placeholder_sprite("Amelia\nsad", "#D4A574")
    # image sarah neutral      = placeholder_sprite("Sarah\nneutral", "#A8B5C5")
    # image sarah withdrawn    = placeholder_sprite("Sarah\nwithdrawn", "#A8B5C5")
    # image ella neutral       = placeholder_sprite("Ella\nneutral", "#FFD700")
    # image ella happy         = placeholder_sprite("Ella\nhappy", "#FFD700")
    # image lucas neutral      = placeholder_sprite("Lucas\nneutral", "#7BA7BC")
    # ... (add remaining as needed during sprite integration)
