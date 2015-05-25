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

all_entries = _BestiaryBase()

__all__ = ()

class BestiaryBase(dict):
    __slots__ = ()

    def __getitem__(self, i):
        try: return self[i]
        except:
            for k in self:
                if self[k]._id == i: return self[k]

    def sorted_by_ids(self, reverse=False):
        return sorted(self, key=attrgetter("_id"), reverse=reverse)


class BestiaryEntry:
    __slots__ = "_name", "_fam", "_id"
    def __init__(self, name, entry_id, fam[]):
        self._name = name
        self._id =  entry_id
        self._fam = fam
        all_entries[self._name] = self  # add to entries

    @property
    def id(self):
        return self._id

class PlayerHist:
    __slots__ = "_encountered", "_killed"
    def __init__(self):
        self._encountered = 0
        self._killed = 0

    @property
    def encountered(self):
        return self._encountered

    @property
    def killed(self):
        return self._encountered


class Bestiary(BestiaryBase):
    __slots__ = ()


    def _get_entry(self, name):
        try: return self[entryname]
        except:
            self[entryname] = (PlayerHist(), all_entries[entryname])
            return self[entryname]

    def add_encounter(self, entryname):
        self._get_entry[entryname][0]._encountered += 1

    def add_kill(self, entryname):
        self._get_entry[entryname][0]._killed += 1

    def get_total(self, k):
        n = 0
        for i in self:
            n += getattr(i, k)

    def _fmtstat(self, x, y, a, b=""):
        if funcb: return "{x} {y}:{spc}{a}, {b}".format(x, y,
            spc=(24-(len(x)+len(y)+1)), a, b)
        return "{x} {y}:{spc}{a}".format(x, y,
            spc=(24-(len(x)+len(y)+1)), a)

    def get_statistics(self):
        # TODO need a better way to handle this
        yield self._fmtstat("Total", "Entries", len(self))
        yield self._fmtstat("Total", "Encountered", self.get_total("encountered"))
        yield self._fmtstat("Total", "Entries", "")
        yield self._fmtstat("Total", "Encountered", self.get_total("encountered"))
        yield self._fmtstat("Most", "Encountered", "", "")
        yield self._fmtstat("Least", "Encountered", "", "")
        yield self._fmtstat("Total", "Killed", get_total("killed"))
        yield self._fmtstat("Most", "Killed", "", "")
        yield self._fmtstat("least", "killed" "", "")

