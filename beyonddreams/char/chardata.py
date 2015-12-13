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

from game.data import gamedata

# will replace char.py
CHAR_ID_LEN = 30

_chardata_dict = {
    "temp":         {}, # non-writable stuff
    # flags
    "temp-flags":   [], # non-writable
    "flags":        [],
    "KO-flags":     [], # cleared after revived|re-spawn
    # base data
    "base":     "",

    # name
    "name-first":   "",
    "name-last":    "",
    "name-middle":  "",
    "name-nick":    "",

    "location": {
        'region':   0,
        },

    "bodybase":     {
        "type":     0,
        },

    "body-current": {

        },

    # inventory & wallet
    "cash":         [0],
    "coupons":      [],
    "cards":        [],
    "bag":          "default",
    "consumables":  [],
    "weapons":      [],
    "wearables":    [],
    "keyitems":     [],

    # equip
    "handedness":   0,  # 0-left, 1-right, 2-ambidextrous
    "equip":    {
        },

    # stats stuff
    "phys-energy":      100,
    "mental-energy":    100,
    "health":           100,

    "statuses": {
        # physical
        "frozen":       0,   # bool
        "frostbite" :   0,
        "burn" :        0,
        "numb" :        0,
        "stun" :        0,
        "poisoning" :   0,
        "bleed" :       0,

        # mental
        "blind" :       0,
        "drunk" :       0,
        "dumb" :        0,
        "confusion" :   0,
        #"hallucination": 0,

        # transform
        "zombie" :      0,
        "mutagen" :     0,

        # specials
        "immunull":     0,  # bool
        "immundown":    0,
        },
}

# ---- Char creation and deletion -------------------------------------------- #
def _new_game_char(playable):
    cid = _set_chardata_dict(None)
    if playable:
        gamedata['chars'][cid]['game-stats'] = {}
    return gamedata['chars'][cid]

def _del_game_char(charid)
    try: del gamedata['chars'][charid]
    except: KeyError

def _clear_temps():
    for i in gamedata['chars']:
        try: del gamedata['chars'][i]['temp']
        except: KeyError

def _update_chars():
    for i in gamedata['chars']: update_char(gamedata['chars'][i])

def _set_chardata_dict(data=None):
    from xsquare.utils.strutils import rand_alphanumeric
    global _chardata_dict, CHAR_ID_LEN
    cid = rand_alphanumeric(CHARID_LEN)
    while True: # generate a unique cid (char id)
        if cid in gamedata['chars']: cid = rand_alphanumeric(CHAR_ID_LEN)
        else: break
    if data == None:    gamedata['chars'][cid] = _chardata_dict.copy()
    else:               gamedata['chars'][cid] = data
    return cid
