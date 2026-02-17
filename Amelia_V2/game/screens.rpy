## The CK: Amelia V2 — Screens
##
## All screen definitions: standard Ren'Py screens (say, choice, main_menu,
## save, load, preferences, etc.) plus custom screens (journal, phone,
## content_warning).
##
################################################################################
## Alchemical Phase — Dynamic Colour Helper
################################################################################

init python:

    ## ── Video Background Pools ──────────────────────────────────────────
    ## Each menu picks a random video on show.  Add / remove paths as needed.

    main_menu_videos = [
        "videos/main_menu_0.webm",
        "videos/main_menu_1.webm",
        "videos/main_menu_2.webm",
        "videos/main_menu_3.webm",
    ]
    save_load_videos = [
        "videos/save_load_menu_1.webm",
        "videos/save_load_menu_2.webm",
        "videos/save_load_menu_3.webm",
    ]
    history_videos = [
        "videos/history_log_menu_1.webm",
        "videos/history_log_menu_2.webm",
    ]
    preferences_videos = [
        "videos/option_settings_menu_1.webm",
        "videos/option_settings_menu_2.webm",
    ]
    about_videos = [
        "videos/about_credits_menu_1.webm",
        "videos/about_credits_menu_2.webm",
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
    background Frame("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile)
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

## Persistent main-menu video — picked once, reused across menu returns
## We cache the Movie *object* so Ren'Py recognises it as the same displayable
## and doesn't restart playback when the screen rebuilds after a sub-menu visit.
default _mm_movie = None

init python:
    def _ensure_mm_video():
        """Pick a main-menu video once per session and cache the Movie object."""
        if store._mm_movie is None:
            v = _pick_video(main_menu_videos)
            if v:
                store._mm_movie = Movie(play=v, loop=True)

screen main_menu():
    tag menu

    ## Ensure playlist is running (won't restart if already playing)
    ## and pick the background video once per session
    on "show" action [Function(_ensure_mm_video), Function(menu_playlist.ensure_playing)]
    on "replace" action Function(menu_playlist.ensure_playing)

    ## Dark fallback behind video
    add Solid("#0A0A0A")

    ## Video background — same cached Movie object, no restart on re-render
    if _mm_movie:
        add _mm_movie

    ## Slight dark overlay so text is always readable over video
    add Solid("#00000044")

    ## Centered UI container
    frame:
        background None
        align (0.5, 0.5)

        vbox:
            spacing 20
            xalign 0.5

            ## Title
            text "AMELIA":
                style "main_menu_title"
                xalign 0.5

            ## Alchemical divider line
            null height 5
            frame:
                xalign 0.5
                xsize 120
                ysize 2
                background Solid("#D4A574")
            null height 15

            ## Navigation buttons — horizontal
            hbox:
                spacing 40
                xalign 0.5
                textbutton _("Chapters") action ShowMenu("chapter_select") text_style "mm_button_text"
                textbutton _("Recall") action ShowMenu("load") text_style "mm_button_text"
                textbutton _("Reflections") action ShowMenu("preferences") text_style "mm_button_text"
                textbutton _("About") action ShowMenu("about") text_style "mm_button_text"
                textbutton _("Departure") action Quit(confirm=not main_menu) text_style "mm_button_text"

    ## Version number — bottom right
    text "v[config.version]":
        style "main_menu_version"

    ## Mini music player
    use music_player

## ── Main Menu Styles ────────────────────────────────────────────────────────

style main_menu_title:
    size 80
    color "#FFFFFF"
    kerning 15.0
    text_align 0.5

style mm_button_text:
    size 22
    color "#CCCCCC"
    hover_color "#D4A574"
    selected_color "#D4A574"
    kerning 5.0
    outlines [(1, "#00000088", 0, 0)]

style main_menu_version:
    color "#FFFFFF33"
    size 18
    xalign 0.98
    yalign 0.98


################################################################################
## Navigation — Compatibility stub (tabs embedded in game_menu)
################################################################################

screen navigation():
    ## Navigation is now rendered inline as tabs within game_menu.
    ## This screen is retained as a no-op for compatibility.
    pass

################################################################################
## Game Menu — Centred base frame for all sub-menus
################################################################################

screen game_menu(title, scroll=None, yinitial=0.0, video_bg=None):

    ## Cache the Movie object so it isn't re-created on every re-render
    ## (re-creating it causes a one-frame black flash while the decoder starts)
    default gm_cached_movie = Movie(play=video_bg, loop=True) if video_bg else None

    ## Dark base
    add Solid("#0A0A0A")

    ## Video background
    if gm_cached_movie:
        add gm_cached_movie

    ## Dark overlay for readability over video
    add Solid("#00000088")

    ## ── Header: Title + gold divider ────────────────────────────────────
    vbox:
        xalign 0.5
        ypos 30

        text "[title!t]":
            xalign 0.5
            style "gm_title"

        null height 6

        frame:
            xalign 0.5
            xsize 100
            ysize 2
            background Solid("#D4A574")

    ## ── Navigation Tabs ─────────────────────────────────────────────────
    hbox:
        xalign 0.5
        ypos 100
        spacing 35

        if not main_menu:
            textbutton _("Save"):
                action ShowMenu("save")
                style "gm_tab_button"
            textbutton _("Load"):
                action ShowMenu("load")
                style "gm_tab_button"
            textbutton _("History"):
                action ShowMenu("history")
                style "gm_tab_button"
        else:
            textbutton _("Load"):
                action ShowMenu("load")
                style "gm_tab_button"

        textbutton _("Preferences"):
            action ShowMenu("preferences")
            style "gm_tab_button"
        textbutton _("About"):
            action ShowMenu("about")
            style "gm_tab_button"

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            textbutton _("Help"):
                action ShowMenu("help")
                style "gm_tab_button"

        if _in_replay:
            textbutton _("End Replay"):
                action EndReplay(confirm=True)
                style "gm_tab_button"

    ## ── Content Area ────────────────────────────────────────────────────
    frame:
        xalign 0.5
        xsize 1300
        ypos 140
        ysize (config.screen_height - 140 - 65)
        background Solid("#0A0A0A55")
        padding (40, 25, 40, 25)

        if scroll == "viewport":
            side "c r":
                xfill True
                yfill True
                spacing 15

                viewport id "gm_vp":
                    yinitial yinitial
                    mousewheel True
                    draggable True
                    pagekeys True

                    vbox:
                        xfill True
                        transclude

                vbar:
                    value YScrollValue("gm_vp")
                    xsize 18
                    base_bar Solid("#333333")
                    thumb Solid("#D4A574")
                    hover_thumb Solid("#E8C8A0")
                    unscrollable "hide"

        elif scroll == "vpgrid":
            side "c r":
                xfill True
                yfill True
                spacing 15

                vpgrid id "gm_vpg":
                    cols 1
                    yinitial yinitial
                    mousewheel True
                    draggable True
                    pagekeys True

                    transclude

                vbar:
                    value YScrollValue("gm_vpg")
                    xsize 18
                    base_bar Solid("#333333")
                    thumb Solid("#D4A574")
                    hover_thumb Solid("#E8C8A0")
                    unscrollable "hide"

        else:
            transclude

    ## ── Footer ──────────────────────────────────────────────────────────
    hbox:
        xalign 0.5
        yalign 1.0
        yoffset -25
        spacing 40

        textbutton _("Return"):
            action Return()
            style "gm_return_button"

        if not main_menu and not _in_replay:
            textbutton _("Main Menu"):
                action MainMenu()
                style "gm_return_button"

        if renpy.variant("pc") and not main_menu:
            textbutton _("Quit"):
                action Quit(confirm=True)
                style "gm_return_button"

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

## ── Game Menu Styles ────────────────────────────────────────────────────────

style gm_title:
    size 48
    color "#D4A574"
    kerning 8.0
    outlines [(1, "#00000088", 0, 0)]
    text_align 0.5

style gm_tab_button is button:
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

style gm_tab_button_text:
    size 20
    color "#999999"
    hover_color "#D4A574"
    selected_color "#D4A574"
    kerning 3.0
    outlines [(1, "#00000088", 0, 0)]

style gm_return_button is button:
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

style gm_return_button_text:
    size 20
    color "#888888"
    hover_color "#D4A574"
    kerning 3.0
    outlines [(1, "#00000088", 0, 0)]

## Content frame is now inline on the frame above (no named style needed)

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

            ## Page name (editable)
            button:
                style "page_label"
                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## Save-slot grid
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing gui.slot_spacing

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

            ## Page navigation
            vbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5
                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5

## ── Save / Load Styles ──────────────────────────────────────────────────────

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
    color "#D4A574"
    hover_color "#E8C8A0"

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")
    color "#999999"
    hover_color "#D4A574"
    selected_color "#D4A574"

style slot_button:
    properties gui.button_properties("slot_button")
    xsize gui.slot_button_width
    ysize gui.slot_button_height
    background Solid("#1A141088")
    hover_background Solid("#D4A57422")

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    size gui.slot_button_text_size
    xalign gui.slot_button_text_xalign
    text_align gui.slot_button_text_xalign
    color "#AAAAAA"
    hover_color "#D4A574"

style slot_time_text:
    size 16
    color "#999999"

style slot_name_text:
    size 16
    color "#CCCCCC"

################################################################################
## Preferences Screen
################################################################################

screen preferences():
    tag menu
    default pref_video = _pick_video(preferences_videos)
    use game_menu(_("Preferences"), scroll="viewport", video_bg=pref_video):

        vbox:
            spacing 20

            hbox:
                box_wrap True
                spacing 40

                ## Language selector
                vbox:
                    style_prefix "radio"
                    label _("Language")
                    textbutton "English" action Language(None)
                    textbutton "한국어" action Language("korean")
                    textbutton "Svenska" action Language("swedish")

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
                    textbutton _("After Choices") action Preference("after choices", "skip")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                vbox:
                    style_prefix "check"
                    label _("Content")
                    textbutton _("Show Warnings") action ToggleVariable("show_content_warnings", True, False)

            null height 10

            ## Gold divider between option groups and sliders
            frame:
                xalign 0.5
                xsize 800
                ysize 1
                background Solid("#D4A57444")

            null height 10

            hbox:
                style_prefix "slider"
                box_wrap True
                spacing 40

                vbox:
                    label _("Text Speed")
                    bar value Preference("text speed")

                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")

                vbox:
                    if config.has_music:
                        label _("Music Volume")
                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:
                        label _("Sound Volume")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

default show_content_warnings = True

## ── Preferences Styles ──────────────────────────────────────────────────────

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0
    color "#D4A574"
    size gui.label_text_size

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_foreground.png"
    selected_foreground "gui/button/radio_selected_foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    color "#CCCCCC"
    hover_color "#D4A574"
    selected_color "#D4A574"

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_foreground.png"
    selected_foreground "gui/button/check_selected_foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")
    color "#CCCCCC"
    hover_color "#D4A574"
    selected_color "#D4A574"

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")
    color "#CCCCCC"
    hover_color "#D4A574"

style slider_vbox:
    xsize 675

################################################################################
## History Screen — Dialogue Log
################################################################################

screen history():
    tag menu
    predict False
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

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }

## ── History Styles ──────────────────────────────────────────────────────────

style history_window is empty
style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text
style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign
    color "#D4A574"

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
    color "#CCCCCC"

style history_label:
    xfill True

style history_label_text:
    xalign 0.5
    color "#888888"

## About screen is now in gallery_screens.rpy (tabbed: Overview/Characters/World/Narrative)

################################################################################
## Help Screen
################################################################################

screen help():
    tag menu
    default device = "keyboard"
    default help_video = _pick_video(about_videos)
    use game_menu(_("Help"), scroll="viewport", video_bg=help_video):

        style_prefix "help"

        vbox:
            spacing 23

            ## ── Support & Helplines ─────────────────────────────────────
            vbox:
                spacing 10

                text _("{b}Support & Helplines{/b}"):
                    color "#D4A574"
                    size gui.label_text_size

                text _("This game explores themes of mental health, depression, anxiety, and suicide. If you or someone you know is affected, please reach out to one of these services."):
                    color "#CCCCCC"
                    size 22

                null height 5

                hbox:
                    spacing 10
                    text "{b}Samaritans{/b}" color "#D4A574" size 24
                    text "— 116 123  (UK, 24/7, free)" color "#CCCCCC" size 24

                hbox:
                    spacing 10
                    text "{b}Mind{/b}" color "#D4A574" size 24
                    text "— 0300 123 3393  (info line)" color "#CCCCCC" size 24

                hbox:
                    spacing 10
                    text "{b}Crisis Text Line{/b}" color "#D4A574" size 24
                    text "— Text SHOUT to 85258" color "#CCCCCC" size 24

                hbox:
                    spacing 10
                    text "{b}Papyrus{/b}" color "#D4A574" size 24
                    text "— 0800 068 4141  (under 35s)" color "#CCCCCC" size 24

                text _("{a=https://www.iasp.info/resources/Crisis_Centres/}International Association for Suicide Prevention — Crisis Centres{/a}"):
                    color "#A8C0D4"
                    size 22

            ## Gold divider
            null height 5
            frame:
                xalign 0.5
                xsize 800
                ysize 1
                background Solid("#D4A57444")
            null height 5

            ## ── Controls ────────────────────────────────────────────────
            text _("{b}Controls{/b}"):
                color "#D4A574"
                size gui.label_text_size

            hbox:
                spacing 20
                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help

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
    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")

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

screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")
    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")
    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")
    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")
    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")
    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()

## ── Help Styles ─────────────────────────────────────────────────────────────

style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12
    background None

style help_button_text:
    properties gui.button_text_properties("help_button")
    color "#CCCCCC"
    hover_color "#D4A574"
    selected_color "#D4A574"

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0
    color "#D4A574"

style help_text:
    color "#CCCCCC"

################################################################################
## Confirm Screen — Yes/No Prompts
################################################################################

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"

    add Solid("#00000099")

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

## ── Confirm Styles ──────────────────────────────────────────────────────────

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_button
style confirm_button_text is gui_button_text

style confirm_frame:
    background Solid("#1A1410EE")
    padding (50, 50, 50, 50)
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"
    color "#E8DCC8"
    size 28
    outlines [(1, "#00000088", 0, 0)]

style confirm_button:
    background None

style confirm_button_text:
    size 24
    color "#CCCCCC"
    hover_color "#D4A574"
    kerning 3.0
    outlines [(1, "#00000088", 0, 0)]

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
        background Solid("#2A201A")
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
        background Solid("#111111")
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
        textbutton "{size=18}{color=#AAAAAA88}[[J] Journal{/color}{/size}":
            xalign 0.98
            yalign 0.02
            action ShowMenu("journal")
