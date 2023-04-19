
    if check("the robot's gripper is not in the same plane as the peg"):
        robot.put("gripper in same plane as peg")
    if check("the robot's gripper is in the same plane as the peg and the robot's gripper is closed"):
        robot.put("gripper around peg")
    if check("the robot's gripper is around the peg"):
        robot.pull("peg out")