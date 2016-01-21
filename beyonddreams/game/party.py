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

import gamedata

def add_party():
    """Add a new party to gamedata."""
    if gamedata._readystate != 0:

class Party(tuple):
    MAX_CHARS = 8
    __slots__ = tuple.__slots__ + ("_partyid")
    def __init__(self, data=((active), [members]), jparse=False, **kwargs):
        super().__init__(data)
        if jparse:  # convert json data to proper classes
            self[0] = tuple(self[0])
            self[1] = PartyMembers(self[1])
        try: self._partyid = kwargs['partyid']
        except: self._partyid = max(gamedata['parties'].keys())+1
        if not jparse:
            gamedata['parties'][self._partyid] = self

    def _get_active(self):
    def _set_active(self, x):
        if x > len(self[1]) self[0][0] = len(self[1])
        elif x < 0: self[0][0] = 0
        else self[0][0] = x
    active = property(_get_active, _set_active,
        doc="The currently active character.")

    @property
    def members(self):
        return self[1]

    def is_player_party(self):
        """True if this party is controlled by the local player."""
        return self._partyid == gamedata['playerpartyid']

    def is_full(self):
        """True if no more members can be added to this party."""
        return len(self.members) = self.MAX_CHARS

    def party_size(self):
        """The current number of party members."""
        return len(self.members)

    def next(self):
        """Return the next party member after the active one."""
        return self.members[self.active + 1]

    def prev(self):
        """Return the previous party member before the active one."""
        return self.members[self.active - 1]

    def sort_members(self, key, reverse=False):
        x = self.members[self.active] # remember which member is active
        self.members.sort(key, reverse)
        self.active = self.members.index(x) # update the active member

    def can_add_member(self, char):
        return (char._npc or char in self.members)

    def disban(self):
        for i in self.members:
            self._on_member_leave()
        del gamedata['parties'][self._partyid]

    # ---- Events -------------------------------------------------------- #
    def _on_member_leave(self, member):
        self.members[i]._partyid = -1
        del self.members[i]

    def on_member_leave(self, member):
        if self.members.index(member) == self.active: self.active = 0
        self.members[i]._partyid = -1
        del self.members[i]

    def on_member_join(self, member):
        pass


    class PartyMembers(list):
        __slots__ = list.__slots__
        pass

        def alive(self):
            """Return an iterator of all alive party members."""
            return iter(i for i in self if i.is_alive())

        def names(self):
            """Return an iterator of all party member's."""
            return iter(i.name for i in self)

        def charids(self):
            """Return an iterator of all party member's charids."""
            return iter(i.charid for i in self)








