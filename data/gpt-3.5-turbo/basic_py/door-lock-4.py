if check("the robot's gripper is not near the door dial"):
        robot.reach("door dial")
    if check("the robot's gripper is near the door dial"):
        robot.grab("door dial")
    if check("the robot's gripper is holding the door dial and the dial is not in the locked position"):
        robot.turn_left("door dial")
        robot.turn_left("door dial")
        robot.turn_left("door dial")
    if check("the dial is in the locked position"):
        robot.release("door dial")