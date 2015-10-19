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

from properties import get_visible, set_visible


class BDOBrowserCommon:
    _browsertype = ""
    __slots__ = ()


class BDOBrowserSearch(BDBrowserCommon):
    _browsertype = ""
    def __init__(self, browser):
        self._browser = browser


class _BFuncs(list):
    # Shared by BDOBrowser and BDOBrowserSelection
    __slots__ = list.__slots__

    # invalidate some list methods
    def __imul__(self): raise NotImplementedError

    def hidden(self):
        """Return an iterator of all hidden items."""
        return iter(i for i in self if i._visible == False)

    def visible(self):
        """Return an iterator of all visible items."""
        return iter(i for i in self if i._visible)


class BDOBrowserSelection(_BFuncs, BDOBrowserCommon):
    __slots__ = _BFuncs.__slots__ + "_browser"
    def __init__(self, browser):
        self._browser = browser

    def is_multiple(self):
        """True if more than one item is selected."""
        return len(self) > 1

    def hide(self):
        """Hide the current selection."""
        for i in self:
            i.visible = False
        self.clear()

    def get_tags(self):
        t = set()
        for i in self:
            t.update(i.tags)


def _null(): raise NotImplementedError


class BDOBrowserAutoHide:
    __slots__ = ("_inctags", "_exctags")
    def __init__(self):
        self._inctags = set()
        self._exctags = set()


class BDOBrowser(_BFuncs, BDOBrowserCommon):
    __slots__ = _BFuncs.__slots__ + "_selected", "_searchfunc"
    def __init__(self, SelectedCls=None, SearchFuncCls=None):
        if SelectedCls is None: self._selected = _null
        else: self._selected = SelectedCls
        if SearchFuncCls is None: self._searchfunc = _null
        else: self._searchfunc = SearchFunCls

        self._autohide = None

    # Invalidate some list methods (inherited by _BFuncs)
    def clear(self): raise NotImplementedError

    @property
    def autohide_types(self):
        return self._autohide

    @property
    def selected(self):
        return self._selection

    def search(self):
        return self._searchfunc

    def get_menuitems(self):
        if any(i for i in self.hidden()): yield "unhide all"
        for i in self._menuitems_anysel(): yield i
        if len(self._selection) == 0:
            for i in self._menuitems_nonesel(): yield i
        elif len(self._selection) == 1:
            for i in self._menuitems_onesel(): yield i
            for i in self._selected.visible()[0]_menuitems_onesel(): yield i
        else:
            for i in self._menuitems_mulsel(): yield i
            for i in self._selected[0].visible()[0]_menuitems_mulsel()): yield i


    def _menuitems_anysel(self): yield

    def _menuitems_nonsel(self): yield

    def _menuitems_onesel(self): yield

    def _menuitems_mulsel(self): yield


class BDOBrowserItem(BDOBrowserCommon):
    __slots__ = "_visible"
    def __init__(self, obj):
        self._obj = obj
        self._visible = False

    @property
    def tags(self):
        return self._obj.tags

    visible = property(get_visible, set_visible)

    def _menuitems_onesel(self): yield
    def _menuitems_mulsel(self): yield
