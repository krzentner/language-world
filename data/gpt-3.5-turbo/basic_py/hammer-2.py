    if check("the robot's gripper is not holding the hammer and the hammer is not near the robot's gripper"):
        robot.grab("hammer handle")
    if check("the hammer is near the target nail and the hammer head is not aligned with the nail"):
        robot.align("hammer head to nail")
    if check("the hammer head is aligned with the nail and the hammer is above the nail"):
        robot.hit("the nail with the hammer")