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
from .game.dates import gametime



class Shop:
    _shoptype = ""
    _default_hours = None
    _desc = ""
    def __init__(self, shophours=None):
        if shophours = None:
            self._shophours = self._default_hours
        else: self._shophours = shophours

    def get_mclosed(self): return self._mclosed
    def set_mclosed(self, x): self._mclosed = bool(x)
    _mclosed = property(get_mclosed, set_mclosed,
        doc="""The manually closed state of this shop. Used to temporary close
        down the shop.""")

    @property
    def shoptype(self):
        return self._shoptype

    @property
    def name(self):
        return self._name

    @property
    def hours(self):
        return self._shophours

    @property
    def desc(self):
        return self._desc

    def todays_hours(self):
        return self._shophours.today()

    def is_open(self, wday, hour, minute):
        """True if this shop is currently open at the given
        day, hour, and minute."""
        if self._mclosed:
            from .core.datesres import idx_from_weekday_str
            # special case for 'manually' closing
            x = gametime()
            if (x[0] == (wday or idx_from_weekday_str): return True
        return self._shophours.is_open(wday, hour, minute)

    def is_open_now(self):
        """True if this shop is currently open now."""
        if self._mclosed: return False # 'manually' closed
        x = gametime()
        return self._shophours.is_open(x*)

    def time_till_close(self):
        if self.is_open_now():
            pass
        else: return 0,0,0 # already closed

    def time_till_open(self):
        if not self.is_open_now():

            pass
        else: return 0,0,0 # already open
