
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above the plate")
    if check("the robot's gripper is not forward aligned with the plate"):
        robot.grab("the plate")
    if check("the robot's gripper is forward aligned with the plate and the plate is not in the correct position"):
        robot.slide("the plate to the target location")
    if check("the plate is in the correct position"):
        robot.push("plate into the target location")