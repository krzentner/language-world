
    # Steps:
    #  1. Put gripper above and slightly left of the ball
    #  2. Drop the gripper around the ball
    #  3. Close the gripper around the ball
    #  4. Put the ball into the hoop
    # First, put the gripper slightly left of the ball. We want to avoid getting
    # directly above the ball and pushing it away instead of trapping it.
    if check("the robot's gripper is not slightly left of ball"):
        robot.move_gripper("slightly left of ball")
    # If the gripper is above and slightly left of the ball, drop the gripper
    # around the ball.
    if check("the gripper is slightly left of the ball and the gripper is not near the ball"):
        robot.move_gripper("near the ball", close_gripper=True)
    # Now that the gripper is trapping the ball, we can lift it up and put it
    # into the hoop.
    if check("the robot's gripper is near the ball and the robot's gripper is closed"):
        robot.move_gripper("at the hoop")