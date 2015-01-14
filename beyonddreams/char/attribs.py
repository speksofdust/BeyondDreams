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
    def __init__(self, char):
        self._char = char
        
    @property
    def char(self):
        """The char this attribute belongs to."""
        return self._char
        
    @property
    def char_defaults(self):
        """Defaults for the char which this attribute belongs to."""
        return self._char._defaults
        
        
class CharAttribSubAttrib:
    """Subattribute class for use within a CharAttrib class."""
    __slots__ = ()
    def __init__(self, charattrib):
        self._charattrib = charattrib

    @property
    def charattrib(self):
        """The charattrib this is part of."""
        return self._charattrib

    @property
    def char(self):
        """The character which this belongs to."""
        return self._charattrib._char
    
    
class Coupons:
    __slots__ = "_wallet", "_items"
    def __init__(self, wallet, items=[]): 
        self._wallet = wallet
        self._items = list(items)
    

class Wallet(CharAttrib):
    __slots__ = CharAttrib.__slots__ + "_cash", "_coupons"
    def __init__(self, char, zil=0, coupons=[]):
        self._char = char
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
    def __init__(self, char):
        self._char = char


class Body(CharAttrib):
    __slots__ = CharAttrib.__slots__ + "_subparts", "_attribs", "_mesh"
    def __init__(self, char):
        self._char = char
        self._subparts = {}
        self._attribs = {}
        #bd.datapath()  TODO

    @property
    def subparts(self):
        return self._subparts

    @property
    def attribs(self):
        return self._attribs
    
        
class Stats(CharAttrib):
    __slots__ = CharAttrib.__slots__
    def __init__(self, char):
        self._char = char
        
    def base(self):
        return self._char._base._stats
        
        
class StatusEffects(CharAttrib):
    __slots__ = CharAttrib.__slots__
    def __init__(self, char):
        self._char = char
        
    def base(self):
        return self._char._base._stats
