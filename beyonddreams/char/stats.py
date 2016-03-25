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

from attribs import CharAttrDict
from charflags import CFlags


class Energy(CharAttrDict):
    """Dictionary data storage class for 'Energy' type data."""
    _ABSMAX = 1000
    _NORMMAX = 100
    __slots__ = CharAttrDict.__slots__

    def _defaultdict(self):
        return {
            "regen-rate": 1,
            "regen-amt":  1,
            "current":    100,
            "flags":      CFlags(),
            }

    def _parseinit(self):
        self['flags'] = CFlags(self['flags'])

    def _get_rrate(self): return self['regen-rate']
    def _set_rrate(self, x): self['regen-rate'] = clamped(x, 0, 100)
    regen_rate = property(_get_rrate, _set_rrate)

    def _get_ramt(self): return self['regen-amt']
    def _set_ramt(self, x): self['regen-amt'] = clamped(x, 1, 100)
    regen_amt = property(_get_ramt, _set_ramt)

    @property
    def flags(self):
        return self['flags']

    def has_flag(self, x):
        return x in self['flags']


class Stats(CharAttrDict):
    __slots__ = CharAttrDict.__slots__

    def _defaultdict(self):
        return {
            'intellect': 1,
            'strength': 50,
            'focus':    50,
            }

    def _get_intellect(self): return self['intellect']
    def _set_intellect(self, x): self['intellect'] = clamped(x, 1, 100)
    intellect = property(_get_intellect, _set_intellect)

    def _get_strength(self): return self['strength']
    def _set_strength(self, x): self['strength'] = clamped(x, 1, 100)
    strength = property(_get_strength, _set_strength)


