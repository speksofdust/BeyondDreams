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

"""Base classes for 'search' tools."""


class SearchParam:
    _paramtype = ""
    __slots__ = ("_enabled")
    def __init__(self):
        self._enabled = True

    def _get_enabled(self): return self._enabled
    def _set_enabled(self, s): self._enabled = bool(s)
    enabled = property(_get_enabled, _set_enabled)


class ValueSearch(SearchParam):
    _paramtype = "value"
    __slots__ = SearchParam.__slots__ + "_name", "_min", "_max", "_absrange"
    def __init__(self, name, absmin, absmax):
        self._name =    name
        self._enabled = True
        self._min =     absmin
        self._max =     absmax
        self._absrange = (absmin, absmax)

    def _get_min(self): return self._min
    def _set_min(self, x):
        if min < self._absrange[0]: self._min = self._absrange[0]
        else: self._min = min
    min = property(_get_min, _set_min)

    def _get_max(self): return self._max
    def _set_max(self, x):
        if max < self._absrange[1]: self._max = self._absrange[1]
        else: self._max = max
    max = property(_get_max, _set_max)


class TagsParam(SearchParam):
    _paramtype = "tags"
    __slots__ = SearchParam.__slots__ + "_req_all", "_req_any", "_exclude"
    def __init__(self):
        self._enabled = True    # priority
        self._req_all = set()   # 1
        self._req_any = set()   # 3
        self._exclude = set()   # 2

    def _tag_sets(self):
        return iter(self._req_all, self._req_any, self._exclude)

    def _add_tags(self, dest, tags):
        dest.update(tags)
        for i in self._tag_sets():
            if i != dest:
                i.difference_update(tags)


class Search:
    _searchtype = ""
    """Base class for 'search' objects."""
    def __init__(self, items=[]):
        self._items =  items
        self._params = []

