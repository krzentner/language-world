
    # Steps:
    #  1. Put gripper above ball
    #  2. Grab ball with gripper
    #  3. Move the ball to the hoop
    #  4. Line up the ball with the hoop
    #  5. Throw the ball into the hoop
    # First, put the gripper roughly above the ball.
    if check("the robot's gripper is not above the ball"):
        robot.put("gripper above ball")
    # The robot needs to grab the ball to move it, so move the gripper to the
    # ball and close the gripper.
    if check("the robot's gripper is near the ball and the robot's gripper is open"):
        robot.close("gripper around ball")
    # Now that the gripper has the ball, move the ball to the hoop.
    if check("the ball is in the robot's gripper"):
        robot.move("gripper to goal")
    # We need to line up the ball with the hoop, so move the gripper to the side.
    if check("the ball is near the hoop and the ball is not aligned with the hoop"):
        robot.align("ball to goal")
    # Now that the gripper is lined up with the hoop, try to throw the ball into
    # the hoop.
    if check("the ball is aligned with the hoop"):
        robot.throw("ball into goal")