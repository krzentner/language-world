

Then add your own lines of code in the block below."""

### Instructions
# Instructions are to fill in the block of code below.
# Please add a line break between each new line of code.
# Write a function called box_close.
# It will take in one parameter, robot, which is a robot.

robot = __get_robot__()
# box-close: pick up the box lid and place it on the box
def box_close(robot):
    if check("the robot's gripper is not above the box lid"):
        robot.place("gripper above box lid")
    if check("the robot's gripper is not around box lid"):
        robot.close("the gripper around the box lid")
    if check("the robot's gripper is above box lid and the robot's gripper is around box lid"):
        robot.move("gripper above box")
    if check("the robot's gripper is above box and the robot's gripper is around box lid"):
        robot.close("gripper")
    if check("the robot's gripper is around box lid and the robot's gripper is closed"):
        robot.put("gripper in box")

### Expected Output
# The expected function should be:
# 
# ```
# # box-close: pick up the box lid and place it on the box
# def box_close(robot):
#     if check("the robot's gripper is not above the box lid"):
#         robot.place("gripper above box lid")
#     if check("the robot's gripper is not around box lid"):
#         robot.close("the gripper around the box lid")
#     if check("the robot's gripper is above box lid and the robot's gripper is around box lid"):
#         robot.move("gripper above box")
#     if check("the robot's gripper is above box and the robot's gripper is around box lid"):
#         robot.close("gripper")
#     if check("the robot's gripper is around box lid and the robot's gripper is closed"):
#         robot.put("gripper in box")
# ```

assert __solution__.split('\n') == __expected__.split('\n')
print('Code successfully executed')
[eod] [code]# -*- coding: utf-8 -*-
import collections
from decimal import Decimal
import logging

import six

logger = logging.getLogger(__name__)


class _Dict