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
from item import BundableItemType
from item import regitem
from item import ItemDict


BOWS =      ("bow", "longbow", "crossbow")
SWORDS =    ("sword", "longsword")
HAMMERS =   ("hammer", "sledge-hammer")

class WeaponFam:
    name =         ""
    includes =     ()
    def __init__(self):
        pass


class RangedWeaponFam(WeaponFam):
    name =          "ranged"
    includes =      BOWS + ("blowgun",)


class BladedWeaponFam(WeaponFam):
    name =          "bladed"
    includes =      SWORDS + ("knife", "dagger")


class PolearmWeaponFam(WeaponFam):
    name =          "ranged"
    includes =      ("spear", "javelin")


class BludgeonWeaponFam(WeaponFam):
    name =          "bludgeon"
    includes =      HAMMERS + ("mace", "morning-star")


class WeaponFamDict():
    def __init__(self):
        super().__init__({
            "ranged":   RangedWeaponFam(),
            "bladed":   BladedWeaponFam(),
            "polearm":  PolearmWeaponFam(),
            "bludgeon": BludgeonWeaponFam(),
            })


# ---- Ammo ------------------------------------------------------------------ #
class Ammo(BundableItemType):
    max_bundlesize =    25
    weapontypes =   () # weapontypes usable in


class Dart(Ammo):
    weapontypes =   ("blowgun",)


class Arrow(Ammo):
    weapontypes =   BOWS


class DefensiveType(WeaponType):


class WeaponAccessories(WeaponType):


# ---- Weapon Types ---------------------------------------------------------- #
class WeaponType(ItemType):
    """Base class for weapon types."""
    CATTYPE =       "weapon"
    _ammotypes =    ()  # compatable ammo types -- empty if uses no ammo


    @property
    def family(self):
        return weapon_family[self._family]


class RangedWeaponType(WeaponType):
    _family =       "ranged"


class BladedWeaponType(WeaponType):
    _family =       "bladed"


class PolearmWeaponType(WeaponType):
    _family =       "polearm"


class BludgeonWeaponType(WeaponType):
    _family =       "bludgeon"


class WeaponTypeDict(ItemDict):
    CATTYPE = "weapon"
    __slots__ = ItemDict.__slots__
    def __init__(self):
        self = {
            "bow": ,            0,
            "longbow":          0,
            "crossbow":         0,
            "blowgun":          0,
            "sword":            0,
            "longsword":        0,
            "dagger":           0,
            "knife":            0,
            "whip":             0,
            "mace":             0,
            "morning-star":     0,
            "hammer":           0,
            "sledge-hammer":    0,
            "cane":             0,
            "staff":            0,
            "rod":              0,
            "hatchet":          0,
            "axe":              0,
            "spear":            0,
            "javelin":          0,
            "halberd":          0,
            "pike":             0,
            }

    def bludgeon(self):
        return iter(i for i in self if i._family == "bludgeon")

    def polearms(self):
        return iter(i for i in self if i._family == "polearm")

    def bladed(self):
        return iter(i for i in self if i._family == "bladed")

    def ranged(self):
        return iter(i for i in self if i._family == "ranged")
