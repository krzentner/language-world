
    # Steps:
    #  1. Put gripper above handle
    #  2. Push down the handle
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.move_gripper("vertically aligned with handle", close_gripper=True)
    # If the gripper is above the handle, we can just push down on it.
    if check("the robot's gripper is vertically aligned with handle"):
        robot.move_gripper("near the handle")