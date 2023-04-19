
    if check("the robot's gripper is not to the front of the button and the robot's gripper is not vertically aligned with the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is forward aligned with the button and the robot's gripper is not near the button"):
        robot.put("gripper in front of button")
    if check("the robot's gripper is near the button"):
        robot.push("down on button")