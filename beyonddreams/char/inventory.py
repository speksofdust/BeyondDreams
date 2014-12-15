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

from attrib import CharAttrib

CONSUMABLES = 0
WEARABLES = 1
WEAPONS = 2

class Pocket:
    __slots__ = "_inventory", "_items", "_pockettype"
    def __init__(self, inventory, pockettype, items=[]):
        self._inventory =   inventory
        self._pockettype =  pockettype
        self._items =       list(items)
        
    def __eq__(self, x):
        try: return x == self._items
        except: raise Exception(
            "Cannot compare type: {} to Inventory 'Pocket' type.".format(type(x))
        
    def __ne__(self, x):
        try: return x != self._items
        except: raise Exception(
            "Cannot compare type: {} to Inventory 'Pocket' type.".format(type(x))
        
    def __len__(self):          return len(self._items)
    def __contains__(self, x):  return x in self._items
    def __iter__(self, x):      return iter(self._items)
    def __repr__(self):         return str(self._items)
        
    def difference(self, x):
        """Return all items in x but not in this pocket."""
        return set(self._items).difference(x)
    
    def similar(self, x):
        """Return all items in this pocket and x."""
        return set(self._items).intersection(x)
        
    def search_tags(self, include=None, exclude=None):
        """Yield items with all tags in include 
            and none of the tags in exclude"""
        raise NotImplementedError
        # TODO
        
        
class Inventory(CharAttrib):
    __slots__ = "_char", "_pockets"
    def __init__(self, char):
        self._char = char
        self._pockets = (
            Pocket(self, CONSUMABLES),
            Pocket(self, WEARABLES),
            Pocket(self, WEAPONS),
            )
    
    def __str__(self):  return tuple(repr(i) for i in self._pockets)
    __repr__ = __str__    
    
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
        return sum(len(i) for i in iter(self._pockets)):
            
