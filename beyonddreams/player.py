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


class CharStorageBC:
    
    def __eq__(self, x):        return self._chars == x
    def __ne__(self, x):        return self._chars != x
    def __str__(self):          return str(self._chars)[1:-1]
    def __repr__(self):         return repr(self._chars)
    def __getitem__(self, i):   return self._chars[i]
    def __bool__(self):         return len(self._chars) != 0
    def __len__(self):          return len(self._chars)
    def __iter__(self):         return iter(self._chars)
    def __reversed__(self):     return reversed(self._chars)
    
    def index(self, n):
        return self._chars.index(n)
        

class CharRoster(CharStorageBC):
    def __init__(self, chars=[]):
        self._chars = list(chars)
    
    def idx_from_name(self, name):
        for i in self._chars:
            if i.name == name: return i 
    
    def swap_indices(self, idx_a, idx_b):
        tmp = self[idx_a]
        self[idx_a] = self[idx_b] 
        self[idx_b] = tmp


class Party(CharStorageBC):
    MAX_CHARS = 8
    def __init__(self):
        self._items = CharRoster()
        self._current = None    # stored as an index (int)
        
    def is_full(self):
        """True if no more members can be added to this party."""
        return len(self._items) == self.MAX_CHARS
        
    def next(self):
        """Set the next item as the current item."""
        self._current = self.next_index()
        
    def prev(self):
        """Set the previous item as the current item."""
        self._current = self._prev_index()
        
    def get_next(self):
        """Return the next item."""
        return self._items[self.next_index()]
        
    def get_prev(self):
        """Return the previous item."""
        return self._items[self.prev_index()]
    
    def next_index(self):
        """Return the index of the next item."""
        try: 
            if self._current < len(self._items): return self._current + 1
            return 0
        except: return None

    def prev_index(self):
        """Return the index of the previous item."""
        try:
            if self._current == 0: return len(self._items)
            return self._current - 1
        except:
            return None

    def get_alive(self):
        """Return an iterator of all characters still alive."""
        return iter(i for i in self._items if i.is_alive())
        
    def get_critical(self):
        """Return an iterator of all characters with critical health levels."""
        return iter(i for i in self._items if i.is_critical())


class Player:
    _type = ""
    def __init__(self):
        self._party =   Party()
        self._pid =     0   # always 0 if not in online game
        
    @property
    def party(self):
        """The character roster for this player."""
        return self._party
        
        
class AIPlayer(Player):
    _type = "AI"
    
    
        
        
        
        
