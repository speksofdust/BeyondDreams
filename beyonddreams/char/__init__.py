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

def _get_new_char():
    return
    
    
from attribs import Body
from attribs import Wallet
from attribs import Inventory
from attribs import Equip

    
class Char:
    def __init__(self):
        self._body =        Body(self)
        self._wallet =      Wallet(self)
        self._inventory =   Inventory(self)
        self._equip =       Equip(self)

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
        
        
