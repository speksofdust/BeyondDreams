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

QUEST_STATES = ("not started", "incomplete", "completed", "failed")

class _QCommon:
    # Mixin for Quest and QuestTask
    @property
    def name(self):
        return self._name

    @property
    def statename(self):
        return QUEST_STATES[self._state]


class _QContainerCommon:
    # Mixin for Quest and (*QuestManager* see _QContainerCommonX)
    def completed(self):
        """Return an iterator of all completed items."""
        return iter(i for i in self if i._state = 2)

    def not_started(self):
        """Return an iterator of all items that have not yet been started."""
        return iter(i for i in self if i._state = 0)

    def failed(self):
        """Return an iterator of all items that have been failed."""
        return iter(i for i in self if i._state = 3)


class _QContainerCommonX(_QCommon, _QContainerCommon): pass


class QuestTask(_QuestCommon):
    def __init__(self, name, optional=False):
        self._state = 0
        self._name = name
        self._optional = bool(optional)


class Quest(tuple, _QContainerCommonX):
    def __init__(self, name):
        self._name = name
        self = ()

    @property
    def _state(self):
        if any(i._state == 3 for i in self.required_tasks()): return 3 #failed
        elif any(i._state == 2 for i in self.required_tasks()):
            if all(i._state == 2 for i in self.required_tasks(): return 0 #not started
            return 1 # incomplete
        else: return 2 # completed

    def required_tasks(self):
        """Return an iterator of all non optional items."""
        return iter(i for i in self if i._optional == False)

    def optional_tasks(self):
        """Return an iterator of all optional items."""
        return iter(i for i in self if i._optional)


class QuestManager(list, _QContainerCommon):
    def __init__(self):
        self = []

    def incomplete(self):
        """Return an iterator of all incomplete items."""
        return iter(i for i in self if i._state = 1)

