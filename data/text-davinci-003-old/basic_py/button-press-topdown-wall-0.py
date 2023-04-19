
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not forward aligned with the button"):
        robot.put("gripper in front of button")
    if check("the robot's gripper is forward aligned with the button"):
        robot.push("down on button")