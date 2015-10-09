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


__all__ = ()

class BestiaryBase(dict):
    _sort_attrs = 'id', 'name'
    __slots__ = dict.__slots__

    def __getitem__(self, i):
        try: return self[i]
        except:
            for k in self: # access by id
                if self[k].id == i: return self[k]

    def _sorted_by(self, r=False, k):
        return sorted(self.values(), key=attrgetter(k), reverse=r)

    def sortby(self, reverse=False):
        return self._sorted_by(self.values(), reverse=reverse)
        def id(self, reverse=False): return self._sorted_by(reverse, 'id')


all_entries = BestiaryBase() # The full bestiary


class BestiaryEntry:
    __slots__ = "_name", "_fam", "_id"
    def __init__(self, name, entry_id, fam[]):
        self._name = name
        self._id =  entry_id
        self._fam = fam
        all_entries[self._name] = self  # add to entries

    def __str__(self): return ", ".join(self.name, self.id, self.fam)

    @property
    def name(self):
        """The entry name."""
        return self._name

    @property
    def id(self):
        """The entry id."""
        return self._id

    @property
    def fam(self):
        """Family types data."""
        return self._fam


class PlayerBestiaryEntry:
    __slots__ = "_parent", "_entry", "_encountered", "_killed"
    def __init__(self, parent, entry):
        self._parent = parent
        self._entry = entry
        self._encountered = 0
        self._killed = 0

    def __str__(self):
        return ", ".join(self.id, self.encountered, self.killed)

    def _wrfmt(self): # write formatting
        return "{}:{},{}".format(self.id, self.encountered, self.killed)

    # ---- Some stuff to make compatible with BestiaryEntry ---- #
    @property
    def id(self):
        """The entry id."""
        return self._entry.id

    @property
    def name(self):
        """The entry name."""
        return self._entry.name
    # ----------------------------------------------------------- #

    @property
    def entry:
        return self._entry

    @property
    def encountered(self):
        """The total number encountered."""
        return self._encountered

    @property
    def killed(self):
        """The total number killed."""
        return self._killed


class PlayerBestiary(BestiaryBase):
    __slots__ = BestiaryBase.__slots__



    def _get_entry(self, x):
        try: return self[x]
        except: self[x] = PlayerBestiaryEntry(self, x)

    def add_encounter(self, entryname):
        self._get_entry[entryname]._encountered += 1

    def add_kill(self, entryname):
        self._get_entry[entryname]._killed += 1

    def get_total(self, k):
        n = 0
        for i in self:
            n += getattr(i, k)
        return n

    def _fmtstat(x, y, a, b=""):
        if funcb: return "{x} {y}:{spc}{a}, {b}".format(x, y,
            spc=(24-(len(x)+len(y)+1)), a, b)
        return "{x} {y}:{spc}{a}".format(x, y,
            spc=(24-(len(x)+len(y)+1)), a)

    def get_statistics(self):
         for i in (
            ("Total", "Entries", len(self)),
            ("Total", "Encountered", self.get_total("encountered")),
            ("Most", "Encountered", "", ""),
            ("Least", "Encountered", "", ""),
            ("Total", "Killed", get_total("killed")),
            ("Most", "Killed", "", ""),
            ("least", "killed" "", ""),
            ):
                yield self._fmstat(*i)


