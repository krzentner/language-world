

    # Put gripper roughly around the drawer handle
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    # Push the drawer closed
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")