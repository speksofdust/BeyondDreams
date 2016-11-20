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
NAME =      "Beyond Dreams"
session =   None


__all__ = "getversion", "session", "NAME"


def getversion():
    global VERSION
    return VERSION

# major, minor, rev
def _gva(v=VERSION): return VERSION.split(".")[0]
def _gvb(v=VERSION): return VERSION.split(".")[1]
def _gvc(v=VERSION): return VERSION.split(".")[2]

getversion.major = _gva
getversion.minor = _gvb
getversion.revision = _gvc


def _start():
    # first get a console up
    from msg import Console
    console = Console()
    console.log.info(
                    "Initalizing Beyond Dreams <Version: {}>...".format(
                    VERSION), verbosity=0)
    from core.paths import set_localcfg_path
    set_localcfg_path()

    try: import xsquare
    except:
        #from core.paths import xs_path_from_file
        #try: # TODO xs_path_from_file()
        #except:
        raise ImportError("""Could not find package 'xsquare'. Make sure XSquare  is installed and try setting the path to xsquare in '{}'""".format(
            get_xs_path_file()))

    # init session then run xsquare app
    global session
    session = _Session()
    session.console = console
    if session._initargs:
        "::Beyond Dreams Session started <using initargs: {}>".format(
            str(session._initargs[1:-1]))
    else: session.console.log.info(
        "::Beyond Dreams Session started::", verbosity=10)
    xsquare.app.run()

class _Session:
    def __init__(self):
        from user import User
        from screen import ScreenNav
        self._initargs = []
        self.console = None
        self._user = None
        self._screen = ScreenNav() # The current screen

    @property
    def user(self):
        """The current user."""
        return self._user

    @property
    def screen(self):
        """The current screen."""
        return self._screen

    def quit(self):
        """Quit Beyond Dreams."""
        self._globvars.update
        try: self._user.logout("q")
        except: pass
        self.console.log_info("::Quit BeyondDreams Session::", verbosity=10)

