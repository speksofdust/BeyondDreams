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


__all__ = ('stat_def_basemult', 'status_basemult', 'stats_basemult',
    'stats_abs_range')

# Multipliers
stat_def_basemult = {
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

status_basemult = {
    'burn':         1,
    'frostbite':    1,
    'poisoned':     1,
    'drunk':        1,
    'blind':        1,
    'numb':         1,
    'zombie':       1,
}

stats_basemult = {
    'intellect':    1,
    'stamina':      1,
    'strength':     1,
    'willpower':    1,
    'luck':         1,
    'focus':        1,
}

class StatsAbsRange(dict):
    def __init__(self, items):
        self = items

    def get_clamped(self, name, val):
        if self[name][0] <= val: return self[name][0]
        elif self[name][1] >= val: return self[name][1]
        else: return val


# Absolute minimum and maximum for stats
stats_abs_range = StatsAbsRange(
    {
    # Levels change with equip, skill, etc. changes.
    'phys-stamina':     (0, 200),
    'mental-stamina':   (0, 200),
    'intellect':        (1, 200),
    'strength':         (1, 200),
    'willpower':        (0, 200),
    'agility':          (1, 100),
    'luck':             (-1000, 1000),

    # hidden stats
    'karma':            (-1000, 1000),
    'adrenaline':       (0, 100),
    'rage':             (-100, 100),

    # Frequently Varying Levels
    'focus':            (0, 200),
    'phys-energy':      (0, 200),
    'mental-energy':    (0, 200),
    'health':           (0, 200),
    })


# rage - > 0 increases strength but uses more phys-energy < 0 does the opposite

def calc_energy(c, energy):
    # energy + (adrenaline * 0.02) + (rage * 0.02)
    return  (c[stats][energy] + (c[stats]['adrenaline'] * 0.02) +
        (c[stats]['rage'] * 0.02))

def calc_focus(c):
    # focus * (mental-energy + (adrenaline * 0.02) + (rage * 0.02))
    return stats_abs_range.clamped('focus',
        c[stats]['focus'] * calc_energy(c, 'mental-energy'))

def calc_strength(c):
    # strength * (phys-energy + (adrenaline * 0.02) + (rage * 0.02))
    return stats_abs_range.clamped('strength',
        c[stats]["strength"] * calc_energy(c, "phys-energy"))

