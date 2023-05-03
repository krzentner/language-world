# Steps:
    #  1. Put gripper above handle
    #  2. Push down on the handle
    # First, put the gripper mostly above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above handle")
    # Once the gripper is above the handle we can just push down on it.
    if check("the robot's gripper is above the handle"):
        robot.push("down on the handle")