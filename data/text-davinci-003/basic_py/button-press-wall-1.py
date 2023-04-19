
    if check("the robot's gripper is not horizontally aligned with the button and the wall"):
        robot.position("gripper to the side of the wall")
    if check("the robot's gripper is in front of the button"):
        robot.push("short wall away")
    if check("the robot's gripper is close to the button"):
        robot.push("button")