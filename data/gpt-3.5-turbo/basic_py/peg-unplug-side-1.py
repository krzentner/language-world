if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("the peg is not held by the robot's gripper and the robot's gripper is forward aligned with the peg"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is almost fully out of the hole"):
        robot.pull("peg out of hole")