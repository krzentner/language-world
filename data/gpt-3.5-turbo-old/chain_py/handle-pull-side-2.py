# Steps:
#  1. Put gripper beside the handle
#  2. Grab the handle with the gripper
#  3. Start pulling the handle up
#  4. Pull the handle up harder
# First, put the gripper beside the handle.
if check("the robot's gripper is not beside the handle and the robot's gripper is not above the handle"):
    robot.move("gripper beside handle")
# If the gripper is beside the handle, we can grab it.
if check("the robot's gripper is beside the handle and the robot's gripper is open"):
    robot.grab("handle")
# If the gripper is around the handle, we can start pulling it up.
if check("the robot's gripper is around the handle"):
    robot.pull("handle up")
# If the handle is starting to be lifted but not yet fully lifted, pull harder.
if check("the handle is partially lifted"):
    robot.pull("handle up harder")