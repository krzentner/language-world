# Steps:
    #  1. Put gripper above the ball
    #  2. Grab the ball with the gripper
    #  3. Pull the gripper back to the starting point
    #  4. Put gripper above the hoop
    #  5. Release the ball
    # First, put the gripper above the ball.
    if check("the robot's gripper is not above the ball"):
        robot.put("gripper above ball")
    # If the gripper isn't around the ball, put it around the ball.
    if check("the robot's gripper is not around ball and the robot's gripper is open"):
        robot.drop("gripper around ball")
    # If the gripper is near the ball and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near ball and the robot's gripper is open"):
        robot.close("gripper around ball")
    # We closed the gripper, so we need to move the ball back to starting point.
    if check("the robot's gripper is above the ball and the robot's gripper is closed"):
        robot.pull("ball to starting point")
    # After we moved the ball to starting point, we position the gripper above the hoop.
    if check("the ball is at starting point and the robot's gripper is above the hoop"):
        robot.put("gripper above hoop")
    # When gripper is above the hoop, we release the ball into the hoop.
    if check("the robot's gripper is above the hoop and the robot's gripper is closed"):
        robot.release("ball into the hoop")