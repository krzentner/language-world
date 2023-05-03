if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    if check("the robot's gripper is vertically aligned with the wrench and the wrench is not in the robot's gripper"):
        robot.grab("wrench")
    if check("the wrench is in the robot's gripper"):
        robot.pull("wrench off peg")