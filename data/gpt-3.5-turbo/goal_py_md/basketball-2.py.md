# basketball: put the ball into into the hoop
def basketball(robot):
    # Steps:
    #  1. Put gripper above the ball
    #  2. Grab the ball with the gripper
    #  3. Move the gripper to the hoop
    #  4. Release the ball into the hoop
    # First, put the gripper above the ball.
    if check("the robot's gripper is not vertically aligned with the ball"):
        robot.move_gripper("vertically aligned with the ball")
    # If the ball is not yet in the gripper and the gripper is above the ball,
    # grab the ball with the gripper.
    if check("the robot's gripper is above the ball and the robot's gripper is open"):
        robot.move_gripper("around the ball", close_gripper=True)
    # Move the gripper to the hoop position above the hoop.
    if check("the robot's gripper is not above the hoop"):
        robot.move_gripper("above the hoop")
    # If the gripper is above the hoop, release the ball into the hoop.
    if check("the robot's gripper is above the hoop and the robot's gripper is closed"):
        robot.move_gripper("released above the hoop")