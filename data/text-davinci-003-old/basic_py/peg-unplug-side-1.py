
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("the peg is not left of the robot's gripper and the peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with the hole"):
        robot.align("peg to hole")
    if check("the peg is horizontally aligned with the hole"):
        robot.pull("peg away from hole")