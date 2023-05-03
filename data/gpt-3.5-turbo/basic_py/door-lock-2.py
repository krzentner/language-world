if check("the robot's gripper is not near the door lock and the dial is not aligned to zero"):
        robot.move("gripper to door lock")
    if check("the robot's gripper is near the door lock and the dial is not aligned to zero"):
        robot.turn("dial to zero")
    if check("the dial is aligned to zero"):
        robot.turn("dial clockwise to unlock the door")