
    if check("the robot's gripper is not above plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is above plate and the plate is not left of the target"):
        robot.slide("plate to left")
    if check("the plate is left of the target"):
        robot.slide("plate to target location")