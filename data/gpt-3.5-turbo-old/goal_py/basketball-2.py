# Steps:
#  1. Put gripper above ball
#  2. Grab the ball with the gripper
#  3. Move the ball over to the hoop
#  4. Release the ball into the hoop
# First, put the gripper above the ball.
if check("the robot's gripper is not vertically aligned with the ball"):
    robot.move_gripper("vertically aligned with the ball")
# If the gripper is above the ball, grab the ball.
if check("the robot's gripper is above the ball and the gripper is open"):
    robot.move_gripper("around the ball", close_gripper=True)
# If the gripper is grabbing the ball, move the ball over to the hoop.
if check("the robot's gripper is around the ball"):
    robot.move_gripper("above the hoop")
# If the ball is above the hoop and the gripper is grabbing it, release it into
# the hoop.
if check("the robot's gripper is above the hoop and the gripper is closed"):
    robot.move_gripper("around the ball", close_gripper=False)