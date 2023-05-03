
    if check("the robot's gripper is not near the plate"):
        robot.reach("to plate")
    if check("the robot's gripper is near the plate and the robot's gripper is not below plate"):
        robot.drop("gripper below plate")
    if check("the robot's gripper is below the plate"):
        robot.push("plate back")