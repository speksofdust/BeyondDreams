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
        

class BDCharException(Exception): pass
        
        
def _initca(char, v, attribcls):
    # helper for initalizing each charattirb type
    if isinstance(v, attribcls): return charattrib
    elif v is None: return charratrib(char)
    else: return charattrib(char, *v)
        
def finalize_char(char, player):
    """Finalize changes, called when character editing (post creation)
        is done."""
    try: char._finalize(player)
    except: raise BDCharException("Character '{}' already finalized".format(char)))


class Char:
    _type = "normal"
    def __init__(self, player):
        self._finalized =       False
        self._player =          player
        self._base =            base
        self._items = {
            BODY:   Body(self)
            }
    
    def _finalize(self, player):
        if not self._finalized
            self._player =  player
            self._items = {
                "body":           None,
                "inventory":      Inventory(self),
                "equip":          Equip(self),
                "wallet":         Wallet(self),
                "stats":          Stats(self),
                "statuses":       Statuses(self),
                "resistances":    None
                }
        else: raise BDCharException
    
    def __iter__(self):         return iter(self._items)
    def __len__(self):          return len(self._items)
    def __str__(self):          return str(self._items)[1:-1]
    def __repr__(self):         return repr(self._items)
    def __bool__(self):         return True
    def __hash__(self):         return hash(id(self))
    def __getitem__(self, i):   return self._items[i]
        
    def __eq__(self, x):
        if isinstance(x, type(self)): return x is self
        raise TypeError("Cannot compare type: '{type(self)}' to '{type(x)}'")
    
    def __ne__(self, x):
        if isinstance(x, type(self)): return x is not self
        raise TypeError("Cannot compare type: '{type(self)}' to '{type(x)}'")

    @property
    def party(self):
        """The party this char is in."""
        return self._player._items[PARTY]

    @property
    def base(self):
        """Base values for this character."""
        return self._base

    @property
    def body(self):
        """This characters body attributes."""
        return self._items[BODY]

    @property
    def wallet(self):
        """This characters wallet."""
        return self._items[WALLET]

    @property
    def inventory(self):
        """This characters inventory."""
        return self._items[INVENTORY]

    @property
    def equip(self):
        """This characters equipment."""
        return self._items[EQUIP]

    def is_player(self):
        """True if this char is controlled by the "player" object
            on the local machine."""
        return self._player == session.screen.player

    def is_alive(self):
        """True if this character is alive."""
        if self._items[STATS][HP] == 0: return False
        return True

    def is_critical(self):
        """True if this characters health level is in the critical range."""
        return self._items[STATS][HP].is_critical()

    @property
    def famtypes(self):
        """Return family types for this character."""
        return ()

    def is_undead(self):
        """True if this character is an undead type or has zombie status."""
        return ("zombie" in self._items[STATUSES]["bools"] or 
            "zombie" in self.famtypes)


        
class NPC(Char):
    """Non playable char."""
    
