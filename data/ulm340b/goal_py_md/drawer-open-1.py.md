

The task is to *open* the drawer (pulling the gripper *away* from the target).
I will run the code and show you whether the program worked or not.
"""

def drawer_open(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # First, put the gripper mostly above drawer handle.
    if check("the robot's gripper is not almost vertically aligned with drawer handle"):
        robot.move_gripper("almost vertically aligned with the drawer handle", close_gripper=True)
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is vertically aligned with drawer handle"):
        robot.move_gripper("left of the drawer handle")

# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # First, put the gripper mostly above drawer handle.
    if check("the robot's gripper is not almost vertically aligned with drawer handle"):
        robot.move_gripper("almost vertically aligned with the drawer handle", close_gripper=True)
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is vertically aligned with drawer handle"):
        robot.move_gripper("left of the drawer handle")

"""
Thanks. Please wait while I run the program.
...
Program succeeded.

We're almost done. Please write a short summary of your actions:

```
summary_drawer_open
```
"""

summary_drawer_open = """
# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # First, put the gripper mostly above drawer handle.
    if check("the robot's gripper is not almost vertically aligned with drawer handle"):
        robot.move