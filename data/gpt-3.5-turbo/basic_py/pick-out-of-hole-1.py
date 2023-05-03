if check("the robot's gripper is not above the peg"):
    robot.place("gripper above peg")
if check("the robot's gripper is not around the peg and the robot's gripper is open"):
    robot.drop("gripper around peg")
if check("the robot's gripper is inside the hole and the robot's gripper is closed"):
    robot.lift("the peg out of the hole")
if check("the robot's gripper is above peg and the robot's gripper is closed"):
    robot.place("peg at goal")