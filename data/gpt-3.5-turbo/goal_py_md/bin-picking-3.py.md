# bin-picking: pick up the cube and place it in the target bin
# def bin_picking(robot):
    # Steps:
    #  1. Move the gripper above the cube
    #  2. Grab the cube with the gripper
    #  3. Move the gripper to the target bin
    #  4. Release the cube into the bin
    # First, put the gripper roughly above the cube, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is near the cube and closed, we've grabbed the cube.
    if check("the robot's gripper is near the cube and the robot's gripper is closed"):
        robot.move_gripper("above the target bin")
        robot.move_gripper("inside the target bin", open_gripper=True)