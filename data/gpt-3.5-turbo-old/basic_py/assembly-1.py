if check("the robot's gripper is not above the wrench"):
        robot.place("gripper above wrench")
    if check("the robot's gripper is not open"):
        robot.drop("gripper is open")
    if check("the robot's gripper is not surrounding the peg and the wrench is not aligned with the peg"):
        robot.adjust("align wrench with peg")
    if check("the wrench is aligned with the peg"):
        robot.grab("peg with wrench")
        robot.rotate("wrench around the peg")