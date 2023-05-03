# Steps:
    #  1. Put gripper left of the drawer handle
    #  2. Pull the drawer open
    # If the gripper is not near the drawer handle, move it near the drawer handle
    # from the left.
    if check("the robot's gripper is not left of the drawer handle"):
        robot.move_gripper("left of the drawer handle")
    # If the gripper is left of the drawer handle, we can pull it open.
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.move_gripper("around the drawer handle")