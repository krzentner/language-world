# Steps:
#  1. Put gripper above the dial
#  2. Grab the dial with the gripper
#  3. Turn the dial to the right until it clicks
# First, put the gripper above the dial.
if check("the robot's gripper is not vertically aligned with the dial"):
    robot.move_gripper("vertically aligned with the dial")
# If the gripper is above the dial, grab it with the gripper.
if check("the robot's gripper is above the dial and the gripper is open"):
    robot.move_gripper("around the dial")
# Once we have a good grip around the dial, turn it to the right (clockwise)
# until it clicks.
if check("the robot's gripper is around the dial"):
    robot.turn_gripper("clockwise", until="click")