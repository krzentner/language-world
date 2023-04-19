# Steps:
#  1. Put the gripper above the wrench
#  2. Grab the wrench with the gripper
#  3. Put the gripper above the peg
#  4. Move the gripper down to place the wrench around the peg
#  5. Release the wrench
# First, put the gripper above the wrench.
if check("the robot's gripper is not above the wrench"):
    robot.place("gripper above wrench")
# If the gripper is above the wrench, we can grab it.
if check("the robot's gripper is above the wrench and the robot's gripper is open"):
    robot.grab("wrench")
# If the wrench is grabbed, we can place the gripper above the peg.
if check("the robot's gripper is holding the wrench and the robot's gripper is not above the peg"):
    robot.put("gripper above peg")
# If the gripper is above the peg, we can move it down to place the wrench around
# the peg.
if check("the robot's gripper is above the peg"):
    robot.move("gripper down to place wrench")
# If the gripper is around the peg, we can release the wrench.
if check("the robot's gripper is around the peg"):
    robot.release("wrench")