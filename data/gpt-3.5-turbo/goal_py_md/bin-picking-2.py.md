# bin-picking: pick up the cube and place it in the target bin
# def bin_picking(robot):

# Steps:
#  1. Move the gripper above the cube in the bin
#  2. Close the gripper around the cube
#  3. Lift the cube out of the bin
#  4. Move the gripper above the target bin
#  5. Move the gripper down to the target bin
#  6. Open the gripper to release the cube
# First, put the gripper roughly above the cube in the bin, so that we don't
# knock it over while trying to grab it.
if check("the robot's gripper is not above the cube in the bin"):
    robot.move_gripper("above the cube in the bin")
# If the gripper isn't around the cube, put it around the cube.
if check("the robot's gripper is not around the cube in the bin and the robot's gripper is open"):
    robot.move_gripper("near the cube in the bin", close_gripper=True)
# If the gripper is around the cube, lift the cube out of the bin.
if check("the robot's gripper is around the cube in the bin" and "the robot's gripper not lifted up"):
    robot.move_gripper("above the cube in the bin", raise_gripper=True)
# If the gripper is above the target bin and closed, drop the cube into the bin
if check("the robot's gripper is above the target bin and the robot's gripper is not closed"):
    robot.move_gripper("above the target bin")
if check("the robot's gripper is above the target bin and the robot's gripper is closed"):
    robot.move_gripper("in the target bin", raise_gripper=True, open_gripper=True)