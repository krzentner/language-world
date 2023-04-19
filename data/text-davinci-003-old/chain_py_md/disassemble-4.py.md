

Steps:
1. Put gripper above the wrench 
2. Drop gripper around the wrench
3. Pull the wrench off the peg

if check("the robot's gripper is not above the wrench"):
    robot.put("gripper above wrench")
if check("the robot's gripper is not around the wrench and the robot's gripper is open"):
    robot.drop("gripper around wrench")
if check("the robot's gripper is around the wrench"):
    robot.pull("wrench off peg")