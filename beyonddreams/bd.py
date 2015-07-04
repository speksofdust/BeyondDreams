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

VERSION =   "0.1.1"
session =   None

def version():
    """Return the version number.."""
    global VERSION
    def major(): return VERSION.split(".")[0]
    def minor(): return VERSION.split(".")[1]
    def revision(): return VERSION.split(".")[2]
    return VERSION


__all__ = "version", "session"


def _start():
    global session
    import xsquare
    from core.paths import set_localcfg_path
    set_localcfg_path()

    # init session then run xsquare app
    session = _Session()
    xsquare.app.run()


class Session:
    def __init__(self):
        from globvars import GlobVars
        from user import User
        from screen import ScreenNav

        # If no globals path can be found defaults will be used
        self._globvars = GlobVars(BD_GLOBALS_PATH)
        self._user = None
        self._screen = ScreenNav() # The current screen

    @property
    def screen(self):
        """The current screen."""
        return self._screen

    def quit(self):
        """Quit Beyond Dreams."""
        self._globvars.update
        try: self._user.logout("q")
        except: pass

