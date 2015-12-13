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

from charflags import *
import charquery



# ---- Actions --------------------------------------------------------------- #
def get_status(char, s):
    """Return the uncalculated status value."""
    return char['statuses']['name']

def set_status(char, name, v):
    char['statuses'][name] = v

def _inc_stat(char, name, v=1):
    try: char['game-stats'][name] += v
    except: char['game-stats'][name] = v

# ---- *Forced* Actions (These must always succeed) -------------------------- #
def _clear_statuses(char):
    """Reset all status values to 0."""
    for i in char['statuses']: char['statuses'][i] = 0

def _clear_physical_statuses(char):
    pass

def _clear_mental_statuses(char):
    pass

def _clear_transform_statuses(char):
    pass

def _full_recovery(char):
    """Clear all statuses and restore health and energy."""
    _clear_statuses(char)
    char["phys-energy"] = 100
    char["mental-energy"] = 100
    char["health"] = 100

def _killchar(char, *flags):
    char['health'] = 0
    char['KO-flags'].append(CHARFLAGS[i] for i in flags)

    # remove revive-once flag if non-revivable KOType
    if any(i >= 200 for i in flags):
        char['KO-flags'].discard(CHARFLAGS['revive-once'])

# ---- Events ---------------------------------------------------------------- #
def update_char(char):
    if charquery.is_alive(char):    # ---- Alive ------------------------ #
        # status ko checks
        # TODO these should be done after each statuses is applied
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

    else:                           # ---- Char KO'd -------------------- #
        if not _has_spawn_timeout(char):
            if has_koflag(char, 'revive-once'):
                return _on_restore(char, revived=True)
        return

# ---- Post KO Query --------------------------------------------------------- #
def _has_spawn_timeout(char):
    try:
        if char['temp']['spawn-timeout'] > 0:
            char['temp']['spawn-timeout'] -= 1
            return True
        del char['temp']['spawn-timeout'] # delete if 0
        return False
    except: return False # no variable exists

# ---- post ko events -------------------------------------------------------- #
def _on_restore(char):
    """Called after restored or revived."""
    if charquery.has_koflag(char, 'revive-once'):
        if char['game-stats']: _inc_stat(char, 'revived') # increment revived stat
    if charquery.has_koflag(char, 'full-recover'): _full_recover(char)

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
