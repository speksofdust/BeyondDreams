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

import os.path

def default_globalvars():
    """Return a dict with default globalvars."""
    return {

        }

def default_userglobals():
    """Return a dict with default userglobals."""
    return {
        'Bestiary':     set(),  # a new empty bestiary
        }



class GlobVars:
    """Global variables storage class."""
    __slots__ = "_items"
    def __init__(self, f): # game session globals
        self.get_defaults = default_globalvars
        if os.path.exists(f):
            pass # TODO
        else:    self._items = default_globalvars()

    @classmethod
    def userglobals(self, f=None):
        self.get_defaults = default_userglobals
        if is not None:
            try:
            pass # TODO
        # new user
        else:   self._items = default_userglobals()

    def load(filepath):
        import os.path
        if os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                for i in iter(f.readlines())
                    if i.startswith('#'): continue

        else:
            os.path.mkdir(filepath)

    def get_defaults():
        raise NotImplementedError

    def clear(self):
        self._items = get_defaults()

