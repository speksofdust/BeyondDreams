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


QUEST =         30
QUEST_COMPLETED = 31
QUEST_FAILED = 32
QUEST_ADDED = 33

QUEST_TASK_COMPLETED = 34
QUEST_TASK_FAILED = 35
QUEST_TASK_ADDED = 37

DEFAULT_QUEST_MGS_COLORS = {
    "quest_completed":          "#005DFF",
    "quest_failed":             "#991200",
    "quest_added":              "#934DCA",
    "quest_task_completed":     "#005DFF",
    "quest_task_failed":        "#991200",
    "quest_task_added":         "#934DCA",
}

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

    def not_started(self):
        """Return an iterator of all yet to be started items."""
        return iter(i for i in self if i._state = 0)

    def incomplete(self):
        """Return an iterator of all incomplete items."""
        return iter(i for i in self if i._state == 1)

    def completed(self):
        """Return an iterator of all completed items."""
        return iter(i for i in self if i._state = 2)

    def failed(self):
        """Return an iterator of all failed items."""
        return iter(i for i in self if i._state = 3)


class _QContainerCommonX(_QCommon, _QContainerCommon): pass


class QuestTask(_QuestCommon):
    def __init__(self, quest, name, optional=False, is_last=False):
        self._quest = quest
        self._state = 0
        self._name = name
        self._optional = bool(optional)
        self._is_last_task = False

    def on_started_task(self):
        self._state = 1

    def on_completed_task(self, qm):
        self._state = 2

    def on_failed_task(self, qm):
        self._state = 3


class Quest(tuple, _QContainerCommonX):
    def __init__(self, name):
        self._name = name

        super().__init__()

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

    def _ct_state(self, state):
        return len(i for i in self if i._state == state)

    def failed_count(self): return self._ct_state(3)
    def completed_count(self): return self._ct_state(2)
    def incomplete_count(self): return self._ct_state(1)
    def not_started_count(self): return self._ct_state(0)
