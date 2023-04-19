if check("the wrench is attached to the peg and the robot's gripper is not above the wrench"):
        robot.put("gripper above wrench")
    if check("the robot's gripper is above the wrench and the gripper is not closed"):
        robot.close("gripper around wrench")
    if check("the gripper is closed around the wrench and the wrench is not removed from the peg"):
        robot.pull("wrench off peg")