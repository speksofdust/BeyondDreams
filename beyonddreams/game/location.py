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


class Regions(dict):
    def __init__(self):
        self = {}

    def visited_regions(self, char):
        return iter(i for i in self if i._region_id in
            char.data["regions.visited."])


class Region(dict):
    def __init__(self, name, region_id):
        self._name = name
        self._region_id = region_id
        self = {}

    @property
    def name(self):
        """The name of this region."""
        return self._name

    def has_visited(self, char):
        """True if given character has visited this region at least once."""
        return self._region_id in char.data["regions.visited"]


class Location:
    def __init__(self, name="", region, sublocations=(), parentloc=None):
        self._name =  name
        self._region = region
        self._parentloc = parentloc
        self._sublocations = sublocations

    # ---- read/write ---- #
    # str to obj
    def _str_to_subloc(self, *s):
        # returns a location object from separated strings
        # can go multiple layers deep (subloc --> subsubloc, etc.)
        if len(s) > 1: return self._get_subloc_from_str(self._sublocations[s[0]])
        return self._sublocations[s[0]]

    # obj to str
    def _fullparentloc(self):
        if self._parentloc is None: return ""
        elif self._parentloc._parentloc is None:
            return self._parentloc._name
        else:
            return "-".join(self._parentloc._fullparentloc(),
                self._parentloc._name)

    def _keyname(self):
        return "-".join(self._region, self._fullparentloc())

    @property
    def _fullkeyname(self):
        """The full key name as a string. Used when writing data to disk."""
        return "".join("loc.", self._keyname())
    # -------------------------------------------------------------------- #

    @property
    def name(self):
        return self._name

    @property
    def sublocations(self):
        return self._sublocations

    def visited_sublocations(self, char):
        """Return an iterator of sublocations of this location (if any) that have
        been visited by the given character at least once."""
        return iter(i for i in self._sublocations if self.times_visited(char) >= 1)

    def unvisited_sublocations(self, char):
        """Return an iterator of sublocations of this location (if any) that have
        never been visited by the given character."""
        return iter(i for i in self._sublocations if self.times_visited(char) == 0)

    def is_sublocation(self):
        """True if this location is located within a parent location."""
        return self._parentloc is not None

    def times_visited(self, char):
        """The number of times a given char has visited this location."""
        try: return char.location[self._keyname].visited
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
                i.location.update_loc_data(self)
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


class CurrentLocation:
    def __init__(self, location):
        self._location = location

    def __str__(self): return self.name

    @property
    def region(self):
        """The Region of the current location."""
        return self._location._region


class _CharLocDataBase:
    def __init__(self, char):
        self._current = CurrentLocation()

    def update_loc_data(self, loc):
        self._current.location = loc._fullkeyname

    def _curloc_to_str(self):
        # string from loc obj -- writing
        return self._current._fullkeyname

    def _curloc_from_str(s):
        # loc obj from string loc -- reading
        n = iter(s[3:].split("-"))

        if len(n) >= 3:
            # region --> location --> subloc --> (subsubloc --> etc. as needed)
            return regions[next(n)][next(n)]._str_to_subloc
        # region --> location
        return regions[next(n)][next(n)]


class CharLocData(dict):
    def __init__(self, char):
        self._char = char
        self._current = CurrentLocation()
        self = {
            "regions.visited":  set()
            }

    def update_loc_data(self, loc):
        try: self[loc.name].update_visit_data
        except:
            self[loc.name] = LocationData(1)
        self["regions.visited"].add(self._region._region_id


class NPCCharLocData(_CharLocDataBase):
    pass

