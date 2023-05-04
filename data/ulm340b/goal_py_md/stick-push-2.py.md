

# > :fa-robot:
# >
# > Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.

Here's some code that demonstrates how the robot can do a variety of tasks:

```
# door-open: pull the door open
def door_open(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
    # First, put the gripper mostly above the door handle.
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.move_gripper("vertically aligned with the door handle")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the door handle"):
        robot.move_gripper("near the door handle")
    # If the gripper is near the door handle, we can probably pull it.
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.move_gripper("near the door handle")

# button-press-side: push the button from the side
def button_press_side(robot):
    # Steps:
    #  1. Put gripper above button
    #  2. Push the button from above
    # Put the gripper above the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button")
    # Put the gripper near the button, so that the gripper is not in front of the button anymore.
    if check("the robot's gripper is not near button"):
        robot.move_gripper("near button")

# drawers-open-all: open all drawers, one at a time
def drawers_open_all(robot):
    # Steps:
    #  1. Open each drawer one at a time
    # Open each drawer.
    if check("drawer is closed"):
        robot.move_gripper("almost vertically aligned with drawer handle", close_gripper=True)
    # If the drawer is almost vertically aligned with drawer handle, close it