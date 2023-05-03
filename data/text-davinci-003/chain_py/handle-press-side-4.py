
    # Steps:
    #  1. Put gripper above the handle
    #  2. Push the handle down
    #  Put the gripper roughly above the handle, so that we don't bump it while
    # trying to push it.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    # If the gripper is lined up with the handle, just push down on the handle.
    if check("the robot's gripper is vertically aligned with handle"):
        robot.push("down on handle")