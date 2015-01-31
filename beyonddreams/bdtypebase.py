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
    pass


class BDTypeDefSet(typedef.TypeDefSet):
    """Beyond Dreams Type Definition Set class. Base class for all Beyond Dreams
    type definiton container classes.
    """
    pass


class BDType:
    """Base class for Beyond Dreams types."""
    _typetags = ()
    _typedesc = ""
    def __init__(self, tags=()):
        self._tags = tags

    @property
    def typedesc(self):
        """A brief description about this type."""
        return self._typedesc

    @property
    def typename(self):
        """The name of this type as a string"""
        return self.__class__.__name__

    def typetags(self):
        """Return an iterator of all typetags."""
        return iter(self._typetags)

    def tags(self):
        yield self.typename
        for i in chain.from_iterable(self._typetags): yield i
        for i in chain.from_iterable(self._tags): yield i


