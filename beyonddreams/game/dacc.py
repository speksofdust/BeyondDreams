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

"""Data accessor base classes for gamedata and chardata."""


class GameDataAccessor:
    def __dpath(): raise NotImplementedError
    __slots__ = ()
    def __init__(self): pass
    def __eq__(self, x):        return self.__dpath == (x or x.__dpath())
    def __ne__(self, x):        return self.__dpath != (x or x.__dpath())


class GameDataAccessorSeq(GameDataAccessor):
    """Game data accessor for data stored in a sequence."""
    __slots__ = ()
    def __iter__(self):         return iter(self.__dpath())
    def __len__(self):          return len(self.__dpath())
    def __contains__(self, i):  return i in self.__dpath()
    def __getitem__(self, i):   return self.__dpath[i]
    def index(self, i):         return self.__dpath.index(i)


class GameDataAccessorDict(GameDataAccessorSeq):
    """Game data accessor for data stored in a dict."""
    __slots__ = ()
    def keys(self):     return self.__dpath.keys()
    def values(self):   return self.__dpath.values()
    def index(self):    raise NotImplementedError


# ---- Char Data Accessors --------------------------------------------------- #
class _CA:
    __slots__ = "char"
    def __init__(self, char):
        self.char = char


class CharDataAccessor(GameDataAccessor, _CA):
    __slots__ = _CA.__slots__

    def __eq__(self, c): return self._char == (c or c._char)
    def __ne__(self, c): return self._char != (c or c._char)


class CharDataAccessorDict(GameDataAccessorDict, _CA):
    """Character data accessor for data stored in a dict."""
    __slots__ = _CA.__slots__


class CharDataAccessorSeq(GameDataAccessorSeq, _CA):
    """Char data accessor for data stored as a sequence."""
    __slots__ = _CA.__slots__
