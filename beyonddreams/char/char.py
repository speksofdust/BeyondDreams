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


class CharName(tuple):
    __slots__ = "_editable"
    def __init__(self, first="", middle="", last="", nick=""):
        self._editable = False
        self = (first, middle, last, nick) # first, middle, last, nick

    def _set_tuple(self, a, b, c, d):
        if self._editable: self = (a, b, c, d)

    def _get_first(self): return self[0]
    def _set_first(self, n): self._set_tuple(n, *self[1:3])
    first = property(_get_first, _set_first)

    def _get_middle(self): return self[1]
    def _set_middle(self, n): self._set_tuple(self[0], n, *self[-2:])
    middle = property(_get_middle, _set_middle)

    def _get_last(self): return self[2]
    def _set_last(self, n): self._set_tuple(self[0], self[1], n, self[-1])
    last = property(_get_last, _set_last)

    def _get_nick(self): return self[3]
    def _set_nick(self, n): self._set_tuple(self[0], self[1], self[2], n)
    nick = property(_get_nick, _set_nick)


class CharData(BDDataDict):
    __slots__ = "_char", "_base"
    def __init__(self, char, base=""):
        self._char =    char
        self._base =    base
        self = {
            "name":         CharName(),
            "party":        None
            "body":         None,
            "inventory":    None,
            "equip":        None,
            "wallet":       None,
            "stats":        Stats(self),
            "resistances":  None,
            }


class Char:
    """Base class for character objects."""
    _type = ""
    __slots__ = "_chardata"
    def __init__(self, base):
        self._chardata =    CharData(self, base)

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

    def is_local_player(self):
        """True if this char is controlled by the "player" object
            on the local machine."""
        return self._player == session.screen.player

    # ---- Query ---- #
    @property
    def party(self):
        """The party this char is in."""
        return self._chardata["party"]

    def famtypes(self):
        """Return an iterator of family types for this character."""
        return ()

    def is_alive(self):
        """True if this character is alive."""
        if self._items["stats"]["HP"] == 0: return False
        return True

    def is_critical(self):
        """True if this characters health level is in the critical range."""
        return self._chardata["stats"]["HP"].is_critical()

    def is_undead(self):
        """True if this character is an undead type or has zombie status."""
        return ("zombie" in self._items["statuses"]["bools"] or
            "zombie" in self.famtypes)

