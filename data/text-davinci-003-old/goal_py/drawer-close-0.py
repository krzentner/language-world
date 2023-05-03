
    # Steps:
    #  1. Put gripper around drawer handle
    #  2. Push the drawer closed
    # If the gripper isn't already around the drawer handle, move it there.
    if check("the robot's gripper is not around drawer handle"):
        robot.move_gripper("around the drawer handle")
    # If the gripper is around the drawer handle, just push it closed.
    if check("the robot's gripper is around drawer handle"):
        robot.move_gripper("right of the drawer handle")