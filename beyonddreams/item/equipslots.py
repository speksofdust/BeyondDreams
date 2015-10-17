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

from eqslotdata import EQUIPSLOTS

NULL = 0

class EquipError(Exception): pass


def glued(suffix=""):
    return "".join(("The currently equipped item cannot be removed.\n",
        suffix))


class _EquipSlot:
    __slots__ = "_name", "_item", "_glued"
    def __init__(self, name):
        self._name = name
        self._item = NULL
        self._glued() = False

    def __str__(self):
        return "{}:{},{}".format(self._name, self._item, int(self._glued()))

    def is_glued(self):
        """True if the item cannot normally be removed from this slot."""
        return self._glued()

    def weight(self):
        """The weight of all items in this slot."""
        try: return self._item.weight
        except: return 0

    def equip(self, item, glued=False):
        if self._glued(): return 1
        self._item = item


class EquipSlot(_EquipSlot):
    """Single layer equip slot."""
    _layers = 0
    __slots__ = _EquipSlot.__slots__

    # Make compatable with EquipSlotML when accessing item or object #
    def _get_layer(self, layer=None): return self
    def _get_item(self, layer=None): return self._item
    def _set_item(self, i, layer=None): self._item = i
    # -------------------------------------------------------------- #

    def item_count(self):
        """Total number of items equipped in this slot."""
        return int(self._item != NULL)

    def is_empty(self):
        """True if no items are equiped in this slot (on any layer)."""
        return self._item == NULL


class SlotLayer(_EquipSlot):
    __slots__ = _EquipSlot.__slots__
    # the name attr is an int indicating the layer starting with 0
    def __str__(self):
        return "({}:{},{})".format(self._name, self._item, int(self._glued()))


class EquipSlotML(tuple):
    """Multi-layer equip slot."""
    def __init__(self, name):
        self._name = name
        super().__init__(
            tuple(SlotLayer(i) for i in range(EQUIPSLOTS[name]._layers]))

    def __str__(self):
        return "{}:{}".format(self._name, ", ".join(self))

    def _get_layer(self, layer):
        if layer == 'default': return self[0]
        return self[layer]

    def _get_item(self, layer): return self._get_layer(layer)
    def _set_item(self, i, layer): self._get_layer(layer)._item = i

    def item_count(self):
        """Total number of items equipped in this slot."""
        return sum(1 for i in self if i._item != NULL)

    def is_empty(self):
        """True if no items are equiped in this slot (on any layer."""
        return all(i == NULL for i in self)

    def weight(self):
        """The weight of all items in this slot."""
        return sum(i.weight for i in self)

    def unequip_all(self):
        """Unequip all layers in this slot."""
        for i in self: i._item = NULL

    def free_layers(self):
        """Return an iterator of all free layers."""
        return iter(i for i in self if i._item == NULL)

    def layer_is_free(self, i):
        """True if layer i is free."""
        return self[x]._item == NULL

    def _get_next_free(self, i):
        """Return the next free layer after i."""
        for j in self[i:]:
            if j._item == NULL: return i
        return NONE


class Equip(dict):
    def __init__(self):

    def equip(self, item, slot="default", layer='default'):
        """Equip item in slot on layer."""
        self._equip(item, self._getslot(slot), layer)

    def _equip(self, i, s, layer):
        try: # check if item is glued
            if self[s]._get_layer(layer).is_glued()
                return glued("This item cannot be removed!")
        except:
            if s not in self:
                if EQUIPSLOTS[s].layers == 0: self[s] = EquipSlot(s)
                else: self[s] = EquipSlotML(s)
            self[s]._set_item(i, layer)

    def _get_slot(self, item, slot):
        if slot == (0 or 'default'): return self[item.equipslots[1])
        try: return self[item.equipslots[slot]]
        except: EquipError("invalid slot {}, {}".format(item.name, slot)


