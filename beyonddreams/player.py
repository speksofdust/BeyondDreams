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

def indexed_chardict(chars):
    d = {}
    for i in enumerate(tuple(chars)): d[i[0]] = i[1]
    return d

class CharRoster:
    def __init__(self, chars={}):
        if isinstance(chars, dict): self._chars = chars
        else:
            self._chars = indexed_chardict(chars):
            
    def __getitem__(self, i):   return self._chars[i]
    def __len__(self):          return len(self._chars)
    def __str__(self):          return str(tuple(iter(self._chars)))[1:-1]
    def __repr__(self):         return str(tuple(iter(self._chars)))
    
    def __iter__(self): 
        return iter(self._chars[i] for i in range(0, len(self._chars)))
    
    def __reversed__(self): 
        return iter(self._chars[i] for i in range(len(self._chars)-1, -1, -1))
    
    def idx_from_name(self, name):
        for i in self._chars:
            if i.name == name: return i 
    
    def swap_indices(self, idx_a, idx_b):
        tmp = self[idx_a]
        self[idx_a] = self[idx_b] 
        self[idx_b] = tmp
        
    # ---- game only ----------------------------------------------------- #
    def get_alive(self):
        """Return an iterator of all characters still alive."""
        return iter(i for i in self._chars if i.is_alive())
        
    def get_critical(self):
        """Return an iterator of all characters with critical health levels."""
        return iter(i for i in self._chars if i.is_critical())


class Player:
    def __init__(self):
        self._chars =   CharRoster()
        self._pid =     0   # always 0 if not in online game
        
    @property
    def chars(self):
        """The character roster for this player."""
        return self._chars
        
    
    
        
        
        
        
