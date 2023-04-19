if check("the robot's gripper is not near the puck"):
        robot.grab("the puck")
    if check("the puck is not at the target location"):
        robot.move("the puck to the target location")
    if check("the puck is at the target location"):
        robot.release("the puck")