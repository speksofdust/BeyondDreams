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


class Location:
    def __init__(self, name="", sublocations):
        self._name =  name
        self._sublocations = ()

    @property
    def _locdata(self):
        return ".".join("locdata", self._name) 

    def times_visited(self, char):
        """The number of times a given char has visited this location."""
        try: return char.data[self._locdata].visited
        except: return 0    # never visited


    # ---- Location Events ---- #
    def _on_visit(self, visitor):
        if visitor.ident = "party":
            self._on_first_visit(iter(i for i in visitors if self.times_visited == 1))
            self._on_visit(visitors)
        elif visitor.ident = "char":
            self._on_first_visit(visitor)
        elif visitor.ident = "player":
            self.on_visit(visitor.party)
        else:
            raise TypeError("invalid visitor type")

    def _on_first_visit(self, *chars):
        if chars:
            for i in chars:
                try:    c.data[_locdata]update_visit_data
                except: c.data[_locdata] = LocationData(1)
            self.on_first_visit(chars)

    def on_first_visit(self, *chars):
        return

    def on_visit(self, chars):
        return
    

class LocationData:
    def __init__(self, times_visited=0, timeout=0):
        self._timeout = timeout
        if times_visited < 0: self._visited = 0
        else: self._visited = int(times_visited)

    def update_visit_data(self):
        if self._timeout <= 0: self._visited += 1
