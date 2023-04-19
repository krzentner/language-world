# Steps:
#  1. Put gripper above the mug
#  2. Grab the mug with the gripper
#  3. Line the mug up with the target location
#  4. Pull the mug towards the target location
# First, put the gripper above the mug.
if check("the robot's gripper is not vertically aligned with the mug"):
    robot.move_gripper("vertically aligned with the mug")
# If the gripper is above the mug, we can grab it.
if check("the robot's gripper is above the mug and the robot's gripper is not around the mug"):
    robot.move_gripper("around the mug", close_gripper=True)
# Once we have the mug, line it up with the target location.
if check("the robot's gripper is around the mug and the mug is not horizontally aligned with the target location"):
    robot.move_gripper("horizontally aligned with the target location")
# Finally, pull the mug towards the target location.
if check("the robot's gripper is horizontally aligned with the target location and the robot's gripper is not at the target location"):
    robot.move_gripper("at the target location")