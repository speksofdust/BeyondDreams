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

__all__ = ()

def write(f, data):
    pass
    
def load(f):
    import os.path
    if os.path.exists(filepath):
        with open(filepath, 'rb') as f:
            for i in iter(f.readlines())
                if i.startswith('#'): continue
    else:
        os.path.mkdir(filepath)
        # TODO


class VarData:
    """Variable data storage class."""
    def __init__(self, items):
        self._items = items
        self._saved = True
    
    def is_saved(self):
        """True if no (writable) changes have been made since the last save."""
        return self._saved == True
    
    def update(self):
        if self._saved == False: write(f, self._items)
        self._saved = True
    

def default_globalvars():
    """Return a dict with default globalvars."""
    return {

        }

def default_userglobals():
    """Return a dict with default userglobals."""
    return {
        'Bestiary':     set(),  # a new empty bestiary
        }



class GlobVars(VarData):
    """Global variables storage class."""
    def __init__(self, f): # game session globals
        self.get_defaults = default_globalvars
        if os.path.exists(f):
            pass # TODO
        else:    self._items = default_globalvars()
        self._saved = True

    @classmethod
    def userglobals(self, f=None):
        self.get_defaults = default_userglobals
        if f is None:   # New User
            self._items = default_userglobals()
        else:           # Attempt to load users globvars file
            pass        # TODO
            
        self._saved = True

    def get_defaults(self):
        """Return a dict of the default variables."""
        raise NotImplementedError

    def clear(self):
        """Reset all variables to the defaults."""
        self._items = get_defaults()

