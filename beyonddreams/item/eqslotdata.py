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

# classifiers
ARM = "armor"
CLO = "clothing"
TOP = "tops"
BTM = "Bottoms"
UND = "undies"
SWM = "swimwear"
JEW = "jewelry",
ACC = "accessories"
FTW = "footwear"
HDW = "headwear"
NEK = "neckwear"
BOD = "bodysuit"
GLV = "glove"


class _EqSlotData:
    __slots__ = "_name", "_layers", "_linking",
    def __init__(self, name, layers=0):
        self.name = name
        self._layers = layers   # expiremental
        self._linking = 0   # always 0 for the basic type
        self._tags =

    @property
    def layers(self):
        """The max layer index or 0 if layers are unsupported."""
        return self._layers

    #@property
    #def fullnames(self):
    #    """A tuple of all the full names of this slot."""
    #    return (self._name,)

    @property
    def linking(self):
        """Whether linking is allowed. (0 - False, 1 - optional, 2 - required)"""
        return self._linking

    @property
    def plural_name(self):
        """The plural name of this slot."""
        if self._name not in EQUIPSLOTS._noplural: return self._name
        return "".join(self._name, 's')


class _EqSlotDataLR(EqSlot):
    """Slot data type for left and right slot pairs."""
    __slots__ = EqSlot.__slots__
    def __init__(self, name, layers=1, linking=1):
        self.name = name
        self._linking = linking

    @property
    def opp_name(self):
        if self.name.endswith("L"): return "".join(self.name[:-1], "R")
        return "".join(self.name[:-1], "L")

    #@property
    #def fullnames(self):
    #    return "".join(name, '.R'), "".join(name, '.L')


class _EqSlots(dict):
    _noplural = (HDW, FTW, BTM, TOP, NEK)
    __slots__ = dict.__slots__
    def __init__(self):
        self = {
            # LR - no linking
            'ankle.L':          _EqSlotDataLR('ankle.L',    3, 0),
            'ankle.R':          _EqSlotDataLR('ankle.R',    3, 0),
            'wrist.L':          _EqSlotDataLR('wrist.L',    3, 0),
            'wrist.R':          _EqSlotDataLR('wrist.R',    3, 0),
            'thigh.L':          _EqSlotDataLR('thigh.L',    3, 0),
            'thigh.R':          _EqSlotDataLR('thigh.R',    3, 0),
            # LR - linking
            'sock.L':           _EqSlotDataLR('sock.L',     1, 1),
            'sock.R':           _EqSlotDataLR('sock.R',     1, 1),
            'glove.L':          _EqSlotDataLR('glove.L',    1, 1),
            'glove.R':          _EqSlotDataLR('glove.R',    1, 1),
            # Normal
            'headwear':         _EqSlotData(HDW             0),
            'tops':             _EqSlotData(TOP,            2),
            'bottoms':          _EqSlotData(BOT,            2),
            'undies-top':       _EqSlotData('undies-top',   0),
            'undies-bottom':    _EqSlotData('undies-bottom' 0),
            # Normal - misc
            'glasses':          _EqSlotData('glasses',  0),
            'belt':             _EqSlotData('belt',     0),
            }


EQUIPSLOTS = _EQSlots()


