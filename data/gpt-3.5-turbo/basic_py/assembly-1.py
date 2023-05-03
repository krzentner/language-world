if check("the robot's gripper is not near the wrench"):
        robot.grab("wrench")
    if check("the robot's gripper is near the wrench and the robot's gripper is not around peg"):
        robot.put("gripper around peg")
    if check("the robot's gripper is around peg"):
        robot.turn("peg with wrench")