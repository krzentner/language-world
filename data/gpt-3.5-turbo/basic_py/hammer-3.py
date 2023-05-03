if check("the hammer is not picked up by the robot"):
        robot.grab("hammer")
    if check("the robot's gripper is near the nail"):
        robot.swing("hammer")
    if check("the hammer is swung at the nail"):
        robot.hit("nail")