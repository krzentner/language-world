
    if check("the robot's gripper is not forward aligned with the handle"):
        robot.put("gripper in front of the handle")
    if check("gripper is forward aligned, but not around the handle"):
        robot.grab("handle")
    if check("gripper around the handle"):
        robot.pull("handle up")