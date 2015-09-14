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

from item import BundableItemType
from item import regitem
from item import ItemDict


class ConsumableTypeDict(ItemDict):
    CATTYPE = "consumable"
    __slots__ = ItemDict.__slots__


class ConsumableType(BundableItemType):
    """Base class for all consumable item types."""
    _sc =           (BundableItemType,)
    CATTYPE =       "consumable"
    edible =        0   # 0-False 1-True 2-Drinkable ('can' be eaten/drunk)
    _perishable =   0   # 0=False or max time as 3 ints (min, hours, days)
    _ingredient =   0   # 0=False, 1=Dry, 2=Wet
    itemeffects =   None

    def _edible_tagname(self):
        return ("", "edible", "drinkable")self.edible

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

class _DIng(DryIngredient):
    _sc =       (DryIngredient,)

class _EDing(_DIng):
    edible =    1

class WetIngredient(Ingredient):
    _sc =       (Ingredient,)
    edible =    2

class _WIng(WetIngredient):
    _sc =       (WetIngredient)


# ---- Dry Ingredient -------------------------------------------------------- #
class Dust(_DIng):
    _typename = "dust"


class Powder(_DIng):
    _typname =  "powder"


class Seed(_EDing):
    _typename = "seed"


class Flower(_EDIng):
    _typename = "flower"


class Bark(_EDIng):
    _typename = "bark"


class Root(_EDIng):
    _typename = "root"


class Leaf(_EDIng):
    _typename = "leaf"


class Mushroom(_EDIng):
    _typename = "mushroom"


class Fruit(_EDIng):
    _typename = "fruit"


# ---- Wet Ingredient -------------------------------------------------------- #
class Gel(_WIng):
    _typename = "gel"
    edible =    1


class Oil(_WIng):
    _typename = "oil"


class Potion(_WIng):
    _typename = "potion"


class Perfume(_WIng):
    _typename = "perfume"


# ---- Consumable ------------------------------------------------------------ #
class Feather(ConsumableType):
    _sc =       (ConsumableType,)
    _typename = "feather"


class Shell(ConsumableType):
    _sc =       (ConsumableType,)
    _typename = "shell"


class Tooth(ConsumableType):
    _sc =       (ConsumableType,)
    _typename = "tooth"


class Bone(ConsumableType):
    _sc =       (ConsumableType,)
    _typename = "bone"


class String(ConsumableType):
    _sc =       (ConsumableType,)
    _typename = "string"


class Button(ConsumableType):
    _sc =       (ConsumableType,)
    _typename = "button"


class Ribbon(ConsumableType):
    _sc =       (ConsumableType,)
    _typename = "ribbon"


class Rock(ConsumableType):
    _sc =       (ConsumableType,)
    _typename = "rock"


class Gem(ConsumableType):
    _sc =       (ConsumableType,)
    _typename = "gem"


class Ingot(ConsumableType):
    _sc =       (ConsumableType,)
    _typename = "ingot"


class Cloth(ConsumableType):
    _sc =       (ConsumableType,)
    _typename = "cloth"



