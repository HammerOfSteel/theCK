## The CK: Amelia V2 — Options & Build Configuration
##
## Game identity, audio settings, transitions, save directory, and build config.
##

################################################################################
## Basics
################################################################################

define config.name = _("The CK: Amelia")

define config.version = "2.0-dev"

define build.name = "TheCK"

## Text shown on the About screen (between triple-quotes, blank lines = paragraphs)
define gui.about = _p("""
{b}The CK: Amelia{/b} is a choice-driven visual novel about a young psychology student's transformative first year at the University of Plymouth — where Jungian shadows, Cornish folklore, and the quiet alchemy of growing up collide.

Written and developed by Hammer of Steel.

{b}Content Notice{/b}
This game explores themes of mental health, depression, anxiety, and suicide. It is handled with care and respect, but if you are affected by these topics, please reach out:

{b}Samaritans{/b} — 116 123 (UK, 24/7, free)
{b}Mind{/b} — 0300 123 3393
{b}Crisis Text Line{/b} — Text SHOUT to 85258
{b}International Association for Suicide Prevention{/b} — https://www.iasp.info/resources/Crisis_Centres/
""")

################################################################################
## Screen Dimensions (defined in gui.rpy at init -2)
################################################################################

################################################################################
## Sound & Music
################################################################################

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

## Voice configuration
define config.voice_filename_format = "{filename}"

## Main menu music — managed by music_player.rpy playlist
# define config.main_menu_music = "audio/songs/Amelia.ogg"

## Uncomment when sample files exist:
# define config.sample_sound = "audio/sfx/sample.ogg"

################################################################################
## Window Management
################################################################################

define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

################################################################################
## Transitions
################################################################################

define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None
define config.enter_yesno_transition = dissolve
define config.exit_yesno_transition = dissolve
define config.enter_replay_transition = dissolve
define config.exit_replay_transition = dissolve

################################################################################
## Preference Defaults
################################################################################

default preferences.text_cps = 30
default preferences.afm_time = 15

################################################################################
## Save Directory
################################################################################
## Must be a literal string. Once set, do not change.

define config.save_directory = "TheCK-Amelia-V2"

################################################################################
## Taskbar Icon
################################################################################

define config.window_icon = "gui/window_icon.png"

################################################################################
## Build Configuration
################################################################################

init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.documentation('*.html')
    build.documentation('*.txt')
