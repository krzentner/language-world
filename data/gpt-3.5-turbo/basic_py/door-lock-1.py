if check("the robot's gripper is not near the door lock"):
        robot.move("to door lock")
    if check("the dial is not aligned with the correct combination"):
        robot.turn("dial to correct combination")
    if check("the dial is aligned with the correct combination"):
        robot.turn("the lock handle to lock the door")