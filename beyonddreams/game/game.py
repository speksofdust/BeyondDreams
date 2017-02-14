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


GAME =          40
THOUGHTS =      41
READ_THOUGHTS = 42
CHAR_SPEECH =   43
CHAR_WHISPER =  44
PARTY_SPEECH =  45
PARTY_WHISPER = 46


DEFAULT_GAME_MGS_COLORS = {
    "game":             "#55A855",
    "thoughts":         "",         # own thoughts
    "read_thoughts":    "",        # mind reading
    "char_speech":      "",         #
    "char_whisper":     "",
    "party_speech":     "",
    "party_whisper":    "",
    }

current = _GameBC # current game

def _init_game(setup):
    if setup._networked: g = NetworkedGame()
    else: g = Game()
    global current
    current = g


class _GameBC():
    _name = ""
    _networked = False
    _pausable = False
    _gid = "00000000" # game id -- used for syncing
    def __init__(self):
        self._ended = False
        self._paused = False
        from data import GameData
        from player import Player
        self._data = GameData(self) # local data
        self._player = Player(self) # local player

    def _get_paused(self): return self._paused
    def _set_paused(self, p): pass
    paused = property(_get_paused, _set_paused,
        doc="""Sets the 'paused' state of the current game.
(May not be available in all game types)""")

    @property
    def player(self):
        """The local player."""
        return self._player

    @property
    def _init_epoch(self):
        return self._data['epoch']

    @property
    def _last_epoch(self):
        return self._data['epoch last']

    def time_tuple(self):
        """Return the current time in game. as a tuple of integers
            (weekday, hour, minute, current_day).
        """
        d = 0
        #TODO calc time diff 'd'
        self._data['time'] = []
        return self._data['time']

    def _ltime(self):
        return self._data['time']

    def time(self):
        from dates import GameTime
        return GameTime.now()


class Game(_GameBC):
    _pausable = True

    def _set_paused(self, p):
        if self._pausable: self._paused = bool(p)


class NetworkedGame(_GameBC):
    _pausable = False
    _networked = True

    def time(self):
        # for networked games we request the current *in game* time from server
        d = self.server.req('game.time')
        # TODO calc time diff d
        self._data['time'] = []
        return self._data['time']

