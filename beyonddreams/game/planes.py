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

REALMS = {


}

PLANES = {

    # primaries
    'mortal':   MortalPlane(),  # normal plane
    'spirit':   SpiritPlane(),
    'dead':     DeadPlane(),

    # secondaries
    'dream':    DreamPlane(),   # dreaming on any plane
    'none':     NonePlane(),    # not on plane

    # dual
    'null':     NullPlane()
}
PPLANES = 'mortal', 'spirit', 'dead', 'null'
SPLANES = 'dream', 'none', 'null'
DPLANES = ('null',)

class Plane:
    _order = 0  # 0 - primary 1 - secondary 2 - any
    _name = ""
    _can_dream = True
    _can_die = True     # True for all except DeadPlane

    # Events
    def _on_enter(self, char, *args): return
    def on_enter(self, char, *args): return
    def on_leave(self, char, *args): return
    def on_die(self, char, *args): return


class PrimaryPlane(Plane):
    """Primary Exclusive Plane type."""
    _order = 0
    _can_dream = True

    def can_dream(self, char):
        return self._can_dream

    def on_enter(self, char, *args):
        char.pplane.on_leave_plane(char, 0)
        self._on_enter_plane(char, 0)
        char['plane'][0] = self._name


class SecondaryPlane(Plane):
    """Secondary Exclusive Plane type."""
    _order = 1
    _can_dream = False # always false for secondary

    def can_dream(self, char): return False # always false for secondary

    def on_enter(self, char, *args):
        char.splane.on_leave_plane(char, 1)
        self._on_enter_plane(char, 1)
        char['plane'][1] = self._name


class DualOrderPlane(Plane):
    """Plane which can be either primary or secondary."""
    _order = 2

    def on_enter(self, char, order=0):
        char.splane.on_leave_plane(char, order)
        self._on_enter(char, order)
        char['plane'][order] = self._name

    def can_dream(self, char):
        if char['plane'][0] == self._name: return self._can_dream
        return False


class MortalPlane(PrimaryPlane):
    _name = "mortal"

    def on_die(self, char):
        # check if become spirit
        #
        pass

class DreamPlane(SecondaryPlane):
    _name = "dream"

class NonePlane(SecondaryPlane):
    _name = "none"

class SpiritPlane(PrimaryPlane):
    _name = "spirit"


class DeadPlane(PrimaryPlane):
    _name = "dead"
    _can_dream = False
    _can_die = False


class NullPlane(DualPlane):
    _name = "null"
    _can_dream = False

    def on_die(self, char):
        pass


def set_pplane(char, plane):
    if plane != char.pplane and plane in PPLANES: PLANES[plane].on_enter(char)

def set_splane(char, plane):
    if plane != char.splane and plane in SPLANES:
        if plane in DPLANES: PLANES[plane].on_enter(char, 1)
        else: PLANES[plane].on_enter(char)

def is_dreaming(char):
    return char['plane'][1] == 'dream'

def wakeup(char):
    if is_dreaming(char):
        PLANES[char.pplane].on_wakeup(char)
        char['plane'][1] = 'none'

def on_die(char):
    if char.splane._name != 'none': return char.splane.on_die()
    return char.pplane.on_die()

def on_enter_pplane(char, plane):
    """Called on entering a new primary plane."""
    if plane == 'dead':
        if char['plane'][1] == 'dream':
            pass #TODO
