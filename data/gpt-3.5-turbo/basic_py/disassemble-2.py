    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    if check("the wrench is attached to the peg and the robot's gripper is around the peg"):
        robot.move("gripper to wrench")
    if check("the robot's gripper is around the wrench and the wrench is not attached to anything else"):
        robot.pull("wrench off peg")