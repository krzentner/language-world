# Steps:
#   1. Put gripper above ball
#   2. Grab the ball with the gripper
#   3. Align the ball with the hoop
#   4. Toss the ball into the hoop
# First, put the gripper above the ball
if check("the robot's gripper is not vertically aligned with the ball"):
    robot.put("gripper above ball")
# If the gripper is not around the ball, grab it
if check("the robot's gripper is not around ball"):
    robot.grab("ball")
# If the ball is not aligned with the hoop, align it
if check("ball is not aligned with the hoop"):
    robot.align("ball with hoop")
# Once the ball is aligned with the hoop, toss it in
if check("the ball is aligned with the hoop"):
    robot.toss("ball into hoop")