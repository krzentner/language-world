if check("the robot's gripper is not near the handle"):
        robot.grab("handle")
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is forward aligned with handle"):
        robot.pull("handle up")