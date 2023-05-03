# Steps:
    #  1. Put gripper around drawer handle
    #  2. Pull open the drawer
    # If the gripper is not near the drawer handle, move it to the drawer handle.
    # We need to be careful about the direction, since we're pulling the drawer
    # open.
    if check("the robot's gripper is not near the drawer handle"):
        robot.move_gripper("left of the drawer handle")
    # If the gripper is around the drawer handle, we can pull the drawer open.
    if check("the robot's gripper is around the drawer handle"):
        robot.move_gripper("almost vertically aligned with the drawer handle", close_gripper=True)