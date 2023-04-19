
    if check("the robot's gripper is not near the hammer"):
        robot.grab("hammer")
    if check("the robot's gripper is near the hammer and the hammer is not near the nail"):
        robot.move("hammer near nail")
    if check("the hammer is near the nail and the hammer is not above the nail"):
        robot.raise("hammer above nail")
    if check("the hammer is near the nail and the hammer is above the nail"):
        robot.strike("hammer onto nail")