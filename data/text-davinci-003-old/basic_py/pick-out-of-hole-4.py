
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("the peg is not forward aligned with the robot's gripper and the robot's gripper is open"):
        robot.grab("peg")
    if check("the robot's gripper is near the peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is above the peg and the robot's gripper is closed"):
        robot.place("peg at goal")