
    # Steps:
    #  1. Put gripper above the handle
    #  2. Push down on the handle
    # Put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.move_gripper("vertically aligned with the handle", close_gripper=True)
    # Once the gripper is above the handle, push down on it.
    if check("the robot's gripper is vertically aligned with handle"):
        robot.move_gripper("near the handle")