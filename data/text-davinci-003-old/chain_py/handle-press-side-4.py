
    # Steps:
    #  1. Put gripper perpendicular to the handle
    #  2. Push down on the handle
    # First, put the gripper perpendicular to the handle.
    if check("the robot's gripper is not perpendicular to the handle"):
        robot.put("gripper perpendicular to handle")
    # Now that the gripper is lined up, just push down on the handle.
    if check("the robot's gripper is perpendicular to the handle"):
        robot.push("down on handle")