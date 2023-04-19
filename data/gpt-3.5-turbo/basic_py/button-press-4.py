if check("the robot's gripper is not horizontally aligned with the button"):
        robot.move("gripper to the side of button")
    if check("the robot's gripper is horizontally aligned with button and the robot's gripper is not in front of button"):
        robot.move("gripper in front of button")
    if check("the robot's gripper is in front of button"):
        robot.push("button down")