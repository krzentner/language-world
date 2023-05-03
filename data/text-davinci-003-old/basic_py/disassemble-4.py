
    if check("the robot's gripper is not forward aligned with wrench and the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    if check("the robot's gripper is forward aligned with the wrench and the wrench is not vertically aligned with the peg"):
        robot.align("wrench to peg")
    if check("the gripper is vertically aligned with the wrench"):
        robot.pull("wrench off peg")