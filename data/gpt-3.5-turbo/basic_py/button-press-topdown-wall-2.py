if check("the robot's gripper is not above the wall and the robot's gripper is not close to the wall"):
        robot.move("gripper to above the wall")
    if check("the robot's gripper is above the wall"):
        robot.slide("gripper to the button")
    if check("the robot's gripper is above the button"):
        robot.push("down on button")