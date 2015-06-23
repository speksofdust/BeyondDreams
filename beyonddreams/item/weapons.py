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


class WeaponType(ItemType):
    """Base class for weapon types."""
    _sc =           (ItemType,)
    CATTYPE =       "weapon"
    BUNDLESIZE =    1


class Ammo(WeaponType):
    _sc =           (WeaponType,)
    BUNDLESIZE =    25
    weapontypes =   () # weapontypes usable in


class DefensiveType(WeaponType):
    _sc =           (WeaponType,)



class WeaponAccessories(WeaponType):
    _sc =           (WeaponType,)

