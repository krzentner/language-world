

if check("the robot's gripper is not forward aligned with button"):
    robot.put("gripper in front of button")
if check("the robot's gripper is forward aligned with button"):
    robot.push("button")