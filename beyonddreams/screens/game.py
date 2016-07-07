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

from screen import BDScreen
from screen import GAME


class GameScreen(BDScreen):
    _name = "game"
    def __init__(self):
        super().__init__()

    def exit_to_title(self):
        pass

    def quit(self):
        pass


class GameSetupScreen(BDScreen):
    _name = "game setup"
    def __init__(self):
        super().__init__()
        self._gamesetup = GameSetup()

    def exit_to_title(self):
        pass

    def quit(self):
        pass


class GameSetup:
    def __init__(self):
        self._gametype = -1     # -1 for unset TODO
        self._networked = False
        self._pausable = False

    def load_game_config(self):
        pass

    def _can_start(self):
        return False

    def _checks(self):
        if self._networked: self._pausable = False

    def start_game(self):
        """Start the game with the current configuration."""
        if self._can_start():
            from .game import game
            game._init_game(self)


