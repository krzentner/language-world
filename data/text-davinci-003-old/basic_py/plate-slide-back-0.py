
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above the plate")
    if check("the robot's gripper is above the plate and the plate is not aligned with target"):
        robot.align("plate to target")
    if check("the plate is aligned with target and the plate is not near target"):
        robot.slide("plate to target")