# ---------------------------------------------------------------------------- #
#                                                                              #
#     This program is free software: you can redistribute it and/or modify     #
#     it under the terms of the GNU General Public License as published by     #
#     the Free Software Foundation, either version 3 of the License, or        #
#     (at your option) any later version.                                      #
#                                                                              #
#     This program is distributed in the hope that it will be useful,          #
#     but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the             #
#     GNU General Public License for more details.                             #
#                                                                              #
#     You should have received a copy of the GNU General Public License        #
#     along with this program. If not, see <http://www.gnu.org/licenses/>.     #
#                                                                              #
# ---------------------------------------------------------------------------- #

DEFAULT_USER_CONFIG = {
    "chareditor-undohist":      64,
    #"chareditor-undo-maxmem":   "auto",


    "sidepanel-defaultorder-game":     (0,1,2),
    "session-confirm-logout":           1,  # 0-False, 1-True, 2-InMainMenuOnly

    # game stuff


    # menu stuff


    # volume
    "volume-master":                    100,
    "volume-speech":                    80,
    "volume-game-music",                90,
    "volume-game-sfx":                  80,
    "volume-menu-sfx":                  60,
    "volume-menu-music":                90,

    "censors-allow-toggle":             False,
    "censors-mode":                     0,
    "censors-size":                     1.0,
    }



DEFAULT_KEY_SET = {
    # Movement
    "strafe-left":              "Q",
    "strafe-right":             "E",
    "move-fowrard":             "W",
    "move-back":                "S",
    "turn-left":                "A",
    "turn-right":               "D",
    "action-primary":           "",     # open doors, talk, pickup/interact, etc.
    "action-secondary":         "",     #
    "jump":                     "SPACE",
    "attack-primary":           "",     # attack with primary weapon/fists
    "attack-secondary":         "",     # attack with secondary weapon
    "throw":                    "",     # throw selected item
    "drop":                     "",     # drop selected item
    "kick":                     "",
    "block":                    "",     # block with arms or shield (when holding)

    # item
    "item-prev":                "",
    "item-next":                "",
    "item-prev-favs":           "",
    "item-next-favs":           "",
    #"item-quick-1":             "",
    #"item-quick-2":             "",
    #"item-quick-3":             "",

    # camera
    "camera-rotate-left":       "NUM_4",
    "camera-rotate-right":      "NUM_6",
    "camera-zoom-in":           "NUM_PLUS",
    "camera-zoom-out":          "NUM_MINUS",
    "camera-center":            "NUM_5",
    "camera-tilt-up":           "NUM_8",
    "camera-tilt-down":         "NUM_2",
    "target":                   "",     # target an object

    # sidepanel
    "sidepanel-toggle":         "F2",     # Show/Hide the sidepanel
    "sidepanel-page-next":      "F3",
    "sidepanel-page-prev":      "F4",
    # sidepanel -- go to or open given page
    "sidepanel-page-inventory": "F5",
    "sidepanel-page-config":    "F6",
    "sidepanel-page-stats":     "F7",

    # misc
    "help":                     "F1",
    "fullscreen-toggle":        "F11",
    "pause":                    "PAUSE",
    "quit":                     ("ALT", "Q"),

    # censors -- only used if 'censors-allow-toggle' is enabled in user settings
    "censor-toggle":            ("ALT", "F2"),
    "censor-toggle-full":       ("SHIFT", "ALT", "F2"),
    "censor-mode-next":         "",
    "censor-type-next":         "",
    "censor-type-prev":         "",
    }
