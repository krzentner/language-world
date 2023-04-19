# Steps:
    #  1. Place the gripper above the ball
    #  2. Close the gripper around the ball
    #  3. Align the gripper and ball with the hoop
    #  4. Toss the ball up towards the hoop
    # First, put the gripper above the ball.
    if check("the robot's gripper is not above the ball"):
        robot.place("gripper above ball")
    # If the gripper isn't around the ball, grab it by closing the gripper.
    if check("the robot's gripper is not around ball and the robot's gripper is open"):
        robot.close("gripper around ball")
    # If the gripper is around the ball, align the gripper and ball with the
    # hoop.
    if check("the robot's gripper is around ball and the ball is below the hoop"):
        robot.align("gripper and ball with hoop")
    # Toss the ball up towards the hoop.
    if check("the gripper and ball are aligned with the hoop"):
        robot.toss("ball towards hoop")