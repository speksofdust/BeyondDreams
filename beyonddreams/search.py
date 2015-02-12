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
    """Base class for search params.
      Note all param class names must end in 'Param'
    """
    _enabled = True
    def __init__(self, value):
        self._value = value

    @property
    def name(self):
        return self.__class__.__name__.lower()[:-5]

    def _get_enabled(self): return self._enabled
    def _set_enabled(self, s): self._enabled = bool(s)
    enabled = property(_get_enabled, _set_enabled)
    
    
class NumParam(SearchParam):
    """Search parameter for numeric values."""
    ABSMIN = 1
    ABSMAX = 99
    def __init__(self, min):
        if min < self.ABSMIN: self._min = self.ABSMIN
        else: self._min = min
        if max > self.ABSMAX: self._max = self.ABSMAX
        else: self._max = max

    def _get_min(self): return self._min
    def _set_min(self, x):
        if min < self.ABSMIN: self._min = self.ABSMIN
        else: self._min = min
    min = property(_get_min, _set_min)

    def _get_max(self): return self._max
    def _set_max(self, x):
        if max < self.ABSMAX: self._max = self.ABSMAX
        else: self._max = max
    max = property(_get_max, _set_max)


class TagsParam(SearchParam):
    """Search parameter for tags."""
    SEARCH_MODES = "include", "exclude"
    def __init__(self, tags, search_mode="include"):
        try:
            self._search_mode = self._search_mode.index(search_mode)
        except: raise ValueError("Invalid search mode: '{}'.".format(search_mode))
        
        
class Search:
    _searchtype = ""
    """Base class for 'search' objects."""
    def __init__(self, items=[]):
        self._items =  items
        self._params = []

