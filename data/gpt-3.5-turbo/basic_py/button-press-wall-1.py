if check("the robot's gripper is not near the button and there is a wall in the way"):
        robot.move("gripper to the side of the button")
    if check("the robot's gripper is near the button"):
        robot.push("button forward")