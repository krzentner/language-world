
    if check("the robot's gripper is below button"):
        robot.put("gripper above button")
    if check("the robot's gripper is not forward aligned with button"):
        robot.put("gripper directly in front of button")
    if check("the robot's gripper is forward aligned with the button"):
        robot.push("button")