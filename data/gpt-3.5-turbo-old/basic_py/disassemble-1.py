if check("the robot's gripper is not vertically aligned with wrench and the robot's gripper is not around wrench"):
        robot.put("gripper above wrench")
    if check("the robot's gripper is vertically aligned with the wrench and the wrench is attached to the peg"):
        robot.pull("wrench off the peg")
    if check("the robot's gripper is holding the wrench and the wrench is not attached to the peg"):
        robot.drop("wrench at the designated location")