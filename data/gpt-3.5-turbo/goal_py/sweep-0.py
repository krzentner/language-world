# Steps:
#  1. Put gripper vertically above the cube
#  2. Open the gripper to allow for the cube to fit inside
#  3. Descend the gripper onto the cube
#  4. Close the gripper around the cube
#  5. Move the gripper with the cube sideways to the target location
#  6. Open the gripper to release the cube
# First, put the gripper vertically above the cube
if check("the robot's gripper is not vertically aligned with the cube"):
    robot.move_gripper("above the cube")
# If the gripper is above the cube, we can open the gripper to fit the cube
if check("the robot's gripper is above the cube and the robot's gripper is closed"):
    robot.move_gripper("above the cube", close_gripper=False)
# Lower the gripper to the cube and close the gripper to grab it
if check("the robot's gripper is above the cube and the robot's gripper is open"):
    robot.move_gripper("around the cube")
# Move the gripper and cube sideways to target location
if check("the robot's gripper is holding the cube and the cube is between the robot's gripper and the target location"):
    robot.move_gripper("above the target location")
# Release the cube by opening the gripper
if check("the robot's gripper is above the target location and the robot's gripper is holding the cube"):
    robot.move_gripper("above the target location", close_gripper=False)