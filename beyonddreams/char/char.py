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

from .bd import session
from beyonddreams.core.baseclasses import BDDataDict
from .vident import VIDENT_TYPES
from .game.location import Visited


CHAR_TYPEFLAGS = ('VISITED_NOMEM',)


def _boolkw(char, k, **kwargs): if k in kwargs: char[k] = bool(kwargs[k])


class Char(dict):
    """Character data storage class."""
    _ident = VIDENT_TYPES["char"]
    __slots__ = dict.__slots__ + ('_gamechar', '_npc', '_controller',
        '_specialflags')
    def __init__(self, data={}, jparse=False, **kwargs):
        self._gamechar = False
        self._npc = False
        self._controller = None # AI, player, etc. # needed for gamechar only
        self._specialflags = set()
        _boolkw(self, 'gamechar', kwargs)
        _boolkw(self, 'npc', kwargs)
        if 'specialflags' in kwargs:
            self._specialflags = set(kwargs['specialflags'])
        if jparse == False:
            super().__init__({
                'npc':          False,
                'charid':       0,  # local charid
                'handedness':   0,
                'partyid':      -1,
                'equip':        Equip(self),
                'inventory':    Inventory(self),
                'stats':        Stats(self, *kwargs),
                'statuses':     Statuses(self, *kwargs),
                'visited':      False,
            })
            if 'VISITED_NOMEM' not in self._specialflags:
                self['visited'] = Visted()
            # assign charid

        else:
            super().__init__(data)
            # convert json data to proper classes
            self['equip'] =     Equip(self, self['equip'])
            self['inventory'] = Inventory(self, self['inventory'])
            self['stats'] =     Stats(self, self['stats'])
            self['statuses'] =  Statuses(self, self['statuses'])

            if 'VISITED_NOMEM' in self._specialflags: self['visited'] = False
            else: self['visited'] = Visited(self['visited'])
            # validate charid

        if self._gamechar: # add to gamechars
            gamedata['chars'][self['charid']] = self


    # ---- Quick access to common stuff ---------------------------------- #
    @property
    def handedness(self):
        """This character's primary hand. (0=Left, 1=Right 2=Ambidextrous)"""
        return self['handedness']

    # ---- Object access ------------------------------------------------- #
    @property
    def party(self):
        """This character's party."""
        return gamedata.party_by_id(self._partyid)

    @property
    def inventory(self):
        """This character's inventory."""
        return self['inventory']

    @property
    def stats(self):
        """This character's stats."""
        return self['stats']

    @property(self):
    def statuses(self):
        """This character's statuses."""
        return self['statuses']

    @property
    def famtypes(self):
        """This character's family types."""
        return iter() # TODO

    # ---- Management ---------------------------------------------------- #
    def typeflags(self):
        """Returns an iterator of chartypeflags for this character."""
        return iter(self._typeflags)

    @property
    def controller(self):
        """This character's controller. ('ai', 'player', etc.)"""
        return self._controller

    def _set_controller(self, mode, party=None):
        if mode == 'player':
        elif mode == 'ai':
        else: pass # TODO should log this


class Chars(dict):
    """Character storage & management class."""
    __slots__ = dict.__slots__


class GameChars(Chars):
    """Ingame character storage & management class."""
    __slots__ = dict.__slots__


    def npcs(self):
        """Return an iterator of all NPCs (Non-playable characters)."""
        return iter(i for i in self if i._npc)

    def ai(self):
        """Return an iterator of all ai controlled characters."""
        return iter(i for i in self if i._controller == 'ai')


class Char:
    """Base class for character objects."""
    __slots__ = "_chardata", "_controller", "_owner"
    def __init__(self, player, base):
        self._owner =       owner
        self._player =      owner
        self._chardata =    CharData(self, base)

    @property
    def owner(self):
        """The player who owns this character."""
        return self._owner

    @property
    def player(self):
        """The player currently controlling this character."""
        return self._player

    def owner_is_player(self):
        """True if the owner of this character is also the one controlling it."""
        return self._owner == self._player

    def is_local_player(self):
        """True if this char is controlled by the "player" object
            on the local machine."""
        return self._player == session.screen.player


    # ---- Chardata access ---- #
    @property
    def location(self):
        return self._chardata["location"]

    @property
    def name(self):
        return self._chardata["name"]

    @property
    def base(self):
        """Base values for this character."""
        return self._chardata.base

    @property
    def body(self):
        """This characters body attributes."""
        return self._chardata["body"]

    @property
    def wallet(self):
        """This characters wallet."""
        return self._chardata["wallet"]

    @property
    def inventory(self):
        """This characters inventory."""
        return self._chardata["inventory"]

    @property
    def equip(self):
        """This characters equipment."""
        return self._chardata["equip"]

    @property
    def party(self):
        """The party this char is in."""
        return self._chardata["party"]

    # ---- Query ---- #
    def famtypes(self):
        """Return an iterator of family types for this character."""
        return ()

    def is_alive(self):
        """True if this character is alive."""
        if self._chardata["stats"]["HP"] == 0: return False
        return True

    def is_critical(self):
        """True if this characters health level is in the critical range."""
        return self._chardata["stats"]["HP"].is_critical()

    def is_undead(self):
        """True if this character is an undead type or has zombie status."""
        return ("zombie" in self._items["statuses"]["bools"] or
            "zombie" in self.famtypes)

    def hp(self):
        return self._chardata["stats"]["HP"]


