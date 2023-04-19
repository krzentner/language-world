# Steps:
#  1. Put gripper above peg
#  2. Grab wrench with gripper
#  3. Line up wrench with peg
#  4. Rotate wrench to put it around the peg
#  5. Move the wrench with the peg to the target location
# First, put the gripper above the peg.
if check("the robot's gripper is not vertically aligned with the peg"):
    robot.put("gripper above peg")
# If the gripper isn't around the wrench, grab it with the gripper.
if check("the robot's gripper is not around wrench and the robot's gripper is open"):
    robot.grab("wrench")
# If the gripper is near the peg and the wrench is not around it, line the wrench
# up with the peg and rotate it to put it around the peg.
if check("the robot's gripper is near peg and the wrench is not around peg"):
    robot.align("wrench to peg")
    robot.rotate("wrench around peg")
# If the wrench is around the peg and the robot's gripper is near the peg, move
# the wrench and peg to the target location.
# Close the gripper to make sure we keep control of the peg and wrench.
if check("wrench is around peg and the robot's gripper is near peg"):
    robot.move("wrench and peg to goal")