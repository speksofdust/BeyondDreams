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

__all__ = ()
ZERO = 0 # cache 0 to reduce ram usage a here a bit (Effects gets used alot)

class _B:
    typename = ""
    def __init__(self):
        pass

    # HACK -- Allow cross referencing when using dict keys with "-" chars
    def __getattr__(self, i):
        if "-" in i: return getattr(self, i.replace("-", "_")
        else: return getattr(i)

    def __setattr__(self, i, v):
        if "-" in i: setattr(self, i.replace("-", "_"), v)
        else: setattr(self, i, v)

    def _iteritems(self):
        return


class StatusEffects(_B):
    typename = "statuseffects"
    # StatusEffects
    prevents =          ()
    causes =            ()
    cures =             ()

    physical_status =   ZERO
    frostbite =         ZERO
    burn =              ZERO
    numb =              ZERO
    stun =              ZERO
    poisoning =         ZERO
    bleed =             ZERO

    mental_status =     ZERO
    blind =             ZERO
    drunk =             ZERO
    dumb =              ZERO
    confusion =         ZERO

    transform_status =  ZERO
    zombie =            ZERO
    mutagen =           ZERO

    def __bool__(self):
        return any(i for i in self.prevents, self.causes, self.cures)

    def __eq__(self, x):
        if isinstance(x, StatusEffects):
            if self._iteritems != x._iteritems: return False
            for i in self._iteritems:
                if any(getattr(self, j) != getattr(x, j) for j in i):
                    return False

    def __ne__(self, x):
        if isinstance(x, StatusEffects):
            if self._iteritems != x._iteritems: return True
            for i in self._iteritems:
                if any(getattr(self, j) != getattr(x, j) for j in i):
                    return True

    def _iteritems(self):
        return iter((self.prevents, self.causes, self.cures))


class PEffects(_B):
    typename = "peffects"
    # Physical/Non-Physical
    reduces =           ()  # reduces dmg from
    increases =         ()

    dark =              ZERO
    light =             ZERO
    psychic =           ZERO
    spirit =            ZERO
    acid =              ZERO
    fire =              ZERO
    ice =               ZERO
    wind =              ZERO
    water =             ZERO
    electric =          ZERO

    physical =          ZERO
    non_physical =      ZERO
    non_elemental =     ZERO
    elemental =         ZERO

    def __bool__(self):
        return any(i for i in self.reduces, self.increases)

    def __eq__(self, x):
        if isinstance(x, PEffects):
            if self._iteritems != x._iteritems: return False
            for i in self._iteritems:
                if any(getattr(self, j) != getattr(x, j) for j in i):
                    return False

    def __ne__(self, x):
        if isinstance(x, PEffects):
            if self._iteritems != x._iteritems: return True
            for i in self._iteritems:
                if any(getattr(self, j) != getattr(x, j) for j in i):
                    return True

    def _iteritems(self):
        return iter((self.reduces, self.increases))
