# Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull up on the handle
    # First, put the gripper mostly above the handle.
    if check("the robot's gripper is not almost vertically aligned with handle"):
        robot.move_gripper("almost vertically aligned with the handle", close_gripper=True)
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is vertically aligned with handle"):
        robot.move_gripper("above the goal location")