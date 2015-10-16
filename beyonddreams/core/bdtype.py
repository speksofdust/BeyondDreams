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

from baseclasses import BDTags


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


class BDTypeDict(dict):
    """Dictionary for storing BDType objects."""
    __slots__ = dict.__slots__
    def __init__(self, *args, **kwargs):
        pass
