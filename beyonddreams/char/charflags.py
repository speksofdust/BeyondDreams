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

def calc_factor(flags, value, fullvalue=100, cf=CHARFLAGS):
    # TODO move this
    if cf['no-multiplier'] in flags: return value
    elif cf['null'] in flags: return 0
    elif cf['half'] in flags: return value / 2
    elif cf['2x'] in flags: return value * 2
    elif cf['4x'] in flags: return value * 4
    elif cf['full'] in flags: return fullvalue
    else return value


CHARFLAGS = {
    "RESERVED":         0,  # reserved
    # Temp Flags
    "in-savepoint":     49,
    "has-encounter":    50, # currently attacked or in battle, etc.


    # factor
    "no-multiplier":    150
    "null":             151,
    "half":             152,
    "2x":               153,
    "4x":               154,
    "full":             155,

    # cast flags
    "aura":             1000,
    "fire":             1100,
    "ice":              1101,
    "wind":             1102,
    "elec":             1103,
    "light":            1108,
    "dark":             1109,
    "mag":              1111,
}
CHARFLAGS.MAX_SPECIAL = 50
CHARFLAGS.MIN_FACTOR = 150
CHARFLAGS.MAX_FACTOR = 155

def is_factor(n, c=CHARFLAGS): return n in range(c.MINFACTOR, c.MAXFACTOR)

def cf_to_num(x, flags):
    if isinstance(x, int): return x
    return flags[x]


DFLAGS = {
    "RESERVED":         0,
    "suffocated":       111,
    "drowned":          112,

    # last hit
    "stabbed":          113,
    "beaten":           114,
    "electrocuted":     115,
    "burned":           116,
    "frozen":           117,

    # status(s) maxed
    "bled":             120, # bleed level maxed
    "poisoned":         121, # poisoning level maxed
    "drunk":            122, # drunk & poisioning levels maxed

    # misc
    "revived-as-zombie": 170,

    # barely revivable
    "gutted":           198,
    "halved":           199, # split in half

    # non-revivable dflags
    "beheaded":         200,
    "exploded":         201,
    "vaporized":        202,
    "flattened":        203,
    }
DFLAGS.MAX_REVIVABLE = 199


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
        else:
            try: return self._items = x
            except: raise TypeError("incompatible types for comparison.")

    def __ne__(self, x):
        if isinstance(CharFlags): return x._items != self._items
        else:
            try: return self._items = x
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
        return any(i for i in self._items if is_factor(i, self._FLAGS))

    def set_factor(self, f): self._set_factor(cf_to_num(f, self._FLAGS))

    def _set_factor(self, n):
        for i in self:
            if is_factor(i):
                self._items.remove(i)
                break
        self._items.add(n)

    def add(self, i): self._add(cf_to_num(i, self._FLAGS))

    def _add(self, n):
        if (i not in self._items and i > self._FLAGS.MAX_SPECIAL):
            if is_factor(i): self._set_factor(i)
            else: self._items.add(i)


class DFlags(CFlags):
    _FLAGS = DFLAGS
    __slots__ = _CFlags.__slots__

    def has_nonrevivable(self):
        return any(i > self._FLAGS.MAX_REVIVABLE for i in self)

