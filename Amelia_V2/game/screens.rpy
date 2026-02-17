## The CK: Amelia V2 — Screens
##
## All screen definitions: standard Ren'Py screens (say, choice, main_menu,
## save, load, preferences, etc.) plus custom screens (journal, phone,
## content_warning).

################################################################################
## Alchemical Phase — Dynamic Colour Helper
################################################################################

init python:

    ## ── Video Background Pools ──────────────────────────────────────────
    ## Each menu picks a random video on show.  Add / remove paths as needed.

    main_menu_videos = [
        "videos/main_menu_0.mp4",
        "videos/main_menu_1.mp4",
        "videos/main_menu_2.mp4",
        "videos/main_menu_3.mp4",
    ]
    save_load_videos = [
        "videos/save_load_menu_1.mp4",
        "videos/save_load_menu_2.mp4",
        "videos/save_load_menu_3.mp4",
    ]
    history_videos = [
        "videos/history_log_menu_1.mp4",
        "videos/history_log_menu_2.mp4",
    ]
    preferences_videos = [
        "videos/option_settings_menu_1.mp4",
        "videos/option_settings_menu_2.mp4",
    ]
    about_videos = [
        "videos/about_credits_menu_1.mp4",
        "videos/about_credits_menu_2.mp4",
    ]

    def _pick_video(pool):
        """Return a random loadable video from *pool*, or None."""
        loadable = [v for v in pool if renpy.loadable(v)]
        if loadable:
            return renpy.random.choice(loadable)
        return None

    ## ── Alchemical Phase Helpers ─────────────────────────────────────────

    def get_phase_accent():
        """Return the accent colour for the current alchemical phase."""
        ch = getattr(store, "current_chapter", 1)
        if ch <= 3:
            return gui.NIGREDO_ACCENT
        elif ch <= 7:
            return gui.ALBEDO_ACCENT
        elif ch <= 9:
            return gui.CITRINITAS_ACCENT
        else:
            return gui.RUBEDO_ACCENT

    def get_phase_bg():
        """Return the background tint for the current alchemical phase."""
        ch = getattr(store, "current_chapter", 1)
        if ch <= 3:
            return gui.NIGREDO_BG
        elif ch <= 7:
            return gui.ALBEDO_BG
        elif ch <= 9:
            return gui.CITRINITAS_BG
        else:
            return gui.RUBEDO_BG

    def get_phase_name():
        """Return the alchemical phase name."""
        ch = getattr(store, "current_chapter", 1)
        if ch <= 3:
            return "Nigredo"
        elif ch <= 7:
            return "Albedo"
        elif ch <= 9:
            return "Citrinitas"
        else:
            return "Rubedo"

################################################################################
## Say Screen — Displays dialogue
################################################################################

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    ## Quick menu at the bottom
    use quick_menu

## Styles for the say screen
style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Frame("gui/textbox.png", xalign=0.5, yalign=1.0) if renpy.loadable("gui/textbox.png") else Frame(Solid("#00000099"), 0, 0, 0, 0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile) if renpy.loadable("gui/namebox.png") else None
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    text_align gui.dialogue_text_xalign
    layout ("subtitle" if gui.dialogue_text_xalign else "tex")

################################################################################
## Input Screen — For text input (player naming, etc.)
################################################################################

screen input(prompt):
    style_prefix "input"

    window:
        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default
style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width

################################################################################
## Choice Screen — Player decisions
################################################################################
## Custom: choice buttons tinted by current alchemical phase.

screen choice(items):
    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 33

        for i in items:
            textbutton i.caption:
                action i.action
                style "choice_button"

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5
    spacing 33

style choice_button is default:
    properties gui.button_properties("choice_button")
    xsize gui.choice_button_width
    ## Phase-coloured background — falls back to solid if no image
    background Frame(Solid(get_phase_accent() + "33"), gui.choice_button_borders)
    hover_background Frame(Solid(get_phase_accent() + "66"), gui.choice_button_borders)
    padding gui.choice_button_borders.padding

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    text_align 0.5
    layout "subtitle"

################################################################################
## Quick Menu — In-game navigation overlay
################################################################################

screen quick_menu():
    zorder 100

    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 1.0
            yoffset -8

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu("history")
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu("save")
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu("preferences")

init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    size 18

################################################################################
## Main Menu
################################################################################

screen main_menu():
    tag menu

    ## Dark fallback behind video
    add Solid("#1A1410")

    ## Video background — random pick each time the menu is shown
    default mm_video = _pick_video(main_menu_videos)
    if mm_video:
        add Movie(play=mm_video, loop=True, size=(config.screen_width, config.screen_height))

    frame:
        style "main_menu_frame"

    use navigation

    ## Game title
    text "{size=72}{color=#D4A574}The CK: Amelia{/color}{/size}":
        xalign 0.05
        yalign 0.2

    text "{size=28}{color=#E8DCC888}A visual novel about identity, friendship,\nand the alchemy of growing up.{/color}{/size}":
        xalign 0.05
        yalign 0.3

    ## Version number
    if gui.show_name:
        text "[config.version]":
            style "main_menu_version"

style main_menu_frame is empty
style main_menu_frame:
    xsize 420
    yfill True
    background Solid("#1A141099")

style main_menu_vbox is vbox
style main_menu_vbox:
    xalign 0.05
    xoffset 30
    xmaximum 360
    yalign 0.6

style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text:
    color "#FFFFFF33"
    size 20
    xalign 0.98
    yalign 0.98

define gui.show_name = True

################################################################################
## Navigation — Shared menu buttons
################################################################################

screen navigation():
    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.6

        spacing 6

        if main_menu:
            textbutton _("Start") action Start()
        else:
            textbutton _("History") action ShowMenu("history")
            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):
            textbutton _("Quit") action Quit(confirm=not main_menu)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

################################################################################
## Game Menu — Base frame for save/load/preferences
################################################################################

screen game_menu(title, scroll=None, yinitial=0.0, video_bg=None):
    style_prefix "game_menu"

    ## Dark fallback always present
    add Solid("#1A1410")

    ## Video background (passed from calling screen)
    if video_bg:
        add Movie(play=video_bg, loop=True, size=(config.screen_width, config.screen_height))
    elif main_menu:
        ## Fallback to main menu image if no video supplied
        if renpy.loadable(gui.main_menu_background):
            add gui.main_menu_background
    else:
        if renpy.loadable(gui.game_menu_background):
            add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True
                        vbox:
                            transclude
                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True
                        transclude
                else:
                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"
        action Return()

    label title:
        style "game_menu_label"

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180
    background Solid("#1A141099")

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_label is gui_label
style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text is gui_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button is navigation_button
style return_button_text is navigation_button_text

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45

################################################################################
## Save / Load Screens
################################################################################

screen save():
    tag menu
    default save_video = _pick_video(save_load_videos)
    use file_slots(_("Save"), save_video)

screen load():
    tag menu
    default load_video = _pick_video(save_load_videos)
    use file_slots(_("Load"), load_video)

screen file_slots(title, video_bg=None):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title, video_bg=video_bg):
        fixed:
            order_reverse True

            ## Page selector
            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0
                spacing 25

                textbutton _("<") action FilePagePrevious()
                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")
                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()

            ## Save slots grid
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing 15

                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    button:
                        action FileAction(slot)
                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text

style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")
    xsize gui.slot_button_width
    ysize gui.slot_button_height

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    size gui.slot_button_text_size
    xalign gui.slot_button_text_xalign
    text_align gui.slot_button_text_xalign

################################################################################
## Preferences Screen
################################################################################

screen preferences():
    tag menu
    default pref_video = _pick_video(preferences_videos)
    use game_menu(_("Preferences"), scroll="viewport", video_bg=pref_video):
        vbox:
            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("skip", "after choices")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Content warnings toggle
                vbox:
                    style_prefix "check"
                    label _("Content")
                    textbutton _("Show Warnings") action ToggleVariable("show_content_warnings", True, False)

            null height 15

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:
                    label _("Text Speed")
                    bar value Preference("text speed")

                vbox:
                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")

                if config.has_music:
                    vbox:
                        label _("Music Volume")
                        hbox:
                            bar value Preference("music volume")

                if config.has_sound:
                    vbox:
                        label _("Sound Volume")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)

## Content warnings preference variable
default show_content_warnings = True

style pref_label is gui_label
style pref_label_text is gui_label_text
style radio_label is pref_label
style radio_label_text is pref_label_text
style check_label is pref_label
style check_label_text is pref_label_text
style slider_label is pref_label
style slider_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style check_button is gui_button
style check_button_text is gui_button_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style pref_label:
    top_margin 15
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox is pref_vbox
style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png" if renpy.loadable("gui/button/radio_idle_foreground.png") else None

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox is pref_vbox
style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png" if renpy.loadable("gui/button/check_idle_foreground.png") else None

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675

################################################################################
## History Screen — Dialogue log
################################################################################

screen history():
    tag menu
    default hist_video = _pick_video(history_videos)
    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, video_bg=hist_video):
        style_prefix "history"

        for h in _history_list:
            window:
                has fixed:
                    yfit True

                if h.who:
                    label h.who:
                        style "history_name"
                        substitute False
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")

define gui.history_allow_tags = { "b", "i", "u", "s", "color", "size" }

style history_window is empty
style history_window:
    xfill True
    ysize gui.history_height

style history_name is gui_label
style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text is gui_label_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text is gui_text
style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label is gui_label
style history_label_text is gui_label_text

################################################################################
## About Screen
################################################################################

screen about():
    tag menu
    default about_video = _pick_video(about_videos)
    use game_menu(_("About"), scroll="viewport", video_bg=about_video):
        style_prefix "about"

        vbox:
            label "[config.name!t]"
            text _("Version [config.version!t]\n")
            if gui.about:
                text "[gui.about!t]\n"

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

################################################################################
## Help Screen
################################################################################

screen help():
    tag menu
    default tab = "keyboard"
    default help_video = _pick_video(about_videos)
    use game_menu(_("Help"), scroll="viewport", video_bg=help_video):
        style_prefix "help"

        vbox:
            spacing 23

            hbox:
                textbutton _("Keyboard") action SetScreenVariable("tab", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("tab", "mouse")

            if tab == "keyboard":
                use keyboard_help
            elif tab == "mouse":
                use mouse_help

screen keyboard_help():
    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")
    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")
    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")
    hbox:
        label _("Escape")
        text _("Accesses the game menu.")
    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")
    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")
    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")
    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")
    hbox:
        label "H"
        text _("Hides the user interface.")
    hbox:
        label "S"
        text _("Takes a screenshot.")
    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

screen mouse_help():
    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")
    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")
    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")
    hbox:
        label _("Mouse Wheel Up / Click Rollback Side")
        text _("Rolls back to earlier dialogue.")
    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")

style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0

################################################################################
## Confirm Screen — Yes/No prompts
################################################################################

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"

    add Solid("#00000088")

    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    key "game_menu" action no_action

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_button
style confirm_button_text is gui_button_text

style confirm_frame:
    background Frame(Solid("#1A1410EE"), gui.confirm_frame_borders) if True else Frame("gui/overlay/confirm.png", gui.confirm_frame_borders)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")

define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

################################################################################
## Skip Indicator
################################################################################

screen skip_indicator():
    zorder 100
    style_prefix "skip"

    frame:
        hbox:
            spacing 9
            text _("Skipping")
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

transform delayed_blink(delay, cycle):
    alpha .5
    pause delay
    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .6)
        repeat

style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_indicator_borders.top
    background Frame(Solid("#00000066"), gui.skip_indicator_borders)
    padding gui.skip_indicator_borders.padding

style skip_text:
    size 24

style skip_triangle:
    font "DejaVuSans.ttf"

################################################################################
## Notify Screen — Quick messages
################################################################################

screen notify(message):
    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide("notify")

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos 68
    background Frame(Solid("#00000088"), 24, 8, 60, 8)
    padding Borders(24, 8, 60, 8).padding

style notify_text:
    properties gui.text_properties("notify")

################################################################################
## NVL Screen (not used but required)
################################################################################

screen nvl(dialogue, items=None):
    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        use nvl_dialogue(dialogue)

        for i in items:
            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0

screen nvl_dialogue(dialogue):
    for d in dialogue:
        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is not None

                if d.who is not None:
                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id

define gui.nvl_spacing = 15

style nvl_window is default
style nvl_entry is default
style nvl_label is say_label
style nvl_dialogue is say_dialogue
style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True
    background Solid("#000000CC")
    padding Borders(0, 15, 0, 30).padding

################################################################################
## CUSTOM: Content Warning Screen
################################################################################
## Called before scenes with sensitive content. Shows a warning overlay
## that the player can dismiss or skip.

screen content_warning(warning_text="This scene contains sensitive content.", details=""):
    modal True
    zorder 150
    style_prefix "cw"

    add Solid("#000000DD")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 500
        background Solid("#1A1410EE")
        padding (60, 40, 60, 40)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20

            text "{size=42}{color=#DAA520}⚠ Content Notice{/color}{/size}":
                xalign 0.5

            null height 10

            text "[warning_text]":
                xalign 0.5
                text_align 0.5
                color "#E8DCC8"
                size 28

            if details:
                text "{size=22}{color=#AAAAAA}[details]{/color}{/size}":
                    xalign 0.5
                    text_align 0.5

            null height 20

            hbox:
                xalign 0.5
                spacing 40

                textbutton "Continue":
                    action Hide("content_warning")
                    text_size 28
                    text_color "#D4A574"
                    text_hover_color "#E8C8A0"

            text "{size=18}{color=#888888}Content warnings can be toggled in Preferences.{/color}{/size}":
                xalign 0.5

################################################################################
## CUSTOM: Journal Screen
################################################################################
## An in-game journal that tracks Amelia's progress without revealing
## exact stat numbers. Themed as a leather-bound notebook.

screen journal():
    tag menu
    modal True
    zorder 100

    add Solid("#000000CC")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1000
        ysize 700
        background "images/ui/journal_bg.png" if renpy.loadable("images/ui/journal_bg.png") else Solid("#2A201A")
        padding (60, 40, 60, 40)

        vbox:
            spacing 10

            ## Title
            text "{size=40}{color=#D4A574}Amelia's Journal{/color}{/size}":
                xalign 0.5

            null height 10

            ## Current phase indicator
            text "{size=24}{color=#AAAAAA}Current Phase: [get_phase_name()]{/color}{/size}":
                xalign 0.5

            null height 15

            ## Stat reflections — qualitative, not numeric
            hbox:
                spacing 30
                xalign 0.5

                ## Left column
                vbox:
                    xsize 400
                    spacing 8
                    text "{b}Academic Journey{/b}" color "#E8DCC8" size 24

                    if stat_aa >= 15:
                        text "I feel confident in my studies." color "#A8C0A8" size 20
                    elif stat_aa >= 8:
                        text "I'm finding my academic footing." color "#E8DCC8" size 20
                    else:
                        text "Studies feel overwhelming right now." color "#C0A8A8" size 20

                    null height 8
                    text "{b}Connections{/b}" color "#E8DCC8" size 24

                    if stat_si >= 15:
                        text "I've learned to truly listen to others." color "#A8C0A8" size 20
                    elif stat_si >= 8:
                        text "I'm getting better at reading people." color "#E8DCC8" size 20
                    else:
                        text "I still struggle with social situations." color "#C0A8A8" size 20

                    null height 8
                    text "{b}Inner Peace{/b}" color "#E8DCC8" size 24

                    if stat_mh >= 15:
                        text "I feel grounded and at peace." color "#A8C0A8" size 20
                    elif stat_mh >= 8:
                        text "Some days are harder than others." color "#E8DCC8" size 20
                    else:
                        text "My mind feels very unsettled." color "#C0A8A8" size 20

                ## Right column
                vbox:
                    xsize 400
                    spacing 8
                    text "{b}Self-Knowledge{/b}" color "#E8DCC8" size 24

                    if stat_sd >= 15:
                        text "I'm beginning to understand who I am." color "#A8C0A8" size 20
                    elif stat_sd >= 8:
                        text "The mirror is getting clearer." color "#E8DCC8" size 20
                    else:
                        text "I don't quite know myself yet." color "#C0A8A8" size 20

                    null height 8
                    text "{b}Courage{/b}" color "#E8DCC8" size 24

                    if stat_mc >= 15:
                        text "I can face difficult truths." color "#A8C0A8" size 20
                    elif stat_mc >= 8:
                        text "I'm learning when to speak up." color "#E8DCC8" size 20
                    else:
                        text "I tend to avoid confrontation." color "#C0A8A8" size 20

                    null height 8
                    text "{b}Curiosities{/b}" color "#E8DCC8" size 24

                    if stat_ok >= 15:
                        text "The hidden world feels familiar now." color "#A8C0A8" size 20
                    elif stat_ok >= 8:
                        text "I sense there's more beneath the surface." color "#E8DCC8" size 20
                    else:
                        text "The ordinary world is enough for me." color "#C0A8A8" size 20

            null height 15

            ## Key relationships (shown qualitatively)
            text "{size=24}{color=#D4A574}People on my mind:{/color}{/size}":
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 20

                if rel_ella >= 4:
                    text "{size=20}{color=#FFD700}Ella ♡{/color}{/size}"
                if rel_sarah >= 3:
                    text "{size=20}{color=#A8B5C5}Sarah{/color}{/size}"
                if rel_lucas >= 3:
                    text "{size=20}{color=#7BA7BC}Lucas{/color}{/size}"
                if rel_zara >= 3:
                    text "{size=20}{color=#C0392B}Zara{/color}{/size}"
                if rel_raj >= 3:
                    text "{size=20}{color=#E8A87C}Raj{/color}{/size}"
                if rel_maya >= 3:
                    text "{size=20}{color=#2E8B57}Maya{/color}{/size}"
                if mentor_path:
                    text "{size=20}{color=#808000}[mentor_path.capitalize()]{/color}{/size}"

        ## Close button
        textbutton "✕":
            xalign 1.0
            yalign 0.0
            text_size 36
            text_color "#AAAAAA"
            text_hover_color "#FFFFFF"
            action Hide("journal")

################################################################################
## CUSTOM: Phone Screen
################################################################################
## Overlay for texting scenes. Shows a phone frame with messages.

screen phone_overlay(messages=None):
    zorder 50

    frame:
        xalign 0.85
        yalign 0.5
        xsize 420
        ysize 720
        background "images/ui/phone_frame.png" if renpy.loadable("images/ui/phone_frame.png") else Solid("#111111")
        padding (30, 60, 30, 30)

        vbox:
            spacing 8
            yalign 1.0

            if messages:
                for sender, msg in messages:
                    frame:
                        xsize 340
                        if sender == "amelia":
                            xalign 1.0
                            background Solid("#D4A57444")
                        else:
                            xalign 0.0
                            background Solid("#FFD70033")
                        padding (12, 8, 12, 8)

                        text "[msg]":
                            size 20
                            color "#E8DCC8"

################################################################################
## CUSTOM KEYBIND — Journal access via J key
################################################################################

init python:
    config.keymap["game_menu"].append("j")

## Allow toggling journal from in-game
init python:
    config.overlay_screens.append("journal_hint")

screen journal_hint():
    if not main_menu:
        textbutton "{size=18}{color=#AAAAAA88}[J] Journal{/color}{/size}":
            xalign 0.98
            yalign 0.02
            action ShowMenu("journal")
