
    # Steps:
    #  1. Put gripper above ball
    #  2. Grab ball with gripper
    #  3. Line up the ball with the hoop
    #  4. Dunk the ball into the hoop
    # We need to put the gripper above the ball before we can grab it
    if check("the robot's gripper is not above the ball"):
        robot.move_gripper("above the ball")
    # If the ball isn't near the gripper, move the gripper near it.
    if check("the robot's gripper is not near the ball"):
        robot.move_gripper("near the ball", close_gripper=True)
    # If the ball is near the gripper and the gripper is open, close the gripper
    # to grab the ball.
    if check("the robot's gripper is above the ball and the gripper is closed"):
        robot.move_gripper("vertically aligned with the hoop")
    # Once the ball is lined up with the hoop, dunk the ball.
    if check("the ball is lined up with the hoop"):
        robot.move_gripper("above the hoop")