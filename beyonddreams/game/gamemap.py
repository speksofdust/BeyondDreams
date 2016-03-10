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

from .core.baseclasses import BDList


class Compass:
    def __init__(self):
        self._scale = 1


class MapObject(dict):
    _mapobject_type = ""
    __slots__ = dict.__slots__ + ("_parent")
    def __init__(self, parent, pos):
        self._parent = parent
        super().__init__({
            'pos': pos,
            })

    @property
    def _map(self):
        return self._parent._parent

    @property
    def pos(self):
        """The position of this object on the map."""
        return self._pos


class MapMarker(MapObject):
    _mapobject_type = "marker"
    __slots__ = MapObject.__slots__
    def __init__(self, parent, pos, name, color, symbol, notes=[]):
        super().__init__({
            'pos':      pos,
            'name':     name,
            'color':    color,
            'symbol':   symbol,
            'notes':    notes,
            'locked':   False,
            })

    def __del__(self):
        self['color'] = None
        self['symbol'] = None
        self['locked'] = None

    def _get_locked(self): return self['locked']
    def _set_locked(self): self['locked'] = bool(self['locked'])
    locked = property(_get_locked, _set_locked,
        doc="If True this map marker cannot be altered or removed.")

    def _get_color(self): return self['color']
    def _set_color(self, x): self['color'] = x
    color = property(_get_color, _set_color, doc="The color of this map marker.")

    @property
    def name(self):
        """The name of this map marker."""
        return self['name']

    @property
    def notes(self):
        """Access notes for this map marker."""
        return self['notes']

    def delete(self):
        """Delete this map marker from the map."""
        self._parent.delete_marker(self)


class MapMarkers(BDList):
    """Storage class for map markers."""
    _markercls = None
    __slots__ = BDList.__slots__ + "parent"
    def __init__(self, parent):
        self._parent = parent
        super().__init__([])

    __setitem__ = __delitem__ = remove, discard, clear = append

    @property
    def map(self):
        return self._parent

    def add_marker(self, pos, name, notes=()):
        """Add a new marker to the map."""
        self._markercls(self, pos, name, notes)

    def delete_marker(self, x):
        """Delete a marker from the map."""
        if not self[x]._locked: del self[x]


class _MapBase:
    _maptype = ""
    def __init__(self):
        self._zoom = 0
        self._markers = MapMarkers(self)

    @property
    def markers(self):
        """Access map markers."""
        return self._markers


class LocalMap(_MapBase):
    """Game 'Map' object for non-interactive maps."""
    _maptype = ""


class InteractiveMap:
    _maptype = ""
