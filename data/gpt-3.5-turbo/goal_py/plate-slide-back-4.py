# Steps:
#  1. Put gripper above the plate handle
#  2. Drop gripper around the handle
#  3. Slide the plate back
# First, put the gripper above the plate handle so that we can grab it.
if check("the robot's gripper is not vertically aligned with the plate handle"):
    robot.move_gripper("vertically aligned with the plate handle")
# If the gripper is above the handle, we can drop it around the handle to grab
# it.
if check("the robot's gripper is vertically aligned with the plate handle and the robot's gripper is not around the plate handle"):
    robot.move_gripper("around the plate handle", close_gripper=True)
# If the plate is grabbed by the gripper, we can slide it back.
if check("the robot's gripper is around the plate handle"):
    robot.move_gripper("horizontally aligned with the target location")