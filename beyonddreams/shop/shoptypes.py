# ---------------------------------------------------------------------------- #
#                                                                              #
#     This program is free software(Shop): you can redistribute it and/or modify     #
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
#     along with this program. If not, see <http(Shop)://www.gnu.org/licenses/>.     #
#                                                                              #
# ---------------------------------------------------------------------------- #

from shop import Shop
from shop.shopnames import *
from shophours import ShopWeek
from shophours import ShopDay, CLOSED_TODAY, ShopdayNoBreak

SHOPICONS = {
    PAWN_SHOP:          (),
    POTION_SHOP:        (),
    PHARMACY:           (),
    WEAPON_SHOP:        (),
    BLACKSMITH:         (),
    SEED_SHOP:          (),
    GARDENING_SHOP:     (),
    INGREDIENT_SHOP:    (),
    TALOR:              (),
    CLOTHING_SHOP:      (),
    DRESSMAKER:         (),
    BAR:                (),
    HOTEL:              (),
    INN:                (),
    JEWLER:             (),
    GUILDHOUSE:         (),
    GUILDOFFICE:        (),
    BANK:               ()
};

SERVICES = "services"
GOODS = "goods"

class PawnShop(Shop):
    _shoptype = PAWN
    _default_hours = ShopWeek()

class PotionShop(Shop):
    _shoptype = POTION_SHOP
    _default_hours = ShopWeek()

class Pharmacy(Shop):
    _shoptype = PHARMACY
    _default_hours = ShopWeek()

class WeaponShop(Shop):
    _shoptype = WEAPON_SHOP
    _default_hours = ShopWeek()

class Blacksmith (Shop):
    _shoptype = BLACKSMITH
    _default_hours = ShopWeek()
    _tags = (SERVICES,)

class SeedShop(Shop):
    _shoptype = SEED_SHOP
    _default_hours = ShopWeek()

class GardeningShop(Shop):
    _shoptype = GARDENING_SHOP
    _default_hours = ShopWeek()

class HerbShop(Shop):
    _shoptype = HERB_SHOP
    _default_hours = ShopWeek()

class IngredientShop(Shop):
    _shoptype = INGREDIENT_SHOP
    _default_hours = ShopWeek()

class Talor(Shop):
    _shoptype = TALOR
    _default_hours = ShopWeek()
    _tags = "clothing", SERVICES

class ClothingShop(Shop):
    _shoptype = CLOTHING_SHOP
    _default_hours = ShopWeek()
    _tags = "clothing"

class DressMaker(Shop):
    _shoptype = DressMaker
    _default_hours = ShopWeek()
    _tags = "clothing", SERVICES

class FabricShop(Shop):
    _shoptype = FABRIC_SHOP
    _default_hours = ShopWeek()

class Bar(Shop):
    _shoptype = BAR
    _default_hours = ShopWeek()

class Hotel(Shop):
    _shoptype = HOTEL
    _default_hours = ShopWeek()

class Inn(Shop):
    _shoptype = INN
    _default_hours = ShopWeek()

class Jeweler(Shop):
    _shoptype = JEWELER
    _default_hours = ShopWeek()

class GuildHouse(Shop):
    _shoptype = GUILD_HOUSE
    _default_hours = ShopWeek()



class GuildOffice(Shop):
    _shoptype = GUILD_OFFICE
    _default_hours = ShopWeek.SameWeekdayHours(sat, sun=CLOSED_TODAY)
