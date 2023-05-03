if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is not around peg and the peg is close to the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with peg and the peg is not stuck in the hole"):
        robot.pull("peg out of hole")
    if check("the peg is out of the hole and the robot's gripper is holding it"):
        robot.release("peg")