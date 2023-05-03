
    # Steps:
    #  1. Move the gripper in front of the ball
    #  2. Put the gripper above the ball
    #  3. Pick up the ball with the gripper
    #  4. Push the ball towards the hoop
    # First, put the gripper in front of the ball.
    if check("the robot's gripper is not in front of ball and the robot's gripper is not close to the ball"):
        robot.move_gripper("close to the ball")
    # If the gripper is in front of the ball, lower it so it's mostly above it.
    if check("the robot's gripper is in front of the ball and the robot's gripper is not near the ball"):
        robot.move_gripper("near the ball", close_gripper=True)
    # If the gripper is near the ball, grab it and push it in the direction of
    # the hoop.
    if check("the robot's gripper is near the ball and the ball is below the robot's gripper"):
        robot.move_gripper("towards the hoop")