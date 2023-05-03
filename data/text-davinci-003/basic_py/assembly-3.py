
    if check("the robot's gripper is not near the wrench"):
        robot.pick("up wrench")
    if check("the robot's gripper is near the wrench and the wrench is not around the peg"):
        robot.wrap("wrench around peg")
    if check("the wrench is around the peg and the wrench is not tight"):
        robot.tighten("wrench around peg")