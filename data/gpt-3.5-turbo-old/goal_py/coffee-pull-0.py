# Steps:
#  1. Put gripper above mug handle
#  2. Drop gripper around mug handle
#  3. Close gripper around mug handle
#  4. Move mug to target location
# First, put the gripper above the mug handle.
if check("the robot's gripper is not above mug handle"):
    robot.move_gripper("above mug handle")
# If the gripper isn't around the mug handle, put it around the handle.
if check("the robot's gripper is not around mug handle and the robot's gripper is open"):
    robot.move_gripper("near mug handle", close_gripper=True)
# If the gripper is around the mug handle, we can pull the mug to the target
# location.
# Close the gripper to make sure we keep control of the mug.
if check("the robot's gripper is around mug handle and the robot's gripper is not at target location"):
    robot.move_gripper("above the target location")