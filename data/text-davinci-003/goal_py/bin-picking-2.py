
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move cube to the target bin
    # If the robot's gripper isn't near the cube, move it closer.
    if check("the robot's gripper is not near the cube"):
        robot.move_gripper("near the cube")
    # If the gripper is above the cube, we should be able to close the gripper
    # around the cube to grab it.
    if check("the robot's gripper is above cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is closed and around the cube, move the cube to the target
    # bin.
    if check("the robot's gripper is closed and around the cube"):
        robot.move_gripper("near the target bin")