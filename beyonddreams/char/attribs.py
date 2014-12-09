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
    def __init__(self, c):
        self._char = c

    @property
    def char(self):
        """The char this attribute belongs to."""
        return self._char


CONSUMABLES =   "consumables"
WEARABLES =     "wearables"
WEAPONS =       "weapons"
        
class Pocket:
    __slots__ = "_inventory", "_items", "_pockettype"
    def __init__(self, inventory, pockettype, items=[]):
        self._inventory =   inventory
        self._pockettype =  pockettype
        self._items =       list(items)
        
        
class Inventory(CharAttrib):
    __slots__ = "_char", "_pockets"
    def __init__(self, char):
        self._char = char
        self._pockets = (
            Pocket(self, CONSUMABLES),
            Pocket(self, WEARABLES),
            Pocket(self, WEAPONS),
            )
        
    def consumables(self):
        """Consumable items."""
        return self._pocket[0]
        
    def wearables(self):
        """Wearable items."""
        return self._pocket[1]
        
    def weapons(self):
        """Weapon items."""
        return self._pocket[2]
        
    def total_items(self):
        """Return the total number of items."""
        return (len(self._pockets[0]) + len(self._pockets[1]) +
            len(self._pockets[2]))
    

class Wallet(CharAttrib):
    __slots__ = ("_char",)
    def __init__(self, char):
        self._char = char


class Equip(CharAttrib):
    __slots__ = ("_char",)
    def __init__(self, char):
        self._char = char


class Body(CharAttrib):
    __slots__ = "_char", "_subparts", "_attribs", "_mesh"
    def __init__(self, char):
        self._char = char
        self._subparts = {}
        self._attribs = {}
        #bd.datapath()  TODO

    @property
    def subparts(self):
        return self._subparts

    @property
    def attribs(self):
        return self._attribs
