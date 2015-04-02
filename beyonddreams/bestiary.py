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

def get_entry(entryname):
    return


class BestiaryEntry:
    def __init__(self, name, fam[]):
        self._name = name
        self._fam = fam


class PlayerHist:
    def __init__(self):
        self._encountered = 0
        self._killed = 0

    @property
    def encountered(self):
        return self._encountered

    @property
    def killed(self):
        return self._encountered


class Bestiary:
    def __init__(self):
        self._items = {}

    def _get_entry(self, entryname):
        try: return self._items[entryname]
        except:
            self._items[entryname] = (PlayerHist(), get_entry(entryname))
            return self._items[entryname]

    def add_encounter(self, entryname):
        self._get_entry[entryname][0]._encountered += 1

    def add_kill(self, entryname):
        self._get_entry[entryname][0]._killed += 1

    def get_total(self, k):
        n = 0
        for i in self._items:
            n += getattr(i, k)

    def get_statistics(self):
        yield "Total Entries: {}".format(len(self._items))
        yield "Total Encountered: {}".format(self.get_total("encountered"))
        yield "Most Encountered: {}".format()
        yield "Least Encountered: {}".format()
        yield "Total Killed: {}".format(get_total("killed"))
        yield "Most Killed: {}".format()
        yield "least killed: {}".format()

