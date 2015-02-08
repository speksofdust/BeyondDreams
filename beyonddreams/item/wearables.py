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
    equipslots =    _typename
    
    
class Jewelry(WearableType):
    _inc_ttags =      "jewelry"
    
    
class Clothing(WearableType):
    _inc_ttags =    "clothing"
    baseres =       BaseRes()
    basestats =     BaseStats()

#define some different base types
class Tops(Clothing):
    _inc_ttags = "clothing", "tops"

class Bottoms(Clothing):
    _inc_ttags = "clothing", "bottoms"

class Undies(Clothing):
    _inc_ttags = "clothing", "undies"
    _bwt =      0.2

class UndiesBottoms(Undies):
    _inc_ttags = "clothing", "undies", "bottoms"

class UndiesTops(Undies):
    _inc_ttags = "clothing", "undies", "tops"
