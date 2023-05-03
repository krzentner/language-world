# Steps:
    #  1. Put gripper around the handle from the side
    #  2. Push down on the handle
    # Since we're pressing the handle from the side, we need to first get the
    # gripper around the handle.
    if check("the robot's gripper is not around handle from the side"):
        robot.put("gripper around handle from the side")
    # Once the gripper is around the handle, we can just push down on it.
    if check("the robot's gripper is around handle from the side"):
        robot.push("down on handle")