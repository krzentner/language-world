
    # Steps:
    #  1. Put gripper above ball
    #  2. Drop gripper around ball
    #  3. Close gripper around ball
    #  4. Move ball towards hoop
    #  5. Release ball into hoop
    # First, put the gripper above the ball.
    if check("the robot's gripper is not vertically aligned with the ball"):
        robot.move_gripper("vertically aligned with the ball")
    # If the gripper isn't around the ball, put it around the ball.
    if check("the robot's gripper is not around ball and the robot's gripper is open"):
        robot.move_gripper("near the ball", close_gripper=True)
    # If the gripper is near the ball and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is vertically aligned with ball and the robot's gripper is closed"):
        robot.move_gripper("towards the hoop")
    # If the gripper is moving the ball towards the hoop, but isn't near it,
    # move the gripper closer.
    if check("the robot's gripper is not near the hoop and the ball is below the robot's gripper"):
        robot.move_gripper("near the hoop")
    # If the gripper is near the hoop, we can release the ball and it should
    # fall in.
    if check("the robot's gripper is near the hoop"):
        robot.move_gripper("above the hoop", open_gripper=True)