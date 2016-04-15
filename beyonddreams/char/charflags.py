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

RESERVED = 0
IN_SAVEPOINT = 49
IN_ENCOUNTER = 50

# Factors
FT_NONE = 150
FT_NULL = 151
FT_HALF = 152
FT_2X =   153
FT_4X =   154
FT_FULL = 155
FACTORS = (FT_NONE, FT_NULL, FT_2X, FT_4X, FT_FULL)


CHARFLAGS = {
    # cast flags
    "aura":             1000,
    "fire":             1100,
    "ice":              1101,
    "wind":             1102,
    "elec":             1103,
    "light":            1108,
    "dark":             1109,
    "mag":              1111,
}


DFLAGS = {
    RESERVED:         0,
    SUFFOCATED:       111,
    DROWNED:          112,

    # last hit
    STABBED:          113,
    BEATEN:           114,
    ELECTROCUTED:     115,
    BURNED:           116,
    FROZE:            117,
    FROZEN:           118,

    # status(s) maxed
    BLED:             120, # bleed level maxed
    POISIONED:          121, # poisoning level maxed
    DRANK:            122, # drunk & poisioning levels maxed

    # misc
    REVIVED_WHILE_ZOMBIE: 170,

    # barely revivable
    GUTTED:           198,
    HALVED:           199, # split in half

    # non-revivable dflags
    BEHEADED:         200,
    EXPLODED:         201,
    VAPORIZED:        202,
    FLATTENED:        203,
    }
DFLAGS.MAX_REVIVABLE = 199
