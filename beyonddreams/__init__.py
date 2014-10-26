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

if __name__ == "__main__":
    #import xsquare
    
    # TODO set BD_GLOBALS_PATH by operating system
    
    
BD_GLOBALS_PATH = ""

session = None

class Session:
    __slots__ = "_user", "_globvars"
    def __init__(self, firstrun):
        from globvars import GlobVars
        from user import User

        #self._globvars = GlobVars(BD_GLOBALS_PATH)
        self._user = User()
        
    def quit(self):
        self._globvars.update
        self._user.logout("q")
        
            
    
    
    
    
    
    
    
    
    
    
    
    
