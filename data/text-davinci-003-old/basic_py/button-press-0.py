
    if check("the robot's gripper is not forward aligned with the button"):
        robot.put("gripper in front of button")
    if check("the robot's gripper is forward aligned with the button"):
        robot.push("button")