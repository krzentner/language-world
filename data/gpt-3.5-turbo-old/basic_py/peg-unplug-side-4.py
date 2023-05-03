if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is in the hole"):
        robot.align("peg to be horizontally aligned with hole")
    if check("the robot's gripper is horizontally aligned with the peg and the peg is in the hole"):
        robot.pull("peg out from the hole")