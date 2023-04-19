
    if check("the robot's gripper is not near the door lock"):
        robot.move("gripper to near door lock")
    if check("the robot's gripper is near the door lock"):
        robot.turn("dial")