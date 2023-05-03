# Steps:
#  1. Put gripper above the peg
#  2. Grab the peg with the gripper
#  3. Line the peg up with the hole
#  4. Slide the peg sideways into the hole
# First, put the gripper above the peg.
if check("the robot's gripper is not vertically aligned with the peg"):
    robot.put("gripper above peg")
# If the gripper is not around the peg, grab it.
if check("the robot's gripper is not around peg and the robot's gripper is open"):
    robot.grab("peg")
# If the gripper is around the peg, but not lined up with the hole, align the
# peg with the hole.
if check("the robot's gripper is around peg and the peg is not lined up with the hole"):
    robot.align("peg to hole")
# Once the peg and the hole are aligned, slide the peg sideways into the hole.
if check("peg is horizontally aligned with hole"):
    robot.insert("peg into hole")