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




class PawnShop(Shop):
    _name = PAWN_SHOP

class PotionShop(Shop):
    _name = POTION_SHOP

class WeaponShop(Shop):
    _name = WEAPON_SHOP

class SeedShop(Shop):
    _name = SEED_SHOP

class GardeningShop(Shop):
    _name = GARDENING_SHOP

class Pharmacy(Shop):
    _name = PHARMACY


class HerbShop(Shop):
    _name = HERB_SHOP

class IngredientShop(Shop):
    _name = INGREDIENT_SHOP

class Talor(Shop):
    _name = TALOR

class Bar(Shop):
    _name = BAR

class Hotel(Shop):
    _name = HOTEL
