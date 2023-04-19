
    if check("the robot's gripper is not near the wrench handle"):
        robot.move("gripper near wrench handle")
    if check("the robot's gripper is near the wrench handle and the robot's gripper is not around the wrench handle"):
        robot.grab("wrench handle")
    if check("the robot's gripper is around the wrench handle and the wrench is not off the peg"):
        robot.pull("wrench off peg")