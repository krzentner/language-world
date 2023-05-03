# bin-picking: pick up the cube and place it in the target bin
# def bin_picking(robot):

# First, the robot needs to locate the cube in the bin. We can assume that the robot's camera
# can detect the cube and provide its location.
# If the cube is not in the gripper, the robot should move above the cube.
if check("the robot's gripper is not around cube"):
    robot.move_gripper("above the cube")

# Then, the robot should lower the gripper to grab the cube.
if check("the robot's gripper is above the cube"):
    robot.move_gripper("around the cube", close_gripper=True)

# The robot should then lift the cube off the bin.
if check("the robot's gripper is around cube"):
    robot.move_gripper("above the target bin")

# Finally, the robot should release the cube into the target bin.
if check("the robot's gripper is above the target bin"):
    robot.move_gripper("open") 

# End of task.