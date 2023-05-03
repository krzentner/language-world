
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is above the handle and the robot's gripper is not forward aligned with handle"):
        robot.push("handle forward")
    if check("the robot's gripper is forward aligned with handle"):
        robot.pull("handle up")