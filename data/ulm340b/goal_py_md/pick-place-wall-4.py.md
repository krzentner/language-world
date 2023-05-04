

Now, imagine that you are the robot, that the target is to the left of where you start, and that there is a low wall blocking the puck from your gripper.

The first step is to get around the wall.
To get around a wall, you should move around the side of the wall, and then move to the target.
To move around a wall, use `robot.move_gripper("around the wall")`
"""


# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
def pick_place_wall(robot):
    # Steps:
    #  1. Move the gripper around the wall
    #  2. Pick up the puck and hold it at the target location
    if check("the robot's gripper is in front of the puck and the puck is on the other side of the wall"):
        robot.move_gripper("around the wall")
    if check("the puck is near the robot's gripper and the puck is on the same side of the wall as the robot's gripper"):
        robot.move_gripper("above the puck")
    if check("the robot's gripper is above puck and the robot's gripper is open and the puck is near the robot's gripper"):
        robot.move_gripper("near the puck", close_gripper=True)
    if check("the robot's gripper is above puck and the robot's gripper is closed and the puck is in the robot's gripper"):
        robot.move_gripper("near the target location")


if __name__ == "__main__":
    print("Done")[eod] [code]# Copyright (c) 2019 Uber Technologies, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for the base class of hyperparameter search methods."""
from __future__ import absolute_import, division, print_function

import unittest

from bayesmark.space import *
from bayesmark.methods