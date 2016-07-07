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
from .bdobj import StorableObj
from .bdobj import BDObjSet


def regitem(i):
    """Register an item with 'itemtypes'."""
    from .bdtypes import itemtypes
    itemtypes._items[i._name] = iv


def _iter_by_attrval(ob, attr, val):
    return iter(i for i in ob if i.attr == val)

def _iterbycattype(ob, cattype):
    return iter(i for i in t if ob.CATTYPE == cattype)


class ItemDict():
    CATTYPE = ""
    __slots__ = "_items", "_sets"
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


class ItemType(StorableObj):
    """Base class for all item types."""
    _bundleable =   False
    _classifiers =  ()
    ATTRIBS =       ()    # attribs for items when in inventory
    ALL_TYPE_ATTRIBS = () # all possible attribs for this type

    def typetags(self):
        """Yield all type tags for this."""
        yield self._cattype
        for i in self._classifiers: yield i
        if (self._typename and typename not in self._classifiers):
            yield self._typename

    def tags(self):
        for i in self._tags: yield i
        for i in self.typetags(): yield i

    def is_bundable(self):
        """True if this item can be bundled."""
        return (self._bundleable and self._max_bundlesize > 1)


class BundableItemType(ItemType):
    """Item type with support for bundling."""
    _bundlable = True
    ABS_MAX_BUNDLE =    99
    _max_bundlesize =   1   # max num items grouped per bundle


class ItemSet(BDObjSet):
    """Data Storage class for sets of items"""
