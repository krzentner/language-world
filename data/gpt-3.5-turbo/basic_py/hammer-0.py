    if check("the hammer is not in the robot's gripper"):
        robot.grab("hammer")
    if check("the hammer is in the robot's gripper and the hammer is not above the nail"):
        robot.move("gripper above nail")
    if check("the hammer is above the nail and the hammer is not tilted"):
        robot.tilt("hammer towards nail")
    if check("the hammer is tilted and the hammer is not near the nail"):
        robot.move("gripper near nail")
    if check("the hammer is near the nail and the hammer is tilted"):
        robot.hit("nail with hammer")