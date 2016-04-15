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

import cacc
from cacc import CharName
from charflags import *
from wallet import Wallet
from famtypes import FamTypeAccessor
import statgroups


# ---- Bio ------------------------------------------------------------------- #
def name(char):
    return CharName(char)

def age(char):
    return char['age']

def height(char):
    return

def weight(char):
    return


# ---- Equipment ------------------------------------------------------------- #
def handedness(char):
    """The handedness of this character.
    0: left    1: right    2: ambidextrious"""
    return char['handedness']

def is_barefoot(char):
    """True if char has no foot coverings."""
    if char['equip']:
        return True # TODO
    return True # no equipment

# ---- Health / Alive, etc. Query -------------------------------------------- #
def is_alive(char):
    """True if this character's hp is 0."""
    return char['stats']['hp'] != 0

def is_critical(char):
    """True if this character's hp is health is between 1 and 10 percent."""
    return 1 <= char['stats']['hp'] <= 10

def hp(char):
    """Health for this character."""
    return char['stats']['hp']

# ---- Specials
def is_revivable(char):
    """True if this character is in KO state and currently revivable.
    (must not have any unrevivable KO-FLAGs)"""
    if is_alive(char): return False
    return any(i for i in char['KO-flags'] if i >= MIN_NON_REVIVABLE_KOFLAG)

def has_koflag(char, flag):
    """True if char currently has given flag."""
    return CHARFLAGS[flag] in char['KO-flags']

def get_koflags(char):
    """Return an iterator of all current KO-FLAGS."""
    return CHARFLAGS[flag] in char['KO-flags']

# ---- Base Data Access & Query ---------------------------------------------- #
def base(char):
    """Access the base stats and other properties of this character."""
    return char['base']

# ---- Type Query ------------------------------------------------------------ #
def is_undead(char):
    """True if this character has a fam type of 'undead' or has 'zombie'
    status."""
    return ('undead' in famtypes(char) or char['statuses']['zombie'] == 100)

def famtypes(char):
    """Return an iterator of family types for this character starting with
    the primary type."""
    yield (i for i in char['base'].famtypes)


# ---- Status Query ---------------------------------------------------------- #
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

def is_deimmunized(char):
    """True if character has 'immunull' or 'immundown' status."""
    return (char['statuses']['immunull'] == 1 or
        char['statuses']['immundown'] >= 1)

def status_immunities(char):
    """Return an iterator of a character's current status immunities."""
    if is_deimmunized(char): yield
    else:
        for i in char['base'].status_immunities(): yield i

def elemental_immunities(char):
    """Return an iterator of currently active elemental immunities."""
    if is_deimmunized(char): yield
    else:
        for i in char['base'].elemental_immunities(): yield i


# ---- Calculated stat/status getters ---------------------------------------- #
def phys_energy(char):
    """The current physical energy for this character."""
    return

def mental_energy(char):
    """The current mental energy for this character."""
    return
