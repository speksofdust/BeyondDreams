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


WEEKDAYS = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday",
    "saturday")

def index_from_weekday_string(w):
    global WEEKDAYS
    return WEEKDAYS[w.lower()].index()


class ShopHours(Tuple):
    def __init__(self, sun=CLOSED_TODAY, mon=CLOSED_TODAY, tue=CLOSED_TODAY,
        wed=CLOSED_TODAY, thu=CLOSED_TODAY, fri=CLOSED_TODAY, sat=CLOSED_TODAY):
        super().__init__((sun, mon, tue, wed, thu, fri, sat))

    def today(self, day):
        try: return self[day]
        except:
            try: return self[index_from_weekday_string(day)]
            except: raise IndexError("Invalid day string: {}".format(day))

    def is_open(self, day, hour, minute):
        return self.today(day).is_open(hour, minute)


def _fmtt(t): return "{}:{}".format(t[0], t[1])

def _fmtsdtime(t):
    if t == None: return (None, None)
    elif len(t) == 1: return (t, 0) # add a 0 for min
    else return t

class ShopDay:
    def __init__(self, opentime, closetime, breakstart, breakend):
        self._opentime =     _fmtsdtime(opentime)
        self._closetime =    _fmtsdtime(closetime)
        self._breakstart =   _fmtsdtime(breakstart)
        self._breakend =     _fmtsdtime(breakend)

    def _is_ob(self, x): return self.opens_at[0] <= x < self.break_start[0]
    def _is_bc(self, x): return self.break_end[0] <= x <= self.closes_at[0]

    def __str__(self):
        return "".join((_fmtt(self.opens_at), "-", _fmtt(self.closes_at), " ",
        _fmtt(self.break_start) "-", _fmtt(self.break_end)))

    @property
    def opens_at(self):
        return self._opentime

    @property
    def closes_at(self):
        return self._closetime

    @property
    def break_start(self):
        return self._break_start

    @property
    def break_end(self):
        return self._break_end

    def is_open_hours(self, hour):
        """True if hour is during a time that the shop will be open today.
        Does not check for break hours."""
        return self.opens_at[0] <= x < self.closes_at[0]

    def has_break(self):
        return self._break_start is not None

    def is_before_break(self, hour):
        return self.break_start < hour

    def is_after_break(self, hour):
        return self.break_end >= hour

    def is_on_break(self, hour):
        return self.break_start[0] <= hour < self.break_end[0]

    def _atopenchk(self, h, m):
        if self.opens_at[0] < hour: return False
        elif self.opens_at[0] == hour and self.opens_at[1] <= min:
            return False
        return True

    def is_open(self, hour, minute):
        if self.is_on_break: return False
        elif self.is_before_break(hour):
            return self._atopenchk(hour, min)
        else:
            return self.closes_at > hour

class ShopdayNoBreak(ShopDay):
    def __init__(self, opentime, closetime):
        self._opentime =     _fmtsdtime(opentime)
        self._closetime =    _fmtsdtime(closetime)
        self._breakstart = self._breakend = (None, None)

    def __str__(self):
        return "-".join((_fmtt(self.opens_at), _fmtt(self.closes_at)))

    def is_after_break(self, hour): return False
    is_before_break = is_after_break = is_on_break

    def is_open(self, hour, minute):
        return self.is_open_hours(hour) and self._atopenchk(hour, min)


class ShopDayClosed(ShopDay):
    def __init__(self):
        self._opentime = (None, None)
        self._closetime = self._opentime
        self._breakstart = self._opentime
        self._breakend =    self._opentime

    def __str__(self): return "Closed"

    def is_open(self, hour, minute): return False
    def is_after_break(self, hour): return False
    is_before_break = is_after_break = is_on_break


CLOSED_TODAY = ShopdayClosed()
SD_7Ato7P = ShopDay(6, 19, 12, 13)
SD_6Ato8P = ShopDay(5, 8, 10, 11)
SD_6Ato9P = ShopDay(5, 20, 10, 11)
SD_5Ato10P = ShopDay(4, 21, 9, 10)
SD_5Pto12A = ShopDayNoBreak(16, 23)


# code generator #
def _cl(x):
    if x > 23: return 0
    return x

def _cf(x):
    if x > 23: return x - 23
    return x

def _gsd(op, opa, cl, bs=0, be=0, nb=""):
    o = "".join(("SD_", str(op), opa.capitalize(), "to"))
    c = op + cl
    cc = _cl(c-1)
    op = _cl(op-1)
    if nb: nb = "NoBreak({}, {})".format(op, _cf(cc))
    else: nb = "({}, {}, {}, {})".format(op, _cf(cc), _cf(op+bs), _cf(op+be))
    if c > 12: return "{}{}A = ShopDay{}".format(o, c - 12, nb)
    return "{}{}P = ShopDay{}".format(o, c, nb)



