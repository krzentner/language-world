# Steps:
#  1. Put gripper above the mug handle
#  2. Drop gripper around the mug handle
#  3. Close gripper around handle
#  4. Pull mug to target location
# First, put the gripper above the mug handle, so that we don't bump it while
# trying to grab it.
if check("the robot's gripper is not above the mug handle"):
    robot.move_gripper("above the mug handle")
# If the gripper isn't around the mug handle, put it around the mug handle.
if check("the robot's gripper is not around the mug handle and the robot's gripper is open"):
    robot.move_gripper("near the mug handle", close_gripper=True)
# If the gripper is around the mug handle, grip and pull the mug to the target location.
if check("the robot's gripper is around the mug handle"):
    robot.move_gripper("above the target location")