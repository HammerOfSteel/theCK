## slideshows.rpy — Song Slideshow Labels
##
## Each label plays a song while cycling through background images.
## Called from chapter scripts via: call slideshow_chX_song_name
## No dialogue — purely visual/musical interludes.

# =========================================================================
# CHAPTER 1 — "Paper Planes"
# Context: After Thames at Night. Amelia's last London evening.
# =========================================================================
label slideshow_ch1_paper_planes:
    stop music fadeout 1.0
    play music "audio/songs/paper_planes.ogg" noloop

    scene bg_thames_night with dissolve
    pause 12.0
    scene bg_park_bench_sunset with dissolve
    pause 12.0
    scene bg_bookshop_interior with dissolve
    pause 12.0
    scene bg_amelia_bedroom_night with dissolve
    pause 12.0
    scene bg_amelia_bedroom_dark with dissolve
    pause 12.0

    scene bg_thames_night with dissolve
    pause 12.0
    scene bg_park_bench_sunset with dissolve
    pause 12.0
    scene bg_bookshop_interior with dissolve
    pause 12.0
    scene bg_amelia_bedroom_night with dissolve
    pause 12.0
    scene bg_amelia_bedroom_dark with dissolve
    pause 12.0

    scene bg_thames_night with dissolve
    pause 12.0
    scene bg_park_bench_sunset with dissolve
    pause 12.0
    scene bg_bookshop_interior with dissolve
    pause 12.0
    scene bg_amelia_bedroom_night with dissolve
    pause 12.0
    scene bg_amelia_bedroom_dark with dissolve
    pause 12.0

    stop music fadeout 2.0
    return


# =========================================================================
# CHAPTER 2 — "Lighthouse in the Fog"
# Context: The drive from London to Plymouth. England unspooling.
# =========================================================================
label slideshow_ch2_lighthouse_in_the_fog:
    stop music fadeout 1.0
    play music "audio/songs/lighthouse_in_the_fog.ogg" noloop

    scene bg_james_house_morning with dissolve
    pause 12.0
    scene bg_motorway_daytime with dissolve
    pause 12.0
    scene bg_motorway_daytime with dissolve
    pause 15.0
    scene bg_plymouth_first_sight with dissolve
    pause 12.0
    scene bg_plymouth_hoe_grey with dissolve
    pause 12.0

    scene bg_motorway_daytime with dissolve
    pause 12.0
    scene bg_plymouth_first_sight with dissolve
    pause 15.0
    scene bg_halls_corridor with dissolve
    pause 12.0
    scene bg_campus_daytime with dissolve
    pause 12.0
    scene bg_plymouth_hoe_grey with dissolve
    pause 12.0

    scene bg_motorway_daytime with dissolve
    pause 12.0
    scene bg_plymouth_first_sight with dissolve
    pause 12.0
    scene bg_plymouth_hoe_grey with dissolve
    pause 12.0
    scene bg_campus_daytime with dissolve
    pause 12.0
    scene bg_plymouth_first_sight with dissolve
    pause 12.0

    stop music fadeout 2.0
    return


# =========================================================================
# CHAPTER 3 — "Two Birds"
# Context: After the panic attack. Homesickness, missing Ella.
# =========================================================================
label slideshow_ch3_two_birds:
    stop music fadeout 1.0
    play music "audio/songs/two_birds.ogg" noloop

    scene bg_library_night with dissolve
    pause 12.0
    scene bg_amelia_room_plymouth_rain with dissolve
    pause 12.0
    scene bg_plymouth_hoe_grey with dissolve
    pause 12.0
    scene bg_halls_kitchen_night with dissolve
    pause 12.0
    scene bg_amelia_room_plymouth_rain with dissolve
    pause 12.0

    scene bg_library_night with dissolve
    pause 12.0
    scene bg_plymouth_hoe_grey with dissolve
    pause 12.0
    scene bg_halls_kitchen_night with dissolve
    pause 12.0
    scene bg_amelia_room_plymouth_rain with dissolve
    pause 12.0
    scene bg_library_night with dissolve
    pause 12.0

    scene bg_plymouth_hoe_grey with dissolve
    pause 12.0
    scene bg_amelia_room_plymouth_rain with dissolve
    pause 12.0
    scene bg_halls_kitchen_night with dissolve
    pause 12.0
    scene bg_library_night with dissolve
    pause 12.0
    scene bg_amelia_room_plymouth_rain with dissolve
    pause 12.0

    stop music fadeout 2.0
    return


# =========================================================================
# CHAPTER 4 — "Hawthorne"
# Context: Cornwall trip. Ancient landscape, mentor's wisdom.
# =========================================================================
label slideshow_ch4_hawthorne:
    stop music fadeout 1.0
    play music "audio/songs/hawthorne.ogg" noloop

    scene bg_bodmin_moor with dissolve
    pause 12.0
    scene bg_tintagel with dissolve
    pause 12.0
    scene bg_madron_well with dissolve
    pause 12.0
    scene bg_men_an_tol with dissolve
    pause 12.0
    scene bg_merry_maidens with dissolve
    pause 12.0
    scene bg_eden_project with dissolve
    pause 12.0

    scene bg_bodmin_moor with dissolve
    pause 12.0
    scene bg_tintagel with dissolve
    pause 12.0
    scene bg_madron_well with dissolve
    pause 12.0
    scene bg_men_an_tol with dissolve
    pause 12.0
    scene bg_merry_maidens with dissolve
    pause 12.0
    scene bg_eden_project with dissolve
    pause 12.0

    scene bg_bodmin_moor with dissolve
    pause 12.0
    scene bg_tintagel with dissolve
    pause 12.0
    scene bg_madron_well with dissolve
    pause 12.0

    stop music fadeout 2.0
    return


# =========================================================================
# CHAPTER 5 — "Circles in the Sand"
# Context: Group Cornwall trip. Friends on the coast.
# =========================================================================
label slideshow_ch5_circles_in_the_sand:
    stop music fadeout 1.0
    play music "audio/songs/circles_in_the_sand.ogg" noloop

    scene bg_cornwall_coast with dissolve
    pause 12.0
    scene bg_campus_quad with dissolve
    pause 12.0
    scene bg_library_study_area with dissolve
    pause 12.0
    scene bg_cornwall_coast with dissolve
    pause 12.0
    scene bg_halls_corridor with dissolve
    pause 12.0

    scene bg_cornwall_coast with dissolve
    pause 12.0
    scene bg_campus_quad with dissolve
    pause 12.0
    scene bg_library_study_area with dissolve
    pause 12.0
    scene bg_cornwall_coast with dissolve
    pause 12.0
    scene bg_halls_corridor with dissolve
    pause 12.0

    scene bg_cornwall_coast with dissolve
    pause 12.0
    scene bg_campus_quad with dissolve
    pause 12.0
    scene bg_cornwall_coast with dissolve
    pause 12.0
    scene bg_library_study_area with dissolve
    pause 12.0
    scene bg_cornwall_coast with dissolve
    pause 12.0

    stop music fadeout 2.0
    return


# =========================================================================
# CHAPTER 6 — "Kindeling Kin"
# Context: Christmas at home. Grace's kitchen, childhood echoes.
# =========================================================================
label slideshow_ch6_kindeling_kin:
    stop music fadeout 1.0
    play music "audio/songs/kindeling_kin.ogg" noloop

    scene bg_family_home with dissolve
    pause 12.0
    scene bg_london_cafe with dissolve
    pause 12.0
    scene bg_family_home with dissolve
    pause 15.0
    scene bg_london_cafe with dissolve
    pause 12.0
    scene bg_family_home with dissolve
    pause 12.0

    scene bg_london_cafe with dissolve
    pause 12.0
    scene bg_family_home with dissolve
    pause 15.0
    scene bg_london_cafe with dissolve
    pause 12.0
    scene bg_family_home with dissolve
    pause 12.0
    scene bg_london_cafe with dissolve
    pause 12.0

    scene bg_family_home with dissolve
    pause 12.0
    scene bg_london_cafe with dissolve
    pause 12.0
    scene bg_family_home with dissolve
    pause 15.0
    scene bg_london_cafe with dissolve
    pause 12.0
    scene bg_family_home with dissolve
    pause 12.0

    stop music fadeout 2.0
    return


# =========================================================================
# CHAPTER 6 (conditional) — "The Mist-Laden Path"
# Context: Midwinter solstice. Candles in woods, longest night.
# Requires: stat_ok >= 5
# =========================================================================
label slideshow_ch6_the_mist_laden_path:
    stop music fadeout 1.0
    play music "audio/songs/the_mist_laden_path.ogg" noloop

    scene bg_cornwall_night with dissolve
    pause 12.0
    scene bg_cornwall_coast with dissolve
    pause 12.0
    scene bg_madron_well with dissolve
    pause 12.0
    scene bg_cornwall_night with dissolve
    pause 15.0
    scene bg_cornwall_coast with dissolve
    pause 12.0

    scene bg_madron_well with dissolve
    pause 12.0
    scene bg_cornwall_night with dissolve
    pause 12.0
    scene bg_cornwall_coast with dissolve
    pause 15.0
    scene bg_cornwall_night with dissolve
    pause 12.0
    scene bg_madron_well with dissolve
    pause 12.0

    scene bg_cornwall_night with dissolve
    pause 12.0
    scene bg_cornwall_coast with dissolve
    pause 12.0
    scene bg_cornwall_night with dissolve
    pause 12.0
    scene bg_madron_well with dissolve
    pause 12.0
    scene bg_cornwall_night with dissolve
    pause 12.0

    stop music fadeout 2.0
    return


# =========================================================================
# CHAPTER 7 — "Mirror of the Mind"
# Context: The Gathering Storm. February, the Hoe, pre-crisis tension.
# =========================================================================
label slideshow_ch7_mirror_of_the_mind:
    stop music fadeout 1.0
    play music "audio/songs/mirror_of_the_mind.ogg" noloop

    scene bg_plymouth_hoe_day with dissolve
    pause 12.0
    scene bg_library_study_area with dissolve
    pause 12.0
    scene bg_psych_building_corridor with dissolve
    pause 12.0
    scene bg_plymouth_hoe_day with dissolve
    pause 12.0
    scene bg_lecture_theatre with dissolve
    pause 12.0

    scene bg_plymouth_hoe_day with dissolve
    pause 12.0
    scene bg_library_study_area with dissolve
    pause 12.0
    scene bg_psych_building_corridor with dissolve
    pause 12.0
    scene bg_plymouth_hoe_day with dissolve
    pause 12.0
    scene bg_lecture_theatre with dissolve
    pause 12.0

    scene bg_plymouth_hoe_day with dissolve
    pause 12.0
    scene bg_library_study_area with dissolve
    pause 12.0
    scene bg_plymouth_hoe_day with dissolve
    pause 12.0
    scene bg_psych_building_corridor with dissolve
    pause 12.0
    scene bg_plymouth_hoe_day with dissolve
    pause 12.0

    stop music fadeout 2.0
    return


# =========================================================================
# CHAPTER 8 — "Oh Sarah" (opening — before the crisis)
# Context: Porthcurno Beach. Reaching out to someone in darkness.
# The most literal, character-named song in the entire collection.
# =========================================================================
label slideshow_ch8_oh_sarah:
    stop music fadeout 1.0
    play music "audio/songs/oh_sarah.ogg" noloop

    scene bg_cornwall_coast with dissolve
    pause 12.0
    scene bg_plymouth_hoe_grey with dissolve
    pause 12.0
    scene bg_halls_corridor with dissolve
    pause 12.0
    scene bg_cornwall_coast with dissolve
    pause 15.0
    scene bg_amelia_room_plymouth_night with dissolve
    pause 12.0

    scene bg_plymouth_hoe_grey with dissolve
    pause 12.0
    scene bg_cornwall_coast with dissolve
    pause 12.0
    scene bg_halls_corridor with dissolve
    pause 15.0
    scene bg_plymouth_hoe_grey with dissolve
    pause 12.0
    scene bg_amelia_room_plymouth_night with dissolve
    pause 12.0

    scene bg_cornwall_coast with dissolve
    pause 12.0
    scene bg_plymouth_hoe_grey with dissolve
    pause 12.0
    scene bg_halls_corridor with dissolve
    pause 12.0
    scene bg_cornwall_coast with dissolve
    pause 15.0

    stop music fadeout 2.0
    return


# =========================================================================
# CHAPTER 8 — "Bare With Me" (primary)
# Context: In the Ashes. After Sarah's crisis, before the aftermath.
# The emotional centre of the entire game.
# =========================================================================
label slideshow_ch8_bare_with_me:
    stop music fadeout 1.0
    play music "audio/songs/bare_with_me.ogg" noloop

    scene black with dissolve
    pause 15.0
    scene bg_halls_corridor with dissolve
    pause 12.0
    scene bg_counsellor_office with dissolve
    pause 12.0
    scene bg_hospital_corridor with dissolve
    pause 12.0
    scene black with dissolve
    pause 15.0

    scene bg_plymouth_hoe_dawn with dissolve
    pause 12.0
    scene bg_halls_corridor with dissolve
    pause 12.0
    scene bg_counsellor_office with dissolve
    pause 12.0
    scene black with dissolve
    pause 15.0
    scene bg_hospital_corridor with dissolve
    pause 12.0

    scene bg_plymouth_hoe_dawn with dissolve
    pause 12.0
    scene bg_halls_corridor with dissolve
    pause 12.0
    scene black with dissolve
    pause 15.0
    scene bg_plymouth_hoe_dawn with dissolve
    pause 12.0

    stop music fadeout 2.0
    return


# =========================================================================
# CHAPTER 8 — "Living on the Moon" (secondary)
# Context: The Bottom. Amelia alone in her room, rain, darkness.
# =========================================================================
label slideshow_ch8_living_on_the_moon:
    stop music fadeout 1.0
    play music "audio/songs/living_on_the_moon.ogg" noloop

    scene bg_amelia_room_plymouth_night with dissolve
    pause 12.0
    scene bg_plymouth_hoe_grey with dissolve
    pause 12.0
    scene bg_library_night with dissolve
    pause 12.0
    scene bg_amelia_room_plymouth_night with dissolve
    pause 15.0
    scene bg_halls_corridor with dissolve
    pause 12.0

    scene bg_amelia_room_plymouth_night with dissolve
    pause 12.0
    scene bg_plymouth_hoe_grey with dissolve
    pause 12.0
    scene bg_amelia_room_plymouth_night with dissolve
    pause 15.0
    scene bg_library_night with dissolve
    pause 12.0
    scene bg_halls_corridor with dissolve
    pause 12.0

    scene bg_amelia_room_plymouth_night with dissolve
    pause 12.0
    scene bg_plymouth_hoe_grey with dissolve
    pause 12.0
    scene bg_amelia_room_plymouth_night with dissolve
    pause 15.0
    scene bg_library_night with dissolve
    pause 12.0
    scene bg_amelia_room_plymouth_night with dissolve
    pause 12.0

    stop music fadeout 2.0
    return


# =========================================================================
# CHAPTER 8 — "Forgetmeknot" (conditional — tragic path only)
# Context: "In the twilight of our first-year dreams." Sarah has died.
# A friend's death in first year. The forget-me-not as promise.
# Condition: sarah_alive == False
# =========================================================================
label slideshow_ch8_forgetmeknot:
    stop music fadeout 1.0
    play music "audio/songs/forgetmeknot.ogg" noloop

    scene bg_halls_corridor with dissolve
    pause 12.0
    scene bg_plymouth_hoe_grey with dissolve
    pause 15.0
    scene bg_amelia_room_plymouth_night with dissolve
    pause 12.0
    scene bg_campus_quad with dissolve
    pause 12.0
    scene bg_plymouth_hoe_grey with dissolve
    pause 12.0

    scene bg_halls_corridor with dissolve
    pause 15.0
    scene bg_amelia_room_plymouth_night with dissolve
    pause 12.0
    scene bg_campus_quad with dissolve
    pause 12.0
    scene bg_plymouth_hoe_grey with dissolve
    pause 15.0
    scene bg_halls_corridor with dissolve
    pause 12.0

    scene bg_amelia_room_plymouth_night with dissolve
    pause 12.0
    scene bg_campus_quad with dissolve
    pause 12.0
    scene bg_plymouth_hoe_grey with dissolve
    pause 12.0
    scene bg_halls_corridor with dissolve
    pause 15.0

    stop music fadeout 2.0
    return


# =========================================================================
# CHAPTER 9 — "jolly-rum-ba-low!"
# Context: Cornwall healing trip. Spring, Cornish May Day energy.
# =========================================================================
label slideshow_ch9_jolly_rum_ba_low:
    stop music fadeout 1.0
    play music "audio/songs/jolly_rum_ba_low.ogg" noloop

    scene bg_cornwall_coast with dissolve
    pause 10.0
    scene bg_plymouth_hoe_day with dissolve
    pause 10.0
    scene bg_eden_project with dissolve
    pause 10.0
    scene bg_tintagel with dissolve
    pause 10.0
    scene bg_cornwall_coast with dissolve
    pause 10.0
    scene bg_campus_quad with dissolve
    pause 10.0

    scene bg_cornwall_coast with dissolve
    pause 10.0
    scene bg_plymouth_hoe_day with dissolve
    pause 10.0
    scene bg_eden_project with dissolve
    pause 10.0
    scene bg_tintagel with dissolve
    pause 10.0
    scene bg_cornwall_coast with dissolve
    pause 10.0
    scene bg_campus_quad with dissolve
    pause 10.0

    scene bg_cornwall_coast with dissolve
    pause 10.0
    scene bg_plymouth_hoe_day with dissolve
    pause 10.0
    scene bg_eden_project with dissolve
    pause 10.0
    scene bg_cornwall_coast with dissolve
    pause 10.0
    scene bg_tintagel with dissolve
    pause 10.0
    scene bg_cornwall_coast with dissolve
    pause 10.0

    stop music fadeout 2.0
    return


# =========================================================================
# CHAPTER 10 — "The Long Way Home" (primary)
# Context: Train back to London for Easter. The reverse journey.
# =========================================================================
label slideshow_ch10_the_long_way_home:
    stop music fadeout 1.0
    play music "audio/songs/the_long_way_home.ogg" noloop

    scene bg_london_train with dissolve
    pause 12.0
    scene bg_plymouth_hoe_day with dissolve
    pause 12.0
    scene bg_cornwall_coast with dissolve
    pause 12.0
    scene bg_london_train with dissolve
    pause 15.0
    scene bg_amelia_home with dissolve
    pause 12.0

    scene bg_london_train with dissolve
    pause 12.0
    scene bg_plymouth_hoe_day with dissolve
    pause 12.0
    scene bg_london_train with dissolve
    pause 15.0
    scene bg_cornwall_coast with dissolve
    pause 12.0
    scene bg_amelia_home with dissolve
    pause 12.0

    scene bg_london_train with dissolve
    pause 12.0
    scene bg_plymouth_hoe_day with dissolve
    pause 12.0
    scene bg_london_train with dissolve
    pause 12.0
    scene bg_amelia_home with dissolve
    pause 12.0
    scene bg_london_train with dissolve
    pause 12.0

    stop music fadeout 2.0
    return


# =========================================================================
# CHAPTER 12 — "Amelia" (credits theme)
# Context: The protagonist's anthem. The full Hero's Journey in one song.
# "Born by the sea, where ideas set free / Off the moor, into the Plym she sails."
# Plays during the credits as a final emotional statement.
# =========================================================================
label slideshow_ch12_amelia_credits:
    stop music fadeout 1.0
    play music "audio/songs/amelia.ogg" noloop

    scene bg_park_bench_sunset with dissolve
    pause 12.0
    scene bg_motorway_daytime with dissolve
    pause 12.0
    scene bg_campus_quad with dissolve
    pause 12.0
    scene bg_cornwall_coast with dissolve
    pause 12.0
    scene bg_plymouth_hoe_day with dissolve
    pause 12.0

    scene bg_amelia_room_plymouth_night with dissolve
    pause 12.0
    scene bg_halls_corridor with dissolve
    pause 12.0
    scene bg_flat_kitchen with dissolve
    pause 12.0
    scene bg_plymouth_hoe_dawn with dissolve
    pause 12.0
    scene bg_london_train with dissolve
    pause 12.0

    scene bg_park_bench_sunset with dissolve
    pause 12.0
    scene bg_cornwall_coast with dissolve
    pause 12.0
    scene bg_plymouth_hoe_day with dissolve
    pause 12.0
    scene bg_campus_quad with dissolve
    pause 12.0

    scene black with dissolve
    pause 5.0

    stop music fadeout 3.0
    return
# =========================================================================
# CHAPTER 10 — "Here, Now, and Blues" (secondary)
# Context: Solo London walk. Familiar streets, April light.
# =========================================================================
label slideshow_ch10_here_now_and_blues:
    stop music fadeout 1.0
    play music "audio/songs/here_now_and_blues.ogg" noloop

    scene bg_london_park with dissolve
    pause 12.0
    scene bg_thames with dissolve
    pause 12.0
    scene bg_bookshop with dissolve
    pause 12.0
    scene bg_london_park with dissolve
    pause 12.0
    scene bg_amelia_home with dissolve
    pause 12.0

    scene bg_thames with dissolve
    pause 12.0
    scene bg_london_park with dissolve
    pause 12.0
    scene bg_bookshop with dissolve
    pause 12.0
    scene bg_amelia_home with dissolve
    pause 12.0
    scene bg_london_park with dissolve
    pause 12.0

    scene bg_thames with dissolve
    pause 12.0
    scene bg_london_park with dissolve
    pause 12.0
    scene bg_bookshop with dissolve
    pause 12.0
    scene bg_amelia_home with dissolve
    pause 12.0
    scene bg_london_park with dissolve
    pause 12.0

    stop music fadeout 2.0
    return


# =========================================================================
# CHAPTER 11 — "Between the Veil" (primary)
# Context: Fogou / mystical climax. The transformative encounter.
# =========================================================================
label slideshow_ch11_between_the_veil:
    stop music fadeout 1.0
    play music "audio/songs/between_the_veil.ogg" noloop

    scene bg_fogou_entrance with dissolve
    pause 12.0
    scene bg_cornwall_coast with dissolve
    pause 12.0
    scene bg_madron_well with dissolve
    pause 12.0
    scene bg_men_an_tol with dissolve
    pause 12.0
    scene bg_merry_maidens with dissolve
    pause 12.0
    scene bg_fogou_entrance with dissolve
    pause 15.0

    scene bg_cornwall_coast with dissolve
    pause 12.0
    scene bg_madron_well with dissolve
    pause 12.0
    scene bg_fogou_entrance with dissolve
    pause 15.0
    scene bg_men_an_tol with dissolve
    pause 12.0
    scene bg_merry_maidens with dissolve
    pause 12.0

    scene bg_fogou_entrance with dissolve
    pause 15.0
    scene bg_cornwall_coast with dissolve
    pause 12.0
    scene bg_madron_well with dissolve
    pause 12.0
    scene bg_fogou_entrance with dissolve
    pause 12.0

    stop music fadeout 2.0
    return


# =========================================================================
# CHAPTER 11 — "The_Work" (secondary — Red Dawn / Rubedo)
# Context: Sunrise over Plymouth Sound. THE climax. Red and gold.
# =========================================================================
label slideshow_ch11_the_work:
    stop music fadeout 1.0
    play music "audio/songs/the_work.ogg" noloop

    scene bg_plymouth_hoe_dawn with dissolve
    pause 15.0
    scene bg_cornwall_coast with dissolve
    pause 12.0
    scene bg_plymouth_hoe_day with dissolve
    pause 12.0
    scene bg_campus_quad with dissolve
    pause 12.0
    scene bg_plymouth_hoe_dawn with dissolve
    pause 15.0

    scene bg_cornwall_coast with dissolve
    pause 12.0
    scene bg_plymouth_hoe_day with dissolve
    pause 12.0
    scene bg_plymouth_hoe_dawn with dissolve
    pause 15.0
    scene bg_campus_quad with dissolve
    pause 12.0
    scene bg_cornwall_coast with dissolve
    pause 12.0

    scene bg_plymouth_hoe_dawn with dissolve
    pause 15.0
    scene bg_plymouth_hoe_day with dissolve
    pause 12.0
    scene bg_cornwall_coast with dissolve
    pause 12.0
    scene bg_plymouth_hoe_dawn with dissolve
    pause 15.0

    stop music fadeout 2.0
    return


# =========================================================================
# CHAPTER 12 — "The Quiet of Morning" (primary — farewell)
# Context: Last goodbye. The flat emptying, corridor hugs.
# =========================================================================
label slideshow_ch12_the_quiet_of_morning:
    stop music fadeout 1.0
    play music "audio/songs/the_quiet_of_morning.ogg" noloop

    scene bg_amelia_room_plymouth_day with dissolve
    pause 12.0
    scene bg_flat_kitchen with dissolve
    pause 12.0
    scene bg_halls_corridor with dissolve
    pause 12.0
    scene bg_campus_quad with dissolve
    pause 12.0
    scene bg_plymouth_hoe_day with dissolve
    pause 12.0
    scene bg_amelia_room_plymouth_day with dissolve
    pause 12.0

    scene bg_flat_kitchen with dissolve
    pause 12.0
    scene bg_halls_corridor with dissolve
    pause 12.0
    scene bg_campus_quad with dissolve
    pause 12.0
    scene bg_plymouth_hoe_day with dissolve
    pause 12.0
    scene bg_amelia_room_plymouth_day with dissolve
    pause 12.0
    scene bg_flat_kitchen with dissolve
    pause 12.0

    scene bg_halls_corridor with dissolve
    pause 12.0
    scene bg_plymouth_hoe_day with dissolve
    pause 12.0
    scene bg_amelia_room_plymouth_day with dissolve
    pause 12.0

    stop music fadeout 2.0
    return


# =========================================================================
# CHAPTER 12 — "Daffodils in the Snow" (closing — before ending title)
# Context: The game's final musical statement. Universal, all endings.
# Seven variants — one per ending, each with thematically matched images.
# =========================================================================

label slideshow_ch12_daffodils_grief:
    # THE GRIEF ending — loss, empty spaces
    stop music fadeout 1.0
    play music "audio/songs/daffodils_in_the_snow.ogg" noloop

    scene bg_london_park with dissolve
    pause 12.0
    scene bg_hospital_corridor with dissolve
    pause 12.0
    scene bg_plymouth_hoe_grey with dissolve
    pause 12.0
    scene bg_london_park with dissolve
    pause 15.0
    scene bg_amelia_home with dissolve
    pause 12.0

    scene bg_hospital_corridor with dissolve
    pause 12.0
    scene bg_london_park with dissolve
    pause 12.0
    scene bg_plymouth_hoe_grey with dissolve
    pause 15.0
    scene bg_amelia_home with dissolve
    pause 12.0
    scene bg_london_park with dissolve
    pause 12.0

    scene bg_hospital_corridor with dissolve
    pause 12.0
    scene bg_plymouth_hoe_grey with dissolve
    pause 12.0
    scene bg_london_park with dissolve
    pause 15.0
    scene bg_amelia_home with dissolve
    pause 12.0

    stop music fadeout 2.0
    return

label slideshow_ch12_daffodils_alchemist:
    # THE ALCHEMIST ending — Cornwall, stones, the gold
    stop music fadeout 1.0
    play music "audio/songs/daffodils_in_the_snow.ogg" noloop

    scene bg_cornwall_coast with dissolve
    pause 12.0
    scene bg_men_an_tol with dissolve
    pause 12.0
    scene bg_madron_well with dissolve
    pause 12.0
    scene bg_merry_maidens with dissolve
    pause 12.0
    scene bg_cornwall_coast with dissolve
    pause 15.0

    scene bg_fogou_entrance with dissolve
    pause 12.0
    scene bg_men_an_tol with dissolve
    pause 12.0
    scene bg_cornwall_coast with dissolve
    pause 12.0
    scene bg_madron_well with dissolve
    pause 12.0
    scene bg_merry_maidens with dissolve
    pause 15.0

    scene bg_cornwall_coast with dissolve
    pause 12.0
    scene bg_fogou_entrance with dissolve
    pause 12.0
    scene bg_men_an_tol with dissolve
    pause 12.0
    scene bg_cornwall_coast with dissolve
    pause 12.0

    stop music fadeout 2.0
    return

label slideshow_ch12_daffodils_scholar:
    # THE SCHOLAR ending — academia, libraries, knowledge
    stop music fadeout 1.0
    play music "audio/songs/daffodils_in_the_snow.ogg" noloop

    scene bg_library with dissolve
    pause 12.0
    scene bg_hawthorne_office with dissolve
    pause 12.0
    scene bg_lecture_theatre with dissolve
    pause 12.0
    scene bg_library_study_area with dissolve
    pause 12.0
    scene bg_library with dissolve
    pause 15.0

    scene bg_hawthorne_office with dissolve
    pause 12.0
    scene bg_lecture_theatre with dissolve
    pause 12.0
    scene bg_library with dissolve
    pause 12.0
    scene bg_library_study_area with dissolve
    pause 12.0
    scene bg_hawthorne_office with dissolve
    pause 15.0

    scene bg_library with dissolve
    pause 12.0
    scene bg_lecture_theatre with dissolve
    pause 12.0
    scene bg_library_study_area with dissolve
    pause 12.0
    scene bg_library with dissolve
    pause 12.0

    stop music fadeout 2.0
    return

label slideshow_ch12_daffodils_companion:
    # THE COMPANION ending — friendship, Plymouth, togetherness
    stop music fadeout 1.0
    play music "audio/songs/daffodils_in_the_snow.ogg" noloop

    scene bg_plymouth_hoe_day with dissolve
    pause 12.0
    scene bg_flat_kitchen with dissolve
    pause 12.0
    scene bg_london_cafe with dissolve
    pause 12.0
    scene bg_campus_quad with dissolve
    pause 12.0
    scene bg_plymouth_hoe_day with dissolve
    pause 15.0

    scene bg_flat_kitchen with dissolve
    pause 12.0
    scene bg_london_cafe with dissolve
    pause 12.0
    scene bg_plymouth_hoe_day with dissolve
    pause 12.0
    scene bg_campus_quad with dissolve
    pause 12.0
    scene bg_flat_kitchen with dissolve
    pause 15.0

    scene bg_plymouth_hoe_day with dissolve
    pause 12.0
    scene bg_london_cafe with dissolve
    pause 12.0
    scene bg_campus_quad with dissolve
    pause 12.0
    scene bg_plymouth_hoe_day with dissolve
    pause 12.0

    stop music fadeout 2.0
    return

label slideshow_ch12_daffodils_healer:
    # THE HEALER ending — care, counselling, quiet strength
    stop music fadeout 1.0
    play music "audio/songs/daffodils_in_the_snow.ogg" noloop

    scene bg_amelia_home with dissolve
    pause 12.0
    scene bg_counsellor_office with dissolve
    pause 12.0
    scene bg_plymouth_hoe_dawn with dissolve
    pause 12.0
    scene bg_amelia_home with dissolve
    pause 12.0
    scene bg_counsellor_office with dissolve
    pause 15.0

    scene bg_plymouth_hoe_dawn with dissolve
    pause 12.0
    scene bg_amelia_home with dissolve
    pause 12.0
    scene bg_counsellor_office with dissolve
    pause 12.0
    scene bg_plymouth_hoe_dawn with dissolve
    pause 15.0
    scene bg_amelia_home with dissolve
    pause 12.0

    scene bg_counsellor_office with dissolve
    pause 12.0
    scene bg_plymouth_hoe_dawn with dissolve
    pause 12.0
    scene bg_amelia_home with dissolve
    pause 12.0
    scene bg_counsellor_office with dissolve
    pause 12.0

    stop music fadeout 2.0
    return

label slideshow_ch12_daffodils_whole:
    # THE WHOLE ending — integration, everywhere, all of it
    stop music fadeout 1.0
    play music "audio/songs/daffodils_in_the_snow.ogg" noloop

    scene bg_london_train with dissolve
    pause 12.0
    scene bg_plymouth_hoe_day with dissolve
    pause 12.0
    scene bg_cornwall_coast with dissolve
    pause 12.0
    scene bg_amelia_home with dissolve
    pause 12.0
    scene bg_london_train with dissolve
    pause 12.0

    scene bg_flat_kitchen with dissolve
    pause 12.0
    scene bg_plymouth_hoe_dawn with dissolve
    pause 12.0
    scene bg_bodmin_moor with dissolve
    pause 12.0
    scene bg_london_train with dissolve
    pause 12.0
    scene bg_campus_quad with dissolve
    pause 12.0

    scene bg_plymouth_hoe_day with dissolve
    pause 12.0
    scene bg_cornwall_coast with dissolve
    pause 12.0
    scene bg_amelia_home with dissolve
    pause 12.0
    scene bg_plymouth_hoe_dawn with dissolve
    pause 12.0

    stop music fadeout 2.0
    return

label slideshow_ch12_daffodils_bittersweet:
    # THE BITTERSWEET ending — some gold, some lead, the journey
    stop music fadeout 1.0
    play music "audio/songs/daffodils_in_the_snow.ogg" noloop

    scene bg_london_train with dissolve
    pause 12.0
    scene bg_plymouth_hoe_day with dissolve
    pause 12.0
    scene bg_amelia_room_plymouth_day with dissolve
    pause 12.0
    scene bg_london_train with dissolve
    pause 12.0
    scene bg_cornwall_coast with dissolve
    pause 15.0

    scene bg_amelia_home with dissolve
    pause 12.0
    scene bg_plymouth_hoe_day with dissolve
    pause 12.0
    scene bg_london_train with dissolve
    pause 12.0
    scene bg_amelia_room_plymouth_day with dissolve
    pause 12.0
    scene bg_cornwall_coast with dissolve
    pause 15.0

    scene bg_london_train with dissolve
    pause 12.0
    scene bg_plymouth_hoe_day with dissolve
    pause 12.0
    scene bg_amelia_home with dissolve
    pause 12.0
    scene bg_london_train with dissolve
    pause 12.0

    stop music fadeout 2.0
    return
