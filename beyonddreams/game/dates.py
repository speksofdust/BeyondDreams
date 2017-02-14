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

from .core.datesres import *
from game import current


class GameTime:
    def __init__(self, wd, h, m, d):
        self._wd = wd
        self._h = h
        self._m = m
        self._d = d

    @classmethod
    def now(cls):
        return cls(*current.time_tuple())

    @property
    def weekday(self): return self._wd

    @property
    def hour(self): return self._h

    @property
    def minute(self): return self._m

    @property
    def day(self): return self._d

    def todays_name(self): return WEEKDAYS[self._wd]

    def tomorrows_name(self):WEEKDAYS[tomorrows_weekday_idx()]

    def tomorrows_weekday_idx(self):
        if self._wd + 1 == 6: return 0
        return self._wd + 1


def gametime():
    return current.time_tuple()

def _gt_wd(): return current.time_tuple()[0]
def _gt_hour(): return current.time_tuple()[1]
def _gt_min(): return current.time_tuple()[2]
def _gt_day(): return current.time_tuple()[3]

gametime.weekday = _gt_wd
gametime.hour = _gt_hour
gametime.min = _gt_min
gametime.day = _gt_day
