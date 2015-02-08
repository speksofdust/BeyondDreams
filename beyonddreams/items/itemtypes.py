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


class ItemDict(BDTypeDict):

    def __init__(self):
        self._items = {}

    def _iterbycattype(self, cattype):
        return iter(i for i in self._items if i.CATTYPE == cattype)

    def consumables(self):
        return self._iterbycattype(CONSUMABLE)

    def wearables(self):
        return self._iterbycattype(WEARABLE)

    def weapons(self):
        return self._iterbycattype(WEAPONS)
        
        
def regitem(i):
    """Register an item with 'itemtypes'."""
    from .bdtypes import itemtypes
    itemtypes._items[i._name] = i
    
    
class ItemType:
    """Base class for all item types."""
    MAX_BUNDLE =    99    # Absolute max allowed bundle size
    CATTYPE =       ""    # Primary catagory type (CONSUMABLE, WEAPON, etc.)
    _inc_ttags =    ()    # typetags to be inherited
    _typetags =     ()    # tags to describe this item type
    _typename =     ""    # name for this item type
    typedesc =      ""
    BUNDLESIZE =    1
    ATTRIBS =       ()    # attribs for items when in inventory
    ALL_TYPE_ATTRIBS = () # all possible attribs for this type
    SLOTSIZE =      1     # base num slots taken in inventory
    _desc =         ""
    _bwt =          1.0   # base weight must be (float)

    @property
    def name(self):
        """The name of this item."""
        return self._name

    def typename(self):
        """The name of this item type."""
        if not self._typename: return self.__class__.__name__.lower()
        return self._typename

    def typetags(self):
        """Yield all type tags for this."""
        for i in self._inc_ttags: yield i
        for i in self._typetags: yield i
        yield self.TYPENAME
        yield self.CATTYPE
