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

from item import ItemType
from item import regitem
from item import ItemDict


class ConsumableTypeDict(ItemDict):
    CATTYPE = "consumable"
    __slots__ = ItemDict.__slots__


class ConsumableType(ItemType):
    """Base class for all consumable item types."""
    _sc =           (ItemType,)
    CATTYPE =       "consumable"
    edible =        0   # 0-False 1-True 2-Drinkable ('can' be eaten/drunk)
    _perishable =   0   # 0=False or max time as 3 ints (min, hours, days)
    _ingredient =   0   # 0=False, 1=Dry, 2=Wet
    itemeffects =   None

    def is_ingredient(self):
        """True if this item can be used as an ingredient."""
        return bool(self._ingredient)

    def is_perishable(self):
        """True if this item is perishable."""
        return self._perishable != 0

    def typetags(self):
        """Yield all type tags for this."""
        for i in self._get_typetags(): yield i
        if self._perishable: yield "perishable"
        if self._ingredient == 1:
            yield "ingredient"
            yield "dry"
        elif: self._ingredient == 2:
            yield "ingredient"
            yield "wet"
            yield "liquid"
        else: pass


class Ingredient(ConsumableType):
    """Consumable types that can always be used as an ingredient."""
    _sc =       (ConsumableType,)


class DryIngredient(Ingredient):
    _sc =       (Ingredient,)


class WetIngredient(Ingredient):
    _sc =       (Ingredient,)
    edible =    2


class Dust(DryIngredient):
    _sc =       (DryIngredient,)


class Powder(Dust):
    pass


class Potion(WetIngredient):
    _sc =       (WetIngredient,)


class Shell(ConsumableType):
    _sc =       (ConsumableType,)


class Tooth(ConsumableType):
    _sc =       (ConsumableType,)


class String(ConsumableType):
    _sc =       (ConsumableType,)


class Gel(WetIngredient):
    _sc =       (WetIngredient,)


class Oil(WetIngredient):
    _sc =       (WetIngredient,)


class Flower(ConsumableType):
    _sc =       (ConsumableType,)


class Perfume(ConsumableType):
    _sc =       (ConsumableType,)


class Bark(ConsumableType):
    _sc =       (ConsumableType,)


class Root(ConsumableType):
    _sc =       (ConsumableType,)


class Leaf(ConsumableType):
    _sc =       (ConsumableType,)


class Rock(ConsumableType):
    _sc =       (ConsumableType,)


class Gem(ConsumableType):
    _sc =       (ConsumableType,)


class Mushroom(ConsumableType):
    _sc =       (ConsumableType,)
