# Steps:
#  1. Put gripper above the peg
#  2. Grab the peg with the gripper
#  3. Line the peg up with the hole
#  4. Slide the peg sideways into the hole
# First, put the gripper above the peg.
if check("the robot's gripper is not vertically aligned with the peg"):
    robot.put("gripper above peg")
# If the gripper is not around the peg, grab the peg with the gripper.
if check("the robot's gripper is not around the peg"):
    robot.grab("peg")
# If the peg isn't lined up with the hole, line it up.
# Because the peg is a long object, we're checking the alignment from the front.
if check("the peg is not horizontally aligned with hole"):
    robot.align("peg to hole")
# If the peg is lined up with the hole to the side, insert it.
if check("peg is horizontally aligned with hole"):
    robot.insert("peg into hole")