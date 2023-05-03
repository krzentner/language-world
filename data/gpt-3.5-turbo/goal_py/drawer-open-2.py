# Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Pull the drawer open
    # If the gripper is not near the drawer handle, move it to the drawer
    # handle.
    # We need to be careful about the direction, since we're pulling the drawer
    # open.
    if check("the robot's gripper is not near the drawer handle"):
        robot.move_gripper("right of the drawer handle")
    # If the drawer handle is left of the gripper and the gripper is mostly on
    # the front of the drawer handle, we can pull the drawer open.
    if check("the robot's gripper is forward aligned with drawer handle and the drawer handle is left of the robot's gripper"):
        robot.move_gripper("around the drawer handle")