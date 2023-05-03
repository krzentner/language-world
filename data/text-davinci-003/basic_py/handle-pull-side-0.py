
    if check("the robot's gripper is not near the handle"):
        robot.grab("handle")
    if check("the robot's gripper is near the handle"):
        robot.pull("up on handle")