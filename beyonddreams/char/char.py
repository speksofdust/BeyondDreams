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
import charflags
from chardictkwds import *


CHAR_SPECIALFLAGS = ('VISITED_NOMEM', 'RELATIONSHIPS_OFF')


def _boolkw(char, k, **kwargs): if k in kwargs: char[k] = bool(kwargs[k])


class Char(pdict.PDict):
    """Character data storage class."""
    _ident = VIDENT_TYPES["char"]
    __slots__ = pdict.PDict.__slots__ + ('_gamechar', '_controller',
        '_specialflags')
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
        if 'VISITED_OFF' not in self._specialflags or
            gamedata['constflags']:
                self[VISITED] = Visited()

        #if ('RELATIONSHIPS_OFF' not in self._specialflags or
        #    gamedata['constflags']):


        # TODO validate/assign charid

        if self._gamechar: # add to gamechars
            gamedata['chars'][self[CHARID]] = self

    def _defaultdict(self):
        return {
                BASE:           None,
                NPC:            False,
                CHARID:         0,  # local charid
                PARTYID =       -1,
                HANDEDNESS:     0,
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
                'dflags':       charflags.DFlags(), # died flags
                'ond-flags':    charflags.CharFlags(), # on died flags
                'onr-flags':    charflags.CharFlags(), # on revive flags

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
            )
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
        return self[INVENTORY]

    @property
    def stats(self):
        """This character's stats."""
        return self[STATS]

    @property(self):
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

    def has_dflag(self, name):
        """True if at this char has at least one Died flag."""
        return DFLAGS[name] in self['dflags']

    def has_onr_flag(self, name):
        """True if this char has at least one On-Revive flag."""
        return x in self['onr-flags']

    def has_ond_flag(self, name):
        """True if this char has at least one On-Died flag."""
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


