# Steps:
    #  1. Put gripper around the door dial
    #  2. Turn the dial to the right
    #  3. Turn the dial to the left
    #  4. Turn the dial to the right again
    # Put the gripper around the door dial.
    if check("the robot's gripper is not around the door dial"):
        robot.grab("door dial")
    # Turn the dial to the right.
    if check("the dial is not turned to the right"):
        robot.turn("dial to the right")
    # Turn the dial to the left.
    if check("the dial is not turned to the left"):
        robot.turn("dial to the left")
    # Turn the dial to the right again.
    if check("the dial is not turned to the right again"):
        robot.turn("dial to the right again")