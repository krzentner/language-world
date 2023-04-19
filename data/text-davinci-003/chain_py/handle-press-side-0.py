
    # Steps:
    #  1. Put gripper left of the handle
    #  2. Push down on the handle
    # We need to put the gripper left of the handle before pushing it.
    # This is so the robot can push down on the handle from the side.
    if check("the robot's gripper is not left of handle"):
        robot.put("gripper left of handle")
    # Once the gripper is lined up, just push down on the handle.
    if check("the robot's gripper is left of handle"):
        robot.push("down on handle")