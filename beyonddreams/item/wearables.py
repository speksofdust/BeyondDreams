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
from item import ItemDict
#from item import regitem

class WearableTypeDict(ItemDict):
    CATTYPE = "wearable"
    __slots__ = ItemDict.__slots__


class WearableType(ItemType):
    """Base class for wearable item types."""
    CATTYPE =       "wearable"
    _classifiers =  ()
    _sc =           (ItemType, )
    equipslots =    _typename


class _Clothing(WearableType):
    _sc =           (WearableType, )
    _inctags =      "clothing"
    baseres =       BaseRes()
    basestats =     BaseStats()


class _Accessories(WearableType):
    _sc =           (WearableType,)
    _inctags =      "accessories"


class _Jewelry(Accessories):
    _sc =           (_Accessories,)
    _inctags =      "jewelry"


# Transitional *helper* classes -- subclasses inherit from these so we dont
#   have to enter _sc values on every subclass
class Clothing(_Clothing):
    _sc =           (Clothing, )

class Accessories(_Accessories):
    _sc =           (Accessories,)

class Jewelry(_Jewelry):
    _sc =           (Jewelry,)


# ---- Jewelry Base Types ---------------------------------------------------- #



# ---- Clothing Base Types --------------------------------------------------- #
class HeadWear(Clothing):
    _inctags =      "headwear"


class Footwear(Clothing):
    _surface_grip_mult =    1   # slick surface grip multiplier
    #_kick_dmg_mult =        1   # kick damage multiplier


class Tops(Clothing):
    _inctags =      "tops"


class Bottoms(Clothing):
    _inctags =    "bottoms"


class BodySuit(Clothing):
    _inctags =  "bodysuit"


# ---- Undies Base Types ---- #
class Undies(Clothing):
    _inctags =    "undies"
    _bwt =          0.2


class UndiesBottoms(Undies):
    _sc =           Undies, Bottoms


class UndiesTops(Undies):
    _sc =           Undies, Tops


# ---- Swimwear Base Types ---- #
class Swimwear(Clothing):
    _inctags =  "swimwear"
    _bwt =      0.2


class SwimTop(Tops):
    _sc = Swimwear, Tops


class SwimBottom(Bottoms):
    _sc = Swimwear, Bottoms


# ---- Armor Base Types ---- #
class Armor(Clothing):
    _inctags = "armor"


class ArmorTop(Tops):
    _sc =   Armor, Tops


class ArmorBottoms(Bottoms):
    _sc =   Armor, Bottoms


# ---- Clothing Sub Types ---------------------------------------------------- #
class Shoe(Footwear):
    _sc =       (Footwear, )
    _bwt =      0.5


class Boot(Footwear):
    _sc =       (Footwear, )
    _bwt =      0.7


class Glove(Clothing):
    # increases punch damage
    # may increase weapon grip
    _typename =         "glove"
    _weapon_grip =      0   # vs barehanded
    #_punch_dmg_mult =   1   # punch damage multplier


class Sock(Clothing):
    _typename =     "sock"


class Shirt(Tops):
    _typename =     "shirt"


class Bustier(Tops):
    _typename =     "bustier"


class Dress(Tops):
    _typename =     "dress"


class Skirt(Bottoms):
    _typename =     "skirt"


class Loincloth(Bottoms):
    _typename =     "loincloth"


class Pants(Bottoms):
    _typename =     "pants"


class CatSuit(BodySuit):
    _sc =       BodySuit


# ---- Swimwear -------------------------------------------------------------- #
class _Bikini:
    _inctags = "bikini"


class BikiniTop(SwimwearTop, _Bikini):
    _typename = "bikini top"


class BikiniBottom(SwimwearBottom, _Bikini):
    _typename = "bikini bottom"


class BikiniThong(SwimwearBottoms, _Bikini):
    _typename = "bikini thong"


# ---- Armor (min +1 def) ---------------------------------------------------- #
class Gauntlet(Armor, Glove):
    _typename = "gauntlet"
    _typedesc = """An armored glove."""


class Curiass(ArmorTop):
    _typename = "curiass"


class Breastplate(ArmorTop):
    _typename = "breastplate"


class Helm(Armor, Headwear):
    _typename = "helm"


# ---- Jewelry --------------------------------------------------------------- #
class Hairpin(Jewelry):
    _typename = "hairpin"


class Bangle(Jewelry):
    _typename = "bangle"
    equipslots = "ankle", "wrist"


class Bracelet(Jewelry):
    _typename = "bracelet"
    equipslots = "ankle", "wrist"


class Necklace(Jewelry):
    _typename = "necklace"
    _inctags =  "neckwear"


class Choker(Jewelry):
    _typename = "choker"
    _inctags =  "neckwear"
    _typedesc = """Tight fitting jewelry warn around the neck."""


class Ring(Jewelry):
    _typename = "ring"
    _typedesc = """A piece of jewelry to be worn on a finger or toe."""


# ---- Accessories ----------------------------------------------------------- #
class Glasses(Accessory):
    _typename = "glasses"


class Belt(Accessory):
    _typename = "belt"


class Collar(Accessory):
    _typename = "collar"
    _inctags =  "neckwear"

