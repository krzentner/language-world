
    if check("the robot's gripper is not vertically aligned with wrench and the wrench is not left aligned with the robot's gripper"):
        robot.put("gripper above wrench")
    if check("the robot's gripper is forward aligned with the wrench"):
        robot.grab("wrench")
    if check("the robot's gripper is around the wrench and the wrench is still on the peg"):
        robot.pull("wrench off peg")