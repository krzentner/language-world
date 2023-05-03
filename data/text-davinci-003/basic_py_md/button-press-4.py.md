

If check("the robot's gripper is not near the button"):
    robot.move("gripper to button")

If check("the robot's gripper is near the button"):
    robot.push("button")