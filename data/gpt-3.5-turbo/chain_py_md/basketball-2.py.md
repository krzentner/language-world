# basketball: put the ball into into the hoop
def basketball(robot):
    # Steps:
    #  1. Put gripper above ball
    #  2. Grab the ball with the gripper
    #  3. Line up the hoop with the ball
    #  4. Launch the ball into the hoop
    # First, put the gripper above the ball.
    if check("the robot's gripper is not above the ball"):
        robot.place("gripper above ball")
    # If the gripper is above the ball, we can try to grab the ball.
    if check("the robot's gripper is above the ball"):
        robot.grab("ball")
    # If we have the ball, move it towards and line it up with the hoop.
    if check("the robot's gripper is holding the ball"):
        robot.move("ball towards hoop")
        if check("the ball is near the hoop"):
            robot.align("ball with hoop")
    # If the ball is lined up with the hoop, try to launch it in.
    if check("the ball is aligned with hoop"):
        robot.launch("ball into hoop")