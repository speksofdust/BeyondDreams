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

import pdict

from .. import bd


class CharAttrib:
    __slots__ = ("_parent",)
    """Base class for all character attributes."""

    @property
    def char(self):
        """The char this attribute belongs to."""
        try: return self._parent.char
        except: return self._parent # parent is char

    @property
    def base(self):
        """Defaults for the char which this attribute belongs to."""
        return self._parent.base


class CharAttrDict(ChildPDict, CharAttrib):
    """CharAttrib dict type for use with Char attributes and sub attributes."""
    __slots__ = ChildPDict.__slots__



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
