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


class CardType:
    _typename = "card"
    __slots__ = ()


class CouponType:
    _typename = "coupon"
    __slots__ = ()


class CashType(int):
    _typename = "cash"
    _name = ""
    _symbol = ""
    __slots__ = ()


class Zil(CashType):
    _name = "Zil"
    _symbol = "Z"
    __slots__ = ()


class Pocket:
    _name = ""


    @property
    def name(self):
        """The name of this pocket."""
        return self._name


class InventoryPocket(Pocket):
    """Pocket class for inventory objects."""


class WalletPocket(Pocket):
    """Pocket class for wallet objects."""


class CashPocketItem:
    _typename = ""
    def __init__(self, value=0):
        self = value

    def has_cash(self, *needed):
        """Return True if the current amount of cash is equal or greater than the
        sum of all values in 'needed'"""
        return self >= sum(needed)


class CashPocket(WalletPocket):
    _name = "cash"
    def __init__(self, zil):
        self = [zil]


class CouponPocket(WalletPocket):
    _name = "coupons"


class CardPocket(WalletPocket):
    _name = "cards"


class Wallet(CharAttrib):
    _name = "wallet"
    __slots__ = CharAttrib.__slots__ + "_coupons"
    def __init__(self, chardata, zil=0):
        self._chardata = chardata
        self = (
            CashPocket((zil)),
            CouponPocket(),
            CardPocket()
            )

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

