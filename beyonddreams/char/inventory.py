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

#pocket ids
CONSUMABLES = 0
WEARABLES = 1
WEAPONS = 2


class InventoryItem:
    """Base class for items stored in the inventory."""
    __slots__ = "_item"
    def __init__(self, item):
        self._item = item
        
    def __del__(self):
        self._item = None
        try: self._qty = None
        except: pass
        
        
    # Note: AttributeError will be raised if comparing an item that is not an
    #   instance of InventoryItem (doesnt have a qty attrib)
    #   to compare item only use the item property
    def __eq__(self, x): 
        return (self._item == x._item and self.qty == x.qty) 
    
    def __ne__(self, x):
        return (self._item != x._item or self.qty != x.qty) 
        
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
        
    def __repr__(self): return str(self._item.name, self.qty)

    @property
    def itemdata(self):
        """Access item data."""
        return self._item

    @property
    def qty(self):
        """The number of this item in the inventory, reguardless of whether
        it may be used now."""
        try:    return self._qty # bundled
        except: return 1

    # for convience
    @property
    def name(self):
        """The name of this item."""
        return self._item.name
        

class InvItem(InventoryItem):
    """"""
    __slots__ = "_item"


class InvItemBundled(InventoryItem):
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


class Pocket:
    __slots__ = "_inventory", "_items", "_pockettype"
    def __init__(self, inventory, pockettype, items=[]):
        self._inventory =   inventory
        self._pockettype =  pockettype
        self._items =       list(items)

    # Note: Pocket x Pocket comparison must compare pockettype
    def __eq__(self, x):
        if isinstance(x, Pocket):       # Pocket x Pocket comp
            # must be exact match
            return (self._pockettype != x._pockettype and self._items != x._items)
        try: return x == self._items    # Pocket x OtherType comp
        except: raise TypeError(
            "Cannot compare type: {} to Inventory 'Pocket' type.".format(type(x))
        
    def __ne__(self, x):
        if isinstance(x, Pocket):       # Pocket x Pocket comp
            # any relavent difference returns False
            if self._pockettype == x._pockettype:   return self._items != x._items)
            return False
        try: return x != self._items    # Pocket x OtherType comp
        except: raise TypeError(
            "Cannot compare type: {} to Inventory 'Pocket' type.".format(type(x))
        
    def __len__(self):          return len(self._items)
    def __contains__(self, x):  
        for i in self._items:
            if (x == i or x == i.name): return True
        return False
        
    def __iter__(self, x):      return iter(self._items)
    def __repr__(self):         return str(self._items)
        
    def _additem(self, item):
        for i in self._items:
            if i == item:
                if isinstance(i, InvItemBundled):
                    i._qty += item.qty
                elif isinstance(i, InvItemBundled):
                    item._qty += i.qty
                    self._items[i] = item
                else:
                    self._items[i] = InvItemBundled(i, i.qty + item.qty)
            return self._items[i]
        self._items.append(item)
        return self._items[-1]
        
        
    @property
    def pockettype(self):
        """The type of pocket. This determines what item types get 
            stored in this pocket."""
        return self._pockettype
        
    def itemnames(self):
        """Return an iterator of the names of all items in this pocket."""
        return iter(i.name for i in self._items))
        
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
    def __init__(self):
        self._char = None
        self._pockets = (
            Pocket(self, CONSUMABLES),
            Pocket(self, WEARABLES),
            Pocket(self, WEAPONS),
            )
    
    def __str__(self):  return tuple(repr(i) for i in self._pockets)
    __repr__ = __str__    
    
    def add_item(self, i):
        if isinstance(i, InventoryItem):
            self._pockets[i.itemdata.pockettype]._additem(i)
        raise TypeError("Invalid item type for inventory.")
    
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
        """Return the total number of items in the inventory."""
        return sum(len(i) for i in iter(self._pockets)):
            
