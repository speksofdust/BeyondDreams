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

from bdobj import Sittable
from bdobj import Storage
from bdobj import BDObj
from bdobj import ObMeta

LAY =       100
SIT =       101
MOVE =      200 # move object
PICKUP =    201 # pickup object
SWITCH =    300 # switch on/off etc
OPENCLOSE = 388 # open/close door etc
PUSH =      389
PULL =      390

#placement
FLOOR =     0
WALL =      1
CEILING =   2
ON_OBJECT = 3

SEATING = "seating"
BEDDING = "bedding"
LIGHTING = "lighting"
DECORATIVE = "decorative"

class FurnMeta(ObMeta):
    ptype = "furnature"
    __slots__ = ObMeta.__slots__ + "base_interactions", "default_placement"
    def __init__(self, name, subcats=(), base_interactions=(), desc=""):
        super().__init__(name, subcats, desc)
        self._base_interactions = base_interactions


class Furnature(BDObj):
    _ob_type = 'furnature'
    _default_placement = FLOOR


# ---- Furnature types ------------------------------------------------------- #
class Bed(Furnature):
    meta = FurnMeta("bed",
        subcats=(BEDDING,),
        base_ias=(LAY, SIT, MOVE),
        desc=""
        )


class Chair(Furnature):
    meta = FurnMeta('chair',
        subcats=(SEATING,),
        base_ias=(SIT, MOVE),
        desc=""
        )


class Stool(Furnature):
    meta = FurnMeta('stool',
        subcats=(SEATING,),
        base_ias=(SIT, MOVE),
        desc=""
        )


class LoveSeat(Furnature):
    meta = FurnMeta('loveseat',
        subcats=(SEATING,),
        base_ias=(SIT, MOVE),
        desc=""
        )


class Couch(Furnature):
    meta = FurnMeta('couch',
        subcats=(SEATING,),
        base_ias=(LAY, SIT, MOVE),
        desc=""
        )


class Chest(Furnature):
    meta = FurnMeta('couch',
        subcats=(STORAGE,),
        base_ias=(SIT, OPENCLOSE, MOVE),
        desc="")
    _max_slots = 15


class Trunk(Furnature):
    meta = FurnMeta('couch',
        subcats=(STORAGE,),
        base_ias=(SIT, OPENCLOSE, MOVE),
        desc="")
    _max_slots = 20


class Dresser(Furnature):
    meta = FurnMeta('dresser',
        subcats=(STORAGE,),
        base_ias=(MOVE,),
        desc="")
    _max_slots = 15


class Table(Furnature):
    meta = FurnMeta('table',
        subcats=(),
        base_ias=(SIT, MOVE),
        desc="")


class Rug(Furnature):
    meta = FurnMeta('rug',
        subcats=(),
        base_ias=(SIT, LAY, MOVE),
        desc="")


class Frame(Furnature):
    meta = ObMeta("frame",
        subcats=(DECORATIVE),
        base_ias=(MOVE,),
        desc=""
        )
    _default_placement = WALL
    def __init__(self, image=None):
        self._image = image


class Lighting(Furnature):
    pass


class TableLamp(Lighting):
    meta = FurnMeta('floor lamp',
        subcats=(LIGHTING,),
        base_ias=(SWITCH, MOVE),
        desc=""
        )


class FloorLamp(Lighting):
    meta = FurnMeta('floor lamp',
        subcats=(LIGHTING,),
        base_ias=(SWITCH, MOVE),
        desc=""
        )

FURNISHING_TYPES = {
    "chair":    Chair,
    "couch":    Couch,
    "loveseat": LoveSeat,
    "table":    Table,
    "trunk":    Trunk,
    "chest":    Chest,
    "rug":      Rug,
    "frame":    Frame,
    "table lamp": TableLamp,
    "floor lamp": FloorLamp,
}
