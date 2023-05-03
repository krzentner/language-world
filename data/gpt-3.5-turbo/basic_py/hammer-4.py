if check("the robot's gripper is not holding the hammer"):
        robot.grab("hammer")
    if check("the robot's gripper is holding the hammer and it is not above the nail"):
        robot.move("gripper above nail")
    if check("the hammer is above the nail and the hammer is not swung back"):
        robot.swing("hammer back")
    if check("the hammer is swung back and is above the nail"):
        robot.swing("hammer forward")