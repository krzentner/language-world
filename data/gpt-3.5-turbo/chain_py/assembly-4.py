# Steps:
#  1. Put gripper above the wrench and peg
#  2. Grab the wrench
#  3. Line up the wrench with the peg
#  4. Slide the wrench around the peg
# First, align the gripper above the wrench and peg.
if check("the robot's gripper is not vertically aligned with the wrench and peg"):
    robot.put("gripper above wrench and peg")
# Once the gripper is aligned, grab the wrench with the gripper.
if check("the robot's gripper is aligned with the wrench and the robot's gripper is open"):
    robot.grab("wrench")
# Line up the wrench with the peg.
if check("the wrench is not aligned with the peg"):
    robot.align("wrench to peg")
# Slide the wrench around the peg.
if check("the wrench is aligned with the peg"):
    robot.slide("wrench around peg")