# ---------------------------------------------------------------------------- #
#                                                                              #
#     This program is free software: you can redistribute it and/or modify     #
#     it under the terms of the GNU General Public Lcoldnse as published by     #
#     the Free Software Foundation, either version 3 of the Lcoldnse, or        #
#     (at your option) any later version.                                      #
#                                                                              #
#     This program is distributed in the hope that it will be useful,          #
#     but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the             #
#     GNU General Public Lcoldnse for more details.                             #
#                                                                              #
#     You should have received a copy of the GNU General Public Lcoldnse        #
#     along with this program. If not, see <http://www.gnu.org/lcoldnses/>.     #
#                                                                              #
# ---------------------------------------------------------------------------- #

#from xsquare.utils.iterutils import tupilize

from statgroups import statgroups


PRIMARY_FAMS = "reptile", "insect", "beast", "plant", "mechanical", "goo"
SECONDARY_FAMS = "poison", "psychic", "aquatic", "sqirit", "undead", "demon", "fae"
AUX_FAMS = ("parasitic",)
ELEMENTALS = "dark", "light", "fire", "cold", "water", "wind", "electric"


def tuplize(*args): return args


class FamTypeData(tuple):
    __slots__ = tuple.__slots__
    """Storage class for fam type data."""
    def __init__(self, primary, secondaries=(), classifiers=(), auxillaries=(),
        elementals=()):
        super().__init__((primary,
            tuplize(secondaries),
            tuplize(classifiers),
            tuplize(auxillaries),
            tuplize(elementals)
            ))

    @property
    def primary(self):
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

    def immunities(self):
        """Return an iterator of all combined immunities."""
        return iter(set(i.immunities() for i in chain.from_iterable(self)))

    def status_immunities(self):
        """Return an iterator of all combined status immunities."""
        return iter(i for i in self.immunities if i in statgroups.ALL_STATUSES)

    def elemental_immunities(self):
        """Return an iterator of all combined elemental immunities."""
        return iter(i for i in self.immunities if i in statgroups.ELEMENTALS)

    def _sum_res(self, i, name):
        try: return sum(self[i][name] // len(self[i][name]))
        except: return 0

    def _calc_resistance(self, name):
        c = 0 # valid count
        x = 0 # valid sum
        # valid only if not 0 from each subtype (primary, secodary, etc.)
        # avg of x (valid sum) divided by c (valid count)
        # this prevents skewed results from always dividing by 5 which we dont want
        if self[0][name] > 0:   # check primary
            c += 1
            x = self[0][name]
        for i in range(1,5):    # check secondary, and so on
            self._sum_res(i, name)
            if n > 0:
                c += 1
                x += n
        try: return x // c
        except: return 0


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
            self[self._name] = 100
        else: self._immunities = immunities
        # init override mechanism so we dont have to call this every time
        super().__init__({
            # status effects
            "frozen":       50,
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

            # specials
            "immunull":     0,
            "immundown":    0,

            # Group type bonuses
            "physical":         0,  # any physical
            "non-physical":     0,  # any non-physical (spirit, psychic, etc.)
            "elemental":        0,  # any elemental
            "non-elemental":    0,  # any non-elemental
            "any-transform":    0,  # any transform
            "animal-transform": 0,  # transform into any animal
            })
            # set default overrides to 100 for immunities
        for i in immunities: self[i] = 100

    @property
    def desc(self): return self.__doc__

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
    _compatable_types = () # compatable primary family types

class AuxFam(FamType):
    _famorder = 2

class ElemFam(FamType):
    _famorder = 3
    _elem_opp = ""
    _associated_status = ""
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

    def associated_status(self):
        """Status effect that may be added in conjunction with an attack of this elemental type."""
        return self._associated_status

    def has_opposite(self): return bool(self._elem_opp)


# ---- Primaries -- (char can be only one) ----------------------------------- #
class Reptile(PrimaryFam):
    _name = "reptile"
    def __init__(self):
        self.__init_ft()
        self["cold"] =       -15
        self["paralysis"] = 10
        self["acid"] = 10


class Insect(PrimaryFam):
    _name = "insect"
    def __init__(self):
        self.__init_ft()
        self["frozen"] -= 15
        self["cold"] =       -5
        self["fire"] =      -5
        self["poisoning"] = -10


class Beast(PrimaryFam):
    _name = "beast"
    def __init__(self):
        self.__init_ft()
        self["frozen"] += 25
        self["fire"] =      -5
        self["poisoning"] = -5
        self["acid"] =      -10
        self["mutagen"] =   -10


class Plant(PrimaryFam):
    _name = "plant"
    def __init__(self):
        self.__init_ft(("paralysis", "dumb", "confusion", "blind"))
        self["frozen"] =    -40
        self["fire"] =      -15
        self["cold"] =      -50
        self["water"] =     50


class Mechanical(PrimaryFam):
    _name = "mechanical"
    def __init__(self):
        self.__init_ft(("poisoning", "frostbite", "burn", "dumb", "confusion",
            "stun", "paralysis", "bleed", "numb", "mutagen"))
        self["frozen"] =    95
        self["electric"] =  -50
        self["water"] =     -10


class Inorganic(PrimaryFam):
    _name = "inorganic"
    def __init__(self):
        self.__init_ft(("poisioning", "frostbite", "burn", "dumb", "confusion",
            "stun", "paralysis", "bleed", "numb", "mutagen"))
        self["frozen"] = 95


class Goo(PrimaryFam):
    _name = "goo"
    def __init__(self):
        self.__init_ft(("frostbite", "burn", "paralysis", "bleed"))
        self["frozen"] =    -50
        self["water"] =     20
        self["physical"] =  200 # physical attack need more exclusive value
        self["psychic"] = 25


# ---- Secondaries -- (char can be multiple as long as compatible) ----------- #
class BioMechanical(SecondaryFam):
    _compatable_types = Reptile, Insect, Beast
    _name = "bio mechanical"
    def __init__(self):
        self.__init_ft(())
        self["electric"] = -50


class Poison(SecondaryFam):
    _compatable_types = Reptile, Insect, Beast, Plant, Goo
    _name = "poison"
    def __init__(self):
        self.__init_ft("poisoning",)


class Psychic(SecondaryFam):
    _compatable_types = Reptile, Insect, Beast, Plant, Goo
    _name = "psychic"
    def __init__(self):
        self.__init_ft(())
        self["psychic"] = 25


class Aquatic(SecondaryFam):
    _compatable_types = Reptile, Insect, Beast, Plant, Goo
    _name = "aquatic"
    def __init__(self):
        self.__init_ft("water",)
        self["frozen"] =    20
        self["mutagen"] =   -10
        self["electric"] =  -50


class Spirit(SecondaryFam):
    _compatable_types = Reptile, Insect, Beast, Goo
    _name = "spirit"
    # Note Spirit attacks work one way unless both entities are on the spirit plane
    #   Spirit type can attack but can only be affected by spirit attacks from
    #   other planes
    def __init__(self):
        self.__init_ft((statgroups['all-physical']))
        self["psychic"] =   -10


class Undead(SecondaryFam):
    _compatable_types = Reptile, Insect, Beast, Plant, Goo
    _name = "undead"
    def __init__(self):
        self.__init_ft(('undead',))
        self["fire"] =      -25
        self["heal"] =      -25
        self["cold"] =       10
        self["mutagen"] =   50


class Demon(SecondaryFam):
    _compatable_types = Reptile, Insect, Beast, Plant, Goo
    _name = "demon"
    def __init__(self):
        self.__init_ft()
        self["undead"] =    20
        self["mutagen"] =   50


class Fae(SecondaryFam):
    _compatable_types = Reptile, Insect, Beast, Plant, Goo
    _name = "fae"
    def __init__(self):
        self.__init_ft()
        self["poisoning"] =    -25
        self["acid"] =      -25
        self["mutagen"] =   -25
        self["animal-transform"] = 10


# ---- Elementals ------------------------------------------------------------ #
class Dark(ElemFam):
    _name = "dark"
    _elem_opp = "light"
    _associated_status
    def __init__(self):
        self.__init_ft()


class Light(ElemFam):
    _name = "light"
    _elem_opp = "dark"
    _associated_status = "blind"
    def __init__(self):
        self.__init_ft()
        self["blind"] = 50 # associated status
        self["dark"] = -50 # elem opp


class Fire(ElemFam):
    _name = "fire"
    _elem_opp = "water"
    _associated_status = "burn"
    def __init__(self):
        self.__init_ft()
        self["burn"] = 50   # associated status
        self["water"] = -50 # elem opp
        self["cold"] = -25  # weak-ish


class Cold(ElemFam):
    _name = "cold"
    _associated_status = "frostbite"
    def __init__(self):
        self.__init_ft()
        self["frostbite"] = 50 # associated status
        self["fire"] = -50  # weak


class Water(ElemFam):
    _name = "water"
    _elem_opp = "fire"
    #_associated_status = ""
    def __init__(self):
        self.__init_ft()
        self["fire"] = -50 # elem opp
        self["electric"] = -50 # weak


class Wind(ElemFam):
    _name = "wind"
    #_associated_status = ""
    def __init__(self):
        self.__init_ft()


class Electric(ElemFam):
    _name = "electric"
    _associated_status = "paralysis"
    def __init__(self):
        self.__init_ft()
        self["paralysis"] = 50 # elem opp


# ---- Auxillaries -- (char can be multiple as long as compatible) ----------- #
class Parasitic(AuxFam):
    """A creature that feeds off of other creatures."""
    _name = "parasitic"
    def __init__(self):
        self.__init_ft()


class Possessed(AuxFam):
    """A creature or object that has been taken control of by some other entity."""
    _name = "possessed"
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
            'fae':              Fae(),

            # aux
            'parasitic':        Parasitic(),
            'possessed':        Possessed(),

            # elementals
            "dark":         Dark(),
            "light":        Light(),
            "fire":         Fire(),
            "cold":         Cold(),
            "water":        Water(),
            "wind":         Wind(),
            "electric":     Electric(),
            })
        # Add elemental opposites
        self['dark']._elem_opp = Light
        self['dark']["light"] = -50

        self['light']._elem_opp = Dark
        self['light']["dark"] = -50

        self['fire']._elem_opp = Water
        self['fire']["water"] = -50

        self['water']._elem_opp = Fire
        self['water']["fire"] = -50



    def primaries(self):
        return iter(self.keys[i] for i in PRIMARY_FAMS)

    def secondaries(self):
        return iter(self.keys[i] for i in SECONDARY_FAMS)

    def auxillaries(self):
        return iter(self.keys[i] for i in AUX_FAMS)

    def elementals(self):
        return iter(self.keys[i] for i in ELEMENTALS)


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
            try: return self[i]
            except: raise KeyError

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

    class BodyTypeTC(TypeClassifier):
        classifier_name = "stance"


    # ---- Classifier data ----------------------- #
    evolution = ClassifierTuple(
                        EvolutionTC("primative",
                        "Incapable of making higher order decisions."
                            ),
                        EvolutionTC("non-primative",
                            "Capable of making higher order decisions."
                            ),
                        )
    stance =    ClassifierTuple(
                        BodyTypeTC("biped", "Creatures that walk on two legs."),
                        BodyTypeTC("quadruped", "Creatures that walk on four legs."),
                        BodyTypeTC("fish"),
                        BodyTypeTC("snake"),
                        BodyTypeTC("avian"),
                        )
    def __init__(self):
        pass

    def _gettc_by_idx(self, tcd_name, i):
        return self.__slots__[tcdname].keys()[i]

