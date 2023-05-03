if check("the robot's gripper is not near the plate"):
        robot.reach("to plate")
    if check("the robot's gripper is near the plate and the plate is not aligned with the target location"):
        robot.slide("the plate back to target location")