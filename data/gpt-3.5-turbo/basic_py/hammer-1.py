if check("the robot's gripper does not hold the hammer"):
        robot.pick("up hammer")
    if check("the robot's gripper is not above the nail"):
        robot.move("to nail")
    if check("the hammer is above the nail and the hammer is not touching the nail"):
        robot.drop("hammer onto nail")