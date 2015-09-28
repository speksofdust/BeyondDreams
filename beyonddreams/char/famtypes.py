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

from statgroups import statgroups


class FamTypeData(tuple):
    def __init__(self, primary, secondaries=(), auxillaries=(), classifiers=()):
        self = (primary,) + tuple(secondaries) + tuple(auxillaries) + tuple(classifiers)

    def primary:
        return self[0]

    def secondaries(self):
        return iter(i for i in self[1:] if i._famorder == 1)

    def auxillaries(self):
        return iter(i for i in self[1:] if i._famorder == 2)

    def classifiers(self):
        return iter(i for i in self[1:] if i._famorder >= -1)


class FamType:
    name = ""
    desc = ""
    def __init__(self):
        pass


class _FamType(FamType, dict):
    def __init__(self):
        self._immunities = ()
        self = {
            # status effects
            "frostbite":    0,
            "burn":         0,
            "numb":         0,
            "stun":         0,
            "paralysis":    0,
            "poisoing":     0,
            "bleed":        0,
            "blind":        0,
            "drunk":        0,
            "dumb":         0,
            "confusion":    0,
            "undead":       0,
            "mutagen":      0,

            # Non-Elemental
            "acid":         0,
            "psychic":      0,
            "spirit":       0,

            # Elemental
            "dark":         0,
            "light":        0,
            "fire":         0,
            "ice":          0,
            "water":        0,
            "wind":         0,
            "electric":     0,

            # Groups
            "physical":         0,  # any physical
            "non-physical"      0,  # any non-physical (spirit, psychic, etc.)
            "elemental":        0,  # any elemental
            "non-elemental":    0,  # any non-elemental
            "transform":        0,  # any transform
            "animal-transform": 0,  # transform into any animal
            }

    def altered(self):
        for i in self._immunities: yield i
        for i in self:
            if self[i] != 0: yield i

    def unaltered(self):
        return iter(i for i in self if self[i] == 0)

    def immunities(self):
        return iter(self._immunities)

    def strengths(self):
        return iter(i for i in self if self[i] > 0)

    def weaknesses(self):
        return iter(i for i in self if self[i] < 0)


    def _get_sgval(name, s=0):
        for key in statgroups:
            if name in statgroups[key]:
                if self[key] in self._immunities: return "immune"
                else: s+= self[key]
        return s + self[name]

    def _get_value(self, name):
        if name in self._immunities:    return "immune"
        else: return self._get_sgval(name)


class PrimaryFam(_FamType):
    _famorder = 0

class SecondaryFam(_FamType):
    _famorder = 1

class AuxillaryFam(FamType):
    _famorder = 2


# ---- Primaries -- (char can be only one) ----------------------------------- #
class Reptile(PrimaryFam):
    _name = "reptile"
    def __init__(self):
        self["ice"] =       -15
        self["paralysis"] = 10


class Insect(PrimaryFam):
    _name = "insect"
    def __init__(self):
        self["ice"] =       -5
        self["fire"] =      -5
        self["poison"] =    -10


class Beast(PrimaryFam):
    _name = "beast"
    def __init__(self):
        self["fire"] =      -5
        self["poison"] =    -5
        self["acid"] =      -10
        self["mutagen"] =   -10


class Plant(PrimaryFam):
    _name = "plant"
    def __init__(self):
        self["fire"] =      -15
        self["ice"] =       -20
        self["water"] =     40


class Mechanical(PrimaryFam):
    _name = "mechanical"
    def __init__(self):
        self._immunities =  ("poison", "frostbite", "burn", "dumb", "confusion",
            "stun", "paralysis", "bleed", "numb")
        self["electric"] =  -10
        self["water"] =     -10


class Goo(PrimaryFam):
    _name = "goo"
    def __init__(self):
        self._immunities =  ("frostbite", "burn", "paralysis", "bleed")
        self["water"] =     20
        self["physical"] =  200 # physical attack need more exclusive value


# ---- Secondaries -- (char can be multiple as long as compatible) ----------- #
class Poison(SecondaryFam):
    _name = "poison"
    def __init__(self):
        self._immunities =  ("poison",)


class Aquatic(SecondaryFam):
    _name = "aquatic"
    def __init__(self):
        self._immunities =  ("water",)
        self["mutagen"] =   -5
        self["electric"] =  -15


class Spirit(SecondaryFam):
    _name = "spirit"
    def __init__(self):
        self._immunities =  ('physical', "poison", "acid", "frostbite", "burn",
            "mutagen", "paralysis", "bleed")
        self["psychic"] =   -10


class Undead(SecondaryFam):
    _name = "undead"
    def __init__(self):
        self._immunities =  ('zombie',)
        self["fire"] =      -5
        self["heal"] =      -10
        self["ice"] =       10
        self["mutagen"] =   20


class Demon(SecondaryFam):
    _name = "demon"
    def __init__(self):
        self._strengths =   ("mutagen")
        self["mutagen"] =   50


class Fae(SecondaryFam):
    _name = "fae"
    def __init__(self):
        self._immunities =  ()
        self["poison"] =    -25
        self["acid"] =      -25
        self["mutagen"] =   -25
        self["animal-transform"] = 10


# ---- Auxillaries -- (char can be multiple as long as compatible) ----------- #



class FamTypes(dict):
    def __init__(self):
        self = {
            'reptile':          Reptile(),
            'poison':           Poison(),
            'spirit':           Spirit(),
            'psychic':          Psychic(),
            'undead':           Undead(),
            "demon":            Demon(),
            'fae':              Fae()
            }

    def primaries(self):
        return iter(i for i in self if i._famorder == 0)

    def secondaries(self):
        return iter(i for i in self if i._famorder == 1)

    def auxillaries(self):
        return iter(i for i in self if i._famorder == 2


# ---- Type Classifiers -- (pick one of each as applicable) --------------------------- #
class TypeClassifier:
    _classifier_name = ""
    def __init__(self, name, desc=""):
        self.name = name
        self.desc = desc


class EvolutionTC(TypeClassifier):
    classifier_name = "evolution"

class StanceTC(TypeClassifier):
    classifier_name = "stance"


class _TCD(Tuple):
    __slots__ = ()
    def __init__(self, items):
        self = items

    def __getitem__(self, i):
        if isinstance(i, int): return self._keys(i)
        elif: try: return self[i]
        else: raise KeyError

    def __iadd__(self): raise NotImplementedError

    def keys(self):
        return iter(i._name for i in self)

    @property
    def classifier_name(self):
        return self[0]._classifier_name


class _TCDSS:
    evolution = _TCD("evolution", items=(
                        EvolutionTC("primative"),
                        EvolutionTC("non-primative")
                        )
    stance =    _TCD("stance", items(
                        StanceTC("biped"),
                        StanceTC("quadruped"),
                        StanceTC("other"),
                        )

    def _gettc_by_idx(self, tcd_name, i):
        return self.__dict__[tcdname].keys()[i]

