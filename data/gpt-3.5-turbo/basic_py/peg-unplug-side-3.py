if check("the robot's gripper is not vertically aligned with the peg and the peg is not in contact with the hole"):
        robot.move("gripper above peg")
    if check("peg is in contact with hole and the robot's gripper is not around peg"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is in contact with hole"):
        robot.align("peg to hole")
    if check("peg is fully inserted in hole and the robot's gripper is around peg"):
        robot.pull("peg out from side")