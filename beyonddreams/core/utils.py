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


def tuplized(*items):
    """Converts items to a tuple."""
    return items


def getversion(v):
    x = _GetVersion(v)
    return x.version


class _GetVersion:
    def __init__(self, v):
        self._v = v
        def _a(): return self._v.split(".")[0]
        def _b(): return self._v.split(".")[1]
        def _c(): return self._v.split(".")[2]
        version.major = _a
        version.minor = _b
        version.revision = _c

    def version(self):
        """Return the version number."""
        return self._v
