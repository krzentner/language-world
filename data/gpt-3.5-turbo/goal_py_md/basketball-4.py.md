# basketball: put the ball into the hoop
def basketball(robot):
    # Steps:
    #  1. Put gripper above ball
    #  2. Grab the ball with the gripper
    #  3. Line the ball up with the hoop
    #  4. Toss the ball into the hoop
    # First, put the gripper above the ball.
    if check("the robot's gripper is not above the ball"):
        robot.move_gripper("above the ball")
    # If the ball is not trapped in the gripper, grab it.
    if check("the robot's gripper is above the ball and the robot's gripper is open"):
        robot.move_gripper("around the ball", close_gripper=True)
    # If the ball is trapped, move the gripper towards the hoop.
    if check("the robot's gripper is around the ball"):
        robot.move_gripper("near the hoop")
    # Toss the ball into the hoop by releasing the gripper.
    if check("the robot's gripper is near the hoop"):
        robot.move_gripper("around the ball", close_gripper=False)