if check("the robot's gripper is not near the puck"):
        robot.pickup("the puck")
    if check("the robot's gripper is holding the puck"):
        robot.move("the puck to the goal location")
    if check("the robot's gripper is at the goal location"):
        robot.release("the puck")