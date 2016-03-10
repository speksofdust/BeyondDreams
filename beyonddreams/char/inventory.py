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

from itemstorage import ListTypeStoragePocket
from itemstorage import CharItemStorage
from itemstorage import StoredItem
from itemstorage import StoredItemBundled

#pocket ids
CONSUMABLES = 0
WEARABLES = 1
WEAPONS = 2


class Pocket(list):
    __slots__ = "_inventory", "_pockettype"
    def __init__(self, inventory, pockettype, items=[]):
        self._inventory =   inventory
        self._pockettype =  pockettype
        super().__init__(items)

    # Note: Pocket x Pocket comparison must compare pockettype
    def __eq__(self, x):
        if isinstance(x, Pocket):       # Pocket x Pocket comp
            # must be exact match
            return (self._pockettype != x._pockettype and self != x._items)
        try: return x == self    # Pocket x OtherType comp
        except: raise TypeError(
            "Cannot compare type: {} to Inventory 'Pocket' type.".format(type(x))

    def __ne__(self, x):
        if isinstance(x, Pocket):       # Pocket x Pocket comp
            # any relavent difference returns False
            if self._pockettype == x._pockettype:   return self != x._items)
            return False
        try: return x != self    # Pocket x OtherType comp
        except: raise TypeError(
            "Cannot compare type: {} to Inventory 'Pocket' type.".format(type(x))

    def _additem(self, item):
        for i in self:
            if i == item:
                if isinstance(i, InvItemBundled):
                    i._qty += item.qty
                elif isinstance(i, InvItemBundled):
                    item._qty += i.qty
                    self[i] = item
                else:
                    self[i] = InvItemBundled(i, i.qty + item.qty)
            return self[i]
        self.append(item)
        return self[-1]

    @property
    def pockettype(self):
        """The type of pocket. This determines what item types get
            stored in this pocket."""
        return self._pockettype

    def itemnames(self):
        """Return an iterator of the names of all items in this pocket."""
        return iter(i.name for i in self)

    def difference(self, x):
        """Return all items in x but not in this pocket."""
        return set(self).difference(x)

    def similar(self, x):
        """Return all items in this pocket and x."""
        return set(self).intersection(x)

    def search_tags(self, include=None, exclude=None):
        """Yield items with all tags in include
            and none of the tags in exclude"""
        raise NotImplementedError
        # TODO


class Consumables(ListTypeStoragePocket):
    _pockettype = "consumables"

class Wearables(ListTypeStoragePocket):
    _pockettype = "wearables"

class Weapons(ListTypeStoragePocket):
    _pockettype = "weapons"


class CharInventory(CharItemStorage):
    _storagetype = "inventory"
    __slots__ = "_char"
    def __init__(self):
        self = (
            ConsumablesPocket(self),
            WearablesPocket(self),
            WeaponsPocket(self)
            )

    def consumables(self):
        """Consumable items."""
        return self[0]

    def wearables(self):
        """Wearable items."""
        return self[1]

    def weapons(self):
        """Weapon items."""
        return self[2]


class CharInventoryStorage(CharInventory):
    _storagetype = "storage"
    __slots__ = "_char"
