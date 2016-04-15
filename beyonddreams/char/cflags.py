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

from charflags import *


class CFlags:
    _FLAGS = None
    __slots__ = ("_items")
    def __init__(self, items={}):
        self._items = set(items)

    def __iter__(self): return iter(self._items)
    def __len__(self): return len(self._items)
    def __str__(self): return str(self._items)
    __repr__ = __str__

    def __eq__(self, x):
        if isinstance(CharFlags): return x._items == self._items
        try: return self._items == x
        except: raise TypeError("incompatible types for comparison.")

    def __ne__(self, x):
        if isinstance(CharFlags): return x._items != self._items
        try: return self._items != x
        except: raise TypeError("incompatible types for comparison.")

    def __contains__(self, x):
        if isinstance(x, int): return x in self._items
        else: return self._FLAGS[x] in self._items

    def copy(self):
        import copy
        return copy.copy(self)

    def clear(self): self._items.clear()
    def remove(self, i): self._items.remove(cf_to_num(x, self._FLAGS))
    def discard(self, x): self._items.discard(cf_to_num(x, self._FLAGS))

    @property
    def FLAGS(self):
        return self._FLAGS


class CharFlags(CFlags):
    _FLAGS = CHARFLAGS
    __slots__ = _CFlags.__slots__

    def get_factor(self):
        return any(i for i in self._items if i in FACTORS)

    def set_factor(self, f):
        if f in FACTORS:
            x = 0
            for i in self:
                if i in FACTORS:
                    x = self._items.pop()
                break
            if (f == x):
                if (x == FT_2X): self._items.add(FT_4X)
                else: self._items.add(x)
            elif (f == FT_NULL): self._items.add(FT_NULL)
            elif x == 0: self._items.add(f)
            elif f == FT_HALF: # reduce by half
                if x == FT_FULL: self._items.add(FT_HALF)
                elif x == FT_2X: self._items.add(FT_NONE)
                elif x == FT_4X: self._items.add(FT_2X)
                else: self._items.add(f)
            else:
                pass


    def add(self, i):
        if (i not in self._items and i > self._FLAGS.MAX_SPECIAL):
            if i in FACTORS: self.set_factor(i)
            else: self._items.add(i)


class DFlags(CFlags):
    _FLAGS = DFLAGS
    __slots__ = _CFlags.__slots__

    def has_nonrevivable(self):
        return any(i > self._FLAGS.MAX_REVIVABLE for i in self)


DFLAGS_NAMES = {
    SUFFOCATED: 'suffocated',
    DROWNED:    'drowned',

    # last hit
    STABBED:    'stabbed',
    BEATEN:     'beaten',
    ELECTROCUTED:     'electrocuted',
    BURNED:           'burned',
    FROZE:            'froze',
    FROZEN:           'frozen',

    # status(s) maxed
    BLED:             'bled', # bleed level maxed
    POISIONED:          'poisioned', # poisoning level maxed
    DRANK:            'drank', # drunk & poisioning levels maxed

    # misc
    REVIVED_WHILE_ZOMBIE: 'revived while zombified',

    # barely revivable
    GUTTED:           'gutted',
    HALVED:           'split in half',

    # non-revivable dflags
    BEHEADED:         'beheaded',
    EXPLODED:         'exploded',
    VAPORIZED:        'vaporized',
    FLATTENED:        'flattened',
    }

def get_on_died_msg(pfx, flag, names=DFLAG_NAMES):
    if names[flag] in (FROZE, DRANK): return '{} {} to death'.format(pfx, flag)
    elif (names[flag].endswith('ed') or names[flag] == FROZEN):
        return '{} was {} to death'.format(pfx, flag)
    elif names[flag] in (REVIVED_WHILE_ZOMBIE, HALVED):
        return '{} was {}'.format(pfx, flag)
    else:
        pass

def calc_factor(flags, value, fullvalue=100, cf=CHARFLAGS):
    # TODO move this
    if cf['no-multiplier'] in flags: return value
    elif cf['null'] in flags: return 0
    elif cf['half'] in flags: return value / 2
    elif cf['2x'] in flags: return value * 2
    elif cf['4x'] in flags: return value * 4
    elif cf['full'] in flags: return fullvalue
    else: return value
