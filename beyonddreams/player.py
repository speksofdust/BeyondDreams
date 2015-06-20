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


class CharStorageMixin:

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

    def _move_down(self, x):
        if idx < len(self._chars):
            self._chars[idx + 1] = self._chars[idx].pop()

    def _move_up(self, x):
        if idx > 0: self._chars[idx - 1] = self._chars[idx].pop()

    def move_down(self, x):
        self._move_down(self.index(x))

    def move_up(self, x):
        self._move_up(self.index(x))

    def idx_from_name(self, name):
        for i in self._chars:
            if i.name == name: return i

    def index(self, x):
        try: return self._chars.index(char)
        except:
            try: return idx_from_name(char)
            except: raise IndexError("Cannot get index from item: {}".format(x))

    def swap_indices(self, idx_a, idx_b):
        tmp = self._chars[idx_a]
        self._chars[idx_a] = self._chars[idx_b]
        self._chars[idx_b] = tmp


class Party(CharStorageBC):
    MAX_CHARS = 8
    def __init__(self):
        self._chars = CharRoster()
        self._current = None    # stored as an index (int)

    def is_full(self):
        """True if no more members can be added to this party."""
        return len(self._chars) == self.MAX_CHARS

    def next(self, available=True):
        """Set the next item as the current item."""
        self._current = self.next_index(available)

    def prev(self, available=True):
        """Set the previous item as the current item."""
        self._current = self._prev_index(available)

    def get_next(self, available=True):
        """Return the next item."""
        return self._chars[self.next_index(available)]

    def get_prev(self, available=True):
        """Return the previous item."""
        return self._chars[self.prev_index(available)]

    def next_index(self, available=True):
        """Return the index of the next item."""
        try:
            if available:
                if self._current < len(self._chars):
                    n = self._current
                    while True:
                        if n > self._current:
                            if self.is_available(self._chars[n + 1]): return n + 1
                        break
                if self.is_available(self._chars[0]): return 0
                return self._current
            if self._current < len(self._chars): return self._current + 1
            return 0
        except: return None

    def prev_index(self, available=True):
        """Return the index of the previous item."""
        try:
            if available:
                n = self._current
                while True:
                    if n != self._current:
                        if n == 0:
                            if self.is_available(self._chars[n-1]): return len(self._chars)
                            else: n = len(self._chars)
                        else:
                            if self.is_available(self._chars[n-1]): return n
                            else: n -= 1
            if self._current == 0: return len(self._chars)
            return self._current - 1
        except:
            return None

    def is_available(self, i):
        """True if a given character is currently available for play."""
        return i in self.get_available()

    def get_available(self):
        """Return an iterator of characters that are currently alive and available
        for play, sorted by highest health to lowest."""
        from operator import methodcaller
        for i in sorted(self._chars, key=methodcaller(i.health))
            if i.is_alive(): yield i

    def get_alive(self):
        """Return an iterator of all characters still alive."""
        return iter(i for i in self._chars if i.is_alive())

    def get_critical(self):
        """Return an iterator of all characters with critical health levels."""
        return iter(i for i in self._chars if i.is_critical())


class Player:
    _is_ai = False
    def __init__(self):
        self._party =   Party()
        self._pid =     0   # always 0 if not in online game

    @property
    def party(self):
        """The character roster for this player."""
        return self._party

    def is_ai(self):
        """True is this player is AI controlled. (Non-Human)."""
        return self._is_ai


class AIPlayer(Player):
    _is_ai = True


