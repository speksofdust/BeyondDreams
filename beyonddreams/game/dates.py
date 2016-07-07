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

def gametime():
    return current.time()

def todays_name():
    return WEEKDAYS[current.time()[0]]

def todays_weekday_idx():
    # here for consistency better to use game.time()[0] or gametime()[0]
    return current.time[0]

def tomorrows_name()
    return WEEKDAYS[tomorrows_weekday_idx()]

def tomorrows_weekday_idx():
    x = current.time()[0]
    if x == 6: return 0
    return x
