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
BD_GLOBALS_PATH =   ""

session =   None


def datapath(*args):
    """Returns the absolute path of "beyonddreams/data/" joined with args."""
    import os.path
    return os.path.join(os.path.split(os.path.abspath(__file__)),
        "data", *args)

__all__ = "datapath", "session"


def _start():
    global session
    import xsquare
    
    # TODO set BD_GLOBALS_PATH by operating system
    
    # init session then run xsquare app
    session = _Session()
    xsquare.app.run()
    

class Session:
    def __init__(self):
        from globvars import GlobVars
        from user import User
        
        # If no globals path can be found defaults will be used
        self._globvars = GlobVars(BD_GLOBALS_PATH)
        self._user = None
        self._screen = None # The current screen
        
    @property
    def screen(self):
        """The current screen."""
        return self._screen
        
    def quit(self):
        """Quit Beyond Dreams."""
        self._globvars.update
        try: self._user.logout("q")
        except: pass
  

# ---------------------------------------------------------------------------- #
class BDScreen:
    """Base class for Beyond Dreams "Screen" Objects.
        This defines what will be displayed when 
        'session.screen' = a given screen object.
    """
    _running =  False
    _name =     "dummy"
    def __init__(self): pass
        
    # eq, ne -- test 'x is self', then x 'isinstance of' and so on
    def __eq__(self, x):
        if x is not self:
            if (isinstance(x, BDScreen): return x._name == self._name
            raise TypeError("cannot compare type '{}' to BDScreen type.".format(
                x.type))
        return True

    def __ne__(self, x):
        if x is not self:
            if isinstance(x, BDScreen): return x._name != self._name
            raise TypeError("cannot compare type '{}' to BDScreen type.".format(
                x.type))
        return False


    def start(self):
        """Start this screen."""
        if session._screen != self:
            try: self.pre_run
            except: pass
            session._screen = self
            self.run

    def pre_run(self):
        """Called before the screen becomes active."""
        raise NotImplementedError
        
    def run(self):
        raise NotImplementedError

    @property
    def name(self):
        """The name of this screen."""
        return self._name

    def is_running(self):
        """True if this scene is currently running."""
        return self._running

