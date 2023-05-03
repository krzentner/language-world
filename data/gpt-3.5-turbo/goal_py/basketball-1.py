# Steps:
    #  1. Put the gripper above the ball
    #  2. Grab the ball with the gripper
    #  3. Move the ball towards the hoop
    if check("the robot's gripper is not above the ball"):
        robot.move_gripper("above the ball")
    # If the gripper is above the ball, close it to grab the ball.
    if check("the robot's gripper is above the ball and open"):
        robot.move_gripper("around the ball")
    # If the gripper has the ball, move it towards the hoop.
    if check("the ball is in the robot's gripper and the robot's gripper is above the hoop"):
        robot.move_gripper("above the hoop")