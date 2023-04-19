# Steps:
#  1. Put the gripper around the handle
#  2. Pull up on the handle from the side
#  3. Hold the handle in the pulled position
# First, put the gripper around the handle.
if check("the robot's gripper is not around the handle and the robot's gripper is open"):
    robot.move_gripper("around the handle", close_gripper=True)
# Once the gripper is around the handle, pull up on the handle from the side.
if check("the robot's gripper is around the handle and the robot's gripper is not vertically aligned with the handle"):
    robot.move_gripper("vertically aligned with the handle")
# Pull the handle up from the side.
if check("the robot's gripper is vertically aligned with the handle and the handle is not fully pulled up"):
    robot.move_gripper("horizontally aligned with the handle")