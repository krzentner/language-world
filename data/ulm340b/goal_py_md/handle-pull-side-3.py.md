

Once you have written your program, please save it and copy its contents into the box below.

```
# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    # Steps:
    #  1. Put the gripper above the handle
    #  2. Close the gripper around the handle
    #  3. Pull up the handle
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    if check("the robot's gripper is above the handle"):
        robot.move_gripper("around the handle", close_gripper=True)
    if check("the robot's gripper is forward aligned with the handle"):
        robot.move_gripper("above the handle")
```
"""

"""


##### Code 8


def handle_pull_side(robot):
    # Steps:
    #  1. Put the gripper above the handle
    #  2. Close the gripper around the handle
    #  3. Pull up the handle
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    if check("the robot's gripper is above the handle"):
        robot.move_gripper("around the handle", close_gripper=True)
    if check("the robot's gripper is forward aligned with the handle"):
        robot.move_gripper("above the handle")


def handle_pull_side_2(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    if check("the robot's gripper is above the handle"):
        robot.move_gripper("around the handle", close_gripper=True)
    if check("the robot's gripper is forward aligned with the handle"):
        robot.move_gripper("above the handle")


def drawer_open(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # We need to put the gripper above