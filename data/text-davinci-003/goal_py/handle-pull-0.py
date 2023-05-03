
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull up handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle", close_gripper=True)
    # Once the gripper is lined up we can move the gripper down to grab the
    # handle.
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is not around handle"):
        robot.move_gripper("around the handle")
    # Now that the gripper is around the handle, pull it up.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("upward")