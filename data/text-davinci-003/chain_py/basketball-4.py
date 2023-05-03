
    # Steps:
    #  1. Put gripper above the ball
    #  2. Grab the ball with the gripper
    #  3. Line up the ball with the hoop
    #  4. Throw the ball into the hoop
    # First, put the gripper above the ball.
    if check("the robot's gripper is not above ball"):
        robot.put("gripper above ball")
    # If the gripper is near the ball and it's open, close the gripper
    # to grab it.
    if check("the robot's gripper is near ball and the robot's gripper is open"):
        robot.close("gripper around ball")
    # If the gripper is closed around the ball and the ball isn't yet lined up
    # with the hoop, line up the ball with the hoop.
    if check("the robot's gripper is closed around ball and the ball is not aligned with the hoop"):
        robot.align("ball with hoop")
    # If the ball is lined up with the hoop, throw it into the hoop.
    if check("the ball is aligned with the hoop"):
        robot.throw("ball in hoop")