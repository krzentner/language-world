

If check("the robot's gripper is not above the hole"):
    robot.place("gripper above hole")
if check("the robot's gripper is above the hole and the peg is still in the hole"):
    robot.drop("gripper into the hole")
if check("the robot's gripper is around the peg and the robot's gripper is open"):
    robot.close("gripper around peg")
if check("the robot's gripper is near the peg and the robot's gripper is closed"):
    robot.lift("peg out of the hole")
if check("the robot's gripper is near the peg and the peg is out of the hole"):
    robot.place("peg at goal")