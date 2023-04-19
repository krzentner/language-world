if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is not around the peg and the peg is not in the hole"):
        robot.grab("peg")
    if check("the robot's gripper is around the peg"):
        robot.pull("peg out of hole")
    if check("the robot's gripper is above the goal"):
        robot.drop("peg at goal")