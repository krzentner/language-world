
    if check("the robot's gripper is not near the hammer and the hammer is not above the nail"):
        robot.grasp("hammer")
    if check("the robot's gripper is near the hammer and the hammer is not above the nail"):
        robot.put("hammer above the nail")
    if check("the hammer is above the nail"):
        robot.hit("the hammer")