
    # Steps:
    #  1. Put gripper near handle
    #  2. Pull up handle
    # To start, just move the gripper near the handle.
    # We don't need to be precise with the direction, since we'll be pulling
    # up the handle.
    if check("the robot's gripper is not near the handle"):
        robot.put("gripper near handle")
    # If the handle is forward of the gripper, we can just pull it up.
    if check("the handle is forward of the robot's gripper"):
        robot.pull("handle up")