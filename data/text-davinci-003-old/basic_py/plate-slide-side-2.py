
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above the plate")
    if check("the robot's gripper is above the plate and the plate is not aligned with the target location"):
        robot.slide("plate sideways to the target location")
    if check("the plate is aligned with the target location"):
        robot.slide("plate into the target location")