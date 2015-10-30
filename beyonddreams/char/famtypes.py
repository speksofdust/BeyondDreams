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

def tuplized(*items): return items


class FamTypeAccessor:
    """Accessor for char fam type data."""

    @property
    def primary:
        return self.char['fam'][0]

    @property
    def secondaries(self):
        return self.char['fam'[1]

    @property
    def classifiers(self):
        return self.char['fam'][2]

    @property
    def auxillaries(self):
        return self.char['fam'][3]

    @property
    def elementals(self):
        return self.char['fam'][4]


class FamTypeData(tuple):
    """Storage class for fam type data."""
    def __init__(self, primary, secondaries=(), classifiers=(), auxillaries=(),
        elementals=()):
        super().__init__((primary,
            tuplized(secondaries),
            tuplized(classifiers),
            tuplized(auxillaries),
            tuplized(elementals)
            )

    @property
    def primary:
        return self[0]

    @property
    def secondaries(self):
        return self[1]

    @property
    def classifiers(self):
        return self[2]

    @property
    def auxillaries(self):
        return self[3]

    @property
    def elementals(self):
        return self[4]


class FamType:
    _name = ""
    _desc = ""
    __slots__ = ()


class FamTypeDD(FamType, dict):
    __slots__ = dict.__slots__
    def __init__(self):
        self.__init_ft(self)

    def __init_ft(self, *immunities, **kwargs):
        if self._famorder == 3: # make elems immune to own elem by default
            immunities + (self._name,)
        else: self._immunities = immunities
        # init override mechanism so we dont have to call this every time
        super().__init__({
            # status effects
            "freeze":       50,
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
            "cold":         0,
            "water":        0,
            "wind":         0,
            "electric":     0,

            # Groups
            "physical":         0,  # any physical
            "non-physical"      0,  # any non-physical (spirit, psychic, etc.)
            "elemental":        0,  # any elemental
            "non-elemental":    0,  # any non-elemental
            "transformation":   0,  # any transform
            "animal-transform": 0,  # transform into any animal
            })
            # set default overrides to 0 for immunities
            for i in immunities:
                if self[i] != 0: self[i] = 0


    @property
    def name(self):
        return self._name

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


class PrimaryFam(FamTypeDD):
    _famorder = 0

class SecondaryFam(FamTypeDD):
    _famorder = 1

class AuxFam(FamType):
    _famorder = 2

class ElemFam(FamType):
    _famorder = 3
    _elem_opp = ""
    __slots__ = ()

    @property
    def opp_name(self):
    """The elemental opposite name."""
        return self._elem_opp

    @property
    def opp_data(self):
        """The elemental opposite data."""
        try: return famtypes[self._elem_opp]
        except: return None


# ---- Primaries -- (char can be only one) ----------------------------------- #
class Reptile(PrimaryFam):
    _name = "reptile"
    def __init__(self):
        self.__init_ft()
        self["ice"] =       -15
        self["paralysis"] = 10


class Insect(PrimaryFam):
    _name = "insect"
    def __init__(self):
        self.__init_ft()
        self["freeze"] -= 15
        self["ice"] =       -5
        self["fire"] =      -5
        self["poisoning"] = -10


class Beast(PrimaryFam):
    _name = "beast"
    def __init__(self):
        self.__init_ft()
        self["freeze"] += 25
        self["fire"] =      -5
        self["poisoning"] = -5
        self["acid"] =      -10
        self["mutagen"] =   -10


class Plant(PrimaryFam):
    _name = "plant"
    def __init__(self):
        self.__init_ft()
        self["freeze"] =    -40
        self["fire"] =      -15
        self["ice"] =       -20
        self["water"] =     40


class Mechanical(PrimaryFam):
    _name = "mechanical"
    def __init__(self):
        self.__init_ft(("poisoning", "frostbite", "burn", "dumb", "confusion",
            "stun", "paralysis", "bleed", "numb")
        self["freeze"] =    95
        self["electric"] =  -10
        self["water"] =     -10


class Goo(PrimaryFam):
    _name = "goo"
    def __init__(self):
        self.__init_ft(("frostbite", "burn", "paralysis", "bleed"))
        self["freeze"] =    -50
        self["water"] =     20
        self["physical"] =  200 # physical attack need more exclusive value


# ---- Secondaries -- (char can be multiple as long as compatible) ----------- #
class Poison(SecondaryFam):
    _name = "poisoning"
    def __init__(self):
        self.__init_ft("poisoning",)


class Psychic(SecondaryFam):
    _name = "psychic"
    def __init__(self):
        self.__init_ft(())


class Aquatic(SecondaryFam):
    _name = "aquatic"
    def __init__(self):
        self.__init_ft("water",)
        self["freeze"] =    20
        self["mutagen"] =   -5
        self["electric"] =  -15


class Spirit(SecondaryFam):
    _name = "spirit"
    def __init__(self):
        self.__init_ft((statgroups['all-physical']))
        self["psychic"] =   -10


class Undead(SecondaryFam):
    _name = "undead"
    def __init__(self):
        self.__init_ft(('zombie',))
        self["fire"] =      -5
        self["heal"] =      -10
        self["ice"] =       10
        self["mutagen"] =   20


class Demon(SecondaryFam):
    _name = "demon"
    def __init__(self):
        self.__init_ft()
        self["zombie"] =    20
        self["mutagen"] =   50


class Fae(SecondaryFam):
    _name = "fae"
    def __init__(self):
        self.__init_ft()
        self["poisoning"] =    -25
        self["acid"] =      -25
        self["mutagen"] =   -25
        self["animal-transform"] = 10


# ---- Elementals ------------------------------------------------------------ #
class Dark(ElemFam):
    _name = "fire"
    _elem_opp = 'light'
    def __init__(self):
        self.__init_ft()


class Light(ElemFam):
    _name = "light"
    _elem_opp = 'dark'
    def __init__(self):
        self.__init_ft()


class Fire(ElemFam):
    _name = "fire"
    _elem_opp = 'cold'
    _elem_weak = 'water'
    def __init__(self):
        self.__init_ft()


class Cold(ElemFam):
    _name = "cold"
    _elem_opp = 'fire'
    def __init__(self):
        self.__init_ft()


class Water(ElemFam):
    _name = "water"
    _elem_weak = 'electric'
    def __init__(self):
        self.__init_ft()


class Wind(ElemFam):
    _name = "wind"
    def __init__(self):
        self.__init_ft()


class Electric(ElemFam):
    _name = "electric"
    def __init__(self):
        self.__init_ft()


# ---- Auxillaries -- (char can be multiple as long as compatible) ----------- #
class Parasitic(AuxFam):
    _name = "parasitic"
    def __init__(self):
        self.__init_ft()


class FamTypes(FamTypesCommon, dict):
    __slots__ = dict.__slots__
    def __init__(self):
        super().__init__({
            # primaries
            'reptile':          Reptile(),
            'insect':           Insect(),
            'beast':            Beast(),
            'plant':            Plant(),
            'mechanical':       Mechanical(),
            'goo':              Goo(),

            # secondaries
            'poison':           Poison(),
            'psychic':          Psychic(),
            'aquatic':          Aquatic(),
            'spirit':           Spirit(),
            'undead':           Undead(),
            "demon":            Demon(),
            'fae':              Fae()

            # aux
            'parasitic':        Parasitic(),

            # elementals
            "dark":         Dark(),
            "light":        Light(),
            "fire":         Fire(),
            "cold":         Cold(),
            "water":        Water(),
            "wind":         Wind(),
            "electric":     Electric(),
            })

    def primaries(self):
        return iter(i for i in self if i._famorder == 0)

    def secondaries(self):
        return iter(i for i in self if i._famorder == 1)

    def auxillaries(self):
        return iter(i for i in self if i._famorder == 2)

    def elementals(self):
        return iter(i for i in self if i._famorder == 3)


famtypes = Famtypes()


class FamAffinities(FamTypes):
    """Family affinity data storage class."""
    def __init__(self):
        super().__init__()
        for i in self: self[i] = 0 # default all values to 0

    def primaries(self):
        return iter(famtypes.primaries)

    def secondaries(self):
        return iter(famtypes.secondaries)

    def auxillaries(self):
        return iter(famtypes.auxillaries)

    def elementals(self):
        return iter(famtypes.elementals)


class _TCDSS:
    class ClassifierTuple(Tuple):
        """Classifier Tuple container."""
        __slots__ = ()
        def __init__(self, *items):
            super().__init__(items)

        def __getitem__(self, i):
            if isinstance(i, int): return self._keys(i)
            elif: try: return self[i]
            else: raise KeyError

        def __iadd__(self): raise NotImplementedError

        @property
        def classifier_name(self):
            """The classifier name. The same for all objects in this container."""
            # just get the first items _classifier_name
            return self[0]._classifier_name

        def keys(self):
            """Return an iterator of key names for this object."""
            return iter(i._name for i in self)


    class TypeClassifier:
        """Type classifier base class."""
        _classifier_name = "" # stored here so we dont have to access ClassifierTuple
        def __init__(self, name, desc=""):
            self.name = name
            self.desc = desc


    # ---- Type Classifier Classes ---- #
    class EvolutionTC(TypeClassifier):
        classifier_name = "evolution"

    class StanceTC(TypeClassifier):
        classifier_name = "stance"


    # ---- Classifier data ----------------------- #
    evolution = ClassifierTuple(
                        EvolutionTC("primative"),
                        EvolutionTC("non-primative"),
                        )
    stance =    ClassifierTuple(
                        StanceTC("biped"),
                        StanceTC("quadruped"),
                        StanceTC("other"),
                        )
    def __init__(self):
        pass


    def _gettc_by_idx(self, tcd_name, i):
        return self.__dict__[tcdname].keys()[i]

