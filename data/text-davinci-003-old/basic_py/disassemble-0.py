
    if check("the robot's gripper is not above the wrench"):
        robot.grab("wrench")
    if check("the robot's gripper is under the wrench and the wrench is not near peg"):
        robot.rotate("wrench above peg")
    if check("the robot's gripper is not near peg and wrench is above peg"):
        robot.slide("wrench to peg")
    if check("the robot's gripper is near peg and wrench is above peg"):
        robot.release("wrench from peg")