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

# will replace char.py
import cacc
from wallet import Wallet
from famtypes import FamTypeAccessor

CHAR_ID_LEN = 30

_chardata = {
    # base data
    "base":     "",

    # name
    "name-first":   "",
    "name-last":    "",
    "name-middle":  "",
    "name-nick":    "",

    "location": {
        'region':   0,
        }

    "body":     {
        }

    # inventory & wallet
    "cash":         [0],
    "coupons":      [],
    "cards":        [],
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

        # transform
        "zombie" :      0,
        "mutagen" :     0,

        # specials
        "immunnull":    0,  # bool
        "immundown":    0,
        },


def _new_game_char():
    from game.data import gamedata
    from utils import rand_alphanum
    global CHAR_ID_LEN, _chardata_dict
    cid = rand_alphanum(CHAR_ID_LEN)
    while True:
        if cid in gamedata['chars']:
            cid = rand_alphanum(CHAR_ID_LEN)
        gamedata['chars'][cid] = _chardata_dict.copy()

def _del_game_char(charid)
    from game.data import gamedata
    try: del gamedata['chars'][charid]
    except: KeyError

class Chars(list):

    def alive(self):
        """Return an iterator of all alive characters."""
        return iter(i for i in self if i.isalive())

    def critical(self):
        """Return an iterator of all characters who's health is between 1 and
        10 percent."""
        return iter(i for i in self if i.critical())

    def undead(self):
        """Return an iterator of all characters of undead fam type or who have
        zombie status of 100."""
        return iter(i for i in self if i.is_undead())


class CharAccessor(GameDataAccessorDict):
    __slots__ = ("char", "data")
    def __init__(self, char):
        self.char = char

    def __dpath(self): return gamedata['chars'][self.char]

    @property
    def name(self):
        return cacc.CharNameAccessor(self)

    @property
    def inventory(self):
        return cacc.CharInventory(self)

    @property
    def statuses(self):
        return cacc.Statuses(self)

    @property
    def wallet(self):
        return Wallet(self)

    # ---- Query --------------------------------------------------------- #
    @property
    def famtypes(self):
        """Return an iterator of family types for this character starting with
        the primary type."""
        return FamTypeAccessor(self.char)

    @property
    def handedness(self):
        """The handedness of this character.
        0: left    1: right    2: ambidextrious"""
        return self['handedness']

    def is_alive(self):
        """True if this character's hp is 0."""
        return self.char['stats']['hp'] != 0

    def is_critical(self):
        """True if this character's hp is health is between 1 and 10 percent."""
        return 1 <= self.char['stats']['hp'] <= 10

    def is_undead(self):
        """True if this character has a fam type of 'undead' or has 'zombie'
        status."""
        return ('undead' in self.famtypes or self['statuses']['zombie'] == 100)

    # ---- Calculated stat/status getters -------------------------------- #
    def hp(self):
        """Health for this character."""
        return self['stats']['hp']

    def phys_energy(self):
        """The current physical energy for this character."""
        return

    def mental_energy(self):
        """The current mental energy for this character."""
        return
