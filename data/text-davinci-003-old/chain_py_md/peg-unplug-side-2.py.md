

Steps:
1. Put gripper above the peg
2. Grab the peg with the gripper
3. Pull the peg out of the hole

if check("the robot's gripper is not vertically aligned with the peg"):
    robot.put("gripper above peg")
if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
    robot.grab("peg")
if check("the robot's gripper is forward aligned with the peg"):
    robot.pull("peg out of hole")