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


class Game(BDScreen):
    _name = "game"
    _writable = False
    _pausable = False   # defaults to false is set after __init__ if otherwise
    _paused = False
    def __init__(self):
        self._ended = False
        self._local_player = None # the main machine local player
        from .game.data import GameData
        self._data = GameData(self)

    #@classmethod
    #def load_game(self, fp):
        #self._init_game
        # do loading stuff
        #self._start_game

    @classmethod
    def new_game(self):
        self._init_game
        self._start_game

    def _init_game(self):
        from .game.player import Player
        self._local_player = Player(self)

    def _start_game(self):
        pass

    def is_ended(self):
        """True if the current game has ended."""
        return self._ended

    @property
    def player(self):
        """The player of this game (at the current machine)."""
        return self._local_player

    def _get_paused(self): return self._paused
    def _set_paused(self, p):
        if self._pausable: self._paused = bool(p)
    paused = property(_get_paused, _set_paused,
        doc="""Sets the 'paused' state of the current game.
(May not be available in all game types)""")
