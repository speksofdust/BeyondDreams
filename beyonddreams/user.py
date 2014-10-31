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


class User:
    __slots__ = "_globvars", "_data"
    def __init__(self):
        self._globvars = None
        self._data = None
        
    @property
    def globvars(self):
        return self._globvars
        
    @property
    def data(self):
        return self._data
        
    def is_saved(self):
        return (self._globvars._saved and self._data._saved) == True
            
    def _update_write(self):
        try: 
            self._globvars.update
            self._data.update
        except: pass
    
    def logout(self, q=False):
        """Logout the current user. (if any)"""
        self._globvars.update
        self._data.update
        self._gvars = None
        self._data = None
        if q: # quit
            pass

class UserRoster:
    __slots__ = "_data"
    def __init__(self):
        self._data = {}
        
    def read(self):
        pass
        
    def write(self):
        pass
        
        
class UserSettings:
    __slots__ = "_user", "_roster"
    def __init__(self, roster, username):
        self._roster = UserRoster()
        self._username = username
        
    def change_name(self):
        pass
        
    def delete(self):
        pass
        # del self._roster._data[name]
