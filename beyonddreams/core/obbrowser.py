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


class BDObjectBrowserCommon:
    _browsertype = ""
    __slots__ = ()


class BDObjectBrowserSearch(BDObjectBrowserCommon):
    _browsertype = ""
    def __init__(self, browser):
        self._browser =         browser


class BDObjectBrowserSelection(list, BDObjectBrowserCommon):
    __slots__ = ("_browser")
    def __init__(self, browser):
        self._browser = browser
        self = []

    def is_multiple(self):
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


class BDObjectBrowser(list, BDObjectBrowserCommon):
    __slots__ = ("_selected", "_searchfunc")
    def __init__(self, SelectedCls=None, SearchFuncCls=None):
        self = []
        if SelectedCls is None: self._selected = _null
        else: self._selected = SelectedCls
        if SearchFuncCls is None: self._searchfunc = _null
        else: self._searchfunc = SearchFunCls

    @property
    def selected(self):
        return self._selection

    def hidden(self):
        """Return an iterator of all hidden items."""
        return iter(i for i in self if i._visible == False)

    def visible(self):
        """Return an iterator of all visible items."""
        return iter(i for i in self if i._visible)

    def search(self):
        return self._searchfunc


class BDBrowserItem(BDObjectBrowserCommon):
    __slots__ = "_visible"
    def __init__(self, obj):
        self._obj = obj
        self._visible = False

    @property
    def tags(self):
        return self._obj.tags

    def _get_visible(self): return self._visible
    def _set_visible(self, x): self._visible = bool(x)
    visible = property(_get_visible, _set_visible)
