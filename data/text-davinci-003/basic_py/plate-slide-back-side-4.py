
    if check("the robot's gripper is not left of the plate"):
        robot.move("gripper to left of plate")
    if check("the robot's gripper is near the plate and the plate is not aligned with the target location"):
        robot.slide("the plate sideways into the target location")
    if check("the robot's gripper is near the plate and the plate is almost aligned with the target location"):
        robot.push("the plate further into the target location")