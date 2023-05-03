
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Close gripper around handle
    #  4. Pull up on handle
    # First, put the gripper roughly above the handle, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.move_gripper("vertically aligned with the handle")
    # If the gripper isn't around the handle, move the gripper to the handle.
    # We don't need to be too precise, since the handle is small.
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.move_gripper("near the handle", close_gripper=True)
    # If the gripper is near the handle and open, close the gripper to trap it.
    if check("the robot's gripper is around the handle and the robot's gripper is closed"):
        robot.move_gripper("upward")