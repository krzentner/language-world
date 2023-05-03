
    if check("the robot's arm is not in front of the target"):
        robot.move("arm to in front of target")
    if check("the robot's arm is in front of the target"):
        robot.reach("arm to target")