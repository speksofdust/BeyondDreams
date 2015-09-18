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


from core.obbrowser import BDOBrowserSearch
from core.obbrowser import BDOBrowserSelection
from core.obbrowser import BDOBrowser
from core.obbrowser import BDOBrowserItem
from core.obbrowser import BDOBrowserAutoHide


class CharBrowserSearch(BDOBrowserSearch):
    def __init__(self, browser):
        BDOBrowserSearch.__init__(browser=browser)


class CharBrowserSelection(BDOBrowserSelection):
    _browsertype = "char"
    __slots__ = BDOBrowserSelection.__slots__
    def __init__(self):
        BDOBrowserSelection.__init__(self, browser=charbrowser):


class CharBrowserItem(BDOBrowserItem):
    _browsertype = "char"
    __slots__ = BDOBrowserItem.__slots__


class CharBrowserAutoHide(BDOBrowserAutoHide):
    pass


class CharBrowser(BDOBrowser):
    _browsertype = "char"
    __slots__ = BDOBrowser.__slots__
    def __init__(self):
        BDOBrowser.__init__(self, SelectedCls=CharBrowserSelection,
            SearchFuncCls=CharBrowserSearch)

    def _menuitems_nonsel(self):
        yield

    def _menuitems_onesel(self):
        yield

    def _menuitems_mulsel(self):
        yield



charbrowser = None
