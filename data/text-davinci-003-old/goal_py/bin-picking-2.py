
    # Steps:
    #  1. Put gripper above the cube
    #  2. Grab the cube with the gripper
	#  3. Move the cube to the target bin
	#  4. Release the cube into the target bin
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is around the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.move_gripper("above the target bin")
    # If the gripper is near the cube and open, just drop it into the bin.
    if check("the robot's gripper is near the cube and the cube is above the target bin"):
        robot.move_gripper("above the target bin", open_gripper=True)