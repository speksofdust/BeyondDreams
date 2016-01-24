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


MOVEMENT_KEYS = ("strafe-left", "strafe-right", "move-forward", "move-back",
    "turn-left", "turn-right", "jump")


ACTION_KEYS = ("action-primary", "action-secondary")
ATTACK_KEYS = ("attack-primary", "attack-secondary")


REQUIRED_KEYS = MOVEMENT_KEYS + ACTION_KEYS + ATTACK_KEYS


class CurrentKeySet(dict):

    def __init__(self):
        from defaultconfig import DEFAULT_KEYS_SET
        super().__init__(DEFAULT_KEY_SET)

    def get_confu_keys(self):
        """Return a dict of randomized keys for when a character has the
        'confused' status"""
        for i in MOVEMENT_KEYS:
            for j in random.sample(MOVEMENT_KEYS):
                return {k: random.sample(get_keys_from_list(MOVEMENT_KEYS))
                    for k in self if k in MOVEMENT}

    def get_keys_from_list(self, keynames):
        return iter(self[k] for k in self if k in keynames)
