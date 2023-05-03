
    if check("the robot's gripper is not above peg"):
        robot.place("gripper above peg")
    if check("the robot's gripper is above peg and the robot's gripper is not around peg"):
        robot.drop("gripper around peg")
    if check("the robot's gripper is near peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is near peg and the robot's gripper is closed"):
        robot.insert("peg into hole on side")