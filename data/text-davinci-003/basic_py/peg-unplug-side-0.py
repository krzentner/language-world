
    if check("the robot's gripper is not vertically aligned with peg"):
        robot.put("gripper above peg")
    if check("peg is not left of robot's gripper"):
        robot.grab("peg")
    if check("peg is forward aligned with robot's gripper and peg is not out of hole"):
        robot.pull("out of hole")