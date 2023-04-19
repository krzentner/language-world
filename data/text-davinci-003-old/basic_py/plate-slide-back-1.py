
    if check("the robot's gripper is not above the plate"):
        robot.move("gripper above plate")
    if check("the robot's gripper is above the plate and the plate is not aligned with the target location"):
        robot.align("plate with target location")
    if check("the plate is aligned with the target location"):
        robot.slide("plate into target location")