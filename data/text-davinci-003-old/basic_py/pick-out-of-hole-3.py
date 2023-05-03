
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.place("gripper above peg")
    if check("the peg is forward aligned with the robot's gripper and the robot's gripper is open"):
        robot.grab("peg from the hole")
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is above peg and the robot's gripper is closed"):
        robot.place("peg at goal")