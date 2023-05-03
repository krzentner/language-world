
    if check("the handle is not left of the robot's gripper and the handle is not forward aligned with the robot's gripper"):
        robot.grab("handle")
    if check("the robot's gripper is forward aligned with handle"):
        robot.pull("upward on handle")