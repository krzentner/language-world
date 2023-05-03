
    if check("the robot's gripper is not vertical aligned with the wrench"):
        robot.put("gripper above wrench")
    if check("the robot's gripper is not close to the wrench and the robot's gripper is open"):
        robot.drop("gripper around wrench")
    if check("the robot's gripper is closed around the wrench and the wrench is not horizontally aligned with the peg"):
        robot.align("wrench to peg")
    if check("the robot's gripper is closed around the wrench and the wrench is horizontally aligned with the peg"):
        robot.pull("wrench off peg")