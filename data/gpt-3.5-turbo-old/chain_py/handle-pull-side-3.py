# Steps:
#  1. Put gripper above handle
#  2. Grab the handle
#  3. Pull up on the handle
# First, put the gripper above the handle.
if check("the robot's gripper is not vertically aligned with the handle"):
    robot.put("gripper above handle")
# Once the gripper is above the handle, grab it.
if check("the robot's gripper is above handle and the robot's gripper is open"):
    robot.grab("handle")
# With the handle grabbed, pull it up.
if check("the robot's gripper is around handle"):
    robot.pull("handle up")