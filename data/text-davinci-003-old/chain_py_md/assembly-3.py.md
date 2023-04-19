

Steps:
1. Put gripper above wrench
2. Drop gripper around wrench
3. Put wrench around peg
4. Tighten wrench around peg

if check("the robot's gripper is not above the wrench"):
    robot.put("gripper above wrench")
if check("the robot's gripper is not around the wrench and the robot's gripper is open"):
    robot.drop("gripper around wrench")
if check("the robot's gripper is vertically aligned with the peg and the robot's gripper is closed"):
    robot.put("wrench around peg")
if check("the robot's gripper is forward aligned with the peg and the robot's gripper is closed"):
    robot.tighten("wrench around peg")