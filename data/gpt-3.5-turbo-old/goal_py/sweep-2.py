# Steps:
#  1. Put gripper above cube
#  2. Drop gripper around the cube
#  3. Close gripper around the cube
#  4. Move cube to target location
#  5. Open gripper to release cube

# First, put the gripper roughly above the cube without touching the cube.
if check("the robot's gripper is not above the cube"):
    robot.move_gripper("above the cube")
# If the gripper isn't around the cube, put it around the cube.
if check("the robot's gripper is not around cube and the robot's gripper is open"):
    robot.move_gripper("near the cube", close_gripper=True)
# If the gripper is near the cube, we can probably grab it by closing the gripper.
if check("the robot's gripper is near the cube and the cube is below the robot's gripper"):
    # Make sure the gripper has a good grasp on the cube by closing it.
    robot.move_gripper("above the target location", close_gripper=True)
# If the gripper is above the target location, move the gripper down to the target location.
if check("the robot's gripper is above the target location and the robot's gripper is not near the target location"):
    robot.move_gripper("above the target location", close_gripper=False)
# Finally, release the cube by opening the gripper.
if check("the robot's gripper is above the target location and the gripper is closed"):
    robot.move_gripper("above the target location", close_gripper=False)