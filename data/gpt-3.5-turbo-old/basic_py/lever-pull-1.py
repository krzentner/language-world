    if check("the robot's gripper is not near the lever handle"):
        robot.grab("lever handle")
    if check("the robot's gripper is below the lever handle"):
        robot.lift("lever up")