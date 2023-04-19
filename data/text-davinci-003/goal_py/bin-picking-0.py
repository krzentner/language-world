
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move cube to goal
    # The robot needs to move the gripper above the cube, to avoid bumping the
    # cube while trying to grab it.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.move_gripper("around the cube", close_gripper=True)
    # If the gripper is around the cube, move it towards the target bin.
    if check("the robot's gripper is around the cube"):
        robot.move_gripper("above the target bin")