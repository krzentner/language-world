
    if check("the robot's gripper is not near the wrench handle"):
        robot.move("gripper to right of wrench handle")
    if check("the robot's gripper is in front of the wrench handle"):
        robot.pull("wrench away from peg")