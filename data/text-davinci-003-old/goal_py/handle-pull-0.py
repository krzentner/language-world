
    # Steps:
    #  1. Put gripper in line with handle
    #  2. Pull handle up
    # We need to move the gripper in line with the handle before we can pull it.
    # Line up gripper as viewed from the side.
    if check("the robot's gripper is not horizontally aligned with handle"):
        robot.move_gripper("horizontally aligned with handle", close_gripper=True)
    # Now that the gripper is lined up, just pull the handle up.
    if check("the robot's gripper is horizontally aligned with handle"):
        robot.move_gripper("above the handle")