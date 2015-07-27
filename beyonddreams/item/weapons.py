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


class WeaponTypeDict(ItemDict):
    CATTYPE = "weapon"
    __slots__ = ItemDict.__slots__


class WeaponType(ItemType):
    """Base class for weapon types."""
    _sc =           (ItemType,)
    CATTYPE =       "weapon"
    BUNDLESIZE =    1
    _ammotypes =    ()  # compatable ammo types -- empty if uses no ammo


class Ammo(WeaponType):
    _sc =           (WeaponType,)
    BUNDLESIZE =    25
    weapontypes =   () # weapontypes usable in


class DefensiveType(WeaponType):
    _sc =           (WeaponType,)



class WeaponAccessories(WeaponType):
    _sc =           (WeaponType,)

