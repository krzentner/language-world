# Steps:
    #  1. Put gripper in front of drawer handle
    #  2. Push drawer closed
    # If the gripper is not in front of the drawer handle, move it there.
    if check("the robot's gripper is not in front of the drawer handle"):
        robot.move("gripper to front of drawer handle")
    # Once the gripper is in front of the drawer handle, we can push the drawer
    # closed.
    if check("the robot's gripper is in front of the drawer handle"):
        robot.push("drawer closed")