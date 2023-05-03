
    # Steps:
    #  1. Put gripper to the side of the handle
    #  2. Push down on the handle
    # To press the handle from the side, we need to move the robot's gripper to the side of the handle.
    if check("the robot's gripper is not horizontally aligned with the handle"):
        robot.put("gripper to the side of the handle")
    # Now that the gripper is near the handle, we can press down on it.
    if check("the robot's gripper is horizontal aligned with the handle"):
        robot.push("down on the handle")