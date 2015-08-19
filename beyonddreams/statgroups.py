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


class _StatGroups(dict):
    def __init__(self):
        self = {
        "physical-statuses":  ("frostbite", "burn", "numb", "stun", "poisioning",
            "bleed")
        "mental-statuses":    ("blind", "drunk", "dumb", "confusion"),
        "transform-statuses":   ("undead", "mutagen"),
        "non-elemental":    ("acid", "psychic", "spirit"),
        "elemental":        ("dark", "light", "fire", "ice", "wind", "water",
            "electric"),
        "non-physical":      ("dark", "light", "psychic", "spirit"),
        "physical":          ("acid", "fire", "ice", "wind", "water",
            "electric"),
        }

    def statuseffect_groupnames(self):
        return iter(i for i in self if i.endswith("statuses"))

    def other_groupnames(self):
        return iter(i for i in self if not i.endswith("statuses"))

    def all_statuses(self):
        return iter(self[i] for i in self if i.endswith("statuses"))


statgroups = _Statgroups()

__all__ = "statgroups"
