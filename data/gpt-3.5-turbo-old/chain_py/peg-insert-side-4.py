# Steps:
#  1. Put gripper above the peg
#  2. Grab the peg with the gripper
#  3. Line the peg up with the hole
#  4. Slide the peg sideways into the hole

# First, put the gripper above the peg.
if check("the robot's gripper is not vertically aligned with the peg"):
    robot.put("gripper above peg")
    
# If the peg is left of the gripper, move the gripper to the left of the peg.
if check("the peg is left of the robot's gripper"):
    robot.move("gripper to the left of the peg")
    
# If the gripper is not around the peg, grab the peg with the gripper.
if check("the robot's gripper is not around the peg"):
    robot.grab("peg")
    
# If the gripper is almost aligned with the hole, align the peg with the hole.
if check("the peg is not aligned with the hole" and "the gripper is almost aligned with the hole"):
    robot.align("peg to hole")
    
# If the peg is aligned with the hole and the gripper is near the hole, slide the peg into the hole.
if check("the peg is aligned with the hole" and "the gripper is near the hole"):
    robot.slide("peg into the hole")