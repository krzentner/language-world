# Steps:
    #  1. Put gripper above drawer handle
    #  2. Push drawer closed
    # To close the drawer, the robot just needs to push it closed. First, put the
    # gripper above the drawer handle to align it.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    # Once the gripper is aligned, we can push the drawer closed.
    if check("the robot's gripper is vertically aligned with drawer handle"):
        robot.push("drawer closed")