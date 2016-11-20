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

class StatMeta(MetaDataBaseCls):
    __slots__ = MetaDataBaseCls.__slots__ + 'abbr', 'min', 'max'
    def __init__(self, name, abbr, min=0, max=100, desc="", **kwargs):
        super().__init__(name, desc, *args, **kwargs)
        if abbr is None: self.abbr = self.name
        else: self.abbr = abbr
        self.min = 0
        self.max = 100
        try: self._hidden = kwargs['hidden']
        except: self._hidden = False


class Stat:
    def __init__(self, name, abbr, min=0, max=100):
        self.name =  name
        if abbr is None: self.abbr = self.name
        else: self.abbr = abbr
        self.min =   0
        self.max =   100

    def clamped(self, v):
        if v <= self.min: return self.min
        if v >= self.max: return self.max
        return v


class _PStat(Stat):
    _stattype = "physical"


class _MStat(Stat):
    _stattype = "mental"


class _Hidden(Stat):
    pass


class _Energy():
    def __init__(self, name, abbr, min=0, max=200):
        Stat.__init__(self, name, abbr, min, max)


class _PEnergy(_PStat, _Energy):
    pass


class _MEnergy(_MStat, _Energy):
    pass


class _Stam():
    def __init__(self, name, abbr, min=0, max=200):
        Stat.__init__(self, name, abbr, min, max)


class _PStam(_PStat, _Stam):
    pass


class _MStam(_MStat, _Stam):
    pass


class _Health(_EnergyStat):
    def __init__(self, name, abbr, min=0, max=200):
        Stat.__init__(self, name, abbr, min, max)


class _StatConst(dict):
    def __init__(self):
        super().__init__({
            # physical
            "p-stamina":    meta("physical-stamina",
                                abbr="p-stam",
                                subcats='physical',
                                desc="",
                                ),
            "p-energy":     _PEnergy("physical-energy",
                                abbr="p-nrg",
                                ),
            "strength":     Stat("strength",
                                "str",
                                min=1,
                                max=200,
                                desc="",
                                ),
            "agility":      Stat("agility",
                                abbr="agil",
                                min=1,
                                desc=""
                                ),

            # mental
            "m-stamina":    _MStam("mental-stamina",
                                "m-stam",
                                ),
            "m-energy":     _MEnergy("mental-energy", "m-energy"),
            "focus":        Stat("focus", "foc", 1, 200),
            "intellect":    Stat("intellect", "int", 1, 200),
            "willpower":    Stat("willpower", "will", 0, 200),

            "health":       _Health("health", "hp"),
            "karma":        _Hidden("karma", None, -1000, 1000),
            "luck":         Stat("luck", None, -1000, 1000),
            "adrenaline":   Stat("adrenaline", "adr", 0),
            "rage":         Stat("rage", None, -100),
            })

    def __getitem__(self, i):
        try: return self[i]
        except:
            for i in self:
                if (self[i].name or self[i].abbr) == i: return self[i]
            raise KeyError

    def __contains__(self, i):
        try: return i in self
        except:
            for i in self:
                if (self[i].name or self[i].abbr) == i: return True
            return False

    def get_clamped(self, name, v):
        return self.__getitem__(name).clamped(v)


# Statuses
PHYSICAL_STATUSES = ("freeze", "frostbite", 'burn', 'numb', 'stun', 'poisoning',
    'bleed')
BOOL_STATUSES = 'freeze', 'immunnull'
MENTAL_STATUSES = 'blind', 'drunk', 'dumb', 'confusion'
XFORM_STATUSES = 'undead', 'mutagen'
ALL_STATUSES = (BOOL_STATUSES + PHYSICAL_STATUSES[1:] + MENTAL_STATUSES +
    XFORM_STATUSES)

ELEMENTALS = 'dark', 'light', 'fire', 'cold', 'water', 'wind', 'electric'
NON_ELEMENTALS = 'psychic', 'spirit', 'acid'
PHYSICAL = () + ELEMENTALS[2:] + NON_ELEMENTALS[2:]
NON_PHYSICAL = () + ELEMENTALS[:2] + NON_ELEMENTALS[:2]



statgroups = _Statgroups()
statconst = _StatConst()

__all__ = ('stat_def_basemult', 'status_basemult', 'stats_basemult',
    'stats_abs_range', "statgroups", "statconst")
