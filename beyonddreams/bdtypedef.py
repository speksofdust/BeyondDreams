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

from xsquare import typedef

# Some overides so we can tell were using BD specific instances and
# so we can do future tweaks if needed
class BDTypeDef(typedef.TypeDef):
    """Beyond Dreams Type Definition class. Base class for all BeyondDreams
    type definitions.
    """
    def __init__(self, name, cls=None):
        self._name = name
        self._cls = cls

    def typetags(self):
        """Tags to describe this type. (non-exclusive)"""
        return self._typetags


class BDTypeDefSet(typedef.TypeDefSet):
    """Beyond Dreams Type Definition Set class. Base class for all Beyond Dreams
    type definiton container classes.
    """

    def _cont_as_iter(self, n):
        return iter(self._items[i] for i in n)


def _defaultchk(instance, variable, variablename):
    # return default value if n is None
    if variable is None: return getattr(instance._typebase, variablename)
    return variable


class BDTypesDict:
    def __init__(self):
        self._items = {}

    def __iter__(self):         return iter(self._items)
    def __len__(self):          return len(self._items)
    def __getitem__(self, i):   return self._items[i]
    def __contains__(self, i):  return i in self._items
