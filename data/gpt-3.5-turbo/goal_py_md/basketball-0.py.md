# basketball: put the ball into into the hoop
def basketball(robot):
    # Steps:
    #  1. Put gripper above the ball
    #  2. Grab the ball with the gripper
    #  3. Move the ball towards the hoop
    #  4. Align the ball with the hoop
    #  5. Release the ball into the hoop
    # First, put the gripper above the ball.
    if check("the robot's gripper is not above the ball"):
        robot.move_gripper("above the ball")
    # If the gripper is above the ball, grab the ball.
    if check("the robot's gripper is above the ball and the robot's gripper is open"):
        robot.move_gripper("near the ball", close_gripper=True)
    # If the ball is in the gripper, move it towards the hoop.
    if check("the robot's gripper is holding onto the ball"):
        robot.move_gripper("above the hoop")
    # If the ball is close to the hoop, align it with the hoop.
    if check("the robot's gripper is above the hoop and the ball is in front of the hoop"):
        robot.move_gripper("horizontally aligned with the hoop")
    # If the ball is aligned with the hoop, release it.
    if check("the robot's gripper is aligned with the hoop and the ball is almost inside the hoop"):
        robot.move_gripper("inside the hoop", open_gripper=True)