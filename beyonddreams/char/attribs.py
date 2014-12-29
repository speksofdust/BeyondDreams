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

from .. import bd

class CharAttrib:
    __slots__ = ("_char",)
    """Base class for all character attributes."""
    def __init__(self):
        self._char = None

    @property
    def char(self):
        """The char this attribute belongs to."""
        return self._char
    
    
class Coupons:
    __slots__ = "_wallet", "_items"
    def __init__(self, wallet, items=[]): 
        self._wallet = wallet
        self._items = list(items)
    

class Wallet(CharAttrib):
    __slots__ = CharAttrib.__slots__ + "_cash", "_coupons"
    def __init__(self, zil=0, coupons=[]):
        self._char = None
        self._cash = (zil,)
        self._coupons = Coupons(self, coupons)
        
    @classmethod
    def default(self):
        self._cash = (0,)
        self._coupons = Coupons(self) 

    @property
    def zil(self):
        """The primary form of currency in bd."""
        return self._cash[0]


class Equip(CharAttrib):
    __slots__ = CharAttrib.__slots__
    def __init__(self):
        self._char = None


class Body(CharAttrib):
    __slots__ = CharAttrib.__slots__ + "_subparts", "_attribs", "_mesh"
    def __init__(self):
        self._char = None
        self._subparts = {}
        self._attribs = {}
        #bd.datapath()  TODO

    @property
    def subparts(self):
        return self._subparts

    @property
    def attribs(self):
        return self._attribs
