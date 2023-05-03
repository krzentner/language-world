
    if check("the robots gripper is not horizontally aligned with the wrench"):
        robot.put("gripper above wrench")
    if check("the robot's gripper is forward aligned with the wrench and the wrench is not above the peg"):
        robot.grab("wrench")
    if check("the robot's gripper is forward aligned with the wrench and the wrench is above the peg"):
        robot.put("wrench around peg")
    if check("the robot's gripper is around the peg"):
        robot.turn("wrench to tighten peg")