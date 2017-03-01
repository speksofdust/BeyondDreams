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

    # --- Usage Flags --- #
    _use_as_ing =   False  # can be used as an ingredient
    _use_eat =      0       # 0-False, 1-Eat, 2-Drink
    #_use_perfume =  False   # can be sprayed on

    # --- Other Flags --- #
    _is_poison =    False # causes poison status if eaten, drunk
    _formtype =     0 # 0-dry, 1-liquid, 2-gelly (sap, jelly, slime, etc)
    #_perishable =   0   # 0=False or max time as 3 ints (min, hours, days)

    #@property
    #def edibility(self):
    #    """Ease of eating or drinking this item. 0 is impossible, 9 is easiest."""
    #    return self._edibility

    # ---- Usage flags ---- #
    def can_eat(self): return self._use_eat == 1
    def can_drink(self): return self._use_eat == 2
    def is_ingredient(self): return self._use_as_ing

    def _edible_tagname(self):
        return ("", "eat", "drink")[self._use_eat]


# ---- (Form) Mixins --------------------------------------------------------- #
class _Gelly:
    # Not quite liquid, not quite solid slime, gel, jelly, sap
    _formtype = 2
    _use_eat = 1

    def can_drink(self): return False


class _Liquid:
    _formtype = 1
    _use_eat = 2
    _use_perfume = True # liquids only

    def can_eat(self): return False
    def _edible_tagname(self): return "drink"


class _Dry:
    _formtype = 0
    _use_eat = 1

    def can_drink(self): return False


class _InEdible:
    # -- All classes to inherit from this MUST also be inedible when using this
    # -- for gelly or dry only
    _use_eat = 0

    def can_eat(self): return False
    def can_drink(self): return False
    def _edible_tagname(self): return ""


# ---------------------------------------------------------------------------- #
#    Raw Ingredient                                                            #
# ---------------------------------------------------------------------------- #
class rawingredient(ConsumableType):
    # -- non-craftable
    # -- must be found/bought
    #       (flowers, seeds, etc.)
    _ringredient = True
    _use_as_ing = True

    def is_ingredient(self): return True
    def is_rawingredient(self): return True
    def is_craftable(self): return False

    class Gelly(rawingredient, _Gelly): pass
    class Liquid(rawingredient, _Liquid): pass
    class Dry(rawingredient, _Dry): pass


# ---- Gelly ----------------------- #
class Gel(rawingredient.Gelly):
    _typename = "gel"


class Jelly(rawingredient.Gelly):
    _typename = "jelly"


class Sap(rawingredient.Gelly):
    _typename = "sap"
    _edibility = 6

# ---- Liquid ---------------------- #
class Oil(rawingredient.Liquid):
    _typename = "oil"
    _ingredient = True


# ---- Dry ------------------------- #
class Dust(rawingredient.Dry):
    _typename = "dust"


class Powder(rawingredient.Dry):
    _typname =  "powder"


# ---------------------------------------------------------------------------- #
#    drop Sourced (Ingredient)                                                 #
# ---------------------------------------------------------------------------- #
class dropsourced(rawingredient):
    # -- non-craftable
    # -- dropped by monsters, wildlife, etc
    #       (feather, shell, tooth, etc.)
    _sourcedfrom = "drops"
    _edible = 0

    class Gelly(plantsourced, _Gelly): pass
    class Liquid(plantsourced, _Liquid): pass
    class Dry(plantsourced, _Dry, _InEdible): pass # always inedible


# ---- Gelly ---------------------- #
# Not used

# ---- Liquid --------------------- #
class Blood(dropsourced.Liquid):
    _typename = "blood"


# ---- Dry ------------------------ #
class Feather(dropsourced.Dry):
    _typename = "feather"


class Shell(dropsourced.Dry):
    _typename = "shell"


class Tooth(dropsourced.Dry):
    _typename = "tooth"


class Bone(dropsourced.Dry):
    _typename = "bone"


class Hide(dropsourced.Dry):
    _typename = "hide"


class Scale(dropsourced.Dry):
    _typename = "scale"


class Spike(dropsourced.Dry):
    _typename = "spike"


class Claw(dropsourced.Dry):
    _typename = "claw"


class Dung(dropsourced.Dry):
    _typename = "dung"


class Horn(dropsourced.Dry):
    _typename = "horn"


# ---------------------------------------------------------------------------- #
#    inorganic Sourced (Ingredient)                                            #
# ---------------------------------------------------------------------------- #
class inorganicsourced(rawingredient):
    # -- non-craftable
    # -- must be found/bought
    #       (rocks, gems, crystals, etc.)
    _sourcedfrom = "inorgainc"
    _edible = 0

    def typetags(self):
        """Yield all type tags for this."""
        for i in self._get_typetags(): yield i

    class Gelly(inorganicsourced, _Gelly): pass
    class Liquid(inorganicsourced, _Liquid): pass
    class Dry(inorganicsourced, _Dry, _InEdible): pass # always inedible


# ---- Gelly ----------------------- #
# not currently used


# ---- Liquid ---------------------- #
# not currently used


# ---- Dry ------------------------- #
class Rock(inorganicsourced.Dry):
    _typename = "rock"


class Gem(inorganicsourced.Dry):
    _typename = "gem"
    _crafting = 1


class Crystal(inorganicsourced.Dry):
    _typename = "crystal"
    _crafting = 1


# ---------------------------------------------------------------------------- #
#    Plant Sourced (Ingredient)                                                #
# ---------------------------------------------------------------------------- #
class plantsourced(rawingredient):
    # -- non-craftable
    # -- must be found/bought
    #       (flowers, seeds, etc.)
    _sourcedfrom = "plant"

    class Gelly(plantsourced, _Gelly): pass
    class Liquid(plantsourced, _Liquid): pass
    class Dry(plantsourced, _Dry): pass

# ---- Gelly ----------------------- #
# not currently used


# ---- Liquid ---------------------- #
# not currently used


# ---- Dry ------------------------- #
class Seed(plantsourced.dry):
    _typename = "seed"
    _resale_shoptypes = (GARDENING_SHOP, SEED_SHOP)


class Flower(plantsourced.dry):
    _edibility = 9
    _typename = "flower"


class Bark(plantsourced.dry):
    _ediblility = 2
    _typename = "bark"


class Root(plantsourced.dry):
    _edibility = 2
    _typename = "root"


class Leaf(plantsourced.dry):
    _edibility = 8
    _typename = "leaf"


class Mushroom(plantsourced.dry):
    _edibility = 9
    _typename = "mushroom"


class Fruit(plantsourced.dry):
    _typename = "fruit"
    _edibility = 9


# ---------------------------------------------------------------------------- #
#    Craftables                                                                #
# ---------------------------------------------------------------------------- #
class craftable(ConsumableType):
    # -- craftable
    #       (perfume, ointment, potions, etc)

    def is_rawingredient(self): return False
    def is_craftable(self): return True

    def typetags(self):
        """Yield all type tags for this."""
        for i in self._get_typetags(): yield i
        yield "craftable"
        try:
            if self._is_med: yield "medicine"
        except: AttributeError

    class Gelly(craftable, _Gelly): pass
    class Liquid(craftable, _Liquid): pass
    class Dry(craftable, _Dry): pass


# ---- Gelly ----------------------- #
class Balm(craftable.Liquid):
    _typename = "balm"
    _is_med =   True


class Cream(craftable.Liquid):
    _typename = "cream"
    _is_med =   True


class Ointment(craftable.Liquid):
    _typename = "ointment"
    _is_med =   True


class Paste(craftable.Liquid):
    _typename = "paste"


# ---- Liquid ---------------------- #
class Potion(craftable.Liquid):
    _typename = "potion"
    _is_med =   True


class Elixer(craftable.Liquid):
    _typename = "elixer"
    _is_med = True


class Perfume(craftable.Liquid):
    _typename = "perfume"
    _resale_shoptypes = (INGREDIENT_SHOP, PERFUME_SHOP)


class Dye(craftable.Liquid):
    _typename = "dye"


# ---- Dry ------------------------- #
class Pill(craftable.Dry):
    _typename = "pill"
    _is_med =   True


class Ingot(craftable.Dry):
    _typename = "ingot"
    _use_as_ing = False

class Cloth(craftable.Dry):
    _typename = "cloth"
    _use_as_ing = False

class String(craftable.Dry):
    _typename = "string"
    _use_as_ing = False

class Button(craftable.Dry):
    _typename = "button"
    _use_as_ing = False

class Ribbon(craftable.Dry):
    _typename = "ribbon"
    _use_as_ing = False

