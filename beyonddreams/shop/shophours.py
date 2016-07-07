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
from .game.dates import *

def _fmtt(t): return "{}:{}".format(t[0], t[1])
def _fmttx(o, a, b):
    return '{}:{}-{}:{}'.format(o[a][0], o[a][1], o[b][0], o[b][1])

def _fmtsdtime(t):
    if t == ((24, 0) or (-1, 0) return t
    if (t is None or t == -1): return (-1, 0)
    elif t == 24: return (24, 0)
    elif len(t) == 1:
        if t <= -2: t = 0
        elif t >= 25:
        else return (t, 0) # add a 0 for min
    else:
        if t[1] < 0: return (t[0], 0)
        elif t[1] > 59: return (t[0], 59]
        return t


class ShopDay(tuple):
    def __init__(self, opentime, closetime, breakstart, breakend):
        super().__init__((
            _fmtsdtime(opentime)
            _fmtsdtime(closetime)
            _fmtsdtime(breakstart)
            _fmtsdtime(breakend)
            )

    @classmethod
    def NoBreak(cls, opentime, closetime):
        return cls(opentime, closetime,

    @classmethod
    def Open24Hours(cls):
        return cls((24, 0),(24, 0), (-1, 0), (-1, 0))

    @classmethod
    def Closed(cls):
        return cls((-1, -1), (-1, -1), (-1, 0), (-1, 0))

    def _is_ob(self, x): return self.opens_at[0] <= x < self.break_start[0]
    def _is_bc(self, x): return self.break_end[0] <= x <= self.closes_at[0]

    def __str__(self):
        return "".join((_fmttx(self, 0, 1), " ", _fmttx(self, 2, 3)))

    def hours_as_str(self):
        if self[0] == 24: return 'Open 24 Hours'
        elif self[0] == -1: return 'Closed'
        elif self.has_break():
            return "".join((_fmttx(self, 0, 1), " break: ", _fmttx(self, 2, 3)))
        else: return "".join((_fmttx(self, 0, 1)))

    @property
    def opens_at(self):
        return self[0]

    @property
    def closes_at(self):
        return self[1]

    @property
    def break_start(self):
        return self[2]

    @property
    def break_end(self):
        return self[3]

    def is_open_hours(self, hour):
        """True if hour is during a time that the shop will be open today.
        Does not check for break hours."""
        return self.opens_at[0] <= x < self.closes_at[0]

    def has_break(self):
        return (self.break_start[0] != (-1 or 24))

    def is_closed_today(self):
        """True if is not open at all today."""
        return self.opens_at[0] == -1


    def _atopenchk(self, h, m):
        if self.opens_at[0] == 24: return True
        elif self.opens_at[0] == -1 return False
        elif self.opens_at[0] < hour: return False
        elif self.opens_at[0] == hour and self.opens_at[1] <= min:
            return False
        return True

    def is_open(self, hour, minute):
        if self.is_on_break: return False
        elif self.is_before_break(hour):
            return self._atopenchk(hour, min)
        else:
            return self.closes_at > hour


CLOSED_TODAY = ShopDay.Closed()
OPEN_ALL_DAY = ShopDay.Open24Hours()


class ShopWeek(tuple):
    def __init__(self, sun=CLOSED_TODAY, mon=CLOSED_TODAY, tue=CLOSED_TODAY,
        wed=CLOSED_TODAY, thur=CLOSED_TODAY, fri=CLOSED_TODAY, sat=CLOSED_TODAY):
        super().__init__((sun, mon, tue, wed, thur, fri, sat))

    @classmethod
    def SameWeekdayHours(cls, weekdayhours, sat=CLOSED_TODAY, sun=CLOSED_TODAY):
        return cls(sun, weekdayhours, weekdayhours, weekdayhours, weekdayhours,
            weekdayhours, sat)

    @classmethod
    def ClosedWeekdays(cls, sun, sat):
        return cls(sun, sat)

    @classmethod
    def ClosedWeekends(cls, mon, tue, wed, thur, fri):
        return cls(mon, tue, wed, thur, fri)

    def today(self):
        return self[gametime()[0]]

    def tommorrow(self):
        return self[tomorrows_weekday_idx()]

    def is_open(self, wday, hour, minute):
        return self[wday].is_open(hour, minute)

    def _days_open(self):
        return iter(self[i] for i in self if not i.is_closed_today())

    def days_open(self):
        """Return an iterator of weekday names open this week."""
        return iter(WEEKDAYS[self[i]] for i in self if not i.is_closed_today())

    def is_before_break(self):
        if self[day].has_break():
            return self[day]break_start < hour
        return False

    def is_after_break(self):
        if self[day].has_break():
            return self[day]break_end >= hour
        return False

    def is_on_break(self):
        if self[day].has_break():
            return (self[day]break_start[0] <= hour < self[day]break_end[0])



OPEN_24_7 = ShopWeek(OPEN_ALL_DAY, OPEN_ALL_DAY, OPEN_ALL_DAY,
    OPEN_ALL_DAY, OPEN_ALL_DAY, OPEN_ALL_DAY, OPEN_ALL_DAY)


__ALL__ = ('OPEN_24_7', 'CLOSED_TODAY', 'OPEN_ALL_DAY')



# code generator #
#def _cl(x):
    #if x > 23: return 0
    #return x

#def _cf(x):
    #if x > 23: return x - 23
    #return x

#def _gsd(op, opa, cl, bs=0, be=0, nb=""):
    #o = "".join(("SD_", str(op), opa.capitalize(), "to"))
    #c = op + cl
    #cc = _cl(c-1)
    #op = _cl(op-1)
    #if nb: nb = "NoBreak({}, {})".format(op, _cf(cc))
    #else: nb = "({}, {}, {}, {})".format(op, _cf(cc), _cf(op+bs), _cf(op+be))
    #if c > 12: return "{}{}A = ShopDay{}".format(o, c - 12, nb)
    #return "{}{}P = ShopDay{}".format(o, c, nb)

