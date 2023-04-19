# basketball: put the ball into the hoop
# def basketball(robot):
    # Steps:
    #  1. Put gripper above ball
    #  2. Grab the ball
    #  3. Bring gripper to the hoop
    #  4. Release the ball
    # First, put the gripper roughly above the ball, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the ball"):
        robot.move_gripper("above the ball")
    # If the gripper isn't around the ball, put it around the ball.
    if check("the robot's gripper is not around ball and the robot's gripper is open"):
        robot.move_gripper("near the ball", close_gripper=True)
    # If the gripper is around the ball, we can bring it over to the hoop
    if check("the robot's gripper is around the ball and the robot's gripper is not near the hoop"):
        robot.move_gripper("above the hoop")
    # Once we're above the hoop, we can release the ball
    if check("the robot's gripper is near the hoop"):
        robot.move_gripper("above the hoop", close_gripper=False)