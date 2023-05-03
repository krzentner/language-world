
    # Steps:
    #  1. Move gripper to top of the ball
    #  2. Push the ball to the target location
    # First move the robot's gripper to the top of the ball.
    if check("the robot's gripper is not above the ball"):
        robot.move_gripper("above the ball")
    # If the ball is still behind the robot, move it to the front of the robot.
    # Again, because this is a ball, check if it's in front of the robot's
    # gripper instead of around it.
    if check("the ball is not left of the robot's gripper and the ball is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the ball")
    # When the gripper is in front of the ball, we can start pushing it to the
    # target location.
    # If the gripper is forward aligned with the ball and not near the target
    # location, move the gripper near the target location.
    if check("the robot's gripper is forward aligned with the ball and the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")