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

# will replace char.py
import cacc
from wallet import Wallet
from famtypes import FamTypeAccessor
import statgroups

CHAR_ID_LEN = 30


CHARFLAGS = {
    # Temp Flags
    "has-encounter":    50, # currently attacked or in battle, etc.
    "full-recover":     98,

    # ---- ko-flags ---- #
    "revive_once":      99, # fails if ko'd in non revivable condition

    # ---- KO-Type flags (as many as applicapable) ---- #
    "suffocated":       111,
    "drowned":          112,

    # last hit
    "stabbed":          113,
    "beaten":           114,
    "electrocuted":     115,
    "burned":           116,
    "froze":            117,

    # status(s) maxed
    "bled":             120, # bleed level maxed
    "poisoned":         121, # poisoning level maxed
    "drunk":            122, # drunk & poisioning levels maxed

    # other
    "gutted":           198,
    "halved":           199, # split in half

    # non-revivable ko-type flags
    "beheaded":         200,
    "exploded":         201,
    "vaporized":        202,
    "flattened":        203,
    }

def _inc_stat(char, name, v=1):
    try: char['game-stats'][name] += v
    except: char['game-stats'][name] = v


# ---- status stuff ---------------------------------------------------------- #
def clear_statuses(char):
    """Reset all status values to 0."""
    for i in char['statuses']: char['statuses'][i] = 0

def full_recovery(char):
    """Clear all statuses and restore health and energy."""
    clear_statuses(char)
    char["phys-energy"] = 100
    char["mental-energy"] = 100
    char["health"] = 100

def get_status(char, name):
    return char['statuses'][name]

def set_status(char, name, v):
    char['statuses'][name] = v


# ---- Query ----------------------------------------------------------------- #
def is_alive(char):
    """True if char is currently in ko state."""
    return not any(i>=100 for i in char['KO-flags'])

def has_koflag(char, flag):
    global CHARFLAGS
    return CHARFLAGS[flag] in char['KO-flags']

def _has_spawn_timeout(char):
    try:
        if char['temp']['spawn-timeout'] > 0:
            char['temp']['spawn-timeout'] -= 1
            return True
        del char['temp']['spawn-timeout'] # delete if 0
        return False
    except: return False # no variable exists

def _killchar(char, *flags):
    global CHARFLAGS
    char['health'] = 0
    char['KO-flags'].append(CHARFLAGS[i] for i in flags)

    # remove revive-once flag if non-revivable KOType
    if any(i >= 200 for i in flags):
        char['KO-flags'].discard(CHARFLAGS['revive-once'])

def update_char(char):
    if is_alive(char):  # ---- Alive ------------------------------------ #
        # status ko checks -- these should be done after each statuses is applied
            if char['statuses']['poisioned'] == 100:
                # drunk > 200 starts to slowly increment poisoned stat
                #   as char keeps drinking
                if char['statuses']['drunk'] == DRUNK_MAX:
                    _killchar(char, 'drunk') # alcohol poisioning
                _killchar(char, 'poisioned') # just poisioned
            elif char['statuses']['bleed'] == 100:
                _killchar(char, 'bleed')
            else:
                return

    else:               # ---- Char KO'd -------------------------------- #
        if not _has_spawn_timeout(char):
            if has_koflag(char, 'revive-once'):
                return _on_restore(char, revived=True)
        return


# ---- post ko events -------------------------------------------------------- #
def _on_restore(char):
    """Called after restored or revived."""
    if has_koflag(char, 'revive-once'):
        if char['game-stats']: _inc_stat(char, 'revived') # increment revived stat
    if has_koflag(char, 'full-recover'): _full_recover(char)

    # lastly
    if char['stats']:
        for i in char['KO-flags']:
            if i<= 100: _inc_stat(char, i)  # increment 'KO'd by' stat
    char['KO-flags'] = []               # clear KO flags

def _respawn(char):
    pass

# ---- Other Events ---------------------------------------------------------- #
def _warp(char):
    pass


_chardata_dict = {
    "temp":         {}, # non-writable stuff
    # flags
    "temp-flags":   [], # non-writable
    "flags":        [],
    "KO-flags":     [], # cleared after revived|re-spawn
    # base data
    "base":     "",

    # name
    "name-first":   "",
    "name-last":    "",
    "name-middle":  "",
    "name-nick":    "",

    "location": {
        'region':   0,
        }

    "body":     {
        }

    # inventory & wallet
    "cash":         [0],
    "coupons":      [],
    "cards":        [],
    "bag":          "default",
    "consumables":  [],
    "weapons":      [],
    "wearables":    [],
    "keyitems":     [],

    # equip
    "handedness":   0,  # 0-left, 1-right, 2-ambidextrous
    "equip":    {
        },

    # stats stuff
    "phys-energy":      100,
    "mental-energy":    100,
    "health":           100,

    "statuses": {
        # physical
        "frozen":       0,   # bool
        "frostbite" :   0,
        "burn" :        0,
        "numb" :        0,
        "stun" :        0,
        "poisoning" :   0,
        "bleed" :       0,

        # mental
        "blind" :       0,
        "drunk" :       0,
        "dumb" :        0,
        "confusion" :   0,
        #"hallucination": 0,

        # transform
        "zombie" :      0,
        "mutagen" :     0,

        # specials
        "immunull":     0,  # bool
        "immundown":    0,
        },
    }

from game.data import gamedata

# ---- Char creation and deletion -------------------------------------------- #
def _new_game_char(playable):
    from xsquare.utils.strutils import rand_alphanumeric
    global CHAR_ID_LEN, _chardata_dict
    cid = rand_alphanumeric(CHAR_ID_LEN)
    while True:
        if cid in gamedata['chars']:
            cid = rand_alphanumeric(CHAR_ID_LEN)
        gamedata['chars'][cid] = _chardata_dict.copy()
        if playable:
            gamedata['chars'][cid]['game-stats'] = {}

def _del_game_char(charid)
    try: del gamedata['chars'][charid]
    except: KeyError

def _clear_temps():
    for i in gamedata['chars']:
        try: del gamedata['chars'][i]['temp']
        except: KeyError

def _update_chars():
    for i in gamedata['chars']: update_char(gamedata['chars'][i])


class Chars(list):

    def alive(self):
        """Return an iterator of all alive characters."""
        return iter(i for i in self if i.isalive())

    def critical(self):
        """Return an iterator of all characters who's health is between 1 and
        10 percent."""
        return iter(i for i in self if i.critical())

    def undead(self):
        """Return an iterator of all characters of undead fam type or who have
        zombie status of 100."""
        return iter(i for i in self if i.is_undead())


class CharAccessor(GameDataAccessorDict):
    __slots__ = ("char", "data")
    def __init__(self, char):
        self.char = char

    def __dpath(self): return gamedata['chars'][self.char]

    @property
    def name(self):
        return cacc.CharNameAccessor(self)

    @property
    def inventory(self):
        return cacc.CharInventory(self)

    @property
    def statuses(self):
        return cacc.Statuses(self)

    @property
    def wallet(self):
        return Wallet(self)


# ---- Query --------------------------------------------------------- #
def base(char):
    """Access the base stats and other properties of this character."""
    return char['base']

def famtypes(char):
    """Return an iterator of family types for this character starting with
    the primary type."""
    yield i for i in char['base'].famtypes

def handedness(char):
    """The handedness of this character.
    0: left    1: right    2: ambidextrious"""
    return char['handedness']

def is_alive(char):
    """True if this character's hp is 0."""
    return char['stats']['hp'] != 0

def is_critical(char):
    """True if this character's hp is health is between 1 and 10 percent."""
    return 1 <= char['stats']['hp'] <= 10

def is_undead(char):
    """True if this character has a fam type of 'undead' or has 'zombie'
    status."""
    return ('undead' in famtypes(char) or self['statuses']['zombie'] == 100)


# ---- Status Iterators ---- #
def bool_statuses(char):
    """Return an iterator of active 'bool' (statuses with a value of 0 or 1)
    status names."""
    return iter(i for i in statgroups.BOOL_STATUSES if char['statuses'][i])

def active_statuses(char):
    """Return an iterator of currently active status names.
    (Has a value of at least 1)"""
    return iter(i for i in statgroups.ALL_STATUSES if char['statuses'][i] >= 1)

def inactive_statuses(char):
    """Return an iterator of currently inactive status names.
    (Has a value of 0)"""
    return iter(i for i in statgroups.ALL_STATUSES if char['statuses'][i] == 0)


# ---- Status getters ---- #
def is_deimmunized(char):
    """True if character has 'immunull' or 'immundown' status."""
    return (char['statuses']['immunull'] == 1 or
        char['statuses']['immundown'] >= 1)

def status_immunities(char):
    """Return an iterator of a character's current status immunities."""
    if is_deimmunized(char): return iter()
    for i in char['base'].status_immunities(): yield i

def elemental_immunities(char):
    """Return an iterator of currently active elemental immunities."""
    if is_deimmunized(char): return iter()
    for i in char['base'].elemental_immunities(): yield i


# ---- Calculated stat/status getters -------------------------------- #
def hp(char):
    """Health for this character."""
    return char['stats']['hp']

def phys_energy(char):
    """The current physical energy for this character."""
    return

def mental_energy(char):
    """The current mental energy for this character."""
    return
