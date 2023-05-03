if check("the robot's gripper is not vertically aligned with the wrench and the wrench is on the peg"):
        robot.move("gripper to right of wrench")
    if check("the robot's gripper is vertically aligned with the wrench and the wrench is on the gripper"):
        robot.pull("wrench off the peg")