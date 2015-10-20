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

"""Top level gamedata accessors."""

from data import gamedata
import dacc


class _Visited(da.GameDataAccessorDict):
    def __dpath(): return gamedata['visited']
    __slots__ = ()


class GDVisitedAccessor(_Visited):
    __slots__ = ()


class EMVisitedAccessor(_Visited):
    __slots__ = ()


class AllCharsAccessor(da.GameDataAccessorDict):
    def __dpath(): return gamedata['chars']
    __slots__ = ()

    def party_chars(self):
        """Return an iterator of all party character data in current party
        order."""
        return iter(gamedata['chars'][i] for i in gamedata['party']


class PartyAccessor(da.GameDataAccessorSeq):
    MAX_CHARS = 8
    def __dpath(): return gamedata['chars']
    __slots__ = ()

    def _get_active(self): return gamedata['party'][0]
    def _set_active(self, i):
        if i <= -1:         gamedata['party'][0] = len(self)
        elif i > len(self): gamedata['party'][0] = 0
        else:               gamedata['party'][0] = i
    active = (_get_active, _set_active,
        doc="The currently active character for this party.")

    def activate_next(self, available=True):
        if available:
            for i in self.get_alive():
                if i != self: gamedata['party'][0] = self.index(i)
        else: self.active = self.index(self[self.active -1])

    def activate_prev(self, available=True):
        if available:
            for i in reversed(self.get_alive()):
                if i != self: gamedata['party'][0] = self.index(i)
        else: self.active = self.index(self[self.active -1])

    def get_alive(self):
        """Return an iterator of all currently alive party members."""
        return i for i in self

