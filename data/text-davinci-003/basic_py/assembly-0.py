
    if check("the robot's gripper is not above the wrench and the robot's gripper is open"):
        robot.grab("wrench")
    if check("the robot's gripper is above the wrench and the robot's gripper is open"):
        robot.drop("wrench around peg")
    if check("the robot's gripper is closed around wrench and wrench is not tightened around peg"):
        robot.turn("wrench until tight")