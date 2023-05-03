# Steps:
    #  1. Put gripper above the ball
    #  2. Grab the ball with the gripper
    #  3. Line up the ball with the hoop
    #  4. Toss the ball into the hoop
    # First, put the gripper above the ball.
    if check("the robot's gripper is not vertically aligned with the ball"):
        robot.put("gripper above ball")
    # If the ball becomes too far from the gripper or the gripper isn't around
    # the ball, go back to putting the gripper above the ball.
    if check("the ball is not below the robot's gripper and the robot's gripper is not around the ball"):
        robot.grab("ball")
    # As long the gripper is still mostly around the ball and the ball isn't
    # lined up with the hoop, line up the ball with the hoop.
    if check("the robot's gripper is around ball and the ball is not lined up with the hoop"):
        robot.align("ball to hoop")
    # If the ball is lined up with the hoop, toss it into the hoop.
    if check("the ball is lined up with the hoop"):
        robot.toss("ball into hoop")