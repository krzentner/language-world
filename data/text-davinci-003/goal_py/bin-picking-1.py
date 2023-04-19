
    # Steps:
    #  1. Align gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move cube to target bin
    # First, roughly align the gripper with the cube.
    if check("the robot's gripper is not aligned with the cube"):
        robot.move_gripper("near the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.move_gripper("around the cube", close_gripper=True)
    # If the gripper is around the cube but not near the target bin, move
    # the gripper to the target bin.
    if check("the robot's gripper is around the cube and the robot's gripper is not near target bin"):
        robot.move_gripper("near the target bin")
    # If the gripper is near the target bin, we should be able to drop it in.
    if check("the robot's gripper is near target bin"):
        robot.move_gripper("above the target bin")