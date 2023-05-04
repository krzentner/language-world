

'''
import pytest
from sph_pyhelpers import (
    _, check,
)
from sph_pyhelpers_robot import (
    Action,
    robot,
)


class Robot:

    def __init__(self):
        self.gripper = Action()
        self.gripper.reset_to('closed')
        self.action = None

    def move_gripper(self, target, close_gripper=False, allow_repeat=True):
        self.gripper.set_action(
            target=target,
            closed=close_gripper,
            allow_repeat=allow_repeat
        )
        self.action = 'gripper'

    def check(self):
        if self.action == 'gripper':
            self.action = None
            return True
        else:
            return False


def _button_press_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")


def _drawer_open(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # We need to put the gripper above the drawer handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle")
    # Once the gripper is lined up above the drawer handle, we should be able to
    # grab the drawer handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned