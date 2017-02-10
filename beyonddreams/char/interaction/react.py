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


class Reaction:
    def __init__(self, id, delay=10):
        self.id = id

    def envoke(self, char, intensity): pass

AFFINITY_NEW = [
    0, # char
    0, # affinity score (-999 to 999)
    0, #
    0, #
    0] #

reactions = {
    "disgust":  Reaction(),
    "gag":      Reaction(),
    "pleased":  Reaction(),
    "displeased":   Reaction(),
    "shiver":   Reaction(),
    "cough":    Reaction(),
    "pleasure":    Reaction(),
    "pain":     Reaction(),
    }

def _envoke_reaction(cls, char, name, intensity):
    cls[name].envoke(char, intesity)

#def _get_reaction(cls, action, intensity):
    #if action ==
        #reactions.envoke("disgust", intensity)
        #reactions.envoke("gag", intensity)
        #reactions.envoke("pleased", intensity)
        #reactions.envoke("displeased", intensity)
        #reactions.envoke("shiver", intensity)
        #reactions.envoke("cough", intensity)
        #reactions.envoke("pleasure", intensity
        #reactions.envoke("pain", intensity)

reactions.envoke = _envoke_reaction
#reactions.get_reaction = _get_reaction

