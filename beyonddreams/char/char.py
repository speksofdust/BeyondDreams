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

class CFWrapper:
    """Character data access wrapper."""
    def __init__(self, char): self.char = char

    def __eq__(self, c): return self._char == (c or c._char)
    def __ne__(self, c): return self._char != (c or c._char)


class CharName(CFWrapper):

    def __str__(self): return str(self.__repr__[1:-1])
    def __repr__(self): return str((self.first, self.last, self.middle, self.nick))

    def _sn(self, n, v):
        if self.char._name_is_ediatble: self.char["".join('name-', v)] = n

    def _get_first(self): return self.char['name-first']
    def _set_first(self, n): self._sn(n, 'first')
    first = property(_get_first, _set_first)

    def _get_middle(self): return self.char['name-middle']
    def _set_middle(self, n): self._sn(n, 'middle')
    middle = property(_get_middle, _set_middle)

    def _get_last(self): return self.char['name-last']
    def _set_last(self, n): self._sn(n, 'last')
    last = property(_get_last, _set_last)

    def _get_nick(self): return self.char['name-nick']
    def _set_nick(self, n): self._sn(n, 'nick')
    nick = property(_get_nick, _set_nick)

    @property
    def full(self):
        """The first and last name."""
        return self.char[0], self.char[2]

    @property
    def middle_initial(self):
        """The first letter of the middle name."""
        return self.char[1][0]

    @property
    def initials(self):
        """The first letters of the first and last name."""
        return self.char[0][0], self.char[2][0]


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


class Stauses:

    def _gs(self, status):
        pass
        # self.char['statuses'][status]

    def _set_status(self, status):
        pass
        # self.char['statuses'][status]

    def _gs_bool(self, status):
        pass

    def _ss_bool(self, status):
        pass


    def _get_frozen(self):    return self._gs_bool(self, "frozen")
    def _set_frozen(self, x): self._ss_bool(self, "frozen")
    frozen = property(_get_frozen, _set_frozen)

    def _get_frostbite(char): return self._gs(self, "frostbite")
    def _set_frostbite(char, x): self._ss(self, "frostbite")
    frostbite = property(_get_frostbite, _set_frostbite)

    def _get_burn(char): return self._gs(self, "burn")
    def _set_burn(char, x): self._ss(self, "burn")
    burn = property(_get_burn, _set_burn)


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


