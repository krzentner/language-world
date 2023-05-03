
    if check("the robot's gripper is not near the lever"):
        robot.grab("lever")
    if check("the robot's gripper is near the lever and the lever is down"):
        robot.rotate("up")