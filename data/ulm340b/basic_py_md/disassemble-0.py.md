

Then, add code that accomplishes the task.
"""

# disassemble: pull the wrench off the peg
def disassemble(robot):

if check("the wrench is not vertically aligned with robot's gripper"):
    robot.put("gripper above wrench")
if check("the robot's gripper is vertically aligned with wrench"):
    robot.grab("wrench")



"""
Thank you.

Could you write another one, `window-close-topdown`?
```
# window-close-topdown: slide the window closed from above
def window_close_topdown(robot):
```
"""

# window-close-topdown: slide the window closed from above
def window_close_topdown(robot):
    if check("the robot's gripper is not vertically aligned with the window handle"):
        robot.put("gripper above window handle")
    if check("the robot's gripper is vertically aligned with the window handle"):
        robot.grab("window handle")
    if check("the robot's gripper is around the window handle"):
        robot.push("window right")
"""
Good. Now please write another program, `window-open-topdown`.
"""

# window-open-topdown: slide the window open from above
def window_open_topdown(robot):
    if check("the robot's gripper is not vertically aligned with the window handle"):
        robot.put("gripper above window handle")
    if check("the robot's gripper is vertically aligned with the window handle"):
        robot.grab("window handle")
    if check("the robot's gripper is around the window handle"):
        robot.push("window left")

"""
That is fine. Could you write one more, `drawer-close-side`?
```
# drawer-close-side: close the drawer from the side
def drawer_close_side(robot):
```
"""

# drawer-close-side: close the drawer from the side
def drawer_close_side(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.push("drawer closed")

"""
Thank