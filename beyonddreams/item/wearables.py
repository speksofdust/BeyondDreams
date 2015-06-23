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


class WearableType(ItemType):
    """Base class for wearable item types."""
    CATTYPE =       "wearable"
    _sc =           (ItemType, )
    equipslots =    _typename


class Jewelry(WearableType):
    _sc =           (WearableType, )
    _inc_ttags =    "jewelry"


class Clothing(WearableType):
    _sc =           (WearableType, )
    _inctags =      "clothing"
    baseres =       BaseRes()
    basestats =     BaseStats()

#define some different base types
class Tops(Clothing):
    _sc =           (Clothing, )
    _inctags =      "tops"

class Bottoms(Clothing):
    _sc =           (Clothing, )
    _inc_ttags =    "bottoms"

class Undies(Clothing):
    _sc =           (Clothing, )
    _inc_ttags =    "undies"
    _bwt =          0.2

class UndiesBottoms(Undies):
    _sc =           Undies, Bottoms

class UndiesTops(Undies):
    _sc =           Undies, Tops
