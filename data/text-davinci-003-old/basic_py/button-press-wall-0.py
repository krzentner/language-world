
    if check("the robot's gripper is not vertically aligned with the button and the robot's gripper is right of the button"):
        robot.move("gripper to left of button")
    if check("the robot's gripper is not near the button and the robot's gripper is left of the button"):
        robot.move("gripper to in front of button")
    if check("the robot's gripper is in front of the button"):
        robot.push("button")