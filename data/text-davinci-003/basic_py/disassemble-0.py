
    if check("the robot's gripper is not above the wrench and the robot's gripper is open"):
        robot.put("gripper above wrench")
    if check("the robot's gripper is above the wrench and the robot's gripper is not around the wrench"):
        robot.drop("gripper around wrench")
    if check("the robot's gripper is above the wrench and the robot's gripper is around the wrench"):
        robot.pull("wrench off peg")