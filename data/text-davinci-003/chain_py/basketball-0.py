
    # Steps:
    #  1. Put gripper above ball
    #  2. Drop gripper around ball
    #  3. Close gripper around ball
    #  4. Aim towards the hoop
    #  5. Throw the ball
    # First, put the gripper above the ball.
    if check("the robot's gripper is not above the ball"):
        robot.put("gripper above ball")
    # If the gripper isn't around the ball, put it around the ball by dropping
    # the gripper.
    if check("the robot's gripper is not around ball and the robot's gripper is open"):
        robot.drop("gripper around ball")
    # Now that the gripper is around the ball, close it.
    if check("the robot's gripper is near ball and the robot's gripper is open"):
        robot.close("gripper around ball")
    # Now that the ball is firmly in the gripper's grasp, we can aim towards the
    # hoop.
    if check("the robot's gripper is forward aligned with ball"):
        robot.align("gripper towards hoop")
    # Now that the gripper is aligned with the hoop, throw the ball.
    if check("the robot's gripper is aligned with hoop"):
        robot.throw("ball at hoop")