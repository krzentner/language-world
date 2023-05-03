
    if check("the robot's gripper is not near the wall"):
        robot.put("gripper near wall")
    if check("the robot's gripper is near the wall but not near the button"):
        robot.put("gripper near button")
    if check("the robot's gripper is close to the button and the button is forward of the Robot's gripper"):
        robot.push("button with wall")