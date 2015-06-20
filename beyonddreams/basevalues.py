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


__all__ = 'base_def_stats_mult', 'base_stats_mult'

# Multipliers
base_stat_def_mult = {
    # Elemental
    'water':    1,
    'wind':     1,
    'ice':      1,
    'elec':     1,
    'fire':     1,
    'dark':     1,
    'light':    1,

    # Non-Elemental
    'psychic':  1,
    'spirit':   1,
    'undead':   1,
    'radia':    1,
    'mag':      1,
    'acid':     1,
}

base_status_mult = {
    'burn':         1,
    'frostbite':    1,
    'poisoned':     1,
    'drunk':        1,
    'blind':        1,
    'numb':         1,
    'zombie':       1,

}


base_stats_mult = {
    'intellect':    1,
    'stamina':      1,
    'strength':     1,
    'willpower':    1,
    'luck':         1,

    'focus':        1,
}

# Absolute minimum and maximum for stats
stats_abs_range = {
    # Levels change with equip, skill, etc. changes.
    'intellect':    (1, 200),
    'stamina':      (0, 200),
    'strength':     (1, 200),
    'willpower':    (0, 200),
    'agility':      (1, 100),
    'luck':         (-1000, 1000),
    'karma':        (-1000, 1000),

    # Frequently Varying Levels
    'focus':            (0, 200),
    'phys-energy':      (0, 200),
    'mental-energy':    (0, 200),
    'health':           (0, 200),
}

# stamina - determines phy-energy loss rate
# strength - maximum current strength value possible (real is calculated with
#   current physical energy)
