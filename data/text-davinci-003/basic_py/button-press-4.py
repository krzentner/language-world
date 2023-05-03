
    if check("the robot's gripper is not forward of button"):
        robot.put("gripper in front of button")
    if check("the robot's gripper is in forward of button"):
        robot.push("button")