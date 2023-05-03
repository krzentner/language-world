
    if check("the robot's gripper is not above the peg and the peg is not forward aligned with the robot's gripper"):
        robot.put("gripper above peg") 
    if check("peg is forward aligned with the robot's gripper and the robot's gripper is not forward aligned with the hole"):
        robot.grab("peg") 
    if check("peg is forward aligned with the hole and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("peg is in robot's gripper and the robot's gripper is closed"):
        robot.place("peg at goal")