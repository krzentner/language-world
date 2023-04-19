
    # Steps:
    #  1. Put gripper above handle
    #  2. Push the handle down
    # We need to put the gripper above the handle before we can push it down.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    # As long as the gripper is aligned with the handle from the top, we can
    # safely push down on it.
    if check("the robot's gripper is vertically aligned with handle"):
        robot.push("handle down")