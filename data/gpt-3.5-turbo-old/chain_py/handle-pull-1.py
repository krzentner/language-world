# Steps:
#  1. Put gripper around handle
#  2. Lift up on the handle
# We need to position the gripper around the handle before we can lift it up.
if check("the robot's gripper is not around the handle and the robot's gripper is open"):
    robot.grab("the handle")
# Once the gripper is around the handle, lift up on it.
if check("the robot's gripper is around the handle"):
    robot.lift("the handle")