
    # Steps:
    #  1. Put gripper above the ball
    #  2. Drop gripper around the ball
    #  3. Move the ball towards the hoop
    #  4. Drop the ball into the hoop
    # First, put the gripper above the ball.
    if check("the robot's gripper is not above the ball"):
        robot.move_gripper("above the ball")
    # If the gripper isn't around the ball, put it around the ball.
    if check("the robot's gripper is not around the ball and the robot's gripper is open"):
        robot.move_gripper("near the ball", close_gripper=True)
    # If the gripper is near the ball, move it towards the hoop.
    if check("the robot's gripper is around the ball and the ball is not above the hoop"):
        robot.move_gripper("above the hoop")
    # If the ball is above the hoop, open the gripper to drop the ball into the
    # hoop.
    if check("the ball is above the hoop"):
        robot.move_gripper("open the gripper")