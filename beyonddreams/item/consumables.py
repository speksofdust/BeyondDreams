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
    _edibility =    0
    _perishable =   0   # 0=False or max time as 3 ints (min, hours, days)
    _ingredient =   0   # 0=False, 1=Dry, 2=Wet, 3=DrySolid, 4=WetSolid
    _crafting =     0   # can be used in making non consumables
    itemeffects =   None

    @property
    def edibility(self):
        """Ease of eating or drinking this item. 0 is impossible, 9 is easies."""
        return self._edibility

    def is_edible(self):
        return self.edible != 0

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
        elif self._ingredient == 3:
            yield "ingredient"
            yield "dry"
            yield "solid"
        elif self._ingredient == 4:
            yield "ingredient"
            yield "wet"
            yield "solid"
        else: pass
        if self._medicine: yield "medicine"
        if self._herb: yield "herb"




class Ingredient:
    """Consumable types that can always be used as an ingredient."""
    class Ingredient(ConsumableType):
        pass

    class Dry(Ingredient):
        _ingredient = 1

    class Edible(Ingredient):
        edible = 1
        _edibility = 1 # minimum

    class Wet(Ingredient):
        _ingredient = 2
        edible = 2
        _edibility = 8 # minimum

    class SolidDry(Dry):
        _ingredient=3

    class SolidWet(Wet):
        _ingredient=4
        _edibility = 7 # default

    class SolidDryEdible(SolidDry):
        _edible = 1
        _edibility = 1


# ---- Wet Ingredient -------------------------------------------------------- #
class Balm(Ingredient.SolidWet):
    _typename = "balm"

class Cream(Ingredient.SolidWet):
    _typename = "cream"

class Paste(Ingredient.SolidWet):
    _typename = "paste"

class Ointment(Ingredient.SolidWet)
    _typename = "ointment"


class Gel(Ingredient.SolidWet):
    _typename = "gel"
    edible =    1

class Oil(Ingredient.Wet):
    _typename = "oil"

class Jelly(Ingredient.SolidWet):
    _typename = "jelly"

class Sap(Ingredient.SolidWet):
    _typename = "sap"
    _edibility = 6

class Potion(Ingredient.Wet):
    _typename = "potion"

class Elixer(Ingredient.Wet):
    _typename = "elixer"

class Perfume(Ingredient.Wet):
    _typename = "perfume"
    _resale_shoptypes = (INGREDIENT_SHOP, PERFUME_SHOP)

class Dye(Ingredient.Wet):
    _typename = "dye"
    def __init__(self, color):
        self._color = color



# ---- Dry Ingredient -------------------------------------------------------- #
class Dust(Ingredient.Dry):
    _typename = "dust"


class Powder(Ingredient.Dry):
    _typname =  "powder"


class Pill(Ingredient.SolidDryEdible):
    _typename = "pill"


class Seed(Ingredient.SolidDryEdible):
    _typename = "seed"
    _edibility = 7
    _resale_shoptypes = (GARDENING_SHOP, SEED_SHOP)


class Flower(Ingredient.SolidDryEdible):
    _edibility = 9
    _typename = "flower"


class Bark(Ingredient.SolidDryEdible):
    _ediblility = 2
    _typename = "bark"


class Root(Ingredient.SolidDryEdible):
    _edibility = 2
    _typename = "root"


class Leaf(Ingredient.SolidDryEdible):
    _edibility = 8
    _typename = "leaf"


class Mushroom(Ingredient.SolidDryEdible):
    _edibility = 9
    _typename = "mushroom"


class Fruit(Ingredient.SolidDryEdible):
    _edibility = 9
    _typename = "fruit"


# ---- Ingredient/Crafting---------------------------------------------------- #
class Feather(Ingredient.SolidDry):
    _typename = "feather"
    _crafting = 1

class Shell(Ingredient.SolidDry):
    _typename = "shell"
    _crafting = 1

class Tooth(Ingredient.SolidDry):
    _typename = "tooth"
    _crafting = 1

class Bone(Ingredient.SolidDry):
    _typename = "bone"
    _crafting = 1

class Rock(Ingredient.SolidDry):
    _typename = "rock"


class Gem(Ingredient.SolidDry):
    _typename = "gem"
    _crafting = 1

class Crystal(Ingredient.SolidDry):
    _typename = "crystal"
    _crafting = 1


# ---- Crafting ----------------------------------------------------------- #
class Ingot(ConsumableType):
    _typename = "ingot"
    _crafting = 1

class Cloth(ConsumableType):
    _typename = "cloth"
    _crafting = 1

class String(ConsumableType):
    _typename = "string"
    _crafting = 1


class Button(ConsumableType):
    _typename = "button"
    _crafting = 1

class Ribbon(ConsumableType):
    _typename = "ribbon"
    _crafting = 1
