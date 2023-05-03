# Steps:
#  1. Put gripper above the hole
#  2. Slide gripper down into the hole and around the peg
#  3. Lift the peg out of the hole
#  4. Move the peg to the target location
# First, put the gripper above the hole.
if check("the robot's gripper is not above the hole"):
    robot.place("gripper above hole")
# If the gripper is above the hole, maybe we can slide it down and around the
# peg.
if check("the robot's gripper is above the hole and the robot's gripper is not around the peg"):
    robot.place("gripper around the peg")
# If the gripper is around the peg, maybe we can lift the peg out of the hole.
if check("the robot's gripper is around the peg"):
    robot.lift("peg out of hole")
# If we've picked up the peg, let's try moving it to the target location.
if check("the robot's gripper is holding the peg"):
    robot.place("peg at goal")