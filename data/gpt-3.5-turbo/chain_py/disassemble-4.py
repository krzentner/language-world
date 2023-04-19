# Steps:
#  1. Put gripper above wrench
#  2. Grab the wrench with the gripper
#  3. Move the wrench to disengage it from the peg
#  4. Release the wrench
# First, put the gripper above the wrench.
if check("the robot's gripper is not vertically aligned with the wrench"):
    robot.put("gripper above wrench")
# If the gripper isn't around the wrench, put it around the wrench.
if check("the robot's gripper is not around wrench and the robot's gripper is open"):
    robot.drop("gripper around wrench")
# If the gripper is near the wrench and around it, we can try to disengage it
# from the peg by moving the wrench downwards.
if check("the robot's gripper is around wrench and the wrench is not disengaged from the peg"):
    robot.move("wrench downwards to disengage it from the peg")
# If the wrench is disengaged from the peg, we can release it by opening the
# gripper.
if check("the wrench is disengaged from the peg and the robot's gripper is not open"):
    robot.release("wrench")