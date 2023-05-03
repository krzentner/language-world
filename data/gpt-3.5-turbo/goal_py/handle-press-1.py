# Steps:
    #  1. Put gripper above the handle
    #  2. Push down on the handle
    # First, put the gripper over the handle.
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("above the handle", close_gripper=True)
    # Once the gripper is above the handle, just push down on it.
    if check("the robot's gripper is near the handle"):
        robot.move_gripper("around the handle")