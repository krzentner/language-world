# Steps:
#  1. Put the gripper above the cube, away from the target location
#  2. Move the gripper down while rotating it to grab the cube
#  3. Use the gripper to push the cube into the target location
# First, put the gripper above the cube.
if check("the robot's gripper is not above the cube and the robot's gripper is not near the target location"):
    robot.move_gripper("above the cube")
# If the gripper is above the cube, move the gripper down and rotate it to grab
# the cube.
if check("the robot's gripper is above the cube"):
    robot.move_gripper("around the cube", close_gripper=True)
# Once the gripper has the cube, push it into the target location.
if check("the robot's gripper is holding the cube and the cube is not in the target location"):
    robot.move_gripper("above the target location")