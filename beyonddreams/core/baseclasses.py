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

"""Provides base classes and methods for various Beyond Dreams types."""


def overwrite_dictupdate(d, [e,], **kwargs):
    for i in e:
        try:
            for k in i.keys():
                if k in d:
                    d[k] = d[k]
        except:
            for k, v in i:
                if k in d:
                    d[k] = v
    for k in kwargs:
        if k in self:
            d[k] = kwargs[k]

def pop(x, i):
    yield x[i]
    del x[i]


class BDList(list):
    __slots__ = ()
    def __init__(self, items=[]):
        self = list(items)

    def append(self): raise NotImplementedError
    pop = extend = extend = append
    __imul__ = __iadd__ = append

    def swap_indices(self, x, y):
        if 0 <= x <= y <= len(self):
            tmp = self[y]
            self[x] = self[y]
            self[y] = self[x]

    def move_down_by_index(self, i):
        if idx < len(self):
            self[idx + 1] = self[idx].pop()

    def move_up_by_index(self, i):
        if idx > 0: self[idx - 1] = self[idx].pop()

    def move_down(self, x):
        self._move_down_by_index(self.index(x))

    def move_up(self, x):
        self._move_up_by_index(self.index(x))


class BDTags:
    _sc = ()    # tuple of super classes to this -- shared by all instances
    def __init__(self, tags=()):
        self._tags = set(tags).difference(self._sc_tags())

    def _sc_tags(self):
        """Return tags from this objects super class."""
        for i in self._inctags: yield i         # yield own include tags
        for i in self._sc: yield _sc._sc_tags() # include tags from super classes

    def tags(self):
        for i in self._tags: yield i
        for i in self._sc_tags(): yield i

    def has_tag(self, tag):
        return any(i.startswith(tag) for i in self.tags())


class BDType:
    """Primative level baseclass form most Beyond Dreams types."""
    __slots__ = "_name"
    _desc = ""
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        """The name of this."""
        return self._name

    def desc(self):
        """Return the main description about this."""
        try: return self._desc[self._name]
        except: return ""


class BDTaggedType(BDType, BDTags):
    def __init__(self, name, tags=()):
        BDTags.__init__(tags=tags)
        self._name = name


class BDBaseValueDict(dict):
    """Dictionary for storing (usually static) base values."""
    __slots__ = dict.__slots__
    def __init__(self, **kwargs):
        for k in kwargs:
            if k in self: self[k] = kwargs[k]


from xsquare.utils import NumDict

class BDValueDict(NumDict):
    __slots__ = NumDict.__slots__
