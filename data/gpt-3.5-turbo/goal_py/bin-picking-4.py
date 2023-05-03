# Steps:
    #  1. Move gripper to above the cube
    #  2. Move gripper down to the cube
    #  3. Grab the cube with the gripper
    #  4. Move gripper to above the target bin
    #  5. Move gripper down to the target bin
    #  6. Release the cube into the target bin
    # First, move the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper is above the cube, move it down to the cube
    if check("the robot's gripper is above the cube"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is around the cube, move it to above the target bin
    if check("the robot's gripper is around the cube"):
        robot.move_gripper("above the target bin")
    # If the gripper is above the target bin, move it down to the target bin
    if check("the robot's gripper is above the target bin"):
        robot.move_gripper("near the target bin")
    # If the gripper is near the target bin, release the cube into the target bin
    if check("the robot's gripper is near the target bin"):
        robot.move_gripper("above the cube")  # move gripper back up
        robot.move_gripper("open")  # release cube into target bin