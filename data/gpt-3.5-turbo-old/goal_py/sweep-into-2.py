# Steps:
#  1. Put gripper above the cube
#  2. Use a sweeping motion to grab the cube
#  3. Move the gripper to the target location
#  4. Release the cube at the target location
# First, put the gripper above the cube.
if check("the robot's gripper is not vertically aligned with the cube"):
    robot.move_gripper("vertically aligned with the cube")
# Use a sweeping motion to grab the cube.
if check("the robot's gripper is above the cube and the robot's gripper is open"):
    robot.sweep_gripper("around the cube", close_gripper=True)
# Move the gripper to the target location.
if check("the robot's gripper is around the cube and the robot's gripper is not vertically aligned with the target location"):
    robot.move_gripper("vertically aligned with the target location")
# Release the cube at the target location.
if check("the robot's gripper is vertically aligned with the target location and the robot's gripper is closed"):
    robot.move_gripper("above the target location", open_gripper=True)