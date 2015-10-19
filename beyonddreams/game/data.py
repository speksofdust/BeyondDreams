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

from .core.bddata import BDDataDict


gamedata = None

__all__ = gamedata


def fmt_filename(name, number):
    return '{}_{}'.format(name, number)


class GameDataAccessor:
    def __dpath(): raise NotImplementedError
    __slots__ = ()

    def __eq__(self, x): return self.__dpath == (x or x.__dpath())
    def __ne__(self, x): return self.__dpath != (x or x.__dpath())


class GameDataAccessorSeq(GameDataAccessor):
    __slots__ = ()
    def __init__(self):
        pass
    def __iter__(self): return iter(self.__dpath())
    def __len__(self): return len(self.__dpath())
    def __contains__(self, i): return i in self.__dpath()
    def __getitem__(self, i): return self.__dpath[i]


class GamaData(BDDataDict):
    """Storage class for game data."""
    path_suffix = 'savedgames'
    datatype = "gamedata"
    def __init__(self, game):
        self._game = game
        self._last_save_num = 0
        super().__init__({
            'chars': {},
            'party': (0, []), # active, list of members
            }

    @classmethod
    def load_game(self, filepath):
        if self._game:
            from gui.prompts import QuitPrompt
            x = QuitPrompt(("""There is already a game in progress.\nDo you wish to load a new game?\n(Your progress will not be saved.)""")
            if x.get_input() == True:
                pass
                # TODO
                # do we need to create a new player object?
        else:
            pass
        #super().__init__() # json.loads stuff here


    def quick_save(self):
        if self._game._writable:
            self.write(self.default_dirname, fmt_filename(
                ''.join(self._name, '_', 'quicksave'), self._last_save_num += 1))

    def write(self, filename, dirname, comment=''):
        if self._game._writable:
            bddata._wd(self, filename, dirname, comment)

    # ---- Data Accessors ----------------------------------------------- #
    @property
    def party(self):
        """Access party data."""
        return

    @property
    def all_chars(self):
        """Access all character data."""
        return
