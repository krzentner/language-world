
    if check("the robot's gripper is not near and forward aligned with the button"):
        robot.put("gripper near and forward aligned with button")
    if check("the robot's gripper is not on a short wall and forward aligned with the button"):
        robot.put("gripper on short wall in front of button")
    if check("the robot's gripper is on a short wall and forward aligned with the button"):
        robot.push("down on button")