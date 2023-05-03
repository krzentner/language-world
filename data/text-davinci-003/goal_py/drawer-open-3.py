
    # Steps:
    #  1. Put gripper left of the drawer handle
    #  2. Pull the drawer open
    # If the gripper isn't almost vertically aligned with the drawer handle,
    # move it to the drawer handle
    if check("the robot's gripper is not almost vertically aligned with drawer handle"):
        robot.move_gripper("almost vertically aligned with the drawer handle", close_gripper=True)
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is vertically aligned with the drawer handle"):
        robot.move_gripper("right of the drawer handle")