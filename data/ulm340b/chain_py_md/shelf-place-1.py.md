
"""

import re

def task(robot):
    #  1. Put gripper above block
    if check("the robot's gripper is not above the block"):
        robot.place("gripper above block")
    #  2. Grab the block
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.drop("gripper around block")
    #  3. If the gripper is near the block and open, maybe we can grab it by closing the gripper.
    if check("the robot's gripper is near block and the robot's gripper is open"):
        robot.close("gripper around block")
    #  4. Move block to goal
    if check("the robot's gripper is above block and the robot's gripper is closed"):
        robot.place("block at goal")

# shelf-place: pick up the block and place it at the target location
def shelf_place(robot):
    task(robot)

#
# Tasks
#

# Push the drawer closed
def drawer_close(robot):
    # Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Push the drawer closed
    # If the gripper is not near the drawer handle, move it to the drawer handle.
    # We don't need to be careful about the direction, since the drawer is large
    # and we're just pushing it (unlike when opening the drawer).
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    # If the drawer is aligned with the gripper as seen from in front, we can
    # push the drawer closed.
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")

# Push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):