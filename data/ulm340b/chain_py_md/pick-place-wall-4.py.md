

and fill in lines below it so that the code runs correctly.

(To run the code, click `Test Run` above.)

(If you don't understand what the program should be doing, ask.)

```
# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck above short wall
    #  5. Drop puck to goal
    # If the robot's gripper is not above the puck, put it there.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # If the gripper is not around the puck, drop it there.
    if check("the robot's gripper is not around the puck"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck, maybe we can close it.
    if check("the robot's gripper is near the puck"):
        robot.close("gripper around puck")
    # We closed the gripper, so maybe we can move the puck above the wall.
    if check("the robot's gripper is above the puck and the robot's gripper is closed"):
        robot.move("puck above wall")
    # We moved the puck to above the wall, so maybe we can move it near the
    # goal.
    if check("the robot's gripper is above wall"):
        robot.drop("puck near goal")
```
"""
from bisect import bisect, bisect_left

def is_in(x, a):
    "Is x in array a?"
    if x in a:
        return True
    else:
        return False

def is_not_in(x, a):
    "Is x not in array a?"
    if not(x in a):
        return True
    else:
        return False

def check(condition):
    "Checks whether condition (string) holds on the world state."
    if condition == 'the robot\'s gripper is closed':
        return True
    elif condition == 'the