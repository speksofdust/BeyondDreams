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

from .game import gacc

class CharName(gacc.CharDataAccessor):
    __slots__ = gacc.CharDataAccessor.__slots__

    def __str__(self): return str(self.__repr__[1:-1])
    def __repr__(self): return str((self.first, self.last, self.middle, self.nick))

    def _sn(self, n, v):
        if self.char._name_is_ediatble: self.char["".join('name-', v)] = n

    def _get_first(self): return self.char['name-first']
    def _set_first(self, n): self._sn(n, 'first')
    first = property(_get_first, _set_first)

    def _get_middle(self): return self.char['name-middle']
    def _set_middle(self, n): self._sn(n, 'middle')
    middle = property(_get_middle, _set_middle)

    def _get_last(self): return self.char['name-last']
    def _set_last(self, n): self._sn(n, 'last')
    last = property(_get_last, _set_last)

    def _get_nick(self): return self.char['name-nick']
    def _set_nick(self, n): self._sn(n, 'nick')
    nick = property(_get_nick, _set_nick)

    @property
    def full(self):
        """The first and last name."""
        return self.char[0], self.char[2]

    @property
    def middle_initial(self):
        """The first letter of the middle name."""
        return self.char[1][0]

    @property
    def initials(self):
        """The first letters of the first and last name."""
        return self.char[0][0], self.char[2][0]


class Inventory(gacc.CharDataAccessor):
    __slots__ = gacc.CharDataAccessor.__slots__


class Stauses(gacc.CharDataAccessorDict):
    __slots__ = gacc.CharDataAccessorDict.__slots__
    #priorities:
    #   Status 'immunnull' (nullifies effect of all immunites)
    #   Status 'immundown' (all immune stats become 100 - immunodown level
    #   Char Equip
    #   Primary & Secondary Fam Immunities
    #   Primary Fam stat + Secondary Fam stat(s)


    def _gs(self, s): # uncalculated
        return self.char['statuses'][s]

    def _set_status(self, s, v):
        if s not in self.immunities():
            self.char['statuses'][s] = v # TODO clamping

    def _gs_bool(self, s, v): # uncalculated
        return self.char['statuses'][s]

    def _ss_bool(self, s, v):
        if s not in self.immunities(): self['stats'][s] = bool(v)

    def has_immunity_nullifiers(self):
        return (self.char['statuses']['immunnull'] or
            self.char['statuses']['immundown'] >= 1)

    def immunities(self):
        """Return an iterator of all immunities."""
        if self.has_immunity_nullifiers(): return iter(())
        return iter(())

    # ---- bool type ----------------------------------------------------- #
    def _get_frozen(self):    return self._gs_bool(self, "frozen")
    def _set_frozen(self, x): self._ss_bool(self, "frozen")
    frozen = property(_get_frozen, _set_frozen)

    def _get_immunnull(self):    return self._gs_bool(self, "immunnull")
    def _set_immunnull(self, x): self._ss_bool(self, "immunnull")
    immunnull = property(_get_immunnull, _set_immunnull)


    # ---- level type ---------------------------------------------------- #
    def _get_frostbite(char): return self._gs(self, "frostbite")
    def _set_frostbite(char, x): self._ss(self, "frostbite")
    frostbite = property(_get_frostbite, _set_frostbite)

    def _get_burn(char): return self._gs(self, "burn")
    def _set_burn(char, x): self._ss(self, "burn")
    burn = property(_get_burn, _set_burn)

    def _get_drunk(char): return self._gs(self, "drunk")
    def _set_drunk(char, x): self._ss(self, "drunk")
    drunk = property(_get_drunk, _set_drunk)

    def _get_poisoned(char): return self._gs(self, "poisoned")
    def _set_poisoned(char, x): self._ss(self, "poisoned")
    poisoned = property(_get_poisoned, _set_poisoned)
