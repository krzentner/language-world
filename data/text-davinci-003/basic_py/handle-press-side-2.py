
    if check("the robot's gripper is not right aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is not forward aligned with the handle and the robot's gripper is open"):
        robot.grab("handle")
    if check("the robot's gripper is forward aligned with the handle and the robot's gripper is open"):
        robot.push("gripper down on handle")