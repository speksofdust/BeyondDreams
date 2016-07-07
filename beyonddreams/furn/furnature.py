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

_FURNATURE_IAS = ('move',)


class Furnature(BDObj):
    _object_type = 'furnature'
    _base_desc = """ """
    _base_interactions = []


class StorageFurnature(Furnature, _Storage) pass
class SittableFurnature(Furnature, Sittable): pass
class WallHanging(Furnature): pass


# ---- Furnature types ------------------------------------------------------- #
class Bed(Furnature):
    _typename = 'bed'


class Chair(SittableFurnature):
    _typename = 'chair'


class Stool(SittableFurnature):
    _typename = 'stool'


class Couch(SittableFurnature):
    _typename = 'couch'


class Chest(StorageFurnature):
    _typename = "chest"
    _max_slots = 15


class Trunk(StorageFurnature):
    _typename = "trunk"
    _max_slots = 20


class Table(Furnature):
    _typename = "table"


class Rug(Furnature):
    _typename = "rug"


class Frame(WallHanging):
    _typename = "frame"
    def __init__(self, image):
        self._image = image
