# Steps:
#  1. Put gripper around the dial
#  2. Turn the dial
# We need to put the gripper around the dial before we can turn it.
if check("the robot's gripper is not around the dial"):
    robot.grab("the dial")
# If the gripper is around the dial, we can turn it.
if check("the robot's gripper is around the dial"):
    robot.turn("the dial")