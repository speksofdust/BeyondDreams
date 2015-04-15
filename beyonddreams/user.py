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

import string

from globvars import GlobVars

def load_user_roster():
    pass

def valid_username_chars():
    yield '_'
    yield string.ascii_lowercase
    yield string.digits

def valid_charname_chars():
    yield string.ascii_letters


class User:
    def __init__(self):
        self._username = username
        self._config = UserConfig()
        self._data = UserData()
        # makes a new user if filepath is None
        #self._globvars = GlobVars.userglobals(filepath)
        #self._data = None
        import msg
        self._msgchans = msg._Channels()

    @property
    def name(self):
        return self._settings.name

    @property
    def data(self):
        return self._data
    
    def logout(self, q=False):
        """Logout the current user. (if any)"""
        self._settings.write
        del self._msgchans
        self._msgchans = None
        del self._settings
        if q: # quitting
            pass


class _UserStore(dict):
    _is_saved = True
    

class UserConfig(_UserStore):
    pass


class UserData(_UserStore):
    pass


class UserRoster:
    """Stores userdata locations."""
    __slots__ = "_data"
    def __init__(self):
        self._data = {}

    def read(self):
        pass

    def write(self):
        pass
