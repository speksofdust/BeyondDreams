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
from .core.baseclasses import BDDataDict


class Game(BDScreen):
    _name = "game"
    _writable = False
    _pausable = False   # defaults to false is set after __init__ if otherwise
    _paused = False
    def __init__(self):
        self._player = None
        self._data = None
        self._ended = False

    def _start_game(self):
        if self._player:
            self._data = GameData(self) # create initial game data

    def is_ended(self):
        """True if the current game has ended."""
        return self._ended

    @property
    def player(self):
        """The player of this game (at the current machine)."""
        return self._player

    def _get_paused(self): return self._paused
    def _set_paused(self, p):
        if self._pausable: self._paused = bool(p)
    paused = property(_get_paused, _set_paused,
        doc="""Sets the 'paused' state of the current game.
(May not be available in all game types)""")


class GamaData(BDDataDict):
    """Storage class for game data."""
    path_suffix = 'savedgames'

    def fmt_filename(name, number):
        return '{}_{}'.format(name, number)

    def __init__(self, game):
        self._game = game
        self._last_save_num = 0
        self = {
            }

    def quick_save(self):
        if self._game._writable:
            self.write(self.default_dirname, fmt_filename(
                ''.join(self._name, '_', 'quicksave'), self._last_save_num += 1))

    def write(self, filename, dirname, comment=''):
        if self._game._writable:
            import os.path
            if os.path.isdir(dirname):
            # TODO
            #import datetime
            #f.write(created = datetime.datetime.now())
            #f.write(comment = comment)
            pass
