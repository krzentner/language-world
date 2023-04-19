

If check("the robot's gripper is not above the hole"):
    robot.reach("gripper above hole")
if check("the robot's gripper is not around peg and the robot's gripper is open"):
    robot.drop("gripper around peg")
if check("the robot's gripper is near peg and the robot's gripper is open"):
    robot.close("gripper around peg")
if check("the robot's gripper is above peg and the robot's gripper is closed"):
    robot.pull("peg out of hole")
if check("the robot's gripper is near peg and the peg is above the robot's gripper"):
    robot.place("peg at goal")