
    # Steps:
    #  1. Put gripper near the drawer handle
    #  2. Pull open the drawer
    # Before pulling, we need to line up the gripper so it's centered on the
    # drawer handle or else we'll only be able to move it slightly.
    if check("the robot's gripper is not almost vertically aligned with drawer handle"):
        robot.move_gripper("almost vertically aligned with the drawer handle", close_gripper=True)
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is vertically aligned with the drawer handle"):
        robot.move_gripper("right of the drawer handle")