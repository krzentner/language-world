
    # Steps:
    #  1. Put gripper left of the drawer handle
    #  2. Pull open the drawer
    # Put the gripper left of the drawer handle.
    if check("the robot's gripper is not left of drawer handle"):
        robot.move_gripper("left of the drawer handle", close_gripper=True)
    # Pull open the drawer.
    if check("the robot's gripper is left of drawer handle"):
        robot.move_gripper("forward aligned with drawer handle")