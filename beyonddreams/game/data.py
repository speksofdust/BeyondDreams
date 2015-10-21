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
import gameaccessors as gacc

gamedata = None

__all__ = gamedata


def fmt_filename(name, number):
    return '{}_{}'.format(name, number)


class GamaData(BDDataDict):
    """Storage class for game data."""
    path_suffix = 'savedgames'
    bd_datatype = "gamedata"
    bd_dataver = '0.1'
    def __init__(self, game=None, *args, **kwargs):
        self._game = game
        self._last_save_num = 0
        super().__init__({
            'chars': {},
            'party': (0, []), # active, list of members
            'visited': {},    # locations visited data
            }

    @classmethod
    def load_data(self, filepath):
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

    @property
    def writable(self):
        """True if this gamedata is writable."""
        return self._game.writable

    def quick_save(self):
        if self.writable:
            self.write(self.default_dirname, fmt_filename(
                ''.join(self._name, '_', 'quicksave'), self._last_save_num += 1))

    def write_data(self, filename, dirname, comment=''):
        if self.writable:
            bddata._wd(self, filename, dirname, comment)

    # ---- Data Accessors ----------------------------------------------- #
    @property
    def party(self):
        """Access party data."""
        return gacc.PartyAccessor(self)

    @property
    def all_chars(self):
        """Access all character data."""
        return gacc.AllCharsAccessor(self)

    def party_chars(self):
        """Return an iterator of all party character data in current party order."""
        return iter(self['chars'][i] for i in self['party'][1])

    #def _get_char(self, char):
    #    return CharDataAccessor(self, char)

    @property
    def visited(self):
        """Access the data visited locations."""
        return gacc.VisitedAccessor(self)


class EntryModeData(GameData):
    """Storage class for entry mode data."""
    path_suffix = 'savedgames'
    datatype = "emdata"

    def quick_save(self): raise NotImplementedError

    @property
    def visited(self):
        return gacc.EMVisitedAccessor
