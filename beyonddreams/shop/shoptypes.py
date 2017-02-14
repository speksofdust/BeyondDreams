# ---------------------------------------------------------------------------- #
#                                                                              #
#     This program is free software(shop.): you can redistribute it and/or modify     #
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
#     along with this program. If not, see <http(shop.)://www.gnu.org/licenses/>.     #
#                                                                              #
# ---------------------------------------------------------------------------- #

import shop
from shop.shopnames import *
from shophours import ShopWeek
from shophours import ShopDay, CLOSED_TODAY, ShopdayNoBreak


class PawnShop(shop.Store):
    name = "pawn shop"
    _icon = ()
    _default_hours = ShopWeek()
    _tags = ("pawn",)


class Bank(shop.Service):
    name = "bank"
    _icon = ()
    _default_hours = ShopWeek()


# ---- Alchemy? -------------------------------------------------------------- #
class IngredientShop(shop.Store):
    name = "ingredient shop"
    _icon = ()
    _default_hours = ShopWeek()
    _tags = "alchemy", "ingredients"


class PotionShop(shop.Store):
    name = "potion shop"
    _icon = ()
    shoptype = GOODS
    _default_hours = ShopWeek()
    _tags = "alchemy", "potion"


# ---- Health ---------------------------------------------------------------- #
class Pharmacy(shop.Store):
    name = "pharmacy"
    _icon = ()
    _default_hours = ShopWeek()


class Gym(shop.Service):
    name = "gym"
    _icon = ()
    _default_hours = ShopWeek()


# ---- Weapons & Armor ------------------------------------------------------- #
class WeaponShop(shop.Store):
    name = "weapon shop"
    _icon = ()
    _default_hours = ShopWeek()
    _tags = "weapons"


class Armory(shop.Store):
    name = "armory"
    _icon = ()
    _default_hours = ShopWeek()
    _tags = "armor"


class Blacksmith (shop.Service):
    name = "blacksmith"
    _icon = ()
    _default_hours = ShopWeek()


# ---- Gardening ------------------------------------------------------------- #
class SeedShop(shop.Store):
    name = "seed shop"
    _icon = ()
    _default_hours = ShopWeek()
    _shoptags = "store"


class GardeningShop(shop.Store):
    name = "gardening shop"
    _icon = ()
    _default_hours = ShopWeek()
    _tags = ("gardening",)


class HerbShop(shop.Store):
    name = "herb shop"
    _icon = ()
    _default_hours = ShopWeek()
    _tags = "crafting", "ingredients"


# ---- Clothing -------------------------------------------------------------- #
class ClothingShop(shop.Store):
    name = "clothing shop"
    _icon = ()
    _default_hours = ShopWeek()
    _tags = ("clothing",)


class Jeweler(shop.Both):
    name = "jeweler"
    _icon = ()
    _default_hours = ShopWeek()
    _tags = ("jewelry",)


class Talor(shop.Both):
    name = "talor"
    _icon = ()
    _default_hours = ShopWeek()
    _tags = ("clothing",)


class DressMaker(shop.Both):
    name = "dressmaker"
    _icon = ()
    _default_hours = ShopWeek()
    _tags = ("clothing",)


class FabricShop(shop.Store):
    name = "fabric shop"
    _icon = ()
    _default_hours = ShopWeek()
    _tags = ("clothing",)


# ---- Rest and Relaxation ---- #
class Bar(shop.Service):
    name = "bar"
    _icon = ()
    _default_hours = ShopWeek()


class Hotel(shop.Service):
    name = "hotel"
    _icon = ()
    _default_hours = ShopWeek()


class Inn(shop.Service):
    name = "inn"
    _icon = ()
    _default_hours = ShopWeek()


class Spa(shop.Service):
    name = "spa"
    _icon = ()
    _default_hours = ShopWeek()


# ---- Guild Related ---- #
class GuildHouse(shop.Service):
    name = "guild house"
    _icon = ()
    _default_hours = ShopWeek()
    _tags = ("guild",)


class GuildOffice(shop.Service):
    name = "guild office"
    _icon = ()
    _default_hours = ShopWeek.SameWeekdayHours(sat, sun=CLOSED_TODAY)
    _tags = ("guild",)
