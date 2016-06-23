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
from shophours import ShopHours
from shophours import ShopDay, CLOSED_TODAY, ShopdayNoBreak





class PawnShop(Shop):
    _shoptype = PAWN
    _default_hours = ShopHours()

class PotionShop(Shop):
    _shoptype = POTION_SHOP
    _default_hours = ShopHours()

class WeaponShop(Shop):
    _shoptype = WEAPON_SHOP
    _default_hours = ShopHours()

class Blacksmith (Shop):
    _shoptype = BLACKSMITH
    _default_hours = Shop hours()

class SeedShop(Shop):
    _shoptype = SEED_SHOP
    _default_hours = ShopHours()

class GardeningShop(Shop):
    _shoptype = GARDENING_SHOP
    _default_hours = ShopHours()

class Pharmacy(Shop):
    _shoptype = PHARMACY
    _default_hours = ShopHours()

class HerbShop(Shop):
    _shoptype = HERB_SHOP
    _default_hours = ShopHours()

class IngredientShop(Shop):
    _shoptype = INGREDIENT_SHOP
    _default_hours = ShopHours()

class Talor(Shop):
    _shoptype = TALOR
    _default_hours = ShopHours()

class Bar(Shop):
    _shoptype = BAR
    _default_hours = ShopHours()

class Hotel(Shop):
    _shoptype = HOTEL
    _default_hours = ShopHours()

class Inn(Shop):
    _shoptype = INN
    _default_hours = ShopHours()
