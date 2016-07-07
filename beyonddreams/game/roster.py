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

import gamedata

class _Members:
    __slots__ = '_members'
    def __init__(self, members):
        self._members = members

    def __len__(self): return len(self._members)
    def __iter__(self): return iter(self._members)
    def __getitem__(self, i): return self._members[i]
    def __setitem__(self, i, v): self._members[i] = v
    def __contains__(self, x): return x in self._members


class Roster(_Members):
    _maxmembers = 'inf'
    __slots__ = _Members.__slots__
    def __init__(self, members):
        self._members = members

    def _can_add_member(self, charid):
        return not(self.is_full and charid not in self)

    def is_full(self):
        return len(self._members == self._maxmembers)

    def _add_member(self, charid):
        pass

    def on_member_leave(self, member): pass
    def on_member_join(self, member): pass


class BannedRoster(Roster):
    __slots__ = Roster.__slots__



