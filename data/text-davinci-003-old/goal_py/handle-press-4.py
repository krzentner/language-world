
    # Steps:
    #  1. Put gripper above handle
    #  2. Push down on handle
    # Because this problem is similar to the button press, we need to put the
    # gripper above the handle first.
    if check("the robot's gripper is not almost vertically aligned with the handle"):
        robot.move_gripper("almost vertically aligned with the handle", close_gripper=True)
    # Once the gripper is lined up above the handle, we should be able to push
    # down on it.
    if check("the robot's