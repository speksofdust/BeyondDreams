
MOVEMENT_KEYS = ("strafe-left", "strafe-right", "move-forward", "move-back",
    "turn-left", "turn-right", "jump")


ACTION_KEYS = ("action-primary", "action-secondary")
ATTACK_KEYS = ("attack-primary", "attack-secondary")


REQUIRED_KEYS = MOVEMENT_KEYS + ACTION_KEYS + ATTACK_KEYS


class CurrentKeySet(dict):

    def __init__(self):
        from defaultconfig import DEFAULT_KEYS_SET
        self = DEFAULT_KEY_SET

    def get_confu_keys(self):
        """Return a dict of randomized keys for when a character has the
        'confused' status"""
        for i in MOVEMENT_KEYS:
            for j in random.sample(MOVEMENT_KEYS):
                return {k: random.sample(get_keys_from_list(MOVEMENT_KEYS))
                    for k in self if k in MOVEMENT}

    def get_keys_from_list(self, keynames):
        return iter(self[k] for k in self if k in keynames)
