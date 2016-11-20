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


from core.baseclasses import BDList
from core.baseclasses import BBSelectedItemList
from vident import VIDENT_TYPES


class CharRoster(BDList):
    _sort_kwds = "name"

    def sort_by(self, kw, reverse):
        if kw in self._sort_kwds:
            from operator import attrgetter
            self.sort(key=attrgetter(kw), reverse=reverse)

    def idx_from_name(self, name):
        for i in self:
            if i.name == name: return i

    def index(self, x):
        try: return self._chars.index(char)
        except:
            try: return idx_from_name(char)
            except: raise IndexError("Cannot get index from item: {}".format(x))


class _Party(GameDataAccessor):
    _ident = VIDENT_TYPES["party"]
    MAX_CHARS = 8
    def __dpath(): return gamedata['party'][1]
    __slots__ = ()
    def __init__(self): pass

    def is_full(self):
        """True if no more members can be added to this party."""
        return len(self) == self.MAX_CHARS

    def _get_active(self): return gamedata['party'][0]
    def _set_active(self, i):
        if 0 <= i <= 8: gamedata['party'][0] = i
        else:
            if i in self.__dpath(): gamedata['party'][0] = self.__dpath.index(i)
    current = property(_get_current, _set_current,
        doc="""The active party member.""")

    def alive(self):
        """Return an iterator of all alive party members."""
        pass


class Party(BDSelectedItemList, CharRoster):
    _ident = VIDENT_TYPES["party"]
    MAX_CHARS = 8
    def __init__(self):
        self = []
        self._current = None    # stored as an index (int)

    def is_full(self):
        """True if no more members can be added to this party."""
        return len(self) == self.MAX_CHARS

    def next(self, available=True):
        """Set the next item as the current item."""
        self._current = self.next_index(available)

    def prev(self, available=True):
        """Set the previous item as the current item."""
        self._current = self._prev_index(available)

    def get_next(self, available=True):
        """Return the next item."""
        return self[self.next_index(available)]

    def get_prev(self, available=True):
        """Return the previous item."""
        return self[self.prev_index(available)]

    def next_index(self, available=True):
        """Return the index of the next item."""
        try:
            if available:
                if self._current < len(self):
                    n = self._current
                    while True:
                        if n > self._current:
                            if self.is_available(self[n + 1]): return n + 1
                        break
                if self.is_available(self[0]): return 0
                return self._current
            if self._current < len(self): return self._current + 1
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
                            if self.is_available(self[n-1]): return len(self)
                            else: n = len(self)
                        else:
                            if self.is_available(self[n-1]): return n
                            else: n -= 1
            if self._current == 0: return len(self)
            return self._current - 1
        except:
            return None

    def is_available(self, i):
        """True if a given character is currently available for play."""
        return i in self.get_available()

    def get_available(self):
        """Return an iterator of characters that are currently alive and available
        for play, sorted by highest health to lowest."""
        from operator import attrgetter
        x = sorted(self, key=attrgetter(i.health))
        for i in x:
            if i.is_alive(): yield i

    def get_alive(self):
        """Return an iterator of all characters still alive."""
        return iter(i for i in self if i.is_alive())

    def get_critical(self):
        """Return an iterator of all characters with critical health levels."""
        return iter(i for i in self if i.is_critical())


class Player:
    _ident = VIDENT_TYPES["player"]
    _is_ai = False
    def __init__(self, game):
        self._game =    game
        self._party =   Party()
        self._pid =     0   # player id -- always 0 if not in online game

    def __eq__(self, other): return this._pid == other._pid
    def __ne__(self, other): return this._pid != other._pid

    # ---- Network only ------------------------------------ #
    #def _req_pid(self):
    #   try:
    #       self._pid = self._game.server.send
    #   except:
    #       self._game.console.log()

    def _on_svr_refreshed(self, svr):
        # networked only
        #self._pid = svr.sendreq('pid')
        pass
    # ------------------------------------------------------ #

    @property
    def game(self):
        return self._game

    @property
    def party(self):
        """The character roster for this player."""
        return self._party

    def is_ai(self):
        """True is this player is AI controlled. (Non-Human)."""
        return self._is_ai


class AIPlayer(Player):
    _is_ai = True


