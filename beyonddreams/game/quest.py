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
        return self[1]

    @property
    def state(self):
        return self[2]

    @property
    def statename(self):
        return QUEST_STATES[self[2]]

    def is_optional(self):
        return self[3]


class _QContainerCommon:
    # Mixin for Quest and (*QuestManager* see _QContainerCommonX)

    def not_started(self):
        """Return an iterator of all yet to be started items."""
        return iter(i for i in self if i.state == 0)

    def incomplete(self):
        """Return an iterator of all incomplete items."""
        return iter(i for i in self if i.state == 1)

    def completed(self):
        """Return an iterator of all completed items."""
        return iter(i for i in self if i.state == 2)

    def failed(self):
        """Return an iterator of all failed items."""
        return iter(i for i in self if i.state == 3)


class _QContainerCommonX(_QCommon, _QContainerCommon): pass


class QuestTask(tuple, _QuestCommon):
    def __init__(self, qid, name, optional=0, is_last=0):
        super().__init__((
            qid,
            name,
            0,      # state
            optional,
            is_last,
            ))

    def on_started_task(self):
        self[2] = 1

    def on_completed_task(self, qm):
        self[2] = 2
        qm.get_by_qid(self[qid]).update_state(2, self.is_optional(), self[4])

    def on_failed_task(self, qm):
        self[2] = 3
        if not self.is_optional():
            qm.get_by_qid(self[qid]).update_state(3, False)


class Quest(tuple, _QContainerCommonX):
    def __init__(self, qid, name):
        super().__init__((
            qid,
            name,
            0, # state
            0, # optional
            [], # tasks
            ))

    def update_state(self, taskstate, optional, is_last=False):
        if taskstate == 3: self[1] = 3 # failed
        elif taskstate == 2:
            if is_last:
                self[2] = 2 # completed
            # else: pass # TODO retrieve next task


    #@property #### is this still needed ####
    #def _state(self):
    #    if any(i.state == 3 for i in self.required_tasks()): return 3 #failed
    #    elif any(i.state == 2 for i in self.required_tasks()):
    #        # check if not started
    #        if all(i.state == 2 for i in self.required_tasks()): return 0
    #        return 1 # incomplete
    #    else: return 2 # completed

    def required_tasks(self):
        """Return an iterator of all non optional items."""
        return iter(i for i in self[4] if i.is_optional())

    def optional_tasks(self):
        """Return an iterator of all optional items."""
        return iter(i for i in self[4] if not i.is_optional())


class QuestManager(list, _QContainerCommon):
    def __init__(self):
        super().__init__([])

    def _get_by_qid(self, qid):
        for i in self:
            if i[0] == qid:
                return i
        raise ValueError("qid does not exist")

    def _ct_state(self, state):
        return len(i for i in self if i.state == state)

    def failed_count(self): return self._ct_state(3)
    def completed_count(self): return self._ct_state(2)
    def incomplete_count(self): return self._ct_state(1)
    def not_started_count(self): return self._ct_state(0)
