if check("the robot's gripper is not above the wrench and the wrench is not vertically aligned with the robot's gripper"):
        robot.put("gripper above wrench")
    if check("the robot's gripper is vertically aligned with the wrench and the wrench is not around the peg"):
        robot.grab("wrench")
    if check("the robot's gripper is around the peg"):
        robot.rotate("wrench around peg")