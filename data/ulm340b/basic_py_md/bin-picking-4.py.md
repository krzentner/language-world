
"""

import random


class Environment(object):

    def __init__(self, description):
        self.description = description
        self._stepcount = 0

    def reset(self):
        self.description = self.description.lower()
        self._stepcount = 0
        self._progress = 0
        self._total = 0
        self._subtasks = {subtask: self._Subtask(self, subtask) for subtask in self.task_names()}

    def progress(self):
        return float(self._progress) / self._total

    def step(self, subtask):
        self._progress += 1
        if self._stepcount == 0:
            self._stepcount = 1
            return 'begin-subtask: ' + subtask
        if self._progress == self._total:
            self.reset()
            return 'end-subtask: ' + subtask
        return self._subtasks[subtask].step()

    def goal(self, subtask):
        return 'end-subtask: ' + subtask

    def task_names(self):
        return self._subtasks.keys()


class Subtask(object):

    def __init__(self, env, subtask, mdp_task):
        self.env = env
        self.description = subtask.lower()
        self.mdp_task = mdp_task
        self.progress = 0
        self.total = 0

    def progress(self):
        return float(self.progress) / self.total

    def step(self):
        self.progress += 1
        if self.progress == self.total:
            self.reset()
            return 'end-subtask: ' + self.description
        if self.progress == 0:
            return self.mdp_task.begin_message()
        return self.mdp_task.step(self.env)


#
#
# MDP tasks
#
#
def button_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")


def drawer_close(robot):
    if check("the robot's gripper is not