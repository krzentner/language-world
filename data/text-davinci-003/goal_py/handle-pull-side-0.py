
    # Steps:
    #  1. Put gripper near handle
    #  2. Pull up on handle
    # First, put the gripper near the handle.
    # We don't need to worry about the angle because it's flat, so just move the
    # gripper near it from any direction.
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle")
    # If the handle is left of the gripper, just move the gripper back to the
    # handle to start pull it up.
    if check("the handle is left of the robot's gripper"):
        robot.move_gripper("right of the handle")
    # If the handle is right of the gripper, pull the handle up.
    if check("the handle is right of the robot's gripper"):
        robot.move_gripper("upwards aligned with the handle")