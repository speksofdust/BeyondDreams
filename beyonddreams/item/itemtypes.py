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


from .baseclasses import BDTaggedType

class ItemType(BDTaggedType):
    """Base class for all item types."""
    CATTYPE =       ""    # Primary catagory type (CONSUMABLE, WEAPON, etc.)
    _typename =     ""    # name for this item type -- not for primary types
    _typedesc =      ""
    BUNDLESIZE =    1
    ATTRIBS =       ()    # attribs for items when in inventory
    ALL_TYPE_ATTRIBS = () # all possible attribs for this type
    SLOTSIZE =      1     # base num slots taken in inventory
    _bwt =          1.0   # base weight must be (float)


    @property
    def typename(self):
        """The name of this item type."""
        if self._typename: return self._typename
        return self.__class__.__name__.lower() # only for primary types

    def _get_typetags(self):
        yield i for i in self._sc_tags()
        yield self.typename
        yield self.CATTYPE

    def typetags(self):
        """Yield all type tags for this."""
        return iter(self._get_typetags())

    def tags(self):
        for i in self._tags: yield i
        for i in self.typetags(): yield i



