

if check("the robot's gripper is not vertically aligned with the peg"):
    robot.put("gripper above peg")
if check("the peg is not left of the robot's gripper"):
    robot.grab("peg")
if check("the peg is left of the robot's gripper"):
    robot.pull("peg away from hole")