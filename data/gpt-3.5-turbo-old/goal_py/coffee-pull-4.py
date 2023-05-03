# Steps:
#   1. Put gripper above the mug
#   2. Grab the mug handle with the gripper
#   3. Move the mug to the target location
# The following assumes the mug handle is on the right side of the mug.
# First, put the gripper above the mug handle.
if check("the robot's gripper is not vertically aligned with the mug handle"):
    robot.move_gripper("vertically aligned with the mug handle")
# If the gripper is vertically aligned with the mug handle, grab the mug handle.
if check("the robot's gripper is vertically aligned with the mug handle and the gripper is not around the mug handle"):
    robot.move_gripper("around the mug handle")
# If the gripper is around the mug handle, move the mug to the target location.
if check("the robot's gripper is around the mug handle and the gripper is not near the target location"):
    robot.move_gripper("above the target location")