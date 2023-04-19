
    # Steps:
    #  1. Put the gripper below the handle
    #  2. Pull up on the handle
    # First, put the gripper below the handle.
    if check("the robot's gripper is not below the handle"):
        robot.move_gripper("below handle", close_gripper=True)
    # If the handle is above the gripper, just pull the handle up
    if check("handle is above the fleamatic's gripper"):
        robot.move_gripper("above the handle")