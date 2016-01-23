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
from eqslotdata import *    # classifiers, EQUIPSLOTS


class WearableTypeDict(ItemDict):
    CATTYPE = "wearable"
    __slots__ = ItemDict.__slots__


class WearableType(ItemType):
    """Base class for wearable item types."""
    CATTYPE =       "wearable"
    _equipslots =   'default'
    _forcelayer =   False   # top, bottom or False
    _removes =      ()      # items to be remove when equipped

    def _equipslots(self):
        """ """
        yield 'default'
        for i in self._equipslots:
            for j in i: yield EQUIPSLOTS[j]

    @property
    def equipslots(self):
        """Returns a tuple of equipslot names. The first (index 0) is always
        'default' which is used to reference whatever slot name is at index 1.
        """
        if self._equipslots == 'default': return ('default', self._typename)
        return ('default',) + self._equipslots


# ---- Base Types ------------------------------------------------------------ #
class HeadWear:
    _typename = HDW
    _classifiers = HDW
    _equipslots = "head"


class Neckwear:
    _typename = NEK
    _classifiers = NEK
    _equipslots = "neck"


class Tops:
    _classifiers = TOP
    _typename = TOP


class Bottoms:
    _classifiers = BTM
    _typename = BTM


class Onepiece:
    _classifiers = ONE
    _typename = ONE
    _equipslots = ONE


class Glove:
    _classifiers = GLV
    _typename = GLV
    _weapon_grip = 0 # vs barehanded
    #_punch_dmg_mult =   1   # punch damage multplier


class Footwear:
    _typename = FTW
    _classifiers = FTW
    _slotsize = 2
    _surface_grip_mult = 1   # slick surface grip multiplier
    #_kick_dmg_mult =    1   # kick damage multiplier


# ---- Main wearable sub types ----------------------------------------------- #
class Clothing(WearableType):
    _subcattype =   (CLO,)
    baseres =       BaseRes()
    basestats =     BaseStats()

    class Tops:
        _classifiers = CLO, TOP

    class Bottoms:
        _classifiers = CLO, BTM

    class BodySuit(Onepiece):
        _typename =  BOD
        _classifiers = CLO, BOD
        _slotsize =    3


class Armor(WearableType):
    # min +1 def
    _typename = ARM

    class Top(Tops):
        _classifiers = ARM, TOP

    class Bottoms(Bottoms):
        _classifiers = ARM, BTM,

    class Headwear(Headwear):
        _classifiers = ARM, HDW

    class Glove(Glove):
        _classifiers = ARM, GLV

    class Footwear(Footwear):
        _classifiers = ARM, FTW


class Undies(Clothing):
    _classifiers =  CLO, UND
    _bwt =          0.2

    class Tops(Clothing.Tops):
        _classifiers = CLO, UND, TOP
        _equipslots =  'undies.tops'

    class Bottoms(Clothing.Bottoms):
        _classifiers =  CLO, UND, BTM
        _equipslots =   'undies.Bottoms'


class Swimwear(Clothing):
    _typename = "swimwear"
    _classifiers =  CLO, SWM
    _bwt =      0.2

    class Tops(Tops):
        _classifiers = CLO, SWM, TOP
        _equipslots = 'undies.tops'

    class Bottoms(Bottoms):
        _classifiers = CLO, SWM, BTM
        _equipslots = 'undies.Bottoms'

    class Onepiece(Onepiece):
        _classifiers = CLO, SWM, ONE


class Accessories(WearableType):
    _classifiers =   (ACC,)

    class Headwear(Headwear):
        _classifiers = ACC, HDW

    class Neckwear(Neckwear):
        _classifiers = ACC, NEK


class Jewelry(Accessories):
    _classifiers =   (JEW, ACC)

    class Headwear(Headwear):
        _classifiers = JEW, ACC, HDW

    class Neckwear(Neckwear):
        _classifiers = JEW, ACC, NEK


# ---- clothing types -------------------------------------------------------- #
# tops
class Shirt(Clothing.Tops):
    _classifiers =  CLO, TOP
    _typename =     "shirt"

class Bustier(Clothing.Tops):
    _classifiers =  CLO, TOP
    _typename =     "bustier"

class Dress(Clothing.Tops):
    _classifiers =  CLO, TOP
    _typename =     "dress"


# Bottoms
class Skirt(Clothing.Bottoms):
    _classifiers =  CLO, BTM
    _typename =     "skirt"

class Loincloth(Clothing.Bottoms):
    _classifiers =  CLO, BTM
    _typename =     "loincloth"

class Pants(Clothing.Bottoms):
    _classifiers =  CLO, BTM
    _typename =     "pants"


# misc
class CatSuit(Clothing.BodySuit):
    _typename = "catsuit"
    _forcelayer = "top"


class Glove(Clothing.Glove):
    _classifiers = CLO, "glove"


class Sock(Clothing):
    _classifiers = CLO,
    _typename =     "sock"

class Stocking(Sock):
    _classifiers = CLO,
    _typename = "stocking"


class Shoe(Footwear):
    _bwt =      0.5

class Boot(Footwear):
    _bwt =      0.7


# ---- Swimwear types -------------------------------------------------------- #
class _Bikini(Swimwear):
    _inctags = "bikini"

    class Top(Swimwear.Top):
        _typename = "bikini top"

    class Bottom(Swimwear.Bottoms):
        _typename = "bikini Bottom"

    class Thong(Swimwear.Bottoms):
        _typename = "bikini thong"


# ---- Armor types ----------------------------------------------------------- #
class Gauntlet(Armor.Glove):
    _typename = "gauntlet"
    _typedesc = """An armored glove."""
    _forcelayer = "top"


class Curiass(Armor.Top):
    _typename = "curiass"
    _forcelayer = "top"


class Breastplate(Armor.Top):
    _typename = "breastplate"
    _forcelayer = "top"


class Helm(Armor.Headwear):
    _classifiers = ARM, HDW
    _typename = "helm"


# ---- Jewelry --------------------------------------------------------------- #
class Hairpin(Jewelry):
    _typename = "hairpin"


class Bangle(Jewelry):
    _typename = "bangle"
    _equipslots = "ankle", "wrist"


class Bracelet(Jewelry):
    _typename = "bracelet"
    _equipslots = "ankle", "wrist"


class Necklace(Jewelry.Neckwear):
    _typename = "necklace"


class Choker(Jewelry.Neckwear):
    _typename = "choker"
    _typedesc = """Tight fitting jewelry warn around the neck."""


class Ring(Jewelry):
    _typename = "ring"
    _typedesc = """A piece of jewelry to be worn on a finger or toe."""


class Crown(Jewelry.Headwear):
    _typename = "crown"


class Circlet(Jewelry.Headwear):
    _typename = "circlet"
    _equipslots = "forehead"


# ---- Accessories ----------------------------------------------------------- #
class Glasses(Accessory):
    _typename = "glasses"


class Belt(Accessory):
    _typename = "belt"


class Collar(Accessory.Neckwear):
    _typename = "collar"

