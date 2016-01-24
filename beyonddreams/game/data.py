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
from location import Visited
from .char.char import GameChars
from party import parties


gamedata = None

__all__ = gamedata


def fmt_filename(name, number):
    return '{}_{}'.format(name, number)


def load_game(filepath):
    global gamedata
    if gamedata._game is not None:
        from gui.prompts import QuitPrompt
        prompt = QuitPrompt(("""There is already a game in progress.\nDo you wish to load a new game?\n(Your progress will not be saved.)""")
        if prompt.get_input() == True:
            _do_loading_stuff(filepath)
            # TODO
            # do we need to create a new player object?
    else: _do_loading_stuff(filepath)

def _do_loading_stuff(filepath):
    global gamedata
    gamedata = None
    ok = False
    # do json.loads stuff

    gamedata = GameData(, jparse=True)


class GamaData(BDDataDict):
    """Storage class for game data."""
    path_suffix = 'savedgames'
    bd_datatype = "gamedata"
    bd_dataver = '0.1'
    def __init__(self, game=None, jparse=False, *args, **kwargs):
        self._game = game
        self._readystate = 0     #0-no, 1-yes (not started), 2-yes (started)
        self._last_save_num = 0
        if not jparse: # new game
            super().__init__({
                'chars': GameChars({}),
                'parties': {},
                'playerpartyid': 0,
                'visited': Visited(),    # locations visited data
                }

        self._readystate = 1
        else:
            ok = False
            super().__init__(kwargs['data'])
            # convert json data to proper classes
            self['chars'] = GameChars(self['chars'])
            for i in self['chars'] i = Char(self['chars'][i]
            self['visited'] = Visited(self['visited'])

            if not ok:
                gamedata._game = False
            else:
                gamedata._readystate = 1


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
    def parties(self):
        """Access parties."""
        return self['parties']

    def party_by_id(self, partyid):
        """Get and return a given party using a party id, or None
        if unavailable."""
        if partyid == -1: return None
        try: return self['parties'][partyid]
        except:
            return None

    @property
    def playerparty
        """Access the player party data."""
        return self.party_by_id(self['playerpartyid']

    @property
    def chars(self):
        """Access all character data."""
        return self['chars']

    #def _get_char(self, char):
    #    return CharDataAccessor(self, char)

    @property
    def visited(self):
        """Access the data visited locations."""
        return self['visited']


class EntryModeData(GameData):
    """Storage class for entry mode data."""
    path_suffix = 'savedgames'
    datatype = "emdata"

    def quick_save(self): raise NotImplementedError

    @property
    def visited(self):
        return gacc.EMVisitedAccessor
