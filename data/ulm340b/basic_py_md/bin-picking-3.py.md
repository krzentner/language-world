

Please use the following robot commands:
`robot.put(string)`: place the robot gripper at the location indicated by the `string`.

`robot.drop(string)`: drop the robot gripper to the location indicated by the `string`.

`robot.move(string)`: move the robot gripper to the location indicated by the `string`.

`robot.align(string)`: align the robot gripper to the location indicated by the `string`.

`robot.close(string)`: close the robot gripper around the object indicated by the `string`.

`robot.grab(string)`: move the robot gripper to grab the object indicated by the `string`.

`robot.reach(string)`: move the robot gripper to reach for the target location indicated by the `string`.

`robot.slide(string)`: slide the object indicated by the `string`.

`robot.push(string)`: push the object indicated by the `string`.

`robot.insert(string)`: insert the object indicated by the `string`.

`robot.pick(string)`: pick up the object indicated by the `string`.

`robot.place(string)`: place the object indicated by the `string`.

`robot.pull(string)`: pull the object indicated by the `string`.

`robot.rotate(string)`: rotate the robot gripper along the object indicated by the `string`.

For example, here is one possible code for `bin_picking`:

```
# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):
    if check("the robot's gripper is not open and the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is above the cube"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is near cube"):
        robot.close("gripper around cube")
    if check("the robot's gripper is around cube"):
        robot.move("gripper above target")
    if check("the robot's gripper is above target"):
        robot.drop("gripper around target")
    if check("the robot's gripper is near target"):
        robot.place("cube in bin")
```
[eod] [code]#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
import time
from pymysql import cursors
