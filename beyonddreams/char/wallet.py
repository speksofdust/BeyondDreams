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

from .item import ItemStorageChar
from .item import ItemStoragePocket


class CardType:
    _typename = "card"
    __slots__ = ()


DEFAULT = 0
PERCENT_OFF = 1
FREE = 2

# coupon abbrs
BQGQ = 0
PERCOFF = 1
class CouponType:
    _typename = "coupon"
    modes = {BQGQ:(1,2),}
    __slots__ = ()

    def _set_coupon(char, name, coupontype, a, b, exp, d=0):
        char.wallet.coupons.append(name, coupontype, a, b, exp, d)

    def bqgq(char, name, req_qty, get_qty, expires, mode=0):
        """'Buy qty get qty' coupon type."""
        if (get_qty > 0 and req_qty >= 0)
            _set_coupon(char, name, BQGQ, req_qty, get_qty, expires, mode)

    def percentoff(char, name, req_qty, val_off, expire):
            if (req_qty >= 1 and off > 0):
                _set_coupon(char, name, PERCOFF, req_qty, val_off, expire)


class CashType(int):
    _typename = "cash"
    _name = ""
    _symbol = ""
    __slots__ = ()


class Zil(CashType):
    _name = "Zil"
    _symbol = "Z"
    __slots__ = ()


class CashPocketItem:
    _typename = ""
    def __init__(self, value=0):
        self = value

    def has_cash(self, *needed):
        """Return True if the current amount of cash is equal or greater than the
        sum of all values in 'needed'"""
        return self >= sum(needed)


class Pockets:
    class _BC(list):
        _pockettype = ""
        __slots__ = list.__slots__

    class Cash(_BC):
        _pockettype = "cash"
        __slots__ = list.__slots__

    class Coupon(_BC,):
        _pockettype = "coupon"
        __slots__ = list.__slots__

    class Cards(_BC, list):
        _pockettype = "cards"
        __slots__ = list.__slots__


class Wallet(tuple):
    _name = "wallet"
    __slots__ = '_char'
    def __init__(self, char, data=[[],[],[]]):
        super().__init__((
            Pockets.Cash(data[0]),
            PocketsCoupons(data[1]),
            Pockets.Cards(data[2])
            )
        self._char = char

    @property
    def cash(self):
        """Access the cash pocket."""
        return self[0]

    @property
    def coupons(self):
        """Access the coupons pocket."""
        return self[1]

    @property
    def cards(self):
        """Access the cards pocket."""
        return self[2]

