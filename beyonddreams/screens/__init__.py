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
import Title

screens = {
    "title" : Title,
    }


class ScreenNav:
    """Handles the navagation between 'screen objects'."""
    def __init__(self):
        self._last = None
        self._current = None
    
    @property
    def current(self):
        """The current screen."""
        return self._current

    @property
    def last(self):
        """The last screen."""
        return self._last
    
    def can_go_back(self):
        """True if can return to the previous screen."""
        return (self._last is not None or self._current._can_go_back)
    
    def go_back(self):
        """Go back to the previous screen, if the current screen permits it."""
        if self.can_go_back():
            self._change_screen(self._last, self._current._cleanup_on_go_back)

    def goto(self, screen):
        """Goto given screen."""
        if screen != self._current:
            if screen == self._last: self.go_back
            if screen in screens:
                if isinstance(screen, str): screen = screens[screen]
            if isinstance(screen, Screen):
                self._change_screen(screen, self._current._cleanup_on_goto)
            else: raise valueError("invalid screen: {}".format(screen))

    def _change_screen(self, n, cleanup):
        # helper for go_back and goto
        if cleanup: # kill the current screen
            self.current.end
            x = self._current
            self._current = n
            self._last = None
            x.cleanup
        else:   # keep both screens alive
            x = self._last
            self._last = self._current
            self._current = x


class BDScreen:
    """Base class for Beyond Dreams "Screen" Objects.
        This defines what will be displayed when 
        'session.screen' = a given screen object.
    """
    def __init__(self):
        self._name =     "dummy"
        self._running =  False
        self._can_go_back = False
        self._cleanup_on_go_back = True
        self._cleanup_on_goto = True

    # eq, ne -- test 'x is self', then x 'isinstance of' and so on
    def __eq__(self, x):
        if x is not self:
            if (isinstance(x, str) and x == self._name): return True
            if (isinstance(x, BDScreen): return x._name == self._name
            raise TypeError("cannot compare type '{}' to BDScreen type.".format(
                x.type))
        return True

    def __ne__(self, x):
        if x is not self:
            if (isinstance(x, str) and x != name): return True
            if isinstance(x, BDScreen): return x._name != self._name
            raise TypeError("cannot compare type '{}' to BDScreen type.".format(
                x.type))
        return False

    @property
    def name(self):
        """The name of this screen."""
        return self._name

    def is_running(self):
        """True if this screen is currently running."""
        return self._running

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

    def end(self):
        """Called to end this screen."""
        pass

    def cleanup(self):
        """Called to kill this screen after screen transition."""
        pass

