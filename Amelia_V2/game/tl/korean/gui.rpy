## Korean Font Override
##
## Noto Sans CJK KR provides full Korean (Hangul) character support.
## Style overrides activate when the player switches to Korean language.
## Using "translate <lang> style" blocks — the correct Ren'Py mechanism
## for per-language font changes (gui.* variables are read at init time
## so translate python: can't retroactively change styles built from them).

translate korean python:

    gui.text_font = "fonts/NotoSansCJKkr-Regular.otf"
    gui.name_text_font = "fonts/NotoSansCJKkr-Bold.otf"
    gui.interface_text_font = "fonts/NotoSansCJKkr-Regular.otf"
    gui.button_text_font = "fonts/NotoSansCJKkr-Regular.otf"
    gui.choice_button_text_font = "fonts/NotoSansCJKkr-Regular.otf"

## Core text styles
translate korean style default:
    font "fonts/NotoSansCJKkr-Regular.otf"

translate korean style input:
    font "fonts/NotoSansCJKkr-Regular.otf"

translate korean style say_dialogue:
    font "fonts/NotoSansCJKkr-Regular.otf"

translate korean style say_thought:
    font "fonts/NotoSansCJKkr-Regular.otf"

translate korean style say_label:
    font "fonts/NotoSansCJKkr-Bold.otf"

## UI / interface styles
translate korean style button_text:
    font "fonts/NotoSansCJKkr-Regular.otf"

translate korean style navigation_button_text:
    font "fonts/NotoSansCJKkr-Regular.otf"

translate korean style label_text:
    font "fonts/NotoSansCJKkr-Bold.otf"

translate korean style choice_button_text:
    font "fonts/NotoSansCJKkr-Regular.otf"

translate korean style slot_name_text:
    font "fonts/NotoSansCJKkr-Regular.otf"

translate korean style slot_time_text:
    font "fonts/NotoSansCJKkr-Regular.otf"

translate korean style page_label_text:
    font "fonts/NotoSansCJKkr-Bold.otf"

translate korean style notify_text:
    font "fonts/NotoSansCJKkr-Regular.otf"

translate korean style pref_label_text:
    font "fonts/NotoSansCJKkr-Bold.otf"

translate korean style radio_button_text:
    font "fonts/NotoSansCJKkr-Regular.otf"

translate korean style check_button_text:
    font "fonts/NotoSansCJKkr-Regular.otf"

translate korean style confirm_prompt_text:
    font "fonts/NotoSansCJKkr-Regular.otf"

translate korean style game_menu_label_text:
    font "fonts/NotoSansCJKkr-Bold.otf"

translate korean style return_button_text:
    font "fonts/NotoSansCJKkr-Regular.otf"

translate korean style main_menu_text:
    font "fonts/NotoSansCJKkr-Regular.otf"
