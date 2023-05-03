
    # Steps:
    #  1. Put gripper above the cube
    #  2. Put gripper around the cube
    #  3. Close gripper to trap the cube
    #  4. Move cube to the target bin
    # Put the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the cube is in the wrong orientation, rotate it before trapsing it.
    if check("the cube is not vertically aligned with the robot's gripper"):
        robot.move_gripper("vertically aligned with the cube")
    # If the cube is correctly aligned, trap it by closing the gripper.
    if check("the cube is vertically aligned with the robot's gripper and the robot's gripper is not around the cube"):
        robot.move_gripper("around the cube", close_gripper=True)
    # Now that the gripper has the cube, we can just move it to the target bin.
    if check("the robot's gripper is holding the cube"):
        robot.move_gripper("above the target bin")