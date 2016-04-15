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


class _DummyVIdent:
    """Visitor identity. Stores constant identifier values for certain objects
    which allow location visitation. Used for object type identification in
    some cases as well."""
    name = "dummy"
    index = 0

    def __str__(self):      return self.name
    __repr__ = __str__

    def __iseq__(self, x):
        if isinstance(x, _DummyVIdent): return x._name == self._name
        raise TypeError('Incompatible types for comparison.')

    def __isne__(self, x):
        if isinstance(x, _DummyVIdent): return x._name != self._name
        raise TypeError('Incompatible types for comparison.')


class _PlayerVIdent(_DummyVIdent):
    name = "player"
    index = 1

class _CharVIdent(_DummyVIdent):
    name = "char"
    index = 2

class _PartyVIdent(_DummyVIdent):
    name = "party"
    index = 3


VIDENT_TYPES = {"dummy":    _DummyVIdent(),
                "player":   _PlayerVIdent(),
                "char":     _CharVIdent(),
                "party":    _PartyVIdent()
                }

def vident_from_index(index):
    global VIDENT_TYPES
    for i in VIDENT_TYPES:
        if i.index == index: return i

def vident_name(actor):
    """Returns a 'name' ('player', 'char', 'party', etc) from given actor."""
    return actor._ident.name


__all__ = "vident_from_index", "vident_name", "VIDENT_TYPES"
