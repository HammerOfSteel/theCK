## The CK: Amelia V2 — Master Definitions
## All characters, variables, flags, and configuration for the full game.

init offset = -2

init python:
    gui.init(1920, 1080)

define config.check_conflicting_properties = True

###############################################################################
## CHARACTERS
###############################################################################

## Protagonist
define a = Character("Amelia", color="#D4A574")
define amelia = Character("Amelia", color="#D4A574")

## Amelia's internal monologue — rendered in italics, no name shown
define thought = Character(None, what_italic=True, what_color="#E8DCC8")

## Phone screen text — for texting scenes
define phone = Character(None, what_color="#FFD700", what_size=22)

## Core Cast
define ella = Character("Ella", color="#FFD700")
define lucas = Character("Lucas", color="#7BA7BC")
define zara = Character("Zara", color="#C0392B")
define raj = Character("Raj", color="#E8A87C")
define sarah = Character("Sarah", color="#A8B5C5")
define liz = Character("Liz", color="#40E0D0")
define maya = Character("Maya", color="#2E8B57")

## Antagonists / Complicators
define tasha = Character("Tasha", color="#FFB6C1")
define sophia = Character("Sophia", color="#708090")

## Mentors
define hawthorne = Character("Prof. Hawthorne", color="#808000")
define simmons = Character("Dr. Simmons", color="#800020")
define elena = Character("Elena", color="#A8B5C5")

## Family
define david = Character("David", color="#808080")
define grace = Character("Grace", color="#E8A87C")
define lily = Character("Lily", color="#FF4040")

## Minor / Utility
define michael = Character("Michael", color="#8B0000")
define mr_osei = Character("Mr. Osei", color="#8B6914")
define narrator = Character(None)

###############################################################################
## STATS — The Hidden Karma System (all stats invisible to the player)
###############################################################################

## Academic Achievement
default stat_aa = 0
## Social Intelligence
default stat_si = 0
## Mental Health
default stat_mh = 0
## Self-Discovery
default stat_sd = 0
## Moral Courage
default stat_mc = 0
## Occult Knowledge
default stat_ok = 0

###############################################################################
## RELATIONSHIPS — Tracked per character, starting values per design
###############################################################################

default rel_ella = 6        # Childhood best friend — starts high
default rel_lucas = 0
default rel_zara = 0
default rel_raj = 1          # Natural warmth — slight head start
default rel_sarah = 0
default rel_liz = 0
default rel_maya = 0
default rel_tasha = -2       # Starts hostile
default rel_sophia = -1      # Starts cool
default rel_mentor = 0       # Whichever mentor is assigned
default rel_lily = 0
default rel_michael = 0
default rel_parents = 0

###############################################################################
## FLAGS — Story branching, unlock conditions, narrative memory
###############################################################################

## Elena unlock keys (all three required)
default elena_key_paracelsus = False    # Bought the Paracelsus book (Ch1.5C)
default elena_key_ceremony = False      # Attended Maya's ceremony (Ch3.5A)
default elena_key_ok_threshold = False  # OK ≥ 5 by end of Ch3

## Mentor assignment
default mentor_path = None              # "hawthorne", "simmons", "maya", "elena"
default elena_path_complete = False

## Sarah-specific
default sarah_bench_choice = None       # "honest", "clinical", "dismissive"
default sarah_room_visited = False
default sarah_alarm_acted = False
default sarah_alarm_denied = False
default sarah_score = 0
default sarah_outcome = None            # "full_save", "late_save", "partial_save", "tragic"
default sarah_alive = True

## Chapter 1 memory
default ch1_reading = None              # "kahneman", "jung", "tibetan"
default ch1_ella_response = None        # "promise", "honest"
default ch1_dinner_speech = None        # "degree", "self", "esoteric"
default ch1_packing = None              # "flashcards", "photo", "journal"
default ch1_bookshop = None             # "psychology", "rilke", "paracelsus"
default ch1_thames = None               # "proud", "terrified", "watches"

## Ending
default ending = None

###############################################################################
## UTILITY FUNCTIONS
###############################################################################

init python:

    def clamp_stat(value):
        """Floor all stats at 0."""
        return max(0, value)

    def add_stat(stat_name, delta):
        """Safely modify a stat with floor clamping."""
        current = getattr(store, stat_name)
        setattr(store, stat_name, clamp_stat(current + delta))

    def add_rel(rel_name, delta):
        """Modify a relationship value."""
        current = getattr(store, rel_name)
        setattr(store, rel_name, current + delta)

    def calculate_sarah_score():
        """Calculate the Sarah Score at Chapter 8."""
        score = (store.rel_sarah * 3) + store.stat_mh + store.stat_si + store.stat_mc + int(store.rel_ella * 0.5)
        if store.mentor_path == "elena" and store.stat_ok >= 18:
            score += 10
        store.sarah_score = score
        if score >= 45:
            store.sarah_outcome = "full_save"
        elif score >= 30:
            store.sarah_outcome = "late_save"
        elif score >= 15:
            store.sarah_outcome = "partial_save"
        else:
            store.sarah_outcome = "tragic"
            store.sarah_alive = False
