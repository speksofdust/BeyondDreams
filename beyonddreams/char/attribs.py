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

from .. import bd


class CharAttrib:
    __slots__ = ("_char",)
    """Base class for all character attributes."""
    def __init__(self, char):
        self._char = char

    @property
    def char(self):
        """The char this attribute belongs to."""
        return self._char._char

    @property
    def base(self):
        """Defaults for the char which this attribute belongs to."""
        return self._char._base


class CharAttribDict(CharAttrib):
    __slots__ = CharAttrib.__slots__ + "_items"
    def __init__(self, char):
        self._char = char
        self = {}

    def __getitem__(self, i):       return self._items[i]
    def __len__(self):              return len(self._items)
    def __contains__(self, i):      return i in self._items
    def __iter__(self):             return iter(self._items)
    def __str__(self):              return str(self._items)[0:-1]
    def __repr__(self):             return repr(self._items)

    def _getiter(self, n):          return iter(self._items[i] for i in n)


class StatAttrib(CharAttribDict):
    __slots__ = CharAttribDict.__slots__

    def __setitem__(self, i, v):    self._items[i].value = v

class CharAttribSubAttrib:
    """Subattribute class for use within a CharAttrib class."""
    __slots__ = ()
    def __init__(self, charattrib):
        self._charattrib = charattrib

    @property
    def charattrib(self):
        """The charattrib this is part of."""
        return self._charattrib

    @property
    def char(self):
        """The character which this belongs to."""
        return self._charattrib._char


class Equip(CharAttrib):
    __slots__ = CharAttrib.__slots__ + "_slots"
    def __init__(self, char, slots):
        self._char = char
        self._slots = {}

    def __bool__(self):         return len(self._slots) > 0
    def __len__(self):          return len(self._slots)
    def __iter__(self):         return iter(self._slots)
    def __contains__(self, i):  return i in self._slots
    def __getitem__(self, i):   return self._slots[i]


class Body(CharAttrib):
    __slots__ = CharAttrib.__slots__ + "_subparts", "_attribs", "_mesh"
    def __init__(self, char):
        self._char = char
        self._subparts = {}
        self._attribs = {}
        self._mesh = None
        #bd.datapath()  TODO

    @property
    def subparts(self):
        return self._subparts

    @property
    def attribs(self):
        return self._attribs


class Stats(CharAttrib):
    __slots__ = CharAttrib.__slots__
    def __init__(self, char):
        self._char = char

    def base_stats(self):
        """The base stats."""
        return self._char._base._stats


class StatusEffects(CharAttrib):
    __slots__ = CharAttrib.__slots__
    def __init__(self, char):
        self._char = char

    def base_statuseffects(self):
        """The base status effects."""
        return self._char._base._statuseffects
