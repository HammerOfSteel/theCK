## The CK: Amelia V2 — Main Menu Music Player
##
## Shuffled playlist with a mini-player overlay (song name, artist,
## prev/next/pause controls).
##

################################################################################
## Playlist Engine
################################################################################

init python:

    import os

    class MenuPlaylist(object):
        """Shuffled music playlist for the main menu."""

        ## ── song catalogue ──────────────────────────────────────────────
        ## (filename-stem, display title)
        ## Add / remove entries as songs arrive.  Order here doesn't matter —
        ## the list is shuffled on every fresh visit to the main menu.
        SONGS = [
            ("audio/songs/amelia.ogg",               "Amelia"),
            ("audio/songs/bare_with_me.ogg",         "Bare with Me"),
            ("audio/songs/between_the_veil.ogg",     "Between the Veil"),
            ("audio/songs/circles_in_the_sand.ogg",  "Circles in the Sand"),
            ("audio/songs/daffodils_in_the_snow.ogg","Daffodils in the Snow"),
            ("audio/songs/familiar_strangers.ogg",   "Familiar Strangers"),
            ("audio/songs/forgetmeknot.ogg",         "Forgetmeknot"),
            ("audio/songs/hawthorne.ogg",            "Hawthorne"),
            ("audio/songs/here_now_and_blues.ogg",   "Here Now and Blues"),
            ("audio/songs/jolly_rum_ba_low.ogg",     "Jolly Rum Ba Low"),
            ("audio/songs/kindeling_kin.ogg",        "Kindeling Kin"),
            ("audio/songs/lighthouse_in_the_fog.ogg","Lighthouse in the Fog"),
            ("audio/songs/living_on_the_moon.ogg",   "Living on the Moon"),
            ("audio/songs/mindful_meddling.ogg",     "Mindful Meddling"),
            ("audio/songs/mirror_of_the_mind.ogg",   "Mirror of the Mind"),
            ("audio/songs/oh_sarah.ogg",             "Oh Sarah"),
            ("audio/songs/paper_planes.ogg",         "Paper Planes"),
            ("audio/songs/the_long_way_home.ogg",    "The Long Way Home"),
            ("audio/songs/the_mist_laden_path.ogg",  "The Mist Laden Path"),
            ("audio/songs/the_quiet_of_morning.ogg", "The Quiet of Morning"),
            ("audio/songs/the_work.ogg",             "The Work"),
            ("audio/songs/two_birds.ogg",            "Two Birds"),
        ]

        ARTIST = "Dancing Salamanders"
        ARTIST_URL = "https://dancingsalamanders.com"
        CHANNEL = "music"

        def __init__(self):
            self._order = []      # list of (path, title) in shuffled order
            self._index = 0
            self._paused = False
            self._active = False

        ## ── public API ──────────────────────────────────────────────────

        def start(self):
            """Shuffle and begin playing from track 0."""
            available = [(p, t) for p, t in self.SONGS if renpy.loadable(p)]
            if not available:
                return
            self._order = list(available)
            renpy.random.shuffle(self._order)
            self._index = 0
            self._paused = False
            self._active = True
            self._play_current()

        def ensure_playing(self):
            """Start only if not already active.  Safe to call on every
            menu show/replace without restarting the current song."""
            if self._active and renpy.music.get_playing(channel=self.CHANNEL):
                return
            self.start()

        def stop(self):
            """Stop playback entirely."""
            renpy.music.stop(channel=self.CHANNEL, fadeout=1.0)
            self._active = False

        def next_track(self):
            if not self._order:
                return
            self._index = (self._index + 1) % len(self._order)
            self._paused = False
            self._play_current()

        def prev_track(self):
            if not self._order:
                return
            self._index = (self._index - 1) % len(self._order)
            self._paused = False
            self._play_current()

        def toggle_pause(self):
            if self._paused:
                renpy.music.set_pause(False, channel=self.CHANNEL)
                self._paused = False
            else:
                renpy.music.set_pause(True, channel=self.CHANNEL)
                self._paused = True

        ## ── queries ─────────────────────────────────────────────────────

        @property
        def current_title(self):
            if self._order:
                return self._order[self._index][1]
            return ""

        @property
        def artist(self):
            return self.ARTIST

        @property
        def artist_url(self):
            return self.ARTIST_URL

        @property
        def is_paused(self):
            return self._paused

        @property
        def is_active(self):
            return self._active

        @property
        def track_info(self):
            """e.g.  '3 / 7'"""
            if self._order:
                return "{} / {}".format(self._index + 1, len(self._order))
            return ""

        ## ── internals ───────────────────────────────────────────────────

        def _play_current(self):
            path = self._order[self._index][0]
            # Queue the *next* track so playback is seamless
            next_idx = (self._index + 1) % len(self._order)
            next_path = self._order[next_idx][0]
            renpy.music.play(path, channel=self.CHANNEL, fadeout=1.0, fadein=1.0)
            renpy.music.queue(next_path, channel=self.CHANNEL, loop=False)

        def check_advance(self):
            """Call every interact.  If the current track finished and the
            queued track started, advance our index so the UI matches."""
            if not self._active or not self._order or self._paused:
                return
            playing = renpy.music.get_playing(channel=self.CHANNEL)
            if playing is None:
                # Nothing playing — restart
                self._play_current()
                return
            current_path = self._order[self._index][0]
            if playing != current_path:
                # The queued track started — advance index
                next_idx = (self._index + 1) % len(self._order)
                next_path = self._order[next_idx][0]
                if playing == next_path:
                    self._index = next_idx
                    # Queue the one after that
                    after_next = (self._index + 1) % len(self._order)
                    renpy.music.queue(
                        self._order[after_next][0],
                        channel=self.CHANNEL, loop=False
                    )

    ## Create the singleton
    menu_playlist = MenuPlaylist()


################################################################################
## Mini-Player Screen — shows in bottom-left of main menu
################################################################################

screen music_player():
    ## Call check_advance every interaction so the title stays in sync
    timer 2.0 action Function(menu_playlist.check_advance) repeat True

    if menu_playlist.is_active:
        frame:
            style "mp_frame"

            hbox:
                spacing 10
                yalign 0.5

                ## Transport controls
                hbox:
                    spacing 6
                    yalign 0.5

                    textbutton "<<":
                        style "mp_btn"
                        action Function(menu_playlist.prev_track)
                        tooltip "Previous track"

                    if menu_playlist.is_paused:
                        textbutton "{size=22}\u25B6{/size}":
                            style "mp_btn"
                            action Function(menu_playlist.toggle_pause)
                            tooltip "Play"
                    else:
                        textbutton "||":
                            style "mp_btn"
                            action Function(menu_playlist.toggle_pause)
                            tooltip "Pause"

                    textbutton ">>":
                        style "mp_btn"
                        action Function(menu_playlist.next_track)
                        tooltip "Next track"

                ## Song info
                vbox:
                    spacing 2
                    yalign 0.5

                    text "[menu_playlist.current_title]":
                        style "mp_title"

                    textbutton "{size=14}[menu_playlist.artist]{/size}":
                        style "mp_artist_btn"
                        action OpenURL(menu_playlist.artist_url)
                        tooltip "Visit dancingsalamanders.com"


## ── Mini-Player Styles ──────────────────────────────────────────────────────

style mp_frame:
    xalign 0.02
    yalign 0.96
    background Solid("#0A0A0ACC")
    padding (14, 8, 18, 8)

style mp_btn is gui_button:
    background None
    xsize None
    ysize None

style mp_btn_text:
    size 18
    color "#888888"
    hover_color "#D4A574"

style mp_title:
    size 16
    color "#D4A574"
    bold True

style mp_artist_btn is gui_button:
    background None
    xsize None
    ysize None

style mp_artist_btn_text:
    size 14
    color "#999999"
    hover_color "#E8C8A0"
    underline True
