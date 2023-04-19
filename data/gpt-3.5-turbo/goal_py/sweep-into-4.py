# Steps:
#  1. Move gripper to be above the cube and start closing it
#  2. Trap the cube in the gripper and lift it up
#  3. Move the gripper to the target location and release the cube
# Move the gripper to be above the cube and start closing it.
if check("the robot's gripper is not above the cube"):
    robot.move_gripper("above the cube")
if check("the robot's gripper is above the cube and the robot's gripper is open"):
    robot.move_gripper("near the top of the cube", close_gripper=True)
# Trap the cube in the gripper and lift it up.
if check("the cube is below the robot's gripper"):
    robot.move_gripper("above the target location")
# Move the gripper to the target location and release the cube.
if check("the robot's gripper is near the target location"):
    robot.move_gripper("near the target location", open_gripper=True)