

if check("the robot's gripper is not above the hole"):
    robot.place("gripper above hole")
if check("the robot's gripper is not around the peg and the robot's gripper is open"):
    robot.drop("gripper around peg")
if check("the robot's gripper is near the peg and the robot's gripper is open"):
    robot.close("gripper around peg")
if check("the robot's gripper is above peg and the robot's gripper is closed"):
    robot.pull("peg out of hole")
if check("the robot's gripper is around the peg and the robot's gripper is closed"):
    robot.place("peg at goal")