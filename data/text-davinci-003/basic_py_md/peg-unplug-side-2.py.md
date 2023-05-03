

If check("the robot's gripper is not vertically aligned with the peg"):
    robot.put("gripper above peg")
if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
    robot.grab("peg")
if check("the robot's gripper is forward aligned with the peg"):
    robot.pull("gripper away from peg")
if check("the robot's gripper is not around the peg"):
    robot.put("gripper around peg")
if check("the robot's gripper is around the peg"):
    robot.pull("peg out of the hole")