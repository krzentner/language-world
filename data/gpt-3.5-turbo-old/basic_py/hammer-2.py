    if check("the robot's gripper is not holding the hammer"):
        robot.grab("hammer")
    if check("the hammer is not above the nail"):
        robot.move("hammer above nail")
    if check("the hammer is above and near the nail"):
        robot.hit("nail with hammer")