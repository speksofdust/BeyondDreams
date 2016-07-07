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
from pdict import *

from beyonddreams.core.baseclasses import BDDataDict
from .vident import VIDENT_TYPES
from .game.location import Visited
from .game.planes import PLANES
from stats import Stats
from statuses import Statuses
import cflags
from chardictkwds import *


CHAR_SPECIALFLAGS = ('VISITED_NOMEM', 'RELATIONSHIPS_OFF')


def _boolkw(char, k, **kwargs):
    if k in kwargs: char[k] = bool(kwargs[k])


class Char(pdict.PDict):
    """Character data storage class."""
    _ident = VIDENT_TYPES["char"]
    __slots__ = pdict.PDict.__slots__ + ('_gamechar', '_controller',
        '_specialflags', '_tempflags')
    def __init__(self, data={}, parseinit=True, **kwargs):
        # Non-Writable values
        self._gamechar = False
        self._controller = None # AI, player, etc. # needed for gamechar only
        self._specialflags = set()
        self._tempflags = set()

        # parse kwargs
        _boolkw(self, 'gamechar', kwargs)
        _boolkw(self, NPC, kwargs)
        if 'specialflags' in kwargs:
            self._specialflags = set(kwargs['specialflags'])

        super().__init__(data=data, parseinit=parseinit, *args, **kwargs)

        # special flags/gamedata constflags stuff
        if ('VISITED_OFF' not in self._specialflags or
            gamedata['constflags']):
                self[VISITED] = Visited()

        #if ('RELATIONSHIPS_OFF' not in self._specialflags or
        #    gamedata['constflags']):


        # TODO validate/assign charid

        if self._gamechar: # add to gamechars
            gamedata['chars'][self[CHARID]] = self

    def _defaultdict(self):
        return {
                BASE:           None,
                NPC:            False,    # True if NPC
                CHARID_LOCAL:   0,
                CHARID:         0,         # server assigned charid
                PARTYID:       -1,
                HANDEDNESS:     0,
                ALLIANCE:       'none',
                GUILD:          'none',
                EQUIP:          Equip(self),
                INVENTORY:      Inventory(self),
                STATS:          Stats(self, kwargs),
                STATUSES:       Statuses(self, kwargs),
                VISITED:        False,
                #### partially implemented ####
                #RELATIONSHIPS = {},
                #### not yet implemented ####
                #PERSONALITY:  Personality(),
                #MOOD:         Mood(),

                # -- flags -- #
                'dflags':       cflags.DFlags(), # died flags
                'ond-flags':    cflags.CharFlags(), # on died flags
                'onr-flags':    cflags.CharFlags(), # on revive flags

                PLANE:        ['mortal', 'none'],
                }

    def _parseinit(self):
        # convert json data to proper classes
        init_from_key_cls_pairs_child(self, (
            (EQUIP, Equip),
            (INVENTORY, Inventory),
            (STATS, Stats),
            (STATUSES, Statuses),
            #(PERSONALITY, Personality),
            #(MOOD, Mood),
            ))
        # convert flags to sets
        self['dflags'] = cflags.DFlags(self['dflags'])
        init_from_key(self, 'ond-flags', cflags.CharFlags)
        init_from_key(self, 'onr-flags', cflags.CharFlags)


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
        return self[INVENTORY]

    @property
    def stats(self):
        """This character's stats."""
        return self[STATS]

    @property
    def statuses(self):
        """This character's statuses."""
        return self[STATUSES]

    @property
    def famtypes(self):
        """This character's family types."""
        return iter(self[BASE].famtypes)

    @property
    def base(self):
        return self[BASE]

    #@property
    #def personality(self):
        #return self['personality']

    #@property
    #def mood(self):
        #return self['mood']

    @property
    def pplane(self):
        """The current primary plane."""
        return PLANES[self[PLANE][0]]

    @property
    def splane(self):
        """The current secondary plane."""
        return PLANES[self[PLANE][1]]

    # ---- Tests --------------------------------------------------------- #
    def bodytype(self):
        return self.body.bodytype()

    def is_alive(self):
        return self.hp > 0

    def hp(self):
        return self[STATS][HEALTH]

    def is_critical(self):
        return self[STATS][HEALTH].is_critical()

    def is_undead(self):
        """True if this character is an undead type or has zombie status."""
        return ("zombie" in self[STATUSES]["bools"] or
            "zombie" in self.famtypes)

    # ---- NPC and auto actions ------------------------------------------ #

    @property
    def alliance(self):
        return self[ALLIANCE]

    def _is_foe_of(self, x):
        """True if x is a foe of this character."""
        return False

    def _is_neutral_of(self, x):
        """True if x is neutral to this character."""
        return True



    # ---- Management ---------------------------------------------------- #
    @property
    def controller(self):
        """This character's controller. ('ai', 'player', etc.)"""
        return self._controller

    def _set_controller(self, mode, party=None, req=False):
        if mode != self.controller:
            if mode == 'player':
                self._controller = mode
            elif mode == 'ai':
                self._controller = mode
            else:
                # dont raise unless req=True
                x = "Unknown controller mode '{}' for char._set_controller.".format(
                    mode)
                if req: raise(x)
                print(x) # TODO should log this instead of print

    def tempflags(self):
        return self._tempflags

    @property
    def dflags(self):
        """Died flags."""
        return self['dflags']

    @property
    def ond_flags(self):
        """On Died flags."""
        return self['ond-flags']

    @property
    def onr_flags(self):
        """On Revive flags."""
        return self['onr-flags']

    # ---- Event actions ------------------------------------------------- #
    def died(self, *causes):
        self.stats.health.hp = 0
        for i in causes: self.dflags.add(i)


    def revive(self, restore_amt=0):
        # has no effect on any if restore_amt==0
        if (restore_amt > 0 and 'null' not in self.onr_flags):
            if not self.is_alive():
                if not self.dflags.has_nonrevivable():

                    self.dflags.clear()

                    if 'half' in self.onr_flags:
                        self.stats.health.hp = restore_amt/2
                    elif '2x' in self.onr_flags:
                        self.stats.health.hp = restore_amt*2
                    else:
                        self.stats.health.hp = restore_amt

                    self.onr_flags.clear()
                    self.on_revived(self)

            # zombie checks
            # TODO zombie famtype
            elif self.statuses['undead'] > 0: # undead status
                import random # TODO 'calc_factor' in restore_amt
                n = random.randint(0, int(val)) # FIXME
                if val > 50:
                    x = bool(n in range(0, 100)) # FIXME
                    if x: self.died('revived-as-zombie')
                    else: pass # do n% dmg of health
                else: # do n% dmg of health
                    pass
            else: pass # no effect


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


class _Char_old:
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


