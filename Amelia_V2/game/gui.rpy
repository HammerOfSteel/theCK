## The CK: Amelia V2 — GUI Configuration
##
## This file sets all GUI properties: colours, sizes, fonts, textbox, menus.
## Alchemical phase colours shift based on chapter progress.

################################################################################
## Init
################################################################################

init offset = -2

################################################################################
## Colour Palette — Alchemical Phases
################################################################################

## These are used throughout the GUI. The active palette changes by chapter
## via the set_phase() function in definitions.rpy.

define gui.accent_color = "#D4A574"               # Warm amber (default/Nigredo)
define gui.idle_color = "#AAAAAA"
define gui.idle_small_color = "#888888"
define gui.hover_color = "#E8C8A0"
define gui.selected_color = "#D4A574"
define gui.insensitive_color = "#555555"
define gui.muted_color = "#6A6A5A"
define gui.hover_muted_color = "#8A8A7A"
define gui.text_color = "#E8DCC8"                  # Warm parchment

## Phase accent colours — referenced by screens for dynamic colouring
define gui.NIGREDO_ACCENT = "#D4A574"              # Burnt umber / warm amber
define gui.NIGREDO_BG = "#1A1410"                  # Deep warm dark
define gui.ALBEDO_ACCENT = "#A8C0D4"               # Sea grey / cool silver
define gui.ALBEDO_BG = "#141A1E"                   # Deep cool dark
define gui.CITRINITAS_ACCENT = "#DAA520"            # Goldenrod / saffron
define gui.CITRINITAS_BG = "#1A1810"               # Deep warm gold-dark
define gui.RUBEDO_ACCENT = "#C04040"               # Wine / cinnabar
define gui.RUBEDO_BG = "#1A1014"                   # Deep wine dark

################################################################################
## Fonts
################################################################################

## The default font. Can be swapped for a custom .ttf in game/fonts/
define gui.text_font = gui.preference("font_family", "DejaVuSans.ttf")
define gui.name_text_font = "DejaVuSans.ttf"
define gui.interface_text_font = "DejaVuSans.ttf"

## If you add custom fonts, place .ttf files in game/fonts/ and use e.g.:
## define gui.text_font = "fonts/Lora-Regular.ttf"
## define gui.name_text_font = "fonts/Lora-Bold.ttf"

################################################################################
## Resolution & Scaling
################################################################################

define config.screen_width = 1920
define config.screen_height = 1080

define gui.text_size = 28
define gui.name_text_size = 32
define gui.interface_text_size = 28
define gui.label_text_size = 36
define gui.notify_text_size = 22
define gui.title_text_size = 64

################################################################################
## Main Menu & Game Menu
################################################################################

define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"

## About screen text
define gui.about = _p("""
{b}The CK: Amelia{/b}

A visual novel about identity, friendship, and the alchemy of growing up.

Written by Erik S.
Music by Dancing Salamanders / Geddon Bird.

Built with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].
""")

define build.name = "TheCK"
define config.name = _("The CK: Amelia")
define config.version = "0.1.0"

define config.has_sound = True
define config.has_music = True
define config.has_voice = False

define config.main_menu_music = "audio/songs/Amelia.wav"

################################################################################
## Dialogue — Say Screen
################################################################################

## Textbox
define gui.textbox_height = 278
define gui.textbox_yalign = 1.0

## Character name
define gui.name_xpos = 360
define gui.name_ypos = 0
define gui.name_xalign = 0.0
define gui.namebox_width = None
define gui.namebox_height = None
define gui.namebox_borders = Borders(5, 5, 5, 5)
define gui.namebox_tile = False

## Dialogue text
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75
define gui.dialogue_width = 1116
define gui.dialogue_text_xalign = 0.0

################################################################################
## Choice Buttons
################################################################################

## Base button properties (used by all button types via gui.button_properties)
define gui.button_width = None
define gui.button_height = None
define gui.button_borders = Borders(6, 6, 6, 6)
define gui.button_tile = False
define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size
define gui.button_text_xalign = 0.0
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## Type-specific button properties — used by gui.button_properties("type")
define gui.radio_button_borders = Borders(27, 6, 6, 6)
define gui.check_button_borders = Borders(27, 6, 6, 6)
define gui.confirm_button_text_xalign = 0.5
define gui.page_button_borders = Borders(15, 6, 15, 6)
define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color
define gui.navigation_button_width = 290

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#CCCCCC"
define gui.choice_button_text_hover_color = "#FFFFFF"
define gui.choice_button_text_insensitive_color = "#444444"

################################################################################
## File Slot Buttons (Save/Load)
################################################################################

define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 20
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

define config.thumbnail_width = 384
define config.thumbnail_height = 216

define gui.file_slot_cols = 3
define gui.file_slot_rows = 2

################################################################################
## Spacing
################################################################################

define gui.navigation_spacing = 6
define gui.pref_spacing = 15
define gui.pref_button_spacing = 0
define gui.page_spacing = 0
define gui.slot_spacing = 15
define gui.choice_spacing = 33

################################################################################
## Frames
################################################################################

define gui.frame_borders = Borders(6, 6, 6, 6)
define gui.frame_tile = False
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)
define gui.skip_frame_borders = Borders(24, 8, 75, 8)
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

################################################################################
## Navigation / Quick Menu
################################################################################

define gui.navigation_xpos = 60
define gui.skip_indicator_borders = Borders(24, 8, 60, 8)

################################################################################
## Scrollbars
################################################################################

define gui.scrollbar_size = 18
define gui.scrollbar_tile = False
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)

define gui.unscrollable = "hide"

################################################################################
## Bars
################################################################################

define gui.bar_size = 38
define gui.bar_tile = False
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.vbar_borders = Borders(6, 6, 6, 6)

################################################################################
## Sliders
################################################################################

define gui.slider_size = 38
define gui.slider_tile = False
define gui.slider_borders = Borders(6, 6, 6, 6)

################################################################################
## History (Dialogue Log)
################################################################################

define config.history_length = 250

define gui.history_height = 210
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0

################################################################################
## NVL Mode (not used but defined for safety)
################################################################################

define gui.nvl_height = 173
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0

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
## Window auto/show/hide
################################################################################

define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

################################################################################
## Preference defaults
################################################################################

default preferences.text_cps = 30
default preferences.afm_time = 15

################################################################################
## Sound channel configuration
################################################################################

init python:
    ## Allow ambient sounds on the sound channel or create a dedicated one
    renpy.music.register_channel("ambient", mixer="sfx", loop=True)
