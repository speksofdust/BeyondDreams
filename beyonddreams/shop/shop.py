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

from shophours import ShopHours

class Shop:
    _shoptype = ""
    _default_shophours = None
    def __init__(self, shophours=None):
        if shophours = None:
            self._shophours = self._default_hours
        else: self._shophours = shophours

    @property
    def shoptype(self):
        return self._shoptype

    @property
    def name(self):
        return self._name

    @property
    def hours(self):
        return self._shophours

    def todays_hours(self, day):
        return self._shophours.today(day)

    def is_open(self, day, hour, minute):
        """True if this shop is currently open at the given
        day, hour, and minute."""
        self._shophours.is_open(day, hour, minute)