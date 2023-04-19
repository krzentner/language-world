# basketball: put the ball into the hoop
# def basketball(robot):
    # Steps:
    #  1. Put gripper above ball
    #  2. Grab ball with gripper
    #  3. Line up gripper with hoop
    #  4. Toss ball into the hoop
    # First, put the gripper above the ball.
    if check("the robot's gripper is not above the ball"):
        robot.move_gripper("above the ball")
    # If the gripper isn't grabbing the ball, put it around the ball.
    if check("the robot's gripper is not around the ball and the robot's gripper is open"):
        robot.move_gripper("near the ball", close_gripper=True)
    # If the gripper is grabbing the ball, we need to line it up with the hoop.
    if check("the robot's gripper is around the ball"):
        robot.move_gripper("aligned with the hoop")
    # Finally, toss the ball into the hoop.
    if check("the robot's gripper is aligned with the hoop"):
        robot.move_gripper("above the hoop", close_gripper=False)