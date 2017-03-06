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

from loctypes import Maptype


# ---------------------------------------------------------------------------- #
#     Map Type Base Classes                                                    #
# ---------------------------------------------------------------------------- #
class MapType(LocationType):
    __slots__ = LocationType.__slots__

class SubMapType(MapType):
    __slots__ = MapType.__slots__


class _UrbanMapType(MapType): # populated areas (towns, castles, etc)
    __slots__ = MapType.__slots__

class _RuralMapType(MapType): # unpopulated areas
    __slots__ = MapType.__slots__

# ---------------------------------------------------------------------------- #
#    Map Types                                                                 #
# ---------------------------------------------------------------------------- #
class Town(_UrbanMapType):
    typename = "town"
    _icon = ()
    __slots__ = _UrbanMapType.__slots__


class Castle(_UrbanMapType):
    typename = "castle"
    _icon = ()
    __slots__ = _UrbanMapType.__slots__


class Temple(MapType):
    typename = "temple"
    _icon = ()
    __slots__ = MapType.__slots__


class Dungeon(MapType):
    typename = "dungeon"
    _icon = ()
    __slots__ = MapType.__slots__


class Cave(MapType):
    typename = "cave"
    _icon = ()
    __slots__ = MapType.__slots__


class Sewer(MapType):
    typename = "sewer"
    _icon = ()
    __slots__ = MapType.__slots__
