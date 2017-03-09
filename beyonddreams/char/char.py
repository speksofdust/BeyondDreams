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

from game.data import gamedata

CHAR_SPECIALFLAGS = ('VISITED_NOMEM', 'RELATIONSHIPS_OFF')

def _boolkw(char, k, **kwargs):
    if k in kwargs: char[k] = bool(kwargs[k])

# will replace char.py
CHARID_LEN = 30

statuses_dict = {
        # physical
        "frozen":       0,   # bool
        "frostbite" :   0,
        "burn" :        0,
        "numb" :        0,
        "stun" :        0,
        "poisoning" :   0,
        "bleed" :       0,
        "petrify":      0, # turned to stone

        # mental
        "blind" :       0,
        "drunk" :       0,
        "dumb" :        0,
        "confusion" :   0,
        #"hallucination": 0,

        # transform
        "zombie" :      0,
        "mutagen" :     0,

        # specials
        "immunull":     0,  # bool
        "immundown":    0,
        }

stats_dict = {
    "phys-energy":      100,
    "mental-energy":    100,
    "health":           100,
}

monster_datadict = {
    "temp":         {},
    "temp-flags":   [],
    "flags":        [],
    "KO-flags":     [],
    "base":         "",
}

wildlife_datadict = {
    "temp":         {},
    "temp-flags":   [],
    "flags":        [],
    "KO-flags":     [],
    "base":         "",
}

char_datadict = {
    "temp":         {}, # non-writable stuff
    # flags
    "temp-flags":   [], # non-writable
    "flags":        [],
    "KO-flags":     [], # cleared after revived|re-spawn
    "marker-flags": [0, 0], # added/updated after significant points
    # base data
    "base":         "",

    # name
    "name": {
        "first":        "",
        "last":         "",
        "middle":       "",
        "nick":         ""
        },
    "location": {
        'region':       0,
        },

    "bodybase":     {
        "type":         0,
        },

    "body-current": {

        },

    # inventory & wallet, etc.
    "cash":         [0],
    "coupons":      [],
    "cards":        [],
    "bag":          "default",
    "consumables":  [],
    "weapons":      [],
    "wearables":    [],
    "keyitems":     [],

    # equip
    "handedness":   0,  # 0-left, 1-right, 2-ambidextrous
    "equip":    {
        },
}


def _clear_temps(d):
    for i in gamedata[d]:
        try: del gamedata[d][i]['temp']
        except: KeyError

def _update_chars(d):
    for i in gamedata[d]: update_char(gamedata[d][i])


def _assemble(ob, dd, sd=stats_dict, st=statuses_dict):
    ob._dataid = _get_new_charid(gdata, ob)
    gamedata[ob._gdata][ob._dataid] = dd.copy()
    gamedata[ob._gdata][ob._dataid]["stats"] = sd.copy()
    gamedata[ob._gdata][ob._dataid]["statuses"] = st.copy()
    #gamedict[ob._gdata][ob._dataid]["statusres"] = st.copy()
    ob._data = gamedata[ob._gdata][ob._dataid]

def _get_new_charid(gdata):
    from random import randint
    x = 0
    while True:
        if x not in gamedata[ob._gdata].keys(): break
        x = randint(0, 9999999999999999999999)
    return x

def add_monster_dd(gdata, ob, dd=monster_data_dict): _assemble(ob, dd)
def add_char_dd(gdata, ob, dd=chardata_dict): _assemble(ob, dd)
def add_wildlife_dd(ob, dd=wildlife_datadict): _assemble(ob, dd)


class _CharT: # character type base class
    _ctid = 1 # chartype id -- 0 pc, 1 npc, 2 baddie (different from chartype)
    is_baddie = False
    __slots__ = ()
    def is_npc(self): return True

    def __destroy(self):
        from chardata import gamedata
        try:
            del gamedata[self._gdata][self._dataid]
            self._destroyed = True
        except:
            pass


class _Baddie: # 'bad guy' mixin -- always NPC
    _ctid = 2
    is_baddie = True
    __slots__ = ()


# ---- Chartypes ------------------------------------------------------------- #
class _Normal(_CharT):
    _ctname = "normal"
    __slots__ = ()
    def __init__(self, gamedata):
        from chardata import add_char_dd
        self._destroyed = False
        self._dataid = 0
        self._data = add_char_dd(self)

    def chartype(self): return 0
    def has_tabby(self): return self._data["marker-flags"][0] > 0

    # stuff TODO
    def can_equip(self, item): pass
    def is_in_guild(self, guild): pass


class _WMCommon(_CharT): # mixin for stuff common to both _Wildlife and _Monster
    __slots__ = _CharT.__slots__

    def has_tabby(self): return False
    def can_equip(self, item): return False
    def is_in_guild(self, guild): return False


class _Wildlife(_WMCommon):
    _ctname = "wildlife"
    __slots__ = _WMCommon.__slots__
    def __init__(self):
        from chardata import add_wildlife_dd
        self._destroyed = False
        self._dataid = 0
        self._data = add_wildlife_dd(self)

    def chartype(self): return 1


class _Monster(_WMCommon): # may be playable in certain conditions
    _ctname = "monster"
    __slots__ = _WMCommon.__slots__
    def __init__(self):
        from chardata import add_monster_dd
        self._destroyed = False
        self._dataid =  0
        self._data = add_monster_dd(self)

    def chartype(self): return 2


# ---- Baddie types ---------------------------------------------------------- #
class CharBaddie(_Normal, _Baddie):
    _gdata = "b0"
    __slots__ = _Normal.__slots__


class WildlifeBaddie(_Wildlife, _Baddie):
    _gdata = "b1"
    __slots__ = _Wildlife.__slots__


class MonsterBaddie(_Monster, _Baddie):
    _gdata = "b2"
    __slots__ = _Monster.__slots__


# ---- Npc types ------------------------------------------------------------- #
class NPChar(_Normal)
    _gdata = "np0"
    __slots__ = _Normal.__slots__


class NPCWildlife(_Wildlife):
    _gdata = "np1"
    __slots__ = _Wildlife.__slots__


class NPCMonster(_Monster):
    _gdata = "np2"
    __slots__ = _Monster.__slots__


# ---- Playable types -------------------------------------------------------- #
class _PChar(_Char): # playable character mixin
    _ctid = 0
    __slots__ = _PChar.__slots__
    def is_npc(self): return False


class PChar(_Normal, _PChar)
    _gdata = "pc0"
    __slots__ = _Normal.__slots__


class PCWildlife(_Wildlife, _PChar):
    _gdata = "pc1"
    __slots__ = _Wildlife.__slots__


class PCMonster(_Monster, _PChar):
    _gdata = "pc2"
    __slots__ = _Monster.__slots__

