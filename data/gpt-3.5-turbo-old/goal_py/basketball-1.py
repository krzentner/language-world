# Steps:
#  1. Put gripper above the ball
#  2. Grab the ball with the gripper
#  3. Line up the ball with the hoop
#  4. Push the ball into the hoop
# First, put the gripper above the ball.
if check("the robot's gripper is not above the ball"):
    robot.move_gripper("above the ball")
# If the ball is not trapped inside the gripper, grab the ball.
if check("the robot's gripper is not around the ball"):
    robot.move_gripper("near the ball", close_gripper=True)
# If the ball is not vertically aligned with the hoop, align it.
if check("the ball is not vertically aligned with the hoop"):
    robot.move_gripper("above the ball", close_gripper=True)
# If the ball is aligned with the hoop, push it into the hoop.
if check("the ball is vertically aligned with the hoop"):
    robot.move_gripper("behind the hoop")