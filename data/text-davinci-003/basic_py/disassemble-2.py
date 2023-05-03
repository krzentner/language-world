
    if check("the robot's gripper is not above wrench and the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    if check("the robot's gripper is vertically aligned with the wrench and the robot's gripper is not around the wrench"):
        robot.grab("wrench")
    if check("the robot's gripper is around the wrench and the wrench is not free of the peg"):
        robot.pull("wrench away from peg")