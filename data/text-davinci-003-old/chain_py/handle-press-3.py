
    # Steps:
    #  1. Put gripper near the handle
    #  2. Push down on the handle
    # If the gripper is not near the handle, move it near the handle.
    if check("the robot's gripper is not near the handle"):
        robot.put("gripper near handle")
    # Now that the gripper is near the handle, just push down on it.
    if check("the robot's gripper is near the handle"):
        robot.push("down on handle")