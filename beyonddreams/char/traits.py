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

from famtypes import FamAffinities


class CreatureBaseTraits:
    def __init__(self):
        self._tameness = 0
        self._affinities = FamAffinities()

    @property
    def affinities(self):
        """Family type affinities. These values determine how hostile or tame a creature to different family types. Higher values are more tame."""
        return self._affinities

    def _get_aff(self, char, attr):
        try:    # average of each type attr -- (auxilaries, elemental, secondaries)
            return sum((    # FIXME self[i]?
                self[i] for i in getattr(char.famtypes, attr)) // len(
                    getattr(char.famtypes, attr))
        except: return 0 # none of type (gives ZeroDivisionError)

    def _calc_total_base_affinity(self, char):
        """Calculate and return the base affinity of this creature to a given character or other creature."""
        return sum(self._tameness, self[char.famtypes.primary],
            self._get_aff(char, 'secondaries'),
            self._get_aff(char, 'elementals'),
            self._get_aff(char, 'auxilaries'))


class CreatureTraits:
    def __init__(self):
        self._basetraits = None
        self._tameness = 0

    def calc_total_affinity(self, char):
        """Calculate and return the affinity of this creature to a given character
        or other creature."""
        return int((self._basetraits._calc_total_base_affinity(char) +
            self._tameness)//10)
