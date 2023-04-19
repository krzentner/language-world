# Steps:
#  1. Put gripper above cube
#  2. Grab cube with the gripper
#  3. Move gripper and cube to the target location
#  4. Release the cube
# First, put the gripper above the cube.
if check("the robot's gripper is not vertically aligned with the cube"):
    robot.move_gripper("vertically aligned with the cube")
# If the cube is not in the gripper, grab the cube by closing the gripper.
if check("the robot's gripper is not around the cube"):
    robot.move_gripper("above the cube", close_gripper=True)
# Move the gripper and cube to the target location.
if check("the robot's gripper is not near the target location"):
    robot.move_gripper("near the target location")
# Release the cube by opening the gripper.
if check("the robot's gripper is around the cube"):
    robot.move_gripper("above the current location", open_gripper=True)