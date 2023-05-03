    if check("the robot's gripper is not in front of the button"):
        robot.move("gripper to be in front of button")
    if check("the robot's gripper is in front of the button and the robot's gripper is not around the button"):
        robot.grab("button")
    if check("the robot's gripper is around the button"):
        robot.push("button")