# Steps:
#  1. Put gripper above handle
#  2. Grab handle with gripper
#  3. Pull handle up
# First, put the gripper above the handle.
if check("the robot's gripper is not above the handle"):
    robot.move("gripper to above handle")
# If the gripper isn't around the handle, put it around the handle.
if check("the gripper is not around the handle"):
    robot.grab("handle")
# Once the gripper is around the handle, pull the handle up.
if check("the gripper is around the handle"):
    robot.pull("handle up")