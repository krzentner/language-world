# Steps:
    #  1. Put gripper around the handle
    #  2. Push down on the handle
    # We need to put the gripper around the handle before we can push it down.
    if check("the robot's gripper is not around the handle"):
        robot.grab("handle")
    # Once the gripper is around the handle, we can just push down on it.
    if check("the robot's gripper is around the handle"):
        robot.push("down on handle")