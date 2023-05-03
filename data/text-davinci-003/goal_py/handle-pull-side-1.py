
    # Steps:
    #  1. Put gripper above handle
    #  2. Grab handle with gripper
    #  3. Pull handle up
    # Put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # If the handle is left of the gripper, close the gripper around the handle.
    if check("the robot's gripper is not closed and the handle is left of the robot's gripper"):
        robot.move_gripper("around the handle", close_gripper=True)
    # Now that the gripper is closed, pull the handle up.
    if check("the robot's gripper is closed and the handle is not up"):
        robot.move_gripper("up")