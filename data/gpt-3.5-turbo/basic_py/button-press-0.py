if check("the robot's gripper is not in front of the button"):
        robot.move("gripper in front of button")
    if check("the robot's gripper is in front of the button"):
        robot.push("button")