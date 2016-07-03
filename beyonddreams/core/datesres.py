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

__ALL__ = ["MONTHS", "WEEKDAYS", "WEEKDAYS_ABBR", "idx_from_weekday_str"
    "idx_from_month_str"]

MONTHS = ("january", "febuary", "march", "april", "may", "june", "july",
    "august", "september", "october", "november", "december")

WEEKDAYS = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday",
    "saturday")

WEEKENDS = ("sunday", "saturday")
MIDWEEK = WEEKDAYS[1:5]

WEEKDAYS_ABBR = ("sun", "mon", "tue", "wed", "thur", "fri", "sat")

def idx_from_weekday_str(w):
    global WEEKDAYS
    return WEEKDAYS[w.lower()[0:2]].index()

def idx_from_month_str(m):
    global MONTHS
    return MONTHS[m.lower()[0:2]].index()
