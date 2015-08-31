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


class WearableTypeDict(ItemDict):
    CATTYPE = "wearable"
    __slots__ = ItemDict.__slots__


class WearableType(ItemType):
    """Base class for wearable item types."""
    CATTYPE =       "wearable"
    _sc =           (ItemType, )
    equipslots =    _typename


class Jewelry(WearableType):
    _sc =           (WearableType, )
    _inctags =      "jewelry"


class _WTJ(Jewelry):
    # wearable type jewelry
    # Helper class for Jewlery
    _sc =           (Jewelry, )


class Clothing(WearableType):
    _sc =           (WearableType, )
    _inctags =      "clothing"
    baseres =       BaseRes()
    basestats =     BaseStats()


class _WTC(Clothing):
    # wearable type clothing
    # Helper class for Clothing
    _sc =           (Clothing, )


# ---- Clothing Base Types --------------------------------------------------- #
class Tops(_WTC):
    _inctags =      "tops"


class Bottoms(_WTC):
    _inctags =    "bottoms"


class Undies(_WTC):
    _inctags =    "undies"
    _bwt =          0.2


class UndiesBottoms(Undies):
    _sc =           Undies, Bottoms


class UndiesTops(Undies):
    _sc =           Undies, Tops


class Footwear(_WTC):
    _surface_grip_mult =    1   # slick surface grip multiplier
    #_kick_dmg_mult =        1   # kick damage multiplier


class Shoe(Footwear):
    _sc =       (Footwear, )
    _bwt =      0.5


class Boot(Footwear):
    _sc =       (Footwear, )
    _bwt =      0.7


# ---- Clothing Sub Types ---------------------------------------------------- #
class Glove(_WTC):
    # increases punch damage
    # may increase weapon grip
    _typename =         "glove"
    _weapon_grip =      0   # vs barehanded
    #_punch_dmg_mult =   1   # punch damage multplier


class Sock(_WTC):
    _typename =     "sock"


class Shirt(Tops):
    _typename =     "shirt"


class Dress(Tops):
    _typename =     "dress"


class Skirt(Bottoms):
    _typename =     "skirt"


class Pants(Bottoms):
    _typename =     "pants"



