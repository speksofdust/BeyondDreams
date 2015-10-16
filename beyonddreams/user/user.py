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


def _get_username_input():
    global valid_username_chars
    #while True:
    return x

def _get_charname_input():
    global valid_charname_chars
    #while True:
    return x


class BDUserException(Exception):
    """Generic user exception for Beyond Dreams User objects."""
    pass


class User:
    def __init__(self):
        self._uid = ""
        from keyset import CurrentKeySet
        self._config = UserConfig(self)
        self._data = UserData(self)
        self._keyset = CurrentKeySet()
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

    def datapath(self, *args):
        """Return the users localcfg path from a user id joined with args.
        A ValueError is raised if user_id is an empty string."""
        if self._uid: return get_localcfg_path('users', user._uid, *args)
        raise ValueError("Invalid 'user_id'")
        import core.paths
        core.paths.get_user_path(self, *args)

    def delete(self):
        # confirm(title="Delete User?",
        #    "You are about to delete your user profile, "
        #   "are you sure you wish to continue?")
        pass

    def logout(self, q=False):
        """Logout this user."""
        from .bd import session
        # check if we need to confirm before logout
        if (self._config["session-confirm-logout"] == 1 or
            (self._config["session_confirm_logout"] == 2 and
                session.screen.current.name != "title"):
                    pass    # TODO
                #   confirm(title="Confirm Logout",
                #       "You are about to logout of your user profile, "
                #       "are you sure you wish to continue?")

        self._config.write
        del self._msgchans
        del self._config
        self._msgchans = None
        self._config = None
        if q: # quitting
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
    path_suffix = "charlist"
    def __init__(self, user):
        super().__init__(user)

    def new_char(self, preset=None):
        if preset is not None: pass
        pass

    def del_char(self, char):
        pass


