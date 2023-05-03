
    if check("the robot's gripper is not near plate"):
        robot.grab("plate")
    if check("the robot's gripper is near plate and the plate is not near goal"):
        robot.slide("plate to goal")
    if check("plate is near goal"):
        robot.push("plate into goal")