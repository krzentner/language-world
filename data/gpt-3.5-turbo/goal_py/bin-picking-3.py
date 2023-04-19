# Steps:
    #  1. Search for bin with the cube
    #  2. Move gripper above cube
    #  3. Close gripper around cube
    #  4. Move gripper above target bin
    #  5. Drop cube in bin
    # Search for the bin with the cube by moving the robot's arm.
    if check("the cube is not in view"):
        robot.move_arm("search for the cube")
    # If the cube is in view but not under the gripper, move the gripper above
    # the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the robot's gripper is above the cube but not around it, grab it.
    if check("the robot's gripper is above the cube and the robot's gripper is not around the cube"):
        robot.move_gripper("around the cube")
    # Once the gripper has the cube, move it above the target bin.
    if check("the robot's gripper is around the cube and not above the target bin"):
        robot.move_gripper("above the target bin")
    # Finally, drop the cube in the target bin.
    if check("the robot's gripper is above the target bin and closed"):
        robot.move_gripper("open above the target bin")