if check("the wrench is attached to the peg and the robot's gripper is not near the wrench"):
        robot.reach("to the wrench")
    if check("the robot's gripper is near the wrench and the robot's gripper is not around the wrench"):
        robot.grab("the wrench")
    if check("the robot's gripper is around the wrench and the robot's gripper is not near the peg"):
        robot.pull("the wrench off the peg")