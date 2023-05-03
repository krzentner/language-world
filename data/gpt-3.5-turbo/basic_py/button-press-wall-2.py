    if check("the robot's gripper is not near the button and the wall is between the robot and the button"):
        robot.move("gripper to left of button")
        robot.move("gripper up and over wall")
        robot.move("gripper towards button")
    if check("the robot's gripper is near the button"):
        robot.push("button forward")