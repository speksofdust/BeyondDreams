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
from .shop.shopnames import *


class ConsumableTypeDict(ItemDict):
    CATTYPE = "consumable"
    __slots__ = ItemDict.__slots__


class ConsumableType(BundableItemType):
    """Base class for all consumable item types."""
    CATTYPE =       "consumable"
    edible =        0   # 0-False 1-True 2-Drinkable ('can' be eaten/drunk)
    _perishable =   0   # 0=False or max time as 3 ints (min, hours, days)
    _ingredient =   0   # 0=False, 1=Dry, 2=Wet
    itemeffects =   None

    def _edible_tagname(self):
        return ("", "edible", "drinkable")[self.edible]

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
        elif self._ingredient == 2:
            yield "ingredient"
            yield "wet"
            yield "liquid"
        else: pass


class Ingredient(ConsumableType):
    """Consumable types that can always be used as an ingredient."""

class DryIngredient(Ingredient):
    _resale_shoptypes = (INGREDIENTS_SHOP, )

class EdibleIngredient(DryIngredient):
    edible =    1

class HerbalIngredient(EdibleIngredient):
    _resale_shoptypes = (INGREDIENTS_SHOP, HERB_SHOP)

class WetIngredient(Ingredient):
    edible =    2


# ---- Dry Ingredient -------------------------------------------------------- #
class Dust(DryIngredient):
    _typename = "dust"


class Powder(DryIngredient):
    _typname =  "powder"


class Seed(EdibleIngredient):
    _typename = "seed"
    _resale_shoptypes = (GARDENING_SHOP, SEED_SHOP)


class Flower(EdibleIngredient):
    _typename = "flower"


class Bark(EdibleIngredient):
    _typename = "bark"


class Root(EdibleIngredient):
    _typename = "root"


class Leaf(EdibleIngredient):
    _typename = "leaf"


class Mushroom(EdibleIngredient):
    _typename = "mushroom"


class Fruit(EdibleIngredient):
    _typename = "fruit"


# ---- Herbals --------------------------------------------------------------- #
class HerbalFlower(HerbalIngredient, Flower): pass
class HerbalLeaf(HerbalIngredient, Leaf): pass
class HerbalBark(HerbalIngredient, Bark): pass
class HerbalRoot(HerbalIngredient, Root): pass

# ---- Wet Ingredient -------------------------------------------------------- #
class Gel(WetIngredient):
    _typename = "gel"
    edible =    1

class Oil(WetIngredient):
    _typename = "oil"


class Potion(WetIngredient):
    _typename = "potion"
    _resale_shoptypes = (POTION_SHOP,)


class Perfume(WetIngredient):
    _typename = "perfume"
    _resale_shoptypes = (INGREDIENT_SHOP, PERFUME_SHOP)

class Sap(WetIngredient):
    _typename = "sap"


# ---- Consumable ------------------------------------------------------------ #
class Feather(ConsumableType):
    _typename = "feather"


class Shell(ConsumableType):
    _typename = "shell"


class Tooth(ConsumableType):
    _typename = "tooth"


class Bone(ConsumableType):
    _typename = "bone"


class String(ConsumableType):
    _typename = "string"


class Button(ConsumableType):
    _typename = "button"


class Ribbon(ConsumableType):
    _typename = "ribbon"


class Rock(ConsumableType):
    _typename = "rock"


class Gem(ConsumableType):
    _typename = "gem"


class Ingot(ConsumableType):
    _typename = "ingot"


class Cloth(ConsumableType):
    _typename = "cloth"



