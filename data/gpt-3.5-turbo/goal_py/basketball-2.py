# Steps:
    #  1. Put gripper above ball
    #  2. Drop gripper around ball
    #  3. Close gripper around ball
    #  4. Move ball toward hoop
    #  5. Lift ball into hoop
    # First, put the gripper above the ball.
    if check("the robot's gripper is not above the ball"):
        robot.move_gripper("above the ball")
    # If the gripper isn't around the ball, put it around the ball.
    if check("the robot's gripper is not around ball and the robot's gripper is open"):
        robot.move_gripper("near the ball", close_gripper=True)
    # If the gripper is near the ball and closed, we can move the ball toward
    # the hoop.
    if check("the robot's gripper is around ball and the ball is not in the hoop"):
        robot.move_gripper("near the hoop")
    # If the ball is in the hoop, lift it up by moving the gripper higher.
    if check("the ball is in the hoop"):
        robot.move_gripper("above the hoop")