
    if check("the robot's gripper is not near the lever"):
        robot.grab("lever")
    if check("the robot's gripper is near the lever and the lever is not aligned with the robot's gripper"):
        robot.align("robot's gripper to lever")
    if check("the lever is aligned with the robot's gripper"):
        robot.rotate("lever up")