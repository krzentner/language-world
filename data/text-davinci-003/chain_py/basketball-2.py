
    # Steps:
    #  1. Put gripper above the ball
    #  2. Grab the ball with the gripper
    #  3. Line up the ball with the hoop
    #  4. Throw the ball at the hoop
    # First, put the gripper above the ball.
    if check("the robot's gripper is not above the ball"):
        robot.put("gripper above ball")
    # If the ball is still below the robot's gripper, grab it.
    if check("the robot's gripper is not near the ball and robot gripper is open"):
        robot.grab("ball")
    # If the ball is close to the gripper, then it should be safe to align the
    # ball with the hoop.
    if check("the robot's gripper is above the ball and the ball is not aligned with the hoop"):
        robot.align("ball to hoop")
    # Once the ball is aligned with the hoop, throw it in.
    if check("the ball is aligned with the hoop"):
        robot.throw("ball into hoop")