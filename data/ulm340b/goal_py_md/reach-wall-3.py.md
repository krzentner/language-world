

You'll need to write some code like the following:

```
if check("the robot's gripper is not close to reach target"):
    robot.move_gripper("almost vertically aligned with the reach target")
```

Note that you will need to refer to the object that blocks the gripper's motion as "wall".
"""

def reach_wall(robot):
    # Steps:
    #  1. Reach towards the target
    #  2. Move the arm right above the wall
    #  3. Reach the target location
    # We don't have any objects to manipulate, so we can just move the robot's
    # gripper directly to the target location
    if check("the robot's gripper is not almost near reach target"):
        robot.move_gripper("almost vertically aligned with the reach target")
    # If the robot's gripper is above the wall, we can reach the target location
    if check("the robot's gripper is vertically aligned with the reach target"):
        robot.move_gripper("almost right of the wall", close_gripper=True)
    # If the robot's gripper is below the wall, we can reach the target location
    if check("the wall is almost vertically aligned with the reach target"):
        robot.move_gripper("almost right of the wall")
    # As long as the robot's gripper is almost vertically aligned with the reach target, we can move the arm right of the wall to reach the target location
    if check("the robot's gripper is almost near reach target"):
        robot.move_gripper("close to reach target")
    # If the robot's gripper is below the wall, we can reach the target location
    if check("the wall is almost left of the robot's gripper"):
        robot.move_gripper("almost left of the wall")

[eod] [code]from tkinter import *
from tkinter import ttk


def search():

    def search(search_string):
        results = root.after(500,search)
        if results is None:
            return False
        if len(results) < 1:
            print('Results:None')
        for i in results:
            print(i)
        return False

def clear():
    pass

def set_search_string():