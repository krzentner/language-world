# Steps:
#  1. Put gripper above the peg
#  2. Grab the peg with the gripper
#  3. Line the peg up with the hole
#  4. Slide the peg sideways into the hole

# First, put the gripper above the peg.

if check("the robot's gripper is not vertically aligned with the peg"):
    robot.put("gripper above peg")

# If the gripper is above the peg, grab it with the gripper.

if check("the robot's gripper is above peg and the robot's gripper is open"):
    robot.grab("the peg")

# Align the peg with the hole.

if check("the peg is not aligned with the hole"):
    robot.align("peg with the hole")

# Slide the peg into the hole.

if check("the peg is aligned with the hole"):
    robot.slide("the peg into the hole")