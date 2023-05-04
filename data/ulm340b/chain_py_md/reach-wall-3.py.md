

and then fill in the function definition to have the desired behavior.

The program is supposed to be able to grab the wall and move it out of the way so it can reach the target.

You may want to use the following:

```
check_wall = check("wall is visible")
```

```
print(reach_wall(robot))
```
'''

def reach_wall(robot):
    # Reach towards the target
    if check("the robot's gripper is not near reach target"):
        robot.reach("to goal")
    # Step 1: reach toward the wall
    if check("wall is visible"):
        robot.reach("to wall")
    # Step 2: put the gripper over the wall
    if check("the robot's gripper is not above the wall"):
        robot.put("gripper above wall")
    # Step 3: put the gripper around the wall
    if check("the robot's gripper is not around wall and the robot's gripper is open"):
        robot.drop("gripper around wall")
    # Step 4: close the gripper around the wall
    if check("the robot's gripper is near wall and the robot's gripper is open"):
        robot.close("gripper around wall")
    # Step 5: push the wall to the side of the reach target
    if check("the robot's gripper is above wall and the robot's gripper is closed"):
        robot.slide("wall to side of reach target")

# print(reach_wall(robot))
# print(reach_wall(robot))
# print(reach_wall(robot))
# print(reach_wall(robot))
# print(reach_wall(robot))
# print(reach_wall(robot))
# print(reach_wall(robot))
# print(reach_wall(robot))
# print(reach_wall(robot))
# print(reach_wall(robot))
# print(reach_wall(robot))
# print(reach_wall(robot))
# print(reach_wall(robot))
# print(reach_wall(robot))
# print(reach_wall(robot))
# print(reach_wall(robot))

[eod] [code]#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
import tkFont

#
# Globals
#

myFont = tkFont.Font(family='Helvetica', size