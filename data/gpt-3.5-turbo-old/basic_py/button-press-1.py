    if check("the robot's gripper is not in front of the button"):
        robot.move("gripper in front of button")
    if check("the robot's gripper is in front of the button and the robot's gripper is not touching the button"):
        robot.touch("button")
    if check("the robot's gripper is touching the button"):
        robot.push("button")