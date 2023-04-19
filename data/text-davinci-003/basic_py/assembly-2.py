
    if check("the robot's gripper is not above the wrench"):
        robot.move("gripper above wrench")
    if check("wrench is not left of the robot's gripper and wrench is not forward aligned with the robot's gripper"):
        robot.grab("wrench")
    if check("the robot's gripper is forward aligned with the wrench and the wrench is not near the peg"):
        robot.move("wrench to peg")
    if check("the wrench is near the peg and the robot's gripper is not around the peg"):
        robot.put("wrench around peg")