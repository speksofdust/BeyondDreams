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



class StatsAbsRange(dict):
    def __init__(self, items):
        super().__init__(items)

    def get_clamped(self, name, val):
        if self[name][0] <= val: return self[name][0]
        elif self[name][1] >= val: return self[name][1]
        else: return val


# Absolute minimum and maximum for stats
STATS_ABS_RANGE = StatsAbsRange(
    {
    # ---- Stats -------------------------------------------------------- #
    # Levels change with equip, skill, etc. changes.
    'phys-stamina':     (0, 200),
    'mental-stamina':   (0, 200),
    'intellect':        (1, 200),
    'focus':            (0, 200),
    'strength':         (1, 200),
    'willpower':        (0, 200),
    'agility':          (1, 100),
    'luck':             (-1000, 1000),

    'phys-energy':      (0, 200),
    'mental-energy':    (0, 200),
    'health':           (0, 200),

    # hidden stats
    'karma':            (-1000, 1000),
    'adrenaline':       (0, 100),
    'rage':             (-100, 100),

    # ---- Statuses ----------------------------------------------------- #
    "frozen":           (0, 1),     # bool
    "frostbite" :       (0, 100),
    "burn" :            (0, 100),
    "numb" :            (0, 100),
    "stun" :            (0, 100),
    "poisoning" :       (0, 100),
    "bleed" :           (0, 100),
    'poisioning':       (0, 100),

    # mental
    "blind" :           (0, 100),
    "drunk" :           (0, 200),
    "dumb" :            (0, 200),
    "confusion" :       (0, 100),

    # transform
    "zombie" :          (0, 100),
    "mutagen" :         (0, 100),

    # specials
    "immunnull":        (0, 1),     # bool
    "immundown":        (0, 200),
    })


# rage - > 0 increases strength but uses more phys-energy < 0 does the opposite



# Real value calculations
def calc_energy(c, energy_type):
    # any type
    # (total base)energy + (adrenaline * 0.02) + (rage * 0.02)
    return  (c[stats][energy_type] + (c[stats]['adrenaline'] * 0.02) +
        (c[stats]['rage'] * 0.02))

def calc_focus(c):
    # (total base)focus * (mental-energy + (adrenaline * 0.02) + (rage * 0.02))
    return stats_abs_range.clamped('focus',
        c[stats]['focus'] * calc_energy(c, 'mental-energy'))

def calc_strength(c):
    # (total base)strength * (phys-energy + (adrenaline * 0.02) + (rage * 0.02))
    return stats_abs_range.clamped('strength',
        c[stats]["strength"] * calc_energy(c, "phys-energy"))


class Stauses(gacc.CharDataAccessorDict):
    __slots__ = gacc.CharDataAccessorDict.__slots__
    #priorities:
    #   Status 'immunnull' (nullifies effect of all immunites)
    #   Status 'immundown' (all immune stats become 100 - immunodown level
    #   Char Equip
    #   Primary & Secondary Fam Immunities
    #   Primary Fam stat + Secondary Fam stat(s)

    def set_status(self, name, v):
        if name in BOOLSTATUSES: self.char['statuses'][name] = bool(v)
        else: self.char['statuses'][name] = int(v)

    def get_status(self, name):
        return self.char['statuses'][name]

    def _set_status(self, s, v):
        if s not in self.immunities():
            self.char['statuses'][s] = v # TODO clamping

    def _ss_bool(self, s, v):
        if s not in self.immunities(): self['stats'][s] = bool(v)

    def has_immunity_nullifiers(self):
        """True if this char has 'immunnull' status or 'immundown' level is greater than 0"""
        return (self.char['statuses']['immunnull'] or
            self.char['statuses']['immundown'] >= 1)

    def immunities(self):
        """Return an iterator of all immunities."""
        if self.has_immunity_nullifiers(): return iter(())
        return iter(())




