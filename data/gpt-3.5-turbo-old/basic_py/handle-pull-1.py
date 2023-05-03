if check("the robot's gripper is not around the handle and the handle is down"):
        robot.grab("handle")
    if check("the robot's gripper is around the handle"):
        robot.pull("up on handle")