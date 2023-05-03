
    if check("the robot's gripper is not left of handle and the robot's gripper is not forward aligned with handle"):
        robot.move("gripper to side of handle")
    if check("the robot's gripper is left of handle and the robot's gripper is not forward aligned with handle"):
        robot.put("gripper under handle")
    if check("the robot's gripper is forward aligned with handle"):
        robot.push("down handle")