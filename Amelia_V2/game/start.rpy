###############################################################################
##
##  GAME START — Entry Point
##
##  Ren'Py requires a 'label start' as the game entry point.
##  This shows the content warning, then begins Chapter 1.
##
###############################################################################

label start:

    ## Show content warning if enabled
    ## if show_content_warnings:
    ##     call screen content_warning("This story explores themes of grief, identity, and mental health.", "Some scenes may be emotionally intense.")

    jump chapter_1
