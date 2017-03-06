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

from data import gamedata

PARTYID_LEN = 10
MAX_PARTY_SIZE = 8

def parties(): return gamedata['parties']

def get_party_from_id(partyid):
    return gamedata.party_by_id(partyid)

def is_full(partyid):
    global MAX_PARTY_SIZE
    return len(gamedata['parties'][partyid]) == MAX_PARTY_SIZE


class PartyChars(list):
    def __init__(self, party):
        self._party = party
        super().__init__([]) # TODO

    def _update_party_char(self, char, value):
        gamedata['parties'][self._party._partyid][char.charid] = value

    def charids(self):
        return iter(i for i in gamedata['parties'][self._party._partyid])

    def names(self):
        return iter(gamedata['gamechars'][i]['name']['first'] for
            i in self.charids())


class Party:
    def __init__(self, partyid):
        self._partyid = partyid
        self._active = 0
        self._chars = PartyChars

    def __len__(self): return len(self._chars)
    def __iter__(self): return iter(i for i in self._chars)
    def __contains__(self, x): return x in self._chars

    def __eq__(self, x):
        try: self._partyid == x.partyid
        except:
            raise TypeError("Can only compare to Party type.")

    def __ne__(self, x):
        try: self._partyid != x.partyid
        except:
            raise TypeError("Can only compare to Party type.")

    def _get_active(self): return self._active
    def _set_active(self, x):
        if x <= 0: self._active = 0
        elif x >= MAX_PARTY_SIZE: self._active = MAX_PARTY_SIZE
        else: self._active = x
    active = property(_get_active, _set_active)

    def on_member_leave(self, char):
        gamedata['parties'][self._partyid]
        if len(self) - 1 != 0:
            if self.index(char) == self._active:
                self._active = 0
            del self[char.charid]
            del self._chars[char]

    def _get_party_raw(self): return gamedata['parties'][self._party._partyid]

    def is_full(self): return len(self._party) == MAX_PARTY_SIZE

    def has_member(self, char): pass

    def has_member_by_charid(self, charid):
        return charid in self._chars.charids()


class PlayerParty(Party):
    def __init__(self):
        self._partyid = gamedata['playerpartyid']
        self._party = gamedata.playerparty


playerparty = None

