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


from core.obbrowser import BDObjectBrowserSearch
from core.obbrowser import BDObjectBrowserSelection
from core.obbrowser import BDObjectBrowser
from core.obbrowser import BDObjectBrowserItem


class CharBrowserSearch(BDObjectBrowserSearch):
    def __init__(self, browser):
        BDObjectBrowserSearch.__init__(browser=browser)


class CharBrowserSelection(BDObjectBrowserSelection):
    _browsertype = "char"
    __slots__ = BDObjectBrowserSelection.__slots__
    def __init__(self):
        BDObjectBrowserSelection.__init__(self, browser=charbrowser):


class CharBrowserItem(BDObjectBrowserItem):
    _browsertype = "char"
    __slots__ = BDObjectBrowserItem.__slots__


class CharBrowser(BDObjectBrowser):
    _browsertype = "char"
    __slots__ = BDObjectBrowser.__slots__
    def __init__(self):
        BDObjectBrowser.__init__(self, SelectedCls=CharBrowserSelection,
            SearchFuncCls=CharBrowserSearch)


charbrowser = None
