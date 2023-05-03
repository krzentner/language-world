
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.align("gripper with plate")
    if check("the robot's gripper is vertically aligned with the plate and the plate is not near the target location"):
        robot.slide("plate towards the target")
    if check("the plate is near the target location and the plate is not horizontally aligned with the target location"):
        robot.align("plate with target")
    if check("the plate is horizontally aligned with the target location"):
        robot.push("plate into target")