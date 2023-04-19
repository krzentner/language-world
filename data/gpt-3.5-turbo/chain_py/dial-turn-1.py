# Steps:
#  1. Put gripper around the dial
#  2. Turn the dial
# First, put the gripper around the dial.
if check("the robot's gripper is not around the dial"):
    robot.drop("gripper around the dial")
# If the gripper is around the dial, turn the dial.
if check("the robot's gripper is around the dial"):
    robot.turn("the dial")