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
from attribs import Stats
from attribs import StatusEffects
        
def _initca(char, v, attribcls):
    # helper for initalizing each charattirb type
    if isinstance(v, attribcls): return charattrib
    elif v is None: return charratrib(char)
    else: return charattrib(char, *v)
        
class Char:
    _type = "normal"
    CHARATTRIB_NAMES = "body", "inventory", "equip", "wallet", "stats", "statuseffects"
    def __init__(self, player, base=None, body=None, inventory=None, equip=None, 
        wallet=None, stats=None, statuseffects=None):
        self._player =          player
        self._base =            base
        self._body =            _initca(self, body, Body)
        self._inventory =       _initca(self, inventory, Inventory)
        self._equip =           _initca(self, equip, Equip)
        self._wallet =          _initca(self, wallet, Wallet)
        self._stats =           _initca(self, stats, Stats)
        self._statuseffects =   _initca(self, statuseffects, StatusEffects)
        import random
        self._seed =        random.uniform(0.0, 99999.9)
        
        
    def __bool__(self): return True
    def __hash__(self): return hash(id(self), self._seed)
        
    def __eq__(self, x):
        if isinstance(x, type(self)): return x is self
        raise TypeError("Cannot compare type: '{type(self)}' to '{type(x)}'")
    
    def __ne__(self, x):
        if isinstance(x, type(self)): return x is not self
        raise TypeError("Cannot compare type: '{type(self)}' to '{type(x)}'")

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
        """This characters wallet."""
        return self._wallet

    @property
    def inventory(self):
        """This characters inventory."""
        return self._inventory

    @property
    def equip(self):
        """This characters equipment."""
        return self._equip

        
class NPC(Char):
    """Non playable char."""
    
