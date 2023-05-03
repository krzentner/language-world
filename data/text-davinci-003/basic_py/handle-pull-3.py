
    if check("the handle is not near and forward aligned with the robot's gripper"):
        robot.grab("handle")
    if check("the handle is near and forward aligned with the robot's gripper"):
        robot.pull("handle")