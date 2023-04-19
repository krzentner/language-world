

if check("the robot's gripper is not vertically aligned with the peg"):
    robot.put("gripper above peg")
if check("peg is left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
    robot.grab("peg")
if check("the robot's gripper is forward aligned with the peg"):
    robot.pull("peg out from side")