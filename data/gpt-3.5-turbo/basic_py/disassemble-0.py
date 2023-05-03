if check("the robot's gripper is not near the wrench"):
        robot.reach("to the wrench")
    if check("the robot's gripper is not around the wrench"):
        robot.grab("the wrench")
    if check("the wrench is not detached from the peg"):
        robot.pull("the wrench out of the peg")