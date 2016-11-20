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

_STORAGE_IAS = 'store item', 'view items'


class BDObjSet:
    pass



OB_IDS = {               # sub ob ids
    "furnature":    1000,
    "chest":        1001,
    "trunk":        1002,
    "clothing":     100, # 101-299

    "weapon":       300, # 301-399

    "consumable":   400, # 401-
}


class ObSubDict(dict):
    __slots__ = dict.__slots__ + "_keyname"
    def __init__(self, items, keyname):
        self._keyname = keyname
        super().__init__(self, items)

    @property
    def name(self): return self._keyname

    @property
    def primary_id(self): return OB_IDS[self._keyname]


class MetaDataBaseCls:
    ptype = ""
    _metatags = ""
    __slots__ = 'name', 'desc', 'subcats'
    def __init__(self, name, desc="" **kwargs):
        self.name = name
        self.desc = desc
        parse_kwarg()
        try: self._subcats = kwargs['subcats']
        except: self._subcats = ()
        try: self._inctags = kwargs['inctags']
        except: self._inctags = ()

    #@property
    #def primary_id(self): return OB_IDS[self.name]

    def catagories(self):
        yield self._ptype
        for i in self._subcats: yield i

    def catagory_names(self):
        yield self.ptype
        for i in self._subcats:
            try: yield i.name
            except: yield i


class BDObj:
    _meta = None
    _ob_set = None
    _bwt = 1.0      # Base weight must be float

    @property
    def meta(self):
        return self._meta

    def is_in_set(self):
        """True if this item is part of a set."""
        return self._objset is not None


class StorableObj(BDObj):
    _donatable = True
    _pawnable = True
    _tradable = True
    _resellable = False
    _resale_shoptypes = ()
    # minimum worth values
    _resale_mv = 1 # must be <= all other minimum worth values
    _pawn_mv = 1
    _trade_mv = 1

    _slotsize = 1    # number of slots when stored

    def resale_shoptypes(self):
        """Return an iterable of shoptypes that will buy this."""
        return iter(self._resale_shoptypes)

    def is_donatable(self):     return self._donatable
    def is_pawnable(self):      return self._pawnable
    def is_tradable(self):      return self._tradable
    def is_resellable(self):    return self._resellable

    def can_sell_to(self, buyer=None):
        """True if this can be sold to the given buyer. If buyer is
        'None', then returns True if this itemtype is allowed to be sold."""
        if (buyer is None or buyer.is_player):
            return self.is_tradable()
        else:
            try:
                if buyer.storetype() == 'pawn': return self.is_pawnable()
                else: return (self.is_resellable() and buyer.storetype()
                    in self.resale_shoptypes())
            except:
                return False


class Storage:
    _max_slots = 10
    def __init__(self):
        self._space = []

    def space_used(self):
        x = 0
        for i in self._space:
            x += i._slotsize

    def is_full(self):
        return self._max_slots == self.space_used()

    def space_remaining(self):
        return self._max_slots - self._space_used()

