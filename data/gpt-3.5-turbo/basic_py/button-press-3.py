if check("the robot's gripper is not near the button and the robot's gripper is not vertically aligned with button"):
        robot.move("gripper to button")
    if check("the robot's gripper is near the button"):
        robot.push("button")
    if check("the button is not pressed"):
        robot.push("button harder")