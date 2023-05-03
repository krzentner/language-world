

If check("the robot's gripper is not horizontally aligned with the button"):
    robot.put("gripper in front of button")
if check("the robot's gripper is horizontally aligned with the button"):
    robot.push("button")