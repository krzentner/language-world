
    if check("the robot's gripper is not around the wrench and the robot's gripper is not above the wrench"):
        robot.put("gripper above wrench")
    if check("the robot's gripper is above wrench and the robot's gripper is not around wrench"):
        robot.drop("gripper around wrench")
    if check("the robot's gripper is around wrench and the robot's gripper is not near the peg"):
        robot.pull("wrench off peg")