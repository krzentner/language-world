
    # Steps:
    #  1. Put the gripper above the ball
    #  2. Grab the ball with the gripper
    #  3. Move the ball to the backboard
    #  4. Position the ball in front of the backboard
    #  5. Shoot the ball to put it in the hoop
    # First, put the gripper above the ball.
    if check("the robot's gripper is not above the ball"):
        robot.move_gripper("above the ball", close_gripper=True)
    # If the gripper is above the ball, but not lined up with it, move the
    # gripper around to the ball.
    if check("the robot's gripper is above the ball and the robot's gripper is not around the ball"):
        robot.move_gripper("near the ball")
    # If the robot's gripper is near the ball, move the ball near the backboard.
    if check("the robot's gripper is near the ball and ball is not near the backboard"):
        robot.move_gripper("near the backboard")
    # If the ball is near the backboard, put the ball in front of the backboard
    # where the hoop is.
    if check("the ball is near the backboard and the ball is not in front of the backboard"):
        robot.move_gripper("in front of the backboard")
    # If the ball is in front of the backboard, shoot the ball at the hoop.
    if check("the ball is in front of the backboard"):
        robot.move_gripper("fully aligned with the hoop and fire")