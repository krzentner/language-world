



```
# door-lock: turn the dial on the door
def door_lock(robot):
    # Steps:
    #  1. Put gripper above the door handle
    #  2. Move gripper around the door handle
    #  3. Start turning
    #  4. Turn door handle right
    # If the gripper is not above the door handle, move it to be above the door handle.
    if check("the robot's gripper is not above door handle"):
        robot.move_gripper("above door handle")
    # If the robot's gripper is not around door handle, close the gripper around the door handle.
    if check("the robot's gripper is not around door handle and the robot's gripper is not closed"):
        robot.move_gripper("above door handle", close_gripper=True)
    # If the gripper is around the door handle, start to turn the dial.
    if check("the robot's gripper is above the door handle"):
        robot.move_gripper("to the right")
```

The robot will now attempt `door-lock`, and I will let you know how it went!


# ---


# ./code/tasks.py

import numpy as np

class Task:
    def __init__(self):
        pass
    def step(self, robot):
        pass
    def completed(self, robot):
        pass
    def __repr__(self):
        return self.name


# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Push the drawer closed
    # If the gripper is not near the drawer handle, move it to the drawer
    # handle.
    # We don't need to be careful about the direction, since the drawer is large
    # and we're just pushing it (unlike when opening the drawer).
    if check("the robot's gripper is not near the drawer handle"):
        robot.move_gripper("near the drawer handle")
    # If the drawer is aligned with the gripper as seen from in front, we can
    # push the drawer closed.
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.move_gripper