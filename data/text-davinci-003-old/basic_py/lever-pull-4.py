
    if check("the robot's gripper is not near the lever"):
        robot.grab("lever")
    if check("the robot's gripper is near the lever and the lever is not rotated up"):
        robot.rotate("lever up")
    if check("the robot's gripper is near the lever and the lever is rotated up"):
        robot.hold("lever up")