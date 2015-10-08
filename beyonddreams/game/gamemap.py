from .core.baseclasses import BDList


class Compass:
    def __init__(self):
        self._scale = 1


class MapObject:
    _mapobject_type = ""
    __slots__ = "_parent", "_pos"
    def __init__(self, parent, pos):
        self._parent = parent
        self._pos = pos

    @property
    def _map(self):
        return self._parent._parent

    @property
    def pos(self):
        """The position of this object on the map."""
        return self._pos


class MapMarker(MapObject):
    _mapobject_type = "marker"
    __slots__ = MapObject.__slots__ + ("_name", "_color", "_symbol", "_notes", "_locked")
    def __init__(self, parent, pos, name, color, symbol, notes=[]):
        self._parent = parent
        self._pos = pos
        self._name = name
        self._color = color
        self._symbol = symbol
        self._notes = notes
        self._locked = False

    def __del__(self):
        self._color = None
        self._symbol = None
        self._locked = None

    def _get_locked(self): return self._locked
    def _set_locked(self): self._locked = bool(self._locked)
    locked = property(_get_locked, _set_locked,
        doc="If True this map marker cannot be altered or removed.")

    @property
    def name(self):
        """The name of this map marker."""
        return self._name

    @property
    def notes(self):
        """Access notes for this map marker."""
        return self._notes

    def delete(self):
        """Delete this map marker from the map."""
        self._parent.delete_marker(self)


class _MapMarkersBase(BDList):
    _markercls = None
    __slots__ = "parent"
    def __init__(self, parent):
        self._parent = parent
        self = []

    __setitem__ = __delitem__ = remove, discard, clear = append

    def add_marker(self, pos, name, notes=()):
        self._markercls(self, pos, name, notes)

    def delete_marker(self, x):
        if not self[x]._locked: del self[x]


class _MapBase:
    _maptype = ""
    def __init__(self):
        self._zoom = 0
        self._markers = MapMarkers()

    @property
    def markers(self):
        """Access map markers."""
        return self._markers


class LocalMap(_MapBase):
    """Game 'Map' object for non-interactive maps."""
    _maptype = ""


class InteractiveMap:
    _maptype = ""
