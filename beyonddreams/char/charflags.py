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


CHARFLAGS = {
    # Temp Flags
    "has-encounter":    50, # currently attacked or in battle, etc.
    "full-recover":     98,

    # ---- ko-flags ---- #
    "revive_once":      99, # fails if ko'd in non revivable condition

    # ---- KO-Type flags (as many as applicapable) ---- #
    "suffocated":       111,
    "drowned":          112,

    # last hit
    "stabbed":          113,
    "beaten":           114,
    "electrocuted":     115,
    "burned":           116,
    "frozen":           117,

    # status(s) maxed
    "bled":             120, # bleed level maxed
    "poisoned":         121, # poisoning level maxed
    "drunk":            122, # drunk & poisioning levels maxed

    # other
    "gutted":           198,
    "halved":           199, # split in half

    # non-revivable ko-type flags
    "beheaded":         200,
    "exploded":         201,
    "vaporized":        202,
    "flattened":        203,
    }
MIN_NON_REVIVABLE_KOFLAG = 200 # minimum non revivable flag
