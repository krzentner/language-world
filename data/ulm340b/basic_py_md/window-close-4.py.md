

Your program will be run using the following objects:
```
robot
gripper
gripper_inside
window
window_inside
```
and the following relations:
```
forward
right
left
above
below
front_aligned
vertically_aligned
horizontally_aligned
near
forward_aligned
around
to_the_left_of
to_the_right_of
closed
open
'''

import time
import math
from collections import Counter
import numpy as np
import pandas as pd

df_1 = pd.DataFrame([
['# drawer-open: pull the drawer open',
 'def drawer_open(robot):',
 '    if check("the robot\'s gripper is not vertically aligned with drawer handle"):',
 '        robot.put("gripper above drawer handle")',
 '    if check("the robot\'s gripper is vertically aligned with drawer handle and the robot\'s gripper is not around drawer handle"):',
 '        robot.put("gripper around drawer handle")',
 '    if check("the robot\'s gripper is around drawer handle"):',
 '        robot.pull("away from drawer")',
],
['# reach: reach to the target location',
 'def reach(robot):',
 '    if check("the robot\'s gripper is not near reach target"):',
 '        robot.reach("to goal")',
],
['# button-press-topdown: push the button down from above',
 'def button_press_topdown(robot):',
 '    if check("the robot\'s gripper is not vertically aligned with button"):',
 '        robot.put("gripper above button")',
 '    if check("the robot\'s gripper is vertically aligned with button"):',
 '        robot.push("down on button")',
],
['# door-open: pull the door open',
 'def door_open(robot):',
 '    if check("the robot\'s gripper is not almost vertically aligned with door handle"):',
 '        robot.put("gripper above door handle")',
 '    if check("the robot\'s gripper is almost vertically aligned with the door handle and the robot\'s gripper is open"):',
 '        robot.put("gripper around door handle")',
 '    if check