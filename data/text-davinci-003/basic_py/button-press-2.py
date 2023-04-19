
    if check("the robot's gripper is not forward aligned with the button"):
        robot.move("gripper to front of button")
    if check("the robot's gripper is forward aligned with the button and the robot's gripper is open"):
        robot.close("gripper around the button")
    if check("the robot's gripper is near the button"):
        robot.push("down on the button")