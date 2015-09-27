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

#from itembrowser import ItemBrowserSearch
#from itembrowser import ItemBrowserSelection
#from itembrowser import ItemBrowserItem
#from itembrowser import ItemBrowser
#from itembrowser import ItemBrowserAutoHide
from .char.attribs import CharAttrib


class ItemStorage(Tuple):
    """Base class for certain item storage types."""

    def __str__(self):  return str(self._pockets)
    __repr__ = __str__


class ItemStorageChar(ItemStorage, CharAttrib):
    __slots__ = "_char", "_pockets"
    def __init__(self, char):
        self._char = char
        self = ()


# ---- Storage Pocket Stuff -------------------------------------------------- #
class ItemStoragePocket:
    _pockettype = ""
    def __init__(self, owner):
        self._owner = owner

    @property
    def pockettype(self):
        """The type of pocket. This determines what item types get
            stored in this pocket."""
        return self._name


class DictTypeStoragePocket(dict, StoragePocket):
    pass


class ListTypeStoragePocket(list, StoragePocket):
    pass


# ---- Stored Item ----------------------------------------------------------- #
class StoredItem:
    """Base class for stored items."""
    __slots__ = "_item"
    def __init__(self, item):
        self._item = item

    def __del__(self):
        self._item = None
        try: self._qty = None
        except: pass

    def __repr__(self): return str(self._item.name, self.qty)

    # Note: AttributeError will be raised if comparing an item that is not an
    #   instance of InventoryItem (doesnt have a qty attrib)
    #   to compare item only use the item property
    def __eq__(self, x): return (self._item == x._item and self.qty == x.qty)
    def __ne__(self, x): return (self._item != x._item or self.qty != x.qty)

    # lt, gt, ge, le compare qty -- both items must be the same
    def __lt__(self, x):
        if self._item == x._item: return self.qty < self.qty
        raise Exception("tried to compare mismatched items ({} != {})".format(
            self._item.name, x._item.name)

    def __gt__(self, x):
        if self._item == x._item: return self.qty > self.qty
        raise Exception("tried to compare mismatched items ({} != {})".format(
            self._item.name, x._item.name)

    def __ge__(self, x):
        if self._item == x._item: return self.qty >= self.qty
        raise Exception("tried to compare mismatched items ({} != {})".format(
            self._item.name, x._item.name)

    def __le__(self, x):
        if self._item == x._item: return self.qty <= self.qty
        raise Exception("tried to compare mismatched items ({} != {})".format(
            self._item.name, x._item.name)

    @property
    def qty(self):
        """The number of this item in the inventory, reguardless of whether
        it may be used now."""
        try:    return self._qty # bundled
        except: return 1

    @property
    def itemdata(self):
        """Access item data."""
        return self._item

    # ---- itemdata shortcuts -- (self._item.xxx) ---- #
    @property
    def name(self):
        """The name of this item."""
        return self._item.name

    def tags(self):
        return iter(self._item.tags()


class StoredItemBundled(StoredItem):
    """Class for multiples of the same item stored as a single item with a
    qty (quantity)
    """
    __slots__ = "_item", "_qty"
    def __init__(self, item, qty):
        self._item =    item
        self._qty =     int(qty)

    @property
    def qty(self):
        """The quantity of this item available."""
        return self._qty


