
    # Steps:
    #  1. Put gripper around the handle
    #  2. Pull up the handle
    # 
    # First put the gripper around the handle.
    # Note that we don't need to line it up from above, since the handle is small.
    if check("the robot's gripper is not around handle"):
        robot.grab("handle")
    # Make sure the gripper is mostly lined up with the handle. We don't need to
    # be perfectly lined up, since the rotational degrees of freedom is limited.
    if check("the robot's gripper is of the handle and the robot's gripper is open"):
        robot.align("gripper to handle")
    # If the gripper is around the handle, pull the handle up.
    if check("the robot's gripper is around handle"):
        robot.pull("handle up")