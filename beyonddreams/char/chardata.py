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


# will replace char.py
import cacc

class CharAccessor(GameDataAccessorDict):
    __slots__ = ()
    def __init__(self, char):
        self.char = char

    def __dpath(self): return gamedata['chars'][self.char]

    @property
    def name(self):
        return cacc.CharNameAccessor(self)

    @property
    def inventory(self):
        return cacc.CharInventory(self)

    @property
    def statuses(self):
        return cacc.Statuses(self)

    # ---- Query --------------------------------------------------------- #
    @property
    def famtypes(self):
        """Return an iterator of family types for this character starting with
        the primary type."""
        return () #TODO

    def is_alive(self):
        """True if this character's hp is 0."""
        return self.char['stats']['hp'] != 0

    def is_critical(self):
        """True if this character's hp is less than 10 percent."""
        return self.char['stats']['hp'] <= 10

    def is_undead(self):
        """True if this character has a fam type of 'undead' or has 'zombie'
        status."""
        return ('undead' in self.famtypes or self['statuses']['zombie'] == 100)

    # ---- Calculated stat/status getters -------------------------------- #
    def hp(self):
        """Health for this character."""
        return self['stats']['hp']

    def phys_energy(self):
        """The current physical energy for this character."""
        return

    def mental_energy(self):
        """The current mental energy for this character."""
        return
