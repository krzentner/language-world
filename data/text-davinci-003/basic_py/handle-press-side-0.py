
    if check("the robot's gripper is not against handle"):
        robot.put("gripper against handle")
    if check("the robot's gripper is against the handle"):
        robot.press("handle down")