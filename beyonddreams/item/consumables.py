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

from itemtypes import ItemType
from itemtypes import regitem


class ConsumableType(ItemType):
    """Base class for all consumable item types."""
    _sc =           (WeaponType,)
    CATTYPE =       "consumable"
    edible =        0   # 0-False 1-True 2-Drinkable ('can' be eaten/drunk)
    _perishable =   0   # 0=False or time as 3 ints (min, hours, days)
    _ingredient =   0   # 0=False, 1=Dry, 2=Wet

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

