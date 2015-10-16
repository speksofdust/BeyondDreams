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

ZERO = 0 # cache 0 to reduce ram usage a here a bit

class _B(dict)
    typename = ""
    def __init__(self, items, **kwargs):
        super().__init__(items)

    def immunities(self):
        """Return an iterator of immunities."""
        return iter(i for i in self.keys() if self[i] == "immune")

    def altered(self):
        """Return an iterator of altered items (value != 0)
        where each item is a tuple as (name, value). Includes immunities"""
        return iter((i, self[i]) for i in self.keys() if self[i] != 0)

    def unaltered(self):
        """Return an iterator of the names of all unaltered items (value = 0)."""
        return iter(i for i in self.keys() if self[i] == 0)

    def increases(self):
        """Return an iterator of items which have an increase where each item
        is a tuple as (name, value)."""
        return iter((i, self[i]) for i in self.keys() if self[i] > 0)

    def decreases(self):
        """Return an iterator of items which have a decrease where each item
        is a tuple as (name, value)."""
        return iter((i, self[i]) for i in self.keys() if self[i] < 0)


class StatusEffects(_B):
    typename = "statuseffects"
    # StatusEffects
    def __init__(self, **kwargs):
        super().__init__({
            # physical types
            "frostbite" =         ZERO,
            "burn" =              ZERO,
            "numb" =              ZERO,
            "stun" =              ZERO,
            "poisoning" =         ZERO,
            "bleed" =             ZERO,

            # mental types
            "blind" =             ZERO,
            "drunk" =             ZERO,
            "dumb" =              ZERO,
            "confusion" =         ZERO,

            # transform types
            "zombie" =            ZERO,
            "mutagen" =           ZERO,

            # Bonuses -- Added to all qualifing type
            #   eg: mental_status adds to any mental_status type
            "physical_status" =   ZERO,
            "mental_status" =     ZERO,
            "transform_status" =  ZERO,
            })
        for i in kwargs:    self[i] = kwargs[i]


class AddedEffects(_B):
    typename = "addedeffects"
    # Physical/Non-Physical
    reduces =           ()  # reduces dmg from
    def __init__(self, **kwargs):
        super().__init__({
            "dark" =              ZERO,
            "light" =             ZERO,
            "psychic" =           ZERO,
            "spirit" =            ZERO,
            "acid" =              ZERO,
            "fire" =              ZERO,
            "ice" =               ZERO,
            "wind" =              ZERO,
            "water" =             ZERO,
            "electric" =          ZERO,

            # Bonuses -- Added to all qualifing type
            #   eg: physical adds to all physical types
            "physical" =          ZERO,
            "non-physical" =      ZERO,
            "non-elemental" =     ZERO,
            "elemental" =         ZERO,
            })
        for i in kwargs:    self[i] = kwargs[i]


class _Dummy:
    # speed optomizations for dummy types -- since all values are guarenteed to
    #   be ZERO
    def immunities(self):   return iter(())
    def altered(self):      return iter(())
    def unaltered(self):    return iter(self.keys())
    def increases(self):    return iter(())
    def decreases(self):    return iter(())


class DummySE(StatusEffects, _Dummy): pass
class DummyAE(AddedEffects, _Dummy): pass

# cache dummy objects for items, etc. that don't alter any values
DUMMY_SE = DummySE()
DUMMY_AE = DummyAE()

# handlers to choose whether or not to use the dummy
def get_seffects(cls, **kwargs):
    if kwargs: return AddedEffects(kwargs)
    else:
        global DUMMY_SE
        return DUMMY_SE

def get_aeffects(cls, **kwargs):
    if kwargs: return AddedEffects(kwargs)
    else:
        global DUMMY_AE
        return DUMMY_AE


__all__ = ("DUMMY_SE", "DUMMY_AE", "get_aeffects", "get_seffects")
