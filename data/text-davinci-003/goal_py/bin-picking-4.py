
    # Steps:
    #  1. Put gripper below cube
    #  2. Close gripper around cube
    #  3. Move cube to bin
    # First put the gripper below the cube.
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.move_gripper("vertically aligned with the cube", close_gripper=True)
    # Then close the gripper around the cube.
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is not closed"):
        robot.move_gripper("above the cube")
    # Then move the gripper to the target bin.
    if check("the robot's gripper is closed and the robot's gripper is above the cube"):
        robot.move_gripper("above the target bin")