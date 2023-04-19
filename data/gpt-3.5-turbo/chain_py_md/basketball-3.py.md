# basketball: put the ball into the hoop
# def basketball(robot):
    # Steps:
    # 1. Put the gripper above the ball
    # 2. Grab the ball with the gripper
    # 3. Line up the ball with the hoop
    # 4. Toss the ball into the hoop
    # First, put the gripper roughly above the ball.
    if check("the robot's gripper is not above the ball"):
        robot.place("above ball")
    # Open the gripper and drop it around the ball.
    if check("the robot's gripper is above the ball and the gripper is closed"):
        robot.open("gripper around ball")
    # If the gripper is located around the ball, close it to grab the ball.
    if check("the robot's gripper is around ball"):
        robot.close("gripper around ball")
    # Once we grabbed the ball, line it up with the hoop by moving the gripper
    # sideways.
    if check("the robot's gripper is holding the ball and the ball is not horizontally aligned with the hoop"):
        robot.align("ball to hoop")
    # Toss the ball into the hoop by flicking the gripper upwards.
    if check("the ball is horizontally aligned with the hoop"):
        robot.flick("ball into hoop")