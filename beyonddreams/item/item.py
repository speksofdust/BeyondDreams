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


class ItemType(BDTaggedType):
    """Base class for all item types."""
    _bundleable =   False
    CATTYPE =       ""    # Primary catagory type (CONSUMABLE, WEAPON, etc.)
    _classifiers =  ()
    _typename =     ""    # name for this item type -- not for primary types
    _typedesc =     ""
    ATTRIBS =       ()    # attribs for items when in inventory
    ALL_TYPE_ATTRIBS = () # all possible attribs for this type
    # ---- Minimum worth values ---------------------------------------------- #
    _min_resale_value = 1 # <-- must be <= all other 'worth' 'values'
    _min_pawn_value = 1   #
    _min_trade_value = 1  #
    # ---- Resale/trade attribs ---------------------------------------------- #
    _pawnable = True
    _tradable = True
    _resale_shoptypes = () # shoptypes that will buy this
    # ---- stuff for consumables, weapons, and wearables only ---------------- #
    _bwt =          1.0   # base weight must be (float)
    _slotsize =     1
    _itemset =      None

    def __init__(self, name, tags=(), item_sets=()):
        BDTaggedType.__init__(self, name=name, tags=tags)
        self._item_sets = item_sets

    @property
    def typename(self):
        """The name of this item type."""
        if self._typename: return self._typename
        return self.CATTYPE

    def typetags(self):
        """Yield all type tags for this."""
        yield self.CATTYPE
        for i in self._classifiers: yield i
        if (self._typename and typename not in self._classifiers):
            yield self._typename

    def is_pawnable(self):
        """True if this item can be sold to a pawn shop."""
        return self._pawnable

    def is_tradable(self):
        """True if this item can be traded to another player or npc."""
        return self._tradable

    def is_sellable(self, buyer=None):
        """True if this itemtype can be sold to the given buyer. If buyer is
        'None', then returns True if this itemtype is allowed to be sold."""
        if (buyer is None or buyer.is_player):
            return self.tradable()
        else:
            try:
                if buyer.storetype() == 'pawn': return self.is_pawnable()
                else: return buyer.storetype() in self._resale_shoptypes
            except:
                return False

    def tags(self):
        for i in self._tags: yield i
        for i in self.typetags(): yield i
        for i in self._subcattype_tags: yield i

    def is_bundable:
        """True if this item can be bundled."""
        if self._bundleable and self._max_bundlesize > 1)

    def is_in_set(self):
        """True if this item is part of a set."""
        return self._itemset is not None


class BundableItemType(ItemType):
    """Item type with support for bundling."""
    _bundleable = True
    ABS_MAX_BUNDLE =    99
    _max_bundlesize =   1   # max num items grouped per bundle


class ItemSet(BDTaggedType):
    """Data Storage class for sets of items"""
    def __init__(self, set_name, tags=()):
        BDTaggedType.__init__(self, name=set_name, tags=tags)
