# Steps:
#  1. Put gripper around the dial
#  2. Rotate the dial to the desired position
# First, put the gripper around the dial.
if check("the robot's gripper is not around the dial"):
    robot.drop("gripper around dial")
# Turn the dial to the desired position.
if check("the gripper is around the dial"):
    robot.rotate("dial to desired position")