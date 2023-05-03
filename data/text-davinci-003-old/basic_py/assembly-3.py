
    if check("the robot's gripper is not above the wrench and the wrench is not placed in the desired orientation"):
        robot.put("gripper above wrench")
    if check("the robot's gripper is above the wrench and the wrench is not around the peg"):
        robot.align("wrench to peg")
    if check("the wrench is almost around the peg and the robot's gripper is not above the handle"):
        robot.grasp("wrench handle")
    if check("the robot's gripper is above the wrench handle"):
        robot.put("wrench around peg")