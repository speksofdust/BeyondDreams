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


def valid_username_chars():
    yield '_'
    yield string.ascii_lowercase
    yield string.digits

def valid_charname_chars():
    yield string.ascii_letters


class User:
    def __init__(self):
        self._config = UserConfig(self)
        self._data = UserData(self)
        self._chars = UserChars(self)
        # makes a new user if filepath is None
        #self._globvars = GlobVars.userglobals(filepath)
        #self._data = None
        import msg
        self._msgchans = msg._Channels()

    @property
    def name(self):
        """The name of this user."""
        return self._data['name']

    @property
    def config(self):
        """The BeyondDreams configuration for this user."""
        return self._config

    @property
    def data(self):
        """User data such as username, ."""
        return self._data

    @property
    def chars(self):
        return self._chars

    def _get_path(self, *p):
        import os.path
        # FIXME Homedir
        return os.path.join(self.name, *p)

    def logout(self, q=False):
        """Logout this user."""
        self._config.write
        del self._msgchans
        del self._config
        self._msgchans = None
        self._config = None
        if q: # quitting
            pass


class _UserStore(dict):
    def __init__(self, user, d):
        self = d
        self._user = user
        self._is_saved = True


    @property
    def user(self):
        return self._user

    def is_saved(self):
        return self._is_saved

    #def write(self):
    #    self.user._get_path(pathname)



class UserConfig(_UserStore):
    """Storage class for user local configuration settings, such as
    graphics, audio, etc."""
    pathname = "config"
    def __init__(self, user):
        _UserStore.__init__(user, d={

            })


class UserData(_UserStore):
    """Storage class for user data, such as user statitistics."""
    pathname = "data"
    def __init__(self, user):
        _UserStore.__init__(user, d={
            "name": "",
            })


class UserChars(_UserStore):
    pathname = "charlist"
    def __init__(self, user):
        _UserStore.__init__(user)

