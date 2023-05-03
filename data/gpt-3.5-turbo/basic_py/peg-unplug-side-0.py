if check("the robot's gripper is not vertically aligned with the peg and the gripper is open"):
        robot.put("gripper above peg")
    if check("the peg is not below the gripper and the gripper is open"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not vertically aligned with its hole"):
        robot.align("peg to hole")
    if check("the peg is vertically aligned with its hole and the robot's gripper is around the peg"):
        robot.pull("peg out of hole")