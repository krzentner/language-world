


## Examples:

```
# ------------------------------------------------
# Simple push example
# ------------------------------------------------

def button_press_topdown(robot):
    # Because this is "topdown", we just need to line up the gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")

# ------------------------------------------------
# Push an object to the side example
# ------------------------------------------------

def peg_insert_side(robot):
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    # If the peg is lined up with the hole to the side, insert it.
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")
```
"""

import time
import math
import random
import sys
import malmoutils
import copy

sys.path.append(sys.argv[1])
import language.primitives

# Constants
MOVE_PENALTY = 0.5 # Penalty to apply when a move() action is required

def run_code(code, code_name, agent):
    try:
        malmoutils.evaluate_code_lines(code)
    except Exception as e:
        print 'Code threw an exception:\n%s' % (e,)
        raise e