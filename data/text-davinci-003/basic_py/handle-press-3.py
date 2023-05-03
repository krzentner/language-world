
    if check("the robot's gripper is not above handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is above handle and the robot's gripper is open"):
        robot.put("gripper around handle")
    if check("the robot's gripper is forward aligned with handle"):
        robot.push("down on handle")