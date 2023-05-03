
    # Steps:
    #  1. Line up the gripper from the side
    #  2. Push down on the handle from the side
    # First, line up the robot's gripper from the side by moving it so it
    # becomes parallel with the handle.
    # Note that we don't need to line up the robot's gripper with the handle
    # down to the millimeter.
    if check("the robot's gripper is not side aligned with the handle"):
        robot.put("gripper side aligned with handle")
    # Once the robot's gripper is perpendicular with the handle, we can just
    # push down on the handle.
    if check("the robot's gripper is side aligned with the handle"):
        robot.push("down handle")