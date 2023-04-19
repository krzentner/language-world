

If check("the robot's gripper is not vertically aligned with button"):
    robot.put("gripper in front of button")
if check("the robot's gripper is vertically aligned with button"):
    robot.push("button down")