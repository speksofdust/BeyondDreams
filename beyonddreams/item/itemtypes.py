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
from .bdtypedef import BDTypeDict


def regitem(i):
    """Register an item with 'itemtypes'."""
    from .bdtypes import itemtypes
    itemtypes._items[i._name] = iv


def _iter_by_attrval(ob, attr, val):
    return iter(i for i in ob if i.attr = val)

def _iterbycattype(ob, cattype):
    return iter(i for i in t if ob.CATTYPE == cattype)

class ItemDict(BDTypeDict):

    def __init__(self):
        self._items = {}

    def consumables(self):
        return _iterbycattype(self, "consumable")

    def wearables(self):
        return _iterbycattype(self, "wearable")

    def weapons(self):
        return self._iterbycattype(self, "weapons")
      
      
# some absolute maximums
MAX_BUNDLE =    99
MAX_SLOTSIZE =  100

__slots__ = "MAX_BUNDLE", "MAX_SLOTSIZE"
    
class ItemType:
    """Base class for all item types."""
    CATTYPE =       ""    # Primary catagory type (CONSUMABLE, WEAPON, etc.)
    _inc_ttags =    ()    # typetags to be inherited
    _typetags =     ()    # tags to describe this item type
    _typename =     ""    # name for this item type
    typedesc =      ""
    BUNDLESIZE =    1
    ATTRIBS =       ()    # attribs for items when in inventory
    ALL_TYPE_ATTRIBS = () # all possible attribs for this type
    SLOTSIZE =      1     # base num slots taken in inventory
    _desc =         ""
    _bwt =          1.0   # base weight must be (float)

    @property
    def name(self):
        """The name of this item."""
        return self._name

    def typename(self):
        """The name of this item type."""
        if not self._typename: return self.__class__.__name__.lower()
        return self._typename

    def typetags(self):
        """Yield all type tags for this."""
        for i in self._inc_ttags: yield i
        for i in self._typetags: yield i
        yield self.TYPENAME
        yield self.CATTYPE
