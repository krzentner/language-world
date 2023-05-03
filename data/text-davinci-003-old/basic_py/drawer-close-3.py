
    if check("the robot's gripper is not near drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is in front of the drawer handle"):
        robot.push("drawer closed")