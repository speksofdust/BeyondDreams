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

VERSION =           "0.1.1"
DATA_PATH =         "beyonddreams"
BD_GLOBALS_PATH =   ""

session = None

def datapath(*args):
    """Returns the absolute path of "beyonddreams/data/" joined with args."""
    import os
    return os.path.join(os.path.abspath(__file__), "data", *args)

__all__ = "datapath", "session"

def _start():
    import xsquare
    
    # TODO set BD_GLOBALS_PATH by operating system
    
    # init session then run xsquare app
    session = _Session()
    xsquare.app.run()
    

class Session:
    __slots__ = "_user", "_globvars", "_screen"
    def __init__(self):
        from globvars import GlobVars
        from user import User

        #self._globvars = GlobVars(BD_GLOBALS_PATH)
        self._user = User()
        self._screen = None # The current screen
        
    def quit(self):
        self._globvars.update
        self._user.logout("q")
