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

from .bd import session
from beyonddreams.core.baseclasses import BDDataDict
from .vident import VIDENT_TYPES


# To be replaced by chardata.py
class CharData(BDDataDict):
    __slots__ = "_char", "_base", "_name_is_editable"
    def __init__(self, char, base=""):
        self._char =    char
        self._base =    base
        self._party =   party
        self._name_is_editable = False
        self._location = None
        self._data_id = None        # access data[self._data_id][some_data]
        super().__init__({
            "name-first":           "",
            "name-last":            "",
            "name-middle":          "",
            "name-nick":            "",

            "location": {
                'region':   0,
                }

            "body":     {
                }

            # inventory
            "inventory-consumables":    [],
            "inventory-weapons":        [],
            "inventory-wearables":      [],
            "inventory-keyitems":       [],

            # equip
            "equip":    {
                },

            "handedness":               0,  # 0-left, 1-right, 2-ambidextrous

            # wallet
            "wallet-coupons":           [],
            "wallet-cash":              {},

            # stats stuff
            "stats":        {
                "phys-energy":      100,
                "mental-energy":    100,
                "health":           100,
                }

            "statuses": {
                # physical types
                "frozen":           False
                "frostbite" :       0,
                "burn" :            0,
                "numb" :            0,
                "stun" :            0,
                "poisoning" :       0,
                "bleed" :           0,

                # mental types
                "blind" :           0,
                "drunk" :           0,
                "dumb" :            0,
                "confusion" :       0,

                # transform types
                "zombie" :          0,
                "mutagen" :         0,
                }

            })
        if self._char.is_npc:
            from .game.location import NPCCharLocData
            self._location = NPCCharLocData
        else:
            from .game.location import CharLocData
            self._location = CharLocData

    @property
    def handedness(self):
        return self['handedness']

    @property
    def name(self):
        return Charname(self)

    @property
    def statuses(self):
        return Statuses(self)

    @property
    def location(self):
        return self._location





class Char:
    """Base class for character objects."""
    _ident = VIDENT_TYPES["char"]
    _is_npc = False
    _type = ""
    __slots__ = "_chardata", "_controller", "_owner"
    def __init__(self, player, base):
        self._owner =       owner
        self._player =      owner
        self._chardata =    CharData(self, base)

    @property
    def owner(self):
        """The player who owns this character."""
        return self._owner

    @property
    def player(self):
        """The player currently controlling this character."""
        return self._player

    def owner_is_player(self):
        """True if the owner of this character is also the one controlling it."""
        return self._owner == self._player

    def is_local_player(self):
        """True if this char is controlled by the "player" object
            on the local machine."""
        return self._player == session.screen.player


    # ---- Chardata access ---- #
    @property
    def location(self):
        return self._chardata["location"]

    @property
    def name(self):
        return self._chardata["name"]

    @property
    def base(self):
        """Base values for this character."""
        return self._chardata.base

    @property
    def body(self):
        """This characters body attributes."""
        return self._chardata["body"]

    @property
    def wallet(self):
        """This characters wallet."""
        return self._chardata["wallet"]

    @property
    def inventory(self):
        """This characters inventory."""
        return self._chardata["inventory"]

    @property
    def equip(self):
        """This characters equipment."""
        return self._chardata["equip"]

    @property
    def party(self):
        """The party this char is in."""
        return self._chardata["party"]

    # ---- Query ---- #
    def famtypes(self):
        """Return an iterator of family types for this character."""
        return ()

    def is_alive(self):
        """True if this character is alive."""
        if self._chardata["stats"]["HP"] == 0: return False
        return True

    def is_critical(self):
        """True if this characters health level is in the critical range."""
        return self._chardata["stats"]["HP"].is_critical()

    def is_undead(self):
        """True if this character is an undead type or has zombie status."""
        return ("zombie" in self._items["statuses"]["bools"] or
            "zombie" in self.famtypes)

    def hp(self):
        return self._chardata["stats"]["HP"]


