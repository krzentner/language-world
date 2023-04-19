
    if check("the robot's gripper is not above the wrench"):
        robot.grab("wrench")
    if check("the robot's gripper is above the wrench and the wrench is not above the peg"):
        robot.move("wrench above peg")
    if check("the wrench is above the peg and the peg is not left of the wrench"):
        robot.align("wrench to peg")
    if check("the peg is left of the wrench and the robot's gripper is open"):
        robot.put("wrench around peg")