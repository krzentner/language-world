
    if check("the robot's gripper is not forward aligned with button"):
        robot.put("gripper in front of button")
    if check("the robot's gripper is not very close to button and the robot's gripper is forward aligned with button"):
        robot.push("gripper closer to button")
    if check("the robot's gripper is very close to button"):
        robot.push("down on button")