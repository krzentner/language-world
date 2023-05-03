# Steps:
#  1. Put gripper above the cube
#  2. Move the gripper down around the cube
#  3. Close the gripper around the cube
#  4. Move the cube towards the target location
#  5. Release the cube
# First, put the gripper above the cube.
if check("the robot's gripper is not above the cube"):
    robot.place("gripper above cube")
# Move the gripper down around the cube so that we can close the gripper around it.
if check("the robot's gripper is above the cube and the robot's gripper is not around the cube"):
    robot.move("gripper around cube")
# Close the gripper around the cube.
if check("the robot's gripper is around the cube and the robot's gripper is open"):
    robot.close("gripper around cube")
# Move the cube towards the target location.
if check("the robot's gripper is around the cube and the robot's gripper is not at the target location"):
    robot.move("cube to target location")
# Release the cube at the target location.
if check("the robot's gripper is around the cube at the target location"):
    robot.release("cube")