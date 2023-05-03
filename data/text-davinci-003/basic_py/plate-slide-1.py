
    if check("the robot's gripper is not near the plate and the robot's gripper is not forward aligned"):
        robot.align("the robot's gripper with the plate")
    if check("the robot's gripper is forward aligned with the plate and the plate is not aligned with the target"):
        robot.slide("the plate towards the target")
    if check("the plate is aligned with the target"):
        robot.push("the plate into the target")