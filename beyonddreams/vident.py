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


class _DummyVIdent(int):
    """Visitor identity. Stores constant identiefier values for certain objects
    which allow location visitation."""
    name = "dummy"
    def __init__(self, d):
        self = d

    def __str__(self):      return self.name
    __repr__ = __str__


class _PlayerVIdent(_VIdent):
    _name = "player"

class _CharVIdent(_VIdent):
    _name = "char"

class _PartyVIdent(_VIdent):
    _name = "party"


DUMMY_VIDENT =  _DummyVIdent()
PLAYER_VIDENT = _PlayerVIdent()
CHAR_VIDENT =   _CharVIdent()
PARTY_VIDENT =  _PartyVIdent()
VIDENT_TYPES = (DUMMY_VIDENT, PLAYER_VIDENT, CHAR_VIDENT, PARTY_VIDENT)

def vident_from_index(i):
    global vident_types
    return vident_types[i]


__all__ = ("vident_from_index", "VIDENT_TYPES", "DUMMY_VIDENT", "PLAYER_VIDENT",
    "CHAR_VIDENT", "PARTY_VIDENT"
