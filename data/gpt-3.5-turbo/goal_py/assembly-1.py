# Steps:
#  1. Put gripper above wrench
#  2. Grab the wrench with the gripper
#  3. Line up the wrench with the peg
#  4. Slide the wrench around the peg
# First, put the gripper above the wrench.
if check("the robot's gripper is not vertically aligned with the wrench"):
    robot.move_gripper("vertically aligned with the wrench")
# If the wrench is not grabbed by the gripper, grab it.
if check("the robot's gripper is not around the wrench"):
    robot.move_gripper("around the wrench", close_gripper=True)
# Once the gripper is around the wrench, line up the wrench with the peg.
if check("the wrench is not horizontally aligned with the peg"):
    robot.move_gripper("vertically aligned with the peg")
# If the wrench is lined up with the peg vertically but not slid around it,
# slide it around the peg.
if check("the wrench is not around the peg"):
    robot.move_gripper("around the peg")