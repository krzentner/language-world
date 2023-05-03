if check("the robot's gripper is not near the door and the door is already closed"):
        robot.move("to the door")
    if check("the robot's gripper is near the door and the door is already closed"):
        robot.push("door closed")