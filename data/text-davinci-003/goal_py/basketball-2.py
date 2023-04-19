
    # Steps:
    #  1. Put gripper above the ball
    #  2. Start pushing against the ball
    #  3. Push the ball into the hoop
    # Put the gripper above the ball so that we can start pushing against it.
    if check("the robot's gripper is not above the ball"):
        robot.move_gripper("above the ball")
    # If the ball isn't aligned with the hoop in the direction of the pushing,
    # we should rotate the ball in that direction until it is aligned.
    if check("the ball is not horizontally aligned with the hoop"):
        robot.move_gripper("below the ball")
    # If the ball is aligned with the hoop, we should push the ball into the hoop.
    if check("the ball is horizontally aligned with the hoop"):
        robot.move_gripper("above the hoop")