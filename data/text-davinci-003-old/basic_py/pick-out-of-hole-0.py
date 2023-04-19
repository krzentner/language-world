
    if check("the robot's gripper is not near the peg and the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is vertically aligned with the peg and the robot's gripper is not near the peg"):
        robot.grab("peg")
    if check("the robot's gripper is near the peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is above peg and the robot's gripper is closed"):
        robot.place("peg at goal")