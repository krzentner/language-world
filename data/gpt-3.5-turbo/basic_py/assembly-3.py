if check("the robot's gripper is not near the wrench"):
        robot.move("to wrench")
    if check("the robot's gripper is near the wrench and the robot's gripper is not around the wrench"):
        robot.grab("wrench")
    if check("the robot's gripper is around the wrench and the robot's gripper is not near the peg"):
        robot.move("to peg")
    if check("the robot's gripper is near the peg and the wrench is not wrapped around the peg"):
        robot.wrap("wrench around peg")