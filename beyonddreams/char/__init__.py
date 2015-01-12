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

__all__ = ()


from .bd import session

from attribs import Body
from attribs import Wallet
from inventory import Inventory
from attribs import Equip

CHAR_ATTRIBNAMES = "body", "inventory", "equip", "stats", "wallet"


def _ac(char):
    global CHAR_ATTRIBNAMES
    # give all char attribs ref to char
    for i in CHAR_ATTRIBNAMES: getattr(char, "_{}".format(i))(char)
        
        
class Char:
    _type = ""
    
    def __init__(self, defaults, player, body=None, inventory=None, equip=None, wallet=None):
        if defaults is None: raise ValueError("Cannot create char without with defaults")
        self._defaults =        defaults
        self._player =          player
        if body is None:        self._body = self._defaults.body()
        else:                   self._body = body
        if inventory is None:   self._inventory = self._defaults.inventory()
        else:                   self._inventory = inventory
        if equip is None:       self._equip = self._defaults.equip()
        else:                   self._equip = equip    
        if stats is None:       self._stats = self._defaults.stats()
        else:                   self._stats = stats
        if wallet is None:      self._wallet = self._defaults.wallet()
        else:                   self._wallet = wallet
        import random
        self._seed =            random.uniform(0.0, 99999.9)
        self._initchar(False)
        

    @classmethod
    def new(self, defaults):
        if defaults is None: raise ValueError("Cannot create char without with defaults")
        self._defaults =        defaults
        self._body =            self._defaults.body()
        self._inventory =       self._defaults.inventory()
        self._equip =           self._defaults.equip()
        self._stats =           self._defaults.stats()
        self._wallet =          self._defaults.wallet()
        import random
        self._seed =            random.uniform(0.0, 99999.9)
        self._initchar(True)
        
    def __bool__(self): return True
    def __hash__(self): return hash(id(self), self._seed)
        
    def __eq__(self, x):
        if isinstance(x, type(self)): return x is self
        raise TypeError("Cannot compare type: '{type(self)}' to '{type(x)}'")
    
    def __ne__(self, x):
        if isinstance(x, type(self)): return x is not self
        raise TypeError("Cannot compare type: '{type(self)}' to '{type(x)}'")
        
    def _initchar(self, isnew):
        _ac(self)

    def is_player(self):
        """True if this char is controlled by the "player" object
            on the local machine."""
        return self._player == session.screen.player

    def is_alive(self):
        """True if this character is alive."""
        return self._stats.health != 0

    def is_critical(self):
        """True if this characters health level is in the critical range."""
        return 0 < self._stats.health <= 20

    @property
    def party(self):
        """The party this char is in."""
        return self._player.party

    @property
    def defaults(self):
        """Default values for this character."""
        return self._defaults

    @property
    def body(self):
        """This characters body attributes."""
        return self._body

    @property
    def wallet(self):
        """This characters money."""
        return self._wallet

    @property
    def inventory(self):
        """This characters inventory."""
        return self._inventory

    @property
    def equip(self):
        """This characters equipment."""
        return self._equip
        
        
