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

from .core.exceptions import UserException
from .core.exceptions import UserIDError

import string

UID_LEN = 24

def valid_username_chars():
    yield '_'
    yield string.ascii_letters
    yield string.digits

def _get_username_input():
    global valid_username_chars
    #while True:
    return x

def _get_charname_input():
    #string.ascii_letters
    #while True:
    return x


class BDUserException(Exception):
    """Generic user exception for Beyond Dreams User objects."""
    pass


class User(dict):
    def __init__(self):
        from keyset import CurrentKeySet
        import msg
        super().__init__({
            "uid": "",
            'config': UserConfig(self),
            'data': UserData(self),
            'keyset': CurrentKeySet(),
            'chars': UserChars(self),
            'msgchans': msg._Channels(),
            })
        self._uid = ""


    def __write(self):
        from .core import bddata
        with open(self.datapath(), 'wb') as f:
            bddata.write_hlines(f, d=self)
            for k in self:
                if i[0] != '~':
                    write_dump(f, self[k], k)


    def __read(self, f):
        from .core import bddata
        with open(self.datapath(), 'rb') as f:
            for i in f.readlines():
                for k in self:
                    if i.startswith(k):
                        self[k] = bddata.read_dump(i, k)


    @property
    def name(self):
        """The name of this user."""
        return self._data['name']

    @property
    def config(self):
        """The BeyondDreams configuration for this user."""
        return self['config']

    @property
    def data(self):
        """User data such as username, ."""
        return self['data']

    @property
    def chars(self):
        return self['chars']

    def datapath(self, *args):
        """Return the users localcfg path from a user id joined with args.
        A UserIDError is raised if user_id is an empty string."""
        if self['uid']: return get_localcfg_path('users', self['uid'], *args)
        raise UserIDError("UserID not set.")

    def delete(self):
        # confirm(title="Delete User?",
        #    "You are about to delete your user profile, "
        #   "are you sure you wish to continue?")
        pass

    def logout(self, quitting=False):
        """Logout this user."""
        from .bd import session
        # check if we need to confirm before logout
        if (self['config']["session-confirm-logout"] == 1 or
            (self['config']["session_confirm_logout"] == 2 and
                session.screen.current.name != "title")):
                    pass    # TODO
                #   confirm(title="Confirm Logout",
                #       "You are about to logout of your user profile, "
                #       "are you sure you wish to continue?")

        self._config.write
        del self['msgchans']
        del self['config']
        if quitting:
            pass


class _UserStore(dict):
    def __init__(self, user, d={}):
        super().__init__(d)
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
    path_suffix = "config"
    def __init__(self, user):
        from defaultconfig import DEFAULT_USER_CONFIG
        super().__init__(user, d=DEFAULT_USER_CONFIG)


class UserData(_UserStore):
    """Storage class for user data, such as user statitistics."""
    path_suffix = "data"
    def __init__(self, user):
        super().__init__(user, d={
            "name": "",
            })


class UserChars(_UserStore):
    """Storage class for user characters."""
    path_suffix = "charlist"
    def __init__(self, user):
        super().__init__(user)

    def new_char(self, preset=None):
        if preset is not None: pass
        pass

    def del_char(self, char):
        pass


