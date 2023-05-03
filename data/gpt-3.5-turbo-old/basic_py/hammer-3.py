    if check("the robot's gripper is not holding the hammer"):
        robot.grab("hammer")
    if check("the hammer is not above the nail"):
        robot.move("hammer above the nail")
    if check("the hammer is above the nail and the hammer is not touching the nail"):
        robot.lower("hammer onto the nail")
    if check("the hammer is touching the nail"):
        robot.swing("hammer to hit the nail")