
    # Steps:
    #  1. Put gripper around handle
    #  2. Pull up the handle
    # Put the gripper around the handle.
    if check("the robot's gripper is not around handle"):
        robot.move_gripper("near the handle", close_gripper=True)
    # Once the gripper is around the handle, just pull the handle up.
    if check("the robot's gripper is around handle"):
        robot.move_gripper("above the handle")