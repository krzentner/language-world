# Steps:
#  1. Put gripper above the mug
#  2. Grab the mug with the gripper
#  3. Move the mug to the target location
# First, put the gripper above the mug.
if check("the robot's gripper is not vertically aligned with the mug"):
    robot.move_gripper("vertically aligned with the mug")
# If the gripper is above the mug, grab the mug with the gripper by closing it.
if check("the robot's gripper is vertically aligned with the mug and the robot's gripper is open"):
    robot.move_gripper("near the mug", close_gripper=True)
# If the gripper is near the mug with the mug inside, move the gripper to the target location.
if check("the robot's gripper is near the mug with the mug inside and the robot's gripper is closed"):
    robot.move_gripper("above the target location")