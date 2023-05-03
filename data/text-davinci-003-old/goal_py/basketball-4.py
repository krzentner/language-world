
    # Steps:
    #  1. Put gripper vertically above the ball
    #  2. Drop gripper around ball
    #  3. Line up ball with hoop
    #  4. Shoot ball into hoop
    # First, put the gripper above the ball.
    if check("the robot's gripper is not vertically aligned with the ball"):
        robot.move_gripper("vertically aligned with the ball")
    # If the gripper is vertically aligned, but the gripper is not around the
    # ball, the gripper should move down around the ball.
    if check("the robot's gripper is vertically aligned with the ball and the robot's gripper is open"):
        robot.move_gripper("around the ball", close_gripper=True)
    # Once the gripper is around the ball, line it up with the hoop.
    if check("the robot's gripper is around the ball and the ball is not horizontally aligned with the hoop"):
        robot.move_gripper("horizontally aligned with the hoop")
    # If the ball is almost lined up, shoot it into the hoop.
    if check("the ball is aligned with the hoop"):
        robot.move_gripper("directly above the hoop")