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


class UndoHist:
    __slots__ = "_history", "_max"
    def __init__(self, max):
        self._history = []
        self._max = int(max)
        if max < 1: max = 1
        
    def update(self, action):
        self._history.append(action)
        if len(self._history) < self._max:
            self._history.remove(self._history[-1])
        
    def clear(self):
        self._history = []
        
    def undo(self):
        pass
    
    def redo(self):
        pass
        

class CharEditor:
    def __init__(self, char=None):
        self._saved = True
        self._undohist = UndoHist(64)
        self._original = char
        if self._original is None:  self._editing = None
        else:                       self._editing = char.copy()
        
    def cleanup(self):
        self._undohist.clear
        
    def new_char(self):
        if self._saved == False:
            # save prompt stuff
            # p = GetPrompt("Don't Save", "Save", "Cancel"):
            # if p == 1: self.save
            # elif p == 2: return 
            return
        
        self._undohist.clear
        self._original = None
        from .char import _get_new_char
        self._editing = _get_new_char()
        
    def revert(self):
        """Revert changes to this char."""
        if self._original != None:
            self._undohist.clear
            self._editing = self._original.copy()
        
    def save(self, as_copy=False):
        if as_copy:
            pass
        else:
            self._original = self._editing
        
        self._saved = True
    
    
    
    


