if check("the robot's gripper is not near the plate"):
        robot.put("gripper near plate")
    if check("the robot's gripper is not around the plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
    if check("the robot's gripper is around the plate and the plate is not aligned with the target location"):
        robot.slide("plate sideways to target location")
    if check("the plate is aligned with the target location"):
        robot.push("plate back towards the target location")