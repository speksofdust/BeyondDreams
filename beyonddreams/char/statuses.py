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

from attribs import CharAttrbDict

PHYS_STATUS_NAMES = ("frozen", "frostbite", "burn", "numb", "stun",
    "poisioning", "bleed")
SENSORY_STATUS_NAMES = "blind", "drunk", "dumb", "confusion"
XFORM_STATUS_NAMES = "zombie", "mutagen"
FATAL_AT_MAX = 'poisoned', 'bleed',


def clear_xform_statuses(char):
    global XFORM_STATUS_NAMES
    for i in XFORM_STATUS_NAMES: char['statuses'][i] = 0

def clear_sensory_statuses(char):
    global SENSORY_STATUS_NAMES
    for i in SENSORY_STATUS_NAMES: char['statuses'][i] = 0

def clear_phys_statuses(char):
    global PHYS_STATUS_NAMES
    for i in PHYS_STATUS_NAMES: char['statuses'][i] = 0


class Stauses(CharAttrDict):
    __slots__ = CharAttrDict.__slots__

    def _defaultdict(self):
        return {
            "frozen":       0,  #bool
            "frostbite":    0,
            "burn":         0,
            "numb":         0,
            "stun":         0,
            "poisioning":   0,
            "bleed":        0,

            # Sensory
            "blind":        0,
            "drunk":        0,
            "dumb":         0,
            "confusion":    0,

            # Transform
            "zombie":       0,
            "mutagen":      0,

            "immunnull":    0,  #bool
            "immundown":    0,
            }

    #priorities:
    #   Status 'immunnull' (nullifies effect of all immunites)
    #   Status 'immundown' (all immune stats become 100 - immunodown level
    #   Char Equip
    #   Primary & Secondary Fam Immunities
    #   Primary Fam stat + Secondary Fam stat(s)

    # ---- Statuses ----------------------------------------------------- #
    def _get_frozen(self, x): return self['frozen']
    def _set_frozen(self, x): self['frozen'] = bool(x)
    frozen = property(_get_frozen, _set_frozen)

    def _get_frostbite(self, x): return self['frostbite']
    def _set_frostbite(self, x): self['frostbite'] = bool(x)
    frostbite = property(_get_frostbite, _set_frostbite)

    def _get_burn(self, x): return self['burn']
    def _set_burn(self, x): self['burn'] = bool(x)
    burn = property(_get_burn, _set_burn)

    def _get_numb(self, x): return self['numb']
    def _set_numb(self, x): self['numb'] = bool(x)
    numb = property(_get_numb, _set_numb)

    def _get_stun(self, x): return self['stun']
    def _set_stun(self, x): self['stun'] = bool(x)
    stun = property(_get_stun, _set_stun)

    def _get_poisioning(self, x): return self['poisioning']
    def _set_poisioning(self, x): self['poisioning'] = bool(x)
    poisioning = property(_get_poisioning, _set_poisioning)

    def _get_bleed(self, x): return self['bleed']
    def _set_bleed(self, x): self['bleed'] = bool(x)
    bleed = property(_get_bleed, _set_bleed)


    # ---- Sensory ---- #
    def _get_blind(self, x): return self['blind']
    def _set_blind(self, x): self['blind'] = bool(x)
    blind = property(_get_blind, _set_blind)

    def _get_drunk(self, x): return self['drunk']
    def _set_drunk(self, x): self['drunk'] = bool(x)
    drunk = property(_get_drunk, _set_drunk)

    def _get_dumb(self, x): return self['dumb']
    def _set_dumb(self, x): self['dumb'] = bool(x)
    dumb = property(_get_dumb, _set_dumb)

    def _get_confusion(self, x): return self['confusion']
    def _set_confusion(self, x): self['confusion'] = bool(x)
    confusion = property(_get_confusion, _set_confusion)


    # ---- Transformation ---- #
    def _get_zombie(self, x): return self['zombie']
    def _set_zombie(self, x): self['zombie'] = bool(x)
    zombie = property(_get_zombie, _set_zombie)

    def _get_mutagen(self, x): return self['mutagen']
    def _set_mutagen(self, x): self['mutagen'] = bool(x)
    mutagen = property(_get_mutagen, _set_mutagen)


    # ---- Imunnity ---- #
    def _get_immunnull(self, x): return self['immunnull']
    def _set_immunnull(self, x): self['immunnull'] = bool(x)
    immunnull = property(_get_immunnull, _set_immunnull)

    def _get_immundown(self, x): return self['immundown']
    def _set_immundown(self, x): self['immundown'] = clamped(0, 200)
    immundown = property(_get_immundown, _set_immundown)

    # ---- Iterators ---------------------------------------------------- #
    def bool_statuses(self):
        """Return an iterator with the names of all active boolean statuses."""
        if self['frozen']: yield "frozen"
        if self['immunnull']: yield 'immunull'

    def sensory_statuses(self):
        """Return an iterator with the names of all active sensory statuses."""
        return iter(i for i in SENSORY_STATUS_NAMES if self[i] > 0)

    def transform_statuses(self):
        """Return an iterator with the names of all active transformative
        statuses."""
        return iter(i for i in XFORM_STATUS_NAMES if self[i] > 0)

    def has_immunity_nullifiers(self):
        """True if this char has 'immunnull' status or 'immundown' level is greater than 0"""
        return (self['immunnull'] or self['immundown'] >= 1)

    def immunities(self):
        """Return an iterator of all immunities."""
        if self.has_immunity_nullifiers(): return iter(()) #immunities nullified
        return iter(())

    def current(self):
        """Return an iterator of names of all current statuses."""
        return iter(self.keys()[i] for i in self if i > 0)

    def critical_fatal(self):
        """Return an iterator of names of all current statuses that are reaching
        fatal levels."""
        return iter(i for i in FATAL_AT_MAX if self[i] > 90)

    def _fatal_maxed_check(self):
        #for i in self.critical_fatal():
            #if i >= 100:
         return False
