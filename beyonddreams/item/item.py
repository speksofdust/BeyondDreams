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

from .core.bdtype import BDTaggedType
from .core.bdtype import BDTypeDict


def regitem(i):
    """Register an item with 'itemtypes'."""
    from .bdtypes import itemtypes
    itemtypes._items[i._name] = iv


def _iter_by_attrval(ob, attr, val):
    return iter(i for i in ob if i.attr = val)

def _iterbycattype(ob, cattype):
    return iter(i for i in t if ob.CATTYPE == cattype)


class ItemDict(BDTypeDict):
    CATTYPE = ""
    __slots__ = BDTypeDict.__slots__ + "_sets"
    def __init__(self):
        self._items = {}
        self._sets = set()


class Items:
    def __init__(self):
        from consumables import ConsumableTypeDict
        from weapons import WeaponTypeDict
        from wearables import WearableTypeDict
        self.consumables =  ConsumableTypeDict()
        self.weapons =      WeaponTypeDict()
        self.wearables =    WearableTypeDict()


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
    _bundlesize =    1    # num items grouped per bundle
    _slotsize =      1    # base num slots used in inventory per bundlesize
    ATTRIBS =       ()    # attribs for items when in inventory
    ALL_TYPE_ATTRIBS = () # all possible attribs for this type
    _bwt =          1.0   # base weight must be (float)

    def __init__(self, name, tags=(), item_sets=()):
        BDTaggedType.__init__(self, name=name, tags=tags)
        self._item_sets = item_sets

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


class ItemSet(BDTaggedType):
    """Data Storage class for sets of items"""
    def __init__(self, set_name, tags=()):
        BDTaggedType.__init__(self, name=set_name, tags=tags)
