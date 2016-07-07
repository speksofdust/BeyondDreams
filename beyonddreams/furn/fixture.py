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


class Fixture(BDObject):
    _object_type = 'fixture'
    _base_desc_"""Similar to furnature except that they cannot normally
be moved."""

class StorageFixture(Fixture, _Storage): pass
class SittableFixture(Fixture, Sittable): pass


# ---- Fixture types --------------------------------------------------------- #
class Toilet(Fixture):
    _typename = "toilet"
    _inctags = "bathroom"
    _base_interactions = ['flush']


class Sink(Fixture):
    _typename = "sink"


class BathTub(Fixture):
    _typename = "bathtub"


class Shower(Fixture):
    _typename = "shower"


class Window(Fixture):
    _typename = "window"


class Door(Fixture):
    _typename = "door"


class Cabinet(StorageFixture):
    _typename = "cabinet"
