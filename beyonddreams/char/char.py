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
import pdict

from beyonddreams.core.baseclasses import BDDataDict
from .vident import VIDENT_TYPES
from .game.location import Visited
from stats import Stats
import charflags


CHAR_TYPEFLAGS = ('VISITED_NOMEM',)


def _boolkw(char, k, **kwargs): if k in kwargs: char[k] = bool(kwargs[k])


class Char(pdict.PDict):
    """Character data storage class."""
    _ident = VIDENT_TYPES["char"]
    __slots__ = JparseDict.__slots__ + ('_gamechar', '_controller',
        '_specialflags')
    def __init__(self, data={}, parseinit=True, **kwargs):
        # Non-Writable values
        self._gamechar = False
        self._controller = None # AI, player, etc. # needed for gamechar only
        self._specialflags = set()
        self._tempflags = set()

        # parse kwargs
        _boolkw(self, 'gamechar', kwargs)
        _boolkw(self, 'npc', kwargs)
        if 'specialflags' in kwargs:
            self._specialflags = set(kwargs['specialflags'])


        super().__init__(data=data, parseinit=parseinit)

        if 'VISITED_NOMEM' not in self._specialflags:
            self['visited'] = Visited()

        # TODO validate/assign charid

        if self._gamechar: # add to gamechars
            gamedata['chars'][self['charid']] = self

    def _defaultdict(self):
        return {'base':         None,
                'npc':          False,
                'charid':       0,  # local charid
                'handedness':   0,
                'partyid':      -1,
                'equip':        Equip(self),
                'inventory':    Inventory(self),
                'stats':        Stats(self, kwargs),
                'statuses':     Statuses(self, kwargs),
                'visited':      False,
                # flags
                'dflags':       charflags.DFlags(), # died flags
                'ond-flags':    charflags.CharFlags(), # on died flags
                'onr-flags':    charflags.CharFlags(), # on revive flags
                }

    def _parseinit(self):
        from pdict import init_from_key_child
        from pdict import init_from_key
        # convert json data to proper classes
        init_from_key_child(self, 'equip', Equip)
        init_from_key_child(self, 'inventory', Inventory)
        init_from_key_child(self, 'stats', Stats)
        init_from_key_child(self, 'statuses', Statuses)
        # convert flags to sets
        self['dflags'] = charflags.DFlags(self['dflags']
        init_from_key(self, 'ond-flags', charflags.CharFlags)
        init_from_key(self, 'onr-flags', charflags.CharFlags)


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
        return iter(self['base'].famtypes)

    @property
    def base(self):
        return self['base']

    @property
    def plane(self):
        return 0 # TODO

    # ---- Tests --------------------------------------------------------- #
    def is_alive(self):
        return self.hp > 0

    def hp(self):
        return self['stats']['health']

    def is_critical(self):
        return self['stats']['health'].is_critical()

    def is_undead(self):
        """True if this character is an undead type or has zombie status."""
        return ("zombie" in self["statuses"]["bools"] or
            "zombie" in self.famtypes)

    # ---- Management ---------------------------------------------------- #
    @property
    def controller(self):
        """This character's controller. ('ai', 'player', etc.)"""
        return self._controller

    def _set_controller(self, mode, party=None):
        if mode == 'player':
        elif mode == 'ai':
        else: pass # TODO should log this

    def tempflags(self):
        return self._tempflags

    @property
    def dflags(self):
        return self['dflags']

    @property
    def ond_flags(self):
        return self['ond-flags']

    @property
    def onr_flags(self):
        return self['onr-flags']

    def has_dflag(self, name):
        return DFLAGS[name] in self['dflags']

    def has_onr_flag(self, name):
        return x in self['onr-flags']

    def has_ond_flag(self, name):
        return x in self['ond-flags']

    # ---- Event actions ------------------------------------------------- #
    def died(self, *causes):
        self.stats.health.hp = 0
        for i in causes: self.dflags.add(i)


    def revive(self, restore_amt=0):
        if (restore_amt > 0 and not self.has_onr_flag('null'))
            if self.is_alive():
                if self.dflags.has_nonrevivable() and
                    not in self['onr-flags']):

                    self.dflags.clear()

                    if self.has_onr_flag('half'):
                        self.stats.health.hp = restore_amt/2
                    elif self.has_onr_flag('2x'):
                        self.stats.health.hp = restore_amt*2
                    else:
                        self.stats.health.hp = restore_amt


                    self.onr_flags.clear()
                    self.on_revived(self)

            # zombie checks
            # TODO zombie famtype
            elif self.statuses['undead'] > 0: # undead status
                self._undead_revive(restore_amt, self.statuses['undead'])
            else: pass # no effect

    def _undead_revive(self, res, val):
        import random # TODO 'calc_factor' in restore_amt
        n = random.randint(0, int(val)) # FIXME
        if val > 50:
            x = bool(n in range(0, 100)) # FIXME
            if x: self.died('revived-as-zombie')
            else: pass # do n% dmg of health

        else: # do n% dmg of health
            pass


    # ---- Events -------------------------------------------------------- #
    def on_died(self, plane):
        pass

    def on_revived(self):
        pass


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


