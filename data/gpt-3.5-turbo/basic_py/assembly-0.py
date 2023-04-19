if check("the robot's gripper is not vertically aligned with the wrench and the gripper is closed"):
        robot.put("gripper above wrench and open it")
    if check("the robot's gripper is vertically aligned with the wrench and the wrench is not around peg"):
        robot.grab("wrench")
    if check("the robot's gripper is near the peg, and the wrench is around the peg"):
        robot.rotate("wrench around the peg")
    if check("the wrench is securely around the peg"):
        robot.tighten("the peg with the wrench")